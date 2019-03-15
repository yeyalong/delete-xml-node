#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xml.dom.minidom as xmldom
import xlrd
import os

class Delete():
    def DeleteObsolete(self, xml_path):
        def DeleteMessage():
            xmlfilepath = os.path.abspath(xml_path)
            domobj = xmldom.parse(xmlfilepath)  # 得到文档对象
            elementobj = domobj.documentElement  # 得到元素对象
            elementobj_translation = elementobj.getElementsByTagName("translation")
            for i in range(len(elementobj_translation)):
                if elementobj_translation[i].getAttribute("type") == "obsolete":
                    elementobj_translation[i].parentNode.parentNode.removeChild(elementobj_translation[i].parentNode)
            with open(xml_path, 'w', encoding='utf-8') as fail_write_xml:
                domobj.writexml(fail_write_xml, encoding='utf-8', indent="", addindent="", newl="")
            fail_write_xml.close()

        def DeleteContext():
            xmlfilepath = os.path.abspath(xml_path)
            domobj = xmldom.parse(xmlfilepath)  # 得到文档对象
            elementobj = domobj.documentElement  # 得到元素对象
            elementobj_name = elementobj.getElementsByTagName("name")
            for j in range(len(elementobj_name)):
                if elementobj_name[j].nextSibling.nextSibling == elementobj_name[0].nextSibling.nextSibling:
                    print("a", j)
                    elementobj_name[j].parentNode.parentNode.removeChild(elementobj_name[j].parentNode)
            with open(xml_path, 'w', encoding='utf-8') as fail_write_xml:
                domobj.writexml(fail_write_xml, encoding='utf-8', indent="", addindent="", newl="")
            fail_write_xml.close()

        def DeleteBlankLine():
            with open(xml_path, 'r', encoding="utf-8") as infopen:
                lines = infopen.readlines()
            with open(xml_path, 'w', encoding="utf-8") as outfopen:
                for line in lines:
                    if line.split():
                        outfopen.writelines(line)

        DeleteMessage()
        DeleteContext()
        DeleteBlankLine()

if __name__ == '__main__':
    delete = Delete()
    delete.DeleteObsolete("cutter_zh.ts")