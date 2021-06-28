#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Generated Sat Jun 26 08:21:50 2021 by generateDS.py version 2.38.6.
# Python 3.9.4 (default, Apr  9 2021, 16:34:09)  [GCC 7.3.0]
#
# Command line options:
#   ('-o', 'SI_Format1.py')
#   ('-s', 'SI_Formatsubs1.py')
#   ('--external-encoding', 'utf-8')
#   ('--export', 'write etree')
#
# Command line arguments:
#   SI_Format.xsd
#
# Command line:
#   generateds/generateDS.py -o "SI_Format1.py" -s "SI_Formatsubs1.py" --external-encoding="utf-8" --export="write etree" SI_Format.xsd
#
# Current working directory (os.getcwd()):
#   genxsd
#

import sys
try:
    ModulenotfoundExp_ = ModuleNotFoundError
except NameError:
    ModulenotfoundExp_ = ImportError
from six.moves import zip_longest
import os
import re as re_
import base64
import datetime as datetime_
import decimal as decimal_
try:
    from lxml import etree as etree_
except ModulenotfoundExp_ :
    from xml.etree import ElementTree as etree_


Validate_simpletypes_ = True
SaveElementTreeNode = True
if sys.version_info.major == 2:
    BaseStrType_ = basestring
else:
    BaseStrType_ = str


def parsexml_(infile, parser=None, **kwargs):
    if parser is None:
        # Use the lxml ElementTree compatible parser so that, e.g.,
        #   we ignore comments.
        try:
            parser = etree_.ETCompatXMLParser()
        except AttributeError:
            # fallback to xml.etree
            parser = etree_.XMLParser()
    try:
        if isinstance(infile, os.PathLike):
            infile = os.path.join(infile)
    except AttributeError:
        pass
    doc = etree_.parse(infile, parser=parser, **kwargs)
    return doc

def parsexmlstring_(instring, parser=None, **kwargs):
    if parser is None:
        # Use the lxml ElementTree compatible parser so that, e.g.,
        #   we ignore comments.
        try:
            parser = etree_.ETCompatXMLParser()
        except AttributeError:
            # fallback to xml.etree
            parser = etree_.XMLParser()
    element = etree_.fromstring(instring, parser=parser, **kwargs)
    return element

#
# Namespace prefix definition table (and other attributes, too)
#
# The module generatedsnamespaces, if it is importable, must contain
# a dictionary named GeneratedsNamespaceDefs.  This Python dictionary
# should map element type names (strings) to XML schema namespace prefix
# definitions.  The export method for any class for which there is
# a namespace prefix definition, will export that definition in the
# XML representation of that element.  See the export method of
# any generated element type class for an example of the use of this
# table.
# A sample table is:
#
#     # File: generatedsnamespaces.py
#
#     GenerateDSNamespaceDefs = {
#         "ElementtypeA": "http://www.xxx.com/namespaceA",
#         "ElementtypeB": "http://www.xxx.com/namespaceB",
#     }
#
# Additionally, the generatedsnamespaces module can contain a python
# dictionary named GenerateDSNamespaceTypePrefixes that associates element
# types with the namespace prefixes that are to be added to the
# "xsi:type" attribute value.  See the exportAttributes method of
# any generated element type and the generation of "xsi:type" for an
# example of the use of this table.
# An example table:
#
#     # File: generatedsnamespaces.py
#
#     GenerateDSNamespaceTypePrefixes = {
#         "ElementtypeC": "aaa:",
#         "ElementtypeD": "bbb:",
#     }
#

try:
    from generatedsnamespaces import GenerateDSNamespaceDefs as GenerateDSNamespaceDefs_
except ModulenotfoundExp_ :
    GenerateDSNamespaceDefs_ = {}
try:
    from generatedsnamespaces import GenerateDSNamespaceTypePrefixes as GenerateDSNamespaceTypePrefixes_
except ModulenotfoundExp_ :
    GenerateDSNamespaceTypePrefixes_ = {}

#
# You can replace the following class definition by defining an
# importable module named "generatedscollector" containing a class
# named "GdsCollector".  See the default class definition below for
# clues about the possible content of that class.
#
try:
    from generatedscollector import GdsCollector as GdsCollector_
except ModulenotfoundExp_ :

    class GdsCollector_(object):

        def __init__(self, messages=None):
            if messages is None:
                self.messages = []
            else:
                self.messages = messages

        def add_message(self, msg):
            self.messages.append(msg)

        def get_messages(self):
            return self.messages

        def clear_messages(self):
            self.messages = []

        def print_messages(self):
            for msg in self.messages:
                print("Warning: {}".format(msg))

        def write_messages(self, outstream):
            for msg in self.messages:
                outstream.write("Warning: {}\n".format(msg))


#
# The super-class for enum types
#

try:
    from enum import Enum
except ModulenotfoundExp_ :
    Enum = object

#
# The root super-class for element type classes
#
# Calls to the methods in these classes are generated by generateDS.py.
# You can replace these methods by re-implementing the following class
#   in a module named generatedssuper.py.

try:
    from generatedssuper import GeneratedsSuper
except ModulenotfoundExp_ as exp:
    
    class GeneratedsSuper(object):
        __hash__ = object.__hash__
        tzoff_pattern = re_.compile(r'(\+|-)((0\d|1[0-3]):[0-5]\d|14:00)$')
        class _FixedOffsetTZ(datetime_.tzinfo):
            def __init__(self, offset, name):
                self.__offset = datetime_.timedelta(minutes=offset)
                self.__name = name
            def utcoffset(self, dt):
                return self.__offset
            def tzname(self, dt):
                return self.__name
            def dst(self, dt):
                return None
        def gds_format_string(self, input_data, input_name=''):
            return input_data
        def gds_parse_string(self, input_data, node=None, input_name=''):
            return input_data
        def gds_validate_string(self, input_data, node=None, input_name=''):
            if not input_data:
                return ''
            else:
                return input_data
        def gds_format_base64(self, input_data, input_name=''):
            return base64.b64encode(input_data)
        def gds_validate_base64(self, input_data, node=None, input_name=''):
            return input_data
        def gds_format_integer(self, input_data, input_name=''):
            return '%d' % input_data
        def gds_parse_integer(self, input_data, node=None, input_name=''):
            try:
                ival = int(input_data)
            except (TypeError, ValueError) as exp:
                raise_parse_error(node, 'Requires integer value: %s' % exp)
            return ival
        def gds_validate_integer(self, input_data, node=None, input_name=''):
            try:
                value = int(input_data)
            except (TypeError, ValueError):
                raise_parse_error(node, 'Requires integer value')
            return value
        def gds_format_integer_list(self, input_data, input_name=''):
            if len(input_data) > 0 and not isinstance(input_data[0], BaseStrType_):
                input_data = [str(s) for s in input_data]
            return '%s' % ' '.join(input_data)
        def gds_validate_integer_list(
                self, input_data, node=None, input_name=''):
            values = input_data.split()
            for value in values:
                try:
                    int(value)
                except (TypeError, ValueError):
                    raise_parse_error(node, 'Requires sequence of integer values')
            return values
        def gds_format_float(self, input_data, input_name=''):
            return ('%.15f' % input_data).rstrip('0')
        def gds_parse_float(self, input_data, node=None, input_name=''):
            try:
                fval_ = float(input_data)
            except (TypeError, ValueError) as exp:
                raise_parse_error(node, 'Requires float or double value: %s' % exp)
            return fval_
        def gds_validate_float(self, input_data, node=None, input_name=''):
            try:
                value = float(input_data)
            except (TypeError, ValueError):
                raise_parse_error(node, 'Requires float value')
            return value
        def gds_format_float_list(self, input_data, input_name=''):
            if len(input_data) > 0 and not isinstance(input_data[0], BaseStrType_):
                input_data = [str(s) for s in input_data]
            return '%s' % ' '.join(input_data)
        def gds_validate_float_list(
                self, input_data, node=None, input_name=''):
            values = input_data.split()
            for value in values:
                try:
                    float(value)
                except (TypeError, ValueError):
                    raise_parse_error(node, 'Requires sequence of float values')
            return values
        def gds_format_decimal(self, input_data, input_name=''):
            return_value = '%s' % input_data
            if '.' in return_value:
                return_value = return_value.rstrip('0')
                if return_value.endswith('.'):
                    return_value = return_value.rstrip('.')
            return return_value
        def gds_parse_decimal(self, input_data, node=None, input_name=''):
            try:
                decimal_value = decimal_.Decimal(input_data)
            except (TypeError, ValueError):
                raise_parse_error(node, 'Requires decimal value')
            return decimal_value
        def gds_validate_decimal(self, input_data, node=None, input_name=''):
            try:
                value = decimal_.Decimal(input_data)
            except (TypeError, ValueError):
                raise_parse_error(node, 'Requires decimal value')
            return value
        def gds_format_decimal_list(self, input_data, input_name=''):
            if len(input_data) > 0 and not isinstance(input_data[0], BaseStrType_):
                input_data = [str(s) for s in input_data]
            return ' '.join([self.gds_format_decimal(item) for item in input_data])
        def gds_validate_decimal_list(
                self, input_data, node=None, input_name=''):
            values = input_data.split()
            for value in values:
                try:
                    decimal_.Decimal(value)
                except (TypeError, ValueError):
                    raise_parse_error(node, 'Requires sequence of decimal values')
            return values
        def gds_format_double(self, input_data, input_name=''):
            return '%s' % input_data
        def gds_parse_double(self, input_data, node=None, input_name=''):
            try:
                fval_ = float(input_data)
            except (TypeError, ValueError) as exp:
                raise_parse_error(node, 'Requires double or float value: %s' % exp)
            return fval_
        def gds_validate_double(self, input_data, node=None, input_name=''):
            try:
                value = float(input_data)
            except (TypeError, ValueError):
                raise_parse_error(node, 'Requires double or float value')
            return value
        def gds_format_double_list(self, input_data, input_name=''):
            if len(input_data) > 0 and not isinstance(input_data[0], BaseStrType_):
                input_data = [str(s) for s in input_data]
            return '%s' % ' '.join(input_data)
        def gds_validate_double_list(
                self, input_data, node=None, input_name=''):
            values = input_data.split()
            for value in values:
                try:
                    float(value)
                except (TypeError, ValueError):
                    raise_parse_error(
                        node, 'Requires sequence of double or float values')
            return values
        def gds_format_boolean(self, input_data, input_name=''):
            return ('%s' % input_data).lower()
        def gds_parse_boolean(self, input_data, node=None, input_name=''):
            if input_data in ('true', '1'):
                bval = True
            elif input_data in ('false', '0'):
                bval = False
            else:
                raise_parse_error(node, 'Requires boolean value')
            return bval
        def gds_validate_boolean(self, input_data, node=None, input_name=''):
            if input_data not in (True, 1, False, 0, ):
                raise_parse_error(
                    node,
                    'Requires boolean value '
                    '(one of True, 1, False, 0)')
            return input_data
        def gds_format_boolean_list(self, input_data, input_name=''):
            if len(input_data) > 0 and not isinstance(input_data[0], BaseStrType_):
                input_data = [str(s) for s in input_data]
            return '%s' % ' '.join(input_data)
        def gds_validate_boolean_list(
                self, input_data, node=None, input_name=''):
            values = input_data.split()
            for value in values:
                value = self.gds_parse_boolean(value, node, input_name)
                if value not in (True, 1, False, 0, ):
                    raise_parse_error(
                        node,
                        'Requires sequence of boolean values '
                        '(one of True, 1, False, 0)')
            return values
        def gds_validate_datetime(self, input_data, node=None, input_name=''):
            return input_data
        def gds_format_datetime(self, input_data, input_name=''):
            if input_data.microsecond == 0:
                _svalue = '%04d-%02d-%02dT%02d:%02d:%02d' % (
                    input_data.year,
                    input_data.month,
                    input_data.day,
                    input_data.hour,
                    input_data.minute,
                    input_data.second,
                )
            else:
                _svalue = '%04d-%02d-%02dT%02d:%02d:%02d.%s' % (
                    input_data.year,
                    input_data.month,
                    input_data.day,
                    input_data.hour,
                    input_data.minute,
                    input_data.second,
                    ('%f' % (float(input_data.microsecond) / 1000000))[2:],
                )
            if input_data.tzinfo is not None:
                tzoff = input_data.tzinfo.utcoffset(input_data)
                if tzoff is not None:
                    total_seconds = tzoff.seconds + (86400 * tzoff.days)
                    if total_seconds == 0:
                        _svalue += 'Z'
                    else:
                        if total_seconds < 0:
                            _svalue += '-'
                            total_seconds *= -1
                        else:
                            _svalue += '+'
                        hours = total_seconds // 3600
                        minutes = (total_seconds - (hours * 3600)) // 60
                        _svalue += '{0:02d}:{1:02d}'.format(hours, minutes)
            return _svalue
        @classmethod
        def gds_parse_datetime(cls, input_data):
            tz = None
            if input_data[-1] == 'Z':
                tz = GeneratedsSuper._FixedOffsetTZ(0, 'UTC')
                input_data = input_data[:-1]
            else:
                results = GeneratedsSuper.tzoff_pattern.search(input_data)
                if results is not None:
                    tzoff_parts = results.group(2).split(':')
                    tzoff = int(tzoff_parts[0]) * 60 + int(tzoff_parts[1])
                    if results.group(1) == '-':
                        tzoff *= -1
                    tz = GeneratedsSuper._FixedOffsetTZ(
                        tzoff, results.group(0))
                    input_data = input_data[:-6]
            time_parts = input_data.split('.')
            if len(time_parts) > 1:
                micro_seconds = int(float('0.' + time_parts[1]) * 1000000)
                input_data = '%s.%s' % (
                    time_parts[0], "{}".format(micro_seconds).rjust(6, "0"), )
                dt = datetime_.datetime.strptime(
                    input_data, '%Y-%m-%dT%H:%M:%S.%f')
            else:
                dt = datetime_.datetime.strptime(
                    input_data, '%Y-%m-%dT%H:%M:%S')
            dt = dt.replace(tzinfo=tz)
            return dt
        def gds_validate_date(self, input_data, node=None, input_name=''):
            return input_data
        def gds_format_date(self, input_data, input_name=''):
            _svalue = '%04d-%02d-%02d' % (
                input_data.year,
                input_data.month,
                input_data.day,
            )
            try:
                if input_data.tzinfo is not None:
                    tzoff = input_data.tzinfo.utcoffset(input_data)
                    if tzoff is not None:
                        total_seconds = tzoff.seconds + (86400 * tzoff.days)
                        if total_seconds == 0:
                            _svalue += 'Z'
                        else:
                            if total_seconds < 0:
                                _svalue += '-'
                                total_seconds *= -1
                            else:
                                _svalue += '+'
                            hours = total_seconds // 3600
                            minutes = (total_seconds - (hours * 3600)) // 60
                            _svalue += '{0:02d}:{1:02d}'.format(
                                hours, minutes)
            except AttributeError:
                pass
            return _svalue
        @classmethod
        def gds_parse_date(cls, input_data):
            tz = None
            if input_data[-1] == 'Z':
                tz = GeneratedsSuper._FixedOffsetTZ(0, 'UTC')
                input_data = input_data[:-1]
            else:
                results = GeneratedsSuper.tzoff_pattern.search(input_data)
                if results is not None:
                    tzoff_parts = results.group(2).split(':')
                    tzoff = int(tzoff_parts[0]) * 60 + int(tzoff_parts[1])
                    if results.group(1) == '-':
                        tzoff *= -1
                    tz = GeneratedsSuper._FixedOffsetTZ(
                        tzoff, results.group(0))
                    input_data = input_data[:-6]
            dt = datetime_.datetime.strptime(input_data, '%Y-%m-%d')
            dt = dt.replace(tzinfo=tz)
            return dt.date()
        def gds_validate_time(self, input_data, node=None, input_name=''):
            return input_data
        def gds_format_time(self, input_data, input_name=''):
            if input_data.microsecond == 0:
                _svalue = '%02d:%02d:%02d' % (
                    input_data.hour,
                    input_data.minute,
                    input_data.second,
                )
            else:
                _svalue = '%02d:%02d:%02d.%s' % (
                    input_data.hour,
                    input_data.minute,
                    input_data.second,
                    ('%f' % (float(input_data.microsecond) / 1000000))[2:],
                )
            if input_data.tzinfo is not None:
                tzoff = input_data.tzinfo.utcoffset(input_data)
                if tzoff is not None:
                    total_seconds = tzoff.seconds + (86400 * tzoff.days)
                    if total_seconds == 0:
                        _svalue += 'Z'
                    else:
                        if total_seconds < 0:
                            _svalue += '-'
                            total_seconds *= -1
                        else:
                            _svalue += '+'
                        hours = total_seconds // 3600
                        minutes = (total_seconds - (hours * 3600)) // 60
                        _svalue += '{0:02d}:{1:02d}'.format(hours, minutes)
            return _svalue
        def gds_validate_simple_patterns(self, patterns, target):
            # pat is a list of lists of strings/patterns.
            # The target value must match at least one of the patterns
            # in order for the test to succeed.
            found1 = True
            for patterns1 in patterns:
                found2 = False
                for patterns2 in patterns1:
                    mo = re_.search(patterns2, target)
                    if mo is not None and len(mo.group(0)) == len(target):
                        found2 = True
                        break
                if not found2:
                    found1 = False
                    break
            return found1
        @classmethod
        def gds_parse_time(cls, input_data):
            tz = None
            if input_data[-1] == 'Z':
                tz = GeneratedsSuper._FixedOffsetTZ(0, 'UTC')
                input_data = input_data[:-1]
            else:
                results = GeneratedsSuper.tzoff_pattern.search(input_data)
                if results is not None:
                    tzoff_parts = results.group(2).split(':')
                    tzoff = int(tzoff_parts[0]) * 60 + int(tzoff_parts[1])
                    if results.group(1) == '-':
                        tzoff *= -1
                    tz = GeneratedsSuper._FixedOffsetTZ(
                        tzoff, results.group(0))
                    input_data = input_data[:-6]
            if len(input_data.split('.')) > 1:
                dt = datetime_.datetime.strptime(input_data, '%H:%M:%S.%f')
            else:
                dt = datetime_.datetime.strptime(input_data, '%H:%M:%S')
            dt = dt.replace(tzinfo=tz)
            return dt.time()
        def gds_check_cardinality_(
                self, value, input_name,
                min_occurs=0, max_occurs=1, required=None):
            if value is None:
                length = 0
            elif isinstance(value, list):
                length = len(value)
            else:
                length = 1
            if required is not None :
                if required and length < 1:
                    self.gds_collector_.add_message(
                        "Required value {}{} is missing".format(
                            input_name, self.gds_get_node_lineno_()))
            if length < min_occurs:
                self.gds_collector_.add_message(
                    "Number of values for {}{} is below "
                    "the minimum allowed, "
                    "expected at least {}, found {}".format(
                        input_name, self.gds_get_node_lineno_(),
                        min_occurs, length))
            elif length > max_occurs:
                self.gds_collector_.add_message(
                    "Number of values for {}{} is above "
                    "the maximum allowed, "
                    "expected at most {}, found {}".format(
                        input_name, self.gds_get_node_lineno_(),
                        max_occurs, length))
        def gds_validate_builtin_ST_(
                self, validator, value, input_name,
                min_occurs=None, max_occurs=None, required=None):
            if value is not None:
                try:
                    validator(value, input_name=input_name)
                except GDSParseError as parse_error:
                    self.gds_collector_.add_message(str(parse_error))
        def gds_validate_defined_ST_(
                self, validator, value, input_name,
                min_occurs=None, max_occurs=None, required=None):
            if value is not None:
                try:
                    validator(value)
                except GDSParseError as parse_error:
                    self.gds_collector_.add_message(str(parse_error))
        def gds_str_lower(self, instring):
            return instring.lower()
        def get_path_(self, node):
            path_list = []
            self.get_path_list_(node, path_list)
            path_list.reverse()
            path = '/'.join(path_list)
            return path
        Tag_strip_pattern_ = re_.compile(r'\{.*\}')
        def get_path_list_(self, node, path_list):
            if node is None:
                return
            tag = GeneratedsSuper.Tag_strip_pattern_.sub('', node.tag)
            if tag:
                path_list.append(tag)
            self.get_path_list_(node.getparent(), path_list)
        def get_class_obj_(self, node, default_class=None):
            class_obj1 = default_class
            if 'xsi' in node.nsmap:
                classname = node.get('{%s}type' % node.nsmap['xsi'])
                if classname is not None:
                    names = classname.split(':')
                    if len(names) == 2:
                        classname = names[1]
                    class_obj2 = globals().get(classname)
                    if class_obj2 is not None:
                        class_obj1 = class_obj2
            return class_obj1
        def gds_build_any(self, node, type_name=None):
            # provide default value in case option --disable-xml is used.
            content = ""
            content = etree_.tostring(node, encoding="unicode")
            return content
        @classmethod
        def gds_reverse_node_mapping(cls, mapping):
            return dict(((v, k) for k, v in mapping.items()))
        @staticmethod
        def gds_encode(instring):
            if sys.version_info.major == 2:
                if ExternalEncoding:
                    encoding = ExternalEncoding
                else:
                    encoding = 'utf-8'
                return instring.encode(encoding)
            else:
                return instring
        @staticmethod
        def convert_unicode(instring):
            if isinstance(instring, str):
                result = quote_xml(instring)
            elif sys.version_info.major == 2 and isinstance(instring, unicode):
                result = quote_xml(instring).encode('utf8')
            else:
                result = GeneratedsSuper.gds_encode(str(instring))
            return result
        def __eq__(self, other):
            def excl_select_objs_(obj):
                return (obj[0] != 'parent_object_' and
                        obj[0] != 'gds_collector_')
            if type(self) != type(other):
                return False
            return all(x == y for x, y in zip_longest(
                filter(excl_select_objs_, self.__dict__.items()),
                filter(excl_select_objs_, other.__dict__.items())))
        def __ne__(self, other):
            return not self.__eq__(other)
        # Django ETL transform hooks.
        def gds_djo_etl_transform(self):
            pass
        def gds_djo_etl_transform_db_obj(self, dbobj):
            pass
        # SQLAlchemy ETL transform hooks.
        def gds_sqa_etl_transform(self):
            return 0, None
        def gds_sqa_etl_transform_db_obj(self, dbobj):
            pass
        def gds_get_node_lineno_(self):
            if (hasattr(self, "gds_elementtree_node_") and
                    self.gds_elementtree_node_ is not None):
                return ' near line {}'.format(
                    self.gds_elementtree_node_.sourceline)
            else:
                return ""
    
    
    def getSubclassFromModule_(module, class_):
        '''Get the subclass of a class from a specific module.'''
        name = class_.__name__ + 'Sub'
        if hasattr(module, name):
            return getattr(module, name)
        else:
            return None


#
# If you have installed IPython you can uncomment and use the following.
# IPython is available from http://ipython.scipy.org/.
#

## from IPython.Shell import IPShellEmbed
## args = ''
## ipshell = IPShellEmbed(args,
##     banner = 'Dropping into IPython',
##     exit_msg = 'Leaving Interpreter, back to program.')

# Then use the following line where and when you want to drop into the
# IPython shell:
#    ipshell('<some message> -- Entering ipshell.\nHit Ctrl-D to exit')

#
# Globals
#

ExternalEncoding = 'utf-8'
# Set this to false in order to deactivate during export, the use of
# name space prefixes captured from the input document.
UseCapturedNS_ = True
CapturedNsmap_ = {}
Tag_pattern_ = re_.compile(r'({.*})?(.*)')
String_cleanup_pat_ = re_.compile(r"[\n\r\s]+")
Namespace_extract_pat_ = re_.compile(r'{(.*)}(.*)')
CDATA_pattern_ = re_.compile(r"<!\[CDATA\[.*?\]\]>", re_.DOTALL)

# Change this to redirect the generated superclass module to use a
# specific subclass module.
CurrentSubclassModule_ = None

#
# Support/utility functions.
#


def showIndent(outfile, level, pretty_print=True):
    if pretty_print:
        for idx in range(level):
            outfile.write('    ')


def quote_xml(inStr):
    "Escape markup chars, but do not modify CDATA sections."
    if not inStr:
        return ''
    s1 = (isinstance(inStr, BaseStrType_) and inStr or '%s' % inStr)
    s2 = ''
    pos = 0
    matchobjects = CDATA_pattern_.finditer(s1)
    for mo in matchobjects:
        s3 = s1[pos:mo.start()]
        s2 += quote_xml_aux(s3)
        s2 += s1[mo.start():mo.end()]
        pos = mo.end()
    s3 = s1[pos:]
    s2 += quote_xml_aux(s3)
    return s2


def quote_xml_aux(inStr):
    s1 = inStr.replace('&', '&amp;')
    s1 = s1.replace('<', '&lt;')
    s1 = s1.replace('>', '&gt;')
    return s1


def quote_attrib(inStr):
    s1 = (isinstance(inStr, BaseStrType_) and inStr or '%s' % inStr)
    s1 = s1.replace('&', '&amp;')
    s1 = s1.replace('<', '&lt;')
    s1 = s1.replace('>', '&gt;')
    if '"' in s1:
        if "'" in s1:
            s1 = '"%s"' % s1.replace('"', "&quot;")
        else:
            s1 = "'%s'" % s1
    else:
        s1 = '"%s"' % s1
    return s1


def quote_python(inStr):
    s1 = inStr
    if s1.find("'") == -1:
        if s1.find('\n') == -1:
            return "'%s'" % s1
        else:
            return "'''%s'''" % s1
    else:
        if s1.find('"') != -1:
            s1 = s1.replace('"', '\\"')
        if s1.find('\n') == -1:
            return '"%s"' % s1
        else:
            return '"""%s"""' % s1


def get_all_text_(node):
    if node.text is not None:
        text = node.text
    else:
        text = ''
    for child in node:
        if child.tail is not None:
            text += child.tail
    return text


def find_attr_value_(attr_name, node):
    attrs = node.attrib
    attr_parts = attr_name.split(':')
    value = None
    if len(attr_parts) == 1:
        value = attrs.get(attr_name)
    elif len(attr_parts) == 2:
        prefix, name = attr_parts
        if prefix == 'xml':
            namespace = 'http://www.w3.org/XML/1998/namespace'
        else:
            namespace = node.nsmap.get(prefix)
        if namespace is not None:
            value = attrs.get('{%s}%s' % (namespace, name, ))
    return value


def encode_str_2_3(instr):
    return instr


class GDSParseError(Exception):
    pass


def raise_parse_error(node, msg):
    if node is not None:
        msg = '%s (element %s/line %d)' % (msg, node.tag, node.sourceline, )
    raise GDSParseError(msg)


class MixedContainer:
    # Constants for category:
    CategoryNone = 0
    CategoryText = 1
    CategorySimple = 2
    CategoryComplex = 3
    # Constants for content_type:
    TypeNone = 0
    TypeText = 1
    TypeString = 2
    TypeInteger = 3
    TypeFloat = 4
    TypeDecimal = 5
    TypeDouble = 6
    TypeBoolean = 7
    TypeBase64 = 8
    def __init__(self, category, content_type, name, value):
        self.category = category
        self.content_type = content_type
        self.name = name
        self.value = value
    def getCategory(self):
        return self.category
    def getContenttype(self, content_type):
        return self.content_type
    def getValue(self):
        return self.value
    def getName(self):
        return self.name
    def export(self, outfile, level, name, namespace,
               pretty_print=True):
        if self.category == MixedContainer.CategoryText:
            # Prevent exporting empty content as empty lines.
            if self.value.strip():
                outfile.write(self.value)
        elif self.category == MixedContainer.CategorySimple:
            self.exportSimple(outfile, level, name)
        else:    # category == MixedContainer.CategoryComplex
            self.value.export(
                outfile, level, namespace, name_=name,
                pretty_print=pretty_print)
    def exportSimple(self, outfile, level, name):
        if self.content_type == MixedContainer.TypeString:
            outfile.write('<%s>%s</%s>' % (
                self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeInteger or \
                self.content_type == MixedContainer.TypeBoolean:
            outfile.write('<%s>%d</%s>' % (
                self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeFloat or \
                self.content_type == MixedContainer.TypeDecimal:
            outfile.write('<%s>%f</%s>' % (
                self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeDouble:
            outfile.write('<%s>%g</%s>' % (
                self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeBase64:
            outfile.write('<%s>%s</%s>' % (
                self.name,
                base64.b64encode(self.value),
                self.name))
    def to_etree(self, element, mapping_=None, nsmap_=None):
        if self.category == MixedContainer.CategoryText:
            # Prevent exporting empty content as empty lines.
            if self.value.strip():
                if len(element) > 0:
                    if element[-1].tail is None:
                        element[-1].tail = self.value
                    else:
                        element[-1].tail += self.value
                else:
                    if element.text is None:
                        element.text = self.value
                    else:
                        element.text += self.value
        elif self.category == MixedContainer.CategorySimple:
            subelement = etree_.SubElement(
                element, '%s' % self.name)
            subelement.text = self.to_etree_simple()
        else:    # category == MixedContainer.CategoryComplex
            self.value.to_etree(element)
    def to_etree_simple(self, mapping_=None, nsmap_=None):
        if self.content_type == MixedContainer.TypeString:
            text = self.value
        elif (self.content_type == MixedContainer.TypeInteger or
                self.content_type == MixedContainer.TypeBoolean):
            text = '%d' % self.value
        elif (self.content_type == MixedContainer.TypeFloat or
                self.content_type == MixedContainer.TypeDecimal):
            text = '%f' % self.value
        elif self.content_type == MixedContainer.TypeDouble:
            text = '%g' % self.value
        elif self.content_type == MixedContainer.TypeBase64:
            text = '%s' % base64.b64encode(self.value)
        return text
    def exportLiteral(self, outfile, level, name):
        if self.category == MixedContainer.CategoryText:
            showIndent(outfile, level)
            outfile.write(
                'model_.MixedContainer(%d, %d, "%s", "%s"),\n' % (
                    self.category, self.content_type,
                    self.name, self.value))
        elif self.category == MixedContainer.CategorySimple:
            showIndent(outfile, level)
            outfile.write(
                'model_.MixedContainer(%d, %d, "%s", "%s"),\n' % (
                    self.category, self.content_type,
                    self.name, self.value))
        else:    # category == MixedContainer.CategoryComplex
            showIndent(outfile, level)
            outfile.write(
                'model_.MixedContainer(%d, %d, "%s",\n' % (
                    self.category, self.content_type, self.name,))
            self.value.exportLiteral(outfile, level + 1)
            showIndent(outfile, level)
            outfile.write(')\n')


class MemberSpec_(object):
    def __init__(self, name='', data_type='', container=0,
            optional=0, child_attrs=None, choice=None):
        self.name = name
        self.data_type = data_type
        self.container = container
        self.child_attrs = child_attrs
        self.choice = choice
        self.optional = optional
    def set_name(self, name): self.name = name
    def get_name(self): return self.name
    def set_data_type(self, data_type): self.data_type = data_type
    def get_data_type_chain(self): return self.data_type
    def get_data_type(self):
        if isinstance(self.data_type, list):
            if len(self.data_type) > 0:
                return self.data_type[-1]
            else:
                return 'xs:string'
        else:
            return self.data_type
    def set_container(self, container): self.container = container
    def get_container(self): return self.container
    def set_child_attrs(self, child_attrs): self.child_attrs = child_attrs
    def get_child_attrs(self): return self.child_attrs
    def set_choice(self, choice): self.choice = choice
    def get_choice(self): return self.choice
    def set_optional(self, optional): self.optional = optional
    def get_optional(self): return self.optional


def _cast(typ, value):
    if typ is None or value is None:
        return value
    return typ(value)

#
# Data representation classes.
#


class real(GeneratedsSuper):
    """Meta data element definition for a real measurement quantity.
    The following statements of a real quantity are possible.
    [(m)-mandatory, (o)-optional]
    1. Basic measured quantity
    (o) - element label (string)
    (m) - element value (decimal value type)
    (m) - element unit (string - SI format)
    (o) - element dateTime (xs:dateTime)
    2. Measured quantity with expanded measurement uncertainty
    (o) - element label (string)
    (m) - element value (decimal value type)
    (m) - element unit (string - SI format)
    (o) - element dateTime (xs:dateTime)
    (m) - element expandedUnc (element type expandedUnc - sub structure)
    3. Measured quantity with uncertainty coverage interval (probabilistic-
    symmetric)
    (o) - element label (string)
    (m) - element value (decimal value type)
    (m) - element unit (string - SI format)
    (o) - element dateTime (xs:dateTime)
    (m) - element coverageInterval (element type coverageInterval - sub
    structure)
    Integration into external XML:
    <myXML xmlns:xs="http://www.w3.org/2001/XMLSchema"
    xmlns:si="https://ptb.de/si">
    <xs:element name="individualElement">
    <xs:complexType>
    <xs:sequence>
    <xs:element ref="si:real"/>
    </xs:sequence>
    </xs:complexType>
    </xs:element>
    </mxXML>"""
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, label=None, value=None, unit=None, dateTime=None, expandedUnc=None, coverageInterval=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = "si"
        self.label = label
        self.label_nsprefix_ = "si"
        self.value = value
        self.validate_decimalType(self.value)
        self.value_nsprefix_ = "si"
        self.unit = unit
        self.validate_unitType(self.unit)
        self.unit_nsprefix_ = "si"
        if isinstance(dateTime, BaseStrType_):
            initvalue_ = datetime_.datetime.strptime(dateTime, '%Y-%m-%dT%H:%M:%S')
        else:
            initvalue_ = dateTime
        self.dateTime = initvalue_
        self.dateTime_nsprefix_ = "si"
        self.expandedUnc = expandedUnc
        self.expandedUnc_nsprefix_ = "si"
        self.coverageInterval = coverageInterval
        self.coverageInterval_nsprefix_ = "si"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, real)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if real.subclass:
            return real.subclass(*args_, **kwargs_)
        else:
            return real(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_label(self):
        return self.label
    def set_label(self, label):
        self.label = label
    def get_value(self):
        return self.value
    def set_value(self, value):
        self.value = value
    def get_unit(self):
        return self.unit
    def set_unit(self, unit):
        self.unit = unit
    def get_dateTime(self):
        return self.dateTime
    def set_dateTime(self, dateTime):
        self.dateTime = dateTime
    def get_expandedUnc(self):
        return self.expandedUnc
    def set_expandedUnc(self, expandedUnc):
        self.expandedUnc = expandedUnc
    def get_coverageInterval(self):
        return self.coverageInterval
    def set_coverageInterval(self, coverageInterval):
        self.coverageInterval = coverageInterval
    def validate_decimalType(self, value):
        result = True
        # Validate type decimalType, a restriction on xs:double.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, float):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (float)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_decimalType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_decimalType_patterns_, ))
                result = False
        return result
    validate_decimalType_patterns_ = [['^([-+]?((\\d*\\.\\d+)|(\\d+\\.\\d*)|(\\d+\\.?))([Ee][-+]?\\d+)?)$']]
    def validate_unitType(self, value):
        result = True
        # Validate type unitType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            pass
        return result
    def hasContent_(self):
        if (
            self.label is not None or
            self.value is not None or
            self.unit is not None or
            self.dateTime is not None or
            self.expandedUnc is not None or
            self.coverageInterval is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:si="https://ptb.de/si"', name_='real', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('real')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'real':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='real')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='real', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='real'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:si="https://ptb.de/si"', name_='real', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.label is not None:
            namespaceprefix_ = self.label_nsprefix_ + ':' if (UseCapturedNS_ and self.label_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%slabel>%s</%slabel>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.label), input_name='label')), namespaceprefix_ , eol_))
        if self.value is not None:
            namespaceprefix_ = self.value_nsprefix_ + ':' if (UseCapturedNS_ and self.value_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%svalue>%s</%svalue>%s' % (namespaceprefix_ , self.gds_format_double(self.value, input_name='value'), namespaceprefix_ , eol_))
        if self.unit is not None:
            namespaceprefix_ = self.unit_nsprefix_ + ':' if (UseCapturedNS_ and self.unit_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sunit>%s</%sunit>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.unit), input_name='unit')), namespaceprefix_ , eol_))
        if self.dateTime is not None:
            namespaceprefix_ = self.dateTime_nsprefix_ + ':' if (UseCapturedNS_ and self.dateTime_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sdateTime>%s</%sdateTime>%s' % (namespaceprefix_ , self.gds_format_datetime(self.dateTime, input_name='dateTime'), namespaceprefix_ , eol_))
        if self.expandedUnc is not None:
            namespaceprefix_ = self.expandedUnc_nsprefix_ + ':' if (UseCapturedNS_ and self.expandedUnc_nsprefix_) else ''
            self.expandedUnc.export(outfile, level, namespaceprefix_='si:', namespacedef_='', name_='expandedUnc', pretty_print=pretty_print)
        if self.coverageInterval is not None:
            namespaceprefix_ = self.coverageInterval_nsprefix_ + ':' if (UseCapturedNS_ and self.coverageInterval_nsprefix_) else ''
            self.coverageInterval.export(outfile, level, namespaceprefix_='si:', namespacedef_='', name_='coverageInterval', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='real', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{https://ptb.de/si}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{https://ptb.de/si}' + name_, nsmap=nsmap_)
        if self.label is not None:
            label_ = self.label
            etree_.SubElement(element, '{https://ptb.de/si}label').text = self.gds_format_string(label_)
        if self.value is not None:
            value_ = self.value
            etree_.SubElement(element, '{https://ptb.de/si}value').text = self.gds_format_double(value_)
        if self.unit is not None:
            unit_ = self.unit
            etree_.SubElement(element, '{https://ptb.de/si}unit').text = self.gds_format_string(unit_)
        if self.dateTime is not None:
            dateTime_ = self.dateTime
            etree_.SubElement(element, '{https://ptb.de/si}dateTime').text = self.gds_format_datetime(dateTime_)
        if self.expandedUnc is not None:
            expandedUnc_ = self.expandedUnc
            expandedUnc_.to_etree(element, name_='expandedUnc', mapping_=mapping_, nsmap_=nsmap_)
        if self.coverageInterval is not None:
            coverageInterval_ = self.coverageInterval
            coverageInterval_.to_etree(element, name_='coverageInterval', mapping_=mapping_, nsmap_=nsmap_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'label':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'label')
            value_ = self.gds_validate_string(value_, node, 'label')
            self.label = value_
            self.label_nsprefix_ = child_.prefix
        elif nodeName_ == 'value' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_double(sval_, node, 'value')
            fval_ = self.gds_validate_double(fval_, node, 'value')
            self.value = fval_
            self.value_nsprefix_ = child_.prefix
            # validate type decimalType
            self.validate_decimalType(self.value)
        elif nodeName_ == 'unit':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'unit')
            value_ = self.gds_validate_string(value_, node, 'unit')
            self.unit = value_
            self.unit_nsprefix_ = child_.prefix
            # validate type unitType
            self.validate_unitType(self.unit)
        elif nodeName_ == 'dateTime':
            sval_ = child_.text
            dval_ = self.gds_parse_datetime(sval_)
            self.dateTime = dval_
            self.dateTime_nsprefix_ = child_.prefix
        elif nodeName_ == 'expandedUnc':
            obj_ = expandedUnc.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.expandedUnc = obj_
            obj_.original_tagname_ = 'expandedUnc'
        elif nodeName_ == 'coverageInterval':
            obj_ = coverageInterval.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.coverageInterval = obj_
            obj_.original_tagname_ = 'coverageInterval'
# end class real


class expandedUnc(GeneratedsSuper):
    """Definition of the structure, that gives the necessary components for
    stating
    an expanded measurement uncertainty. This element must always be used in
    the
    context of a real quantity, which is an application within si:real and/or
    si:globalUnivariateUnc.
    The element has the following components [(m)-mandatory, (o)-optional]:
    (m) - element uncertainty (decimal value >= 0)
    (m) - element coverageFactor (decimal value >= 1)
    (m) - element coverageProbability (decimal value in [0,1])
    (o) - element distribution (string)
    The unit of component uncertainty is the unit used in the context of
    si:real and/or si:globalUnivariateUnc."""
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, uncertainty=None, coverageFactor=None, coverageProbability=None, distribution=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = "si"
        self.uncertainty = uncertainty
        self.validate_uncertaintyValueType(self.uncertainty)
        self.uncertainty_nsprefix_ = "si"
        self.coverageFactor = coverageFactor
        self.validate_kValueType(self.coverageFactor)
        self.coverageFactor_nsprefix_ = "si"
        self.coverageProbability = coverageProbability
        self.validate_probabilityValueType(self.coverageProbability)
        self.coverageProbability_nsprefix_ = "si"
        self.distribution = distribution
        self.distribution_nsprefix_ = "si"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, expandedUnc)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if expandedUnc.subclass:
            return expandedUnc.subclass(*args_, **kwargs_)
        else:
            return expandedUnc(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_uncertainty(self):
        return self.uncertainty
    def set_uncertainty(self, uncertainty):
        self.uncertainty = uncertainty
    def get_coverageFactor(self):
        return self.coverageFactor
    def set_coverageFactor(self, coverageFactor):
        self.coverageFactor = coverageFactor
    def get_coverageProbability(self):
        return self.coverageProbability
    def set_coverageProbability(self, coverageProbability):
        self.coverageProbability = coverageProbability
    def get_distribution(self):
        return self.distribution
    def set_distribution(self, distribution):
        self.distribution = distribution
    def validate_uncertaintyValueType(self, value):
        result = True
        # Validate type uncertaintyValueType, a restriction on xs:double.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, float):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (float)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_uncertaintyValueType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_uncertaintyValueType_patterns_, ))
                result = False
        return result
    validate_uncertaintyValueType_patterns_ = [['^(\\+?((\\d*\\.\\d+)|(\\d+\\.\\d*)|(\\d+\\.?))([Ee][-+]?\\d+)?)$']]
    def validate_kValueType(self, value):
        result = True
        # Validate type kValueType, a restriction on xs:double.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, float):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (float)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_kValueType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_kValueType_patterns_, ))
                result = False
        return result
    validate_kValueType_patterns_ = [['^(\\+?(([1-9]\\d*\\.\\d*)|([1-9]\\d*)))$']]
    def validate_probabilityValueType(self, value):
        result = True
        # Validate type probabilityValueType, a restriction on xs:double.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, float):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (float)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_probabilityValueType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_probabilityValueType_patterns_, ))
                result = False
        return result
    validate_probabilityValueType_patterns_ = [['^(\\+?((0(\\.\\d*)?)|(1(\\.0*)?)))$']]
    def hasContent_(self):
        if (
            self.uncertainty is not None or
            self.coverageFactor is not None or
            self.coverageProbability is not None or
            self.distribution is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:si="https://ptb.de/si"', name_='expandedUnc', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('expandedUnc')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'expandedUnc':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='expandedUnc')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='expandedUnc', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='expandedUnc'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:si="https://ptb.de/si"', name_='expandedUnc', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.uncertainty is not None:
            namespaceprefix_ = self.uncertainty_nsprefix_ + ':' if (UseCapturedNS_ and self.uncertainty_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%suncertainty>%s</%suncertainty>%s' % (namespaceprefix_ , self.gds_format_double(self.uncertainty, input_name='uncertainty'), namespaceprefix_ , eol_))
        if self.coverageFactor is not None:
            namespaceprefix_ = self.coverageFactor_nsprefix_ + ':' if (UseCapturedNS_ and self.coverageFactor_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scoverageFactor>%s</%scoverageFactor>%s' % (namespaceprefix_ , self.gds_format_double(self.coverageFactor, input_name='coverageFactor'), namespaceprefix_ , eol_))
        if self.coverageProbability is not None:
            namespaceprefix_ = self.coverageProbability_nsprefix_ + ':' if (UseCapturedNS_ and self.coverageProbability_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scoverageProbability>%s</%scoverageProbability>%s' % (namespaceprefix_ , self.gds_format_double(self.coverageProbability, input_name='coverageProbability'), namespaceprefix_ , eol_))
        if self.distribution is not None:
            namespaceprefix_ = self.distribution_nsprefix_ + ':' if (UseCapturedNS_ and self.distribution_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sdistribution>%s</%sdistribution>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.distribution), input_name='distribution')), namespaceprefix_ , eol_))
    def to_etree(self, parent_element=None, name_='expandedUnc', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{https://ptb.de/si}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{https://ptb.de/si}' + name_, nsmap=nsmap_)
        if self.uncertainty is not None:
            uncertainty_ = self.uncertainty
            etree_.SubElement(element, '{https://ptb.de/si}uncertainty').text = self.gds_format_double(uncertainty_)
        if self.coverageFactor is not None:
            coverageFactor_ = self.coverageFactor
            etree_.SubElement(element, '{https://ptb.de/si}coverageFactor').text = self.gds_format_double(coverageFactor_)
        if self.coverageProbability is not None:
            coverageProbability_ = self.coverageProbability
            etree_.SubElement(element, '{https://ptb.de/si}coverageProbability').text = self.gds_format_double(coverageProbability_)
        if self.distribution is not None:
            distribution_ = self.distribution
            etree_.SubElement(element, '{https://ptb.de/si}distribution').text = self.gds_format_string(distribution_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'uncertainty' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_double(sval_, node, 'uncertainty')
            fval_ = self.gds_validate_double(fval_, node, 'uncertainty')
            self.uncertainty = fval_
            self.uncertainty_nsprefix_ = child_.prefix
            # validate type uncertaintyValueType
            self.validate_uncertaintyValueType(self.uncertainty)
        elif nodeName_ == 'coverageFactor' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_double(sval_, node, 'coverageFactor')
            fval_ = self.gds_validate_double(fval_, node, 'coverageFactor')
            self.coverageFactor = fval_
            self.coverageFactor_nsprefix_ = child_.prefix
            # validate type kValueType
            self.validate_kValueType(self.coverageFactor)
        elif nodeName_ == 'coverageProbability' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_double(sval_, node, 'coverageProbability')
            fval_ = self.gds_validate_double(fval_, node, 'coverageProbability')
            self.coverageProbability = fval_
            self.coverageProbability_nsprefix_ = child_.prefix
            # validate type probabilityValueType
            self.validate_probabilityValueType(self.coverageProbability)
        elif nodeName_ == 'distribution':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'distribution')
            value_ = self.gds_validate_string(value_, node, 'distribution')
            self.distribution = value_
            self.distribution_nsprefix_ = child_.prefix
# end class expandedUnc


class coverageInterval(GeneratedsSuper):
    """Definition of the structure, that gives the necessary components for
    stating
    a probabilistic-symmetric coverage interval for a real uncertainty. This
    element
    must always be used in the context of a real quantity, which is an
    application
    within si:real and/or si:globalUnivariateUnc.
    The element has the following components [(m)-mandatory, (o)-optional]:
    (m) - element stdUncertainty (decimal value >= 0)
    (m) - element intervalMin (decimal value type)
    (m) - element intervalMax (decimal value type)
    (m) - element coverageProbability (decimal value in [0,1])
    (o) - element distribution (string)
    The unit of components stdUncertainty, intervalMin and intervalMax is the
    unit
    used in the context of si:real and/or si:globalUnivaraiteUnc."""
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, standardUnc=None, intervalMin=None, intervalMax=None, coverageProbability=None, distribution=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = "si"
        self.standardUnc = standardUnc
        self.validate_uncertaintyValueType(self.standardUnc)
        self.standardUnc_nsprefix_ = "si"
        self.intervalMin = intervalMin
        self.validate_decimalType(self.intervalMin)
        self.intervalMin_nsprefix_ = "si"
        self.intervalMax = intervalMax
        self.validate_decimalType(self.intervalMax)
        self.intervalMax_nsprefix_ = "si"
        self.coverageProbability = coverageProbability
        self.validate_probabilityValueType(self.coverageProbability)
        self.coverageProbability_nsprefix_ = "si"
        self.distribution = distribution
        self.distribution_nsprefix_ = "si"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, coverageInterval)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if coverageInterval.subclass:
            return coverageInterval.subclass(*args_, **kwargs_)
        else:
            return coverageInterval(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_standardUnc(self):
        return self.standardUnc
    def set_standardUnc(self, standardUnc):
        self.standardUnc = standardUnc
    def get_intervalMin(self):
        return self.intervalMin
    def set_intervalMin(self, intervalMin):
        self.intervalMin = intervalMin
    def get_intervalMax(self):
        return self.intervalMax
    def set_intervalMax(self, intervalMax):
        self.intervalMax = intervalMax
    def get_coverageProbability(self):
        return self.coverageProbability
    def set_coverageProbability(self, coverageProbability):
        self.coverageProbability = coverageProbability
    def get_distribution(self):
        return self.distribution
    def set_distribution(self, distribution):
        self.distribution = distribution
    def validate_uncertaintyValueType(self, value):
        result = True
        # Validate type uncertaintyValueType, a restriction on xs:double.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, float):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (float)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_uncertaintyValueType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_uncertaintyValueType_patterns_, ))
                result = False
        return result
    validate_uncertaintyValueType_patterns_ = [['^(\\+?((\\d*\\.\\d+)|(\\d+\\.\\d*)|(\\d+\\.?))([Ee][-+]?\\d+)?)$']]
    def validate_decimalType(self, value):
        result = True
        # Validate type decimalType, a restriction on xs:double.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, float):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (float)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_decimalType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_decimalType_patterns_, ))
                result = False
        return result
    validate_decimalType_patterns_ = [['^([-+]?((\\d*\\.\\d+)|(\\d+\\.\\d*)|(\\d+\\.?))([Ee][-+]?\\d+)?)$']]
    def validate_probabilityValueType(self, value):
        result = True
        # Validate type probabilityValueType, a restriction on xs:double.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, float):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (float)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_probabilityValueType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_probabilityValueType_patterns_, ))
                result = False
        return result
    validate_probabilityValueType_patterns_ = [['^(\\+?((0(\\.\\d*)?)|(1(\\.0*)?)))$']]
    def hasContent_(self):
        if (
            self.standardUnc is not None or
            self.intervalMin is not None or
            self.intervalMax is not None or
            self.coverageProbability is not None or
            self.distribution is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:si="https://ptb.de/si"', name_='coverageInterval', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('coverageInterval')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'coverageInterval':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='coverageInterval')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='coverageInterval', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='coverageInterval'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:si="https://ptb.de/si"', name_='coverageInterval', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.standardUnc is not None:
            namespaceprefix_ = self.standardUnc_nsprefix_ + ':' if (UseCapturedNS_ and self.standardUnc_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sstandardUnc>%s</%sstandardUnc>%s' % (namespaceprefix_ , self.gds_format_double(self.standardUnc, input_name='standardUnc'), namespaceprefix_ , eol_))
        if self.intervalMin is not None:
            namespaceprefix_ = self.intervalMin_nsprefix_ + ':' if (UseCapturedNS_ and self.intervalMin_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sintervalMin>%s</%sintervalMin>%s' % (namespaceprefix_ , self.gds_format_double(self.intervalMin, input_name='intervalMin'), namespaceprefix_ , eol_))
        if self.intervalMax is not None:
            namespaceprefix_ = self.intervalMax_nsprefix_ + ':' if (UseCapturedNS_ and self.intervalMax_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sintervalMax>%s</%sintervalMax>%s' % (namespaceprefix_ , self.gds_format_double(self.intervalMax, input_name='intervalMax'), namespaceprefix_ , eol_))
        if self.coverageProbability is not None:
            namespaceprefix_ = self.coverageProbability_nsprefix_ + ':' if (UseCapturedNS_ and self.coverageProbability_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scoverageProbability>%s</%scoverageProbability>%s' % (namespaceprefix_ , self.gds_format_double(self.coverageProbability, input_name='coverageProbability'), namespaceprefix_ , eol_))
        if self.distribution is not None:
            namespaceprefix_ = self.distribution_nsprefix_ + ':' if (UseCapturedNS_ and self.distribution_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sdistribution>%s</%sdistribution>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.distribution), input_name='distribution')), namespaceprefix_ , eol_))
    def to_etree(self, parent_element=None, name_='coverageInterval', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{https://ptb.de/si}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{https://ptb.de/si}' + name_, nsmap=nsmap_)
        if self.standardUnc is not None:
            standardUnc_ = self.standardUnc
            etree_.SubElement(element, '{https://ptb.de/si}standardUnc').text = self.gds_format_double(standardUnc_)
        if self.intervalMin is not None:
            intervalMin_ = self.intervalMin
            etree_.SubElement(element, '{https://ptb.de/si}intervalMin').text = self.gds_format_double(intervalMin_)
        if self.intervalMax is not None:
            intervalMax_ = self.intervalMax
            etree_.SubElement(element, '{https://ptb.de/si}intervalMax').text = self.gds_format_double(intervalMax_)
        if self.coverageProbability is not None:
            coverageProbability_ = self.coverageProbability
            etree_.SubElement(element, '{https://ptb.de/si}coverageProbability').text = self.gds_format_double(coverageProbability_)
        if self.distribution is not None:
            distribution_ = self.distribution
            etree_.SubElement(element, '{https://ptb.de/si}distribution').text = self.gds_format_string(distribution_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'standardUnc' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_double(sval_, node, 'standardUnc')
            fval_ = self.gds_validate_double(fval_, node, 'standardUnc')
            self.standardUnc = fval_
            self.standardUnc_nsprefix_ = child_.prefix
            # validate type uncertaintyValueType
            self.validate_uncertaintyValueType(self.standardUnc)
        elif nodeName_ == 'intervalMin' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_double(sval_, node, 'intervalMin')
            fval_ = self.gds_validate_double(fval_, node, 'intervalMin')
            self.intervalMin = fval_
            self.intervalMin_nsprefix_ = child_.prefix
            # validate type decimalType
            self.validate_decimalType(self.intervalMin)
        elif nodeName_ == 'intervalMax' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_double(sval_, node, 'intervalMax')
            fval_ = self.gds_validate_double(fval_, node, 'intervalMax')
            self.intervalMax = fval_
            self.intervalMax_nsprefix_ = child_.prefix
            # validate type decimalType
            self.validate_decimalType(self.intervalMax)
        elif nodeName_ == 'coverageProbability' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_double(sval_, node, 'coverageProbability')
            fval_ = self.gds_validate_double(fval_, node, 'coverageProbability')
            self.coverageProbability = fval_
            self.coverageProbability_nsprefix_ = child_.prefix
            # validate type probabilityValueType
            self.validate_probabilityValueType(self.coverageProbability)
        elif nodeName_ == 'distribution':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'distribution')
            value_ = self.gds_validate_string(value_, node, 'distribution')
            self.distribution = value_
            self.distribution_nsprefix_ = child_.prefix
# end class coverageInterval


class constant(GeneratedsSuper):
    """Definition of a structure for real numbers, that represent for
    fundamental
    physical constants and mathematical constants.
    The element has the following components [(m)-mandatory, (o)-optional]:
    (o) - element label (string)
    (m) - element value (decimal value type)
    (m) - element unit (string - SI unit)
    (o) - element dateTime (xs:dateTime)
    (o) - element uncertainty (decimal value >= 0)
    (o) - element distribution (string)
    The value and the uncertainty have the unit specified by the element unit.
    For fundamental physical constants, that are defined experimentally, the
    uncertainty is the standard deviation.
    For rounded mathematical constants, the uncertainty is the standard
    deviation
    of a rectangular distribution (element value defines center point), that
    contains the exact value of the constant with 100 percent probability."""
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, label=None, value=None, unit=None, dateTime=None, uncertainty=None, distribution=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = "si"
        self.label = label
        self.label_nsprefix_ = "si"
        self.value = value
        self.validate_decimalType(self.value)
        self.value_nsprefix_ = "si"
        self.unit = unit
        self.validate_unitType(self.unit)
        self.unit_nsprefix_ = "si"
        if isinstance(dateTime, BaseStrType_):
            initvalue_ = datetime_.datetime.strptime(dateTime, '%Y-%m-%dT%H:%M:%S')
        else:
            initvalue_ = dateTime
        self.dateTime = initvalue_
        self.dateTime_nsprefix_ = "si"
        self.uncertainty = uncertainty
        self.validate_uncertaintyValueType(self.uncertainty)
        self.uncertainty_nsprefix_ = "si"
        self.distribution = distribution
        self.distribution_nsprefix_ = "si"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, constant)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if constant.subclass:
            return constant.subclass(*args_, **kwargs_)
        else:
            return constant(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_label(self):
        return self.label
    def set_label(self, label):
        self.label = label
    def get_value(self):
        return self.value
    def set_value(self, value):
        self.value = value
    def get_unit(self):
        return self.unit
    def set_unit(self, unit):
        self.unit = unit
    def get_dateTime(self):
        return self.dateTime
    def set_dateTime(self, dateTime):
        self.dateTime = dateTime
    def get_uncertainty(self):
        return self.uncertainty
    def set_uncertainty(self, uncertainty):
        self.uncertainty = uncertainty
    def get_distribution(self):
        return self.distribution
    def set_distribution(self, distribution):
        self.distribution = distribution
    def validate_decimalType(self, value):
        result = True
        # Validate type decimalType, a restriction on xs:double.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, float):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (float)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_decimalType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_decimalType_patterns_, ))
                result = False
        return result
    validate_decimalType_patterns_ = [['^([-+]?((\\d*\\.\\d+)|(\\d+\\.\\d*)|(\\d+\\.?))([Ee][-+]?\\d+)?)$']]
    def validate_unitType(self, value):
        result = True
        # Validate type unitType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            pass
        return result
    def validate_uncertaintyValueType(self, value):
        result = True
        # Validate type uncertaintyValueType, a restriction on xs:double.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, float):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (float)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_uncertaintyValueType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_uncertaintyValueType_patterns_, ))
                result = False
        return result
    validate_uncertaintyValueType_patterns_ = [['^(\\+?((\\d*\\.\\d+)|(\\d+\\.\\d*)|(\\d+\\.?))([Ee][-+]?\\d+)?)$']]
    def hasContent_(self):
        if (
            self.label is not None or
            self.value is not None or
            self.unit is not None or
            self.dateTime is not None or
            self.uncertainty is not None or
            self.distribution is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:si="https://ptb.de/si"', name_='constant', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('constant')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'constant':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='constant')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='constant', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='constant'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:si="https://ptb.de/si"', name_='constant', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.label is not None:
            namespaceprefix_ = self.label_nsprefix_ + ':' if (UseCapturedNS_ and self.label_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%slabel>%s</%slabel>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.label), input_name='label')), namespaceprefix_ , eol_))
        if self.value is not None:
            namespaceprefix_ = self.value_nsprefix_ + ':' if (UseCapturedNS_ and self.value_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%svalue>%s</%svalue>%s' % (namespaceprefix_ , self.gds_format_double(self.value, input_name='value'), namespaceprefix_ , eol_))
        if self.unit is not None:
            namespaceprefix_ = self.unit_nsprefix_ + ':' if (UseCapturedNS_ and self.unit_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sunit>%s</%sunit>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.unit), input_name='unit')), namespaceprefix_ , eol_))
        if self.dateTime is not None:
            namespaceprefix_ = self.dateTime_nsprefix_ + ':' if (UseCapturedNS_ and self.dateTime_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sdateTime>%s</%sdateTime>%s' % (namespaceprefix_ , self.gds_format_datetime(self.dateTime, input_name='dateTime'), namespaceprefix_ , eol_))
        if self.uncertainty is not None:
            namespaceprefix_ = self.uncertainty_nsprefix_ + ':' if (UseCapturedNS_ and self.uncertainty_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%suncertainty>%s</%suncertainty>%s' % (namespaceprefix_ , self.gds_format_double(self.uncertainty, input_name='uncertainty'), namespaceprefix_ , eol_))
        if self.distribution is not None:
            namespaceprefix_ = self.distribution_nsprefix_ + ':' if (UseCapturedNS_ and self.distribution_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sdistribution>%s</%sdistribution>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.distribution), input_name='distribution')), namespaceprefix_ , eol_))
    def to_etree(self, parent_element=None, name_='constant', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{https://ptb.de/si}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{https://ptb.de/si}' + name_, nsmap=nsmap_)
        if self.label is not None:
            label_ = self.label
            etree_.SubElement(element, '{https://ptb.de/si}label').text = self.gds_format_string(label_)
        if self.value is not None:
            value_ = self.value
            etree_.SubElement(element, '{https://ptb.de/si}value').text = self.gds_format_double(value_)
        if self.unit is not None:
            unit_ = self.unit
            etree_.SubElement(element, '{https://ptb.de/si}unit').text = self.gds_format_string(unit_)
        if self.dateTime is not None:
            dateTime_ = self.dateTime
            etree_.SubElement(element, '{https://ptb.de/si}dateTime').text = self.gds_format_datetime(dateTime_)
        if self.uncertainty is not None:
            uncertainty_ = self.uncertainty
            etree_.SubElement(element, '{https://ptb.de/si}uncertainty').text = self.gds_format_double(uncertainty_)
        if self.distribution is not None:
            distribution_ = self.distribution
            etree_.SubElement(element, '{https://ptb.de/si}distribution').text = self.gds_format_string(distribution_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'label':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'label')
            value_ = self.gds_validate_string(value_, node, 'label')
            self.label = value_
            self.label_nsprefix_ = child_.prefix
        elif nodeName_ == 'value' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_double(sval_, node, 'value')
            fval_ = self.gds_validate_double(fval_, node, 'value')
            self.value = fval_
            self.value_nsprefix_ = child_.prefix
            # validate type decimalType
            self.validate_decimalType(self.value)
        elif nodeName_ == 'unit':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'unit')
            value_ = self.gds_validate_string(value_, node, 'unit')
            self.unit = value_
            self.unit_nsprefix_ = child_.prefix
            # validate type unitType
            self.validate_unitType(self.unit)
        elif nodeName_ == 'dateTime':
            sval_ = child_.text
            dval_ = self.gds_parse_datetime(sval_)
            self.dateTime = dval_
            self.dateTime_nsprefix_ = child_.prefix
        elif nodeName_ == 'uncertainty' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_double(sval_, node, 'uncertainty')
            fval_ = self.gds_validate_double(fval_, node, 'uncertainty')
            self.uncertainty = fval_
            self.uncertainty_nsprefix_ = child_.prefix
            # validate type uncertaintyValueType
            self.validate_uncertaintyValueType(self.uncertainty)
        elif nodeName_ == 'distribution':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'distribution')
            value_ = self.gds_validate_string(value_, node, 'distribution')
            self.distribution = value_
            self.distribution_nsprefix_ = child_.prefix
# end class constant


class complex(GeneratedsSuper):
    """The definition of complex quantities in the D-SI meta data model.
    Complex quantities allow two representations of complex numerical values:
    One is the Cartesian coordinate form, the other representation is the
    polar coordinate form.
    The following statements of a complex quantity are possible.
    [(m)-mandatory, (o)-optional]
    1. Basic measured quantity in Cartesian form
    (o) - element label (string)
    (m) - element valueReal (decimal value type)
    (m) - element valueImag (decimal value type)
    (m) - element unit (string - SI unit)
    (o) - element dateTime (xs:dateTime)
    2. Basic measured quantity in polar form
    (o) - element label (string)
    (m) - element valueMagnitude (decimal value type)
    (m) - element valuePhase (decimal value type)
    (m) - element unit (string - SI unit)
    (m) - element unitPhase (string - SI unit for an angular quantity)
    (o) - element dateTime (xs:dateTime)
    3. Basic measured quantity in Cartesian form with ellipsoidal coverage
    region
    (o) - element label (string)
    (m) - element valueReal (decimal value type)
    (m) - element valueImag (decimal value type)
    (m) - element unit (string - SI unit)
    (o) - element dateTime (xs:dateTime)
    (m) - element ellipsoidalRegion (element type ellipsoidalRegion - sub
    structure)
    4. Basic measured quantity in polar form with ellipsoidal coverage region
    (o) - element label (string)
    (m) - element valueMagnitude (decimal value type)
    (m) - element valuePhase (decimal value type)
    (m) - element unit (string - SI unit)
    (m) - element unitPhase (string - SI unit for an angular quantity)
    (o) - element dateTime (xs:dateTime)
    (m) - element ellipsoidalRegion (element type ellipsoidalRegion - sub
    structure)
    5. Basic measured quantity in Cartesian form with rectangular coverage
    region
    (o) - element label (string)
    (m) - element valueReal (decimal value type)
    (m) - element valueImag (decimal value type)
    (m) - element unit (string - SI unit)
    (o) - element dateTime (xs:dateTime)
    (m) - element rectangularRegion (element type rectangularRegion - sub
    structure)
    6. Basic measured quantity in polar form with rectangular coverage region
    (o) - element label (string)
    (m) - element valueMagnitude (decimal value type)
    (m) - element valuePhase (decimal value type)
    (m) - element unit (string - SI unit)
    (m) - element unitPhase (string - SI unit for an angular quantity)
    (o) - element dateTime (xs:dateTime)
    (m) - element rectangularRegion (element type rectangularRegion - sub
    structure)"""
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, label=None, valueReal=None, valueImag=None, valueMagnitude=None, valuePhase=None, unit=None, unitPhase=None, dateTime=None, ellipsoidalRegion=None, rectangularRegion=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = "si"
        self.label = label
        self.label_nsprefix_ = "si"
        self.valueReal = valueReal
        self.validate_decimalType(self.valueReal)
        self.valueReal_nsprefix_ = "si"
        self.valueImag = valueImag
        self.validate_decimalType(self.valueImag)
        self.valueImag_nsprefix_ = "si"
        self.valueMagnitude = valueMagnitude
        self.validate_decimalType(self.valueMagnitude)
        self.valueMagnitude_nsprefix_ = "si"
        self.valuePhase = valuePhase
        self.validate_decimalType(self.valuePhase)
        self.valuePhase_nsprefix_ = "si"
        self.unit = unit
        self.validate_unitType(self.unit)
        self.unit_nsprefix_ = "si"
        self.unitPhase = unitPhase
        self.validate_unitPhaseType(self.unitPhase)
        self.unitPhase_nsprefix_ = "si"
        if isinstance(dateTime, BaseStrType_):
            initvalue_ = datetime_.datetime.strptime(dateTime, '%Y-%m-%dT%H:%M:%S')
        else:
            initvalue_ = dateTime
        self.dateTime = initvalue_
        self.dateTime_nsprefix_ = "si"
        self.ellipsoidalRegion = ellipsoidalRegion
        self.ellipsoidalRegion_nsprefix_ = "si"
        self.rectangularRegion = rectangularRegion
        self.rectangularRegion_nsprefix_ = "si"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, complex)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if complex.subclass:
            return complex.subclass(*args_, **kwargs_)
        else:
            return complex(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_label(self):
        return self.label
    def set_label(self, label):
        self.label = label
    def get_valueReal(self):
        return self.valueReal
    def set_valueReal(self, valueReal):
        self.valueReal = valueReal
    def get_valueImag(self):
        return self.valueImag
    def set_valueImag(self, valueImag):
        self.valueImag = valueImag
    def get_valueMagnitude(self):
        return self.valueMagnitude
    def set_valueMagnitude(self, valueMagnitude):
        self.valueMagnitude = valueMagnitude
    def get_valuePhase(self):
        return self.valuePhase
    def set_valuePhase(self, valuePhase):
        self.valuePhase = valuePhase
    def get_unit(self):
        return self.unit
    def set_unit(self, unit):
        self.unit = unit
    def get_unitPhase(self):
        return self.unitPhase
    def set_unitPhase(self, unitPhase):
        self.unitPhase = unitPhase
    def get_dateTime(self):
        return self.dateTime
    def set_dateTime(self, dateTime):
        self.dateTime = dateTime
    def get_ellipsoidalRegion(self):
        return self.ellipsoidalRegion
    def set_ellipsoidalRegion(self, ellipsoidalRegion):
        self.ellipsoidalRegion = ellipsoidalRegion
    def get_rectangularRegion(self):
        return self.rectangularRegion
    def set_rectangularRegion(self, rectangularRegion):
        self.rectangularRegion = rectangularRegion
    def validate_decimalType(self, value):
        result = True
        # Validate type decimalType, a restriction on xs:double.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, float):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (float)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_decimalType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_decimalType_patterns_, ))
                result = False
        return result
    validate_decimalType_patterns_ = [['^([-+]?((\\d*\\.\\d+)|(\\d+\\.\\d*)|(\\d+\\.?))([Ee][-+]?\\d+)?)$']]
    def validate_unitType(self, value):
        result = True
        # Validate type unitType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            pass
        return result
    def validate_unitPhaseType(self, value):
        result = True
        # Validate type unitPhaseType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            pass
        return result
    def hasContent_(self):
        if (
            self.label is not None or
            self.valueReal is not None or
            self.valueImag is not None or
            self.valueMagnitude is not None or
            self.valuePhase is not None or
            self.unit is not None or
            self.unitPhase is not None or
            self.dateTime is not None or
            self.ellipsoidalRegion is not None or
            self.rectangularRegion is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:si="https://ptb.de/si"', name_='complex', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('complex')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'complex':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='complex')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='complex', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='complex'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:si="https://ptb.de/si"', name_='complex', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.label is not None:
            namespaceprefix_ = self.label_nsprefix_ + ':' if (UseCapturedNS_ and self.label_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%slabel>%s</%slabel>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.label), input_name='label')), namespaceprefix_ , eol_))
        if self.valueReal is not None:
            namespaceprefix_ = self.valueReal_nsprefix_ + ':' if (UseCapturedNS_ and self.valueReal_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%svalueReal>%s</%svalueReal>%s' % (namespaceprefix_ , self.gds_format_double(self.valueReal, input_name='valueReal'), namespaceprefix_ , eol_))
        if self.valueImag is not None:
            namespaceprefix_ = self.valueImag_nsprefix_ + ':' if (UseCapturedNS_ and self.valueImag_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%svalueImag>%s</%svalueImag>%s' % (namespaceprefix_ , self.gds_format_double(self.valueImag, input_name='valueImag'), namespaceprefix_ , eol_))
        if self.valueMagnitude is not None:
            namespaceprefix_ = self.valueMagnitude_nsprefix_ + ':' if (UseCapturedNS_ and self.valueMagnitude_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%svalueMagnitude>%s</%svalueMagnitude>%s' % (namespaceprefix_ , self.gds_format_double(self.valueMagnitude, input_name='valueMagnitude'), namespaceprefix_ , eol_))
        if self.valuePhase is not None:
            namespaceprefix_ = self.valuePhase_nsprefix_ + ':' if (UseCapturedNS_ and self.valuePhase_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%svaluePhase>%s</%svaluePhase>%s' % (namespaceprefix_ , self.gds_format_double(self.valuePhase, input_name='valuePhase'), namespaceprefix_ , eol_))
        if self.unit is not None:
            namespaceprefix_ = self.unit_nsprefix_ + ':' if (UseCapturedNS_ and self.unit_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sunit>%s</%sunit>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.unit), input_name='unit')), namespaceprefix_ , eol_))
        if self.unitPhase is not None:
            namespaceprefix_ = self.unitPhase_nsprefix_ + ':' if (UseCapturedNS_ and self.unitPhase_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sunitPhase>%s</%sunitPhase>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.unitPhase), input_name='unitPhase')), namespaceprefix_ , eol_))
        if self.dateTime is not None:
            namespaceprefix_ = self.dateTime_nsprefix_ + ':' if (UseCapturedNS_ and self.dateTime_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sdateTime>%s</%sdateTime>%s' % (namespaceprefix_ , self.gds_format_datetime(self.dateTime, input_name='dateTime'), namespaceprefix_ , eol_))
        if self.ellipsoidalRegion is not None:
            namespaceprefix_ = self.ellipsoidalRegion_nsprefix_ + ':' if (UseCapturedNS_ and self.ellipsoidalRegion_nsprefix_) else ''
            self.ellipsoidalRegion.export(outfile, level, namespaceprefix_='si:', namespacedef_='', name_='ellipsoidalRegion', pretty_print=pretty_print)
        if self.rectangularRegion is not None:
            namespaceprefix_ = self.rectangularRegion_nsprefix_ + ':' if (UseCapturedNS_ and self.rectangularRegion_nsprefix_) else ''
            self.rectangularRegion.export(outfile, level, namespaceprefix_='si:', namespacedef_='', name_='rectangularRegion', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='complex', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{https://ptb.de/si}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{https://ptb.de/si}' + name_, nsmap=nsmap_)
        if self.label is not None:
            label_ = self.label
            etree_.SubElement(element, '{https://ptb.de/si}label').text = self.gds_format_string(label_)
        if self.valueReal is not None:
            valueReal_ = self.valueReal
            etree_.SubElement(element, '{https://ptb.de/si}valueReal').text = self.gds_format_double(valueReal_)
        if self.valueImag is not None:
            valueImag_ = self.valueImag
            etree_.SubElement(element, '{https://ptb.de/si}valueImag').text = self.gds_format_double(valueImag_)
        if self.valueMagnitude is not None:
            valueMagnitude_ = self.valueMagnitude
            etree_.SubElement(element, '{https://ptb.de/si}valueMagnitude').text = self.gds_format_double(valueMagnitude_)
        if self.valuePhase is not None:
            valuePhase_ = self.valuePhase
            etree_.SubElement(element, '{https://ptb.de/si}valuePhase').text = self.gds_format_double(valuePhase_)
        if self.unit is not None:
            unit_ = self.unit
            etree_.SubElement(element, '{https://ptb.de/si}unit').text = self.gds_format_string(unit_)
        if self.unitPhase is not None:
            unitPhase_ = self.unitPhase
            etree_.SubElement(element, '{https://ptb.de/si}unitPhase').text = self.gds_format_string(unitPhase_)
        if self.dateTime is not None:
            dateTime_ = self.dateTime
            etree_.SubElement(element, '{https://ptb.de/si}dateTime').text = self.gds_format_datetime(dateTime_)
        if self.ellipsoidalRegion is not None:
            ellipsoidalRegion_ = self.ellipsoidalRegion
            ellipsoidalRegion_.to_etree(element, name_='ellipsoidalRegion', mapping_=mapping_, nsmap_=nsmap_)
        if self.rectangularRegion is not None:
            rectangularRegion_ = self.rectangularRegion
            rectangularRegion_.to_etree(element, name_='rectangularRegion', mapping_=mapping_, nsmap_=nsmap_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'label':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'label')
            value_ = self.gds_validate_string(value_, node, 'label')
            self.label = value_
            self.label_nsprefix_ = child_.prefix
        elif nodeName_ == 'valueReal' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_double(sval_, node, 'valueReal')
            fval_ = self.gds_validate_double(fval_, node, 'valueReal')
            self.valueReal = fval_
            self.valueReal_nsprefix_ = child_.prefix
            # validate type decimalType
            self.validate_decimalType(self.valueReal)
        elif nodeName_ == 'valueImag' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_double(sval_, node, 'valueImag')
            fval_ = self.gds_validate_double(fval_, node, 'valueImag')
            self.valueImag = fval_
            self.valueImag_nsprefix_ = child_.prefix
            # validate type decimalType
            self.validate_decimalType(self.valueImag)
        elif nodeName_ == 'valueMagnitude' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_double(sval_, node, 'valueMagnitude')
            fval_ = self.gds_validate_double(fval_, node, 'valueMagnitude')
            self.valueMagnitude = fval_
            self.valueMagnitude_nsprefix_ = child_.prefix
            # validate type decimalType
            self.validate_decimalType(self.valueMagnitude)
        elif nodeName_ == 'valuePhase' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_double(sval_, node, 'valuePhase')
            fval_ = self.gds_validate_double(fval_, node, 'valuePhase')
            self.valuePhase = fval_
            self.valuePhase_nsprefix_ = child_.prefix
            # validate type decimalType
            self.validate_decimalType(self.valuePhase)
        elif nodeName_ == 'unit':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'unit')
            value_ = self.gds_validate_string(value_, node, 'unit')
            self.unit = value_
            self.unit_nsprefix_ = child_.prefix
            # validate type unitType
            self.validate_unitType(self.unit)
        elif nodeName_ == 'unitPhase':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'unitPhase')
            value_ = self.gds_validate_string(value_, node, 'unitPhase')
            self.unitPhase = value_
            self.unitPhase_nsprefix_ = child_.prefix
            # validate type unitPhaseType
            self.validate_unitPhaseType(self.unitPhase)
        elif nodeName_ == 'dateTime':
            sval_ = child_.text
            dval_ = self.gds_parse_datetime(sval_)
            self.dateTime = dval_
            self.dateTime_nsprefix_ = child_.prefix
        elif nodeName_ == 'ellipsoidalRegion':
            obj_ = ellipsoidalRegion.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.ellipsoidalRegion = obj_
            obj_.original_tagname_ = 'ellipsoidalRegion'
        elif nodeName_ == 'rectangularRegion':
            obj_ = rectangularRegion.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.rectangularRegion = obj_
            obj_.original_tagname_ = 'rectangularRegion'
# end class complex


class covarianceMatrix(GeneratedsSuper):
    """Definition of a covariance matrix element that is used for
    multidimensional uncertainty statements in the D-SI format.
    A covariance matrix has n column elements.
    The dimension of the covariance matrix is the amount of columns.
    Each column contains the covariance values of one column of the
    covariance matrix.
    The order of the columns is from left to right column in the
    covariance matrix."""
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, column=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = "si"
        if column is None:
            self.column = []
        else:
            self.column = column
        self.column_nsprefix_ = "si"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, covarianceMatrix)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if covarianceMatrix.subclass:
            return covarianceMatrix.subclass(*args_, **kwargs_)
        else:
            return covarianceMatrix(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_column(self):
        return self.column
    def set_column(self, column):
        self.column = column
    def add_column(self, value):
        self.column.append(value)
    def insert_column_at(self, index, value):
        self.column.insert(index, value)
    def replace_column_at(self, index, value):
        self.column[index] = value
    def hasContent_(self):
        if (
            self.column
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:si="https://ptb.de/si"', name_='covarianceMatrix', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('covarianceMatrix')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'covarianceMatrix':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='covarianceMatrix')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='covarianceMatrix', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='covarianceMatrix'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:si="https://ptb.de/si"', name_='covarianceMatrix', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for column_ in self.column:
            namespaceprefix_ = self.column_nsprefix_ + ':' if (UseCapturedNS_ and self.column_nsprefix_) else ''
            column_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='column', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='covarianceMatrix', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{https://ptb.de/si}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{https://ptb.de/si}' + name_, nsmap=nsmap_)
        for column_ in self.column:
            column_.to_etree(element, name_='column', mapping_=mapping_, nsmap_=nsmap_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'column':
            obj_ = columnType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.column.append(obj_)
            obj_.original_tagname_ = 'column'
# end class covarianceMatrix


class ellipsoidalRegion(GeneratedsSuper):
    """Definition of the structure, that provides a hyper-ellipsoidal coverage
    region for stating the uncertainty of multivariate quantities. It is
    used in the context of uncertainty for complex quantities and
    lists of real or complex quantities.
    The element has the following components [(m)-mandatory, (o)-optional]:
    (m) - element covarianceMatrix (sub structure covarianceMatrix)
    (m) - element coverageFactor (decimal value >= 1)
    (m) - element coverageProbability (decimal value in [0,1])
    (o) - element distribution (string)"""
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, covarianceMatrix=None, coverageFactor=None, coverageProbability=None, distribution=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = "si"
        self.covarianceMatrix = covarianceMatrix
        self.covarianceMatrix_nsprefix_ = "si"
        self.coverageFactor = coverageFactor
        self.validate_kValueType(self.coverageFactor)
        self.coverageFactor_nsprefix_ = "si"
        self.coverageProbability = coverageProbability
        self.validate_probabilityValueType(self.coverageProbability)
        self.coverageProbability_nsprefix_ = "si"
        self.distribution = distribution
        self.distribution_nsprefix_ = "si"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ellipsoidalRegion)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ellipsoidalRegion.subclass:
            return ellipsoidalRegion.subclass(*args_, **kwargs_)
        else:
            return ellipsoidalRegion(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_covarianceMatrix(self):
        return self.covarianceMatrix
    def set_covarianceMatrix(self, covarianceMatrix):
        self.covarianceMatrix = covarianceMatrix
    def get_coverageFactor(self):
        return self.coverageFactor
    def set_coverageFactor(self, coverageFactor):
        self.coverageFactor = coverageFactor
    def get_coverageProbability(self):
        return self.coverageProbability
    def set_coverageProbability(self, coverageProbability):
        self.coverageProbability = coverageProbability
    def get_distribution(self):
        return self.distribution
    def set_distribution(self, distribution):
        self.distribution = distribution
    def validate_kValueType(self, value):
        result = True
        # Validate type kValueType, a restriction on xs:double.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, float):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (float)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_kValueType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_kValueType_patterns_, ))
                result = False
        return result
    validate_kValueType_patterns_ = [['^(\\+?(([1-9]\\d*\\.\\d*)|([1-9]\\d*)))$']]
    def validate_probabilityValueType(self, value):
        result = True
        # Validate type probabilityValueType, a restriction on xs:double.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, float):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (float)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_probabilityValueType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_probabilityValueType_patterns_, ))
                result = False
        return result
    validate_probabilityValueType_patterns_ = [['^(\\+?((0(\\.\\d*)?)|(1(\\.0*)?)))$']]
    def hasContent_(self):
        if (
            self.covarianceMatrix is not None or
            self.coverageFactor is not None or
            self.coverageProbability is not None or
            self.distribution is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:si="https://ptb.de/si"', name_='ellipsoidalRegion', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ellipsoidalRegion')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ellipsoidalRegion':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ellipsoidalRegion')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ellipsoidalRegion', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ellipsoidalRegion'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:si="https://ptb.de/si"', name_='ellipsoidalRegion', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.covarianceMatrix is not None:
            namespaceprefix_ = self.covarianceMatrix_nsprefix_ + ':' if (UseCapturedNS_ and self.covarianceMatrix_nsprefix_) else ''
            self.covarianceMatrix.export(outfile, level, namespaceprefix_='si:', namespacedef_='', name_='covarianceMatrix', pretty_print=pretty_print)
        if self.coverageFactor is not None:
            namespaceprefix_ = self.coverageFactor_nsprefix_ + ':' if (UseCapturedNS_ and self.coverageFactor_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scoverageFactor>%s</%scoverageFactor>%s' % (namespaceprefix_ , self.gds_format_double(self.coverageFactor, input_name='coverageFactor'), namespaceprefix_ , eol_))
        if self.coverageProbability is not None:
            namespaceprefix_ = self.coverageProbability_nsprefix_ + ':' if (UseCapturedNS_ and self.coverageProbability_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scoverageProbability>%s</%scoverageProbability>%s' % (namespaceprefix_ , self.gds_format_double(self.coverageProbability, input_name='coverageProbability'), namespaceprefix_ , eol_))
        if self.distribution is not None:
            namespaceprefix_ = self.distribution_nsprefix_ + ':' if (UseCapturedNS_ and self.distribution_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sdistribution>%s</%sdistribution>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.distribution), input_name='distribution')), namespaceprefix_ , eol_))
    def to_etree(self, parent_element=None, name_='ellipsoidalRegion', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{https://ptb.de/si}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{https://ptb.de/si}' + name_, nsmap=nsmap_)
        if self.covarianceMatrix is not None:
            covarianceMatrix_ = self.covarianceMatrix
            covarianceMatrix_.to_etree(element, name_='covarianceMatrix', mapping_=mapping_, nsmap_=nsmap_)
        if self.coverageFactor is not None:
            coverageFactor_ = self.coverageFactor
            etree_.SubElement(element, '{https://ptb.de/si}coverageFactor').text = self.gds_format_double(coverageFactor_)
        if self.coverageProbability is not None:
            coverageProbability_ = self.coverageProbability
            etree_.SubElement(element, '{https://ptb.de/si}coverageProbability').text = self.gds_format_double(coverageProbability_)
        if self.distribution is not None:
            distribution_ = self.distribution
            etree_.SubElement(element, '{https://ptb.de/si}distribution').text = self.gds_format_string(distribution_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'covarianceMatrix':
            obj_ = covarianceMatrix.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.covarianceMatrix = obj_
            obj_.original_tagname_ = 'covarianceMatrix'
        elif nodeName_ == 'coverageFactor' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_double(sval_, node, 'coverageFactor')
            fval_ = self.gds_validate_double(fval_, node, 'coverageFactor')
            self.coverageFactor = fval_
            self.coverageFactor_nsprefix_ = child_.prefix
            # validate type kValueType
            self.validate_kValueType(self.coverageFactor)
        elif nodeName_ == 'coverageProbability' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_double(sval_, node, 'coverageProbability')
            fval_ = self.gds_validate_double(fval_, node, 'coverageProbability')
            self.coverageProbability = fval_
            self.coverageProbability_nsprefix_ = child_.prefix
            # validate type probabilityValueType
            self.validate_probabilityValueType(self.coverageProbability)
        elif nodeName_ == 'distribution':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'distribution')
            value_ = self.gds_validate_string(value_, node, 'distribution')
            self.distribution = value_
            self.distribution_nsprefix_ = child_.prefix
# end class ellipsoidalRegion


class rectangularRegion(GeneratedsSuper):
    """Definition of the structure that provides a hyper-rectangular coverage
    region for stating the uncertainty of multivariate quantities. It is
    used in the context of uncertainty for complex quantities and
    lists of real or complex quantities.
    The element has the following components [(m)-mandatory, (o)-optional]:
    (m) - element covarianceMatrix (sub structure covarianceMatrix)
    (m) - element coverageFactor (decimal value >= 1)
    (m) - element coverageProbability (decimal value in [0,1])
    (o) - element distribution (string)"""
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, covarianceMatrix=None, coverageFactor=None, coverageProbability=None, distribution=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = "si"
        self.covarianceMatrix = covarianceMatrix
        self.covarianceMatrix_nsprefix_ = "si"
        self.coverageFactor = coverageFactor
        self.validate_kValueType(self.coverageFactor)
        self.coverageFactor_nsprefix_ = "si"
        self.coverageProbability = coverageProbability
        self.validate_probabilityValueType(self.coverageProbability)
        self.coverageProbability_nsprefix_ = "si"
        self.distribution = distribution
        self.distribution_nsprefix_ = "si"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, rectangularRegion)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if rectangularRegion.subclass:
            return rectangularRegion.subclass(*args_, **kwargs_)
        else:
            return rectangularRegion(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_covarianceMatrix(self):
        return self.covarianceMatrix
    def set_covarianceMatrix(self, covarianceMatrix):
        self.covarianceMatrix = covarianceMatrix
    def get_coverageFactor(self):
        return self.coverageFactor
    def set_coverageFactor(self, coverageFactor):
        self.coverageFactor = coverageFactor
    def get_coverageProbability(self):
        return self.coverageProbability
    def set_coverageProbability(self, coverageProbability):
        self.coverageProbability = coverageProbability
    def get_distribution(self):
        return self.distribution
    def set_distribution(self, distribution):
        self.distribution = distribution
    def validate_kValueType(self, value):
        result = True
        # Validate type kValueType, a restriction on xs:double.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, float):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (float)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_kValueType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_kValueType_patterns_, ))
                result = False
        return result
    validate_kValueType_patterns_ = [['^(\\+?(([1-9]\\d*\\.\\d*)|([1-9]\\d*)))$']]
    def validate_probabilityValueType(self, value):
        result = True
        # Validate type probabilityValueType, a restriction on xs:double.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, float):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (float)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_probabilityValueType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_probabilityValueType_patterns_, ))
                result = False
        return result
    validate_probabilityValueType_patterns_ = [['^(\\+?((0(\\.\\d*)?)|(1(\\.0*)?)))$']]
    def hasContent_(self):
        if (
            self.covarianceMatrix is not None or
            self.coverageFactor is not None or
            self.coverageProbability is not None or
            self.distribution is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:si="https://ptb.de/si"', name_='rectangularRegion', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('rectangularRegion')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'rectangularRegion':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='rectangularRegion')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='rectangularRegion', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='rectangularRegion'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:si="https://ptb.de/si"', name_='rectangularRegion', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.covarianceMatrix is not None:
            namespaceprefix_ = self.covarianceMatrix_nsprefix_ + ':' if (UseCapturedNS_ and self.covarianceMatrix_nsprefix_) else ''
            self.covarianceMatrix.export(outfile, level, namespaceprefix_='si:', namespacedef_='', name_='covarianceMatrix', pretty_print=pretty_print)
        if self.coverageFactor is not None:
            namespaceprefix_ = self.coverageFactor_nsprefix_ + ':' if (UseCapturedNS_ and self.coverageFactor_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scoverageFactor>%s</%scoverageFactor>%s' % (namespaceprefix_ , self.gds_format_double(self.coverageFactor, input_name='coverageFactor'), namespaceprefix_ , eol_))
        if self.coverageProbability is not None:
            namespaceprefix_ = self.coverageProbability_nsprefix_ + ':' if (UseCapturedNS_ and self.coverageProbability_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scoverageProbability>%s</%scoverageProbability>%s' % (namespaceprefix_ , self.gds_format_double(self.coverageProbability, input_name='coverageProbability'), namespaceprefix_ , eol_))
        if self.distribution is not None:
            namespaceprefix_ = self.distribution_nsprefix_ + ':' if (UseCapturedNS_ and self.distribution_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sdistribution>%s</%sdistribution>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.distribution), input_name='distribution')), namespaceprefix_ , eol_))
    def to_etree(self, parent_element=None, name_='rectangularRegion', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{https://ptb.de/si}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{https://ptb.de/si}' + name_, nsmap=nsmap_)
        if self.covarianceMatrix is not None:
            covarianceMatrix_ = self.covarianceMatrix
            covarianceMatrix_.to_etree(element, name_='covarianceMatrix', mapping_=mapping_, nsmap_=nsmap_)
        if self.coverageFactor is not None:
            coverageFactor_ = self.coverageFactor
            etree_.SubElement(element, '{https://ptb.de/si}coverageFactor').text = self.gds_format_double(coverageFactor_)
        if self.coverageProbability is not None:
            coverageProbability_ = self.coverageProbability
            etree_.SubElement(element, '{https://ptb.de/si}coverageProbability').text = self.gds_format_double(coverageProbability_)
        if self.distribution is not None:
            distribution_ = self.distribution
            etree_.SubElement(element, '{https://ptb.de/si}distribution').text = self.gds_format_string(distribution_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'covarianceMatrix':
            obj_ = covarianceMatrix.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.covarianceMatrix = obj_
            obj_.original_tagname_ = 'covarianceMatrix'
        elif nodeName_ == 'coverageFactor' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_double(sval_, node, 'coverageFactor')
            fval_ = self.gds_validate_double(fval_, node, 'coverageFactor')
            self.coverageFactor = fval_
            self.coverageFactor_nsprefix_ = child_.prefix
            # validate type kValueType
            self.validate_kValueType(self.coverageFactor)
        elif nodeName_ == 'coverageProbability' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_double(sval_, node, 'coverageProbability')
            fval_ = self.gds_validate_double(fval_, node, 'coverageProbability')
            self.coverageProbability = fval_
            self.coverageProbability_nsprefix_ = child_.prefix
            # validate type probabilityValueType
            self.validate_probabilityValueType(self.coverageProbability)
        elif nodeName_ == 'distribution':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'distribution')
            value_ = self.gds_validate_string(value_, node, 'distribution')
            self.distribution = value_
            self.distribution_nsprefix_ = child_.prefix
# end class rectangularRegion


class list(GeneratedsSuper):
    """Meta data element definition for a list of basic measurement quantities.
    The list can represent independent measurement or multivariate vector
    quantities.
    A list can provide the following structures:
    1: A list of si:real quantities
    - optional list timestamp, list label and/or list unit
    - optional list univariate uncertainty statement with list unit
    - optional multivariate hyper-elliptical or hyper-rectangular coverage
    region
    2: A list of si:complex quantities
    - optional list timestamp, list label and/or list unit(s)
    - optional list bivariate uncertainty statement with list unit(s)
    - optional multivariate hyper-elliptical or hyper-rectangular coverage
    region
    3: A recursive list of si:list elements
    - optional global timestamp and/or global label"""
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, label=None, dateTime=None, listUnit=None, listUnivariateUnc=None, real=None, listUnitPhase=None, listBivariateUnc=None, complex=None, ellipsoidalRegion=None, rectangularRegion=None, list_member=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = "si"
        self.label = label
        self.label_nsprefix_ = "si"
        if isinstance(dateTime, BaseStrType_):
            initvalue_ = datetime_.datetime.strptime(dateTime, '%Y-%m-%dT%H:%M:%S')
        else:
            initvalue_ = dateTime
        self.dateTime = initvalue_
        self.dateTime_nsprefix_ = "si"
        self.listUnit = listUnit
        self.validate_unitType(self.listUnit)
        self.listUnit_nsprefix_ = "si"
        self.listUnivariateUnc = listUnivariateUnc
        self.listUnivariateUnc_nsprefix_ = "si"
        if real is None:
            self.real = []
        else:
            self.real = real
        self.real_nsprefix_ = "si"
        self.listUnitPhase = listUnitPhase
        self.listUnitPhase_nsprefix_ = "si"
        self.listBivariateUnc = listBivariateUnc
        self.listBivariateUnc_nsprefix_ = "si"
        if complex is None:
            self.complex = []
        else:
            self.complex = complex
        self.complex_nsprefix_ = "si"
        self.ellipsoidalRegion = ellipsoidalRegion
        self.ellipsoidalRegion_nsprefix_ = "si"
        self.rectangularRegion = rectangularRegion
        self.rectangularRegion_nsprefix_ = "si"
        if list_member is None:
            self.list = []
        else:
            self.list = list_member
        self.list_nsprefix_ = "si"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, list)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if list.subclass:
            return list.subclass(*args_, **kwargs_)
        else:
            return list(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_label(self):
        return self.label
    def set_label(self, label):
        self.label = label
    def get_dateTime(self):
        return self.dateTime
    def set_dateTime(self, dateTime):
        self.dateTime = dateTime
    def get_listUnit(self):
        return self.listUnit
    def set_listUnit(self, listUnit):
        self.listUnit = listUnit
    def get_listUnivariateUnc(self):
        return self.listUnivariateUnc
    def set_listUnivariateUnc(self, listUnivariateUnc):
        self.listUnivariateUnc = listUnivariateUnc
    def get_real(self):
        return self.real
    def set_real(self, real):
        self.real = real
    def add_real(self, value):
        self.real.append(value)
    def insert_real_at(self, index, value):
        self.real.insert(index, value)
    def replace_real_at(self, index, value):
        self.real[index] = value
    def get_listUnitPhase(self):
        return self.listUnitPhase
    def set_listUnitPhase(self, listUnitPhase):
        self.listUnitPhase = listUnitPhase
    def get_listBivariateUnc(self):
        return self.listBivariateUnc
    def set_listBivariateUnc(self, listBivariateUnc):
        self.listBivariateUnc = listBivariateUnc
    def get_complex(self):
        return self.complex
    def set_complex(self, complex):
        self.complex = complex
    def add_complex(self, value):
        self.complex.append(value)
    def insert_complex_at(self, index, value):
        self.complex.insert(index, value)
    def replace_complex_at(self, index, value):
        self.complex[index] = value
    def get_ellipsoidalRegion(self):
        return self.ellipsoidalRegion
    def set_ellipsoidalRegion(self, ellipsoidalRegion):
        self.ellipsoidalRegion = ellipsoidalRegion
    def get_rectangularRegion(self):
        return self.rectangularRegion
    def set_rectangularRegion(self, rectangularRegion):
        self.rectangularRegion = rectangularRegion
    def get_list(self):
        return self.list
    def set_list(self, list):
        self.list = list
    def add_list(self, value):
        self.list.append(value)
    def insert_list_at(self, index, value):
        self.list.insert(index, value)
    def replace_list_at(self, index, value):
        self.list[index] = value
    def validate_unitType(self, value):
        result = True
        # Validate type unitType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            pass
        return result
    def hasContent_(self):
        if (
            self.label is not None or
            self.dateTime is not None or
            self.listUnit is not None or
            self.listUnivariateUnc is not None or
            self.real or
            self.listUnitPhase is not None or
            self.listBivariateUnc is not None or
            self.complex or
            self.ellipsoidalRegion is not None or
            self.rectangularRegion is not None or
            self.list
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:si="https://ptb.de/si"', name_='list', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('list')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'list':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='list')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='list', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='list'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:si="https://ptb.de/si"', name_='list', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.label is not None:
            namespaceprefix_ = self.label_nsprefix_ + ':' if (UseCapturedNS_ and self.label_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%slabel>%s</%slabel>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.label), input_name='label')), namespaceprefix_ , eol_))
        if self.dateTime is not None:
            namespaceprefix_ = self.dateTime_nsprefix_ + ':' if (UseCapturedNS_ and self.dateTime_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sdateTime>%s</%sdateTime>%s' % (namespaceprefix_ , self.gds_format_datetime(self.dateTime, input_name='dateTime'), namespaceprefix_ , eol_))
        if self.listUnit is not None:
            namespaceprefix_ = self.listUnit_nsprefix_ + ':' if (UseCapturedNS_ and self.listUnit_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%slistUnit>%s</%slistUnit>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.listUnit), input_name='listUnit')), namespaceprefix_ , eol_))
        if self.listUnivariateUnc is not None:
            namespaceprefix_ = self.listUnivariateUnc_nsprefix_ + ':' if (UseCapturedNS_ and self.listUnivariateUnc_nsprefix_) else ''
            self.listUnivariateUnc.export(outfile, level, namespaceprefix_='si:', namespacedef_='', name_='listUnivariateUnc', pretty_print=pretty_print)
        for real_ in self.real:
            namespaceprefix_ = self.real_nsprefix_ + ':' if (UseCapturedNS_ and self.real_nsprefix_) else ''
            real_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='real', pretty_print=pretty_print)
        if self.listUnitPhase is not None:
            namespaceprefix_ = self.listUnitPhase_nsprefix_ + ':' if (UseCapturedNS_ and self.listUnitPhase_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%slistUnitPhase>%s</%slistUnitPhase>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.listUnitPhase), input_name='listUnitPhase')), namespaceprefix_ , eol_))
        if self.listBivariateUnc is not None:
            namespaceprefix_ = self.listBivariateUnc_nsprefix_ + ':' if (UseCapturedNS_ and self.listBivariateUnc_nsprefix_) else ''
            self.listBivariateUnc.export(outfile, level, namespaceprefix_='si:', namespacedef_='', name_='listBivariateUnc', pretty_print=pretty_print)
        for complex_ in self.complex:
            namespaceprefix_ = self.complex_nsprefix_ + ':' if (UseCapturedNS_ and self.complex_nsprefix_) else ''
            complex_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='complex', pretty_print=pretty_print)
        if self.ellipsoidalRegion is not None:
            namespaceprefix_ = self.ellipsoidalRegion_nsprefix_ + ':' if (UseCapturedNS_ and self.ellipsoidalRegion_nsprefix_) else ''
            self.ellipsoidalRegion.export(outfile, level, namespaceprefix_='si:', namespacedef_='', name_='ellipsoidalRegion', pretty_print=pretty_print)
        if self.rectangularRegion is not None:
            namespaceprefix_ = self.rectangularRegion_nsprefix_ + ':' if (UseCapturedNS_ and self.rectangularRegion_nsprefix_) else ''
            self.rectangularRegion.export(outfile, level, namespaceprefix_='si:', namespacedef_='', name_='rectangularRegion', pretty_print=pretty_print)
        for list_ in self.list:
            namespaceprefix_ = self.list_nsprefix_ + ':' if (UseCapturedNS_ and self.list_nsprefix_) else ''
            list_.export(outfile, level, namespaceprefix_='si:', namespacedef_='', name_='list', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='list', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{https://ptb.de/si}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{https://ptb.de/si}' + name_, nsmap=nsmap_)
        if self.label is not None:
            label_ = self.label
            etree_.SubElement(element, '{https://ptb.de/si}label').text = self.gds_format_string(label_)
        if self.dateTime is not None:
            dateTime_ = self.dateTime
            etree_.SubElement(element, '{https://ptb.de/si}dateTime').text = self.gds_format_datetime(dateTime_)
        if self.listUnit is not None:
            listUnit_ = self.listUnit
            etree_.SubElement(element, '{https://ptb.de/si}listUnit').text = self.gds_format_string(listUnit_)
        if self.listUnivariateUnc is not None:
            listUnivariateUnc_ = self.listUnivariateUnc
            listUnivariateUnc_.to_etree(element, name_='listUnivariateUnc', mapping_=mapping_, nsmap_=nsmap_)
        for real_ in self.real:
            real_.to_etree(element, name_='real', mapping_=mapping_, nsmap_=nsmap_)
        if self.listUnitPhase is not None:
            listUnitPhase_ = self.listUnitPhase
            etree_.SubElement(element, '{https://ptb.de/si}listUnitPhase').text = self.gds_format_string(listUnitPhase_)
        if self.listBivariateUnc is not None:
            listBivariateUnc_ = self.listBivariateUnc
            listBivariateUnc_.to_etree(element, name_='listBivariateUnc', mapping_=mapping_, nsmap_=nsmap_)
        for complex_ in self.complex:
            complex_.to_etree(element, name_='complex', mapping_=mapping_, nsmap_=nsmap_)
        if self.ellipsoidalRegion is not None:
            ellipsoidalRegion_ = self.ellipsoidalRegion
            ellipsoidalRegion_.to_etree(element, name_='ellipsoidalRegion', mapping_=mapping_, nsmap_=nsmap_)
        if self.rectangularRegion is not None:
            rectangularRegion_ = self.rectangularRegion
            rectangularRegion_.to_etree(element, name_='rectangularRegion', mapping_=mapping_, nsmap_=nsmap_)
        for list_ in self.list:
            list_.to_etree(element, name_='list', mapping_=mapping_, nsmap_=nsmap_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'label':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'label')
            value_ = self.gds_validate_string(value_, node, 'label')
            self.label = value_
            self.label_nsprefix_ = child_.prefix
        elif nodeName_ == 'dateTime':
            sval_ = child_.text
            dval_ = self.gds_parse_datetime(sval_)
            self.dateTime = dval_
            self.dateTime_nsprefix_ = child_.prefix
        elif nodeName_ == 'listUnit':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'listUnit')
            value_ = self.gds_validate_string(value_, node, 'listUnit')
            self.listUnit = value_
            self.listUnit_nsprefix_ = child_.prefix
            # validate type unitType
            self.validate_unitType(self.listUnit)
        elif nodeName_ == 'listUnivariateUnc':
            obj_ = listUnivariateUnc.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.listUnivariateUnc = obj_
            obj_.original_tagname_ = 'listUnivariateUnc'
        elif nodeName_ == 'real':
            obj_ = realType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.real.append(obj_)
            obj_.original_tagname_ = 'real'
        elif nodeName_ == 'listUnitPhase':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'listUnitPhase')
            value_ = self.gds_validate_string(value_, node, 'listUnitPhase')
            self.listUnitPhase = value_
            self.listUnitPhase_nsprefix_ = child_.prefix
        elif nodeName_ == 'listBivariateUnc':
            obj_ = listBivariateUnc.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.listBivariateUnc = obj_
            obj_.original_tagname_ = 'listBivariateUnc'
        elif nodeName_ == 'complex':
            obj_ = complexType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.complex.append(obj_)
            obj_.original_tagname_ = 'complex'
        elif nodeName_ == 'ellipsoidalRegion':
            obj_ = ellipsoidalRegion.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.ellipsoidalRegion = obj_
            obj_.original_tagname_ = 'ellipsoidalRegion'
        elif nodeName_ == 'rectangularRegion':
            obj_ = rectangularRegion.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.rectangularRegion = obj_
            obj_.original_tagname_ = 'rectangularRegion'
        elif nodeName_ == 'list':
            obj_ = list.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.list.append(obj_)
            obj_.original_tagname_ = 'list'
# end class list


class listUnivariateUnc(GeneratedsSuper):
    """Definition of a structure, for a global univariate uncertainty, that
    is used within the list structure with a list of real quantities.
    The global univariate uncertainty can either be given as an expanded
    measurement uncertainty or as a coverage interval."""
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, expandedUnc=None, coverageInterval=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = "si"
        self.expandedUnc = expandedUnc
        self.expandedUnc_nsprefix_ = "si"
        self.coverageInterval = coverageInterval
        self.coverageInterval_nsprefix_ = "si"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, listUnivariateUnc)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if listUnivariateUnc.subclass:
            return listUnivariateUnc.subclass(*args_, **kwargs_)
        else:
            return listUnivariateUnc(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_expandedUnc(self):
        return self.expandedUnc
    def set_expandedUnc(self, expandedUnc):
        self.expandedUnc = expandedUnc
    def get_coverageInterval(self):
        return self.coverageInterval
    def set_coverageInterval(self, coverageInterval):
        self.coverageInterval = coverageInterval
    def hasContent_(self):
        if (
            self.expandedUnc is not None or
            self.coverageInterval is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:si="https://ptb.de/si"', name_='listUnivariateUnc', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('listUnivariateUnc')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'listUnivariateUnc':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='listUnivariateUnc')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='listUnivariateUnc', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='listUnivariateUnc'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:si="https://ptb.de/si"', name_='listUnivariateUnc', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.expandedUnc is not None:
            namespaceprefix_ = self.expandedUnc_nsprefix_ + ':' if (UseCapturedNS_ and self.expandedUnc_nsprefix_) else ''
            self.expandedUnc.export(outfile, level, namespaceprefix_='si:', namespacedef_='', name_='expandedUnc', pretty_print=pretty_print)
        if self.coverageInterval is not None:
            namespaceprefix_ = self.coverageInterval_nsprefix_ + ':' if (UseCapturedNS_ and self.coverageInterval_nsprefix_) else ''
            self.coverageInterval.export(outfile, level, namespaceprefix_='si:', namespacedef_='', name_='coverageInterval', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='listUnivariateUnc', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{https://ptb.de/si}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{https://ptb.de/si}' + name_, nsmap=nsmap_)
        if self.expandedUnc is not None:
            expandedUnc_ = self.expandedUnc
            expandedUnc_.to_etree(element, name_='expandedUnc', mapping_=mapping_, nsmap_=nsmap_)
        if self.coverageInterval is not None:
            coverageInterval_ = self.coverageInterval
            coverageInterval_.to_etree(element, name_='coverageInterval', mapping_=mapping_, nsmap_=nsmap_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'expandedUnc':
            obj_ = expandedUnc.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.expandedUnc = obj_
            obj_.original_tagname_ = 'expandedUnc'
        elif nodeName_ == 'coverageInterval':
            obj_ = coverageInterval.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.coverageInterval = obj_
            obj_.original_tagname_ = 'coverageInterval'
# end class listUnivariateUnc


class listBivariateUnc(GeneratedsSuper):
    """Definition of a structure, for a global bivariate uncertainty, that
    is used within the list structure with a list of complex quantities.
    The global bivariate uncertainty can either be given as a hyper-ellipsoidal
    coverage region or a hyper-rectangular coverage region. Both
    coverage regions must provide a covariance matrix of dimension 2."""
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, ellipsoidalRegion=None, rectangularRegion=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = "si"
        self.ellipsoidalRegion = ellipsoidalRegion
        self.ellipsoidalRegion_nsprefix_ = "si"
        self.rectangularRegion = rectangularRegion
        self.rectangularRegion_nsprefix_ = "si"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, listBivariateUnc)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if listBivariateUnc.subclass:
            return listBivariateUnc.subclass(*args_, **kwargs_)
        else:
            return listBivariateUnc(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_ellipsoidalRegion(self):
        return self.ellipsoidalRegion
    def set_ellipsoidalRegion(self, ellipsoidalRegion):
        self.ellipsoidalRegion = ellipsoidalRegion
    def get_rectangularRegion(self):
        return self.rectangularRegion
    def set_rectangularRegion(self, rectangularRegion):
        self.rectangularRegion = rectangularRegion
    def hasContent_(self):
        if (
            self.ellipsoidalRegion is not None or
            self.rectangularRegion is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:si="https://ptb.de/si"', name_='listBivariateUnc', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('listBivariateUnc')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'listBivariateUnc':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='listBivariateUnc')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='listBivariateUnc', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='listBivariateUnc'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:si="https://ptb.de/si"', name_='listBivariateUnc', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.ellipsoidalRegion is not None:
            namespaceprefix_ = self.ellipsoidalRegion_nsprefix_ + ':' if (UseCapturedNS_ and self.ellipsoidalRegion_nsprefix_) else ''
            self.ellipsoidalRegion.export(outfile, level, namespaceprefix_='si:', namespacedef_='', name_='ellipsoidalRegion', pretty_print=pretty_print)
        if self.rectangularRegion is not None:
            namespaceprefix_ = self.rectangularRegion_nsprefix_ + ':' if (UseCapturedNS_ and self.rectangularRegion_nsprefix_) else ''
            self.rectangularRegion.export(outfile, level, namespaceprefix_='si:', namespacedef_='', name_='rectangularRegion', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='listBivariateUnc', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{https://ptb.de/si}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{https://ptb.de/si}' + name_, nsmap=nsmap_)
        if self.ellipsoidalRegion is not None:
            ellipsoidalRegion_ = self.ellipsoidalRegion
            ellipsoidalRegion_.to_etree(element, name_='ellipsoidalRegion', mapping_=mapping_, nsmap_=nsmap_)
        if self.rectangularRegion is not None:
            rectangularRegion_ = self.rectangularRegion
            rectangularRegion_.to_etree(element, name_='rectangularRegion', mapping_=mapping_, nsmap_=nsmap_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'ellipsoidalRegion':
            obj_ = ellipsoidalRegion.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.ellipsoidalRegion = obj_
            obj_.original_tagname_ = 'ellipsoidalRegion'
        elif nodeName_ == 'rectangularRegion':
            obj_ = rectangularRegion.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.rectangularRegion = obj_
            obj_.original_tagname_ = 'rectangularRegion'
# end class listBivariateUnc


class hybrid(GeneratedsSuper):
    """The hybrid elements allows to add quantities to the
    machine readable D-SI format, with other units, than those allowed
    to be used with the SI by means of the BIPM SI brochure.
    The hybrid element can contain the following information
    1. A set of real quantities
    - all real elements provide a quantity value for one and the same measured
    quantity
    - each real element provides this quantity with a different unit
    - at least one real element provides the quantity with a machine readable
    SI unit
    - the other real quantities can use any SI or non-SI unit
    2. A set of complex quantities
    - all complex elements provide a quantity value for one and the same
    measured quantity
    - each complex element provides this quantity with a different unit(s)
    - at least one complex element provides the quantity with a machine
    readable SI unit(s)
    - the other complex quantities can use any SI or non-SI unit
    3. A set of list element
    - all list elements must provide the same quantity information and hence,
    must have
    an identical structure.
    - the lists do only differ by using different units for each of the
    quantities
    - at least one list provides all quantities only with machine readable SI
    units
    - the other lists can use any other units for the quantities
    4. A set of constant quantities
    - all constant elements provide a quantity value for one and the same
    quantity
    - each constant element provides this quantity with a different unit
    - at least one constant element provides the quantity with a machine
    readable SI unit
    - the other constant quantities can use any SI or non-SI unit"""
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, real=None, complex=None, list=None, constant=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = "si"
        if real is None:
            self.real = []
        else:
            self.real = real
        self.real_nsprefix_ = "si"
        if complex is None:
            self.complex = []
        else:
            self.complex = complex
        self.complex_nsprefix_ = "si"
        if list is None:
            self.list = []
        else:
            self.list = list
        self.list_nsprefix_ = "si"
        if constant is None:
            self.constant = []
        else:
            self.constant = constant
        self.constant_nsprefix_ = "si"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, hybrid)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if hybrid.subclass:
            return hybrid.subclass(*args_, **kwargs_)
        else:
            return hybrid(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_real(self):
        return self.real
    def set_real(self, real):
        self.real = real
    def add_real(self, value):
        self.real.append(value)
    def insert_real_at(self, index, value):
        self.real.insert(index, value)
    def replace_real_at(self, index, value):
        self.real[index] = value
    def get_complex(self):
        return self.complex
    def set_complex(self, complex):
        self.complex = complex
    def add_complex(self, value):
        self.complex.append(value)
    def insert_complex_at(self, index, value):
        self.complex.insert(index, value)
    def replace_complex_at(self, index, value):
        self.complex[index] = value
    def get_list(self):
        return self.list
    def set_list(self, list):
        self.list = list
    def add_list(self, value):
        self.list.append(value)
    def insert_list_at(self, index, value):
        self.list.insert(index, value)
    def replace_list_at(self, index, value):
        self.list[index] = value
    def get_constant(self):
        return self.constant
    def set_constant(self, constant):
        self.constant = constant
    def add_constant(self, value):
        self.constant.append(value)
    def insert_constant_at(self, index, value):
        self.constant.insert(index, value)
    def replace_constant_at(self, index, value):
        self.constant[index] = value
    def hasContent_(self):
        if (
            self.real or
            self.complex or
            self.list or
            self.constant
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:si="https://ptb.de/si"', name_='hybrid', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('hybrid')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'hybrid':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='hybrid')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='hybrid', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='hybrid'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:si="https://ptb.de/si"', name_='hybrid', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for real_ in self.real:
            namespaceprefix_ = self.real_nsprefix_ + ':' if (UseCapturedNS_ and self.real_nsprefix_) else ''
            real_.export(outfile, level, namespaceprefix_='si:', namespacedef_='', name_='real', pretty_print=pretty_print)
        for complex_ in self.complex:
            namespaceprefix_ = self.complex_nsprefix_ + ':' if (UseCapturedNS_ and self.complex_nsprefix_) else ''
            complex_.export(outfile, level, namespaceprefix_='si:', namespacedef_='', name_='complex', pretty_print=pretty_print)
        for list_ in self.list:
            namespaceprefix_ = self.list_nsprefix_ + ':' if (UseCapturedNS_ and self.list_nsprefix_) else ''
            list_.export(outfile, level, namespaceprefix_='si:', namespacedef_='', name_='list', pretty_print=pretty_print)
        for constant_ in self.constant:
            namespaceprefix_ = self.constant_nsprefix_ + ':' if (UseCapturedNS_ and self.constant_nsprefix_) else ''
            constant_.export(outfile, level, namespaceprefix_='si:', namespacedef_='', name_='constant', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='hybrid', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{https://ptb.de/si}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{https://ptb.de/si}' + name_, nsmap=nsmap_)
        for real_ in self.real:
            real_.to_etree(element, name_='real', mapping_=mapping_, nsmap_=nsmap_)
        for complex_ in self.complex:
            complex_.to_etree(element, name_='complex', mapping_=mapping_, nsmap_=nsmap_)
        for list_ in self.list:
            list_.to_etree(element, name_='list', mapping_=mapping_, nsmap_=nsmap_)
        for constant_ in self.constant:
            constant_.to_etree(element, name_='constant', mapping_=mapping_, nsmap_=nsmap_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'real':
            obj_ = real.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.real.append(obj_)
            obj_.original_tagname_ = 'real'
        elif nodeName_ == 'complex':
            obj_ = complex.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.complex.append(obj_)
            obj_.original_tagname_ = 'complex'
        elif nodeName_ == 'list':
            obj_ = list.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.list.append(obj_)
            obj_.original_tagname_ = 'list'
        elif nodeName_ == 'constant':
            obj_ = constant.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.constant.append(obj_)
            obj_.original_tagname_ = 'constant'
# end class hybrid


class columnType(GeneratedsSuper):
    """Definition of a column in the covariance matrix.
    The column has n covariance elements, where
    n is the amount of columns in the covariance matrix.
    The covariance elements are ordered as in the covariance matrix, started
    at the element in the first row of the matrix and going to the
    last row of the matrix."""
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, covariance=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if covariance is None:
            self.covariance = []
        else:
            self.covariance = covariance
        self.covariance_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, columnType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if columnType.subclass:
            return columnType.subclass(*args_, **kwargs_)
        else:
            return columnType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_covariance(self):
        return self.covariance
    def set_covariance(self, covariance):
        self.covariance = covariance
    def add_covariance(self, value):
        self.covariance.append(value)
    def insert_covariance_at(self, index, value):
        self.covariance.insert(index, value)
    def replace_covariance_at(self, index, value):
        self.covariance[index] = value
    def hasContent_(self):
        if (
            self.covariance
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:si="https://ptb.de/si"', name_='columnType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('columnType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'columnType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='columnType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='columnType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='columnType'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:si="https://ptb.de/si"', name_='columnType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for covariance_ in self.covariance:
            namespaceprefix_ = self.covariance_nsprefix_ + ':' if (UseCapturedNS_ and self.covariance_nsprefix_) else ''
            covariance_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='covariance', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='columnType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{https://ptb.de/si}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{https://ptb.de/si}' + name_, nsmap=nsmap_)
        for covariance_ in self.covariance:
            covariance_.to_etree(element, name_='covariance', mapping_=mapping_, nsmap_=nsmap_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'covariance':
            obj_ = covarianceType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.covariance.append(obj_)
            obj_.original_tagname_ = 'covariance'
# end class columnType


class covarianceType(GeneratedsSuper):
    """Each covariance component is defined by
    - element value (decimal value type)
    - element unit (string - SI format)"""
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, value=None, unit=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.value = value
        self.validate_decimalType(self.value)
        self.value_nsprefix_ = None
        self.unit = unit
        self.validate_unitType(self.unit)
        self.unit_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, covarianceType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if covarianceType.subclass:
            return covarianceType.subclass(*args_, **kwargs_)
        else:
            return covarianceType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_value(self):
        return self.value
    def set_value(self, value):
        self.value = value
    def get_unit(self):
        return self.unit
    def set_unit(self, unit):
        self.unit = unit
    def validate_decimalType(self, value):
        result = True
        # Validate type decimalType, a restriction on xs:double.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, float):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (float)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_decimalType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_decimalType_patterns_, ))
                result = False
        return result
    validate_decimalType_patterns_ = [['^([-+]?((\\d*\\.\\d+)|(\\d+\\.\\d*)|(\\d+\\.?))([Ee][-+]?\\d+)?)$']]
    def validate_unitType(self, value):
        result = True
        # Validate type unitType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            pass
        return result
    def hasContent_(self):
        if (
            self.value is not None or
            self.unit is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:si="https://ptb.de/si"', name_='covarianceType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('covarianceType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'covarianceType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='covarianceType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='covarianceType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='covarianceType'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:si="https://ptb.de/si"', name_='covarianceType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.value is not None:
            namespaceprefix_ = self.value_nsprefix_ + ':' if (UseCapturedNS_ and self.value_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%svalue>%s</%svalue>%s' % (namespaceprefix_ , self.gds_format_double(self.value, input_name='value'), namespaceprefix_ , eol_))
        if self.unit is not None:
            namespaceprefix_ = self.unit_nsprefix_ + ':' if (UseCapturedNS_ and self.unit_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sunit>%s</%sunit>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.unit), input_name='unit')), namespaceprefix_ , eol_))
    def to_etree(self, parent_element=None, name_='covarianceType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{https://ptb.de/si}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{https://ptb.de/si}' + name_, nsmap=nsmap_)
        if self.value is not None:
            value_ = self.value
            etree_.SubElement(element, '{https://ptb.de/si}value').text = self.gds_format_double(value_)
        if self.unit is not None:
            unit_ = self.unit
            etree_.SubElement(element, '{https://ptb.de/si}unit').text = self.gds_format_string(unit_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'value' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_double(sval_, node, 'value')
            fval_ = self.gds_validate_double(fval_, node, 'value')
            self.value = fval_
            self.value_nsprefix_ = child_.prefix
            # validate type decimalType
            self.validate_decimalType(self.value)
        elif nodeName_ == 'unit':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'unit')
            value_ = self.gds_validate_string(value_, node, 'unit')
            self.unit = value_
            self.unit_nsprefix_ = child_.prefix
            # validate type unitType
            self.validate_unitType(self.unit)
# end class covarianceType


class realType(GeneratedsSuper):
    """Meta data element definition for a real measurement quantity in list.
    This implementation differs from the pure real quantity in the way that
    the unit component is optional in order to allow a combination with
    a global unit in the list of real quantities."""
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, label=None, value=None, unit=None, dateTime=None, expandedUnc=None, coverageInterval=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.label = label
        self.label_nsprefix_ = None
        self.value = value
        self.validate_decimalType(self.value)
        self.value_nsprefix_ = None
        self.unit = unit
        self.validate_unitType(self.unit)
        self.unit_nsprefix_ = None
        if isinstance(dateTime, BaseStrType_):
            initvalue_ = datetime_.datetime.strptime(dateTime, '%Y-%m-%dT%H:%M:%S')
        else:
            initvalue_ = dateTime
        self.dateTime = initvalue_
        self.dateTime_nsprefix_ = None
        self.expandedUnc = expandedUnc
        self.expandedUnc_nsprefix_ = None
        self.coverageInterval = coverageInterval
        self.coverageInterval_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, realType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if realType.subclass:
            return realType.subclass(*args_, **kwargs_)
        else:
            return realType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_label(self):
        return self.label
    def set_label(self, label):
        self.label = label
    def get_value(self):
        return self.value
    def set_value(self, value):
        self.value = value
    def get_unit(self):
        return self.unit
    def set_unit(self, unit):
        self.unit = unit
    def get_dateTime(self):
        return self.dateTime
    def set_dateTime(self, dateTime):
        self.dateTime = dateTime
    def get_expandedUnc(self):
        return self.expandedUnc
    def set_expandedUnc(self, expandedUnc):
        self.expandedUnc = expandedUnc
    def get_coverageInterval(self):
        return self.coverageInterval
    def set_coverageInterval(self, coverageInterval):
        self.coverageInterval = coverageInterval
    def validate_decimalType(self, value):
        result = True
        # Validate type decimalType, a restriction on xs:double.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, float):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (float)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_decimalType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_decimalType_patterns_, ))
                result = False
        return result
    validate_decimalType_patterns_ = [['^([-+]?((\\d*\\.\\d+)|(\\d+\\.\\d*)|(\\d+\\.?))([Ee][-+]?\\d+)?)$']]
    def validate_unitType(self, value):
        result = True
        # Validate type unitType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            pass
        return result
    def hasContent_(self):
        if (
            self.label is not None or
            self.value is not None or
            self.unit is not None or
            self.dateTime is not None or
            self.expandedUnc is not None or
            self.coverageInterval is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:si="https://ptb.de/si"', name_='realType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('realType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'realType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='realType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='realType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='realType'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:si="https://ptb.de/si"', name_='realType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.label is not None:
            namespaceprefix_ = self.label_nsprefix_ + ':' if (UseCapturedNS_ and self.label_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%slabel>%s</%slabel>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.label), input_name='label')), namespaceprefix_ , eol_))
        if self.value is not None:
            namespaceprefix_ = self.value_nsprefix_ + ':' if (UseCapturedNS_ and self.value_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%svalue>%s</%svalue>%s' % (namespaceprefix_ , self.gds_format_double(self.value, input_name='value'), namespaceprefix_ , eol_))
        if self.unit is not None:
            namespaceprefix_ = self.unit_nsprefix_ + ':' if (UseCapturedNS_ and self.unit_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sunit>%s</%sunit>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.unit), input_name='unit')), namespaceprefix_ , eol_))
        if self.dateTime is not None:
            namespaceprefix_ = self.dateTime_nsprefix_ + ':' if (UseCapturedNS_ and self.dateTime_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sdateTime>%s</%sdateTime>%s' % (namespaceprefix_ , self.gds_format_datetime(self.dateTime, input_name='dateTime'), namespaceprefix_ , eol_))
        if self.expandedUnc is not None:
            namespaceprefix_ = self.expandedUnc_nsprefix_ + ':' if (UseCapturedNS_ and self.expandedUnc_nsprefix_) else ''
            self.expandedUnc.export(outfile, level, namespaceprefix_='si:', namespacedef_='', name_='expandedUnc', pretty_print=pretty_print)
        if self.coverageInterval is not None:
            namespaceprefix_ = self.coverageInterval_nsprefix_ + ':' if (UseCapturedNS_ and self.coverageInterval_nsprefix_) else ''
            self.coverageInterval.export(outfile, level, namespaceprefix_='si:', namespacedef_='', name_='coverageInterval', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='realType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{https://ptb.de/si}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{https://ptb.de/si}' + name_, nsmap=nsmap_)
        if self.label is not None:
            label_ = self.label
            etree_.SubElement(element, '{https://ptb.de/si}label').text = self.gds_format_string(label_)
        if self.value is not None:
            value_ = self.value
            etree_.SubElement(element, '{https://ptb.de/si}value').text = self.gds_format_double(value_)
        if self.unit is not None:
            unit_ = self.unit
            etree_.SubElement(element, '{https://ptb.de/si}unit').text = self.gds_format_string(unit_)
        if self.dateTime is not None:
            dateTime_ = self.dateTime
            etree_.SubElement(element, '{https://ptb.de/si}dateTime').text = self.gds_format_datetime(dateTime_)
        if self.expandedUnc is not None:
            expandedUnc_ = self.expandedUnc
            expandedUnc_.to_etree(element, name_='expandedUnc', mapping_=mapping_, nsmap_=nsmap_)
        if self.coverageInterval is not None:
            coverageInterval_ = self.coverageInterval
            coverageInterval_.to_etree(element, name_='coverageInterval', mapping_=mapping_, nsmap_=nsmap_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'label':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'label')
            value_ = self.gds_validate_string(value_, node, 'label')
            self.label = value_
            self.label_nsprefix_ = child_.prefix
        elif nodeName_ == 'value' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_double(sval_, node, 'value')
            fval_ = self.gds_validate_double(fval_, node, 'value')
            self.value = fval_
            self.value_nsprefix_ = child_.prefix
            # validate type decimalType
            self.validate_decimalType(self.value)
        elif nodeName_ == 'unit':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'unit')
            value_ = self.gds_validate_string(value_, node, 'unit')
            self.unit = value_
            self.unit_nsprefix_ = child_.prefix
            # validate type unitType
            self.validate_unitType(self.unit)
        elif nodeName_ == 'dateTime':
            sval_ = child_.text
            dval_ = self.gds_parse_datetime(sval_)
            self.dateTime = dval_
            self.dateTime_nsprefix_ = child_.prefix
        elif nodeName_ == 'expandedUnc':
            obj_ = expandedUnc.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.expandedUnc = obj_
            obj_.original_tagname_ = 'expandedUnc'
        elif nodeName_ == 'coverageInterval':
            obj_ = coverageInterval.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.coverageInterval = obj_
            obj_.original_tagname_ = 'coverageInterval'
# end class realType


class complexType(GeneratedsSuper):
    """Meta data element definition for a complex measurement quantity in list.
    This implementation differs from the pure complex quantity, in the way that
    the unit components are optional in order to allow a combination with
    a global unit in the list of complex quantities."""
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, label=None, valueReal=None, valueImag=None, valueMagnitude=None, valuePhase=None, unit=None, unitPhase=None, dateTime=None, ellipsoidalRegion=None, rectangularRegion=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.label = label
        self.label_nsprefix_ = None
        self.valueReal = valueReal
        self.validate_decimalType(self.valueReal)
        self.valueReal_nsprefix_ = None
        self.valueImag = valueImag
        self.validate_decimalType(self.valueImag)
        self.valueImag_nsprefix_ = None
        self.valueMagnitude = valueMagnitude
        self.validate_decimalType(self.valueMagnitude)
        self.valueMagnitude_nsprefix_ = None
        self.valuePhase = valuePhase
        self.validate_decimalType(self.valuePhase)
        self.valuePhase_nsprefix_ = None
        self.unit = unit
        self.validate_unitType(self.unit)
        self.unit_nsprefix_ = None
        self.unitPhase = unitPhase
        self.validate_unitPhaseType(self.unitPhase)
        self.unitPhase_nsprefix_ = None
        if isinstance(dateTime, BaseStrType_):
            initvalue_ = datetime_.datetime.strptime(dateTime, '%Y-%m-%dT%H:%M:%S')
        else:
            initvalue_ = dateTime
        self.dateTime = initvalue_
        self.dateTime_nsprefix_ = None
        self.ellipsoidalRegion = ellipsoidalRegion
        self.ellipsoidalRegion_nsprefix_ = None
        self.rectangularRegion = rectangularRegion
        self.rectangularRegion_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, complexType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if complexType.subclass:
            return complexType.subclass(*args_, **kwargs_)
        else:
            return complexType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_label(self):
        return self.label
    def set_label(self, label):
        self.label = label
    def get_valueReal(self):
        return self.valueReal
    def set_valueReal(self, valueReal):
        self.valueReal = valueReal
    def get_valueImag(self):
        return self.valueImag
    def set_valueImag(self, valueImag):
        self.valueImag = valueImag
    def get_valueMagnitude(self):
        return self.valueMagnitude
    def set_valueMagnitude(self, valueMagnitude):
        self.valueMagnitude = valueMagnitude
    def get_valuePhase(self):
        return self.valuePhase
    def set_valuePhase(self, valuePhase):
        self.valuePhase = valuePhase
    def get_unit(self):
        return self.unit
    def set_unit(self, unit):
        self.unit = unit
    def get_unitPhase(self):
        return self.unitPhase
    def set_unitPhase(self, unitPhase):
        self.unitPhase = unitPhase
    def get_dateTime(self):
        return self.dateTime
    def set_dateTime(self, dateTime):
        self.dateTime = dateTime
    def get_ellipsoidalRegion(self):
        return self.ellipsoidalRegion
    def set_ellipsoidalRegion(self, ellipsoidalRegion):
        self.ellipsoidalRegion = ellipsoidalRegion
    def get_rectangularRegion(self):
        return self.rectangularRegion
    def set_rectangularRegion(self, rectangularRegion):
        self.rectangularRegion = rectangularRegion
    def validate_decimalType(self, value):
        result = True
        # Validate type decimalType, a restriction on xs:double.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, float):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (float)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_decimalType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_decimalType_patterns_, ))
                result = False
        return result
    validate_decimalType_patterns_ = [['^([-+]?((\\d*\\.\\d+)|(\\d+\\.\\d*)|(\\d+\\.?))([Ee][-+]?\\d+)?)$']]
    def validate_unitType(self, value):
        result = True
        # Validate type unitType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            pass
        return result
    def validate_unitPhaseType(self, value):
        result = True
        # Validate type unitPhaseType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            pass
        return result
    def hasContent_(self):
        if (
            self.label is not None or
            self.valueReal is not None or
            self.valueImag is not None or
            self.valueMagnitude is not None or
            self.valuePhase is not None or
            self.unit is not None or
            self.unitPhase is not None or
            self.dateTime is not None or
            self.ellipsoidalRegion is not None or
            self.rectangularRegion is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:si="https://ptb.de/si"', name_='complexType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('complexType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'complexType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='complexType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='complexType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='complexType'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:si="https://ptb.de/si"', name_='complexType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.label is not None:
            namespaceprefix_ = self.label_nsprefix_ + ':' if (UseCapturedNS_ and self.label_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%slabel>%s</%slabel>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.label), input_name='label')), namespaceprefix_ , eol_))
        if self.valueReal is not None:
            namespaceprefix_ = self.valueReal_nsprefix_ + ':' if (UseCapturedNS_ and self.valueReal_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%svalueReal>%s</%svalueReal>%s' % (namespaceprefix_ , self.gds_format_double(self.valueReal, input_name='valueReal'), namespaceprefix_ , eol_))
        if self.valueImag is not None:
            namespaceprefix_ = self.valueImag_nsprefix_ + ':' if (UseCapturedNS_ and self.valueImag_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%svalueImag>%s</%svalueImag>%s' % (namespaceprefix_ , self.gds_format_double(self.valueImag, input_name='valueImag'), namespaceprefix_ , eol_))
        if self.valueMagnitude is not None:
            namespaceprefix_ = self.valueMagnitude_nsprefix_ + ':' if (UseCapturedNS_ and self.valueMagnitude_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%svalueMagnitude>%s</%svalueMagnitude>%s' % (namespaceprefix_ , self.gds_format_double(self.valueMagnitude, input_name='valueMagnitude'), namespaceprefix_ , eol_))
        if self.valuePhase is not None:
            namespaceprefix_ = self.valuePhase_nsprefix_ + ':' if (UseCapturedNS_ and self.valuePhase_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%svaluePhase>%s</%svaluePhase>%s' % (namespaceprefix_ , self.gds_format_double(self.valuePhase, input_name='valuePhase'), namespaceprefix_ , eol_))
        if self.unit is not None:
            namespaceprefix_ = self.unit_nsprefix_ + ':' if (UseCapturedNS_ and self.unit_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sunit>%s</%sunit>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.unit), input_name='unit')), namespaceprefix_ , eol_))
        if self.unitPhase is not None:
            namespaceprefix_ = self.unitPhase_nsprefix_ + ':' if (UseCapturedNS_ and self.unitPhase_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sunitPhase>%s</%sunitPhase>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.unitPhase), input_name='unitPhase')), namespaceprefix_ , eol_))
        if self.dateTime is not None:
            namespaceprefix_ = self.dateTime_nsprefix_ + ':' if (UseCapturedNS_ and self.dateTime_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sdateTime>%s</%sdateTime>%s' % (namespaceprefix_ , self.gds_format_datetime(self.dateTime, input_name='dateTime'), namespaceprefix_ , eol_))
        if self.ellipsoidalRegion is not None:
            namespaceprefix_ = self.ellipsoidalRegion_nsprefix_ + ':' if (UseCapturedNS_ and self.ellipsoidalRegion_nsprefix_) else ''
            self.ellipsoidalRegion.export(outfile, level, namespaceprefix_='si:', namespacedef_='', name_='ellipsoidalRegion', pretty_print=pretty_print)
        if self.rectangularRegion is not None:
            namespaceprefix_ = self.rectangularRegion_nsprefix_ + ':' if (UseCapturedNS_ and self.rectangularRegion_nsprefix_) else ''
            self.rectangularRegion.export(outfile, level, namespaceprefix_='si:', namespacedef_='', name_='rectangularRegion', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='complexType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{https://ptb.de/si}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{https://ptb.de/si}' + name_, nsmap=nsmap_)
        if self.label is not None:
            label_ = self.label
            etree_.SubElement(element, '{https://ptb.de/si}label').text = self.gds_format_string(label_)
        if self.valueReal is not None:
            valueReal_ = self.valueReal
            etree_.SubElement(element, '{https://ptb.de/si}valueReal').text = self.gds_format_double(valueReal_)
        if self.valueImag is not None:
            valueImag_ = self.valueImag
            etree_.SubElement(element, '{https://ptb.de/si}valueImag').text = self.gds_format_double(valueImag_)
        if self.valueMagnitude is not None:
            valueMagnitude_ = self.valueMagnitude
            etree_.SubElement(element, '{https://ptb.de/si}valueMagnitude').text = self.gds_format_double(valueMagnitude_)
        if self.valuePhase is not None:
            valuePhase_ = self.valuePhase
            etree_.SubElement(element, '{https://ptb.de/si}valuePhase').text = self.gds_format_double(valuePhase_)
        if self.unit is not None:
            unit_ = self.unit
            etree_.SubElement(element, '{https://ptb.de/si}unit').text = self.gds_format_string(unit_)
        if self.unitPhase is not None:
            unitPhase_ = self.unitPhase
            etree_.SubElement(element, '{https://ptb.de/si}unitPhase').text = self.gds_format_string(unitPhase_)
        if self.dateTime is not None:
            dateTime_ = self.dateTime
            etree_.SubElement(element, '{https://ptb.de/si}dateTime').text = self.gds_format_datetime(dateTime_)
        if self.ellipsoidalRegion is not None:
            ellipsoidalRegion_ = self.ellipsoidalRegion
            ellipsoidalRegion_.to_etree(element, name_='ellipsoidalRegion', mapping_=mapping_, nsmap_=nsmap_)
        if self.rectangularRegion is not None:
            rectangularRegion_ = self.rectangularRegion
            rectangularRegion_.to_etree(element, name_='rectangularRegion', mapping_=mapping_, nsmap_=nsmap_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'label':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'label')
            value_ = self.gds_validate_string(value_, node, 'label')
            self.label = value_
            self.label_nsprefix_ = child_.prefix
        elif nodeName_ == 'valueReal' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_double(sval_, node, 'valueReal')
            fval_ = self.gds_validate_double(fval_, node, 'valueReal')
            self.valueReal = fval_
            self.valueReal_nsprefix_ = child_.prefix
            # validate type decimalType
            self.validate_decimalType(self.valueReal)
        elif nodeName_ == 'valueImag' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_double(sval_, node, 'valueImag')
            fval_ = self.gds_validate_double(fval_, node, 'valueImag')
            self.valueImag = fval_
            self.valueImag_nsprefix_ = child_.prefix
            # validate type decimalType
            self.validate_decimalType(self.valueImag)
        elif nodeName_ == 'valueMagnitude' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_double(sval_, node, 'valueMagnitude')
            fval_ = self.gds_validate_double(fval_, node, 'valueMagnitude')
            self.valueMagnitude = fval_
            self.valueMagnitude_nsprefix_ = child_.prefix
            # validate type decimalType
            self.validate_decimalType(self.valueMagnitude)
        elif nodeName_ == 'valuePhase' and child_.text:
            sval_ = child_.text
            fval_ = self.gds_parse_double(sval_, node, 'valuePhase')
            fval_ = self.gds_validate_double(fval_, node, 'valuePhase')
            self.valuePhase = fval_
            self.valuePhase_nsprefix_ = child_.prefix
            # validate type decimalType
            self.validate_decimalType(self.valuePhase)
        elif nodeName_ == 'unit':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'unit')
            value_ = self.gds_validate_string(value_, node, 'unit')
            self.unit = value_
            self.unit_nsprefix_ = child_.prefix
            # validate type unitType
            self.validate_unitType(self.unit)
        elif nodeName_ == 'unitPhase':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'unitPhase')
            value_ = self.gds_validate_string(value_, node, 'unitPhase')
            self.unitPhase = value_
            self.unitPhase_nsprefix_ = child_.prefix
            # validate type unitPhaseType
            self.validate_unitPhaseType(self.unitPhase)
        elif nodeName_ == 'dateTime':
            sval_ = child_.text
            dval_ = self.gds_parse_datetime(sval_)
            self.dateTime = dval_
            self.dateTime_nsprefix_ = child_.prefix
        elif nodeName_ == 'ellipsoidalRegion':
            obj_ = ellipsoidalRegion.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.ellipsoidalRegion = obj_
            obj_.original_tagname_ = 'ellipsoidalRegion'
        elif nodeName_ == 'rectangularRegion':
            obj_ = rectangularRegion.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.rectangularRegion = obj_
            obj_.original_tagname_ = 'rectangularRegion'
# end class complexType


GDSClassesMapping = {
}


USAGE_TEXT = """
Usage: python <Parser>.py [ -s ] <in_xml_file>
"""


def usage():
    print(USAGE_TEXT)
    sys.exit(1)


def get_root_tag(node):
    tag = Tag_pattern_.match(node.tag).groups()[-1]
    rootClass = GDSClassesMapping.get(tag)
    if rootClass is None:
        rootClass = globals().get(tag)
    return tag, rootClass


def get_required_ns_prefix_defs(rootNode):
    '''Get all name space prefix definitions required in this XML doc.
    Return a dictionary of definitions and a char string of definitions.
    '''
    nsmap = {
        prefix: uri
        for node in rootNode.iter()
        for (prefix, uri) in node.nsmap.items()
        if prefix is not None
    }
    namespacedefs = ' '.join([
        'xmlns:{}="{}"'.format(prefix, uri)
        for prefix, uri in nsmap.items()
    ])
    return nsmap, namespacedefs


def parse(inFileName, silence=False, print_warnings=True):
    global CapturedNsmap_
    gds_collector = GdsCollector_()
    parser = None
    doc = parsexml_(inFileName, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'real'
        rootClass = real
    rootObj = rootClass.factory()
    rootObj.build(rootNode, gds_collector_=gds_collector)
    CapturedNsmap_, namespacedefs = get_required_ns_prefix_defs(rootNode)
    if not SaveElementTreeNode:
        doc = None
        rootNode = None
    if not silence:
        sys.stdout.write('<?xml version="1.0" ?>\n')
        rootObj.export(
            sys.stdout, 0, name_=rootTag,
            namespacedef_=namespacedefs,
            pretty_print=True)
    if print_warnings and len(gds_collector.get_messages()) > 0:
        separator = ('-' * 50) + '\n'
        sys.stderr.write(separator)
        sys.stderr.write('----- Warnings -- count: {} -----\n'.format(
            len(gds_collector.get_messages()), ))
        gds_collector.write_messages(sys.stderr)
        sys.stderr.write(separator)
    return rootObj


def parseEtree(inFileName, silence=False, print_warnings=True,
               mapping=None, nsmap=None):
    parser = None
    doc = parsexml_(inFileName, parser)
    gds_collector = GdsCollector_()
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'real'
        rootClass = real
    rootObj = rootClass.factory()
    rootObj.build(rootNode, gds_collector_=gds_collector)
    # Enable Python to collect the space used by the DOM.
    if mapping is None:
        mapping = {}
    rootElement = rootObj.to_etree(
        None, name_=rootTag, mapping_=mapping, nsmap_=nsmap)
    reverse_mapping = rootObj.gds_reverse_node_mapping(mapping)
    if not SaveElementTreeNode:
        doc = None
        rootNode = None
    if not silence:
        content = etree_.tostring(
            rootElement, pretty_print=True,
            xml_declaration=True, encoding="utf-8")
        sys.stdout.write(str(content))
        sys.stdout.write('\n')
    if print_warnings and len(gds_collector.get_messages()) > 0:
        separator = ('-' * 50) + '\n'
        sys.stderr.write(separator)
        sys.stderr.write('----- Warnings -- count: {} -----\n'.format(
            len(gds_collector.get_messages()), ))
        gds_collector.write_messages(sys.stderr)
        sys.stderr.write(separator)
    return rootObj, rootElement, mapping, reverse_mapping


def parseString(inString, silence=False, print_warnings=True):
    '''Parse a string, create the object tree, and export it.

    Arguments:
    - inString -- A string.  This XML fragment should not start
      with an XML declaration containing an encoding.
    - silence -- A boolean.  If False, export the object.
    Returns -- The root object in the tree.
    '''
    parser = None
    rootNode= parsexmlstring_(inString, parser)
    gds_collector = GdsCollector_()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'real'
        rootClass = real
    rootObj = rootClass.factory()
    rootObj.build(rootNode, gds_collector_=gds_collector)
    if not SaveElementTreeNode:
        rootNode = None
    if not silence:
        sys.stdout.write('<?xml version="1.0" ?>\n')
        rootObj.export(
            sys.stdout, 0, name_=rootTag,
            namespacedef_='xmlns:si="https://ptb.de/si"')
    if print_warnings and len(gds_collector.get_messages()) > 0:
        separator = ('-' * 50) + '\n'
        sys.stderr.write(separator)
        sys.stderr.write('----- Warnings -- count: {} -----\n'.format(
            len(gds_collector.get_messages()), ))
        gds_collector.write_messages(sys.stderr)
        sys.stderr.write(separator)
    return rootObj


def parseLiteral(inFileName, silence=False, print_warnings=True):
    parser = None
    doc = parsexml_(inFileName, parser)
    gds_collector = GdsCollector_()
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'real'
        rootClass = real
    rootObj = rootClass.factory()
    rootObj.build(rootNode, gds_collector_=gds_collector)
    # Enable Python to collect the space used by the DOM.
    if not SaveElementTreeNode:
        doc = None
        rootNode = None
    if not silence:
        sys.stdout.write('#from SI_Format1 import *\n\n')
        sys.stdout.write('import SI_Format1 as model_\n\n')
        sys.stdout.write('rootObj = model_.rootClass(\n')
        rootObj.exportLiteral(sys.stdout, 0, name_=rootTag)
        sys.stdout.write(')\n')
    if print_warnings and len(gds_collector.get_messages()) > 0:
        separator = ('-' * 50) + '\n'
        sys.stderr.write(separator)
        sys.stderr.write('----- Warnings -- count: {} -----\n'.format(
            len(gds_collector.get_messages()), ))
        gds_collector.write_messages(sys.stderr)
        sys.stderr.write(separator)
    return rootObj


def main():
    args = sys.argv[1:]
    if len(args) == 1:
        parse(args[0])
    else:
        usage()


if __name__ == '__main__':
    #import pdb; pdb.set_trace()
    main()

RenameMappings_ = {
}

#
# Mapping of namespaces to types defined in them
# and the file in which each is defined.
# simpleTypes are marked "ST" and complexTypes "CT".
NamespaceToDefMappings_ = {'https://ptb.de/si': [('unitType', 'SI_Format.xsd', 'ST'),
                       ('unitPhaseType', 'SI_Format.xsd', 'ST'),
                       ('decimalType', 'SI_Format.xsd', 'ST'),
                       ('uncertaintyValueType', 'SI_Format.xsd', 'ST'),
                       ('kValueType', 'SI_Format.xsd', 'ST'),
                       ('probabilityValueType', 'SI_Format.xsd', 'ST')]}

__all__ = [
    "columnType",
    "complex",
    "complexType",
    "constant",
    "covarianceMatrix",
    "covarianceType",
    "coverageInterval",
    "ellipsoidalRegion",
    "expandedUnc",
    "hybrid",
    "list",
    "listBivariateUnc",
    "listUnivariateUnc",
    "real",
    "realType",
    "rectangularRegion"
]
