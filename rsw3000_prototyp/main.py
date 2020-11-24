from room import Room
from robot import Robot
from logger import Logger

def main():
    robby = Robot()
    logger = Logger()
    room = Room("testfiles/room1.txt", logger)

    # Raum vor dem Start ausgeben:
    print(room)

    # Roboter laufen lassen, bis er fertig ist
    while not robby.done:
        dx, dy = robby.step(room.getRobotSurroundings())
        room.moveRobot(dx,dy)
    
    # Raum nach dem Ende ausgeben:
    print(room)

    # Log ausgeben:
    print(room.logger.positionHistory)

main()
