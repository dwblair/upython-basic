# main.py -- put your code here!

import machine
import time

led=machine.Pin('D13',machine.Pin.OUT)
a0 = machine.ADC(machine.Pin('A0'))

while True:
    led.high()
    time.sleep(0.2)
    value = a0.read()
    print('{0}'.format(value))    
    led.low()
    time.sleep(0.2)

