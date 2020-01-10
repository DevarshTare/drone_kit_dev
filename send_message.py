from dronekit import connect, LocationGlobal, Command
import time, sys, math
from pymavlink import mavutil, mavparm



print 'Connecting..'

the_connection = mavutil.mavlink_connection('127.0.0.1:14540')

the_connection.wait_heartbeat()


the_connection.mav.param_set_send(
			the_connection.target_system,  # target_system
            the_connection.target_component,
            'SYS_RESTART_TYPE',
            552,
            6)