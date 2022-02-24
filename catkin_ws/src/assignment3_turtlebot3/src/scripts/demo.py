#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
PI = 3.1415926535897

def move():
    # Starts a new node
    rospy.init_node('square', anonymous=True)
    velocity_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    vel_msg = Twist()
    distance=0.5

    #Receiveing the user's input
    print("Let's move your robot")


    #Checking if the movement is forward or backwards

    vel_msg.linear.x = 0.2

    #Since we are moving just in x-axis
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0
	
    while not rospy.is_shutdown():
        for i in range(4):

            #Setting the current time for distance calculus
            t0 = rospy.Time.now().to_sec()
            current_distance = 0

            #Loop to move the turtle in an specified distance
            while(current_distance < distance):
                #Publish the velocity
                velocity_publisher.publish(vel_msg)
                #Takes actual time to velocity calculus
                t1=rospy.Time.now().to_sec()
                #Calculates distancePoseStamped
                current_distance= 0.2*(t1-t0)
            #After the loop, stops the robot
            vel_msg.linear.x = 0
            #Force the robot to stop
            velocity_publisher.publish(vel_msg)
            t2=rospy.Time.now().to_sec()
            current_angle=0
            angle=90*2*PI/360
            vel_msg.angular.z=0.2
            while(current_angle < angle):
                velocity_publisher.publish(vel_msg)
                t3=rospy.Time.now().to_sec()
                current_angle=0.2*(t3-t2)
            vel_msg.angular.z=0
            vel_msg.linear.x=0.2
            velocity_publisher.publish(vel_msg)
        vel_msg.linear.x=0
        velocity_publisher.publish(vel_msg)
        break


if __name__ == '__main__':
    try:
        #Testing our function
        move()
    except rospy.ROSInterruptException: pass
