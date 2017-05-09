class Car(object):
    """
    A car class that can be used to instantiate various vehicles
    Arguments include:
    - type of vehicle
    - model of vehicle
    - name of vehicle
    There are default attributes set for:
    - Number of doors
    - Number of wheels
    - Speed
    """
    def __init__(self, name='General', model='GM', car_type=None):
        self.name = name
        self.model = model
        self.car_type = car_type
        self.num_of_doors = 4
        self.num_of_wheels = 4
        self.speed = 0
        self.setup_properties()

    # Set up the different default car properties: door and number of wheels
    def setup_properties(self):
        two_doors = ['Porshe', 'Koenigsegg']
        if self.name in two_doors:
            self.num_of_doors = 2

        if self.car_type == 'trailer':
            self.num_of_wheels = 8

    # Return car type
    def is_saloon(self):
        return self.car_type != 'trailer'

    # Method to drive car
    def drive(self, speed):
        if self.car_type == 'trailer':
            self.speed = 77
        else:
            self.speed = pow(10, speed)
        return self
