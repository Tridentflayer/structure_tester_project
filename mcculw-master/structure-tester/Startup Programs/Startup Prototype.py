from mcculw import ul
from mcculw.enums import DigitalIODirection as Diod
from mcculw.enums import DigitalPortType as Dpt
from mcculw.enums import ULRange
from mcculw.enums import AnalogInputMode
import time
import tkinter as tk
# Import libraries

ul.d_config_port(0, Dpt.FIRSTPORTA, Diod.IN)   # 12-20
ul.d_config_port(0, Dpt.FIRSTPORTB, Diod.OUT)  # 2-10
ul.d_config_port(0, Dpt.FIRSTPORTC, Diod.IN)   # 32-40
ul.d_config_port(1, Dpt.AUXPORT, Diod.OUT)              # Configure ports and analog inputs to Single Ended
ul.a_input_mode(1, AnalogInputMode.SINGLE_ENDED)

ManualLock = 1  # Create variable to toggle manual control. Lock is true by default

# Port numbers are completely random right now. Will need to change ports to match actual wiring.

def cylinderbleed():

    for ventcontroller in range(5, 0, -1):  # Cycle controller 5-0
        ul.d_bit_out(0, Dpt.FIRSTPORTA, 8, 0)
        ul.d_bit_out(0, Dpt.FIRSTPORTA, 9, 0)      # During this, send a signal to open the vent cylinders
        time.sleep(.5)                             # Wait so the air has time to escape
        if ventcontroller == 1:
            ul.d_bit_out(0, Dpt.FIRSTPORTA, 8, 1)  # At 1, power the cylinders, so they're shut, and break the loop
            ul.d_bit_out(0, Dpt.FIRSTPORTA, 9, 1)
            break
    return ventcontroller               # Send the variable out

def magsensortest():

    magsensortop = ul.d_bit_in(0, Dpt.FIRSTPORTA, 0)
    magsensorbottom = ul.d_bit_in(0, Dpt.FIRSTPORTA, 1)  # Read True/False from port, set as variable

    if magsensortop == magsensorbottom:
        magsensorstatus = 1  # When the cylinder is at the bottom, and the sensors are equal, there must be an error

    elif magsensortop != magsensorbottom:
        magsensorstatus = 0  # Otherwise, set it as good

    else:
        magsensorstatus = 1   # If anything else happens set an error


    # return magsensorstatus as value of the function
    return magsensorstatus

def pressuresensortest():

    pressuresensor = ul.a_in(1, 0, ULRange.BIP10VOLTS)  # Read pin to get analog value.

    if pressuresensor in range(32760, 32770):       # If the sensor reads zero volts, there is likely an error.
        pressuresensorstatus = 1                    # 0 volts = ~32765

    elif pressuresensor < 32760:                 # If it reads negative volts something's screwy. Need to Fix SE Range
        pressuresensorstatus = 1
    else:
        pressuresensorstatus = 0    # Otherwise, it's good.
        print(pressuresensor)

    return pressuresensorstatus

def distancesensortest():

    distancesensor = ul.a_in(1, 8, ULRange.BIP10VOLTS)

    if distancesensor < 205 or distancesensor > 3072:  # Check if voltage is in operating range
        distancesensorstatus = 1

    else:
        distancesensorstatus = 0

    return distancesensorstatus

def lightbarcheck():
    lightbarstatus = 1  # Once we get the light we'll figure out how to do this
    return lightbarstatus

# Split data from functions into usable components
MagSensorStatus = (magsensortest())
PressureSensorStatus = (pressuresensortest())
DistanceSensorStatus = (distancesensortest())
CylinderBleedStatus = (cylinderbleed())
LightBarStatus = (lightbarcheck())

if MagSensorStatus == 1 or PressureSensorStatus == 1 or DistanceSensorStatus == 1:
    ErrorState = 1  # Check for error state

elif CylinderBleedStatus != 1 or LightBarStatus == 1:
    ErrorState = 1       # Cont. error state check
else:
    ErrorState = 0

# data printout time :)
window = tk.Tk()

frame_a = tk.Frame()
frame_b = tk.Frame()
frame_c = tk.Frame()
frame_d = tk.Frame()
frame_e = tk.Frame()
frame_f = tk.Frame()

if CylinderBleedStatus == 1:
    label_a = tk.Label(master=frame_a, text="Cylinder Bleed Success!")
    label_a.pack()
else:
    label_a = tk.Label(master=frame_a, text="Cylinder Bleed Failure!")
    label_a.pack()

if MagSensorStatus == 0:
    label_b = tk.Label(master=frame_b, text="Magnetic Sensor Check Passed!")
    label_a.pack()
else:
    label_b = tk.Label(master=frame_b, text="Magnetic Sensor Check Failed!")
    label_b.pack()

if PressureSensorStatus == 0:
    label_c = tk.Label(master=frame_c, text="Pressure Sensor Check Passed!")
    label_c.pack()
else:
    label_c = tk.Label(master=frame_c, text="Pressure Sensor Check Failed!")
    label_c.pack()

if DistanceSensorStatus == 0:
    label_d = tk.Label(master=frame_d, text="Distance Sensor Check Passed")
    label_d.pack()
else:
    label_d = tk.Label(master=frame_d, text="Distance Sensor Check Failed!")
    label_d.pack()

if LightBarStatus == 0:
    label_e = tk.Label(master=frame_e, text="Light Bar Check Passed!")
    label_e.pack()
else:
    label_e = tk.Label(master=frame_e, text="Light Bar Check Failed!")
    label_e.pack()

if ErrorState == 0:
    label_f = tk.Label(master=frame_f, text="No Error State!")
    label_f.pack()
else:
    label_f = tk.Label(master=frame_f, text="ERROR STATE!")
    label_f.pack()

frame_a.pack()
frame_b.pack()
frame_c.pack()
frame_d.pack()
frame_e.pack()
frame_f.pack()

window.mainloop()