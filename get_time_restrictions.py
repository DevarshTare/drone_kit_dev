from dronekit import connect, LocationGlobal, Command
from pymavlink import mavutil
import time, sys, math

connection_string = '127.0.0.1:14540'
MAV_MODE_AUTO = 4


permission_artefact = 565
is_valid = True
input_artefact = input(int()) 



the_connection = mavutil.mavlink_connection('127.0.0.1:14540')

the_connection.wait_heartbeat()

def check_system_time():
    message = the_connection.recv_match(type = 'SYSTEM_TIME', blocking= True)

    check_system_time.system_time = message.time_unix_usec / 1000

    boot_time = message.time_boot_ms

    time_since_start = check_system_time.system_time - boot_time
 
    time.sleep(1)

if permission_artefact == input_artefact:
    is_valid = True
    check_system_time()
    new_artefact_time = check_system_time.system_time + 50000
    home_pos = the_connection.recv_match(type = 'HOME_POSITION', blocking= 'True')


else :
    print 'Artefact is not valid.. Please enter valid artefact'

if is_valid:
    check_system_time()
    the_connection.mav.command_long_send(
            the_connection.target_system,  # target_system
            the_connection.target_component,
            mavutil.mavlink.MAV_CMD_DO_SET_MODE, # command
            0, # confirmation
            4, # param1 (1 to indicate arm)
            0, # param2 (all other params meaningless)
            0, # param3
            0, # param4
            0, # param5
            0, # param6
            0) # param7
    the_connection.mav.command_long_send(
            the_connection.target_system,  # target_system
            the_connection.target_component,
            mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM, # command
            0, # confirmation
            1, # param1 (1 to indicate arm)
            0, # param2 (all other params meaningless)
            0, # param3
            0, # param4
            0, # param5
            0, # param6
            0) # param7

    the_connection.mav.command_long_send(
            the_connection.target_system,  # target_system
            the_connection.target_component,
            mavutil.mavlink.MAV_CMD_NAV_TAKEOFF, # command
            0, # confirmation
            0, # param1 
            0, # param2 
            0, # param3
            0, # param4
            home_pos.latitude, # param5
            home_pos.longitude, # param6
            50) # param7
    while is_valid:
        check_system_time()
        if check_system_time.system_time > new_artefact_time:
            print('Valid flight time elasped')
            the_connection.mav.command_long_send(
                the_connection.target_system,  # target_system
                the_connection.target_component,
                mavutil.mavlink.MAV_CMD_NAV_RETURN_TO_LAUNCH, # command
                0, # confirmation
                0, # param1 (1 to indicate arm)
                0, # param2 (all other params meaningless)
                0, # param3
                0, # param4
                0, # param5
                0, # param6
                0) # param7
            is_valid = False
