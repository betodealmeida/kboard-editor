#spencer jackson

hi = [0x04, 0xf0, 0x7e, 0x7f, 0x07, 0x06, 0x01, 0xf7]
default = [
0xf0, 0x00, 0x01, #3
0x5f, 0x7a, 0x1a, 0x00, 0x01, 0x00, 0x02, 0x22, 0x20, 0x2e, 0x46, 0x00, #15
0x10, 0x21, 0x01, 0x56, 0x00, 0x7f, 0x7f, 0x7f, 0x75, 0x7f, 0x64, 0x01, #27
0x0f, 0x32, 0x00, 0x00, 0x01, 0x00, 0x7f, 0x00, 0x01, 0x01, 0x01, 0x01, #39
0x00, 0x01, 0x01, 0x01, 0x00, 0x01, 0x00, 0x0a, 0x00, #48
0x00, 0x00, 0x01, #51
0x00, 0x00, 0x64, 0x7f, 0x00, 0x00, 0x00, 0x00, 0x05, 0x7f, 0x00, 0x00, #63
0x10, 0x64, 0x7f, 0x00, 0x00, 0x00, 0x06, 0x02, 0x00, 0x00, 0x00, 0x64, #75
0x7f, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x64, 0x7f, 0x00, 0x00, #87
0x00, 0x00, 0x00, 0x00, 0x00, 0x64, 0x45, 0x3a, 0x00, #96
0x00, 0x00, 0x06,  #99
0x00, 0x00, 0x64, 0x7f, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x64, #111
0x00, 0x7f, 0x00, 0x00, 0x00, 0x02, 0x00, 0x01, 0x00, 0x30, 0x3c, 0x3d, #123
0x00, 0x7f, 0x00, 0x3f, 0x00, 0x18, 0x7f, 0x00, 0x00, 0x00, 0x01, 0x31, #135
0x00, 0x3e, 0x3f, 0x00, 0x7f, 0x00, 0x3f, 0x19, 0x00, #144
0x7f, 0x00, 0x00,  #147
0x00, 0x01, 0x32, 0x40, 0x00, 0x41, 0x00, 0x7f, 0x00, 0x3f, 0x1a, 0x7f, #159
0x00, 0x00, 0x00, 0x00, 0x01, 0x33, 0x42, 0x43, 0x00, 0x00, 0x7f, 0x00, #171
0x3f, 0x1b, 0x7f, 0x00, 0x00, 0x00, 0x00, 0x01, 0x34, 0x44, 0x45, 0x00, #183
0x00, 0x7f, 0x00, 0x3f, 0x1c, 0x7f, 0x00, 0x00, 0x00, #
0x00, 0x01, 0x35,  #195
0x46, 0x47, 0x00, 0x7f, 0x00, 0x00, 0x3f, 0x1d, 0x7f, 0x00, 0x00, 0x00, #207
0x00, 0x01, 0x36, 0x48, 0x49, 0x00, 0x7f, 0x00, 0x00, 0x3f, 0x1e, 0x7f, #219
0x00, 0x00, 0x00, 0x01, 0x00, 0x37, 0x4a, 0x4b, 0x00, 0x7f, 0x00, 0x3f, #231
0x00, 0x1f, 0x7f, 0x00, 0x00, 0x00, 0x01, 0x38, 0x00, #
0x4c, 0x4d, 0x00,  #243
0x7f, 0x00, 0x3f, 0x20, 0x00, 0x7f, 0x00, 0x00, 0x00, 0x01, 0x39, 0x4e, #255
0x00, 0x4f, 0x00, 0x7f, 0x00, 0x3f, 0x21, 0x7f, 0x00, 0x00, 0x00, 0x00, #267
0x01, 0x3a, 0x50, 0x51, 0x00, 0x00, 0x7f, 0x00, 0x3f, 0x22, 0x7f, 0x00, #279
0x00, 0x00, 0x00, 0x01, 0x3b, 0x52, 0x53, 0x00, 0x00, #
0x7f, 0x00, 0x3f,  #291
0x23, 0x7f, 0x00, 0x00, 0x00, 0x00, 0x01, 0x3c, 0x54, 0x55, 0x00, 0x7f, #303
0x00, 0x00, 0x3f, 0x24, 0x7f, 0x00, 0x00, 0x00, 0x00, 0x01, 0x3d, 0x56, #315
0x57, 0x00, 0x7f, 0x00, 0x00, 0x3f, 0x25, 0x7f, 0x00, 0x00, 0x00, 0x01, #327
0x00, 0x3e, 0x58, 0x59, 0x00, 0x7f, 0x00, 0x3f, 0x00, #
0x26, 0x7f, 0x00,  #339
0x00, 0x00, 0x01, 0x3f, 0x00, 0x5a, 0x5b, 0x00, 0x7f, 0x00, 0x3f, 0x27, #351
0x00, 0x7f, 0x00, 0x00, 0x00, 0x01, 0x40, 0x5c, 0x00, 0x5d, 0x00, 0x7f, #363
0x00, 0x3f, 0x28, 0x7f, 0x00, 0x00, 0x00, 0x00, 0x01, 0x41, 0x5e, 0x5f, #375
0x00, 0x00, 0x7f, 0x00, 0x3f, 0x29, 0x7f, 0x00, 0x00, #
0x00, 0x00, 0x01,  #387
0x42, 0x60, 0x61, 0x00, 0x00, 0x7f, 0x00, 0x3f, 0x2a, 0x7f, 0x00, 0x00, #399
0x00, 0x00, 0x01, 0x43, 0x62, 0x63, 0x00, 0x7f, 0x00, 0x00, 0x3f, 0x2b, #411
0x7f, 0x00, 0x00, 0x00, 0x00, 0x01, 0x44, 0x64, 0x65, 0x00, 0x7f, 0x00, #423
0x00, 0x3f, 0x2c, 0x7f, 0x00, 0x00, 0x00, 0x01, 0x00, #
0x45, 0x66, 0x67,  #435
0x00, 0x7f, 0x00, 0x3f, 0x00, 0x2d, 0x7f, 0x00, 0x00, 0x00, 0x01, 0x46, #447
0x00, 0x68, 0x69, 0x00, 0x7f, 0x00, 0x3f, 0x2e, 0x00, 0x7f, 0x00, 0x00, #459
0x00, 0x01, 0x47, 0x6a, 0x00, 0x6b, 0x00, 0x7f, 0x00, 0x3f, 0x2f, 0x7f, #471
0x00, 0x00, 0x00, 0x00, 0x01, 0x48, 0x6c, 0x6d, 0x00, #
0x00, 0x7f, 0x00,  #483
0x3f, 0x30, 0x7f, 0x00, 0x00, 0x00, 0x00, 0x01, 0x7f, 0x6e, 0x6f, 0x00, #495
0x00, 0x7f, 0x00, 0x3f, 0x01, 0x00, 0x00, 0x64, 0x00, 0x7f, 0x00, 0x00, #507
0x05, 0x70, 0x01, 0x00, 0x00, 0x00, 0x64, 0x7f, 0x00, 0x00, 0x05, 0x71, #519
0x00, 0x01, 0x00, 0x00, 0x64, 0x7f, 0x00, 0x00, 0x00, #
0x06, 0x00, 0x01,  #531
0x00, 0x00, 0x64, 0x7f, 0x02, 0x00, 0x00, 0x06, 0x01, 0x01, 0x00, 0x00, #543
0x00, 0x64, 0x7f, 0x00, 0x00, 0x06, 0x03, 0x06, 0x20, 0x01, 0x00, 0x00, #555
0x00, 0x03, 0x00, 0x00, 0x00, 0xf7 #561
]

#            0  1  2  3  4  5  6  7  8  9  10 11 12
semitones = [64, 58, 53, 48, 43, 37, 32, 27, 23, 16, 11, 6, 0]

def setChannel(sx,val):
    sx[32] = min(max(val,0),15)
    recalcChecksum(sx)
def getChannel(sx):
    return sx[32]

def setPressureCC(sx,val):
    sx[50] = min(max(val,0),0x7f)
    recalcChecksum(sx)
def getPressureCC(sx):
    return sx[50]

def setPressureChanPressureMode(sx,val):
    if(val):
        sx[55] = 0x04
    else:
        sx[55] = 0
    # this doesn't touch checksum
def getPressureChanPressureMode(sx):
    return sx[55]

def setTiltCC(sx,val):
    sx[60] = min(max(val,0),0x7f)
    recalcChecksum(sx)
def getTiltCC(sx):
    return sx[60]

def setTiltBendMode(sx,val):
    if(val):
        sx[63] = 0x10
    else:
        sx[63] = 0
    # this doesn't touch checksum
def getTiltBendMode(sx):
    return sx[63]

def setPadBendMax(sx,val): 
    val = min(max(val,0),12)
    v = 0x7f-semitones[val]
    sx[35] = min(max(v,0),0x7f)
    recalcChecksum(sx)
def setPadBendMin(sx,val):
    val = min(max(val,0),12)
    v = semitones[val]
    sx[36] = min(max(v,0),0x7f)
    recalcChecksum(sx)

def setTiltBendMax(sx,val): 
    val = min(max(val,0),12)
    v = 0x7f-semitones[val]
    sx[93] = min(max(v,0),0x7f)
    recalcChecksum(sx)
def setTiltBendMin(sx,val):
    val = min(max(val,0),12)
    v = semitones[val]
    sx[94] = min(max(v,0),0x7f)
    recalcChecksum(sx)
def getTiltBendMax(sx): 
    return semitones.index(sx[93])
def getTiltBendMin(sx): 
    return semitones.index(sx[94])

#accepts (0,255)
def setVelocitySensitivity(sx,val):
    if(val > 0x7f):
        sx[111] = 0x40
        val -= 0x7f
    else:
        sx[111] = 0x00
    sx[110] = min(max(val,0),0x7f)
    recalcChecksum(sx)
def getVelocitySensitivity(sx):
    return 127*sx[111]/0x40 + sx[110]

def setPressureSensitivity(sx,val):
    sx[53] = min(max(val,0),0x7f)
    recalcChecksum(sx)

def setTiltSensitivity(sx,val):
    sx[28] = min(max(0x7f-val,0),0x7f)
    recalcChecksum(sx)

def setVelocityCurve(sx,val):
    sx[108] = min(max(val,0),0x7f)
    recalcChecksum(sx)

def setPressureDisabledReturnValue(sx,val):
    sx[20] = min(max(val,0),0x7f)
    recalcChecksum(sx)
def setPressureDisabledReturn(sx,val):
    if val:
        sx[23] |= 0x10
    else:
        sx[23] &= 0xef 
    recalcChecksum(sx)

def setTiltDisabledReturnValue(sx,val):
    sx[21] = min(max(val,0),0x7f)
    recalcChecksum(sx)
def setTiltDisabledReturn(sx,val):
    if val:
        sx[23] |= 0x20
    else:
        sx[23] &= 0xdf 
    recalcChecksum(sx)

def setOnThreshold(sx,val):
    sx[15] = min(max(val,0),0x7f)
    recalcChecksum(sx)

def recalcChecksum(sx):
    #sx[556] = sx[32] + sx[50] + sx[60]  + sx[35] + sx[36] + sx[93] + sx[94] + sx[110] + sx[111] + sx[53] + sx[28] + sx[108] + sx[20] + sx[21] + sx[15] + sx[23]
    sx[556] = sx[32] + sx[50] + sx[60]  + sx[110] + sx[111] + sx[53] + sx[28] + sx[108] + sx[20] + sx[21] + sx[15] + sx[23]
    sx[556] %= 0x7f
    return sx[556]

