

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
    degree_turn = 45

    def __init__(self, point = 0) -> None:
        self.point = point

    # ensures result of direction calculation below is between 0 and 360
    def circle(self):
        self.point %= 360

    # turn robot left
    def turn_left(self):
        self.point -= Robot.degree_turn
        self.circle()
        print(f'Now facing {Robot.COMPASS[self.point]}\n')

    # turn robot right
    def turn_right(self):
        self.point += Robot.degree_turn
        self.circle()
        print(f'Now facing {Robot.COMPASS[self.point]}\n')


def main():
    robot_dict = {}
    print('Activating robot...\n')
    # start with a robot
    robot_dict['0'] = Robot()
    current_robot = robot_dict['0']

    # allowed commands from user
    command_list = ['L', 'R', 'E']

    while True: 
        user_action = input('What would you like to do?\n').upper()
        # digit entered either activates that robot or creates and activates a new one
        if user_action.isdigit():
            if user_action not in robot_dict.keys():
                robot_dict[user_action] = Robot()
                print(f'Robot {user_action} created.')

            print(f'Now controlling robot {user_action}\n')
            current_robot = robot_dict[user_action]
            
        elif user_action not in command_list:
            print('Invalid command\n')

        elif user_action == 'L':
            current_robot.turn_left()

        elif user_action == 'R':
            current_robot.turn_right()

        elif user_action == 'E':
            print('Exiting...')
            break

main()
