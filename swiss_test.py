import sys, os

class Groups:
    def __init__(self) -> None:
        self.num_people = 0
        self.lst_players = []
        self.meets = {}
        self.scores = {}
    def AddPlayers(self, name) -> int:
        for names in self.lst_players:
            if name == names:
                print("동명이인이 있습니다. 입력을 취소합니다.\n")
                return 1
        self.lst_players.append(name)
        self.num_people += 1
        self.meets[name] = []
        self.scores[name] = 0
        return 0
    def GetPlayersList(self) -> list:
        return self.lst_players
    def GetMeets(self) -> dict:
        return self.meets
    def GetPlayerMeets(self, name):
        try:
            lst_meets = self.meets[name]
            return lst_meets
        except KeyError:
            print("잘못된 성함을 입력하셨습니다.\n")
            return {}
    def GetNumofPlayers(self) -> int:
        return self.num_people
    def GetDictScore(self) -> dict:
        return self.scores
    def GetPlayerScore(self, name) -> int:
        try:
            score = self.scores[name]
            return score
        except KeyError:
            print("잘못된 성함을 입력하셨습니다.\n")
            return 0