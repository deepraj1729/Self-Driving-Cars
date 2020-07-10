# Testing the Model:
Test the trained model with Flask application and SocketIO

## Test the model with the simulator using `Flask` and `SocketIo`
- To run the drive.py, install the requirements (safer to use in a virtual environment, virtualenv or conda):

      pip install -r requirements.txt
- Once done, run:
      
      python drive.py
- Open the simulator with `(800x600 -Fast)` configuration and click on `autonomous mode`.
- The car must run on it's own if everything works fine else check the errors in ur terminal.
- To close the simulator, just close the simulator window. And close the terminal directly `(instead of ctrl+C)`

#### *NB: The simulator is graphics intensive and don't run it for a significant amount of time unless you have a high performance GPU of >= 4GB RAM and CPU >= 8GB RAM*

## Testing the trained model in the Autonomous mode
![gif](testing_images/self_driving_car.gif)
