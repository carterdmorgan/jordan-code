class robot:
    def __init__(self, idNumber: int, iPoint: int) -> None:
        self.ID = idNumber
        self.point = iPoint

    # ensures result of direction calculation below is between 0 and 360
    def circle(self, angle: int):
        return angle % 360

    def turn(self, direction: str, dPoint: int):
        # turn robot and determine which direction it's facing
        if direction == 'RIGHT':
            dPoint += 45
        else:
            dPoint -= 45

        dPoint = self.circle(dPoint)

        return dPoint
    
    # rounding to nearest mutliple of 45 to correspond to 8 directions, remove if more precision is developed. 
    def round(self, roundPoint):
        return 45*(round(roundPoint/45,0))


def main():

    i = 0

    new = 1

    compass = {
        0:   'north',
        45:  'northeast',
        90:  'east', 
        135: 'southeast', 
        180: 'south',
        225: 'southwest',
        270: 'west',
        315: 'northwest'
    }

    robotList = {}

    currentRobot = 0

    # allowed commands
    list = ['LEFT', 'RIGHT', 'EXIT']

    while i == 0:

        # activates if user has selected to build a new robot, or if no robots have been built
        if new == 1:
            iRobot = input('Would you like to create a robot? Type "YES" or "NO"\n').upper()
            while iRobot != 'YES' and iRobot != 'NO':
                iRobot = input('Invalid response. Would you like to create a robot? Type "YES" or "NO"\n').upper()

            if iRobot == 'YES':
                num = len(robotList)
                robotList[num] = robot(len(robotList), 0)
                currentRobot = robotList[num]
            
            # check if at least one robot
            elif iRobot == 'NO' and len(robotList) == 0:
                print('There are currently no robots created. I will create one for you.\n')                
                num = len(robotList)
                robotList[num] = robot(len(robotList), 0)
                currentRobot = robotList[num]

        print('--------------------------')
        print('Robot', currentRobot.ID, 'is currently facing ' + compass[currentRobot.point])
        direction = input('Please enter a direction: LEFT or RIGHT, or EXIT to quit.\n').upper()
        if direction == 'EXIT':
            i = 1

        else:

            # check if command is allowed
            while direction not in list:
                print('--------------------------')
                direction = input('Please enter a valid direction: LEFT or RIGHT, or EXIT to quit.\n').upper()

            if direction == 'EXIT':
                i = 1

            else:
                currentRobot.point = currentRobot.turn(direction, currentRobot.point)
                roundPoint = round(currentRobot.point)

                print('--------------------------')
                print('Robot', currentRobot.ID, 'is currently facing '  + compass[roundPoint])
                moveAgain = input('Move again, or create a new robot?\n1. Move again\n2.Create a new robot\n')

                while moveAgain != '1' and moveAgain != '2':
                    print('--------------------------')
                    moveAgain = input('Invalid repsonse. Move again, or create a new robot?\n1. Move again\n2. Create a new robot\n')


                if moveAgain == '2':
                    new = 1
                else:
                    new = 0    


main()
