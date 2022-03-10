
from mcculw import ul
from mcculw.enums import DigitalIODirection as Diod
from mcculw.enums import DigitalPortType as Dpt
from mcculw.enums import ULRange
import time
# Import libraries

# Configure the A set of ports on DIO Board (0-7) as inputs
ul.d_config_port(0, Dpt.FIRSTPORTA, Diod.IN)

# Configure the B set of ports on DIO Board (8-15) as outputs
ul.d_config_port(0, Dpt.FIRSTPORTB, Diod.OUT)

# Configure DIO Ports on A/D Converter. Set as Outputs
ul.d_config_port(1, Dpt.AUXPORT, Diod.OUT)

ManualLock = 1  # Create variable to toggle manual control. Lock is true by default

# Port numbers are completely random right now. Will need to change ports to match actual wiring.

def cylinderbleed():

    for ventcontroller in range(5, 0, -1):  # Cycle controller 5-0
        ul.d_out(0, Dpt.FIRSTPORTB, 0)
        ul.d_out(0, Dpt.FIRSTPORTB, 0)      # During this, send a signal to open the vent cylinders
        time.sleep(.5)                  # Wait so the air has time to escape
        if ventcontroller == 1:
            ul.d_out(0, Dpt.FIRSTPORTB, 1)   # At 1, power the cylinders, so they're shut, and break the loop
            ul.d_out(0, Dpt.FIRSTPORTB, 1)
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


    # return MagSensorData as value of the function
    return magsensorstatus

def pressuresensortest():

    pressuresensor = ul.a_in(1, 0, ULRange.BIP10VOLTS)  # Read pin to get analog value.

    if pressuresensor == 2047:       # If the sensor reads zero volts, there is likely an error. Set to error state.
        pressuresensorstatus = 1

    else:
        pressuresensorstatus = 0    # Otherwise, it's good.

    return pressuresensorstatus  # Send pressuresensorstatus out of the function

def distancesensortest():

    distancesensor = ul.a_in(1, 1, ULRange.BIP10VOLTS)

    if distancesensor < 205 or distancesensor > 3072:  # Check if voltage is in operating range
        distancesensorstatus = 1

    else:                            # Set value accordingly
        distancesensorstatus = 0

    return distancesensorstatus    # Send distancesensorstatus out

def lightbarcheck():
    lightbarstatus = 1  # Once we get the light we'll figure out how to do this
    return lightbarstatus

# Split data from functions into usable components
MagSensorStatus = (magsensortest())
PressureSensorStatus = (pressuresensortest())
DistanceSensorStatus = (distancesensortest())
CylinderBleedStatus = (cylinderbleed())
LightBarStatus = (lightbarcheck())

if MagSensorStatus == 1 or PressureSensorStatus == 1 or DistanceSensorStatus == 1 or CylinderBleedStatus != 1 or LightBarStatus == 1:
    ErrorState = 1  # Check for error state
else:
    ErrorState = 0

if CylinderBleedStatus == 1:
    print("Cylinder Bleed Successful!")
else:
    print("Cylinder Bleed Error!")

if MagSensorStatus == 0:
    print("Magnetic sensor check passed!")
else:
    print("Magnetic sensor check failed!")

if PressureSensorStatus == 0:
    print("Pressure sensor check passed!")
else:
    print("Pressure sensor check failed!")

if DistanceSensorStatus == 0:
    print("Distance sensor check passed!")
else:
    print("Distance sensor check failed!")

if LightBarStatus == 0:
    print("Light bar check passed!")
else:
    print("Light bar check failed!")

if ErrorState == 0:
    print("No error state!")
else:
    print("ERROR STATE!")