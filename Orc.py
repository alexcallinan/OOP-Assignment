class Being:
    def __init__(self,name,skill,weapon,species):
        self._name=name
        self._skill=skill
        self._weapon=weapon
        self._species=species

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,name):
        self._name=name

    @property
    def skill(self):
        return self._skill
    @skill.setter
    def skill(self,skill):
        if skill <0:
            print('Invalid skill level')
        else:
            self._skill=int(skill)
    @property
    def weapon(self):
        return self._weapon
    @weapon.setter
    def weapon(self,weapon):
        if weapon== None:
            self._weapon=False
        else:
            self._weapon=weapon
    @property
    def species(self):
        return self._species
    @species.setter
    def species(self,species):
        self._species=species

    skill_increase=1.05

    def __gt__(self, other):
        if self._weapon and other._weapon == False:
            if self._strength > other._strength:
                print(self._name, 'Wins')
                self._skill *= Being.skill_increase
            else:
                print(other._name, 'Wins')
                other._skill *= Being.skill_increase
        if self._weapon and other._weapon == True:
            if self._skill > other._skill:
                print(self._name, 'Wins')
                self._skill *= Being.skill_increase
            else:
                print(other._name, 'Wins')
                other._skill *= Being.skill_increase
        if self._weapon == True and other._weapon == False:
            print(self._name, 'Wins')
            self._skill *= Being.skill_increase
        if self._weapon == False and other._weapon == True:
            print(other._name, 'Wins')
            other._skill *= Being.skill_increase
    def __str__(self):
         return('%s %d %s %s',(self._name,self._skill,self._weapon,self._species))


class Orcs(Being):
    def __init__(self,name,skill,strength,weapon=None,species='Orc'):
        Being.__init__(self,name,skill,weapon,species)
        self._strength=strength
    @property
    def strength(self):
        return self._strength
    @strength.setter
    def strength(self,strength):
        if strength<0:
            print('Invalid strength level')
        else:
            self._strength=strength

    def fight(self,other):
        return self.__gt__(other)

class Knights(Being):
    def __init__(self,name,skill,weapon,kingdom,lead=[],species='Knight'):
        Being.__init__(self,name,skill,weapon,species)
        self._kingdom=kingdom
        self._lead=lead

    def get_kingdom(self):
        return self._kingdom
    def set_kingdom(self,kingdom):
        if kingdom == None:
            print(self._name,'must be in a kingdom')
        else:
            self._kingdom= kingdom

    def get_lead(self):
        print(self._lead)
    def set_lead(self,arch):
        lead=[]
        self._lead=lead.append(arch)
    kingdom= property(get_kingdom, set_kingdom)
    lead=property(get_lead,set_lead)
    def fight(self,other):
        if self._species and other._species != 'Orc':
            print('Knights and archers may only fight Orcs')
        if self._weapon == False:
            print('Knights and Arcgers must have weapons to fight')
        else:
            return self.__gt__(other)

class Archers(Knights):
    def __init__(self, name, skill, weapon, kingdom,species='Archer'):
        Knights.__init__(self, name, skill, weapon, kingdom,species)


def db(creature):
    import shelve
    if creature._species == 'knight':
            k=shelve.open('Knightdb')
            k[creature._name]=creature._name,'knight'
            k.close()
    if creature._species== 'archer':
            a=shelve.open('Archerdb')
            a[creature._name]=creature._name,'archer'
            a.close()
    if creature._species=='orc':
            o=shelve.open('Orcdb')
            o[creature._name]=creature._name,'orc'
            o.close()
s=Knights('tim',5,'sword','gondor')



#s.set_lead('k')
#s.get_lead()




