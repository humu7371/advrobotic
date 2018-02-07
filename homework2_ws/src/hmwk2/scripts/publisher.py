#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

def talker():
    test_pub = rospy.Publisher("/test", String, queue_Size=10)
    rospy.init_node("test node")

    test_message = String()
    while not rospy.is_shutdown():
        rospy.loginfo('Testing Publisher')
        test_pub.publish('test')
        rospy.sleep(1)

if __name__ =='__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        raise
