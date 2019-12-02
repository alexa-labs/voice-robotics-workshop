#!/usr/bin/env python

# Copyright 2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: LicenseRef-.amazon.com.-AmznSL-1.0
# Licensed under the Amazon Software License  http://aws.amazon.com/asl/

import json
import os
import random
import rospy
import signal
import string
import sys
import time

from geometry_msgs.msg import Twist
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient

# Setup some default values
ENDPOINT = os.environ["ENDPOINT"] # Set a RoboMaker environment variable
CERTS_LOCATION = os.environ["CERTS_LOCATION"] # This is set by the ROS node, it is not a RoboMaker environment variable
ROOT_CA = CERTS_LOCATION + "AmazonRootCA1.crt"
KEY = CERTS_LOCATION + "WorkshopRobot.private.key"
CERT = CERTS_LOCATION + "WorkshopRobot.cert.pem"
CLIENT_SUFFIX = "".join([random.choice(string.ascii_letters + string.digits) for n in xrange(12)])
CLIENT = "VoiceRoboticsWorkshop-" + CLIENT_SUFFIX

rospy.loginfo("Alexa node created client " + CLIENT)

# Setup and connect to the MQTT Client
WorkshopMQTTClient = None
WorkshopMQTTClient = AWSIoTMQTTClient(CLIENT)
WorkshopMQTTClient.configureEndpoint(ENDPOINT, 8883)
WorkshopMQTTClient.configureCredentials(ROOT_CA, KEY, CERT)
WorkshopMQTTClient.configureAutoReconnectBackoffTime(1, 32, 20)
WorkshopMQTTClient.configureOfflinePublishQueueing(-1)  # Infinite offline Publish queueing
WorkshopMQTTClient.configureDrainingFrequency(2)  # Draining: 2 Hz
WorkshopMQTTClient.configureConnectDisconnectTimeout(10)  # 10 sec
WorkshopMQTTClient.configureMQTTOperationTimeout(5)  # 5 sec
res = WorkshopMQTTClient.connect()
if res:
    rospy.loginfo("Alexa node connected to MQTT")
else:
    rospy.loginfo("Alexa node could not connect to MQTT")

# Initialize the node
rospy.init_node('alexa', anonymous=True)
rospy.loginfo("Alexa node started loading")
velocity_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
rospy.loginfo("Alexa node created publisher on /cmd_vel")

# Robot Drive Actions
def stop():
    """Stops the robot by sending a message with linear x,y,z values of 0"""
    
    vel_msg = Twist()
    vel_msg.linear.x = 0
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0

    velocity_publisher.publish(vel_msg) # forces stop
    rospy.loginfo("Published stop directive")

    time.sleep(1)
    
def forward(speed=0.5):
    """Moves the robot forward"""
    
    vel_msg = Twist()
    vel_msg.linear.x = abs(speed)
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0
    
    velocity_publisher.publish(vel_msg)
    rospy.loginfo("Published move forward directive")
    
    time.sleep(1)
    stop()
    
def spin(speed=60, angle=360):
    
    vel_msg = Twist()
    PI = 3.14159
    angular_speed = speed * 2 * PI/360
    relative_angle = angle * 2 * PI/360
    
    vel_msg.linear.x = 0
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = abs(angular_speed)

    t0 = rospy.Time.now().to_sec()
    current_angle = 0

    while(current_angle < relative_angle):
        velocity_publisher.publish(vel_msg)
        t1 = rospy.Time.now().to_sec()
        current_angle = angular_speed * (t1-t0)
    
    rospy.loginfo("Published spin directive")
    stop()

# Utility Functions 
def unsubscribe_topics():
    """Unbsubscribes from AWS IoT topics before exiting
    """

    topics = [
        'voice_command'
    ]

    for t in topics:
        WorkshopMQTTClient.unsubscribe(t)

# Interrupt Handler useful to break out of the script
def interrupt_handler(signum, frame):
    unsubscribe_topics()
    sys.exit("Exited and unsubscribed")

# Custom MQTT message callbacks
def driveCallback(CLIENT, userdata, message):
    rospy.loginfo("Received payload!")
    rospy.loginfo(message.topic)
    rospy.loginfo(message.payload)

    payload = json.loads(message.payload)
    
    if 'data' in payload:
        command = payload['data']
        rospy.loginfo("Processing command: " + command)
    else:
        command = ""
        rospy.loginfo("Ignoring invalid payload")
    
    if command == "forward":
        forward()
    elif command == "spin":
        spin()
    elif command == "stop":
        stop()
    elif command == "backward":
        # Extra Credit: Implement this and/or a "right" or "left" method!
        pass
    else:
        rospy.loginfo("Ignoring invalid directive. Looking for `forward`, `spin`, etc.")

# Subscribe to topics
rospy.loginfo("Alexa node attempting subscribing to voice_command with client " + CLIENT)
WorkshopMQTTClient.subscribe("voice_command", 1, driveCallback)
time.sleep(2)
rospy.loginfo("Alexa node ready and listening on the `voice_command` topic")

while True:
    signal.signal(signal.SIGINT, interrupt_handler)
    time.sleep(1)

unsubscribe_topics()