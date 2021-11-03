import random
import cassiopeia
import discord

from dotenv import load_dotenv
load_dotenv()
import os


def leaguesearch(username:str):
    cassiopeia.set_riot_api_key (os.getenv("RIOT_KEY"))
    summoner = cassiopeia.get_summoner(name = username, region = "NA")
    level = summoner.level
    name = summoner.name
    rank = summoner.ranks
    print(type(rank))
    return(f"{name} is level {level}")
