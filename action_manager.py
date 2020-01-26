import time
from PIL import Image

import cozmo
from cozmo.util import degrees, distance_mm, speed_mmps
from cozmo.objects import CustomObjectTypes
from cozmo.anim import Triggers
import random

class ActionManager:

    def __init__(self, robot: cozmo.robot.Robot):
        self.robot = robot

    def launch(self, custom_object):
        switcher={
            CustomObjectTypes.CustomType00: self.roll_cube,
            CustomObjectTypes.CustomType01: self.play_animation,
            CustomObjectTypes.CustomType02: self.star_wars_performance,
            CustomObjectTypes.CustomType03: self.stack_cubes,
            CustomObjectTypes.CustomType04: self.darth_vader_performance,
            CustomObjectTypes.CustomType05: self.display_image,
        }
        func=switcher.get(custom_object.object_type, lambda :"Invalid type")
        return func()

    def display_image(self, image="ETS-blanc.png"):
        print("** Display image on OLED face ***")

        # Open image file
        img = Image.open(image)

        # Change the original resolution of the image to one that the screen can display with the BICUBIC algorithm
        resized = img.resize(cozmo.oled_face.dimensions(), Image.BICUBIC)

        # Transforms the image into a format that the screen can display
        face = cozmo.oled_face.convert_image_to_screen_data(resized)

        self.robot.set_head_angle(cozmo.robot.MAX_HEAD_ANGLE).wait_for_completed()

        # Display image for 5000 ms
        self.robot.display_oled_face_image(face, 5000, in_parallel=True).wait_for_completed()
        self.robot.set_head_angle(degrees(0)).wait_for_completed()

    def play_animation(self):
        print("*** Playing animation ***")

        all_animation_triggers = self.robot.anim_triggers
        random.shuffle(all_animation_triggers)
        for i in range(3):
            animation = random.choice(all_animation_triggers)
            print("Playing: ", animation)
            self.robot.play_anim_trigger(animation).wait_for_completed()

    def got_song(self):
        print("*** Play a song ***")

        notes = [
            cozmo.song.SongNote(cozmo.song.NoteTypes.E2, cozmo.song.NoteDurations.Half),
            cozmo.song.SongNote(cozmo.song.NoteTypes.A2, cozmo.song.NoteDurations.Half),
            cozmo.song.SongNote(cozmo.song.NoteTypes.C2, cozmo.song.NoteDurations.Quarter),
            cozmo.song.SongNote(cozmo.song.NoteTypes.D2, cozmo.song.NoteDurations.Quarter),
            cozmo.song.SongNote(cozmo.song.NoteTypes.E2, cozmo.song.NoteDurations.Half),
            cozmo.song.SongNote(cozmo.song.NoteTypes.A2, cozmo.song.NoteDurations.Half),
            cozmo.song.SongNote(cozmo.song.NoteTypes.C2, cozmo.song.NoteDurations.Quarter),
            cozmo.song.SongNote(cozmo.song.NoteTypes.D2, cozmo.song.NoteDurations.Quarter),
            cozmo.song.SongNote(cozmo.song.NoteTypes.A2,cozmo.song.NoteDurations.ThreeQuarter),
            cozmo.song.SongNote(cozmo.song.NoteTypes.E2, cozmo.song.NoteDurations.Half),
            cozmo.song.SongNote(cozmo.song.NoteTypes.A2, cozmo.song.NoteDurations.Half),
            cozmo.song.SongNote(cozmo.song.NoteTypes.C2, cozmo.song.NoteDurations.Quarter),
            cozmo.song.SongNote(cozmo.song.NoteTypes.D2, cozmo.song.NoteDurations.Quarter),
            cozmo.song.SongNote(cozmo.song.NoteTypes.E2, cozmo.song.NoteDurations.Half),
            cozmo.song.SongNote(cozmo.song.NoteTypes.A2, cozmo.song.NoteDurations.Half),
            cozmo.song.SongNote(cozmo.song.NoteTypes.C2, cozmo.song.NoteDurations.Quarter),
            cozmo.song.SongNote(cozmo.song.NoteTypes.D2, cozmo.song.NoteDurations.Quarter),
            cozmo.song.SongNote(cozmo.song.NoteTypes.C2_Sharp,cozmo.song.NoteDurations.ThreeQuarter),
        ]

        # Play the ascending notes
        self.robot.play_song(notes, loop_count=1).wait_for_completed()

    def star_wars_song(self):
        print("*** Play a song ***")

        notes = [
            cozmo.song.SongNote(cozmo.song.NoteTypes.G2, cozmo.song.NoteDurations.Half),

            cozmo.song.SongNote(cozmo.song.NoteTypes.D2, cozmo.song.NoteDurations.Half),

            cozmo.song.SongNote(cozmo.song.NoteTypes.C2, cozmo.song.NoteDurations.Quarter),
            cozmo.song.SongNote(cozmo.song.NoteTypes.B2, cozmo.song.NoteDurations.Quarter),
            cozmo.song.SongNote(cozmo.song.NoteTypes.A2, cozmo.song.NoteDurations.Quarter),
            cozmo.song.SongNote(cozmo.song.NoteTypes.G2, cozmo.song.NoteDurations.Half),

            cozmo.song.SongNote(cozmo.song.NoteTypes.D2, cozmo.song.NoteDurations.Half),

            cozmo.song.SongNote(cozmo.song.NoteTypes.C2, cozmo.song.NoteDurations.Quarter),
            cozmo.song.SongNote(cozmo.song.NoteTypes.B2, cozmo.song.NoteDurations.Quarter),
            cozmo.song.SongNote(cozmo.song.NoteTypes.A2, cozmo.song.NoteDurations.Quarter),
            cozmo.song.SongNote(cozmo.song.NoteTypes.G2, cozmo.song.NoteDurations.Half),

            cozmo.song.SongNote(cozmo.song.NoteTypes.D2, cozmo.song.NoteDurations.Half),

            cozmo.song.SongNote(cozmo.song.NoteTypes.C2, cozmo.song.NoteDurations.Quarter),
            cozmo.song.SongNote(cozmo.song.NoteTypes.B2, cozmo.song.NoteDurations.Quarter),
            cozmo.song.SongNote(cozmo.song.NoteTypes.A2, cozmo.song.NoteDurations.Quarter),
            cozmo.song.SongNote(cozmo.song.NoteTypes.C2, cozmo.song.NoteDurations.Half),
        ]

        # Play the ascending notes
        self.robot.play_song(notes, loop_count=1).wait_for_completed()

    def darth_vader_song(self):
        print("*** Play a song ***")

        notes = [
            cozmo.song.SongNote(cozmo.song.NoteTypes.A2, cozmo.song.NoteDurations.Half),
            cozmo.song.SongNote(cozmo.song.NoteTypes.A2, cozmo.song.NoteDurations.Half),
            cozmo.song.SongNote(cozmo.song.NoteTypes.A2, cozmo.song.NoteDurations.Half),

            cozmo.song.SongNote(cozmo.song.NoteTypes.F2, cozmo.song.NoteDurations.Quarter),
            cozmo.song.SongNote(cozmo.song.NoteTypes.C2, cozmo.song.NoteDurations.Quarter),
            cozmo.song.SongNote(cozmo.song.NoteTypes.A2, cozmo.song.NoteDurations.Half),

            cozmo.song.SongNote(cozmo.song.NoteTypes.F2, cozmo.song.NoteDurations.Quarter),
            cozmo.song.SongNote(cozmo.song.NoteTypes.C2, cozmo.song.NoteDurations.Quarter),
            cozmo.song.SongNote(cozmo.song.NoteTypes.A2, cozmo.song.NoteDurations.Half),

            cozmo.song.SongNote(cozmo.song.NoteTypes.E2, cozmo.song.NoteDurations.Half),
            cozmo.song.SongNote(cozmo.song.NoteTypes.E2, cozmo.song.NoteDurations.Half),
            cozmo.song.SongNote(cozmo.song.NoteTypes.E2, cozmo.song.NoteDurations.Half),

            cozmo.song.SongNote(cozmo.song.NoteTypes.F2, cozmo.song.NoteDurations.Quarter),
            cozmo.song.SongNote(cozmo.song.NoteTypes.C2, cozmo.song.NoteDurations.Quarter),
            cozmo.song.SongNote(cozmo.song.NoteTypes.A2_Sharp, cozmo.song.NoteDurations.Half),
            cozmo.song.SongNote(cozmo.song.NoteTypes.F2, cozmo.song.NoteDurations.Quarter),
            cozmo.song.SongNote(cozmo.song.NoteTypes.C2, cozmo.song.NoteDurations.Quarter),
            cozmo.song.SongNote(cozmo.song.NoteTypes.A2_Sharp, cozmo.song.NoteDurations.Half),
        ]

        # Play the ascending notes
        self.robot.play_song(notes, loop_count=1).wait_for_completed()

    def stack_cubes(self):
        print("*** Attempt to stack 2 cubes ***")

        # Lookaround until Cozmo knows where at least 2 cubes are:
        lookaround = self.robot.start_behavior(cozmo.behavior.BehaviorTypes.LookAroundInPlace)
        cubes = self.robot.world.wait_until_observe_num_objects(num=2, object_type=cozmo.objects.LightCube, timeout=60)
        lookaround.stop()

        if len(cubes) < 2:
            print("Error: need 2 Cubes but only found", len(cubes), "Cube(s)")
        else:
            # Try and pickup the 1st cube
            current_action = self.robot.pickup_object(cubes[0], num_retries=3)
            current_action.wait_for_completed()
            if current_action.has_failed:
                code, reason = current_action.failure_reason
                result = current_action.result
                print("Pickup Cube failed: code=%s reason='%s' result=%s" % (code, reason, result))
                return

            # Now try to place that cube on the 2nd one
            current_action = self.robot.place_on_object(cubes[1], num_retries=3)
            current_action.wait_for_completed()
            if current_action.has_failed:
                code, reason = current_action.failure_reason
                result = current_action.result
                print("Place On Cube failed: code=%s reason='%s' result=%s" % (code, reason, result))
                return

            print("Cozmo successfully stacked 2 blocks!")

    def unstack_cubes(self):
        print("*** Attempt to unstack 2 cubes ***")
        print("!!! .: SHOW COZMO TWO STACKED CUBES :. !!!")

        lookaround = self.robot.start_behavior(cozmo.behavior.BehaviorTypes.LookAroundInPlace)
        cubes = self.robot.world.wait_until_observe_num_objects(num=2, object_type=cozmo.objects.LightCube, timeout=60)
        lookaround.stop()

        if len(cubes) < 2:
            print("Error: need 2 Cubes but only found", len(cubes), "Cube(s)")
        else:
            print(cubes[0].pose)
            print(cubes[1].pose)

            pickup = self.robot.pickup_object(cubes[1], num_retries=3)
            pickup.wait_for_completed()

            if pickup.has_failed:
                code, reason = pickup.failure_reason
                result = pickup.result
                print("Pickup Cube failed: code=%s reason='%s' result=%s" % (code, reason, result))

                pickup = self.robot.pickup_object(cubes[0], num_retries=3)
                pickup.wait_for_completed()

                if pickup.has_failed:
                    code, reason = pickup.failure_reason
                    result = pickup.result
                    print("Pickup Cube failed: code=%s reason='%s' result=%s" % (code, reason, result))
                    return
                else:
                    self.robot.turn_in_place(degrees(-90)).wait_for_completed()
                    self.robot.place_object_on_ground_here(cubes[0]).wait_for_completed()
            else:
                self.robot.turn_in_place(degrees(-90)).wait_for_completed()
                self.robot.place_object_on_ground_here(cubes[1]).wait_for_completed()

            print("Cozmo successfully unstacked 2 blocks!")

    def roll_cube(self):
        print("*** Attempt to roll a cube ***")

        lookaround = self.robot.start_behavior(cozmo.behavior.BehaviorTypes.LookAroundInPlace)
        cube = self.robot.world.wait_until_observe_num_objects(num=1, object_type=cozmo.objects.LightCube, timeout=60)
        lookaround.stop()

        if len(cube) < 1:
            print("Error: 1 cube needed")
        else:
            self.robot.roll_cube(cube[0], approach_angle=degrees(-90), num_retries=2).wait_for_completed()

    def hit_cube(self):
        lookaround = self.robot.start_behavior(cozmo.behavior.BehaviorTypes.LookAroundInPlace)
        cube = self.robot.world.wait_until_observe_num_objects(num=1, object_type=cozmo.objects.LightCube, timeout=60)
        lookaround.stop()

        if len(cube) < 1:
            print("Error: 1 cube needed")
        else:
            self.robot.go_to_object(cube[0], distance_mm(30)).wait_for_completed()
            self.robot.set_lift_height(1, accel=1, max_speed=1).wait_for_completed()
            self.robot.drive_straight(distance_mm(20), speed_mmps(5)).wait_for_completed()
            self.robot.set_lift_height(0.5, accel=9999, max_speed=9999).wait_for_completed()
            self.robot.set_lift_height(1, accel=9999, max_speed=9999).wait_for_completed()
            self.robot.drive_straight(distance_mm(-30), speed_mmps(100), num_retries=5).wait_for_completed()
            self.robot.set_lift_height(0, accel=1, max_speed=1).wait_for_completed()

    def say(self, text):
        self.robot.say_text(text).wait_for_completed()

    def got_performance(self):
        self.robot.play_anim_trigger(cozmo.anim.Triggers.PeekABooSurprised).wait_for_completed()
        self.robot.set_lift_height(1, 5)
        self.robot.say_text("Dracarise", use_cozmo_voice=False, in_parallel=True).wait_for_completed()
        self.got_song()
        self.display_image('targaryen.png')

    def trial_by_combat_performace(self):
        self.say("Je demande une ordalie par combat")
        self.hit_cube()

    def darth_vader_performance(self):
        self.robot.play_anim_trigger(cozmo.anim.Triggers.CodeLabScaredCozmo).wait_for_completed()
        self.robot.say_text("Je suis ton père", use_cozmo_voice=False, in_parallel=True).wait_for_completed()
        self.darth_vader_song()
        self.display_image('darth_vader.png')

    def star_wars_performance(self):
        self.robot.play_anim_trigger(cozmo.anim.Triggers.CodeLabReactHappy).wait_for_completed()
        self.robot.say_text("Que la force soit avec toi").wait_for_completed()
        self.star_wars_song()
        self.display_image('yoda.png')