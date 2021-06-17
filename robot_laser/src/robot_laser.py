#!/usr/bin/env python

import rospy

from sensor_msgs.msg import LaserScan

class Robot():
     def __init__(self):

        self.robot_sub = rospy.Subscriber("/laser_scan/scan", LaserScan, self.scan_callback)
        self.a = 0.0  #right
        self.b = 0.0  #front
        self.c = 0.0  #left
        self.ctrl_c = False

        self.rate = rospy.Rate(10) #10hz
        rospy.on_shutdown(self.shutdownhook)
    
     def scan_callback(self, msg):
        #print len(msg.ranges) #720
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

if __name__ == '__main__':
    rospy.init_node('robot_test', anonymous=True)     
    robot_object = Robot()
    try:
        robot_object.read_laser()   


    except rospy.ROSInterruptException:
        pass    




