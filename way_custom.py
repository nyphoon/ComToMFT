from way_base import WayBase
import sys
import subprocess
import threading

class WayCustom(WayBase):

    def __init__(self, **kwargs):
        self.argv = kwargs['command'].split()

    def open(self):
        self.child = subprocess.Popen(self.argv, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    def close(self):
        self.child.kill()

    def recv_start(self):
        self.receiver_thread = threading.Thread(target=self._reader)
        self.receiver_thread.setDaemon(True)
        self.receiver_thread.start()
        
    def recv_stop(self):
        self.receiver_thread.join()

    def send(self, data):
        # to do
        pass

    def get_data(self):
        return self.out

    def clear_data(self):
        del self.out
        del self.out

    def _reader(self):
        self.out = ''
        self.err = ''
        while self.child.poll() is None:
            self.out += self.child.stdout.readline()
            self.err += self.child.stderr.readline()
        print("WayCustom reader finish")        

