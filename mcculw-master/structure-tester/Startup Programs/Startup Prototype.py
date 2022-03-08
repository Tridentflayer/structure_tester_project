
from mcculw import ul
from mcculw.enums import DigitalIODirection as Diod
from mcculw.enums import DigitalPortType as Dpt
from mcculw.enums import ULRange
import time
# Import interfacing libraries

# Configure the A set of ports on DIO Board (0-7) as inputs
ul.d_config_port(0, Dpt.FIRSTPORTA, Diod.IN)

# Configure the B set of ports on DIO Board (8-15) as outputs
ul.d_config_port(0, Dpt.FIRSTPORTB, Diod.OUT)

# Configure DIO Ports on A/D Converter. Set as Outputs
ul.d_config_port(1, Dpt.AUXPORT, Diod.OUT)

ManualLock = 1  # Create variable to toggle manual control. Lock is true by default

# Port numbers are completely random right now. Will need to change ports to match actual wiring.

def cylinderbleed():

    ventcontroller = 2

    while ventcontroller == 1:
        ul.d_out(0, Dpt.FIRSTPORTB, 8)
        ul.d_out(0, Dpt.FIRSTPORTB, 9)


    while ventcontroller > 1:
        ul.d_out(0, Dpt.FIRSTPORTB, 8)
        ul.d_out(0, Dpt.FIRSTPORTB, 9)
        time.sleep(1)
        ventcontroller = ventcontroller - 1
        return ventcontroller








def magsensortest():

    magsensortop = ul.d_bit_in(0, Dpt.FIRSTPORTA, 0)
    magsensorbottom = ul.d_bit_in(0, Dpt.FIRSTPORTA, 1)  # Read True/False from port, set as variable

    if magsensortop == magsensorbottom:
        magsensorstatus = 1  # When the cylinder is at the bottom, and the sensors are equal, there must be an error

    elif magsensortop != magsensorbottom:
        magsensorstatus = 0  # Otherwise, set it as good

    else:
        magsensorstatus = 1   # If anything else happens set an error


    # return MagSensorData as value of the function
    return magsensorstatus

def pressuresensortest():

    pressuresensor = ul.a_in(1, 0, ULRange.BIP10VOLTS)  # Read pin to get analog value.

    if pressuresensor == 2048:       # If the sensor reads zero volts, there is likely an error. Set to error state.
        pressuresensorstatus = 1

    else:
        pressuresensorstatus = 0    # Otherwise, it's good.

    return pressuresensorstatus  # Send pressuresensorstatus out of the function

def distancesensortest():

    distancesensor = ul.a_in(1, 1, ULRange.BIP10VOLTS)

    if distancesensor < .5 or distancesensor > 2.5:  # Check if voltage is in operating range
        distancesensorstatus = 1

    else:                            # Set value accordingly
        distancesensorstatus = 0

    return distancesensorstatus    # Send distancesensorstatus out

# Split data from functions into usable components
MagSensorStatus = (magsensortest())
PressureSensorStatus = (pressuresensortest())
DistanceSensorStatus = (distancesensortest())

# Temp Data Readout

print("Mag Sensors =")
print(MagSensorStatus)
print("Pressure Sensor =")
print(PressureSensorStatus)
print("Distance Sensor =")
print(DistanceSensorStatus)
while 1 == 1:
    print(cylinderbleed())