# This programs creates human character stats for RuneQuest 3rd edition
# Done with python 2.7.15
# Matti Eronen

from random import randint
from time import strftime


# main character creation function
def characteristics():

    time_stamp =  strftime("%c") 
    age = 15 + randint(2, 12)
    print time_stamp
    print "Age: ", age
    print "Characteristics:"

# characteristics as constants after dice roll function
    STR = roll_VMA()
    CON  = roll_RR()    
    SIZ = roll_KOK()
    INT = roll_ALY()
    POW = roll_MHT()
    DEX = roll_NPP()
    CHA = roll_ULK()

    print "Total:",  STR + CON + SIZ + INT + POW + DEX + CHA

    agility       = int(float(DEX - 10)) + (int(float(STR - 10) / 2)) - int(float(SIZ - 10))          # primary, secondary, negative
    communication = int(float(INT - 10)) + (int(float(POW - 10) / 2)) + (int(float(CHA - 10) / 2))    # primary, secondary, secondary
    knowledge     = int(float(INT - 10))                                                              # primary
    magic         = int(float(INT - 10)) + int(float(POW - 10)) + (int(float(DEX - 10) / 2))          # primary, secondary, secondary
    manipulation  = int(float(INT - 10)) + int(float(DEX - 10)) + (int(float(STR - 10) / 2))          # primary, secondary, secondary
    perception    = int(float(INT - 10)) + (int(float(POW - 10) / 2)) + (int(float(CON - 10) / 2))    # primary, secondary, secondary
    stealth       = int(float(DEX - 10)) - int(float(SIZ - 10)) - int(float(POW - 10))                # primary, secondary, negative
    hit_points    = int(((float(SIZ) + float(CON)) / 2) + 0.5)
    dmg_bonus     = SIZ + STR
     
    print "Skills & modifiers: "    
    print "Agility: ", agility
    print "Communication: ", communication
    print "Knowledge: ", knowledge
    print "Manipulation: ", manipulation
    print "Perception: ", perception
    print "Stealth: ", stealth
    print "Attributes: "
    print "Hit points: ", hit_points
    print "Magic points: ", POW
    print "Fatigue points: ", STR + CON
    print "A % mod: ", manipulation
    print "P % mod: ", agility

    damage_modifier(dmg_bonus)
    print "Movement: 3"
    print "DEX strike rank: ", DEX_rank(DEX)
    print "SIZ strike rank: ", SIZ_rank(SIZ)

    
    strike_r = strike_rank(DEX_rank(DEX), SIZ_rank(SIZ))
    
    # need return function for txt file printing
    return time_stamp + \
           "\nAge: %2d" % age + "\nCharacteristics:\nSTR: %2d\nCON:  %2d\nSIZ: %2d\nINT: %2d\nPOW: %2d\nDEX: %2d\nCHA: %2d\n" % \
           (STR, CON, SIZ, INT, POW, DEX, CHA) + \
           "Total: %d\n" % (STR + CON + SIZ + INT + POW + DEX + CHA) + \
           "Skills & modifiers:\n" + "Agility: %2d\nCommunication: %2d\nKnowledge: %2d\nManipulation: %2d\nPerception: %2d\n" % \
           (agility, communication, knowledge, manipulation, perception) + \
           "Stealth: %2d\nHit points: %2d\nMagic points: %2d\nFatigue points: %2d\nA - mod: %2d\nP - mod: %2d\n" % \
           (stealth, hit_points, POW, (STR + CON), manipulation, agility) + \
           "Movement: 3\n" + "DEX strike rank: %2d\n" % DEX_rank(DEX) + \
           "SIZ strike rank: %2d\n" % SIZ_rank(SIZ) + \
           "Strike rank: %s\n" % str(strike_r)
           

# individual characteristic rolls
def roll_VMA():
    VMA1 = randint(3, 18)
    print "STR: ", VMA1
    return VMA1


def roll_RR():    
    RR1 = randint(3, 18)
    print "CON: ", RR1
    return RR1                                        


def roll_KOK():
    KOK1 = randint(8, 18)
    print "SIZ: ", KOK1
    return KOK1    
    

def roll_ALY():
    ALY1 = randint(8, 18)
    print "INT: ", ALY1
    return ALY1
    

def roll_MHT():
    MHT1 = randint(3, 18)
    print "POW: ", MHT1
    return MHT1

    
def roll_NPP():
    NPP1 = randint(3, 18)
    print "DEX: ", NPP1
    return NPP1


def roll_ULK():
    ULK1 = randint(3, 18)
    print "CHA: ", ULK1
    return ULK1


# damage modifier 
def damage_modifier(dmg_bonus):
    if dmg_bonus >= 1 and dmg_bonus <= 12:
        return "Damage modifier: -d4"
        print "Damage modifier: -d4"
    elif dmg_bonus >= 13 and dmg_bonus <= 24:
        return "Damage modifier: 0"
        print "Damage modifier: 0"
    elif dmg_bonus >= 25 and dmg_bonus <= 32:
        return "Damage modifier: +d4"
        print "Damage modifier: +d4"
    elif dmg_bonus >= 33 and dmg_bonus <= 40:
        return "Damage modifier: +d6"
        print "Damage modifier: +d6"
    elif dmg_bonus >=41 and dmg_bonus <= 56:
        return "Damage modifier: +2d6"
        print "Damage modifier: +2d6"
    else:
        return "Additional 1d6 damage for each additional increment of 16, or fraction thereof"
        print "Additional 1d6 damage for each additional increment of 16, or fraction thereof"

#DEX strike rank
def DEX_rank(DEX):
    if DEX >= 1 and DEX <= 9:
        NPP_IN = 4
    elif DEX >= 10 and DEX <= 15:
        NPP_IN = 3
    elif DEX >= 16 and DEX <= 19:
        NPP_IN = 2
    else:
        NPP_IN = 1
    return NPP_IN

#SIZ strike rank
def SIZ_rank(SIZ):
    if SIZ >= 1 and SIZ <= 9:
        KOK_IN = 3
    elif SIZ >= 10 and SIZ <= 15:
        KOK_IN = 2
    elif SIZ >= 16 and SIZ <= 19:
        KOK_IN = 1
    else:
        KOK_IN = o
    return KOK_IN

#strike rank calculation
def strike_rank(a, b):
    print "Strike rank is: ", a + b
    return a + b

print "*****************************************************************"
print "This program creates a human character for RuneQuest 3rd edition"
print "*****************************************************************"

choice = (raw_input("Create a new character? Y/N: ")).lower()
output_file = open("Character.txt", "w")
if choice == "n":
    print "Closing program..."
if choice != "n" and choice != "y":
    print "Invalid selection, please answer y = yes or n = no"
    choice = (raw_input("Create another character? Y/N: ")).lower()
while choice == "y":
    character = characteristics()
    output_file.write(str(character))
    choice = (raw_input("Create another character? Y/N: ")).lower()
    if choice == "n":
        print "Closing program..."
    elif choice != "n" and choice != "y":
        print "Invalid selection, please answer y = yes or n = no"
        choice = (raw_input("Create another character? Y/N: ")).lower()

output_file.close()

