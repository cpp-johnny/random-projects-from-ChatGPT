import xml.etree.ElementTree as ET

def parse_xml(data):
    root = ET.fromstring(data)
    return root

data = '<root><element>text</element></root>'
parse_xml(data)
