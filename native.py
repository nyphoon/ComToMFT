# coding=UTF-8
import interop
import env_setting
import sys

def op_msg(elem):
    env_setting.msg_d(__name__)
def op_command(elem):
    env_setting.msg_d(__name__)
def op_judge(elem):
    env_setting.msg_d(__name__)
    
operation_step = {
    'msg': op_msg,
    'command': op_command,
    'judge': op_judge
}

# -----------------------------------------------------------------------------------------------
def exec_native(testitem):
    # to do: implement way's open
    
    # do steps via the way
    for operation in testitem.iter('operation'):
        env_setting.msg_d('\t' + operation.tag + operation.attrib)
        for step in operation:
            env_setting.msg_d( '\t\t' + step.tag + step.attrib)
            operation_step.get(step.tag)(step)
            
    # to do: implement way's close
    