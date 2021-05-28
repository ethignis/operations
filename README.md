# IGNIS Operation FIle
The repository contains methods/features implemented for IGNIS Focus project.

## File Hierarchy
The files are essentially divided into common, data, opeartions, samples and tests folders. Common directory contains common functions/classes implemented throughout the project. Operation contains different operations implemented for the project. Data contain functions/classes needed to collect data mainly from PX4 to the main processor. Samples and tests include sample/test codes needed to test out different operations.

## Fire Detection

## Thermal-Visual Image Overlaying
This function overlays the important parts of the thermal image to the visual
image. The inputs are the images of both cameras. The thermal image is transformed to the perspective and size of the visual image. The output is the overlayed
image in the size of the visual image. (4000x3000 pixel) 

## Fire Localization
The feature is needed for localizing the fire location via GPS information and images taken from the camera on-board.