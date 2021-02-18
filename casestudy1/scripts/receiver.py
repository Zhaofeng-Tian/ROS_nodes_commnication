#!/usr/bin/env python

# receiver.py

import rospy
from std_msgs.msg import String
from std_msgs.msg import Float32
from casestudy1.msg import number_msg

import random	

# Publlish the number to calculator after receiving the random number from sensor
def num_callback(data):
    rospy.loginfo(" The number is : %s", data.data)
    pub = rospy.Publisher('msg_ex', number_msg, queue_size=10)
    rate = rospy.Rate(1) # 1hz
    
    myMessage = number_msg()
      
    myMessage.number = data.data      
    k = random.randint(0, 1) 
	  
    if (k == 0):
        myMessage.operation_name = 'mutiply'
        myMessage.is_multiplication = True         
    else:
        myMessage.operation_name = 'divide'
        myMessage.is_multiplication = False         
         
    rospy.loginfo(myMessage)
    pub.publish(myMessage)
    
def cal_callback(number):
    rospy.loginfo(" The calculation result is : %s", number.number)
    pub = rospy.Publisher('customer', number_msg, queue_size=10)
   
   
    myMessage = number_msg()
      
    myMessage.number = number.number
    myMessage.operation_name = number.operation_name
    myMessage.is_multiplication = number.is_multiplication
    rospy.loginfo(myMessage)
    pub.publish(myMessage)
    # rate.sleep()
def num_rec():
    
    rospy.init_node('receiver', anonymous=True)

    rospy.Subscriber("random_number", Float32, num_callback)
    rospy.Subscriber("calculated", number_msg, cal_callback)
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()


if __name__ == '__main__':
    num_rec()         
