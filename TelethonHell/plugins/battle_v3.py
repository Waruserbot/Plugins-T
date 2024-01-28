import asyncio
import re
import webbrowser
webbrowser.open('')
from telethon import  events
import random
from telethon.errors import MessageIdInvalidError
api_id = '1747534' # Keep this as it is 
api_hash = '5a2684512006853f2e48aca9652d83ea' # same heree
pd = 0
bt = 0
def main():
    @bot.on(events.MessageEdited(from_users=572621020))
    async def _(event):
        if "Choose your next pokemon." in event.raw_text:
            if event.buttons:
                await asyncio.sleep(random.random() + 1)
                await event.click(0, 1)
            return
    @bot.on(events.NewMessage(outgoing=True, pattern='.db_battle'))
    async def _(event):
        await event.edit('''\nData For Auto Battle\nTotal Battles : '''+ str(bt)+'''\nTotal Pd : '''+str(pd))
    @bot.on(events.NewMessage(from_users=5813403535, pattern='.stop'))
    async def _(event):
        await event.edit('Successfully Stopped.')
        return
        pass
        bot.disconnect()
    @bot.on(events.NewMessage(from_users=5491047155, pattern='.start'))
    async def _(event):
        await event.edit('Successfully Started.')          
        await bot.send_message(572621020,'/hunt')


    @bot.on(events.NewMessage(from_users=572621020))
    async def _(event):
        if "has appeared" in event.raw_text:
            if event.buttons:
                await asyncio.sleep(random.random() + 1)
                await event.click(0, 0)
                global bt
                bt+=1
            return

    @bot.on(events.NewMessage(from_users=572621020))
    async def _(event):
        if "Battle begins!" in event.raw_text:
            if event.buttons:
                await asyncio.sleep(random.random() + 1)
                await event.click(0, 0)
                #await message.click(row, column) ye hoga yaad rkahna hai
            return

    @bot.on(events.MessageEdited(from_users=572621020))
    async def _(event):
        if "Battle begins!" in event.raw_text:
            try:
                await asyncio.sleep(random.random() + 1)
                await event.click(0)
            except (asyncio.TimeoutError, MessageIdInvalidError):
                pass

    @bot.on(events.MessageEdited(from_users=572621020))
    async def _(event):
        if "+" in event.raw_text:
            await asyncio.sleep(2)
            await event.respond('/hunt')
            message = event.raw_text
            match = re.search(r'\+(\d+)\s*', message) 
            if match:
                global pd
                num = int(match.group(1))
                pd+=num
            
            

    @bot.on(events.NewMessage(from_users=572621020))
    async def _(event):
        if "has appeared" in event.raw_text:
            if event.buttons:
                await asyncio.sleep(random.random() + 1)
                await event.click(0, 0)
    @bot.on(events.NewMessage(from_users=572621020))
    async def _(event):
        if "An expert trainer has challenged you to a battle." in event.raw_text:
            if event.buttons:
                await asyncio.sleep(random.random() + 1)
                await event.click(0, 0)
                
        
    @bot.on(events.MessageEdited(from_users=572621020))
    async def _(event):
        if "Current turn:" in event.raw_text:
            if event.buttons:
                await asyncio.sleep(random.random() + 1)
                await event.click(0, 0)
            return
    @bot.on(events.MessageEdited(from_users=572621020))
    async def _(event):
        if "Current turn:" in event.raw_text:
            try:
                await asyncio.sleep(random.random() + 1)
                await event.click(0)
            except (asyncio.TimeoutError, MessageIdInvalidError):
                pass

    bot.start()
    bot.run_until_disconnected()

main()
