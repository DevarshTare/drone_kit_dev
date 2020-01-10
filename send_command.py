from dronekit import connect, LocationGlobal, Command
import time, sys, math
from pymavlink import mavutil

the_connection = mavutil.mavlink_connection('127.0.0.1:14540')


the_connection.wait_heartbeat()

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
            mavutil.mavlink.MAV_CMD_NAV_TAKEOFF_LOCAL, # command
            0, # confirmation
            0, # param1 (1 to indicate arm)
            0, # param2 (all other params meaningless)
            3, # param3
            0, # param4
            0, # param5
            0, # param6
            30) # param7

time.sleep(30)

the_connection.mav.command_long_send(
            the_connection.target_system,  # target_system
            the_connection.target_component,
            mavutil.mavlink.MAV_CMD_NAV_LAND, # command
            0, # confirmation
            0, # param1 (1 to indicate arm)
            0, # param2 (all other params meaningless)
            0, # param3
            0, # param4
            0, # param5
            0, # param6
            0) # param7


