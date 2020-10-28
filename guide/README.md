# Welcome to the Voice Robotics Workshop

Welcome to the **Voice Robotics Workshop**! In this workshop, you will learn how you can control robots with your voice using the Alexa Skills Kit. Today we will be using the covering the following technologies:

* the Alexa Skills Kit (ASK)
* the Robotics Operating System (ROS)
* services from Amazon Web Services (AWS), including

    * AWS Lambda
    * AWS IoT Core
    * AWS RoboMaker

Don't worry if any of this is new to you, this guide will step you through each piece, and provide code you need along the way. We will create a virtual robot with [AWS RoboMaker](https://aws.amazon.com/robomaker/) and you'll control it inside the simulation by using your voice. If you have a compatible robot, you will be able to take the code you create today and operate a robot in the real world!

### NOTE: AWS Administrative Rights

To complete this workshop you will need access to an AWS account that has administrative rights, or, has the ability to create resources. If you're taking this workshop at an AWS event like re:Invent or a Summit, speak with the organizer about possible AWS Credits for students. Typically, this course can be completed in around 2 hours and for less than $5 in resources.

## Goal

By the end of this 2 hour workshop, you will have a skill that lets you send voice commands to your robot, like "tell workshop robot to move forward," or "ask workshop robot to spin around." Each command is converted to a directive via ASK, which is then securely passed along to your robot. Your robot will monitor for messages on a special "node" you will create. When the robot recognizes a new command, it can then execute the associated action (e.g., move forward).

### TIP: Use a text editor to store your settings
There will be multiple settings you'll use throughout the workshop. Open a text editor that you can use to copy values to and from, to save you some time along the way.

Ready to go? [Let's get started!](getting-started/README.md)
