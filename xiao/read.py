"""
Example of reading from a card using the ``mfrc522`` module.
"""
import board
import digitalio
import usb_cdc
import time
import mfrc522


def check_unlock(serial, relay_pin):
    available = serial.in_waiting
    data_in = b""

    while available:
        data_in += serial.read(available)
        available = serial.in_waiting

    if data_in[:2] == b"\xde\xad":
        command = data_in[2:6]
        unlock_door(relay_pin)


def read_card(reader, serial):
    (stat, raw_uid) = reader.anticoll()

    if stat == reader.OK:
        uid = bytearray(raw_uid)
        serial.write(b"\xbe\xef" + uid)


def unlock_door(relay_pin):
    print("unlocking door")

    # False pulls the pin down, and the normally open pin on relay to closed
    relay_pin.value = False
    time.sleep(2.5)

    print("locking door")
    # True pulls the pin back up, and opens the normally open pin on relay
    relay_pin.value = True


def do_read():
    serial = usb_cdc.console

    rdr = mfrc522.MFRC522(sck=board.SCK, mosi=board.MOSI, miso=board.MISO, cs=board.D7, rst=board.D6)
    rdr.set_antenna_gain(0x07 << 4)

    relay_pin = digitalio.DigitalInOut(board.D3)
    relay_pin.direction = digitalio.Direction.OUTPUT
    relay_pin.drive_mode = digitalio.DriveMode.OPEN_DRAIN

    # True pulls the pin back up, and opens the normally open pin on relay
    relay_pin.value = True

    try:
        while True:
            check_unlock(serial, relay_pin)
            (stat, tag_type) = rdr.request(rdr.REQIDL)
            if stat == rdr.OK:
                (stat, raw_uid) = rdr.anticoll()
                if stat == rdr.OK:
                    if rdr.select_tag(raw_uid) == rdr.OK:
                        key = [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF]
                        if rdr.auth(rdr.AUTHENT1A, 8, key, raw_uid) == rdr.OK:
                            output = b"\xbe\xef" + bytes(raw_uid)
                            serial.write(output)
                            rdr.stop_crypto1()

                        else:
                            print("Authentication error")
                    else:
                        print("Failed to select tag")

    except KeyboardInterrupt:
        print("Bye")
