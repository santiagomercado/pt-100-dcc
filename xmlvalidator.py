from xml.etree import ElementTree as ET
import xmlschema
import sys

def parse(xml_str):
    try:
        tree = ET.fromstring(xml_str)
    except ET.ParseError:
        tree = None
    return tree

def validate(xml_str, xsd_str):
    try:
        tree = parse(xml_str)
        schema = xmlschema.XMLSchema(xsd_str,build=False)
        _ = schema.import_schema(namespace="extension",
                                 location='./schemas/statement/statement.xsd')
        schema.build()
        schema.validate(tree)
        print('ok')
    except Exception as error:
        print(error)


def xmlvalid(path1, path2):
    with open(path1) as fobj1,open(path2) as fobj2:
        xml_str = fobj1.read()
        xsd_str = fobj2.read()
        validate(xml_str, xsd_str)



def main():
    if len(sys.argv) == 2:
        xml_file = sys.argv[1]
    else:
        xml_file = 'dcc.xml'
    xmlvalid(xml_file,'./schemas/dcc/v3_0_0/dcc.xsd')

if __name__ == '__main__':
    main()
