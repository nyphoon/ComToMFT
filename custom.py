# coding=UTF-8
import verify
import output
import interop
import env_setting

import shutil
import os
import sys


class CustomTest(object):

    class CustomInfo(object):
        def __init__(self, element_custom):
            self.name = element_custom.get('name')
            self.command = element_custom.get('command')
            self.result = element_custom.get('result')

    def __init__(self, element_custom):
        self.elemCustom = element_custom.find('custom')
        if self.elemCustom is None:
            env_setting.msg_w('no custom content')
            return
        self.custominfo = self.CustomInfo(self.elemCustom)


    def start(self):
        elemResultMethod = self.elemCustom.find('verify')
        
        # call the custom tool
        tool_dir = env_setting.dir_tool_custom + self.custominfo.name + '/'

        cwd = os.getcwd().decode(sys.getfilesystemencoding())
        os.chdir(tool_dir)
        argv = self.custominfo.command.split()
        # opresult = interop.op_wait( argv )
        opresult = interop.op_poll( argv )
        os.chdir(cwd)
        print opresult

        # output result
        if elemResultMethod.tag == 'copy':
            try :
                shutil.copy( env_setting.dir_tool_custom+name+'/'+elemResultMethod.text, env_setting.dir_result)
            except :
                env_setting.msg_w("copy file fail")

        if elemResultMethod.tag == 'move':
            try :
                shutil.move( env_setting.dir_tool_custom+name+'/'+elemResultMethod.text, env_setting.dir_result)
            except : 
                env_setting.msg_w("move file fail")
                # handle existed folder
                # env_setting.msg_w('move file error. try to remove des tree and move again.')
                # shutil.rmtree(env_setting.dir_result+elemResultMethod.text)
                # shutil.move( env_setting.dir_tool_custom+name+'/'+elemResultMethod.text, env_setting.dir_result+elemResultMethod.text)

        # judge
        if elemResultMethod.tag == 'judge':
            isPass = {
                # 'return_code' : judge.equal(elemResultMethod.text, opresult[0]),
                'occour_in_stdout' : opresult[1] and judge.occour(elemResultMethod.text, opresult[1]),
                'occour_in_stderr' : opresult[2] and judge.occour(elemResultMethod.text, opresult[2])
            }.get( elemResultMethod.get('method') )

            output.output_result(self.itemname, isPass, 'judge_result.bat')
