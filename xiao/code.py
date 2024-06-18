import read
import microcontroller


while True:

    try:
        read.do_read()
    except:
        microcontroller.reset()

