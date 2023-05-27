import serial
import time

ser = serial.Serial('/dev/ttyUSB0', 115200)  # el primer parametro se reemplaza por el puerto, es necesario conectar el esp32 al pc

temperatures = []

i=0
while (i<=10):
    data = ser.readline().decode().strip()
    if data.startswith("Temperature:"):
        temperature = float(data.split(":")[1])
        temperatures.append(temperature)
        print("Received temperature:", temperature)
        i=i+1
        time.sleep(10)
