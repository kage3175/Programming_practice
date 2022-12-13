class pokemon:
    def __init__(self):
        self.version=' '
        self.name=' '
        self.number=' '
        self.type1=' '
        self.type2=' '
        self.hp=0
        self.attack=0 #공격
        self.block=0 #방어
        self.contact=0 #특공
        self.defense=0 #특방
        self.speed=0
        self.level=1
    def Put_values(self, hp, atk, blo, con, deff, spe, lvl, name, version, number,type1, type2):
        self.hp=hp
        self.attack=atk
        self.block=blo
        self.contact=con
        self.defense=deff
        self.speed=spe
        self.level=lvl
        self.name=name
        self.version=version
        self.number=number
        self.type1=type1
        self.type2=type2
    def Get_types(self):
        if self.type2!=' ':
            return self.type1, self.type2
        else:
            return self.type1, 'NULL'


def main():
    file=open("pokemon_type.txt", "r")
