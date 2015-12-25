# coding=UTF-8
import os

# message
def msg(msg):
	msg = r'[msg] '+ msg
	print(msg)
def msg_w(msg):
    msg =  r'[waring] '+ msg
    print(msg)
def msg_d(msg):
    if __debug__:
        msg = r'[debug] '+ msg
        print(msg)

dir_result = r'MFT_result/'

def setup_dir_result():
    if not os.path.exists(dir_result):
        os.makedirs(dir_result)