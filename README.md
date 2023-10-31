# Code Deploy Example in a ROS2 Workspace
This demonstration is to show how versioning could work in a ROS2 workspace. The intention of this repo is to allow remote changes to a workspace on a turtle bot 4. 

This repository only contains basic ROS2 tutorials:
1. ros_tutorials
2. roscpp_tutorials
3. rospy_tutorials
4. turtlesim

run.sh will
* Create viam_ros2_ws in the home dir.
* Copy the "src" directory hosted in the module.
* Build the workspace.

The user must:
* Source the overlay using ". /install/setup.bash"
* Run the node inside of the workspace.

# Build workspace
colcon build

The intended workflow is to:
1. Deploy this module to your robot.
2. Configure the module to receive latest updates.
3. Source the underlay (ROS2 Humble).
4. Source the overlay (code_deploy_ROS2_WS).
5. Test any tutorial example.
6. Modify any tutorial example (Doesn't have to be locally).
7. Push a new minor version to the Viam modular registry (Doesn't have to be locally).
8. Confirm the deployment of the new module on app.Viam.
9. Test any tutorial example and observe the new behavior.
