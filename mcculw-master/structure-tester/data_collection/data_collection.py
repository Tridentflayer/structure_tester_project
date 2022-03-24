# code ~~stolen~~ BORROWED from Article ID: 50803 on mccdaq.com
from __future__ import absolute_import, division, print_function

import time

from builtins import *  # @UnusedWildImport
from time import sleep
from ctypes import cast, POINTER, c_double, c_ushort, c_ulong

from mcculw import ul
from mcculw.enums import ScanOptions, FunctionType, Status
from mcculw.ul import ULError, a_input_mode
from mcculw.enums import InterfaceType
from mcculw.enums import ULRange
from mcculw.enums import AnalogInputMode
# import libraries to be used

# toggle device detection on or off
use_device_detection = True
def run_example():
    # device detection code to find any USB-1608G device connected
    # only runs if device detection is set to True
    # creates a new board through code rather than through InstaCal
    board_num = 0
    board_index = 0
    find_device = "USB-1608G"
    if use_device_detection:
        board_num = -1
        ul.ignore_instacal()
        dev_list = ul.get_daq_device_inventory(InterfaceType.USB)
        if len(dev_list) > 0:
            for device in dev_list:
                if str(device) == find_device:
                    print(f"Found {find_device} board number = {board_index}")
                    print(f"Serial number: {device.unique_id}")
                    print(f"Product type: {hex(device.product_id)}")
                    board_num = board_index
                    ul.create_daq_device(board_num, device)
                board_index = board_index + 1
            if board_num == -1:
                print(f"Device {find_device} not found")
                return
        else:
            print("No devices detected")
            return
    # **********End of Discovery************
    # rate of data collection
    rate = 1000
    # datapoints per channel
    points_per_channel = 1000
    # lowest channel in scan
    low_chan = 0
    # highest channel in scan
    high_chan = 3
    # total scan number (used later)
    num_chans = 4

    # Defining memory buffer size
    # As well as half that size
    total_count = points_per_channel * num_chans
    half_count = int(total_count / 2)
    # The SCALEDATA option, returns volts instead of A/D counts
    scan_options = ScanOptions.CONTINUOUS | ScanOptions.BACKGROUND

    # Creates memory buffer and a pointer to find it
    memhandle = ul.win_buf_alloc(total_count)
    buf_data = cast(memhandle, POINTER(c_double))

    # Check if the buffer was successfully allocated
    if not memhandle:
        print("Failed to allocate memory.")
        return

    # Sets the board to be single ended analog input
    a_input_mode(board_num, AnalogInputMode.SINGLE_ENDED)