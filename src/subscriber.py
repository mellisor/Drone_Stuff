#!/usr/bin/env python2
import rospy
from std_msgs.msg import Empty, UInt8, Bool
from std_msgs.msg import UInt8MultiArray
from sensor_msgs.msg import Image
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from dynamic_reconfigure.server import Server
from h264_image_transport.msg import H264Packet
from tello_driver.msg import TelloStatus
from tello_driver.cfg import TelloConfig
from cv_bridge import CvBridge, CvBridgeError

import av
import math
import numpy as np
import threading
import time
from tellopy._internal import tello
from tellopy._internal import error
from tellopy._internal import protocol
from tellopy._internal import logger

def statCallback(msg):
    print("Forward Speed: " + str(msg.speed_northing_mps))
    print("Easting Speed: " + str(msg.speed_easting_mps))
    print("Horizontal Speed: " + str(msg.speed_horizontal_mps))
    print("Vertical Speed: " + str(msg.speed_vertical_mps))
    print("Battery %: " + str(msg.battery_percentage))
    print("Pitch: " + str(msg.cmd_pitch_ratio))
    print()
rospy.init_node('listener', anonymous = True)
r = rospy.Rate(.5)
sub = rospy.Subscriber('/tello/status',TelloStatus,statCallback)

try:
    while True:
        r.sleep()
except KeyboardInterrupt:
    pass
