#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
from std_msgs.msg import Float32
import math 

def receive_news_convert(deg):
	rad = math.radians(deg.data)
	 
	rospy.loginfo(f"{deg.data}, -> {rad}")
	
if __name__ == '__main__':
	rospy.init_node('deg2rad')
	sub = rospy.Subscriber("/deg_topic", Float32, receive_news_convert)
	rospy.spin()
