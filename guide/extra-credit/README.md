# Extra credit

If you finish early and want to learn more, here are a few other things you can try:

### Other move commands

Moving forward and spinning around will only take your robot so far. You can give it additional functionality to add more versatility to your navigation. To add functionality, you'll need to update the `listener.py` code back in your AWS RoboMaker development environment. Refer to that code as you investigate additional commands below.

### TIP: Code locations
There are two places where you might update your code:

1. If you need to make changes to the code that rotates your robot, you'll need to use your AWS RoboMaker environment. The code is located at 

    /home/ubuntu/environment/VoiceRoboticsWorkshop/robot_ws/src/alexa/nodes/listener.py

**If you update your `listener.py` code, you need to [build, bundle, and upload your application](/aws-robomaker/#build-bundle-and-upload-your-application), then clone and restart the simulation.**

2. If you need to make changes things like _intents_ or _sample utterances_, you'll need to edit the code in the Alexa Skills Kit "code" tab. 

**Note: The hosted Alexa Skills infrastructure may log you out of your AWS account. Some developers find it useful to keep AWS open in separate browser or private browser window.**

## Moving backwards

What if you wanted your robot to move backwards? Look at the `def forward:` code in listener.py. You could create a new function, `def backward:`, which uses the same code, and change the logic at 

``` python
...
vel_msg.linear.x = abs(speed)
...
```

## Moving greater distances

Hint: Look at the `def forward:` code in listener.py. Notice how it pauses (`time.sleep(1)`) for 1 second before sending the `stop()` command?

## Turning left or right

Hint: Look at the `def spin(speed=60, angle=360):` function. Notice that robot spins for an angle of 360 degrees?

## Welcome message

You probably noticed that when we launch the robot it says "Hi! I'm your friendly robot! You can give me commands like move forward or spin around!". If you've added new functionality, like the ability to turn left or right, be sure to change the welcome and help messages.
