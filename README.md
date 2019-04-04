# Self Driving Car Control Design

## Self Driving Cars Longitudinal and Lateral Control Design 

In this project, I implemented a  controller in Python and use it to drive a car autonomously around a track in Carla Simulator.

### Project notes:

The waypoints include positions as well as the speed the vehicle should attain. As a result, the waypoints
become the reference signal for our controller and navigating to all the waypoints effectively completes the full track.


Since the controller reference contains both position and speed, we need to implement both __Longitudinal and Lateral Control__.


The output of the controller will be the vehicle __throttle__, __brake__ and __steering angle__ commands.

The throttle and brake come from the Longitudinal speed control and the steering comes from our Lateral Control.


If you want to make your own controller design,  I highly recommend that you should consider the following points:

If you open the simulator directory and navigate to the __Course1FinalProject folder__, you will see a file named __controller2d.py__

### These controller functions are as the following:

![Screenshot_6](https://user-images.githubusercontent.com/30608533/55581623-fb1e8a80-5725-11e9-9764-8145816374df.jpg)


You can adjust and re-create these functions according to your own custom controller design.



###  The Race Tack including waypoints:

![Screenshot_4](https://user-images.githubusercontent.com/30608533/55582000-0e7e2580-5727-11e9-83dd-4bafa30da590.jpg)



### Some concepts including formulas and expected output of the controller :

![Screenshot_1](https://user-images.githubusercontent.com/30608533/55582638-b516f600-5728-11e9-9e78-a82bc9afa6d7.jpg)

![Screenshot_2](https://user-images.githubusercontent.com/30608533/55582651-b9431380-5728-11e9-9a26-46e08467ffd3.jpg)

![Screenshot_3](https://user-images.githubusercontent.com/30608533/55582672-be07c780-5728-11e9-9cf3-687fa3179771.jpg)



### Screenshot from the application:

![Screenshot_7](https://user-images.githubusercontent.com/30608533/55583343-52265e80-572a-11e9-9a8d-b4dec7768878.jpg)


### Final Notes:

This poject is my own implementation of the  project assignment of Self Driving Cars Specialization offered by University of Toronto on Coursera.


- I added Carla Simulator Installation guides for Ubuntu and Windows into the __Guides folder__.

- Both in Windows and Ubuntu, add __Course1FinalProject__ folder into the __CarlaSimulator/PythonClient folder.__

Use ***different terminals*** for the ***client and server***.

### How to run in  Ubuntu:

- __Server terminal:__
> `$ cd $HOME /opt/CarlaSimulator      # where the CarlaSimulator is located`

> `$ ./CarlaUE4.sh /Game/Maps/RaceTrack -windowed -carla-server -ResX=640 -ResY=480 -benchmark -fps=20`


- __Client terminal:__
> `$ cd $HOME /opt/CarlaSimulator/PythonClient/Course1FinalProject`

> `$ python3 module_7.py`


### How to run in Windows:

- __Server terminal:__
> `\> C:`

> `\> cd \Coursera\CarlaSimulator`

> `\> CarlaUE4.exe /Game/Maps/RaceTrack -windowed -carla-server -benchmark -fps=15 -ResX=640 -ResY=480`



- __Client terminal:__
> `\> C:`

> `\> cd \Coursera\CarlaSimulator\PythonClient\Course1FinalProject`

> `\> python module_7.py`


### Final Reminders for troubleshooting tips:


- Python 3.7 is not currently compatible with CARLA. Use __Python 3.5.x or Python 3.6.x__ in Windows or Ubuntu.


- Allow CarlaUE4 to access through the Windows firewall if prompted to do so.

- CARLA requires networking enabled with the firewall allowing access to the CARLA
loader, and by default port 2000, 2001 and 2002 (TCP and UDP) available on the
network. When you first run CARLA in server mode, Windows will prompt you to
allow the application to access these ports if they are not already accessible on your
system. If your network does not provide access to port 2000, please look at  FAQ
section in the installation guides in the Guides folder.
