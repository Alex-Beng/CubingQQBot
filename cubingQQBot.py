# -*- coding: utf-8 -*-
import Bot
import getChaos
import Spider
import IP

def onQQMessage(bot, contact, member, content):
    try:
        if len(content) == 0 or content[0] != '-' or bot.isMe(contact,member):
            return
        
        if content == '-5':
            bot.SendTo(contact,getChaos.getScb_555())
        elif content == '-3':
            bot.SendTo(contact,'暂不支持三阶打乱')
        elif content == '-2':
            bot.SendTo(contact,'二阶打乱仅支持旧标准(随机打乱)')
            bot.SendTo(contact,getChaos.getPsbScb_222())
            
        if '-wca' in content:
            flag, thing = Bot.procMsg(content)
            if flag == 0:
                bot.SendTo(contact,'有什么能帮到您的么？')
            elif flag == 1:
                personList = Spider.spider_main(thing)
                if len(personList) == 0:
                    bot.SendTo(contact,'找不到这枚外星人。。。')
                elif len(personList) == 1:
                    for person in personList:
                        sendStr = ''
                        sendStr += str(person[0])+'\n'+str(person[1]+'\n')
                        for item in person[3].keys():
                            sendStr += str(item)+' '+str(person[3][item][0]+'|'+str(person[3][item][1])+'\n' )
                            
                        bot.SendTo(contact, sendStr )
                elif len(personList) >= 2:
                    sendStr = ''
                    sendStr += str(len(personList))+' items\n'
                    if len(personList)>4:
                        for i in range(4):
                            sendStr += str(i+1)+'. '+str(personList[i][0])+' '+str(personList[i][1])+'\n'
                        sendStr += '......'
                    else :
                        for i in range(len(personList)):
                            sendStr += str(i+1)+'. '+str(personList[i][0])+' '+str(personList[i][1])+'\n'
                    bot.SendTo(contact, sendStr )
                    
        if '[@ME]' in content :
            bot.SendTo(contact, '拒绝被撩')

        if '-ip' in content :
            tlist = content.split('-ip')
            ip = tlist[1]
            sendStr = ''
            sendStr += str(ip)
            t = IP.IP(ip)
            sendStr += t.get_phy()
            bot.SendTo(contact, sendStr )
            
        if '-phone' in content:
            sendStr =''
            sendStr += '手机归属地查询正在开发中.....' 
            bot.SendTo(contact,sendStr)
            
        if '-post' in content:
            sendStr = ''
            sendStr += '城市邮编查询正在开发中......'
            bot.SendTo(contact,sendStr)
    except:
        bot.SendTo('SNU 各位大佬的小','Bot又炸了')
            
