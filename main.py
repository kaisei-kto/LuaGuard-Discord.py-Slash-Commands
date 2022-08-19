import discord
from discord import app_commands
import luawl
from resp_messages import *
from config import *

luawl.luawl_token = luawl_token

class abot(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.synced = False
        self.buyer_role = buyer_role_id
        self.admin_role = admin_role_id

    async def on_ready(self):
        await tree.sync(guild=discord.Object(id=guild_id))
        self.synced = True
        print("Bot is online.")

bot = abot()
tree = app_commands.CommandTree(bot)


@tree.command(name="wl", description="Run this command if you already have the buyers role to get whitelisted for " + script_name, guild = discord.Object(id=guild_id))
async def self(interaction: discord.Interaction):
    if buyer_role_check(interaction.guild.get_role(buyer_role_id), interaction.user.roles):
        try:
            luawl.get_whitelist(str(interaction.user.id))
            await interaction.response.send_message(embed=easy_embed("Error", msg_already_whitelisted), ephemeral=True)
        except Exception:
            key = luawl.add_whitelist(str(interaction.user.id))
            msg_success_whitelist = FireWhitelisted(key, script_loadstring)
            await interaction.response.send_message(embed=easy_embed("Success", msg_success_whitelist), ephemeral=True)
    else:
        await interaction.response.send_message(embed=easy_embed("Error", msg_no_buyers_role), ephemeral=True)
                


@tree.command(name="redeem", description="Run this command if you bought a key from shoppy to get your role", guild = discord.Object(id=guild_id))
async def self(interaction: discord.Interaction):
    try:
        key = luawl.get_whitelist(str(interaction.user.id))
        if str(interaction.user.id) == key.discord_id:
            if type(bot.buyer_role) is not discord.Role:
                bot.buyer_role = interaction.guild.get_role(buyer_role_id)
            if bot.buyer_role not in interaction.user.roles:
                await interaction.user.add_roles(bot.buyer_role)
                await interaction.response.send_message(embed=easy_embed("Success", f"You now have the {bot.buyer_role.mention} role. \nYou may run `/getscript` now to get started."), ephemeral=True)
            else:
                await interaction.response.send_message(embed=easy_embed("Error", f"You already have the {bot.buyer_role.mention} role. \nYou may run `/getscript` now to get started."), ephemeral=True)
        else:
            await interaction.response.send_message(embed=easy_embed("Error", f"We couldn't find any whitelist associated with your discord account."), ephemeral=True)
    except Exception as e:
        await interaction.response.send_message(embed=easy_embed("Error", e), ephemeral=True)


@tree.command(name="getscript", description="Gives you your premium ready " + script_name + " script", guild = discord.Object(id=guild_id))
async def self(interaction: discord.Interaction):
    try:
        whitelist = luawl.get_whitelist(str(interaction.user.id))
        msg_script_ready = FireScriptReady(whitelist.wl_key, script_loadstring)
        await interaction.response.send_message(embed=easy_embed("Success", msg_script_ready), ephemeral=True)
    except Exception:
        await interaction.response.send_message(embed=easy_embed("Error", msg_not_whitelisted), ephemeral=True)


@tree.command(name="blacklist", description="Blacklist a user from " + script_name, guild = discord.Object(id=guild_id))
async def self(interaction: discord.Interaction, discord_id_or_wl_key:str):
    if admin_role_check(interaction.guild.get_role(admin_role_id), interaction.user.roles):
        response = luawl.add_blacklist(discord_id_or_wl_key)
        errorText = "error"
        if errorText in response:
            await interaction.response.send_message(embed=easy_embed("Error", msg_blacklist_not_found), ephemeral=True)
        else:
            await interaction.response.send_message(embed=easy_embed("Success", response), ephemeral=True)
    else:
        await interaction.response.send_message(embed=easy_embed("Error", msg_no_admin_role), ephemeral=True)


@tree.command(name="un-blacklist", description="Remove Blacklist of user from " + script_name, guild = discord.Object(id=guild_id))
async def self(interaction: discord.Interaction, discord_id_or_wl_key:str):
    if admin_role_check(interaction.guild.get_role(admin_role_id), interaction.user.roles):
        response = luawl.remove_blacklist(discord_id_or_wl_key)
        errorText = "error"
        if errorText in response:
            await interaction.response.send_message(embed=easy_embed("Error", msg_blacklist_not_found), ephemeral=True)
        else:
            await interaction.response.send_message(embed=easy_embed("Success", response), ephemeral=True)
    else:
        await interaction.response.send_message(embed=easy_embed("Error", msg_no_admin_role), ephemeral=True)


@tree.command(name="update-key-status", description="Update the status of a key, possible statuses: Assigned|Unassigned|Disabled|Active", guild = discord.Object(id=guild_id))
async def self(interaction: discord.Interaction, discord_id_or_wl_key:str, key_status:str):
    if admin_role_check(interaction.guild.get_role(admin_role_id), interaction.user.roles):
        try:
            response = luawl.update_key_status(discord_id_or_wl_key, key_status)
            await interaction.response.send_message(embed=easy_embed("Success", response), ephemeral=True)
        except Exception as e:
            await interaction.response.send_message(embed=easy_embed("Error", "[Error] Invalid status / " + str(e)), ephemeral=True)
    else:
        await interaction.response.send_message(embed=easy_embed("Error", msg_no_admin_role), ephemeral=True)


@tree.command(name="get-logs", description="Gets the most recent log entry of a certain user", guild = discord.Object(id=guild_id))
async def self(interaction: discord.Interaction, discord_id_or_wl_key_or_hwid:str):
    if admin_role_check(interaction.guild.get_role(admin_role_id), interaction.user.roles):
        try:
            response = luawl.get_logs(discord_id_or_wl_key_or_hwid)
            result = next(
                (item for item in response),
                {}
            )
            emb_logs = easy_embed("Latest Log of `" + discord_id_or_wl_key_or_hwid + "`", "\nExecuted on `" + result.get('executed_on') + "`\nType of error: `" + result.get('type') + "`" + "\nFailed with code: `" + result.get('message') + "`" + "\nExecutor: `" + result.get('executor_fingerprint') + "`\n──────────────────────────")
            emb_logs.add_field(name="Discord Id", value='`' + result.get('discord_id') + '`')
            emb_logs.add_field(name="Whitelist Key", value='`' + result.get('wl_key') + '`', inline=True)
            emb_logs.add_field(name="Key Status", value='`' + result.get('key_status') + '`')
            emb_logs.add_field(name="Assigned HWID", value='`' + result.get('assigned_HWID') + '`', inline=True)
            emb_logs.add_field(name="Executor HWID", value='`' + result.get('exec_HWID') + '`')
            await interaction.response.send_message(embed=emb_logs, ephemeral=True)
        except Exception as e:
            print(e)
            if "error" in result:
                responseMSG = "No logs found"
            await interaction.response.send_message(embed=easy_embed("Error", responseMSG), ephemeral=True)
    else:
        await interaction.response.send_message(embed=easy_embed("Error", msg_no_admin_role), ephemeral=True)
        
def buyer_role_check(the_buyer_role, user_roles):
    if type(bot.buyer_role) is not discord.Role:
        bot.buyer_role = the_buyer_role
    if bot.buyer_role in user_roles:
        return True
    else:
        return False
        
def admin_role_check(the_admin_role, user_roles):
    if type(bot.admin_role) is not discord.Role:
        bot.admin_role = the_admin_role
    if bot.admin_role in user_roles:
        return True
    else:
        return False

def easy_embed(title, description):
    emb = discord.Embed(title=title, description=description)
    emb.set_footer(text="LuaGuard Discord.py - https://github.com/xyba1337", icon_url="https://i.imgur.com/Xzg91Pi.png") # be nice and leave credits so others can find and use it too!
    emb.set_thumbnail(url=thumbnail_url)
    emb.color=embedcolor
    return emb
    


bot.run(bot_token)