#!/usr/bin/env python3

import rospy
import serial
import odrive
import logging
from frosty_odrive import frostyOdrive

# NOTE this is made for motor connected to Motor1

odrive = frostyOdrive()

if __name__ == "__main__":
    rospy.init_node("odriveSerialTest")
    print("Testing the serial connection for odrive")
    print("Node is running")
    odrive.connectOdrive()
    rospy.spin()