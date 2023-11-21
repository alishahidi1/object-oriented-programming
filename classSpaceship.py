class Spaceship():
    def __init__(self):

        #instace variables
        self.callSign = ''
        self._shieldStrength = 100

        #methods
        def fireMissile(self):
            return "Pew!"
        
        def reduceShield(self, amount):
            self._shieldStrength -= amount
        

#instantiation
myShip = Spaceship()