#!/usr/bin/env python
# -*- coding_utf-8 -*-
import csv
from xml.dom.minidom import parseString
from lxml.etree import Element, SubElement, tostring
import xml.etree.ElementTree as ET

import sys
import os

def get_xml(target, image_file, tlx,tly,w,h):
    root = os.getcwd()
    if not os.path.exists(os.path.join(root, 'datasets')):
        os.mkdir(os.path.join(root, 'datasets'))

    node_root = Element('annotation')
    node_folder = SubElement(node_root, 'folder')
    node_folder.text = 'datasets'

    node_filename = SubElement(node_root, 'filename')
    node_filename.text = image_file + '.dcm'
    node_size = SubElement(node_root, 'size')
    node_width = SubElement(node_size, 'width')
    node_width.text = str(1024)
    node_height = SubElement(node_size, 'height')
    node_height.text = str(1024)
    node_depth = SubElement(node_size, 'depth')
    node_depth.text = '1'


    node_object = SubElement(node_root, 'object')
    node_name = SubElement(node_object, 'target')
    node_name.text = target

    if tlx == '':
        tlx = 0.0
    if tly == '':
        tly = 0.0
    if w == '':
        w = 0.0
    if h == '':
        h = 0.0

    node_bndbox = SubElement(node_object, 'bndbox')
    node_xmin = SubElement(node_bndbox, 'xmin')
    node_xmin.text = str(float(tlx))
    node_ymin = SubElement(node_bndbox, 'ymin')
    node_ymin.text = str(float(tly))
    node_xmax = SubElement(node_bndbox, 'xmax')
    node_xmax.text = str(float(tlx) + float(w))
    node_ymax = SubElement(node_bndbox, 'ymax')
    node_ymax.text = str(float(tly) + float(h))



    xml = tostring(node_root, pretty_print=True)  # 格式化显示，该换行的换行
    dom = parseString(xml)
    with open(os.path.join(root, 'datasets', image_file +  '.xml'), 'w') as f:
        dom.writexml(f, addindent='\t')


if __name__ == '__main__':
    # read = csv.reader(open('/Users/lees/Downloads/all/stage_1_train_labels.csv'))
    # #leng = len(list(f))
    # j = 1
    # for idx, i in enumerate(read):
    #     if idx != 0:
    #         get_xml(i[5], i[0], i[1], i[2], i[3], i[4])
    #         sys.stdout.write('\r>>> Converting to xml %d/%d ' % (j, 28989))
    #         j += 1
    tree = ET.parse('/Users/lees/Documents/rs/datasets/0a0f91dc-6015-4342-b809-d19610854a21.xml')
    root = tree.getroot()
    size = root.find('size')
    shape = [int(size.find('height').text),
             int(size.find('width').text),
             int(size.find('depth').text)]
    print(shape)
