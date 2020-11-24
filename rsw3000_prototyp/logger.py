class Logger:
    def __init__(self):
        self.positionHistory = []
    
    def moveRobot(self, nextPos):
        self.positionHistory += [nextPos]