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
	def __init__(self):
		# serial.serial_for_url('COM11', 115200)
		self.connected = False
		self.reading = False
		self.read_data = ''

	def scan(self):
		comport_list = []
		for port, desc, hwid in sorted(comports()):
			# comport_set.add(port)
			comport_list.append(port)
		# 	print '{0} {1} \n'.format(port, desc)
		return comports()

	def _reader(self):
		while self.reading:
			data = character(self.serial.read(1))
			self.read_data += data
			# direct output, just have to care about newline setting
			# if data == '\r':
			# 	# sys.stdout.write('\n')
			# 	self.read_data += '\n'
			# else:
			# 	# sys.stdout.write(data)
			# 	self.read_data += data


	## ABC implement
	def connect(self, **kwargs):
		# kwargs['port'] and kwargs['baudrate'] can be configured as argument
		# if port isn't assigned, scan comport and connect to any comport
		if 'port' in kwargs:
			port = kwargs['port']
		else:
			port, desc, hwid = comports().next()

		if 'baudrate' in kwargs:
			baudrate = kwargs['baudrate']
		else:
			baudrate = 9600

		try:
			self.serial = serial.serial_for_url(port, baudrate) #, parity=parity, rtscts=rtscts, xonxoff=xonxoff, timeout=1)
		except AttributeError:
			# happens when the installed pyserial is older than 2.5. use the
			# Serial class directly then.
			self.serial = serial.Serial(port, baudrate) #, parity=parity, rtscts=rtscts, xonxoff=xonxoff, timeout=1)
		except:
			print 'connect fail. port={0} baudrate={1}'.format(port, baudrate)
		else:
			self.connected = True
	
	def disconnect(self):
		if self.reading:
			self.read_stop()
		self.connected = False
		# seems no disconnect in UART
		pass

	def read(self):
		if self.connected:
			self.read_data = self.serial.read(1)
			return self.read_data

	def write(self, data):
		if self.connected:
			self.serial.write(data)

	def read_start(self):
		if self.connected:

			self.reading = True
			self.receiver_thread = threading.Thread(target=self._reader)
			self.receiver_thread.setDaemon(True)
			self.receiver_thread.start()
		
	def read_stop(self):
		if self.connected and self.reading:
			self.reading = False
			self.receiver_thread.join()

	def read_data_get(self):
		return self.read_data


def test():
	way = WaySerial()
	print way.scan().next()
	way.connect( port='COM11', baudrate=115200 )
	# way.connect()

	# way.write('t')

	way.read_start()
	import time
	time.sleep(5)
	way.read_stop()
	print way.read_data_get()

	way.disconnect()
	
if __name__ == '__main__':
	test()