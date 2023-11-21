class Spaceship():
    
    #class variable - static variable
    toughness = 0.8

    def __init__(self,name=None):
        if name is None:
            self.callSign = "Nameless spaceship"
            self._shieldStrength = 100
        else:
            self.callSign = name
            self._shieldStrength = 100

    #methods
    def fireMissile(self):
        return "Pew!"
    
    def reduceShield(self, amount):
        self._shieldStrength -= amount
    
    #static method
    def increaseDifficulty(t):
        Spaceship.toughness += t


#instantiation
myShip = Spaceship()
print(myShip.callSign)
print(Spaceship.toughness)
Spaceship.increaseDifficulty(0.2)
print(Spaceship.toughness)