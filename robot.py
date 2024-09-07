class Robot:
    COMPASS = {
        0:   'north',
        45:  'northeast',
        90:  'east', 
        135: 'southeast', 
        180: 'south',
        225: 'southwest',
        270: 'west',
        315: 'northwest'
    }

    ANGLE_STEP = 45

    def __init__(self, id: int, point: int) -> None:
        self.id = id
        self.point = point

    # ensures result of direction calculation below is between 0 and 360
    def circle(self, angle: int):
        return angle % 360

    def turn(self, direction: str, point: int):
        # turn robot and determine which direction it's facing
        if direction == 'RIGHT':
            point += Robot.ANGLE_STEP
        else:
            point -= Robot.ANGLE_STEP

        point = self.circle(point)

        return point
    
    # rounding to nearest mutliple of 45 to correspond to 8 directions, remove if more precision is developed. 
    def round(self, round_point):
        return Robot.ANGLE_STEP*(round(round_point/Robot.ANGLE_STEP,0))
    
    def get_current_direction(self):
        return Robot.COMPASS[self.round(self.point)]


def main():

    i = 0

    new = 1

    robotMap = {}

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
                num = len(robotMap)
                robotMap[num] = Robot(len(robotMap), 0)
                currentRobot = robotMap[num]
            
            # check if at least one robot
            elif iRobot == 'NO' and len(robotMap) == 0:
                print('There are currently no robots created. I will create one for you.\n')                
                num = len(robotMap)
                robotMap[num] = robot(len(robotMap), 0)
                currentRobot = robotMap[num]

        print('--------------------------')
        print('Robot', currentRobot.id, 'is currently facing ' + currentRobot.get_current_direction())
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
                print('Robot', currentRobot.id, 'is currently facing '  + currentRobot.get_current_direction())
                moveAgain = input('Move again, or create a new robot?\n1. Move again\n2.Create a new robot\n')

                while moveAgain != '1' and moveAgain != '2':
                    print('--------------------------')
                    moveAgain = input('Invalid repsonse. Move again, or create a new robot?\n1. Move again\n2. Create a new robot\n')


                if moveAgain == '2':
                    new = 1
                else:
                    new = 0    


main()
