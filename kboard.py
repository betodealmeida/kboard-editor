#spencer jackson

from pygame import midi
import rlcompleter
import readline
readline.parse_and_bind("tab: complete")

#it would be nice if these were constants
midi.init()
midi_out = midi.Output(midi.get_default_output_id())
hi = [0xf0, 0x7e, 0x7f, 0x07, 0x06, 0x01, 0xf7]
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
work = list(default)

#            0  1  2  3  4  5  6  7  8  9  10 11 12
semitones = [64, 58, 53, 48, 43, 37, 32, 27, 23, 16, 11, 6, 0]


def setChannel(val):
    work[32] = min(max(val,0),15)
    recalcChecksum()
    show();
def getChannel():
    return work[32]

def setPressureCC(val):
    work[50] = min(max(val,0),0x7f)
    recalcChecksum()
    show();
def getPressureCC():
    return work[50]

def setPressureChanPressureMode(val):
    if(val):
        work[55] = 0x04
    else:
        work[55] = 0
    # this doesn't touch checksum
    show()
def getPressureChanPressureMode():
    return work[55]

def setTiltCC(val):
    work[60] = min(max(val,0),0x7f)
    recalcChecksum()
    show();
def getTiltCC():
    return work[60]

def setTiltBendMode(val):
    if(val):
        work[63] = 0x10
    else:
        work[63] = 0
    # this doesn't touch checksum
    show()
def getTiltBendMode():
    return work[63]

def setPadBendMax(val): 
    val = min(max(val,0),12)
    v = 0x7f-semitones[val]
    work[33] = min(max(v,0),0x7f)
    recalcChecksum(work)
    show();
def setPadBendMin(val):
    val = min(max(val,0),12)
    v = semitones[val]
    work[34] = min(max(v,0),0x7f)
    recalcChecksum()
    show();
def getPadBendMax():
    return semitones.index(0x7f-work[33])
def getPadBendMin():
    return semitones.index(work[34])

def setTiltBendMax(val): 
    val = min(max(val,0),12)
    v = 0x7f-semitones[val]
    work[93] = min(max(v,0),0x7f)
    recalcChecksum()
    show();
def setTiltBendMin(val):
    val = min(max(val,0),12)
    v = semitones[val]
    work[94] = min(max(v,0),0x7f)
    recalcChecksum()
    show();
def getTiltBendMax(): 
    return semitones.index(0x7f-work[93])
def getTiltBendMin(): 
    return semitones.index(work[94])

#accepts (0,255)
def setVelocitySensitivity(val):
    if(val > 0x7f):
        work[111] = 0x40
        val -= 0x7f
    else:
        work[111] = 0x00
    work[110] = min(max(val,0),0x7f)
    recalcChecksum()
    show();
def getVelocitySensitivity():
    return int(128*work[111]/0x40) + work[110]

def setPressureSensitivity(val):
    work[53] = min(max(val,0),0x7f)
    recalcChecksum()
    show();
def getPressureSensitivity():
    return work[53]

def setTiltSensitivity(val):
    work[28] = min(max(0x7f-val,0),0x7f)
    recalcChecksum()
    show();
def getTiltSensitivity():
    return work[28]

def setVelocityCurve(val):
    work[108] = min(max(val,0),0x7f)
    recalcChecksum()
    show();
def getVelocityCurve():
    return work[108]

def setPressureDisabledReturnValue(val):
    work[20] = min(max(val,0),0x7f)
    recalcChecksum()
    show();
def setPressureDisabledReturn(val):
    if val:
        work[23] |= 0x10
    else:
        work[23] &= 0xef 
    recalcChecksum()
    show();
def getPressureDisabledReturnValue():
    return work[20]
def getPressureDisabledReturn():
    return work[23]

def setTiltDisabledReturnValue(val):
    work[21] = min(max(val,0),0x7f)
    recalcChecksum()
    show();
def setTiltDisabledReturn(val):
    if val:
        work[23] |= 0x20
    else:
        work[23] &= 0xdf 
    recalcChecksum()
    show();
def getTiltDisabledReturnValue():
    return work[21]
def getTiltDisabledReturn():
    return work[23]

def setOnThreshold(val):
    work[15] = min(max(val,0),0x7f)
    recalcChecksum()
    show();
def getOnThreshold():
    return work[15]

def recalcChecksum():
    work[556] = work[32] + work[50] + work[60]  + work[110] + work[111] + work[53] + work[28] + work[108] + work[20] + work[21] + work[15] + work[23]
    work[556] %= 0x7f
    return work[556] 

def save(filename):
    f = open(filename,'bw')
    pickle.dump(work,f)

def load(filename):
    f = open(filename,'br')
    work = pickle.load(f) 

def show():
    print("")
    print("Current KBoard Configuration:")
    print("")
    print(" Channel:                       " + str(getChannel()))
    print(" Pressure CC:                   " + str(getPressureCC()))
    a = "No"
    if getPressureChanPressureMode():
        a = "Yes"
    print(" Pressure sends Chan. Pressure: " + a)
    print(" Tilt CC:                       " + str(getTiltCC()))
    a = "No"
    if getTiltBendMode():
        a = "Yes"
    print(" Tilt sends Bend:               " + a)
    print(" Pad Bend Max:                 +" + str(getPadBendMax()) + " semitone")
    print(" Pad Bend Min:                 -" + str(getPadBendMin()) + " semitone")
    print(" Tilt Bend Max:                +" + str(getTiltBendMax()) + " semitone")
    print(" Tilt Bend Min:                -" + str(getTiltBendMin()) + " semitone")
    print(" Velocity Sensitivity:          " + str(getVelocitySensitivity()))
    print(" Pressure Sensitivity:          " + str(getPressureSensitivity()))
    print(" Tilt Sensitivity:              " + str(getTiltSensitivity()))
    print("")
    print(" Velocity Curve:                " + str(getTiltSensitivity()))
    print(" Return a Value...")
    a = "No"
    if getPressureDisabledReturn():
        a = "Yes"
    print("   when Pressure Disabled:      " + a)
    print("    Disabled Pressure Value:    " + str(getPressureDisabledReturnValue()))
    a = "No"
    if getTiltDisabledReturn():
        a = "Yes"
    print("   when Tilt Disabled:          " + a)
    print("    Disabled Tilt Value:        " + str(getTiltDisabledReturnValue()))
    print(" Note-On Threshold:             " + str(getOnThreshold()))
    print("")

def reset():
    work = list(default)


#send the current sysex to the kboard
def send():
    #this isn't going to work, expects a string not a list
    show()
    midi_out.write_sys_ex(0,work)
    
#initialize
midi_out.write_sys_ex(0,hi)
show()
