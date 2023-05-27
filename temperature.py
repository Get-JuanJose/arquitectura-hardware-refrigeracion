import machine
import time

adc = machine.ADC(machine.Pin(36))
i=0

def temp(value):
    return (value*500)/1024


def fahrenheit(celsius):
    return (celsius * (9/5)) + 32

while i<=15:
    time.sleep_ms(10000)
    reading = adc.read()

    celsius_temp = temp(reading)
    i=i+1
    fahrenheit_temp = fahrenheit(celsius_temp)

    print("lm35 reading {}\nDegrees Celsius {}\nDegrees Fahrenheit {}".format(
        reading, celsius_temp, fahrenheit_temp))