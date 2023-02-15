
# <p align="center"> Kosame - Discord Bot </p>
![](https://img.shields.io/github/pipenv/locked/dependency-version/ncuphysics/hack_bot/py-cord)
![](https://img.shields.io/bower/l/mi)

--------------
# :file_folder: Prerequisites
* [Pycord](https://docs.pycord.dev/en/stable/installing.html)  
* [Python](https://www.python.org/downloads/) v3 or higher

1. Install python virtual environment
This side project is build under the pipenv. You can click the [pipenv](https://pypi.org/project/pipenv/) or try below commend to install the pipenv:  

```
pip install pipenv
```
 
2. Get your personal token.
Next, get your own token for discord and weather. The discord token can create follow this [page](https://docs.pycord.dev/en/stable/discord.html). The weather api is from [Central Weather Bureau](https://opendata.cwb.gov.tw/dist/opendata-swagger.html), you need to sign to get your own token.  
After the token, edit  `.env`, rename `None` to your token.

```
DISCORD_TOKEN=None
TEST_GUILD_ID=None
```
3. Activate virtual environment and run
```
pipenv shell
python main.py
```
hooray~ your own discord bot is online~~ 