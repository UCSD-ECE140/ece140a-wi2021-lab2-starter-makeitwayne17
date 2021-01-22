# import the necessary packages
import cv2
from djitellopy import Tello
import time
import threading

class DroneControl():
    def __init__(self):
        self.drone = Tello()                       # Instantiate a Tello Object
        self.drone.connect()                       # Connect to the drone
        self.drone.streamoff()                     # In case stream never exited before
        self.drone.streamon()                      # Turn on drone camera stream
        self.timer = 0                             # Timing for printing statements
        self.flying = False                        # Keep track of flying state
        # How many video frames have been requested
        self.frame_count = 0
        self.init_frames = 50                    # Begin flying only after init_frames
        self.myThread = threading.Thread(target=self.fly)

    def __del__(self):
        self.drone.streamoff()

    def get_state(self):
        self.drone.get_battery()
        self.drone.get_speed_x
        self.drone.get_speed_y
        self.drone.get_speed_z
        self.drone.get_height
        self.drone.get_flight_time
        self.drone.get_temperature
        self.drone.get_yaw
        self.drone.get_roll
        self.drone.get_pitch
        self.drone.get_barometer
        self.drone.get_acceleration_x
        self.drone.get_acceleration_y
        self.drone.get_acceleration_z
        self.drone.get_distance_tof
        self.drone.query_wifi_signal_noise_ratio
        ####################################################
        ############## ADD YOUR CODE HERE ##################
        ####################################################

    def fly(self):
        #time.sleep(5)
        #self.get_state()
        #time.sleep(5)
        #self.drone.takeoff()
        #time.sleep(5)
        #self.drone.move_left(50)
        #time.sleep(5)
        #self.drone.rotate_clockwise(90)
        #time.sleep(5)
        #self.drone.rotate_clockwise(180)
        #time.sleep(5)
        #self.drone.land()
        #################################################
        ##################Challenge 1####################
        #################################################
        time.sleep(5)
        self.get_state()
        time.sleep(5)
        self.drone.takeoff()
        time.sleep(5)
        self.drone.move_left(50)
        time.sleep(5)
        self.drone.move_back(50)
        time.sleep(5)
        self.drone.move_right(50)
        time.sleep(5)
        self.drone.move_forward(50)
        time.sleep(5)
        self.drone.land()
        #################################################
        ###################Challenge 2###################
        #################################################
        time.sleep(5)
        self.drone.takeoff()
        time.sleep(10)
        self.drone.move_up(40)
        time.sleep(5)
        self.drone.move_forward(50)
        time.sleep(5)
        self.drone.rotate_counter_clockwise(45)
        time.sleep(5)
        self.drone.move_forward(50)
        time.sleep(5)
        self.drone.rotate_counter_clockwise(70)
        time.sleep(5)
        self.drone.flip_left()
        time.sleep(5)
        self.drone.move_down(25)
        time.sleep(5)
        self.drone.flip_right()
        time.sleep(5)
        self.drone.flip_right()
        time.sleep(5)
        self.drone.move_back(35)
        time.sleep(5)
        self.drone.flip_back()
        time.sleep(5)
        self.get_state()
        time.sleep(5)
        curve_xyz_speed(-50,-50,0,-200,-200,0,10)
        time.sleep(5)
        self.rotate_clockwise(115)
        time.sleep(5)
        self.drone.land()
        ####################################################
        ############## ADD YOUR CODE HERE ##################
        ####################################################
        

    def get_frame(self):
        # only begin flying once a video feed is established
        self.frame_count += 1
        if self.flying == False and self.frame_count > self.init_frames:
            self.flying = True
            # self.fly()
            self.myThread.start()
        # Grab a frame and resize it
        frame_read = self.drone.get_frame_read()
        if frame_read.stopped:
            return
        frame = cv2.resize(frame_read.frame, (360, 240))
        # encode OpenCV raw frame to jpeg
        ret, jpeg = cv2.imencode('.jpg', frame)
        return jpeg.tobytes()
