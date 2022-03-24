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

use_device_detection = True


def run_example():
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

    rate = 1000
    points_per_channel = 1000
    low_chan = 0
    high_chan = 3
    num_chans = 4

    total_count = points_per_channel * num_chans
    half_count = int(total_count / 2)
    # The SCALEDATA option, returns volts instead of A/D counts
    scan_options = ScanOptions.CONTINUOUS | ScanOptions.BACKGROUND | ScanOptions.SCALEDATA

    memhandle = ul.scaled_win_buf_alloc(total_count)
    buf_data = cast(memhandle, POINTER(c_double))

    # Check if the buffer was successfully allocated
    if not memhandle:
        print("Failed to allocate memory.")
        return

    a_input_mode(board_num, AnalogInputMode.SINGLE_ENDED)

    try:
        # Start the scan
        ul.a_in_scan(
            board_num, low_chan, high_chan, total_count,
            rate, ULRange.BIP10VOLTS, memhandle, scan_options)

        # Create a format string that aligns the data in columns
        # plus two for curr_index and curr_count
        row_format = "{:8}" * (num_chans + 3)

        # Print the channel name headers
        labels = []
        for ch_num in range(low_chan, high_chan + 1):
            labels.append("CH" + str(ch_num) + "\t")

        labels.append("index\t")
        labels.append("count\t")
        labels.append("diff")
        print(row_format.format(*labels))

        # boolean flag used to toggle reading upper and lower buffer
        read_lower = True
        # Start updating the displayed values
        status, curr_count, curr_index = ul.get_status(
            board_num, FunctionType.AIFUNCTION)

        last = 0
        diff = 0
        while status != Status.IDLE and curr_count < 100000:
            # Make sure a data point is available for display.
            if curr_count > 0:
                # curr_index points to the start of the last completed
                # channel scan that was transferred between the board and
                # the data buffer. Display the latest value for each
                # channel.

                # display_data = []
                if (curr_index > half_count) and (read_lower == True):
                    diff = curr_count - last
                    ul.scaled_win_buf_to_array(memhandle, buf_data, 0, int(half_count))
                    print(
                        '{:.3f}\t {:.3f}\t {:.3f}\t {:.3f}\t {:d}\t {:d}\t {:d}'.format(buf_data[0], buf_data[1],
                                                                                        buf_data[2],
                                                                                        buf_data[3], curr_index,
                                                                                        curr_count,
                                                                                        diff))
                    last = curr_count
                    read_lower = False
                elif (curr_index < half_count) and (read_lower == False):
                    diff = curr_count - last
                    ul.scaled_win_buf_to_array(memhandle, buf_data, int(half_count), int(half_count))
                    print(
                        '{:.3f}\t {:.3f}\t {:.3f}\t {:.3f}\t {:d}\t {:d}\t {:d}'.format(buf_data[0], buf_data[1],
                                                                                        buf_data[2],
                                                                                        buf_data[3], curr_index,
                                                                                        curr_count,
                                                                                        diff))
                    last = curr_count
                    read_lower = True
            sleep(0.1)
            status, curr_count, curr_index = ul.get_status(
                board_num, FunctionType.AIFUNCTION)

        # Stop the background operation (this is required even if the
        # scan completes successfully)
        ul.stop_background(board_num, FunctionType.AIFUNCTION)

        print("Scan completed successfully.")
    except ULError as e:
        util.print_ul_error(e)
    finally:
        # Free the buffer in a finally block to prevent errors from causing
        # a memory leak.
        ul.win_buf_free(memhandle)

        if use_device_detection:
            ul.release_daq_device(board_num)


if __name__ == '__main__':
    run_example()