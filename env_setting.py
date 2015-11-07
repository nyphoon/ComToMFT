# coding=UTF-8

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
dir_tool_custom = r'MFT_tool_custom/'
dir_tool_native = r'MFT_tool_native/'
