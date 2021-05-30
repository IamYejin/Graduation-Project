#!/usr/bin/env python
import rospy
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
import actionlib
from actionlib_msgs.msg import *
from geometry_msgs.msg import Twist, Pose, Point, Quaternion
from std_msgs.msg import String


class GoToA():

    def __init__(self):
        
        rospy.init_node('gotoA', anonymous=True)
        
        self.goal_sent = False
        rospy.on_shutdown(self.shutdown)   

        self.move_base = actionlib.SimpleActionClient("move_base", MoveBaseAction)
        rospy.loginfo("Wait for the action server to come up")

        # Allow up to 5 seconds for the action server to come up
        self.move_base.wait_for_server(rospy.Duration(5))

        # Subscribe to the /gohome topic to receive 'gohome'commands from the web page.
        rospy.Subscriber('/goA', String, self.go_A_callback)

        # A mapping from keywords or phrases to commands
        self.commands = ['goA']


    def go_A_callback(self, msg):
        # Get the motion command from the recognized phrase
        command = msg.data
        if (command in self.commands):
            if command == 'goA':
                # Send a goal
                self.goal_sent = True
                goal1 = MoveBaseGoal()
                goal1.target_pose.header.frame_id = 'map'
                goal1.target_pose.header.stamp = rospy.Time.now()
                goal1.target_pose.pose = Pose(Point(2.82, -0.31, 0.00), Quaternion(0.000, 0.000, 0.000, 1.000)) # beside the computer

                # Start moving
                self.move_base.send_goal(goal1)

                # Allow TurtleBot up to 60 seconds to complete task
                success = self.move_base.wait_for_result(rospy.Duration(60))    

                state = self.move_base.get_state()
                result = False

                if success and state == GoalStatus.SUCCEEDED:
                    # Achieved goal number#1!
                    self.goal_sent = False
                    rospy.loginfo("Success")

                else:
                    rospy.loginfo("Failed")
  
        else: #command not found
            #print 'command not found: ' + command
            self.cmd_vel.linear.x = 0.0
            self.cmd_vel.angular.z = 0.0
    
    
    def shutdown(self):
        if self.goal_sent:
            rospy.loginfo("Stop")
            rospy.sleep(1)


if __name__=="__main__":
    try:
      turtlebot = GoToA()
      rospy.spin()

    except rospy.ROSInterruptException: pass
rospy.loginfo("Ctrl-C caught. Quitting")

