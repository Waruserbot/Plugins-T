from telethon import  events
import asyncio
import random
hunt_attempts = 0
count = 0
ball = 0
catch = False

@bot.on(events.NewMessage(outgoing=True, pattern='.catch'))
async def toggle_catch(event):
    global catch
    if catch:
        catch = False
        await event.edit('''
𝙏𝙐𝙍𝙉𝙀𝘿 𝙊𝙁𝙁!
''')
        return
    else:
        catch = True
        await event.edit('''
𝙎𝙀𝘼𝙍𝘾𝙃𝙄𝙉𝙂..🧐
''')
        await bot.send_message(572621020,'/hunt')
@bot.on(events.NewMessage(chats=572621020))
async def handle_message(event):
    if 'has appeared' in event.raw_text:
        global hunt_attempts
        number_str = ''.join(filter(str.isdigit, event.text))
        number = int(number_str)
        if number < 15:
            print('Found!  ')
            if event.buttons:
                await asyncio.sleep(random.random() + 1)
                await event.click(0, 0)
        else:
            print('Level is High!')
            await bot.send_message(572621020, '/hunt')

@bot.on(events.NewMessage(chats=572621020))
async def handle_message(event):
    if 'Battle begins!' in event.raw_text:
        if event.buttons:
                global catch
                await asyncio.sleep(random.random() + 1)
                await event.click(2, 0)
                

           
@bot.on(events.NewMessage(chats=572621020))
async def handle_message(event):
     if 'An expert trainer has challenged you to a battle.' in event.raw_text:
         global hunt_attempts
         await event.respond('/hunt')
         
     

                
    
@bot.on(events.MessageEdited(chats=572621020))
async def handle_message(event):
    global catch, count, hunt_attempts
    if 'You caught a wild' in event.raw_text:
        if event.buttons:
            
            count+=1
            await asyncio.sleep(random.random() + 1)
            await bot.send_message(572621020,'/hunt')
@bot.on(events.MessageEdited(chats=572621020))
async def handle_message(event):
        if 'ball failed and the wild' in event.raw_text:
            global hunt_attempts
            await bot.send_message(572621020,'/hunt')

@bot.on(events.MessageEdited(chats=572621020))
async def handle_message(event):
    if 'damage.' in event.raw_text:
        if event.buttons:
                await asyncio.sleep(random.random() + 1)
                await event.click(2, 0)
                
@bot.on(events.MessageEdited(chats=572621020))
async def handle_message(event):
    if 'Dealt' in event.raw_text:
        if event.buttons:
                await asyncio.sleep(random.random() + 1)
                await event.click(2, 0)
@bot.on(events.MessageEdited(chats=572621020))
async def handle_message(event):
    if 'dodged' in event.raw_text:
        if event.buttons:
                await asyncio.sleep(random.random() + 1)
                await event.click(2, 0)
@bot.on(events.MessageEdited(chats=572621020))
async def handle_message(event):
    if 'fainted.' in event.raw_text:
        global hunt_attempts
        await asyncio.sleep(random.random() + 1)
        await event.respond('/hunt')     
@bot.on(events.MessageEdited(chats=572621020))
async def handle_message(event):
    if 'Current turn:' in event.raw_text:
        global ball
        if event.buttons:
                await asyncio.sleep(random.random() + 1)
                ball+=1
                await event.click(0, 0)
@bot.on(events.NewMessage(outgoing=True, pattern='.data'))
async def data(event):
    if ball == 0:
        await event.edit('''```𝘿𝘼𝙏𝘼 : 𝘼𝙐𝙏𝙊 𝘾𝘼𝙏𝘾𝙃 🥵

┏━━━━━  𝘾𝙖𝙪𝙜𝙝𝙩  ━━━┓
┌𝙉𝙞𝙜𝙜𝙖!
├𝘼𝙪𝙩𝙤 𝘾𝙖𝙩𝙘𝙝 𝙉𝙤𝙩 𝙎𝙩𝙖𝙧𝙩𝙚𝙙 𝙮𝙚𝙩.
└𝙎𝙩𝙖𝙧𝙩 𝙞𝙩 𝙗𝙮 𝙪𝙨𝙞𝙣𝙜 .𝙘𝙖𝙩𝙘𝙝
┗━━━━━  𝙄𝙣𝙛𝙤  ━━━━━┛```''')
    else:
        await event.edit('''```𝘿𝘼𝙏𝘼 : 𝘼𝙐𝙏𝙊 𝘾𝘼𝙏𝘾𝙃 🥵

┏━━━━━  𝘾𝙖𝙪𝙜𝙝𝙩  ━━━┓
┌@𝙡1𝙭𝙠𝙮
├𝙋𝙡𝙪𝙜𝙞𝙣: catch_v3.py
├𝘾𝙖𝙪𝙜𝙝𝙩 >  '''+str(count)+'''
├𝘽𝙖𝙡𝙡 𝙐𝙨𝙚𝙙 > '''+str(ball)+'''
└𝘽𝙡𝙖𝙘𝙠 𝙃𝙖𝙩𝙨 😈
┗━━━━━  𝙄𝙣𝙛𝙤  ━━━━━┛```''')
@bot.on(events.NewMessage(chats=572621020))
async def _(event):
    global catch, hunt_attempts
    if 'Daily hunt limit reached' in event.raw_text:
        await bot.send_message('me', "HeXa System limit over.")
        catch = False
    elif 'strange' in event.raw_text:
        await bot.send_message('me', "You found an egg!")
        catch = False
    elif 'Shiny pokemon found!' in event.raw_text:
        await bot.send_message('me', "Shiny found!")
        catch = False
bot.run_until_disconnected()
