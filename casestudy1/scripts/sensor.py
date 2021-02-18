#!/usr/bin/env python

# sensor.py

import rospy
from std_msgs.msg import Float32
import random

def sensor_pub():
    pub = rospy.Publisher('random_number', Float32, queue_size=10)
    rospy.init_node('sensor', anonymous=True)
    rate = rospy.Rate(1) # 1hz
    while not rospy.is_shutdown():
      num = random.random()*100.0 
      rospy.loginfo(num)
      pub.publish(num)
      rate.sleep()
   
if __name__ == '__main__':
    try:
        sensor_pub()
    except rospy.ROSInterruptException:
        pass
