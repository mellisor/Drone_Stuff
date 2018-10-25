#!/usr/bin/env python2
import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import Empty

def main():
    print("I'm in the main")
    
    tak = rospy.Publisher('/tello/takeoff',Empty,queue_size=10)
    lan = rospy.Publisher('/tello/land',Empty,queue_size=10)
    vel = rospy.Publisher('/tello/cmd_vel',Twist,queue_size=10)

    rospy.init_node('square',anonymous=True)

    d = rospy.Duration(1,0)

    LINEAR_SPEED = .5

    cmd_vel = Twist()
    cmd_vel.linear.x = LINEAR_SPEED
    stop = Twist()

    # Take off
    tak.publish()
    rospy.sleep(d*5)

    try:
        # Move forward
        vel.publish(cmd_vel)
        cmd_vel.linear.x = 0
        cmd_vel.linear.y = LINEAR_SPEED
        rospy.sleep(d)

        # Stop
        vel.publish(stop)
        rospy.sleep(d)

        # Move right/left
        vel.publish(cmd_vel)
        cmd_vel.linear.x = -LINEAR_SPEED
        cmd_vel.linear.y = 0
        rospy.sleep(d)

        # Stop
        vel.publish(stop)
        rospy.sleep(d)

        # Move back
        vel.publish(cmd_vel)
        cmd_vel.linear.x = 0
        cmd_vel.linear.y = -LINEAR_SPEED
        rospy.sleep(d)

        # Stop
        vel.publish(stop)
        rospy.sleep(d)

        # Move left/right
        vel.publish(cmd_vel)
        rospy.sleep(d)

        # Stop
        vel.publish(stop)
        rospy.sleep(d)

        #Land
        lan.publish()
    except:
        print("YOU SUCK")
        lan.publish()

if __name__ == "__main__":
    main()





