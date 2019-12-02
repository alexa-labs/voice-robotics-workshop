pip install AWSIoTPythonSDK
sudo bash -c 'echo "yaml https://s3.us-west-2.amazonaws.com/voiceroboticsworkshop/rosdep/iot.yaml" > /etc/ros/rosdep/sources.list.d/10-aws-iot-pip.list'
cd ~/environment/VoiceRoboticsWorkshop/robot_ws
rosdep update

cd ~/environment/VoiceRoboticsWorkshop/simulation_ws
rosws update
rosdep install --from-paths src --ignore-src -r -y
colcon build
colcon bundle