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

    def __init__(self, point = 0) -> None:
        self.point = point

    # ensures result of direction calculation below is between 0 and 360
    def circle(self):
        self.point % 360
    
    def turn_right(self) -> None:
        self.point += Robot.ANGLE_STEP
        self.circle()
    
    def turn_left(self) -> None:
        self.point -= Robot.ANGLE_STEP
        self.circle()

    # rounding to nearest mutliple of 45 to correspond to 8 directions, remove if more precision is developed. 
    def round(self, round_point):
        return Robot.ANGLE_STEP*(round(round_point/Robot.ANGLE_STEP,0))
    
    def get_current_direction(self):
        return Robot.COMPASS[self.round(self.point)]


def main():
    robot_map = {}
    current_robot = Robot()
    current_key = '0'
    robot_map[current_key] = current_robot

    # allowed commands
    valid_commands = ['L', 'R', 'Q']

    while True:
        current_input = input('What would you like to do?\n')
        if current_input.isdigit():
            # TODO: Initialize new robot
            print("valid digit command")
        elif current_input in valid_commands:
            if current_input == "L":
                current_robot.turn_left()
            elif current_input == "R":
                current_robot.turn_right()
            elif current_input == "Q":
                break

            print(f"Robot {current_key} is facing {current_robot.get_current_direction()}")
        else:
            print("Invalid command. Please try again.")
    
    print("Robot shutting down.")


main()
