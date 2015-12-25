import env_setting
from way_base import WayBase
import sys
import threading
import serial

# chose an implementation, depending on os
#~ if sys.platform == 'cli':
#~ else:
import os
# chose an implementation, depending on os
if os.name == 'nt': #sys.platform == 'win32':
    from serial.tools.list_ports_windows import *
elif os.name == 'posix':
    from serial.tools.list_ports_posix import *
#~ elif os.name == 'java':
else:
    raise ImportError("Sorry: no implementation for your platform ('%s') available" % (os.name,))


if sys.version_info >= (3, 0):
    def character(b):
        return b.decode('latin1')
else:
    def character(b):
        return b


class WaySerial(WayBase):

    def scan(self):
        comport_list = []
        for port, desc, hwid in sorted(comports()):
            # comport_set.add(port)
            comport_list.append(port)
        #     print '{0} {1} \n'.format(port, desc)
        return comport_list

    def _reader(self):
        while self.reading:
            data = character(self.serial.read(1))
            self.read_data += data
            # direct output, just have to care about newline setting
            # if data == '\r':
            #     # sys.stdout.write('\n')
            #     self.read_data += '\n'
            # else:
            #     # sys.stdout.write(data)
            #     self.read_data += data
    def recv(self):
        if self.connected:
            self.read_data = self.serial.read(1)
            return self.read_data

    ## ABC implement
    def __init__(self, **kwargs):
        # kwargs['port'] and kwargs['baudrate'] can be configured as argument
        # if port isn't assigned, scan comport and connect to any comport
        if 'port' in kwargs:
            self.port = kwargs['port']
        else:
            self.port, desc, hwid = comports().next()
            env_setting.msg( 'auto scan comport={}'.format(self.port) )

        if 'baudrate' in kwargs:
            self.baudrate = int(kwargs['baudrate'])
        else:
            self.baudrate = 115200
            env_setting.msg( 'default baudrate={}'.format(self.baudrate) )

        self.connected = False
        self.reading = False
        self.read_data = ''

    def open(self):
        try:
            self.serial = serial.serial_for_url(self.port, self.baudrate) #, parity=parity, rtscts=rtscts, xonxoff=xonxoff, timeout=1)
        except AttributeError:
            # happens when the installed pyserial is older than 2.5. use the
            # Serial class directly then.
            self.serial = serial.Serial(self.port, self.baudrate) #, parity=parity, rtscts=rtscts, xonxoff=xonxoff, timeout=1)
        except:
            env_setting.msg( 'connect fail. port={0} baudrate={1}'.format(self.port, self.baudrate) )
        else:
            self.connected = True

    def close(self):
        if self.reading:
            self.read_stop()
        self.connected = False
        # seems no disconnect in UART

    def send(self, data):
        if self.connected:
            self.serial.write(data)

    def recv_start(self):
        if self.connected:
            self.read_data = ''
            self.reading = True
            self.receiver_thread = threading.Thread(target=self._reader)
            self.receiver_thread.setDaemon(True)
            self.receiver_thread.start()
        
    def recv_stop(self):
        if self.connected and self.reading:
            self.reading = False
            self.receiver_thread.join()

    def get_data(self):
        return self.read_data

    def clear_data(self):
        del self.read_data

# unit test
if __name__ == '__main__':
    way = WaySerial()
    # way = WaySerial( port='COM11', baudrate=115200 )
    print way.scan().next()
    way.open()

    way.send('ls')

    way.recv_start()
    import time
    time.sleep(5)
    way.recv_stop()
    print way.get_data()

    way.close()