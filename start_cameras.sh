#!/bin/bash

# Start running both thermal cameras and visual cameras 

echo "Start the thermal camera"
roslaunch thermalgrabber_ros thermalgrabber_ros.launch

echo "Start the visual camera"
roscd 
cd ../src/spinnaker_camera_driver/launch/
roslaunch camera.launch & > /temp/temp_output