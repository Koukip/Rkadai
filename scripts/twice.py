#!/usr/bin/env python3

<<<<<<< HEAD
#SPDX-License-Identifer: GPL-3.0
# *Copyright (c) 2022 kouki Uchida & Ryuichi Ueda. All right reserved.
=======


>>>>>>> 1ede2ed1741fe83f0c8611748c95b58f1a8ef45c

import rospy
from std_msgs.msg import Int32

n = 0

def cb(message):
    global n
    n = message.data*3

rospy.init_node('twice')
sub = rospy.Subscriber('count_up', Int32, cb)
pub = rospy.Publisher('twice', Int32, queue_size=1)
rate = rospy.Rate(10)
while not rospy.is_shutdown():
    pub.publish(n)
    rate.sleep()
rospy.spin()
