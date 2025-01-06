"""Module providing a function printing python version."""
class Robot:
    """Robot base class"""

    def __init__(self, name):
        """constructor"""
        self.name = name
        self.position = [0,0]
        print("My name is", self.name)

    def walk(self, x):
        """function moving the robot to given position"""
        self.position[0] = self.position[0]+x
        print("New position:", self.position)

def main():
    """Program entry point"""
    my_robot = Robot("Adam")
    print(my_robot.name)

    my_robot.walk(10)
    print(my_robot.position)

main()
