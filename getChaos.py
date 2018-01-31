import random

TURN_222 = ("U", "R", "F", "U'", "R'", "F", "U2", "R2", "F2")
TURN_555 = ("U" , "U2" , "Uw" , "Uw2" ,
                    "U'" , "U2'" , "Uw'" , 
                    "R" , "R2" , "Rw" , "Rw2" ,
                    "R'" , "R2'" , "Rw'" , 
                    "F" , "F2" , "Fw" , "Fw2" ,
                    "F'" , "F2'" , "Fw'" , 
                    "B" , "B2" , "Bw" , "Bw2" ,
                    "B'" , "B2'" , "Bw'" , 
                    "L" , "L2" , "Lw" , "Lw2" ,
                    "L'" , "L2'" , "Lw'" , 
                    "D" , "D2" , "Dw" , "Dw2" ,
                    "D'" , "D2'" , "Dw'" , 
                    )

def getPsbScb_222():
    pre_turn = ''
    turn = ''
    scb = ''
    LENGTH = 9
    count =0 
    while count < LENGTH:
        turn = random.choice(TURN_222)
        if turn.find("U") == 0 and pre_turn.find("U") == 0:
            continue
        elif turn.find("R") == 0 and pre_turn.find("R") == 0:
            continue
        elif turn.find("F") == 0 and pre_turn.find("F")  == 0:
            continue
        else :
            scb += turn +' '
            pre_turn =turn
            count += 1
    return scb

def pendingScb(psbScb):
    return 

def getScb_555():
    pre_turn = ''
    turn = ''
    scb = ''
    LENGTH = 60
    count =0 
    while count < LENGTH:
        turn = random.choice(TURN_555)
        #允许[true]w[rev]与[true]连续出现
        if turn.find("U") == 0 and pre_turn.find("U") == 0:
            if turn.find("w") == 0 and pre_turn.find("w") == -1  or pre_turn.find("w") == 0 and turn.find("w") == -1:
                scb += turn + ' '
                pre_turn = turn
                count += 1
            else:
                continue
        elif turn.find("R") == 0 and pre_turn.find("R") == 0:
            if turn.find("w") == 0 and pre_turn.find("w") == -1  or pre_turn.find("w") == 0 and turn.find("w") == -1:
                scb += turn + ' '
                pre_turn = turn
                count += 1
            else:
                continue
        elif turn.find("F") == 0 and pre_turn.find("F")  == 0:
            if turn.find("w") == 0 and pre_turn.find("w") == -1  or pre_turn.find("w") == 0 and turn.find("w") == -1:
                scb += turn + ' '
                pre_turn = turn
                count += 1
            else:
                continue
        elif turn.find("B") == 0 and pre_turn.find("B")  == 0:
            if turn.find("w") == 0 and pre_turn.find("w") == -1  or pre_turn.find("w") == 0 and turn.find("w") == -1:
                scb += turn + ' '
                pre_turn = turn
                count += 1
            else:
                continue
        elif turn.find("L") == 0 and pre_turn.find("L")  == 0:
            if turn.find("w") == 0 and pre_turn.find("w") == -1  or pre_turn.find("w") == 0 and turn.find("w") == -1:
                scb += turn + ' '
                pre_turn = turn
                count += 1
            else:
                continue
        elif turn.find("D") == 0 and pre_turn.find("D")  == 0:
            if turn.find("w") == 0 and pre_turn.find("w") == -1  or pre_turn.find("w") == 0 and turn.find("w") == -1:
                scb += turn + ' '
                pre_turn = turn
                count += 1
            else:
                continue
        else :
            scb += turn +' '
            pre_turn =turn
            count += 1
    return scb
