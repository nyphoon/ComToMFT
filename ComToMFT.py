# coding=UTF-8
import sys

import env_setting
import native
from custom import CustomTest
from test_plan import TestItem
from test_plan import TestPlan

def NoneStr(s):
    if s is None:
        return 'N/A'
    else:
        return str(s)
    
def main():
    env_setting.msg('start')
    
    if len(sys.argv) == 2:
        testplan_file = argv[1]
    else:
        testplan_file = "testplan.xml"
    testplan = TestPlan(testplan_file)
    
    testplan.disp_information()

    # test start
    for elem_testitem in testplan.get_iter_TestItem():
        testitem = TestItem(elem_testitem)
        
        env_setting.msg('item: name={} way={} skip={}'.format(testitem.name, testitem.way, testitem.skip))

        if(testitem.skip):
            env_setting.msg('skip item...')
            continue
        env_setting.msg('start test...')

        if testitem.way == r'custom':
            custom_test = CustomTest(elem_testitem)
            custom_test.start()
        else:
            exec_native(elem_testitem)
    
    env_setting.msg('complete')

if __name__ == '__main__':
    main()
