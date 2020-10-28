# FAQ

### How do I make changes to my robot's code?

From your [AWS RoboMaker environment](https://us-west-2.console.aws.amazon.com/robomaker/home?region=us-west-2#ides), open a terminal and modify the file `/home/ubuntu/environment/VoiceRoboticsWorkshop/robot_ws/src/alexa/nodes/listener.py`

### I updated my robot's code but I don't see any changes in the simulator.

When you update your robot's code (the `listener.py` file in your [AWS RoboMaker environment](https://us-west-2.console.aws.amazon.com/robomaker/home?region=us-west-2#ides)), you must do a few things before the code can live on your robot and be observed in the virtual world. 

#### First...

1. Build the code
2. Bundle the code
3. Upload the output.tar file to Amazon S3

These steps can be found in [Setting up your robot](aws-robomaker/#build-bundle-and-upload-your-application).

#### Then...

Once your file has been uploaded, you need to create a new version of your application. Visit [your robot applications dashboard](https://us-west-2.console.aws.amazon.com/robomaker/home?region=us-west-2#robotApplications) and select your robot.

Click the **Create new version** button. Confirm the creation of your robot, then observe that your application has been updated:

![](../images/new-robot-version.png)

You need to clone the simulation to see your new changes. See "How do I restart my simulation?" below.

### How do I restart my simulation?

To restart your simulation, visit the [simulation jobs](https://us-west-2.console.aws.amazon.com/robomaker/home?region=us-west-2#simulationJobs) dashboard. Click on the last simulation you ran, then click on the "Actions" dropdown and choose "clone."

![](../images/clone-simulation-job.png)

Review the settings for your job. If you've recently updated your robot's code and created a new version, this new simulation job will incorporate those changes.

Click the **Create** button to launch your new smiluation job.

### I keep getting logged out of AWS RoboMaker/my AWS account

This workshop uses an Alexa-hosted skill to build your Alexa Skill. With an Alexa-hosted skill, you can get started quickly using Alexa-hosted AWS resources to power your skill. An Alexa-hosted skill works in conjunction with a code editor in the developer console to edit and deploy changes to your AWS Lambda code. 

Behind the scenes, this provisions AWS resources in a separate account. Sometimes, your browser may notice that another AWS account is being used, and will log you out of the account you were previously in. 

To get around this, it may help to work with your Alexa-hosted skill in one browser (or private window), and your personal AWS account in another browser.

### What is my AWS IoT endpoint?

Your endpoint can be found from the [AWS IoT Core dashboard](https://us-west-2.console.aws.amazon.com/iot/home?region=us-west-2#/settings), and will look similar to:

    a200000000000-ats.iot.us-west-2.amazonaws.com

You can also find your endpoint by opening a terminal in your AWS RoboMaker terminal, and typing the command:

    aws iot describe-endpoint --endpoint-type "iot:Data-ATS"

### I'm testing my `listener.py` code from an AWS RoboMaker terminal and get the error `KeyError: 'CERTS_LOCATION' 

Your terminal just needs to know where to find certificates for communicating with AWS IoT. First, ensure you've copied the certificates you've created to the AWS RoboMaker environment. Then, from the terminal, set this location:

    export CERTS_LOCATION=/home/ubuntu/environment/VoiceRoboticsWorkshop/robot_ws/src/alexa/certs/

### I'm testing my `listener.py` code from an AWS RoboMaker terminal and get the error `Unable to register with master node...`

You need to run the `roscore` master node before launching your listener file. In another terminal window, run the following command:

    roscore

After roscore is running, run `listener.py` again.

### My robot moves too fast and disappears from view / I can't find my robot anymore

There are few things you can do to find your robot.

1. You can expand the Gazebo window to see a larger view of the world

2. After you expand the Gazebo window, change the view angle to a "top-down" view. This will sometimes help you orient and find your robot.

![](../images/view-angle.png)

3. On the left "World" menu, expand "Models," then right-click on "create_2" and select "Move To"

![](../images/move-to.png)

### How do I debug robotic application or simulation issues?

The best way to debug a simulation job is to investigate the "Logs" found under the "Configuration" section of your Simulation Job.

![](../images/simulation-logging.png)