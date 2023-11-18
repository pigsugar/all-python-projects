class score ():
    def __init__(self):
        self.__score = 1
        
    def update(self):
        print(self.__score)
        
    def updatescore(self):
        self.__score = self.__score + 1
        print (self.__score)
        
player = score()
player.score = 100
player.updatescore()
player.updatescore()