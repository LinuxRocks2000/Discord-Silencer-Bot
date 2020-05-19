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
def makeDict(iterator):
    making=[]
    for i in iterator:
        making.append(i)
    made={}
    for i in making:
        made[i[0]]=i[1]
    return made
def isTrue(dict):
    trues=[]
    for i in dict:
        if dict[i]==True:
            trues.append(i)
    return trues
def make(letter): ## Python magic does the same as the original thing
	lets="abcdefghijklmnopqrstuvwxyz"
	maked=eval('''"\\U000'''+hex(lets.index(letter)+127462)[2:]+'''"''')
	return maked
async def addReactWord(word,message):
    for x in word:
        await message.add_reaction(make(x))
#days='mtwhf'  ## As this robot seems more inclined to reek havoc than anything else, no need for a day counter.

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    await client.change_presence(activity=discord.Game(name="be quiet."))
@client.event
async def on_message(message):
    if message.author==client.user:
        return ## Terminates before anything else. Not perhaps the most sensical way to do it, but it works.
    if message.content.startswith('tsb!'):
        args=message.content.split(" ") ## Use split to get argument list.
        if args[1]=="perms":
            await message.channel.send('I have the permissions: '+str(isTrue(makeDict(iter((message.channel.permissions_for(message.channel.guild.me)))))))
        else:
            await message.channel.send("That's not a thing.")
    elif not message.author.bot and not hasRole('The Silent Few',message.author.roles) and message.author!=client.user and not (message.content.startswith('*') and message.content[1]!='*' and not message.content[-2] in ['\\','*'] and message.content[-1]=='*'):
        await message.channel.send(message.author.name+' was silenced.')
        await addReactWord("quiet",message)
        await message.author.ban(reason='Being too loud.')
client.run(input('What is the bot\'s token?'))
