class Robot:
    """
    A class representing a robot that takes in parameters for ID, name, battery, and type.
    """
    # Initializing RobotID, name, battery, and type
    def __init__(self, RobotID, name, battery, type):
        self._RobotID = RobotID
        self._name = name
        self._battery = battery
        self._type = type

    # Getters for attributes
    def get_ID(self):
        return self._RobotID

    def get_name(self):
        return self.name

    def get_battery(self):
        return self.battery

    def get_type(self):
        return self.type

    # Setters for attributes
    def set_ID(self, RobotID):
        self._RobotID = RobotID

    def set_name(self, name):
        self.name = name

    def set_battery(self, battery):
        self.battery = battery

    def set_type(self, type):
        self.type = type

    def perform_task(self, task):
        print(f"{self.name} is performing task: {task}")

    # Returning robot str sentence
    def __str__(self):
        return f"Robot ID: {self._RobotID}, Name: {self.name}, Battery: {self.battery}, Type: {self.type}"

class RoboticArm(Robot):
    """
    A class representing a robotic arm that takes in an additional parameter for arm length.
    """

    # Initializing ID, name, battery, type, armlength
    def __init__(self, ID, name, battery, type, arm_length):
        super().__init__(ID, name, battery, type)
        self._arm_length = arm_length

    # Getters and setters for arm length
    def get_arm_length(self):
        return self._arm_length

    def set_arm_length(self, arm_length):
        self._arm_length = arm_length

    # Specialized task to preform (with Arm Length)
    def perform_task(self, task):
        print(f"{self._name} is performing task: {task} with arm length: {self._arm_length}")

class DeliveryRobot(Robot):
    """
    A class representing a delivery robot that takes in an additional parameter for maximum speed.
    """

    # Initializing RobotID, name, battery, type, and maxspeed
    def __init__(self, RobotID, name, battery, type, max_speed):
        super().__init__(RobotID, name, battery, type)
        self._max_speed = max_speed

    # Getters and setters for maxspeed
    def get_max_speed(self):
        return self.max_speed

    def set_max_speed(self, max_speed):
        self.max_speed = max_speed

    # Specialized task to preform (with Max Speed)
    def perform_task(self, task):
        print(f"{self._name} is performing task: {task} at max speed: {self._max_speed}")

class sensor:
    """
    A class representing a sensor that takes in parameters for sensor type and value.
    """
    
    # Initializing sensor type and value
    def __init__(self, sensor_type, value):
        self._sensor_type = sensor_type
        self._value = value

    # Getters and setters for sensor type and value 
    def get_sensor_type(self):
        return self._sensor_type

    def get_value(self):
        return self._value

    def set_sensor_type(self, sensor_type):
        self._sensor_type = sensor_type

    def set_value(self, value):
        self._value = value
 
def main():
    Feature = input("Enter a robot feature to test (Check sensors, Run tasks, Check battery, Add Robot, Update Robot) or enter \"Done\": ")
    
    # Run loop until user types done
    while Feature != "Done":

        # If statement for each feature
        # Printing kind of sesnor and what its value was depending on user input
        if Feature == "Check sensors":
            sensor_type = input("Enter sensor type: ")
            value = input("Enter sensor value: ")
            new_sensor = sensor(sensor_type, value)
            print(f"Sensor Type: {new_sensor.get_sensor_type()}, Value: {new_sensor.get_value()}")

        # Running tasks for specific type of robot
        # Entering info about robot to create a robot
        elif Feature == "Run tasks":
            robot_type = input("Enter robot type (RoboticArm or DeliveryRobot): ")
            ID = input("Enter robot ID: ")
            name = input("Enter robot name: ")
            battery = input("Enter robot battery: ")
            type = input("Enter robot type: ")
            if robot_type == "RoboticArm":
                arm_length = input("Enter arm length: ")
                new_robot = RoboticArm(ID, name, battery, type, arm_length)
                task = input("Enter task to perform: ")
                new_robot.perform_task(task)
            elif robot_type == "DeliveryRobot":
                max_speed = input("Enter max speed: ")
                new_robot = DeliveryRobot(ID, name, battery, type, max_speed)
                task = input("Enter task to perform: ")
                new_robot.perform_task(task)

        # Checking battery for robots added
        # Printing robot and battery level based on ID
        elif Feature == "Check battery":
            ID = input("Enter robot ID to check battery: ")
            print(f"Checking battery for Robot ID: {ID}")
            print(f"Battery level for Robot ID {ID}: {battery}")

        # Adding robot 
        # Printing new robot for input user entered
        elif Feature == "Add Robot":
            robot_type = input("Enter robot type (RoboticArm or DeliveryRobot): ")
            ID = input("Enter robot ID: ")
            name = input("Enter robot name: ")
            battery = input("Enter robot battery: ")
            type = input("Enter robot type: ")
            if robot_type == "RoboticArm":
                arm_length = input("Enter arm length: ")
                new_robot = RoboticArm(ID, name, battery, type, arm_length)
                print(f"Added Robotic Arm with ID: {ID}, Name: {name}, Battery: {battery}, Type: {type}, Arm Length: {arm_length}")
            elif robot_type == "DeliveryRobot":
                max_speed = input("Enter max speed: ")
                new_robot = DeliveryRobot(ID, name, battery, type, max_speed)
                print(f"Added Delivery Robot with ID: {ID}, Name: {name}, Battery: {battery}, Type: {type}, Max Speed: {max_speed}")
        
        # Updating Robot
        # Updating name, battery, type, speed based on robot ID
        elif Feature == "Update Robot":
                new_robot_type = input("Enter robot (DeliveryRobot or RoboticArm): ")
                print(new_robot_type)
                if new_robot_type == "RoboticArm":   
                    robot_update = input("Choose a Robot to update (ID): ")   
                    print(f"Updating Robot: {robot_update}")
                    update_name = input("Enter Robot new name: ")
                    update_battery = input("Enter robot battery: ")
                    update_type = input("Enter new Robot type: ")
                    print(f"Robot Type: {update_type}, Robot ID: {ID}, Robot name: {update_name}, Robot battery: {update_battery}, Robot type: {robot_type}, Robot arm length: {arm_length}")
                elif new_robot_type == "DeliveryRobot":
                    robot_update = input("Choose a Robot to update (ID): ")
                    print(f"Updating Robot: {robot_update}")
                    update_name = input("Enter Robot new name: ")
                    update_battery = input("Enter Robot new battery: ")
                    update_robot_speed = input("Enter new Robot speed: ")
                    update_type = input("Enter new Robot type: ")
                    print(f"Robot Type: {update_type}, Robot ID: {ID}, Robot name: {update_name}, Robot battery: {update_battery}, Robot type: {robot_type}, Robot speed: {update_robot_speed}")
                else: 
                    print("Invalid Robot.")
        
        Feature = input("Enter a robot feature to test (Check sensors, Run tasks, Check battery, Add Robot, Update Robot) or enter \"Done\": ")
main()