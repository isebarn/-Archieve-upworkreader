import discord

def send_messages(ads):
  client = discord.Client()

  client.loop.create_task(my_background_task(client, ads))
  client.run('NzMyNzEwMzYxMDE0NDY4NzA2.Xw4j6Q.bV2KjT3_dCAGjosSTTv_7pYeEWI')

async def my_background_task(client, ads):

  for message in ads:
    msg = '{}\n{}\n{}'.format(message['title'], message['payment'], message['url'])
    await client.wait_until_ready()
    channel = client.get_channel(732680171143954482)
    await channel.send(msg)

  await client.close()

if __name__ == "__main__":

  ads = [{'id': '01d33e2d5b0742ea28', 'title': 'Lead generation to find MSPs in USLead generation to find MSPs in US', 'url': 'https://www.upwork.com/job/Lead-generation-find-MSPs_~01d33e2d5b0742ea28/', 'payment': 'Fixed: $10'}]

  run(ads)

