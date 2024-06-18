import read
import microcontroller


try:
    read.do_read()
except:
    microcontroller.reset()

