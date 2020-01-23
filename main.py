import time
import sys
from math import sqrt, tan

import cozmo
from cozmo.objects import CustomObject
from cozmo.util import Pose, degrees, radians, speed_mmps, distance_mm

from custom_objects import objects, custom_object_pose
from take_photo import setup_camera, photo
from action_manager import ActionManager

custom_object = None

stops_visited = []


def handle_object_appeared(evt, **kw):
    # Cela sera appelé chaque fois qu'un EvtObjectAppeared est déclanché
    # chaque fois qu'un objet entre en vue
    if isinstance(evt.obj, CustomObject):
        print(f"Cozmo started seeing a type: {str(evt.obj.object_type)} id: {str(evt.obj.object_id)}")

def handle_object_disappeared(evt, **kw):
    # Cela sera appelé lorsqu'un EvtObjectDisappeared est declanché
    # chaque fois qu'un objet est hors de vue.
    if isinstance(evt.obj, CustomObject):
        print(f"Cozmo stopped seeing a {str(evt.obj.object_type)}")

def custom_objects(robot: cozmo.robot.Robot):

    # Gestionnaires d'évennements à chaque fois que Cozmo vois ou arrète de voir un objet
    robot.add_event_handler(cozmo.objects.EvtObjectAppeared, handle_object_appeared)
    robot.add_event_handler(cozmo.objects.EvtObjectDisappeared, handle_object_disappeared)

    # Création des custom objects
    objs = objects(robot)
    if None not in objs:
        print("All objects defined successfully!")
    else:
        print("One or more object definitions failed!")
        return

    robot.say_text("À la recherche des objet").wait_for_completed()
    setup_camera(robot)
    origin = robot.pose
    am = ActionManager(robot)
    stops = 1

    while len(stops_visited) < 6:

        # Chercer les objest
        lookaround = robot.start_behavior(cozmo.behavior.BehaviorTypes.LookAroundInPlace)
        objs = robot.world.wait_until_observe_num_objects(num=1, object_type=CustomObject, timeout=60)
        lookaround.stop()

        if objs[0].object_type in stops_visited:
            continue

        stops_visited.append(objs[0].object_type)

        robot.say_text("Objet trouvé").wait_for_completed()

        if len(objs) > 0:

            photo(robot)

            pose = custom_object_pose(robot, objs[0])
            robot.go_to_pose(pose, relative_to_robot=False).wait_for_completed()

            photo(robot)

            robot.say_text(f"Arrête {stops}").wait_for_completed()
            am.launch(objs[0])

            print("origin: ", origin)
            robot.go_to_pose(origin, relative_to_robot=False).wait_for_completed()
            stops += 1

        else:
            print("Cannot locate custom box")

    robot.play_anim_trigger(cozmo.anim.Triggers.SparkSuccess).wait_for_completed()

    while True:
        time.sleep(0.1)

cozmo.run_program(custom_objects, use_3d_viewer=True, use_viewer=True)