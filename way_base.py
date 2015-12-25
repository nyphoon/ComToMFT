import abc

class WayBase(object):
	__metaclass__ = abc.ABCMeta

	@abc.abstractmethod
	def __init__(self, **kwargs):
		pass

	@abc.abstractmethod
	def open(self):
		pass

	@abc.abstractmethod
	def close(self):
		pass

	@abc.abstractmethod
	def send(self, data):
		pass

	@abc.abstractmethod
	def recv_start(self):
		pass
	@abc.abstractmethod
	def recv_stop(self):
		pass

	@abc.abstractmethod
	def get_data(self):
		pass
	@abc.abstractmethod
	def clear_data(self):
		pass