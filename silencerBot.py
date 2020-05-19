import discord
from random import choice
def hasRole(name='@everyone',list=[]):
    list2=[]
    for i in range(len( list)):
        list2.append(list[i].name)
    if name in list2:
        return True
    else:
        return False
indicators={'a': '\U0001f1e6', 'b': '\U0001f1e7', 'c': '\U0001f1e8', 'd': '\U0001f1e9', 'e': '\U0001f1ea', 'f': '\U0001f1eb', 'g': '\U0001f1ec', 'h': '\U0001f1ed', 'i': '\U0001f1ee', 'j': '\U0001f1ef', 'k': '\U0001f1f0', 'l': '\U0001f1f1', 'm': '\U0001f1f2', 'n': '\U0001f1f3', 'o': '\U0001f1f4', 'p': '\U0001f1f5', 'q': '\U0001f1f6', 'r': '\U0001f1f7', 's': '\U0001f1f8', 't': '\U0001f1f9', 'u': '\U0001f1fa', 'v': '\U0001f1fb', 'w': '\U0001f1fc', 'x': '\U0001f1fd', 'y': '\U0001f1fe', 'z': '\U0001f1ff'}
days='mtwhf'

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    await client.change_presence(activity=discord.Game(name="be quiet."))
@client.event
async def on_message(message):
    if not message.author.bot and not hasRole('The Silent Few',message.author.roles) and message.author!=client.user and not (message.content.startswith('*') and message.content[1]!='*' and not message.content[-2] in ['\\','*'] and message.content[-1]=='*'):
        await message.channel.send(message.author.name+' was silenced.')
        for i in 'quiet':
            await message.add_reaction(indicators[i])
        await message.author.ban
client.run('NzEyMzU2MTY5MjE3NDc0NjUw.XsQXtQ.xemct44hjcAYru8bCEWXmFwTMZo')
