#!/usr/bin/env python

# listener.py

import rospy
from std_msgs.msg import String
from casestudy1.msg import number_msg	

def callback(data):

   rospy.loginfo( " After : %s , the result is : %s", data.operation_name, data.number)
   
  
    
def listener():

    rospy.init_node('consumer', anonymous=True)

    rospy.Subscriber("customer", number_msg, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()         
