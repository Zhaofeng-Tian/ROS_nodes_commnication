#!/usr/bin/env python

# rec2cal.py
import rospy
from std_msgs.msg import String
from std_msgs.msg import Float32
from casestudy1.msg import number_msg

import random	


def result_callback(data):
    
    # rospy.loginfo(rospy.get_caller_id() + " This is : %s", data.operation_name)
    rospy.loginfo(rospy.get_caller_id() + " The number is : %s", data.number)
    result = 0.0
    if (data.is_multiplication):
        rospy.loginfo("\t DO Multiplication to: %s", data.number)
        result = data.number * 2.0
    else:
        rospy.loginfo("\t Do Division to: %s", data.number)
        result = data.number * 0.5
    pub = rospy.Publisher('calculated', number_msg, queue_size=10)
    
    
    myMessage = number_msg()
      
    myMessage.number = result
    myMessage.operation_name = data.operation_name
    myMessage.is_multiplication = data.is_multiplication
    rospy.loginfo(myMessage)
    pub.publish(myMessage)
   
def get_result():
    
    rospy.init_node('calculator', anonymous=True)

    rospy.Subscriber("msg_ex", number_msg, result_callback)
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()


if __name__ == '__main__':
    get_result()         
   
