import logging; logger = logging.getLogger("morse." + __name__)
import morse.core.actuator
from morse.helpers.components import add_data

class MotionXYW(morse.core.actuator.Actuator):
    """
    This actuator reads the values of forwards movement x, sidewards
    movement y and angular speed w and applies them to the robot as
    direct translation. This controller is supposed to be used with
    robots that allow for sidewards movements.
    """

    _name = 'Linear and angular speed (Vx, Vy, W) actuator'

    _short_desc = 'Motion controller using linear and angular speeds'

    add_data('x', 0.0, 'float',
             'linear velocity in x direction (forward movement) (m/s)')
    add_data('y', 0.0, 'float',
             'linear velocity in y direction (sidewards movement) (m/s)')
    add_data('w', 0.0, 'float', 'angular velocity (rad/s)')

    def __init__(self, obj, parent=None):
        logger.info('%s initialization' % obj.name)
        # Call the constructor of the parent class
        super(self.__class__, self).__init__(obj, parent)

        logger.info('Component initialized')



    def default_action(self):
        """ Apply (x, y, w) to the parent robot. """

        # Reset movement variables
        vx, vy, vz = 0.0, 0.0, 0.0
        rx, ry, rz = 0.0, 0.0, 0.0

        # Scale the speeds to the time used by Blender
        try:
            vx = self.local_data['x'] / self.frequency
            vy = self.local_data['y'] / self.frequency
            rz = self.local_data['w'] / self.frequency

        # For the moment ignoring the division by zero
        # It happens apparently when the simulation starts
        except ZeroDivisionError:
            pass
        # Get the Blender object of the parent robot
        parent = self.robot_parent.bge_object

        # Give the movement instructions directly to the parent
        # The second parameter specifies a "local" movement
        parent.applyMovement([vx, vy, vz], True)
        parent.applyRotation([rx, ry, rz], True)
        
