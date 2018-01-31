import Spider

# input raw Message
# output ( flag , proedMsg  )
# flag == 0 is nothing
# flag == 1 is refer person
# flag == 2 is get scramble
def procMsg(rawMsg):
    if rawMsg[0] == '-':
        tList = rawMsg.split('-')
        if tList[1] == '' :
            return   0, ''
        else :
            if '-wca' in rawMsg:
                tList = rawMsg.split('-wca')
                return 1,tList[1]
            # Not complite the disorganize part !
            else:
                if '-3' in rawMsg:
                    return 2, '333'
                elif '-2' in rawMsg:
                    return 2, '222'
                elif '-5' in rawMsg:
                    return 2,'555'

def sendMsg2Group(msg,groupList,bot):
    for group in groupList:
        bg = bot.List('group',group)
        if bg is not None:
            bot.SendTo (bg[0],msg)


