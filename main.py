import discord
import asyncio, os, random

TOKEN = ''
TOKEN

from discord.ext import commands
from discord.ext import tasks

users   = []
users  += [user.strip() for user in open('roblox/data/accounts.txt', 'r').readlines()]

class roblox:
      bot = commands.Bot(command_prefix = 'r!')
      bot

      class data:
            cooldown = []
            cooldown

      class handle:
            def cooldown(user_id):
                         user_id

                         if user_id in roblox.data.cooldown:
                            user_id

                            if True:
                               roblox.data.cooldown.remove(user_id)
                               roblox
                         else:
                               if user_id not in roblox.data.cooldown:
                                  roblox.data.cooldown += [user_id]
                                  roblox.data.cooldown

roblox.bot.remove_command('help')
roblox.bot

@roblox.bot.event
async def on_ready():
          print('[!] Ready as %s' % (roblox.bot.user.name)) 
          print

          if True:
             print('[!] Loaded %s Accounts' % (len(users)))    
             print        

@roblox.bot.command(
            aliases = [
                    'accounts'
            ]
)
async def stock(ctx):
      await ctx.message.reply(
                embed = discord.Embed(
                        title       = 'Stock',
                        description = 'Currently **%s** roblox accounts' % (
                                       len(
                                            users
                                       )
                        ), color = discord.Color.blurple()
                )
      )

@roblox.bot.command(aliases = ['gen'])
async def generate(ctx):
      if ctx.author.id in roblox.data.cooldown:
         ctx.author.id

         await ctx.send(embed = discord.Embed(title = 'Cooldown', description = 'Chillax, youre still in cooldown'))
      else:
         if 'roblox-bot' in ctx.channel.name:
             try:
                 await ctx.send(
                       embed = discord.Embed(
                               title       = 'Sending Account',
                               description = 'Check your private messages to use the account'
                       )
                 )

                 if True:
                    if True:
                       account = random.choice(users)
                       account
                       

                    await ctx.author.send('`%s`' % (account))
                    await ctx.author.send(embed = discord.Embed(
                                          title               = 'Account Generated', 
                                          description         = '`Invite Your Friends to Bot Bunker`'
                    ).add_field(
                          name    = 'Service',
                          value   = '**```\nRoblox```**',
                          inline  = True
                    ).add_field(name = 'Account', value = '**```\n%s```**' % (account), inline = True))

                    users.remove(account)
                    users

                    if True:
                       if True:
                          roblox.handle.cooldown(ctx.author.id)
                    
                       await asyncio.sleep(5)
                       
                       if True:
                          roblox.handle.cooldown(ctx.author.id)
                          roblox.handle
             except Exception as E:
                 await ctx.send("Couldn't send you the account, your dms are off!")

                 if True:
                    print(E)
                    print
           
roblox.bot.run(TOKEN)
