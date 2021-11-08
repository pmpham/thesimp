import random
import cassiopeia
from cassiopeia.core import summoner
import discord
import json
import requests

from dotenv import load_dotenv
load_dotenv()
import os

riotkey = os.getenv("RIOT_KEY")
def leaguesearch(username:str):
    cassiopeia.set_riot_api_key (riotkey)
    summoner = cassiopeia.get_summoner(name = username, region = "NA")
    level = summoner.level
    name = summoner.name
    rank = summoner.ranks
    return(f"{name} is level {level}")

class player(str):

    def __init__(self,username:str):
        self.name = username
        self.puuid = ""
        self.summonerid = ""
        self.level = ""
        self.tier = ""
        self.rank =""
        self.lp =""
        self.fullrank = ""
        self.wins = 0
        self.losses = 0
        self.wr = ""

    def summonerv4search(self,username:str):
        url = (f"https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{self.name}?api_key={riotkey}")
        response = json.loads(requests.get(url).text)
        message = ""
        try:
            message = (response["status"])["message"]
        except KeyError:
            pass
        if message == "":
            self.name = response["name"]
            self.puuid = response["puuid"]
            self.summonerid = response["id"]
            self.level = response ["summonerLevel"]


    def leaguev4search(self,summonerid:str):
        if self.summonerid == "":
            return False
        else:
            url = (f"https://na1.api.riotgames.com/lol/league/v4/entries/by-summoner/{self.summonerid}?api_key={riotkey}")
            response = json.loads(requests.get(url).text)   
            message = ""
            try:
                message = (response[0])[0]
                
            except KeyError:
                pass
            if message == "":
                
                if response[0]["queueType"] == "RANKED_SOLO_5x5":
                    response = response[0]
                    self.tier = response ["tier"]
                    self.rank = response["rank"]
                    self.lp = response ["leaguePoints"]
                    self.fullrank = f"{self.tier} {self.rank} {self.lp} LP"
                    self.wins = response["wins"]
                    self.losses = response["losses"]
                    self.wr = f"{self.wins}W: {self.losses}L"
                else:
                    response = response[1]
                    response = response[0]
                    self.tier = response ["tier"]
                    self.rank = response["rank"]
                    self.lp = response ["leaguePoints"]
                    self.fullrank = f"{self.tier} {self.rank} {self.lp} LP"
                    self.wins = response["wins"]
                    self.losses = response["losses"]
                    self.wr = f"{self.wins}W: {self.losses}L"

    def tftv1search(self,summonerid:str):
        if self.summonerid == "":
            return False   
        else:
            url = (f"https://na1.api.riotgames.com/tft/league/v1/entries/by-summoner/{self.summonerid}?api_key={riotkey}")  
            response = json.loads(requests.get(url).text)   
            message = ""
            try:
                message = (response[0])[0]
            except KeyError:
                pass
            if message == "":
                response = response[0]
                self.tier = response ["tier"]
                self.rank = response["rank"]
                self.lp = response ["leaguePoints"]
                self.fullrank = f"{self.tier} {self.rank} {self.lp} LP"
                self.wins = response["wins"]
                self.losses = response["losses"]
                self.wr = f"{self.wins}W: {self.losses}L"

    def newleaguesearch(self):
        self.summonerv4search(self.name)
        self.leaguev4search(self.summonerid)
        if self.puuid != "":
            return(f"{self.name} is {self.fullrank}, {self.wr}")
        else:
            return(f"not a valid name:{self.name}")
    
    def tftsearch(self):
        self.summonerv4search(self.name)
        self.tftv1search(self.summonerid)
        if self.puuid != "":
            return(f"{self.name} is {self.fullrank}, {self.wr}")
        else:
            return(f"not a valid name:{self.name}")


