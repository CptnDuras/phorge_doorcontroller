import sys
import os
import time
import traceback

from datetime import datetime

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

from django.conf import settings

import serial
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.FileHandler("log_file.log")
formatter = logging.Formatter(
    "%(asctime)s : %(name)s  : %(funcName)s : %(levelname)s : %(message)s"
)
handler.setFormatter(formatter)
logger.addHandler(handler)


def setup_serial_conn(port="/dev/ttyACM0"):
    ser = serial.Serial(port, 9600, timeout=2, xonxoff=False, rtscts=False,
                        dsrdtr=False)  # Tried with and without the last 3 parameters, and also at 1Mbps, same happens.
    ser.flushInput()
    ser.flushOutput()

    return ser


def send_unlock_code(ser, code: bytes):
    prefix = b"\xde\xad"

    output = prefix + code
    print(f"sending output: {output}")
    ser.write(output)


def main_loop(ser):
    from access_control.models import Card, CardSwipeLog

    # bytesToRead = ser.inWaiting()
    message = ser.read(80)

    str_message = str(message)
    if "CTRL-D" in str_message:
        # send ctrl-dr
        time.sleep(50)
        # ser.write(b'\x04')

    if message[:2] == b"\xbe\xef":
        try:
            # codes are only 4 bytes long
            valid_code = message[2:6]
            card = Card.objects.filter(uid=valid_code).first()

            swipe_time = datetime.now()

            if card is None:
                # if the card doesn't exist in the DB, add it
                logger.info(f"Got new card {valid_code}. Writing to DB")
                card = Card.objects.create(
                    uid=valid_code,
                    last_swiped=swipe_time
                )

            # check to see if access should be granted:
            access = True  # card.can_access()

            if access:
                send_unlock_code(ser, valid_code)
                logger.info("Access Granted")

            else:
                logger.info("Access Denied")

            try:
                # Log to the database that we swiped this card
                CardSwipeLog.objects.create(
                    card=card,
                    swiped_on=swipe_time,
                    unlock=access,
                )
            except Exception as ex:
                logger.error(f"Exception on writing swipe date {ex}\n{traceback.format_exc()}")
        except Exception as ex:
            logger.error(f"Got {ex} while trying to read code from arduino ")
    else:
        print(message)


def run():
    django.setup()
    try:
        ser = setup_serial_conn()  # "/dev/ttyUSB0")

        while True:
            main_loop(ser)
    except Exception as ex:
        logger.error(f"Got error while trying to run the serial communication {ex}\n{traceback.format_exc()}")
        # wait for a second
        time.sleep(1)

        # Infinite money glitch
        run()


if __name__ == "__main__":
    run()
