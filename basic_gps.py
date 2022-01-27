import time
import board
import busio
from micropyGPS import MicropyGPS
RX = board.RX
TX = board.TX
uart = busio.UART(TX, RX, baudrate=9600, timeout=30)
my_gps = MicropyGPS()

for sentence_count in range(10):
    stat = str(uart.readline())
    if stat:
        for x in stat:
            my_gps.update(x)
        stat = None
        sentence_count += 1

print('UTC Timestamp:', my_gps.timestamp)
print('Date:', my_gps.date_string('long'))
print('Latitude:', my_gps.latitude_string())
print('Longitude:', my_gps.longitude_string())
print('Horizontal Dilution of Precision:', my_gps.hdop)
print('Time Since Fix:', my_gps.time_since_fix())
