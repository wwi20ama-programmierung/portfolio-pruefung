from logger import Logger

class Room:
    def __init__(self, fileName, logger):
        with open(fileName, 'r') as file:
            self.tiles = [list(line.strip()) for line in file.readlines()]
        self.robotPos = self.find_char('R')
        self.robotBattery = 100
        self.stationPos = self.find_char('S')
        self.logger = logger
        self.tiles[self.roboty()][self.robotx()] = ' '
        self.tiles[self.stationy()][self.stationx()] = ' '

    def height(self):
        return len(self.tiles)

    def width(self):
        return len(self.tiles[0]) if self.height() > 0 else 0

    def robotx(self):
        return self.robotPos[0]
    
    def roboty(self):
        return self.robotPos[1]
    
    def stationx(self):
        return self.stationPos[0]
    
    def stationy(self):
        return self.stationPos[1]

    def find_char(self, c):
        for y in range(self.height()):
            for x in range(self.width()):
                if self.tiles[y][x] == c:
                    return x,y
        return None

    def newRobotPos(self,dx,dy):
        nx = self.robotx() + dx
        ny = self.roboty() + dy
        return nx,ny

    def canMoveRobot(self,dx,dy):
        if abs(dx) > 1 or abs(dy) > 1:
            return False
        nx,ny = self.newRobotPos(dx,dy)
        return nx >= 0 and nx < self.width() and ny > 0 and ny <= self.height() and self.tiles[ny][nx] != 'W' and self.robotBattery > 0

    def moveRobot(self,dx,dy):
        if self.canMoveRobot(dx,dy):
            self.robotPos = self.newRobotPos(dx,dy)
            self.logger.moveRobot(self.robotPos)
        if self.robotPos == self.stationPos:
            self.robotBattery = 10
        else:
            self.robotBattery -= 1
        if self.tiles[self.roboty()][self.robotx()] == 'D':
            self.tiles[self.roboty()][self.robotx()] = ' '
    
    def getRobotSurroundings(self):
        xmin = self.robotx()-1
        xmax = self.robotx()+1
        ymin = self.roboty()-1
        tiles = self.tilesWithMarkers()
        return [tiles[y][xmin:xmax+1] for y in range(ymin, ymin+3)]
    
    def tilesWithMarkers(self):
        result = [line.copy() for line in self.tiles]
        result[self.stationy()][self.stationx()] = 'S'
        result[self.roboty()][self.robotx()] = 'R'
        return result

    def __str__(self):
        return '\n'.join([''.join(line) for line in self.tilesWithMarkers()])

