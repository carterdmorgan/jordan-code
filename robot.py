



class Robot:

    COMPASS = {
        0:   'north',
        45:  'northeast',
        90:  'east',
        135: 'southeast',
        180: 'south',
        225: 'southwest',
        270: 'west'
    }

    MOVEMENT_DICT = {
        0:   (0, 1),
        90:  (1, 0),
        180: (0, -1),
        270: (-1, 0)
    }

    # turn expressed as degrees of a circle
    ANGLE_TURN = 90

    # amount of spaces a move forward moves

    FORWARD_MOVEMENT = 2

    ALLOWED_COMMANDS = ['l', 'r', 'f', 'e']
    
    def __init__(self, direction = 0, position = [0,0]) -> None:
        self.direction = direction
        self.position = position

    def turn_left(self):
        self.direction -= Robot.ANGLE_TURN
        self.direction %= 360

    def turn_right(self):
        self.direction += Robot.ANGLE_TURN
        self.direction %= 360

    def get_cardinal(self):
        return Robot.COMPASS[self.direction]

    def move_forward(self):
        move_x, move_y = Robot.MOVEMENT_DICT.get(self.direction, (0,0))
        self.position[0] += move_x * Robot.FORWARD_MOVEMENT
        self.position[1] += move_y * Robot.FORWARD_MOVEMENT


def main():

    def get_key(d: dict, val: Robot):
        for key, value in d.items():
            if value == val:
                return key

    robot_dict = {'0': Robot()}
    current_robot = robot_dict['0']
    current_robot_ID = get_key(robot_dict, current_robot)
    current_robot_direction = Robot.get_cardinal(current_robot)

    print('Activating robot...\n')
    print('-------------------')
    print(f'Now controlling Robot {current_robot_ID}. Robot {current_robot_ID} is facing {current_robot_direction}\n')

    while True:
        user_action = input('Select an option:\nMove forward: f\nturn left: l\nturn right: r\nexit: e\ncreate new robot: enter any number\n').lower()
        if user_action.isdigit() == True:
            if user_action in robot_dict.keys():
                current_robot = robot_dict[user_action]
            elif user_action not in robot_dict.keys():
                robot_dict[user_action] = Robot()
                current_robot = robot_dict[user_action]
                current_robot_ID = get_key(robot_dict, current_robot)
                current_robot_direction = Robot.get_cardinal(current_robot)
            print('Activating robot...\n')
            print('-------------------')
            print(f'Now controlling Robot {current_robot_ID}. Robot {current_robot_ID} is facing {current_robot_direction}\n')
        elif user_action not in Robot.ALLOWED_COMMANDS:
            print('invalid command')
        elif user_action == 'l':
            current_robot.turn_left()
            cardinal = current_robot.get_cardinal()
            print(f'Turned left. Robot {current_robot_ID} is now facing {cardinal}')
            print('-------------------')
        elif user_action == 'r':
            current_robot.turn_right()
            cardinal = current_robot.get_cardinal()
            print(f'Turned right. Robot {current_robot_ID} is now facing {cardinal}')
            print('-------------------')
        elif user_action == 'f':
            current_robot.move_forward()
            cardinal = current_robot.get_cardinal()
            print(f'Moved forward. Robot {current_robot_ID} is at position {current_robot.position}')
            print(f'Robot {current_robot_ID} is facing {cardinal}')
            print('-------------------')
        elif user_action == 'e':
            print('exiting...')
            break

main()


    