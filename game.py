#Telegram Game (Inspired by Dank memer idle miner and the like)
#Run the .bat file in this folder if you do not have any one of these modules.
#Check out my youtube channel, name is Menye, and i talk about Python.
from telethon import TelegramClient, events, sync
from pathlib import Path
import random
import time

#Local Libraries
from messages import *
import info

#Telethon Details
#Insery your details into the info.py file.
api_id = info.api_id
api_hash = info.api_hash
client = TelegramClient('game', api_id, api_hash)
client.start()

#Variable Initializations
game_name = "Idle City"
starting_cash = 5000
currency = "$"
prefix = "!city"
impjokes = [' \nUnless your blood is overheating \U0001F923\U0001F923\U0001F923', '\nDo not let the greed consume you, ~~its just money~~ \U0001F923\U0001F923\U0001F923', '\nI sincerely cannot believe your impatience. \U0001F923\U0001F923\U0001F923']
temp = {'name': '', 'level': 1, 'xp': 0, 'job': 0, 'bal': 5000, 'bankA': 0, 'bank': 0, 'lm': 0, 'pd': 1, 'b1': 1, 'b2': 1, 'b3': 1, 'sm': 0, 'gb': 0, 'w': 0, 'ib': 0, 'sb': 0, 'dia': 0, 'pet_t': '', 'pet_n': '', 'searcht': 0, 'bt': 0, 'business': '', 'jt': 0, 'jobA': 0, 'jobT': 0, 'salary': 0}
rank = {1: 'Novice', 2: 'Apparentice', 3: 'Senior App.', 4:'Amateur', 5:'Businessman', 6:'Senior Businessman', 7:'Advanced businessman', 8:'Old timer', 9:'Millionare', 10:'Multi-Millionare'}
jobs = {'Telegram User': 5000, 'Programmer': 7500, 'Gamer': 10000, 'Content creator': 15000, 'Relator': 30000, 'International Manager': 40000}
items = {'landmine': 'lm', 'padlock': 'pd', 'b1': 'b1', 'b2': 'b2', 'b3': 'b3', 'scrap_metal': 'sm', 'gold_bar': 'gb', 'wood': 'w', 'iron_bar': 'ib', 'silver_bar': 'sb', 'diamond': 'dia'}
prices = {'landmine': [10000, 20000], 'padlock': [5000, 10000], 'b1': [5000, 12000], 'b2': [8000, 15000], 'b3': [10000, 25000], 'scrap_metal': [500], 'gold_bar': [20000, 40000], 'wood': [1000], 'iron_bar': [10000, 25000], 'silver_bar': [15000, 30000], 'diamond': [75000, 100000]}
levels = {1: 2000, 2: 2500, 3: 3000, 4: 3500, 5: 4000, 6: 5500, 7: 6500, 8: 7500, 9: 8750, 10: 10000}
businesses = {'tuckshop': [500000, 26000], 'game': [1000000, 50000], 'networking': [2000000, 120000], 'fashion': [5000000, 375000], 'restaurant': [8000000, 500000], 'real_estate':[15000000, 750000], 'online_retail': [22500000, 1000000], 'internet_provider': [30000000, 1250000], 'electronics': [40000000, 1500000], 'motors': [50000000, 1750000], 'weapons': [100000000, 2500000], 'country': [200000000, 3000000], 'space_station': [500000000, 5000000], 'GOD': [1000000000, 10000000]}

async def main():
    await client.send_message('someone you want to send to', startMessage)

#MiniGames
#You can switch this up coz i get more tails than heads smh -_-
def coinflip():
    lel = random.randint(0, 1)
    if lel == 0:
        return 'heads'
    else:
        return 'tails'

def snakeEyes():
    d1 = random.randint(1, 6)
    d2 = random.randint(1, 6)
    if d1 == 1 and d2 == 1:
        return 'snakeeyes'
    elif d1 == 1 or d2 == 1:
        return 'one'
    else:
        return 'zero'

#User Function Definitions
def newUser(user):
    f = open(f'{user}.txt', 'w')
    new = temp
    new['name'] = user
    new['level'] = 1
    new['xp'] = 0
    new['date'] = time.time()
    f.write(str(new))

def levelCheck(user):
    f = open(f'{user}.txt', 'r')
    raw_dict = f.readline()
    userDict = eval(raw_dict)
    levelup = levels[userDict['level']]
    if userDict['xp'] >= levelup:
        userDict['xp'] -= levelup
        userDict['level'] += 1
    else:
        pass
    f.close()
    f = open(f'{user}.txt', 'w')
    f.write(str(userDict))
    f.close()

def verifyAccount(user):
    filename = f'{user}.txt'
    my_file = Path(filename)
    if my_file.is_file():
        return True
    else:
        return False
def acc_bal(user):
    levelCheck(user)
    f = open(f'{user}.txt', 'r')
    raw_dict = f.readline()
    userDict = eval(raw_dict)
    return userDict['bal']

def progress(xp, levelup):
    lv = levelup / 10
    pr = xp//lv
    f = '\U0001F315'
    e = '\U0001F311'
    en = int(10-pr)
    fn = int(10-en)
    return f*fn + e*en

def getInfo(user):
    f = open(f'{user}.txt', 'r')
    raw_dict = f.readline()
    userDict = eval(str(raw_dict))
    lvl = userDict['level']
    userDict['rank'] = rank[lvl]
    jb = userDict['job']
    if jb:
        userDict['salary'] = jobs[jb]
        userDict['job'] = 'Jobless baggar'
    else:
        userDict['salary'] = 'You are jobless'
        pass
    idk = userDict['level']
    userDict['levelup'] = levels[idk]
    if userDict['bankA'] == 1:
        userDict['banke'] = userDict['bank']
    else:
        userDict['banke'] = 'N/A'
    return userDict

def credit(user, amount):
    levelCheck(user)
    f = open(f'{user}.txt', 'r')
    raw_dict = f.readline()
    userDict = eval(raw_dict)
    userDict['bal'] += amount
    userDict['xp'] += random.randint(1, 50)
    f.close()
    f = open(f'{user}.txt', 'w')
    f.write(str(userDict))

def startJob(user, job):
    levelCheck(user)
    f = open(f'{user}.txt', 'r')
    raw_dict = f.readline()
    userDict = eval(str(raw_dict))
    userDict['job'] == job
    userDict['jobA'] == 1
    userDict['jt'] == time.time()
    userDict['salary'] == jobs[job]
    f.close()
    f = open(f'{user}.txt', 'w')
    f.write(str(userDict))

def give(user, item, amount, search=0, b=0):
    levelCheck(user)
    it = items[item]
    f = open(f'{user}.txt', 'r')
    raw_dict = f.readline()
    userDict = eval(raw_dict)
    userDict[it] += amount
    userDict['xp'] += random.randint(1, 50)
    f.close()
    if search==1:
        if b != 0:
            userDict['searcht'] = time.time()
            finalvar = 'b'+str(b)
            userDict[finalvar] -= 1
            f = open(f'{user}.txt', 'w')
            f.write(str(userDict))
        else:
            userDict['searcht'] = time.time()
            f = open(f'{user}.txt', 'w')
            f.write(str(userDict))
    else:
        f = open(f'{user}.txt', 'w')
        f.write(str(userDict))

def business(user, busines):
    levelCheck(user)
    f = open(f'{user}.txt', 'r')
    raw_dict = f.readline()
    userDict = eval(raw_dict)
    userDict['xp'] += random.randint(200, 400)
    if userDict['bal'] < businesses[busines][0]:
        pass
    else:
        userDict['business'] = busines
        userDict['bal'] -= businesses[busines][0]
        userDict['bt'] = time.time()
        userDict['income'] = businesses[busines][1]
        f.close()
        f = open(f'{user}.txt', 'w')
        f.write(str(userDict))

def bizClaim(user):
    levelCheck(user)
    f = open(f'{user}.txt', 'r')
    raw_dict = f.readline()
    userDict = eval(raw_dict)
    userDict['bal'] += userDict['income']
    userDict['bt'] = time.time()
    f.close()
    f = open(f'{user}.txt', 'w')
    f.write(str(userDict))

def sell(user, item, amount):
    levelCheck(user)
    itemo = items[item]
    price = prices[item][0]
    am = int(amount)
    selling = price * am
    f = open(f'{user}.txt', 'r')
    raw_dict = f.readline()
    userDict = eval(raw_dict)
    if userDict[itemo] == am or userDict[itemo] > am:
        userDict[itemo] -= am
        userDict['bal'] += selling
        userDict['xp'] += random.randint(1, 50)
        f.close()
        f = open(f'{user}.txt', 'w')
        f.write(str(userDict))

def decredit(user, amount):
    levelCheck(user)
    f = open(f'{user}.txt', 'r')
    raw_dict = f.readline()
    userDict = eval(raw_dict)
    userDict['bal'] -= amount
    userDict['xp'] += random.randint(1, 50)
    f.close()
    f = open(f'{user}.txt', 'w')
    f.write(str(userDict))

def jcrypt(user):
    levelCheck(user)
    f = open(f'{user}.txt', 'r')
    raw_dict = f.readline()
    userDict = eval(raw_dict)
    userDict['jobT'] = '$!@#$%^&*(*&^%$#@'
    userDict['xp'] += random.randint(1, 5)
    f.close()
    f = open(f'{user}.txt', 'w')
    f.write(str(userDict))    

def search():
    rw = 0
    am = 0
    one = random.randint(1, 100)
    two = random.randint(1, 100)
    luck = one * two
    if luck < 401:
        rw = 'nothing'
    elif luck < 3601:
        rw = 'scrap_metal'
        am = random.randint(1, 20)
    elif luck < 6401:
        rw = 'wood'
        am = random.randint(1, 10)
    elif luck < 8100:
        rw = 'iron_bar'
        am = random.randint(1, 5)
    elif luck < 9025:
        rw = 'silver_bar'
        am = random.randint(1, 4)
    elif luck < 9604:
        rw = 'gold_bar'
        am = random.randint(1, 3)
    elif luck < 10001:
        rw = 'diamond'
        am = 1
    return rw, am

def boostSearch(b):
    if b == 1:
        luck = random.randint(1, 100)
        if luck < 20:
            rw = 'nothing'
        elif luck < 60:
            rw = 'scrap_metal'
            am = random.randint(5, 25)
        elif luck < 80:
            rw = 'wood'
            am = random.randint(5, 15)
        elif luck < 90:
            rw = 'iron_bar'
            am = random.randint(3, 6)
        elif luck < 95:
            rw = 'silver_bar'
            am = random.randint(2, 5)
        elif luck < 98:
            rw = 'gold_bar'
            am = random.randint(2, 4)
        elif luck < 101:
            rw = 'diamond'
            am = 1
        return rw, am
    elif b == 2:
        luck = random.randint(1, 100)
        if luck < 15:
            rw = 'nothing'
        elif luck < 50:
            rw = 'scrap_metal'
            am = random.randint(5, 50)
        elif luck < 70:
            rw = 'wood'
            am = random.randint(1, 20)
        elif luck < 80:
            rw = 'iron_bar'
            am = random.randint(3, 7)
        elif luck < 90:
            rw = 'silver_bar'
            am = random.randint(2, 6)
        elif luck < 96:
            rw = 'gold_bar'
            am = random.randint(2, 5)
        elif luck < 101:
            rw = 'diamond'
            am = 1
        return rw, am
    elif b == 3:
        luck = random.randint(1, 100)
        if luck < 10:
            rw = 'nothing'
        elif luck < 40:
            rw = 'scrap_metal'
            am = random.randint(10, 100)
        elif luck < 60:
            rw = 'wood'
            am = random.randint(1, 30)
        elif luck < 75:
            rw = 'iron_bar'
            am = random.randint(2, 14)
        elif luck < 88:
            rw = 'silver_bar'
            am = random.randint(2, 12)
        elif luck < 95:
            rw = 'gold_bar'
            am = random.randint(2, 8)
        elif luck < 101:
            rw = 'diamond'
            am = random.randint(1, 2)
        return rw, am
    else:
        rw = 'scrap_metal'
        am = random.randint(1, 100)
        return rw, am
        

def openBank(user):
    levelCheck(user)
    f = open(f'{user}.txt', 'r')
    raw_dict = f.readline()
    userDict = eval(raw_dict)
    userDict['bankA'] = 1
    userDict['bal'] -= 5000
    userDict['xp'] += random.randint(20, 30)
    f.close()
    f = open(f'{user}.txt', 'w')
    f.write(str(userDict))

def upgrade(user, token):
    levelCheck(user)
    if token == 'iron_bar':
        f = open(f'{user}.txt', 'r')
        raw_dict = f.readline()
        userDict = eval(raw_dict)
        one = userDict['income']
        one *= 0.05
        userDict['income'] = userDict['income'] + one
        userDict['ib'] -= 1
        f.close()
        f = open(f'{user}.txt', 'w')
        f.write(str(userDict))
    elif token == 'silver_bar':
        f = open(f'{user}.txt', 'r')
        raw_dict = f.readline()
        userDict = eval(raw_dict)
        one = userDict['income']
        one *= 0.15
        userDict['income'] = userDict['income'] + one
        userDict['sb'] -= 1
        f.close()
        f = open(f'{user}.txt', 'w')
        f.write(str(userDict))
    elif token == 'gold_bar':
        f = open(f'{user}.txt', 'r')
        raw_dict = f.readline()
        userDict = eval(raw_dict)
        one = userDict['income']
        one *= 0.2
        userDict['income'] = userDict['income'] + one
        userDict['gb'] -= 1
        f.close()
        f = open(f'{user}.txt', 'w')
        f.write(str(userDict))
    elif token == 'diamond':
        f = open(f'{user}.txt', 'r')
        raw_dict = f.readline()
        userDict = eval(raw_dict)
        one = userDict['income']
        one *= 0.4
        userDict['income'] = userDict['income'] + one
        userDict['dia'] -= 1
        f.close()
        f = open(f'{user}.txt', 'w')
        f.write(str(userDict))
    else:
        pass

def withdraw(user, amount):
    levelCheck(user)
    f = open(f'{user}.txt', 'r')
    raw_dict = f.readline()
    userDict = eval(raw_dict)
    userDict['bal'] += amount
    userDict['bank'] -= amount
    userDict['xp'] += random.randint(1, 5)
    f.close()
    f = open(f'{user}.txt', 'w')
    f.write(str(userDict))

def work(user):
    levelcheck(user)
    f = open(f'{user}.txt', 'r')
    raw_dict = f.readline()
    userDict = eval(raw_dict)
    if userDict['jobA'] == 0:
        pass
    else:
        userDict['jt'] = time.time()
        userDict['jobT'] = getWork(userDict['job'])
        userDict['xp'] += random.randint(1, 5)
        f.close()
        f = open(f'{user}.txt', 'w')
        f.write(str(userDict))
        return userDict['jobT']
    
def deposit(user, amount):
    levelCheck(user)
    f = open(f'{user}.txt', 'r')
    raw_dict = f.readline()
    userDict = eval(raw_dict)
    userDict['bal'] -= amount
    userDict['bank'] += amount
    userDict['xp'] += random.randint(1, 5)
    f.close()
    f = open(f'{user}.txt', 'w')
    f.write(str(userDict))

def buy(user, item):
    levelCheck(user)
    item = item.replace(' ', '_')
    f = open(f'{user}.txt', 'r')
    raw_dict = f.readline()
    userDict = eval(raw_dict)
    if item in items:
        if userDict['bal'] > prices[item][1]-1:
            userDict[items[item]] += 1
            userDict['bal'] -= prices[item][1]
            userDict['xp'] += random.randint(1, 50)
    f.close()
    f = open(f'{user}.txt', 'w')
    f.write(str(userDict))
        

#Main reply Loop
@client.on(events.NewMessage)
async def my_event_handler(event):
    if '!city help' in event.raw_text or '!city h' in event.raw_text:
        user = (await event.get_sender())
        sender = user.first_name
        await event.reply(helpMessage)
    if '!city shop' in event.raw_text or '!city store' in event.raw_text:
        user = (await event.get_sender())
        sender = user.first_name
        await event.reply(storeMessage)
    if 'city start' in event.raw_text:
        user = (await event.get_sender())
        sender = user.first_name
        if verifyAccount(sender):
            await event.reply(sender + "You already have an account. Dementia?!")
        else:
            newUser(sender)
            await event.reply(f"""\U0001F525**Welcome to __Idle City__!**\U0001F525
\U0001F449{sender}, Thank you for creating an account!\n
\U0001F449Since you are NEW \U0001F195 here, you can use **!city help** to check some commands.
\U0001F4B0 You need to **LEVEL UP** and get more opportunities.\n
\U000026A1**__Have Fun {sender}!__**

""")
    if '!city cf' in event.raw_text or '!city coinflip' in event.raw_text:
        user = (await event.get_sender())
        sender = user.first_name
        message = event.raw_text
        if 'coinflip' or 'cf' in message:
            m2 = message.replace('!city coinflip ', '')
            m2 = m2.replace('!city cf ', '')
            bet = int(m2)
            brat = coinflip()
            if bet != '' and bet > 0:
                if acc_bal(sender) > bet or acc_bal(sender) == bet:
                    if brat == 'heads':
                        await event.reply(sender + ", you got HEADS! You win $" + str(bet))
                        bel = acc_bal(sender)
                        newbal = bel+bet
                        credit(sender, bet)
                    else:
                        await event.reply(sender + ", you got TAILS! You lose $" + str(bet) + ". Hahahahaha")
                        bel = acc_bal(sender)
                        newbal = bel-bet
                        decredit(sender, bet)
                else:
                    await event.reply(sender + ", Your pockets are empty, didn't you check wallet?")
            elif int(bet) == 0:
                await event.reply(sender + ", you have to wager something, or can you not read?")
            elif int(bet) < 0:
                await event.reply(sender + ", that feature has been removed. Now, you can NO LONGER CHEAT!")

    if '!city profile' in event.raw_text or '!city p' in event.raw_text:
        user = (await event.get_sender())
        sender = user.first_name
        if verifyAccount(sender):
            acc = getInfo(sender)
            bang = progress(acc['xp'], acc['levelup'])
            ban2 = time.time() - acc['date']
            bang2 = round(ban2, 2)
            await event.reply(f"""\U0001F44B **Hello, {sender}**\n
\U0001F449 This is everything there is to know about you.\n
\U0001F601**Name:** {acc['name']}
\U0001F4B0**Job:** {acc['job']}
\U0001F911**Salary:** ${acc['salary']}\n
\U0001F62C**Current balance:** ${acc['bal']}
\U0001F50F**Bank account balance:** ${acc['banke']}\n
\U0001F44D**Current Level:** Level {acc['level']}
\U0001F44D**Current rank:** {acc['rank']}
\U0001F44D**XP:** {acc['xp']}/{acc['levelup']}\n
\U0001F310**XP Progress bar:**\U0001F310
{bang}

Account time: {bang2}s
""")
    if '!city search' in event.raw_text or '!city sa' in event.raw_text:
        user = (await event.get_sender())
        sender = user.first_name
        rewards = search()
        searcht = time.time()
        userInfo = getInfo(sender)
        ev = searcht - userInfo['searcht']
        if ev < 46:
            await event.reply(sender + f", you need to wait at least 45 seconds before searching." + impjokes[random.randint(0, 2)])
            pass
        else:
            if rewards[0] == 'nothing':
                await event.reply(sender + ", are you blind? \U0001F440\n You found NOTHING! \U0001F440\U0001F440\U0001F440")
            else:
                give(sender, rewards[0], rewards[1], 1)
                await event.reply(sender + f", You just won {rewards[0]} [{rewards[1]}]. Nice eyes! \U0001F44D")

    if '!city sell' in event.raw_text:
        user = (await event.get_sender())
        sender = user.first_name
        msg = event.raw_text
        msg2 = msg.replace('!city sell', '')
        msg3 = msg2.split()
        msg4 = msg3[0]
        if len(msg3) == 2:
            msg5 = msg3[1]
            if msg4 in prices:
                if int(msg5):
                    sell(sender, msg4, int(msg5))
                    await event.reply(sender + " just sold " + str(msg5) + " " + msg4 + " for $" + str(int(prices[msg4][0])*int(msg5)) + "!")
            else:
                await event.reply("I do not know what item that is, please try again or just keep it, money is not everything.")
        else:
            msg5 = 1
            sell(sender, msg4, msg5)
            await event.reply(sender + " just sold " + str(msg5) + " " + msg4 + " for " + str(int(prices[msg4][0])*int(msg5)) + "!")

    if '!city items' in event.raw_text or '!city i' in event.raw_text:
        user = (await event.get_sender())
        sender = user.first_name
        if verifyAccount(sender):
            acc = getInfo(sender)
            await event.reply(f"""\U0001F920 Your **items**\n
__**[---- Normal Items ----]**__
\U0001F9FA**Scrap Metal**: {acc['sm']}
\U0001FA91**Wood**: {acc['w']}
\U0001F9F2**Iron**: {acc['ib']}
\U0000FE0F**Silver**: {acc['sb']}
\U0000FE0F**Gold**: {acc['gb']}
\U0001F48E**Diamond**: {acc['dia']}

__**[---- Boosters ----]**__
\U0001F680**Boost Burst (+20%)**: {acc['b1']}
\U0001F680**Amazing Boost (+40%)**: {acc['b2']}
\U0001F680**GoDsPeEd! (+75%)**: {acc['b3']}
""")
    if '!city business' in event.raw_text or '!city b' == event.raw_text:
        user = (await event.get_sender())
        sender = user.first_name
        acc = getInfo(sender)
        await event.reply(f"""\U0001F3E2__Ready to become a__ **BUSINESSMAN**?\U0001F3E2\n
\U0001F3AE**Game Business**:
**Starting cost**: $1,000,000
**Earning**: $50,000

\U0001F310**Networking**:
**Starting cost**: $2,000,000
**Earning**: $120,000

\U0001F46F**Fashion**:
**Starting cost**:$5,000,000
**Earning**:$375,000

\U0001F354**Restaurant**:
**Starting cost**:$8,000,000
**Earning**:$500,000

\U0001F3D7\U0001F3D8**Real Estate**:
**Starting cost**:$15,000,000
**Earning**:$750,000

Note: **You earn every 5 minutes**
To start, use !city open [business_name]
Use all lowercase, and underscore instead of space
""")
    if '!city open' in event.raw_text:
        user = (await event.get_sender())
        sender = user.first_name
        acc = getInfo(sender)
        if acc['level'] < 5:
            await event.reply(sender + f", you must be at least level 5 to start a business.")
        else:
            msg = event.raw_text.replace('!city open ', '')
            if acc['business'] == '':
                if msg in businesses:
                    business(sender, msg)
                    await event.reply(sender + f"{msg} business created\n\nAlso, you just recieved your first income, so you have to wait 5 minutes before claiming another.")
                else:
                    await event.reply(sender + f", I hope you can read, that does not look like a business to me.")
            else:
                if acc['business'] == msg:
                    await event.reply(sender + f", you aLrEaDy have that BUSINESS! You greedy or what?")
                else:
                    business(sender, msg)
                    await event.reply(sender + f"{msg} business created\n\nAlso, you just recieved your first income, so you have to wait 5 minutes before claiming another.")


    if '!city claim' in event.raw_text:
        user = (await event.get_sender())
        sender = user.first_name
        acc = getInfo(sender)
        t = time.time()
        ps = t - acc['bt']
        if ps < 300:
            await event.reply(sender + f", you must wait 5 minutes before claiming your income.")
        else:
            bizClaim(sender)
            await event.reply(sender + f", you just claimed ${acc['income']}.")

    if '!city wallet' in event.raw_text or '!city balance' in event.raw_text or '!city w' == event.raw_text:
        user = (await event.get_sender())
        sender = user.first_name
        acc = getInfo(sender)
        await event.reply(sender + f", your balance is ${acc['bal']}.")
    if '!city transfer' in event.raw_text:
        user = (await event.get_sender())
        sender = user.first_name
        acc = getInfo(sender)
        s = event.raw_text.replace('!city transfer ', '')
        t = s.split()
        r = t[0]
        a = t[1]
        if acc['bal'] > int(a):  
            decredit(sender, int(a))
            credit(r, int(a))
            await event.reply(sender + f", you just gave {r} ${a}. If this was a mistake, LOL!")
        else:
            await event.reply(sender + f", something went wrong. either you POOR or NOT RICH.")

    if '!city bank' == event.raw_text:
        user = (await event.get_sender())
        sender = user.first_name
        acc = getInfo(sender)
        if acc['bankA'] == 1:
            await event.reply(sender + f", your account balance is ${acc['bank']}.")
        else:
            await event.reply(sender + f", to make a bank account, use !city bankacc. Note: you need to pay $5000 to have a bank account.")

    if '!city bankacc' in event.raw_text:
        user = (await event.get_sender())
        sender = user.first_name
        acc = getInfo(sender)
        if acc['bankA'] == 1:
            await event.reply(sender + f", you ALREADY HAVE AN ACCOUNT! I will delete it...")
        else:
            if acc['bal'] < 5000:
                await event.reply(sender + f", you need to have at least $5000 to have an account.")
            else:
                openBank(sender)
                await event.reply(sender + f", bank account created.")

    if '!city withdraw' in event.raw_text or '!city with' in event.raw_text:
        user = (await event.get_sender())
        sender = user.first_name
        acc = getInfo(sender)
        if acc['bankA'] == 1:
            wdraw = event.raw_text.replace('!city withdraw', '')
            wdraw = wdraw.replace('!city with', '')
            if int(wdraw) > acc['bank']:
                await event.reply(sender + f", you are not that rich. Poor 1d10t")
            else:
                abc = int(wdraw)
                withdraw(sender, abc)
                await event.reply(sender + f", ${abc} was withdrawn from your account.")
        else:
            await event.reply(sender + f", you do not have an account. Are u a thief?")

    if '!city deposit' in event.raw_text or '!city d ' in event.raw_text:
        user = (await event.get_sender())
        sender = user.first_name
        acc = getInfo(sender)
        if acc['bankA'] == 1:
            wdraw = event.raw_text.replace('!city deposit ', '')
            wdraw = wdraw.replace('!city d ', '')
            if wdraw != 'all' and int(wdraw) > acc['bal']:
                await event.reply(sender + f", you are not that rich. Poor 1d10t")
            elif wdraw == 'all':
                abc = acc['bal']
                deposit(sender, abc)
                await event.reply(sender + f", ${abc} was deposited into your account.")
            else:
                abc = int(wdraw)
                deposit(sender, abc)
                await event.reply(sender + f", ${abc} was deposited into your account.")
        else:
            await event.reply(sender + f", you do not have an account. Are u a thief?")

    if '!city upgrade' in event.raw_text:
        user = (await event.get_sender())
        sender = user.first_name
        acc = getInfo(sender)
        msg = event.raw_text
        m2 = msg.split()
        if acc['business'] != '':
            upgrade(sender, m2[2])
            await event.reply(sender + f",you just BOOSTED your business income! I wont reveal the secret...")
        else:
            await event.reply(sender + f", you do not have a business.")

    if '!city buy' in event.raw_text:
        user = (await event.get_sender())
        sender = user.first_name
        acc = getInfo(sender)
        msg = event.raw_text
        m2 = msg.split()
        buy(sender, m2[2])
        itn = m2[2].replace('_', ' ')
        await event.reply(sender + f", just bought a(n) {itn}")

    if '!city boost' in event.raw_text:
            user = (await event.get_sender())
            sender = user.first_name
            searcht = time.time()
            msg = event.raw_text
            userInfo = getInfo(sender)
            ev = searcht - userInfo['searcht']
            if ev < 46:
                await event.reply(sender + f", you need to wait at least 45 seconds before searching.")
                pass
            else:
                msg2 = msg.split()
                no = msg2[2]
                finalvar = 'b'+no
                if userInfo[finalvar] < 1:
                    await event.reply(sender + f", you do not have that booster.")
                else:
                    rewards = boostSearch(int(no))
                    if rewards[0] == 'nothing':
                        await event.reply(sender + ", are you blind? You found NOTHING!")
                    else:
                        give(sender, rewards[0], rewards[1], 1, int(no))
                        await event.reply(sender + f", You just BOOSTER won {rewards[0]}[{rewards[1]}]! Nice eyes!")


client.start()
#client.loop.run_until_complete(main())
client.run_until_disconnected()
