from dronekit import connect, LocationGlobal, Command
from pymavlink import mavutil
import time, sys, math

print 'Connecting..'

the_connection = mavutil.mavlink_connection('127.0.0.1:14540')

the_connection.wait_heartbeat()

message = the_connection.recv_match(type = 'SYSTEM_TIME', blocking= 'True')
print(message)