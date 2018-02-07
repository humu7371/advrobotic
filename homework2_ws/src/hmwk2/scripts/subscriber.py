#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

def callback():
    rospy.loginfo(rospy.get_caller_id() + "callback from %s", data.data)

def listener():
    rospy.init_node('test')
    rospy.loginfo('Testing Subscriber')
    sub = rospy.Subscriber("chatter", String, callback)

    rospy.spin()

if __name__ == '__main__':
    listener()
