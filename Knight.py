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