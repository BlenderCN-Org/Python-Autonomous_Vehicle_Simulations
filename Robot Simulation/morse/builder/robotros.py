from morse.builder import*

# Uploads the robot.
atrv = ATRV()

# Sets the position of the robot.
pose = Pose()
pose.translate(z = 0.75)
atrv.append(pose)

# Allows the velocity and angular velocity of the robot to be manipulated.
motion = MotionVW()
atrv.append(motion)

# Configures the socket middleware that can be changed to ROS.
motion.add_default_interface('ros')
pose.add_default_interface('ros')

# Creates the environment for the robot to function in.
env = Environment('outdoors.blend')
# Adds the camera and varies its angle.
env.place_camera([5,-5,6])
env.aim_camera([1.0470,0,0.7854])