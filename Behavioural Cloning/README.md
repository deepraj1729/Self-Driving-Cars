# Behavioural Cloning:
Creating Autonomous cars and simulations

# Topics:
- Getting the Udacity Self-Driving Car Simulator
- Creating training images
- Training the Model
- Testing the trained model in the Autonomous mode

# Using with my default repo:

## Getting the Udacity Self-Driving Car Simulator:
- Get the simulator in the github link [udacity](https://github.com/udacity/self-driving-car-sim) and download the zip folder based on your OS.
- Unzip the downloaded folder and run the executable to open the Unity simulation software.
<img src="https://github.com/deepraj1729/Track/blob/master/screens/start_screen.png" width = "700" height = "500">

## Train the model with default dataset:
- Default dataset is present in the repository [Track](https://github.com/deepraj1729/Track).
- Open the notebook, [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/deepraj1729/Self-Driving-Cars/blob/master/Behavioural%20Cloning/Training_car/Behavioural%20Cloning.ipynb) and run the cells and thereby finally training the model with the images.
- After downloading the trained model (model.h5 file), copy that file in the directory `Behavioural\ Cloning/Testing_car/` and copy the filepath inside the drive.py variable:

      model_path = "./model.h5"
- To run the drive.py, install the requirements (safer to use in a virtual environment, virtualenv or conda):

      pip install -r requirements.txt
- Once done, run:
      
      python drive.py
- Open the simulator with `(800x600 -Fast)` configuration and click on `autonomous mode`.
- The car must run on it's own if everything works fine else check the errors in ur terminal.
- To close the simulator, just close the simulator window. And close the terminal directly `(instead of ctrl+C)`

#### *NB: The simulator is graphics intensive and don't run it for a significant amount of time unless you have a high performance GPU of >= 4GB RAM and CPU >= 8GB RAM*

## Creating custom training images: 
- Open the simulator
<img src="https://github.com/deepraj1729/Track/blob/master/screens/training_mode.png" width = "700" height = "500">
- Click on the record button to record and set the directory in which the training images will be saved.
- Try completing 3 laps in both directions (3 laps in default path, 3 laps in opposite path by turning the car in the opposite direction) 
- Upload training images of the 6 laps (together) in a github repo with `Git LFS` (Files will be large) and make it `public`.

## Training the Model with custom images:
- Once uploaded in github, copy this colab notebook [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/deepraj1729/Self-Driving-Cars/blob/master/Behavioural%20Cloning/Training_car/Behavioural%20Cloning.ipynb) and change the repo link and edit the dir links. 
- Train the model by running all the cells of the notebook and download the `model.h5` file (trained model).
- After downloading the trained model `(model.h5)`, copy that file in the directory `Behavioural\ Cloning/Testing_car/` and copy the filepath inside the drive.py variable:

      model_path = "./model.h5"
- To run the drive.py, install the requirements (safer to use in a virtual environment, virtualenv or conda):

      pip install -r requirements.txt
- Once done, run:

      python drive.py
- Open the simulator with `(800x600 -Fast)` configuration and click on `autonomous mode`.
- The car must run on it's own if everything works fine else check the errors in ur terminal.
- To close the simulator, just close the simulator window. And close the terminal directly `(instead of ctrl+C)`.

#### *NB: The simulator is graphics intensive and don't run it for a significant amount of time unless you have a high performance GPU of >= 4GB RAM and CPU >= 8GB RAM*

## Testing the trained model in the Autonomous mode
![gif](Testing_car/testing_images/self_driving_car.gif)
