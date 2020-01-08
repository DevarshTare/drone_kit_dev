from dronekit import connect, LocationGlobal, Command
from pymavlink import mavutil
import time, sys, math

connection_string = '127.0.0.1:14540'   #px4 port and IP address
MAV_MODE_AUTO = 4

print 'Connecting..'
vehicle = connect(connection_string, wait_ready = True)     #Connect to a vehicle and wait for ready message

#intialize a mode and set vehicle mode to auto

vehicle._master.mav.command_long_send(vehicle._master.target_system, vehicle._master.target_component,
                                           mavutil.mavlink.MAV_CMD_DO_SET_MODE, 0,
                                           MAV_MODE_AUTO,
                                           0, 0, 0, 0, 0, 0)


time.sleep(1)


# define a function fo changing variables inside a message and encode the variables
def send_global_position(lat,lon,alt, duration):
    msg = vehicle.message_factory.set_gps_global_origin_encode(lat,lon,alt, 0)    

    #send message every second
    for x in range(0,duration):
        vehicle.send_mavlink(msg)
        print 'Sending message..'
        time.sleep(1)

#initialize variable and change them
DURATION = 20
LAT = 32.823642
LON = 34.923844
ALT = 1000

send_global_position( LAT, LON, ALT, DURATION)