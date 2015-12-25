# coding=UTF-8
import sys

import env_setting
import result
from test_plan import TestItem
from test_plan import TestPlan

def main():
    if len(sys.argv) == 2:
        testplan_file = sys.argv[1]
    else:
        testplan_file = "testplan.xml"

    testplan = TestPlan(testplan_file)
    try:
        testplan = TestPlan(testplan_file)
    except:
        env_setting.msg('read XML error')
        exit(1)
    
    env_setting.setup_dir_result()
    
    env_setting.msg('testplan inforamtion:')
    env_setting.msg( '\tproduct: {}\t'.format(testplan.info['product']) )
    env_setting.msg( '\tauthor: {}\t'.format(testplan.info['author']) )
    env_setting.msg( '\tdescription:' )
    env_setting.msg( '\t\t{}'.format(testplan.info['description']) )

    for testitem in testplan.get_TestItem_all():
        env_setting.msg('testitem: name="{name}"\tskip={skip}'.format(**testitem.info) )

        if testitem.info['skip'] :
            env_setting.msg('skip...')
            continue
        else:
            env_setting.msg('start...')

        try:
            way = testplan.ways[ testitem.info['way'] ]
        except KeyError:
            env_setting.msg('aquire way={way} fail'.format( **testitem.info ))
            continue

        # run test item
        way.open()
        for op in testitem.get_operation_all():
            way.recv_start()
            env_setting.msg('\toperation[{id}] {name}'.format(**op.info))
            for step in op.get_step_all():
                env_setting.msg_d('tag={} text={}'.format(step[0], step[2]))
                if step[0] == 'msg':
                    print '[ToDo] show msg:'
                    print step[1]
                elif step[0] == 'way':
                    if hasattr(way, step[1]['op']):
                        method = getattr(way, step[1]['op'])
                        method(step[2])
                    else:
                        env_setting.msg("way={} doesn't support op={}".format(op.info['id'], step[1]['op']))
                elif step[0] == 'verify':
                    result_handle = {
                        'occour': result.occour,
                        'equal': result.equal,
                        're_match': result.re_match,
                        'copy': result.copy,
                        'dump': result.dump
                    }.get( step[1]['method'] )
                    
                    if result_handle is None:
                        env_setting.msg("unknown verification method={}".format(step[1]['method']))
                    else:
                        result_handle(step[2], way.get_data(), step[1]['name'], 'result.txt');
                else:
                    env_setting.msg("not support step={}".format(step[0]))
            way.recv_stop()
        way.close()

if __name__ == '__main__':
    main()
