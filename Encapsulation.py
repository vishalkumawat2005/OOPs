# Encapsulation
class Data:
    def __init__(self,name,team):
        self.name=name
        self.team=team
    def info(self):
        return f"my name is {self.name},and team {self.team}"
team1="A"
team2="B"
d1=Data("vishal",team1)
print(d1.info())
