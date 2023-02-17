#!/usr/bin/env python3

import odrive
from odrive.enums import *
import logging
import time
import rospy

class frostyOdrive:
    def __init__(self):
        self.driver = None
        self.motor1 = None
        self.calibration = False
    

    def connectOdrive(self):
        if(self.driver != None):
            print("Odrive is already connected")
        else:
            print("Odrive is not connected, we will try to connect to one")
            try:
                self.driver = odrive.find_any(timeout=15) # timeout is default and so is the logger
                self.motor1 = self.driver.axis1
                print("Odrive is connected!!")
            except:
                print("Error cannot find odrive")
        
    def runCalibration(self):
        if self.calibration == False and self.motor1 != None:
            logging.warning("Don't touch the robot calibrating motor")
            self.motor1.requested_state = AXIS_STATE_FULL_CALIBRATION_SEQUENCE
            time.sleep(1)

            return True
        else:
            logging.warning("Motor Already calibrated theres no need")