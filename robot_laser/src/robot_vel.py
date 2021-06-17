#!/usr/bin/env python

import rospy

from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

class Robot():
     def __init__(self):

        self.robot_sub = rospy.Subscriber("/laser_scan/scan", LaserScan, self.scan_callback)
        self.robot_pub = rospy.Publisher("/cmd_vel", Twist, queue_size=1)
        self.a = 0.0  #right
        self.b = 0.0  #front
        self.c = 0.0  #left
        self.ctrl_c = False

        self.rate = rospy.Rate(1) #1hz
        rospy.on_shutdown(self.shutdownhook)
    
     def scan_callback(self, msg):
        self.a = msg.ranges[180]
        self.b = msg.ranges[len(msg.ranges)/2]
        self.c = msg.ranges[540]
       
     def read_laser(self):
         while not self.ctrl_c:
             if self.b >100:
                 self.b=5
             if self.a >100:
                 self.a=5
             if self.c >100:
                 self.c=5 

             print "a = "+ str(self.a)+ "  b = "+ str(self.b)+ "  c = "+ str(self.c) 
             self.rate.sleep()   
     
     def shutdownhook(self):

        self.ctrl_c = True  

     def main(self):
         self.out_of_maze = False
         self.vel = Twist()
         while not self.out_of_maze:
             print self.b
             if self.b > 2:
                 self.vel.linear.x = 0.5
             else:
                 self.vel.linear.x = 0 

             self.robot_pub.publish(self.vel)   
             self.rate.sleep() 

if __name__ == '__main__':
    rospy.init_node('robot_test', anonymous=True)     
    robot_object = Robot()
    try:
        robot_object.main()   


    except rospy.ROSInterruptException:
        pass    