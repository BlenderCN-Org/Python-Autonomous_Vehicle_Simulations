Segway RMP 400 platform
=======================

The base of the **MANA** robot at LAAS.

This robot uses the Physics Constraints in Blender to allow the wheels to
behave more realistically. The wheels turn as the robot moves, and they have
``Rigid Body`` physics, so that they can also have collisions with nearby
objects.

It has four differential drive wheels, with the pairs of wheels on each side
always moving at the same speed. Since the wheels of this robot use the
``Rigid Body`` physics, it must be controlled with the :doc:`v_omega_diff_drive
<../actuators/v_omega_diff_drive>` actuator.

.. warning::
  Because of the physics constraints used in this robot, its wheels must NOT be
  children of the robot when the simulation is started. To properly include an
  RMP 400 robot in a scene, it must be done using a special class of the
  Builder API, and then calling a method to unparent the wheels from the robot.
  See below for an example.

.. image:: ../../../media/robots/segwayrmp400.png 
  :align: center
  :width: 600

Files
-----

- Blender: ``$MORSE_ROOT/data/robots/segwayrmp400.blend``
- Python: ``$MORSE_ROOT/src/morse/robots/segwayrmp400.py``


Adjustable parameters
---------------------

These parameters are inherent to the Blender model for the robot, and must be
modified directly in the Blender file:

- The **Mass** of the robot can be changed in the **Properties >> Physics**
  panel
- The **Friction** coefficient of the robot can be adjusted in the
  **Properties >> Material** panel


Example in Builder API
----------------------

To add a Segway RMP 400 robot, it is necessary to use the ``WheeledRobot``
class. Also, after giving any transformations to the robot (translation or
rotation), you **MUST** call the method ``unparent_wheels`` of the robot
instance. Otherwise the robot will not move.

.. code-block:: python

    from morse.builder import *

    # Append Segway robot to the scene
    robot = SegwayRMP400()
    robot.rotate(z=0.73)
    robot.translate(x=-2.0, z=0.2)
    robot.unparent_wheels()

Another restriction with this kind of robots is that for any additional
components added to it, translations and rotations must be applied before
parenting them to the robot.

**WRONG:**

.. code-block:: python

    pose = Pose()
    robot.append(pose)
    pose.translate(x=0.5, y=0.1, z=0.4)
    pose.rotate(x=1.57)

**RIGHT:**

.. code-block:: python

    pose = Pose()
    pose.translate(x=0.5, y=0.1, z=0.4)
    pose.rotate(x=1.57)
    robot.append(pose)


Configurable parameters
-----------------------

The robot itself has several properties that describe its physical behaviour.
None of these properties have an effect in the current version of the robot,
but may be used in future releases.
These can be changed using the Builder API:

- **HasSuspension**: (Boolean) flag that determines if the wheels move
  independently of the body of the robot. For the case of the Segway RMP 400,
  this should always be ``False``
- **HasSteering**: (Boolean) flag
  that determines if the wheels turn independently of the body of the robot.
  For the case of the Segway RMP 400, this should always be ``False``
- **Influence**: (double)
- **Friction**: (double)
- **FixTurningSpeed**:(double) Overwrite the value of the distance between
  wheels in the computations of the wheel speeds. This effectively changes the
  turning speed of the robot, and can be used to compensate for the slip of the
  wheels while turning.
  The real distance between wheels in the robot is 0.624m. By forcing a
  distance of 1.23m, the robot will turn over a smaller radius, as would a two
  wheeled differential drive robot.
  Leaving this value as 0.0 (the default) will use the real distance between
  wheels

