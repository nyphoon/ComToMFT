
import abc

class WayBase(object):
	__metaclass__ = abc.ABCMeta

	@abc.abstractmethod
	def connect(self, **kwargs):
		pass

	@abc.abstractmethod
	def disconnect(self):
		pass

	@abc.abstractmethod
	def read(self):
		pass

	@abc.abstractmethod
	def write(self, data):
		pass

	# Craete thread to read data
	@abc.abstractmethod
	def read_start(self, data):
		pass
	@abc.abstractmethod
	def read_stop(self, data):
		pass
	@abc.abstractmethod
	def read_data_get(self, data):
		pass