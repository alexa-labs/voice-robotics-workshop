# Example settings

This guide provides examples for the various settings you'll use throughout the workshop. 

## AWS RoboMaker Development Environment

| KEY                                   | VALUE(S)                                                                         |
|---------------------------------------|----------------------------------------------------------------------------------|
| Name                                  | WorkshopEnvironment                                                              |
| ROS distribution                      | ROS Kinetic                                                                      |
| Instance type                         | m4.large                                                                         |
| IAM Role                              | _leave unchanged_                                                                |
| VPC                                   | _select the "VoiceRoboticsWorkshopVPC" which was created via CloudFormation_     |
| Subnets                               | _select either of the two subnets in the dropdown_                               |

## Robot Application

| KEY                                   | VALUE(S)                                                                         |
|---------------------------------------|----------------------------------------------------------------------------------|
| Robot application                     | WorkshopRobot                                                                    |
| X86_64 source file                    | s3://_s3 bucket created via CloudFormation_/output.tar                           |
| Architecture                          | X86_64                                                                           |
| Tags                                  | _leave empty_                                                                    |

## Simulation Application

| KEY                                   | VALUE(S)                                                                         |
|---------------------------------------|----------------------------------------------------------------------------------|
| Simulation application                | WorkshopSimulation                                                               |
| ROS Distribution                      | ROS Kinetic                                                                      |
| Simulation software suite             | Gazebo 9                                                                         |
| Simulation rendering engine           | OGRE 1.x                                                                         |
| Sources                               | s3://voiceroboticsworkshop/simulation/output.tar                                 |

## Simulation Job

| KEY                                   | VALUE(S)                                                                         |
|---------------------------------------|----------------------------------------------------------------------------------|
| Simulation job duration               | 2 hours                                                                          |
| Failure behavior                      | fail                                                                             |
| ROS Distribution                      | ROS Kinetic                                                                      |
| IAM Role                              | VoiceRoboticsWorkshopExecutionRole                                               |
| Output destination                    | _leave empty_                                                                    |
| VPC                                   | VoiceRoboticsWorkshop                                                            |
| Security groups                       | Choose the "default" SG from the dropdown                                        |
| Subnets                               | (2 subnets as built by your CloudFormation template)                             |
| Assign public IP                      | Yes                                                                              |
| Enable connectivity to simulation     | _do not check_                                                                   |
| Tags                                  | _leave empty_                                                                    |
| Robot application                     | Choose existing application: WorkshopRobot                                       |
| Version                               | $LATEST                                                                          |
| (Robot) Launch package name           | alexa                                                                            |
| (Robot) Launch file                   | voice_robot.launch                                                               |
| Environment Variable: ENDPOINT        | (Found in IoT Core Settings, e.g. a2wxxxxxxrg71-ats.iot.us-west-2.amazonaws.com) |
| Simulation application                | Choose existing application: WorkshopSimulation                                  |
| Version                               | $LATEST                                                                          |
| (Simulation) Launch package name      | hello_world_simulation                                                           |
| (Simulation) Launch file              | empty_world.launch                                                               |
| Environment variables                 | _leave empty_                                                                    |
                                                                
