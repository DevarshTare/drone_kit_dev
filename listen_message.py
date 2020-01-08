from dronekit import connect, LocationGlobal, Command
from pymavlink import mavutil
import time, sys, math

connection_string = '127.0.0.1:14550'
MAV_MODE_AUTO = 4

print 'Connecting..'
vehicle = connect(connection_string, wait_ready = True)

vehicle._master.mav.command_long_send(vehicle._master.target_system, vehicle._master.target_component,
                                           mavutil.mavlink.MAV_CMD_DO_SET_MODE, 0,
                                           MAV_MODE_AUTO,
                                           0, 0, 0, 0, 0, 0)



time.sleep(1)

print " Type: %s" % vehicle._vehicle_type
print " Armed: %s" % vehicle.armed
print " System status: %s" % vehicle.system_status.state
print " GPS: %s" % vehicle.gps_0
print " Alt: %s" % vehicle.location.global_relative_frame.alt

#define a call back function in case message is being read 
@vehicle.on_message('GLOBAL_ORIGIN')
def my_method(self, name, msg):
	print 'Recieved.. %s ' % name


#wait for message to be read
while True:
	time.sleep(1)