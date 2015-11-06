# coding=UTF-8

import xml.etree.ElementTree as ElementTree

class TestItem(object):
    def __init__(self, elem_testitem):
        self.name = ''
        self.way = ''
        self.skip = False
        for att in elem_testitem.attrib:
            if( att=='name' ):
                self.name = elem_testitem.attrib[att]
            elif( att=='way' ):
                self.way = elem_testitem.attrib[att]
            elif( att=='skip' and elem_testitem.attrib[att] == r'yes'):
                self.skip = True
            else:
                env_setting.msg('unknown attribute={}'.format(att))

class TestPlan(object):
    def __init__(self, filepath):
        self.tree = ElementTree.ElementTree(file=filepath)
        self.root = self.tree.getroot()
        self.TestItemList = self.root.find('TestItemList')
        self.information = self.root.find('information')
    
    def get_iter_TestItem(self):
        return self.TestItemList.iter(tag='TestItem')

    def disp_information(self):
        print('inforamtion:')
        for k in self.information.attrib:
            print( '\t{}: {}'.format(k, self.information.attrib[k]) )
        print( '\tdescription:' )
        print( '\t\t{}'.format(self.information.text) )