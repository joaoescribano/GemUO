#
#  GemUO
#
#  (c) 2005-2010 Max Kellermann <max@duempel.org>
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

huffman_tree = [
    1, 2, # 0
    3, 4, # 1
    5, 0, # 2
    6, 7, # 3
    8, 9, # 4
    10, 11, # 5
    12, 13, # 6
    -256, 14, # 7
    15, 16, # 8
    17, 18, # 9
    19, 20, # 10
    21, 22, # 11
    -1, 23, # 12
    24, 25, # 13
    26, 27, # 14
    28, 29, # 15
    30, 31, # 16
    32, 33, # 17
    34, 35, # 18
    36, 37, # 19
    38, 39, # 20
    40, -64, # 21
    41, 42, # 22
    43, 44, # 23
    -6, 45, # 24
    46, 47, # 25
    48, 49, # 26
    50, 51, # 27
    -119, 52, # 28
    -32, 53, # 29
    54, -14, # 30
    55, -5, # 31
    56, 57, # 32
    58, 59, # 33
    60, -2, # 34
    61, 62, # 35
    63, 64, # 36
    65, 66, # 37
    67, 68, # 38
    69, 70, # 39
    71, 72, # 40
    -51, 73, # 41
    74, 75, # 42
    76, 77, # 43
    -101, -111, # 44
    -4, -97, # 45
    78, 79, # 46
    -110, 80, # 47
    81, -116, # 48
    82, 83, # 49
    84, -255, # 50
    85, 86, # 51
    87, 88, # 52
    89, 90, # 53
    -15, -10, # 54
    91, 92, # 55
    -21, 93, # 56
    -117, 94, # 57
    95, 96, # 58
    97, 98, # 59
    99, 100, # 60
    -114, 101, # 61
    -105, 102, # 62
    -26, 103, # 63
    104, 105, # 64
    106, 107, # 65
    108, 109, # 66
    110, 111, # 67
    112, -3, # 68
    113, -7, # 69
    114, -131, # 70
    115, -144, # 71
    116, 117, # 72
    -20, 118, # 73
    119, 120, # 74
    121, 122, # 75
    123, 124, # 76
    125, 126, # 77
    127, 128, # 78
    129, -100, # 79
    130, -8, # 80
    131, 132, # 81
    133, 134, # 82
    -120, 135, # 83
    136, -31, # 84
    137, 138, # 85
    -109, -234, # 86
    139, 140, # 87
    141, 142, # 88
    143, 144, # 89
    -112, 145, # 90
    -19, 146, # 91
    147, 148, # 92
    149, -66, # 93
    150, -145, # 94
    -13, -65, # 95
    151, 152, # 96
    153, 154, # 97
    -30, 155, # 98
    156, 157, # 99
    -99, 158, # 100
    159, 160, # 101
    161, 162, # 102
    -23, 163, # 103
    -29, 164, # 104
    -11, 165, # 105
    166, -115, # 106
    167, 168, # 107
    169, 170, # 108
    -16, 171, # 109
    -34, 172, # 110
    173, -132, # 111
    174, -108, # 112
    175, -22, # 113
    176, -9, # 114
    177, -84, # 115
    -17, -37, # 116
    -28, 178, # 117
    179, 180, # 118
    181, 182, # 119
    183, 184, # 120
    185, 186, # 121
    187, -104, # 122
    188, -78, # 123
    189, -61, # 124
    -79, -178, # 125
    -59, -134, # 126
    190, -25, # 127
    -83, -18, # 128
    191, -57, # 129
    -67, 192, # 130
    -98, 193, # 131
    -12, -68, # 132
    194, 195, # 133
    -55, -128, # 134
    -24, -50, # 135
    -70, 196, # 136
    -94, -33, # 137
    197, -129, # 138
    -74, 198, # 139
    -82, 199, # 140
    -56, -87, # 141
    -44, 200, # 142
    -248, 201, # 143
    -163, -81, # 144
    -52, -123, # 145
    202, -113, # 146
    -48, -41, # 147
    -122, -40, # 148
    203, -90, # 149
    -54, 204, # 150
    -86, -192, # 151
    205, 206, # 152
    207, -130, # 153
    -53, 208, # 154
    -133, -45, # 155
    209, 210, # 156
    211, -91, # 157
    212, 213, # 158
    -106, -88, # 159
    214, 215, # 160
    216, 217, # 161
    218, -49, # 162
    219, 220, # 163
    221, 222, # 164
    223, 224, # 165
    225, 226, # 166
    227, -102, # 167
    -160, 228, # 168
    -46, 229, # 169
    -127, 230, # 170
    -103, 231, # 171
    232, 233, # 172
    -60, 234, # 173
    235, -76, # 174
    236, -121, # 175
    237, -73, # 176
    -149, 238, # 177
    239, -107, # 178
    -35, 240, # 179
    -71, -27, # 180
    -69, 241, # 181
    -89, -77, # 182
    -62, -118, # 183
    -75, -85, # 184
    -72, -58, # 185
    -63, -80, # 186
    242, -42, # 187
    -150, -157, # 188
    -139, -236, # 189
    -126, -243, # 190
    -142, -214, # 191
    -138, -206, # 192
    -240, -146, # 193
    -204, -147, # 194
    -152, -201, # 195
    -227, -207, # 196
    -154, -209, # 197
    -153, -254, # 198
    -176, -156, # 199
    -165, -210, # 200
    -172, -185, # 201
    -195, -170, # 202
    -232, -211, # 203
    -219, -239, # 204
    -200, -177, # 205
    -175, -212, # 206
    -244, -143, # 207
    -246, -171, # 208
    -203, -221, # 209
    -202, -181, # 210
    -173, -250, # 211
    -184, -164, # 212
    -193, -218, # 213
    -199, -220, # 214
    -190, -249, # 215
    -230, -217, # 216
    -169, -216, # 217
    -191, -197, # 218
    -47, 243, # 219
    244, 245, # 220
    246, 247, # 221
    -148, -159, # 222
    248, 249, # 223
    -92, -93, # 224
    -96, -225, # 225
    -151, -95, # 226
    250, 251, # 227
    -241, 252, # 228
    -161, -36, # 229
    253, 254, # 230
    -135, -39, # 231
    -187, -124, # 232
    255, -251, # 233
    -162, -238, # 234
    -242, -38, # 235
    -43, -125, # 236
    -215, -253, # 237
    -140, -208, # 238
    -137, -235, # 239
    -158, -237, # 240
    -136, -205, # 241
    -155, -141, # 242
    -228, -229, # 243
    -213, -168, # 244
    -224, -194, # 245
    -196, -226, # 246
    -183, -233, # 247
    -231, -167, # 248
    -174, -189, # 249
    -252, -166, # 250
    -198, -222, # 251
    -188, -179, # 252
    -223, -182, # 253
    -180, -186, # 254
    -245, -247, # 255
]

class Decompress:
    def __init__(self):
        self._bit = 8
        self._treepos = 0
        self._mask = 0
        self._value = 0

    def decompress(self, src):
        dest = ''

        while True:
            if self._bit >= 8:
                if len(src) == 0:
                    return dest

                self._value = ord(src[0])
                src = src[1:]

                self._bit = 0
                self._mask = 0x80

            if (self._value & self._mask) != 0:
                self._treepos = huffman_tree[self._treepos * 2]
            else:
                self._treepos = huffman_tree[self._treepos * 2 + 1]

            self._mask >>= 1
            self._bit += 1

            if self._treepos <= 0:
                # leaf
                if self._treepos == -256:
                    # special flush character
                    self._bit = 8 # flush rest of byte
                    self._treepos = 0 # start on tree top again
                    continue

                dest += chr(-self._treepos)
                self._treepos = 0