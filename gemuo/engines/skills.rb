#
#  GemUO
#  $Id$
#
#  (c) 2005 Max Kellermann <max@duempel.org>
#
#   This program is free software; you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation; version 2 of the License.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program; if not, write to the Free Software
#   Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.
#

require 'gemuo/rules'

module GemUO::Engines
    class EasySkills < GemUO::TimerEvent
        def initialize(client, skills)
            @client = client
            @skills = skills

            @target_number = 0
        end

        def start
            @client.signal_connect(self)

            # get skills
            @client << GemUO::Packet::MobileQuery.new(0x05, @client.world.player.serial)

            tick
        end
        def stop
            @client.signal_disconnect(self)
        end

        def check_skills
            sum = 0
            down = 0
            @client.world.skills.each_value do
                |skill|
                sum += skill.base
                down += skill.base if skill.lock == GemUO::SKILL_LOCK_DOWN
            end

            line = "Skills:"
            @skills.sort.each do
                |id|
                skill = @client.world.skill(id)
                unless skill
                    puts "No value for skill #{id}\n"
                    stop
                    @client.signal_fire(:on_engine_failed, self)
                    return
                end

                line << "  #{skill.name}=#{skill.base}"
                if skill.base == skill.cap
                    puts "Done with skill #{skill.name}\n"
                    @skills.delete(id)
                elsif skill.lock != GemUO::SKILL_LOCK_UP
                    puts "Skill #{skill.name} is locked\n"
                    stop
                    @client.signal_fire(:on_engine_failed, self)
                    return
                end
            end
            line << "  (sum=#{sum}, down=#{down})\n"
            puts line

            if @skills.empty?
                stop
                @client.signal_fire(:on_engine_complete, self)
                return
            end

            if sum >= 7000 && down == 0
                puts "No skills down\n"
                stop
                @client.signal_fire(:on_engine_failed, self)
                return
            end
        end

        def find_instrument
            backpack = @client.world.backpack
            return unless backpack
            @client.world.each_item_in(backpack) do
                |item|
                return item if item.item_id == 0xeb2 # leap harp
            end
            nil
        end

        def tick
            # roll skills
            @current = @skills.shift
            @skills << @current

            # use skill
            puts "skill #{GemUO::SKILL_NAMES[@current]}\n"

            case @current
            when GemUO::SKILL_MUSICIANSHIP
                instrument = find_instrument
                if instrument
                    @client << GemUO::Packet::Use.new(instrument.serial)
                else
                    puts "No instrument!\n"
                end

            else
                @target_number = 0
                @client << GemUO::Packet::TextCommand.new(0x24, @current.to_s)
            end

            restart(GemUO::Rules.skill_delay(@current))
            @client.timer << self
        end

        def on_skill_update
            check_skills

            # get backpack
            if @client.world.backpack
                @client << GemUO::Packet::Use.new(@client.world.backpack.serial)
            else
                puts "no backpack\n"
                # open paperdoll
                @client << GemUO::Packet::Use.new(GemUO::SERIAL_PLAYER | @client.world.player.serial)
            end
        end

        def find_dagger
            backpack = @client.world.backpack
            return unless backpack
            @client.world.each_item_in(backpack) do
                |item|
                return item if item.item_id == 0xf52
            end
            nil
        end

        def distance2(position)
            player = @client.world.player.position
            dx = player.x - position.x
            dy = player.y - position.y
            return dx*dx + dy*dy
        end

        def find_mobile
            mobiles = []
            @client.world.each_mobile do
                |mobile|
                mobiles << mobile unless mobile == @client.world.player || mobile.position == nil
            end
            return if mobiles.empty?
            mobiles.sort! do
                |a,b|
                distance2(a.position) <=> distance2(b.position)
            end
            mobiles[0]
        end

        def find_animal
            mobiles = []
            @client.world.each_mobile do
                |mobile|
                mobiles << mobile if mobile.notoriety == 3 && mobile.body == 0x1d
            end
            return if mobiles.empty?
            mobiles.sort! do
                |a,b|
                distance2(a.position) <=> distance2(b.position)
            end
            mobiles[0]
        end

        def on_target(allow_ground, target_id, flags)
            target = nil
            case @current
            when GemUO::SKILL_DETECT_HIDDEN
                # point to floor
                p = @client.world.player.position
                @client << GemUO::Packet::TargetResponse.new(1, target_id, flags, 0,
                                                          p.x, p.y, p.z, 0)
                return

            when GemUO::SKILL_ANATOMY, GemUO::SKILL_EVAL_INT, GemUO::SKILL_PEACEMAKING
                target = find_mobile

            when GemUO::SKILL_PROVOCATION
                if @target_number == 1
                    target = @client.world.player
                else
                    target = find_animal
                end

            else
                target = find_dagger
            end

            unless target
                puts "Error: no target found for #{@current}\n"
                return
            end

            @client << GemUO::Packet::TargetResponse.new(0, target_id, flags, target.serial,
                                                         0xffff, 0xffff, 0xffff, 0)
            @target_number += 1
        end
    end
end
