import time
from time import strftime
import datetime
import sys
import os

import cozmo
from cozmo.util import degrees, distance_mm, speed_mmps

# GLOBALS
directory = '.'
liveCamera = False

def on_new_camera_image(evt, **kwargs):    
    global liveCamera
    if liveCamera:
        print("Cozmo is taking a photo")
        pilImage = kwargs['image'].raw_image
        global directory
        pilImage.save(f"photos/{directory}/{directory}-{kwargs['image'].image_number}.jpeg", "JPEG")

def photo(robot: cozmo.robot.Robot):
    global liveCamera       
    
    # Assurez-vous que la tête et le bras de Cozmo sont à un niveau raisonnable
    # robot.set_head_angle(degrees(0.0)).wait_for_completed()
    robot.set_lift_height(0.0).wait_for_completed()
        
    liveCamera = True
    time.sleep(0.1)    
    liveCamera = False   

def setup_camera(robot: cozmo.robot.Robot):
    # Chaque fois que Cozmo voit une "nouvelle" image, prends une photo
    robot.add_event_handler(cozmo.world.EvtNewCameraImage, on_new_camera_image)    

    # Indiquer le dossier pour stocker les photos
    global directory    
    directory = f"{strftime('%y%m%d')}"
    if not os.path.exists('photos'):
        os.makedirs('photos')
    if not os.path.exists(f'photos/{directory}'):
        os.makedirs(f'photos/{directory}')