import discord
client = discord.Client()

@client.event
async def on_ready():
  print('we have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

    if message.content.startswith('$hello'):
      await message.channel.send('hello!')

      client.run('OTQ2MjI5NzA1ODYwODQ5Njc1.YhbrFQ.Ho6AdHAcZHyos3qmHUMeBdRiLgU')
  