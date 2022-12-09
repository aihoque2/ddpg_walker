#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
from std_msgs.msg import Float64

class JointPub(object):
    def __init__(self):
        self.publishers_array = []

        #our different joint publishers
        self.pub_hipR = rospy.Publisher('/waist_thighR_position_controller/command', Float64, queue_size=1)
        self.pub_hipL = rospy.Publisher('/waist_thighL_position_controller/command', Float64, queue_size=1)
        
        self.pub_kneeR = rospy.Publisher('/thighR_shankR_position_controller/command', Float64, queue_size=1)
        self.pub_kneeL = rospy.Publisher('/thighL_shankL_position_controller/command', Float64, queue_size=1)

        #publishers_array is a 2D list that holds each of our publishers
        self.publishers_array.append(self.pub_hipR)
        self.publishers_array.append(self.pub_hipL)
        self.publishers_array.append(self.pub_kneeR)
        self.publishers_array.append(self.pub_kneeL)

    def move_joints(self, joint_msg_array):
        i = 0
        for publisher_obj in self.publishers_array:
            joint_value = Float64()
            joint_value.data = joint_msg_array[i]

            publisher_obj.publish(joint_value)
            i += 1

    def start_loop(self, rate_value=2.0):
        pos1 = [1.57, -1.57, 1.57, -1.57]
        pos2 = [0.0, 0.0, 0.0, 0.0]
        position="pos1"
        
        rate = rospy.Rate(rate_value)
        while not rospy.is_shutdown():
            if position == "pos1":
                self.move_joints(pos1),
                position = "pos2"
            else:
                self.move_joints(pos2)
                position="pos1"

            rate.sleep()


if __name__ == '__main__':
    rospy.init_node('joint_publisher_node')
    joint_publisher = JointPub()
    rate_value = 12.0 #4 cycles a second
    joint_publisher.start_loop(rate_value)
    