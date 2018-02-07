#!/usr/bin/env python3

import rospy
from hmwk2 import *

def handler_add_service(nums):
    print('Adding: %s + %s = %s'%(nums.a, nums.b, (nums.a+nums.b)))
    return (nums.a+nums.b)

def add_service():
    rospy.init_node('add_two_int_service')
    rospy.Service('addition', TwoInts, )
    print("Adding Two Integers")

    rospy.spin()

if __name__ == '__main__':
    add_service()
