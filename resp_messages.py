msg_already_whitelisted = "You are already whitelisted, run `/getscript` instead."

def FireWhitelisted(wl_key, script):
    msg_success_whitelisted = f'''
Your are now whitelisted | Here is your ready script:
```lua\n_G.wl_key="''' + wl_key + f'''"
{script}\n```
    '''

    return msg_success_whitelisted
    
msg_not_whitelisted = 'You are not whitelisted, run `/wl` to get whitelisted.'

def FireScriptReady(wl_key, script):
    msg_ready_script = '''
Here is your ready script:\n```lua\n_G.wl_key="''' + wl_key + f'''"
{script})\n```
Now copy and paste it into your executor and press execute'''

    return msg_ready_script

msg_blacklist_not_found = "Discord id/key not found"

msg_no_buyers_role = "You don't have the buyers role"

msg_no_admin_role = "You don't have the admin role"
