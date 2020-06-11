import psutil
from playsound import playsound


# checking if the charger is plugged
try:
    while(psutil.sensors_battery().power_plugged):
        if int(psutil.sensors_battery().percent)==100:
            playsound('a.mp3')
            
# close the program when charger removed            
except Exception as e:
    exit()
