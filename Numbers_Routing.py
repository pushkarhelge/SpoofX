import random

EMERGENCY = [
    '+919067946303',
    '+919370566952',
    # '+917756885249'
]

HELP = [
    # '+917083022822'
    '+919067946303'
]

INQUIRY = [
    '+919067946303'
    # '+917756885249'
]

e_itr = 0
h_itr = 0
i_itr = 0

def getRandomEmergency():
    global e_itr
    e_itr += 1
    return EMERGENCY[e_itr % len(EMERGENCY)]


def getRandomHelp():
    global h_itr
    h_itr += 1
    return HELP[h_itr % len(HELP)]

def getRandomInquiry():
    global i_itr
    i_itr += 1
    return INQUIRY[i_itr % len(INQUIRY)]