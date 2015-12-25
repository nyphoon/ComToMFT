# coding=UTF-8
import env_setting

import xml.etree.ElementTree as ElementTree

from way_serial import WaySerial
from way_custom import WayCustom

class Operation(object):
    def __init__(self, elem_operation):
        self.elem = elem_operation
        self.retreive_information()

    def retreive_information(self):
        self.info = {'name':'', 'id':''}
        for att in self.elem.attrib:
            if att in self.info:
                self.info[att] = self.elem.attrib[att]
            else:
                env_setting.msg('@{}: unknown attribute={}'.format(type(self).__name__, att))

    def get_step_all(self):
        for elem_step in self.elem.getchildren():
            yield elem_step.tag, elem_step.attrib , elem_step.text

class TestItem(object):
    def __init__(self, elem_testitem):
        self.elem = elem_testitem
        self.retreive_information()
    def retreive_information(self):
        self.info = {'name':'', 'way':'', 'skip':''}
        for att in self.elem.attrib:
            if att in self.info:
                self.info[att] = self.elem.attrib[att]
            else:
                env_setting.msg('@{}: unknown attribute={}'.format(type(self).__name__, att))

        self.info['skip'] = self.info['skip'] == r'yes'

    def get_operation_all(self):
        for elem_operation in self.elem.findall('operation'):
            yield Operation(elem_operation)


class TestPlan(object):
    def __init__(self, filepath):
        tree = ElementTree.ElementTree(file=filepath)
        self.root = tree.getroot()
        self.retreive_way_list()
        self.retreive_information()

    def get_TestItem_all(self):
        TestItemList = self.root.find('testitem_list')
        for elem_testitem in TestItemList.iter(tag='testitem'):
            yield TestItem(elem_testitem)

    def retreive_information(self):
        information = self.root.find('information')
        self.info = {'product':'', 'author':'', 'description':''}
        for k in information.attrib:
            env_setting.msg_d( 'retreive {}: {}'.format(k, information.attrib[k]) )
            if k=='product':
                self.info['product'] = information.attrib[k]
            elif k=='author':
                self.info['author'] = information.attrib[k]
        env_setting.msg_d( 'retreive description:' )
        env_setting.msg_d( '\t{}'.format(information.text) )
        self.info['description'] = information.text

    def retreive_way_list(self):
        self.ways = {}
        for elem_way in self.root.find('way_list').iter(tag='way'):
            if elem_way.attrib['type'] == 'serial':                
                self.ways[ elem_way.attrib['id'] ] = WaySerial(**elem_way.attrib)
            elif elem_way.attrib['type'] == 'adb':
                pass # to do
            elif elem_way.attrib['type'] == 'custom':
                self.ways[ elem_way.attrib['id'] ] = WayCustom(**elem_way.attrib)
            else:
                env_setting.msg( 'unknown way = {}'.format(elem_way.attrib['type']) )
