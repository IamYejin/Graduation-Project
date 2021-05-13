#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist

global speed
speed = 0.2

def callback(msg):

   if msg.data == "forward":
      rospy.loginfo("receive forward")
      move.linear.x = speed
      move.angular.z = 0

   elif msg.data == "back":
      rospy.loginfo("receive back")
      move.linear.x = -speed
      move.angular.z = 0

   elif msg.data == "left":
      rospy.loginfo("receive left")
      if move.linear.x != 0:
         if move.angular.z < speed:
            move.angular.z += 0.10
      else:
         move.angular.z = speed * 2

   elif msg.data == "right":
      rospy.loginfo("receive right")
      if move.linear.x != 0:
         if move.angular.z > -speed:
            move.angular.z -= 0.10
      else:
         move.angular.z = -speed * 2

   elif msg.data == "stop":
      rospy.loginfo("receive stop")
      move.linear.x = 0
      move.linear.y = 0
      move.linear.z = 0
      move.angular.x = 0
      move.angular.y = 0
      move.angular.z = 0
        
   pub.publish(move)

# def miccb(data):
#   if data.data == "mic_2":
#      sub = rospy.Subscriber('/robot_2/recognizer/output', String, mvcb)
#   else:
#      sub.unregister()      

rospy.init_node('robot2_listener') # make file name robot2_listener.py

sub = rospy.Subscriber('/to_robot2_cmd', String, callback) # subscribe to the cmd_vel's topic in Twist()   
pub = rospy.Publisher("/cmd_vel", Twist, queue_size=10)
rate = rospy.Rate(2.0)

move = Twist()

rospy.spin()
