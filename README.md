
<h1 align="center">
  <br>
  <a href="https://luawl.com/"><img src="https://i.imgur.com/Xzg91Pi.png" alt="LuaGuard Discord.py" width="200"></a>
  <br>
  LuaGuard Discord.py
  <br>
</h1>

<h4 align="center">A discord shlash commands bot that utilizes the LuaGuard API. Made in <a href="https://discordpy.readthedocs.io/en/stable/migrating.html" target="_blank">Python & Discord.py 2.0</a>.</h4>

<p align="center">
  <a href="https://www.paypal.me/AmitMerchant">
    <img src="https://img.shields.io/badge/$-donate-ff69b4.svg?maxAge=2592000&amp;style=flat">
  </a>
</p>

<p align="center">
  <a href="#key-features">Key Features</a> •
  <a href="#how-to-use">How To Use</a> •
  <a href="#credits">Credits</a> •
  <a href="#license">License</a>
</p>

![Imgur](https://i.imgur.com/exqAJTI.gif)

## Key Features

* /wl
  - Allow users with a certain role to authenticate themselves (automatically uses own discord id)
* /redeem
  - Run this command if you bought a key from shoppy to get your role (automatically uses own discord id)
* /get-script
  - Gives users a ready-to-use script if they are whitelisted
* /blacklist
  - Blacklist users on the fly
* /un-blacklist
  - Remove Blacklists on the fly
* /update-key-status
  - Update the key status of a user
* /get-logs
  - Get the most recent log entry of a certain user
> More commands coming soon...

## How To Use

To clone and run this application, you'll need [Git](https://git-scm.com) and [Python](https://www.python.org/downloads/) installed on your computer. 
From your command line:

```bash
# Clone this repository
$ git clone https://github.com/xyba1337/LuaGuard-Discord.py-Slash-Commands

# Go into the repository
$ cd LuaGuard-Discord.py-Slash-Commands

# Install dependencies
$ pip3 install -r requirements.txt
# or
$ pip install -r requirements.txt

# Go into config.py and modify everything to your own needs
# FUNCTIONALITY [START]
luawl_token='lua guard api key here'
bot_token='bot token here'
guild_id=guild id here (type int)
buyer_role_id=buyer role id here (type int)
admin_role_id=admin role id here (type int)
script_loadstring='your loadstring here'
# FUNCTIONALITY  [END]

# PERSONALIZATION [START]
script_name='your script name here'
embedcolor=embed color here (type int eg. 0x11038)
thumbnail_url='your thumbnail url here'
# PERSONALIZATION  [END]

# Run the bot
$ python main.py
```

> **Important**
> For an easy configuration and management of roles with payment system, I can highly recommend <a target="blank" href="https://donatebot.io/">donatebot</a>. Unfortunately, only PayPal can be used with it, but this makes it super easy to set up a donator role which will be automatically assigned to someone who has donated.
Below you can see a possible integration config to reduce unneccessary bot calls: 
![Imgur](https://i.imgur.com/MDeauDi.gif)
## Credits

This software uses the following open source packages:

- [Discord.py](https://github.com/Rapptz/discord.py)
- [Luawl.py](https://pypi.org/project/luawl.py/)

## License

MIT

---

> GitHub [@xyba1337](https://github.com/xyba1337) &nbsp;&middot;&nbsp;
> Twitter [@xyba1337](https://twitter.com/xyba1337)

