#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Generated Thu Jun 24 21:47:28 2021 by generateDS.py version 2.38.6.
# Python 3.9.4 (default, Apr  9 2021, 16:34:09)  [GCC 7.3.0]
#
# Command line options:
#   ('-o', 'dcc1.py')
#   ('-s', 'dcc1_sub.py')
#   ('--external-encoding', 'utf-8')
#   ('--export', 'write etree')
#
# Command line arguments:
#   ../xsd-dcc-master/dcc.xsd
#
# Command line:
#   generateds/generateDS.py -o "dcc1.py" -s "dcc1_sub.py" --external-encoding="utf-8" --export="write etree" ../xsd-dcc-master/dcc.xsd
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


class issuerType(str, Enum):
    MANUFACTURER='manufacturer'
    CALIBRATION_LABORATORY='calibrationLaboratory'
    CUSTOMER='customer'
    OWNER='owner'
    OTHER='other'


class stateType(str, Enum):
    BEFORE_ADJUSTMENT='beforeAdjustment'
    AFTER_ADJUSTMENT='afterAdjustment'
    BEFORE_REPAIR='beforeRepair'
    AFTER_REPAIR='afterRepair'


class digitalCalibrationCertificateType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, schemaVersion=None, administrativeData=None, measurementResults=None, comment=None, document=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = "dcc"
        self.schemaVersion = _cast(None, schemaVersion)
        self.schemaVersion_nsprefix_ = None
        self.administrativeData = administrativeData
        self.administrativeData_nsprefix_ = "dcc"
        self.measurementResults = measurementResults
        self.measurementResults_nsprefix_ = "dcc"
        self.comment = comment
        self.comment_nsprefix_ = "dcc"
        self.document = document
        self.document_nsprefix_ = "dcc"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, digitalCalibrationCertificateType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if digitalCalibrationCertificateType.subclass:
            return digitalCalibrationCertificateType.subclass(*args_, **kwargs_)
        else:
            return digitalCalibrationCertificateType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_administrativeData(self):
        return self.administrativeData
    def set_administrativeData(self, administrativeData):
        self.administrativeData = administrativeData
    def get_measurementResults(self):
        return self.measurementResults
    def set_measurementResults(self, measurementResults):
        self.measurementResults = measurementResults
    def get_comment(self):
        return self.comment
    def set_comment(self, comment):
        self.comment = comment
    def get_document(self):
        return self.document
    def set_document(self, document):
        self.document = document
    def get_schemaVersion(self):
        return self.schemaVersion
    def set_schemaVersion(self, schemaVersion):
        self.schemaVersion = schemaVersion
    def validate_schemaVersionType(self, value):
        # Validate type schemaVersionType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_schemaVersionType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_schemaVersionType_patterns_, ))
    validate_schemaVersionType_patterns_ = [['^(2.4.0)$']]
    def hasContent_(self):
        if (
            self.administrativeData is not None or
            self.measurementResults is not None or
            self.comment is not None or
            self.document is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:dcc="https://ptb.de/dcc"', name_='digitalCalibrationCertificateType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('digitalCalibrationCertificateType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'digitalCalibrationCertificateType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='digitalCalibrationCertificateType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='digitalCalibrationCertificateType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='digitalCalibrationCertificateType'):
        if self.schemaVersion is not None and 'schemaVersion' not in already_processed:
            already_processed.add('schemaVersion')
            outfile.write(' schemaVersion=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.schemaVersion), input_name='schemaVersion')), ))
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:dcc="https://ptb.de/dcc"', name_='digitalCalibrationCertificateType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.administrativeData is not None:
            namespaceprefix_ = self.administrativeData_nsprefix_ + ':' if (UseCapturedNS_ and self.administrativeData_nsprefix_) else ''
            self.administrativeData.export(outfile, level, namespaceprefix_, namespacedef_='', name_='administrativeData', pretty_print=pretty_print)
        if self.measurementResults is not None:
            namespaceprefix_ = self.measurementResults_nsprefix_ + ':' if (UseCapturedNS_ and self.measurementResults_nsprefix_) else ''
            self.measurementResults.export(outfile, level, namespaceprefix_, namespacedef_='', name_='measurementResults', pretty_print=pretty_print)
        if self.comment is not None:
            namespaceprefix_ = self.comment_nsprefix_ + ':' if (UseCapturedNS_ and self.comment_nsprefix_) else ''
            self.comment.export(outfile, level, namespaceprefix_, namespacedef_='', name_='comment', pretty_print=pretty_print)
        if self.document is not None:
            namespaceprefix_ = self.document_nsprefix_ + ':' if (UseCapturedNS_ and self.document_nsprefix_) else ''
            self.document.export(outfile, level, namespaceprefix_, namespacedef_='', name_='document', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='digitalCalibrationCertificateType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{https://ptb.de/dcc}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{https://ptb.de/dcc}' + name_, nsmap=nsmap_)
        if self.schemaVersion is not None:
            element.set('schemaVersion', self.gds_format_string(self.schemaVersion))
        if self.administrativeData is not None:
            administrativeData_ = self.administrativeData
            administrativeData_.to_etree(element, name_='administrativeData', mapping_=mapping_, nsmap_=nsmap_)
        if self.measurementResults is not None:
            measurementResults_ = self.measurementResults
            measurementResults_.to_etree(element, name_='measurementResults', mapping_=mapping_, nsmap_=nsmap_)
        if self.comment is not None:
            comment_ = self.comment
            comment_.to_etree(element, name_='comment', mapping_=mapping_, nsmap_=nsmap_)
        if self.document is not None:
            document_ = self.document
            document_.to_etree(element, name_='document', mapping_=mapping_, nsmap_=nsmap_)
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
        value = find_attr_value_('schemaVersion', node)
        if value is not None and 'schemaVersion' not in already_processed:
            already_processed.add('schemaVersion')
            self.schemaVersion = value
            self.validate_schemaVersionType(self.schemaVersion)    # validate type schemaVersionType
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'administrativeData':
            obj_ = administrativeDataType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.administrativeData = obj_
            obj_.original_tagname_ = 'administrativeData'
        elif nodeName_ == 'measurementResults':
            obj_ = measurementResultListType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.measurementResults = obj_
            obj_.original_tagname_ = 'measurementResults'
        elif nodeName_ == 'comment':
            obj_ = commentType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.comment = obj_
            obj_.original_tagname_ = 'comment'
        elif nodeName_ == 'document':
            obj_ = byteDataType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.document = obj_
            obj_.original_tagname_ = 'document'
# end class digitalCalibrationCertificateType


class administrativeDataType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, dccSoftware=None, coreData=None, items=None, calibrationLaboratory=None, respPersons=None, customer=None, statements=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = "dcc"
        self.dccSoftware = dccSoftware
        self.dccSoftware_nsprefix_ = "dcc"
        self.coreData = coreData
        self.coreData_nsprefix_ = "dcc"
        self.items = items
        self.items_nsprefix_ = "dcc"
        self.calibrationLaboratory = calibrationLaboratory
        self.calibrationLaboratory_nsprefix_ = "dcc"
        self.respPersons = respPersons
        self.respPersons_nsprefix_ = "dcc"
        self.customer = customer
        self.customer_nsprefix_ = "dcc"
        self.statements = statements
        self.statements_nsprefix_ = "dcc"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, administrativeDataType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if administrativeDataType.subclass:
            return administrativeDataType.subclass(*args_, **kwargs_)
        else:
            return administrativeDataType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_dccSoftware(self):
        return self.dccSoftware
    def set_dccSoftware(self, dccSoftware):
        self.dccSoftware = dccSoftware
    def get_coreData(self):
        return self.coreData
    def set_coreData(self, coreData):
        self.coreData = coreData
    def get_items(self):
        return self.items
    def set_items(self, items):
        self.items = items
    def get_calibrationLaboratory(self):
        return self.calibrationLaboratory
    def set_calibrationLaboratory(self, calibrationLaboratory):
        self.calibrationLaboratory = calibrationLaboratory
    def get_respPersons(self):
        return self.respPersons
    def set_respPersons(self, respPersons):
        self.respPersons = respPersons
    def get_customer(self):
        return self.customer
    def set_customer(self, customer):
        self.customer = customer
    def get_statements(self):
        return self.statements
    def set_statements(self, statements):
        self.statements = statements
    def hasContent_(self):
        if (
            self.dccSoftware is not None or
            self.coreData is not None or
            self.items is not None or
            self.calibrationLaboratory is not None or
            self.respPersons is not None or
            self.customer is not None or
            self.statements is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:dcc="https://ptb.de/dcc"', name_='administrativeDataType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('administrativeDataType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'administrativeDataType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='administrativeDataType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='administrativeDataType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='administrativeDataType'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:dcc="https://ptb.de/dcc"', name_='administrativeDataType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.dccSoftware is not None:
            namespaceprefix_ = self.dccSoftware_nsprefix_ + ':' if (UseCapturedNS_ and self.dccSoftware_nsprefix_) else ''
            self.dccSoftware.export(outfile, level, namespaceprefix_, namespacedef_='', name_='dccSoftware', pretty_print=pretty_print)
        if self.coreData is not None:
            namespaceprefix_ = self.coreData_nsprefix_ + ':' if (UseCapturedNS_ and self.coreData_nsprefix_) else ''
            self.coreData.export(outfile, level, namespaceprefix_, namespacedef_='', name_='coreData', pretty_print=pretty_print)
        if self.items is not None:
            namespaceprefix_ = self.items_nsprefix_ + ':' if (UseCapturedNS_ and self.items_nsprefix_) else ''
            self.items.export(outfile, level, namespaceprefix_, namespacedef_='', name_='items', pretty_print=pretty_print)
        if self.calibrationLaboratory is not None:
            namespaceprefix_ = self.calibrationLaboratory_nsprefix_ + ':' if (UseCapturedNS_ and self.calibrationLaboratory_nsprefix_) else ''
            self.calibrationLaboratory.export(outfile, level, namespaceprefix_, namespacedef_='', name_='calibrationLaboratory', pretty_print=pretty_print)
        if self.respPersons is not None:
            namespaceprefix_ = self.respPersons_nsprefix_ + ':' if (UseCapturedNS_ and self.respPersons_nsprefix_) else ''
            self.respPersons.export(outfile, level, namespaceprefix_, namespacedef_='', name_='respPersons', pretty_print=pretty_print)
        if self.customer is not None:
            namespaceprefix_ = self.customer_nsprefix_ + ':' if (UseCapturedNS_ and self.customer_nsprefix_) else ''
            self.customer.export(outfile, level, namespaceprefix_, namespacedef_='', name_='customer', pretty_print=pretty_print)
        if self.statements is not None:
            namespaceprefix_ = self.statements_nsprefix_ + ':' if (UseCapturedNS_ and self.statements_nsprefix_) else ''
            self.statements.export(outfile, level, namespaceprefix_, namespacedef_='', name_='statements', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='administrativeDataType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{https://ptb.de/dcc}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{https://ptb.de/dcc}' + name_, nsmap=nsmap_)
        if self.dccSoftware is not None:
            dccSoftware_ = self.dccSoftware
            dccSoftware_.to_etree(element, name_='dccSoftware', mapping_=mapping_, nsmap_=nsmap_)
        if self.coreData is not None:
            coreData_ = self.coreData
            coreData_.to_etree(element, name_='coreData', mapping_=mapping_, nsmap_=nsmap_)
        if self.items is not None:
            items_ = self.items
            items_.to_etree(element, name_='items', mapping_=mapping_, nsmap_=nsmap_)
        if self.calibrationLaboratory is not None:
            calibrationLaboratory_ = self.calibrationLaboratory
            calibrationLaboratory_.to_etree(element, name_='calibrationLaboratory', mapping_=mapping_, nsmap_=nsmap_)
        if self.respPersons is not None:
            respPersons_ = self.respPersons
            respPersons_.to_etree(element, name_='respPersons', mapping_=mapping_, nsmap_=nsmap_)
        if self.customer is not None:
            customer_ = self.customer
            customer_.to_etree(element, name_='customer', mapping_=mapping_, nsmap_=nsmap_)
        if self.statements is not None:
            statements_ = self.statements
            statements_.to_etree(element, name_='statements', mapping_=mapping_, nsmap_=nsmap_)
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
        if nodeName_ == 'dccSoftware':
            obj_ = softwareListType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.dccSoftware = obj_
            obj_.original_tagname_ = 'dccSoftware'
        elif nodeName_ == 'coreData':
            obj_ = coreDataType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.coreData = obj_
            obj_.original_tagname_ = 'coreData'
        elif nodeName_ == 'items':
            obj_ = itemListType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.items = obj_
            obj_.original_tagname_ = 'items'
        elif nodeName_ == 'calibrationLaboratory':
            obj_ = calibrationLaboratoryType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.calibrationLaboratory = obj_
            obj_.original_tagname_ = 'calibrationLaboratory'
        elif nodeName_ == 'respPersons':
            obj_ = respPersonListType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.respPersons = obj_
            obj_.original_tagname_ = 'respPersons'
        elif nodeName_ == 'customer':
            obj_ = contactType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.customer = obj_
            obj_.original_tagname_ = 'customer'
        elif nodeName_ == 'statements':
            obj_ = statementListType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.statements = obj_
            obj_.original_tagname_ = 'statements'
# end class administrativeDataType


class softwareListType(GeneratedsSuper):
    """Clear description of the software-version and the creator of the
    software used to create and process the
    DCC"""
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, software=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = "dcc"
        if software is None:
            self.software = []
        else:
            self.software = software
        self.software_nsprefix_ = "dcc"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, softwareListType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if softwareListType.subclass:
            return softwareListType.subclass(*args_, **kwargs_)
        else:
            return softwareListType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_software(self):
        return self.software
    def set_software(self, software):
        self.software = software
    def add_software(self, value):
        self.software.append(value)
    def insert_software_at(self, index, value):
        self.software.insert(index, value)
    def replace_software_at(self, index, value):
        self.software[index] = value
    def hasContent_(self):
        if (
            self.software
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:dcc="https://ptb.de/dcc"', name_='softwareListType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('softwareListType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'softwareListType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='softwareListType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='softwareListType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='softwareListType'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:dcc="https://ptb.de/dcc"', name_='softwareListType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for software_ in self.software:
            namespaceprefix_ = self.software_nsprefix_ + ':' if (UseCapturedNS_ and self.software_nsprefix_) else ''
            software_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='software', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='softwareListType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{https://ptb.de/dcc}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{https://ptb.de/dcc}' + name_, nsmap=nsmap_)
        for software_ in self.software:
            software_.to_etree(element, name_='software', mapping_=mapping_, nsmap_=nsmap_)
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
        if nodeName_ == 'software':
            obj_ = softwareType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.software.append(obj_)
            obj_.original_tagname_ = 'software'
# end class softwareListType


class softwareType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, id=None, name=None, release=None, description=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = "dcc"
        self.id = _cast(None, id)
        self.id_nsprefix_ = None
        self.name = name
        self.name_nsprefix_ = "dcc"
        self.release = release
        self.release_nsprefix_ = "dcc"
        if description is None:
            self.description = []
        else:
            self.description = description
        self.description_nsprefix_ = "dcc"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, softwareType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if softwareType.subclass:
            return softwareType.subclass(*args_, **kwargs_)
        else:
            return softwareType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name
    def get_release(self):
        return self.release
    def set_release(self, release):
        self.release = release
    def get_description(self):
        return self.description
    def set_description(self, description):
        self.description = description
    def add_description(self, value):
        self.description.append(value)
    def insert_description_at(self, index, value):
        self.description.insert(index, value)
    def replace_description_at(self, index, value):
        self.description[index] = value
    def get_id(self):
        return self.id
    def set_id(self, id):
        self.id = id
    def hasContent_(self):
        if (
            self.name is not None or
            self.release is not None or
            self.description
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:dcc="https://ptb.de/dcc"', name_='softwareType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('softwareType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'softwareType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='softwareType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='softwareType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='softwareType'):
        if self.id is not None and 'id' not in already_processed:
            already_processed.add('id')
            outfile.write(' id=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.id), input_name='id')), ))
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:dcc="https://ptb.de/dcc"', name_='softwareType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.name is not None:
            namespaceprefix_ = self.name_nsprefix_ + ':' if (UseCapturedNS_ and self.name_nsprefix_) else ''
            self.name.export(outfile, level, namespaceprefix_, namespacedef_='', name_='name', pretty_print=pretty_print)
        if self.release is not None:
            namespaceprefix_ = self.release_nsprefix_ + ':' if (UseCapturedNS_ and self.release_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%srelease>%s</%srelease>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.release), input_name='release')), namespaceprefix_ , eol_))
        for description_ in self.description:
            namespaceprefix_ = self.description_nsprefix_ + ':' if (UseCapturedNS_ and self.description_nsprefix_) else ''
            description_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='description', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='softwareType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{https://ptb.de/dcc}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{https://ptb.de/dcc}' + name_, nsmap=nsmap_)
        if self.id is not None:
            element.set('id', self.gds_format_string(self.id))
        if self.name is not None:
            name_ = self.name
            name_.to_etree(element, name_='name', mapping_=mapping_, nsmap_=nsmap_)
        if self.release is not None:
            release_ = self.release
            etree_.SubElement(element, '{https://ptb.de/dcc}release').text = self.gds_format_string(release_)
        for description_ in self.description:
            description_.to_etree(element, name_='description', mapping_=mapping_, nsmap_=nsmap_)
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
        value = find_attr_value_('id', node)
        if value is not None and 'id' not in already_processed:
            already_processed.add('id')
            self.id = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'name':
            obj_ = textType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.name = obj_
            obj_.original_tagname_ = 'name'
        elif nodeName_ == 'release':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'release')
            value_ = self.gds_validate_string(value_, node, 'release')
            self.release = value_
            self.release_nsprefix_ = child_.prefix
        elif nodeName_ == 'description':
            obj_ = textType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.description.append(obj_)
            obj_.original_tagname_ = 'description'
# end class softwareType


class measuringEquipmentListType(GeneratedsSuper):
    """Information about the instruments used"""
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, measuringEquipment=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = "dcc"
        if measuringEquipment is None:
            self.measuringEquipment = []
        else:
            self.measuringEquipment = measuringEquipment
        self.measuringEquipment_nsprefix_ = "dcc"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, measuringEquipmentListType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if measuringEquipmentListType.subclass:
            return measuringEquipmentListType.subclass(*args_, **kwargs_)
        else:
            return measuringEquipmentListType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_measuringEquipment(self):
        return self.measuringEquipment
    def set_measuringEquipment(self, measuringEquipment):
        self.measuringEquipment = measuringEquipment
    def add_measuringEquipment(self, value):
        self.measuringEquipment.append(value)
    def insert_measuringEquipment_at(self, index, value):
        self.measuringEquipment.insert(index, value)
    def replace_measuringEquipment_at(self, index, value):
        self.measuringEquipment[index] = value
    def hasContent_(self):
        if (
            self.measuringEquipment
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:dcc="https://ptb.de/dcc"', name_='measuringEquipmentListType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('measuringEquipmentListType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'measuringEquipmentListType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='measuringEquipmentListType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='measuringEquipmentListType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='measuringEquipmentListType'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:dcc="https://ptb.de/dcc"', name_='measuringEquipmentListType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for measuringEquipment_ in self.measuringEquipment:
            namespaceprefix_ = self.measuringEquipment_nsprefix_ + ':' if (UseCapturedNS_ and self.measuringEquipment_nsprefix_) else ''
            measuringEquipment_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='measuringEquipment', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='measuringEquipmentListType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{https://ptb.de/dcc}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{https://ptb.de/dcc}' + name_, nsmap=nsmap_)
        for measuringEquipment_ in self.measuringEquipment:
            measuringEquipment_.to_etree(element, name_='measuringEquipment', mapping_=mapping_, nsmap_=nsmap_)
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
        if nodeName_ == 'measuringEquipment':
            obj_ = measuringEquipmentType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.measuringEquipment.append(obj_)
            obj_.original_tagname_ = 'measuringEquipment'
# end class measuringEquipmentListType


class measuringEquipmentType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, id=None, name=None, equipmentClass=None, description=None, descriptionData=None, certificate=None, manufacturer=None, model=None, identifications=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = "dcc"
        self.id = _cast(None, id)
        self.id_nsprefix_ = None
        self.name = name
        self.name_nsprefix_ = "dcc"
        self.equipmentClass = equipmentClass
        self.equipmentClass_nsprefix_ = "dcc"
        if description is None:
            self.description = []
        else:
            self.description = description
        self.description_nsprefix_ = "dcc"
        if descriptionData is None:
            self.descriptionData = []
        else:
            self.descriptionData = descriptionData
        self.descriptionData_nsprefix_ = "dcc"
        self.certificate = certificate
        self.certificate_nsprefix_ = "dcc"
        self.manufacturer = manufacturer
        self.manufacturer_nsprefix_ = "dcc"
        self.model = model
        self.model_nsprefix_ = "dcc"
        self.identifications = identifications
        self.identifications_nsprefix_ = "dcc"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, measuringEquipmentType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if measuringEquipmentType.subclass:
            return measuringEquipmentType.subclass(*args_, **kwargs_)
        else:
            return measuringEquipmentType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name
    def get_equipmentClass(self):
        return self.equipmentClass
    def set_equipmentClass(self, equipmentClass):
        self.equipmentClass = equipmentClass
    def get_description(self):
        return self.description
    def set_description(self, description):
        self.description = description
    def add_description(self, value):
        self.description.append(value)
    def insert_description_at(self, index, value):
        self.description.insert(index, value)
    def replace_description_at(self, index, value):
        self.description[index] = value
    def get_descriptionData(self):
        return self.descriptionData
    def set_descriptionData(self, descriptionData):
        self.descriptionData = descriptionData
    def add_descriptionData(self, value):
        self.descriptionData.append(value)
    def insert_descriptionData_at(self, index, value):
        self.descriptionData.insert(index, value)
    def replace_descriptionData_at(self, index, value):
        self.descriptionData[index] = value
    def get_certificate(self):
        return self.certificate
    def set_certificate(self, certificate):
        self.certificate = certificate
    def get_manufacturer(self):
        return self.manufacturer
    def set_manufacturer(self, manufacturer):
        self.manufacturer = manufacturer
    def get_model(self):
        return self.model
    def set_model(self, model):
        self.model = model
    def get_identifications(self):
        return self.identifications
    def set_identifications(self, identifications):
        self.identifications = identifications
    def get_id(self):
        return self.id
    def set_id(self, id):
        self.id = id
    def hasContent_(self):
        if (
            self.name is not None or
            self.equipmentClass is not None or
            self.description or
            self.descriptionData or
            self.certificate is not None or
            self.manufacturer is not None or
            self.model is not None or
            self.identifications is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:dcc="https://ptb.de/dcc"', name_='measuringEquipmentType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('measuringEquipmentType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'measuringEquipmentType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='measuringEquipmentType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='measuringEquipmentType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='measuringEquipmentType'):
        if self.id is not None and 'id' not in already_processed:
            already_processed.add('id')
            outfile.write(' id=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.id), input_name='id')), ))
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:dcc="https://ptb.de/dcc"', name_='measuringEquipmentType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.name is not None:
            namespaceprefix_ = self.name_nsprefix_ + ':' if (UseCapturedNS_ and self.name_nsprefix_) else ''
            self.name.export(outfile, level, namespaceprefix_, namespacedef_='', name_='name', pretty_print=pretty_print)
        if self.equipmentClass is not None:
            namespaceprefix_ = self.equipmentClass_nsprefix_ + ':' if (UseCapturedNS_ and self.equipmentClass_nsprefix_) else ''
            self.equipmentClass.export(outfile, level, namespaceprefix_, namespacedef_='', name_='equipmentClass', pretty_print=pretty_print)
        for description_ in self.description:
            namespaceprefix_ = self.description_nsprefix_ + ':' if (UseCapturedNS_ and self.description_nsprefix_) else ''
            description_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='description', pretty_print=pretty_print)
        for descriptionData_ in self.descriptionData:
            namespaceprefix_ = self.descriptionData_nsprefix_ + ':' if (UseCapturedNS_ and self.descriptionData_nsprefix_) else ''
            descriptionData_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='descriptionData', pretty_print=pretty_print)
        if self.certificate is not None:
            namespaceprefix_ = self.certificate_nsprefix_ + ':' if (UseCapturedNS_ and self.certificate_nsprefix_) else ''
            self.certificate.export(outfile, level, namespaceprefix_, namespacedef_='', name_='certificate', pretty_print=pretty_print)
        if self.manufacturer is not None:
            namespaceprefix_ = self.manufacturer_nsprefix_ + ':' if (UseCapturedNS_ and self.manufacturer_nsprefix_) else ''
            self.manufacturer.export(outfile, level, namespaceprefix_, namespacedef_='', name_='manufacturer', pretty_print=pretty_print)
        if self.model is not None:
            namespaceprefix_ = self.model_nsprefix_ + ':' if (UseCapturedNS_ and self.model_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%smodel>%s</%smodel>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.model), input_name='model')), namespaceprefix_ , eol_))
        if self.identifications is not None:
            namespaceprefix_ = self.identifications_nsprefix_ + ':' if (UseCapturedNS_ and self.identifications_nsprefix_) else ''
            self.identifications.export(outfile, level, namespaceprefix_, namespacedef_='', name_='identifications', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='measuringEquipmentType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{https://ptb.de/dcc}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{https://ptb.de/dcc}' + name_, nsmap=nsmap_)
        if self.id is not None:
            element.set('id', self.gds_format_string(self.id))
        if self.name is not None:
            name_ = self.name
            name_.to_etree(element, name_='name', mapping_=mapping_, nsmap_=nsmap_)
        if self.equipmentClass is not None:
            equipmentClass_ = self.equipmentClass
            equipmentClass_.to_etree(element, name_='equipmentClass', mapping_=mapping_, nsmap_=nsmap_)
        for description_ in self.description:
            description_.to_etree(element, name_='description', mapping_=mapping_, nsmap_=nsmap_)
        for descriptionData_ in self.descriptionData:
            descriptionData_.to_etree(element, name_='descriptionData', mapping_=mapping_, nsmap_=nsmap_)
        if self.certificate is not None:
            certificate_ = self.certificate
            certificate_.to_etree(element, name_='certificate', mapping_=mapping_, nsmap_=nsmap_)
        if self.manufacturer is not None:
            manufacturer_ = self.manufacturer
            manufacturer_.to_etree(element, name_='manufacturer', mapping_=mapping_, nsmap_=nsmap_)
        if self.model is not None:
            model_ = self.model
            etree_.SubElement(element, '{https://ptb.de/dcc}model').text = self.gds_format_string(model_)
        if self.identifications is not None:
            identifications_ = self.identifications
            identifications_.to_etree(element, name_='identifications', mapping_=mapping_, nsmap_=nsmap_)
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
        value = find_attr_value_('id', node)
        if value is not None and 'id' not in already_processed:
            already_processed.add('id')
            self.id = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'name':
            obj_ = textType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.name = obj_
            obj_.original_tagname_ = 'name'
        elif nodeName_ == 'equipmentClass':
            obj_ = equipmentClassType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.equipmentClass = obj_
            obj_.original_tagname_ = 'equipmentClass'
        elif nodeName_ == 'description':
            obj_ = textType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.description.append(obj_)
            obj_.original_tagname_ = 'description'
        elif nodeName_ == 'descriptionData':
            obj_ = byteDataType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.descriptionData.append(obj_)
            obj_.original_tagname_ = 'descriptionData'
        elif nodeName_ == 'certificate':
            obj_ = hashType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.certificate = obj_
            obj_.original_tagname_ = 'certificate'
        elif nodeName_ == 'manufacturer':
            obj_ = contactNotStrictType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.manufacturer = obj_
            obj_.original_tagname_ = 'manufacturer'
        elif nodeName_ == 'model':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'model')
            value_ = self.gds_validate_string(value_, node, 'model')
            self.model = value_
            self.model_nsprefix_ = child_.prefix
        elif nodeName_ == 'identifications':
            obj_ = identificationListType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.identifications = obj_
            obj_.original_tagname_ = 'identifications'
# end class measuringEquipmentType


class coreDataType(GeneratedsSuper):
    """Basic parameters of the Digital Calibration Certificate (DCC)"""
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, countryCodeISO3166_1=None, usedLangCodeISO639_1=None, mandatoryLangCodeISO639_1=None, uniqueIdentifier=None, identifications=None, receiptDate=None, beginPerformanceDate=None, endPerformanceDate=None, previousReport=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = "dcc"
        self.countryCodeISO3166_1 = countryCodeISO3166_1
        self.validate_stringISO3166Type(self.countryCodeISO3166_1)
        self.countryCodeISO3166_1_nsprefix_ = "dcc"
        if usedLangCodeISO639_1 is None:
            self.usedLangCodeISO639_1 = []
        else:
            self.usedLangCodeISO639_1 = usedLangCodeISO639_1
        self.usedLangCodeISO639_1_nsprefix_ = "dcc"
        if mandatoryLangCodeISO639_1 is None:
            self.mandatoryLangCodeISO639_1 = []
        else:
            self.mandatoryLangCodeISO639_1 = mandatoryLangCodeISO639_1
        self.mandatoryLangCodeISO639_1_nsprefix_ = "dcc"
        self.uniqueIdentifier = uniqueIdentifier
        self.uniqueIdentifier_nsprefix_ = "dcc"
        self.identifications = identifications
        self.identifications_nsprefix_ = "dcc"
        if isinstance(receiptDate, BaseStrType_):
            initvalue_ = datetime_.datetime.strptime(receiptDate, '%Y-%m-%d').date()
        else:
            initvalue_ = receiptDate
        self.receiptDate = initvalue_
        self.receiptDate_nsprefix_ = "dcc"
        if isinstance(beginPerformanceDate, BaseStrType_):
            initvalue_ = datetime_.datetime.strptime(beginPerformanceDate, '%Y-%m-%d').date()
        else:
            initvalue_ = beginPerformanceDate
        self.beginPerformanceDate = initvalue_
        self.beginPerformanceDate_nsprefix_ = "dcc"
        if isinstance(endPerformanceDate, BaseStrType_):
            initvalue_ = datetime_.datetime.strptime(endPerformanceDate, '%Y-%m-%d').date()
        else:
            initvalue_ = endPerformanceDate
        self.endPerformanceDate = initvalue_
        self.endPerformanceDate_nsprefix_ = "dcc"
        self.previousReport = previousReport
        self.previousReport_nsprefix_ = "dcc"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, coreDataType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if coreDataType.subclass:
            return coreDataType.subclass(*args_, **kwargs_)
        else:
            return coreDataType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_countryCodeISO3166_1(self):
        return self.countryCodeISO3166_1
    def set_countryCodeISO3166_1(self, countryCodeISO3166_1):
        self.countryCodeISO3166_1 = countryCodeISO3166_1
    def get_usedLangCodeISO639_1(self):
        return self.usedLangCodeISO639_1
    def set_usedLangCodeISO639_1(self, usedLangCodeISO639_1):
        self.usedLangCodeISO639_1 = usedLangCodeISO639_1
    def add_usedLangCodeISO639_1(self, value):
        self.usedLangCodeISO639_1.append(value)
    def insert_usedLangCodeISO639_1_at(self, index, value):
        self.usedLangCodeISO639_1.insert(index, value)
    def replace_usedLangCodeISO639_1_at(self, index, value):
        self.usedLangCodeISO639_1[index] = value
    def get_mandatoryLangCodeISO639_1(self):
        return self.mandatoryLangCodeISO639_1
    def set_mandatoryLangCodeISO639_1(self, mandatoryLangCodeISO639_1):
        self.mandatoryLangCodeISO639_1 = mandatoryLangCodeISO639_1
    def add_mandatoryLangCodeISO639_1(self, value):
        self.mandatoryLangCodeISO639_1.append(value)
    def insert_mandatoryLangCodeISO639_1_at(self, index, value):
        self.mandatoryLangCodeISO639_1.insert(index, value)
    def replace_mandatoryLangCodeISO639_1_at(self, index, value):
        self.mandatoryLangCodeISO639_1[index] = value
    def get_uniqueIdentifier(self):
        return self.uniqueIdentifier
    def set_uniqueIdentifier(self, uniqueIdentifier):
        self.uniqueIdentifier = uniqueIdentifier
    def get_identifications(self):
        return self.identifications
    def set_identifications(self, identifications):
        self.identifications = identifications
    def get_receiptDate(self):
        return self.receiptDate
    def set_receiptDate(self, receiptDate):
        self.receiptDate = receiptDate
    def get_beginPerformanceDate(self):
        return self.beginPerformanceDate
    def set_beginPerformanceDate(self, beginPerformanceDate):
        self.beginPerformanceDate = beginPerformanceDate
    def get_endPerformanceDate(self):
        return self.endPerformanceDate
    def set_endPerformanceDate(self, endPerformanceDate):
        self.endPerformanceDate = endPerformanceDate
    def get_previousReport(self):
        return self.previousReport
    def set_previousReport(self, previousReport):
        self.previousReport = previousReport
    def validate_stringISO3166Type(self, value):
        result = True
        # Validate type stringISO3166Type, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_stringISO3166Type_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_stringISO3166Type_patterns_, ))
                result = False
        return result
    validate_stringISO3166Type_patterns_ = [['^([A-Z]{2})$']]
    def validate_stringISO639Type(self, value):
        result = True
        # Validate type stringISO639Type, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_stringISO639Type_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_stringISO639Type_patterns_, ))
                result = False
        return result
    validate_stringISO639Type_patterns_ = [['^([a-z]{2})$']]
    def hasContent_(self):
        if (
            self.countryCodeISO3166_1 is not None or
            self.usedLangCodeISO639_1 or
            self.mandatoryLangCodeISO639_1 or
            self.uniqueIdentifier is not None or
            self.identifications is not None or
            self.receiptDate is not None or
            self.beginPerformanceDate is not None or
            self.endPerformanceDate is not None or
            self.previousReport is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:dcc="https://ptb.de/dcc"', name_='coreDataType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('coreDataType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'coreDataType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='coreDataType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='coreDataType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='coreDataType'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:dcc="https://ptb.de/dcc"', name_='coreDataType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.countryCodeISO3166_1 is not None:
            namespaceprefix_ = self.countryCodeISO3166_1_nsprefix_ + ':' if (UseCapturedNS_ and self.countryCodeISO3166_1_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scountryCodeISO3166_1>%s</%scountryCodeISO3166_1>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.countryCodeISO3166_1), input_name='countryCodeISO3166_1')), namespaceprefix_ , eol_))
        for usedLangCodeISO639_1_ in self.usedLangCodeISO639_1:
            namespaceprefix_ = self.usedLangCodeISO639_1_nsprefix_ + ':' if (UseCapturedNS_ and self.usedLangCodeISO639_1_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%susedLangCodeISO639_1>%s</%susedLangCodeISO639_1>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(usedLangCodeISO639_1_), input_name='usedLangCodeISO639_1')), namespaceprefix_ , eol_))
        for mandatoryLangCodeISO639_1_ in self.mandatoryLangCodeISO639_1:
            namespaceprefix_ = self.mandatoryLangCodeISO639_1_nsprefix_ + ':' if (UseCapturedNS_ and self.mandatoryLangCodeISO639_1_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%smandatoryLangCodeISO639_1>%s</%smandatoryLangCodeISO639_1>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(mandatoryLangCodeISO639_1_), input_name='mandatoryLangCodeISO639_1')), namespaceprefix_ , eol_))
        if self.uniqueIdentifier is not None:
            namespaceprefix_ = self.uniqueIdentifier_nsprefix_ + ':' if (UseCapturedNS_ and self.uniqueIdentifier_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%suniqueIdentifier>%s</%suniqueIdentifier>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.uniqueIdentifier), input_name='uniqueIdentifier')), namespaceprefix_ , eol_))
        if self.identifications is not None:
            namespaceprefix_ = self.identifications_nsprefix_ + ':' if (UseCapturedNS_ and self.identifications_nsprefix_) else ''
            self.identifications.export(outfile, level, namespaceprefix_, namespacedef_='', name_='identifications', pretty_print=pretty_print)
        if self.receiptDate is not None:
            namespaceprefix_ = self.receiptDate_nsprefix_ + ':' if (UseCapturedNS_ and self.receiptDate_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sreceiptDate>%s</%sreceiptDate>%s' % (namespaceprefix_ , self.gds_format_date(self.receiptDate, input_name='receiptDate'), namespaceprefix_ , eol_))
        if self.beginPerformanceDate is not None:
            namespaceprefix_ = self.beginPerformanceDate_nsprefix_ + ':' if (UseCapturedNS_ and self.beginPerformanceDate_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sbeginPerformanceDate>%s</%sbeginPerformanceDate>%s' % (namespaceprefix_ , self.gds_format_date(self.beginPerformanceDate, input_name='beginPerformanceDate'), namespaceprefix_ , eol_))
        if self.endPerformanceDate is not None:
            namespaceprefix_ = self.endPerformanceDate_nsprefix_ + ':' if (UseCapturedNS_ and self.endPerformanceDate_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sendPerformanceDate>%s</%sendPerformanceDate>%s' % (namespaceprefix_ , self.gds_format_date(self.endPerformanceDate, input_name='endPerformanceDate'), namespaceprefix_ , eol_))
        if self.previousReport is not None:
            namespaceprefix_ = self.previousReport_nsprefix_ + ':' if (UseCapturedNS_ and self.previousReport_nsprefix_) else ''
            self.previousReport.export(outfile, level, namespaceprefix_, namespacedef_='', name_='previousReport', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='coreDataType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{https://ptb.de/dcc}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{https://ptb.de/dcc}' + name_, nsmap=nsmap_)
        if self.countryCodeISO3166_1 is not None:
            countryCodeISO3166_1_ = self.countryCodeISO3166_1
            etree_.SubElement(element, '{https://ptb.de/dcc}countryCodeISO3166_1').text = self.gds_format_string(countryCodeISO3166_1_)
        for usedLangCodeISO639_1_ in self.usedLangCodeISO639_1:
            etree_.SubElement(element, '{https://ptb.de/dcc}usedLangCodeISO639_1').text = self.gds_format_string(usedLangCodeISO639_1_)
        for mandatoryLangCodeISO639_1_ in self.mandatoryLangCodeISO639_1:
            etree_.SubElement(element, '{https://ptb.de/dcc}mandatoryLangCodeISO639_1').text = self.gds_format_string(mandatoryLangCodeISO639_1_)
        if self.uniqueIdentifier is not None:
            uniqueIdentifier_ = self.uniqueIdentifier
            etree_.SubElement(element, '{https://ptb.de/dcc}uniqueIdentifier').text = self.gds_format_string(uniqueIdentifier_)
        if self.identifications is not None:
            identifications_ = self.identifications
            identifications_.to_etree(element, name_='identifications', mapping_=mapping_, nsmap_=nsmap_)
        if self.receiptDate is not None:
            receiptDate_ = self.receiptDate
            etree_.SubElement(element, '{https://ptb.de/dcc}receiptDate').text = self.gds_format_date(receiptDate_)
        if self.beginPerformanceDate is not None:
            beginPerformanceDate_ = self.beginPerformanceDate
            etree_.SubElement(element, '{https://ptb.de/dcc}beginPerformanceDate').text = self.gds_format_date(beginPerformanceDate_)
        if self.endPerformanceDate is not None:
            endPerformanceDate_ = self.endPerformanceDate
            etree_.SubElement(element, '{https://ptb.de/dcc}endPerformanceDate').text = self.gds_format_date(endPerformanceDate_)
        if self.previousReport is not None:
            previousReport_ = self.previousReport
            previousReport_.to_etree(element, name_='previousReport', mapping_=mapping_, nsmap_=nsmap_)
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
        if nodeName_ == 'countryCodeISO3166_1':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'countryCodeISO3166_1')
            value_ = self.gds_validate_string(value_, node, 'countryCodeISO3166_1')
            self.countryCodeISO3166_1 = value_
            self.countryCodeISO3166_1_nsprefix_ = child_.prefix
            # validate type stringISO3166Type
            self.validate_stringISO3166Type(self.countryCodeISO3166_1)
        elif nodeName_ == 'usedLangCodeISO639_1':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'usedLangCodeISO639_1')
            value_ = self.gds_validate_string(value_, node, 'usedLangCodeISO639_1')
            self.usedLangCodeISO639_1.append(value_)
            self.usedLangCodeISO639_1_nsprefix_ = child_.prefix
            # validate type stringISO639Type
            self.validate_stringISO639Type(self.usedLangCodeISO639_1[-1])
        elif nodeName_ == 'mandatoryLangCodeISO639_1':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'mandatoryLangCodeISO639_1')
            value_ = self.gds_validate_string(value_, node, 'mandatoryLangCodeISO639_1')
            self.mandatoryLangCodeISO639_1.append(value_)
            self.mandatoryLangCodeISO639_1_nsprefix_ = child_.prefix
            # validate type stringISO639Type
            self.validate_stringISO639Type(self.mandatoryLangCodeISO639_1[-1])
        elif nodeName_ == 'uniqueIdentifier':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'uniqueIdentifier')
            value_ = self.gds_validate_string(value_, node, 'uniqueIdentifier')
            self.uniqueIdentifier = value_
            self.uniqueIdentifier_nsprefix_ = child_.prefix
        elif nodeName_ == 'identifications':
            obj_ = identificationListType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.identifications = obj_
            obj_.original_tagname_ = 'identifications'
        elif nodeName_ == 'receiptDate':
            sval_ = child_.text
            dval_ = self.gds_parse_date(sval_)
            self.receiptDate = dval_
            self.receiptDate_nsprefix_ = child_.prefix
        elif nodeName_ == 'beginPerformanceDate':
            sval_ = child_.text
            dval_ = self.gds_parse_date(sval_)
            self.beginPerformanceDate = dval_
            self.beginPerformanceDate_nsprefix_ = child_.prefix
        elif nodeName_ == 'endPerformanceDate':
            sval_ = child_.text
            dval_ = self.gds_parse_date(sval_)
            self.endPerformanceDate = dval_
            self.endPerformanceDate_nsprefix_ = child_.prefix
        elif nodeName_ == 'previousReport':
            obj_ = hashType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.previousReport = obj_
            obj_.original_tagname_ = 'previousReport'
# end class coreDataType


class equipmentClassType(GeneratedsSuper):
    """Clear name(s) of the item(s) and identifier(s)"""
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, id=None, reference=None, classID=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = "dcc"
        self.id = _cast(None, id)
        self.id_nsprefix_ = None
        self.reference = reference
        self.reference_nsprefix_ = "dcc"
        self.classID = classID
        self.classID_nsprefix_ = "dcc"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, equipmentClassType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if equipmentClassType.subclass:
            return equipmentClassType.subclass(*args_, **kwargs_)
        else:
            return equipmentClassType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_reference(self):
        return self.reference
    def set_reference(self, reference):
        self.reference = reference
    def get_classID(self):
        return self.classID
    def set_classID(self, classID):
        self.classID = classID
    def get_id(self):
        return self.id
    def set_id(self, id):
        self.id = id
    def hasContent_(self):
        if (
            self.reference is not None or
            self.classID is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:dcc="https://ptb.de/dcc"', name_='equipmentClassType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('equipmentClassType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'equipmentClassType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='equipmentClassType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='equipmentClassType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='equipmentClassType'):
        if self.id is not None and 'id' not in already_processed:
            already_processed.add('id')
            outfile.write(' id=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.id), input_name='id')), ))
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:dcc="https://ptb.de/dcc"', name_='equipmentClassType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.reference is not None:
            namespaceprefix_ = self.reference_nsprefix_ + ':' if (UseCapturedNS_ and self.reference_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sreference>%s</%sreference>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.reference), input_name='reference')), namespaceprefix_ , eol_))
        if self.classID is not None:
            namespaceprefix_ = self.classID_nsprefix_ + ':' if (UseCapturedNS_ and self.classID_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sclassID>%s</%sclassID>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.classID), input_name='classID')), namespaceprefix_ , eol_))
    def to_etree(self, parent_element=None, name_='equipmentClassType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{https://ptb.de/dcc}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{https://ptb.de/dcc}' + name_, nsmap=nsmap_)
        if self.id is not None:
            element.set('id', self.gds_format_string(self.id))
        if self.reference is not None:
            reference_ = self.reference
            etree_.SubElement(element, '{https://ptb.de/dcc}reference').text = self.gds_format_string(reference_)
        if self.classID is not None:
            classID_ = self.classID
            etree_.SubElement(element, '{https://ptb.de/dcc}classID').text = self.gds_format_string(classID_)
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
        value = find_attr_value_('id', node)
        if value is not None and 'id' not in already_processed:
            already_processed.add('id')
            self.id = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'reference':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'reference')
            value_ = self.gds_validate_string(value_, node, 'reference')
            self.reference = value_
            self.reference_nsprefix_ = child_.prefix
        elif nodeName_ == 'classID':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'classID')
            value_ = self.gds_validate_string(value_, node, 'classID')
            self.classID = value_
            self.classID_nsprefix_ = child_.prefix
# end class equipmentClassType


class itemListType(GeneratedsSuper):
    """Clear description of the calibration items"""
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, name=None, equipmentClass=None, description=None, owner=None, identifications=None, item=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = "dcc"
        self.name = name
        self.name_nsprefix_ = "dcc"
        self.equipmentClass = equipmentClass
        self.equipmentClass_nsprefix_ = "dcc"
        self.description = description
        self.description_nsprefix_ = "dcc"
        self.owner = owner
        self.owner_nsprefix_ = "dcc"
        self.identifications = identifications
        self.identifications_nsprefix_ = "dcc"
        if item is None:
            self.item = []
        else:
            self.item = item
        self.item_nsprefix_ = "dcc"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, itemListType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if itemListType.subclass:
            return itemListType.subclass(*args_, **kwargs_)
        else:
            return itemListType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name
    def get_equipmentClass(self):
        return self.equipmentClass
    def set_equipmentClass(self, equipmentClass):
        self.equipmentClass = equipmentClass
    def get_description(self):
        return self.description
    def set_description(self, description):
        self.description = description
    def get_owner(self):
        return self.owner
    def set_owner(self, owner):
        self.owner = owner
    def get_identifications(self):
        return self.identifications
    def set_identifications(self, identifications):
        self.identifications = identifications
    def get_item(self):
        return self.item
    def set_item(self, item):
        self.item = item
    def add_item(self, value):
        self.item.append(value)
    def insert_item_at(self, index, value):
        self.item.insert(index, value)
    def replace_item_at(self, index, value):
        self.item[index] = value
    def hasContent_(self):
        if (
            self.name is not None or
            self.equipmentClass is not None or
            self.description is not None or
            self.owner is not None or
            self.identifications is not None or
            self.item
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:dcc="https://ptb.de/dcc"', name_='itemListType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('itemListType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'itemListType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='itemListType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='itemListType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='itemListType'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:dcc="https://ptb.de/dcc"', name_='itemListType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.name is not None:
            namespaceprefix_ = self.name_nsprefix_ + ':' if (UseCapturedNS_ and self.name_nsprefix_) else ''
            self.name.export(outfile, level, namespaceprefix_, namespacedef_='', name_='name', pretty_print=pretty_print)
        if self.equipmentClass is not None:
            namespaceprefix_ = self.equipmentClass_nsprefix_ + ':' if (UseCapturedNS_ and self.equipmentClass_nsprefix_) else ''
            self.equipmentClass.export(outfile, level, namespaceprefix_, namespacedef_='', name_='equipmentClass', pretty_print=pretty_print)
        if self.description is not None:
            namespaceprefix_ = self.description_nsprefix_ + ':' if (UseCapturedNS_ and self.description_nsprefix_) else ''
            self.description.export(outfile, level, namespaceprefix_, namespacedef_='', name_='description', pretty_print=pretty_print)
        if self.owner is not None:
            namespaceprefix_ = self.owner_nsprefix_ + ':' if (UseCapturedNS_ and self.owner_nsprefix_) else ''
            self.owner.export(outfile, level, namespaceprefix_, namespacedef_='', name_='owner', pretty_print=pretty_print)
        if self.identifications is not None:
            namespaceprefix_ = self.identifications_nsprefix_ + ':' if (UseCapturedNS_ and self.identifications_nsprefix_) else ''
            self.identifications.export(outfile, level, namespaceprefix_, namespacedef_='', name_='identifications', pretty_print=pretty_print)
        for item_ in self.item:
            namespaceprefix_ = self.item_nsprefix_ + ':' if (UseCapturedNS_ and self.item_nsprefix_) else ''
            item_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='item', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='itemListType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{https://ptb.de/dcc}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{https://ptb.de/dcc}' + name_, nsmap=nsmap_)
        if self.name is not None:
            name_ = self.name
            name_.to_etree(element, name_='name', mapping_=mapping_, nsmap_=nsmap_)
        if self.equipmentClass is not None:
            equipmentClass_ = self.equipmentClass
            equipmentClass_.to_etree(element, name_='equipmentClass', mapping_=mapping_, nsmap_=nsmap_)
        if self.description is not None:
            description_ = self.description
            description_.to_etree(element, name_='description', mapping_=mapping_, nsmap_=nsmap_)
        if self.owner is not None:
            owner_ = self.owner
            owner_.to_etree(element, name_='owner', mapping_=mapping_, nsmap_=nsmap_)
        if self.identifications is not None:
            identifications_ = self.identifications
            identifications_.to_etree(element, name_='identifications', mapping_=mapping_, nsmap_=nsmap_)
        for item_ in self.item:
            item_.to_etree(element, name_='item', mapping_=mapping_, nsmap_=nsmap_)
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
        if nodeName_ == 'name':
            obj_ = textType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.name = obj_
            obj_.original_tagname_ = 'name'
        elif nodeName_ == 'equipmentClass':
            obj_ = equipmentClassType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.equipmentClass = obj_
            obj_.original_tagname_ = 'equipmentClass'
        elif nodeName_ == 'description':
            obj_ = textType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.description = obj_
            obj_.original_tagname_ = 'description'
        elif nodeName_ == 'owner':
            obj_ = contactType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.owner = obj_
            obj_.original_tagname_ = 'owner'
        elif nodeName_ == 'identifications':
            obj_ = identificationListType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.identifications = obj_
            obj_.original_tagname_ = 'identifications'
        elif nodeName_ == 'item':
            obj_ = itemType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.item.append(obj_)
            obj_.original_tagname_ = 'item'
# end class itemListType


class itemType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, id=None, name=None, equipmentClass=None, description=None, descriptionData=None, manufacturer=None, model=None, identifications=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = "dcc"
        self.id = _cast(None, id)
        self.id_nsprefix_ = None
        self.name = name
        self.name_nsprefix_ = "dcc"
        self.equipmentClass = equipmentClass
        self.equipmentClass_nsprefix_ = "dcc"
        if description is None:
            self.description = []
        else:
            self.description = description
        self.description_nsprefix_ = "dcc"
        if descriptionData is None:
            self.descriptionData = []
        else:
            self.descriptionData = descriptionData
        self.descriptionData_nsprefix_ = "dcc"
        self.manufacturer = manufacturer
        self.manufacturer_nsprefix_ = "dcc"
        self.model = model
        self.model_nsprefix_ = "dcc"
        self.identifications = identifications
        self.identifications_nsprefix_ = "dcc"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, itemType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if itemType.subclass:
            return itemType.subclass(*args_, **kwargs_)
        else:
            return itemType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name
    def get_equipmentClass(self):
        return self.equipmentClass
    def set_equipmentClass(self, equipmentClass):
        self.equipmentClass = equipmentClass
    def get_description(self):
        return self.description
    def set_description(self, description):
        self.description = description
    def add_description(self, value):
        self.description.append(value)
    def insert_description_at(self, index, value):
        self.description.insert(index, value)
    def replace_description_at(self, index, value):
        self.description[index] = value
    def get_descriptionData(self):
        return self.descriptionData
    def set_descriptionData(self, descriptionData):
        self.descriptionData = descriptionData
    def add_descriptionData(self, value):
        self.descriptionData.append(value)
    def insert_descriptionData_at(self, index, value):
        self.descriptionData.insert(index, value)
    def replace_descriptionData_at(self, index, value):
        self.descriptionData[index] = value
    def get_manufacturer(self):
        return self.manufacturer
    def set_manufacturer(self, manufacturer):
        self.manufacturer = manufacturer
    def get_model(self):
        return self.model
    def set_model(self, model):
        self.model = model
    def get_identifications(self):
        return self.identifications
    def set_identifications(self, identifications):
        self.identifications = identifications
    def get_id(self):
        return self.id
    def set_id(self, id):
        self.id = id
    def hasContent_(self):
        if (
            self.name is not None or
            self.equipmentClass is not None or
            self.description or
            self.descriptionData or
            self.manufacturer is not None or
            self.model is not None or
            self.identifications is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:dcc="https://ptb.de/dcc"', name_='itemType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('itemType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'itemType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='itemType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='itemType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='itemType'):
        if self.id is not None and 'id' not in already_processed:
            already_processed.add('id')
            outfile.write(' id=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.id), input_name='id')), ))
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:dcc="https://ptb.de/dcc"', name_='itemType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.name is not None:
            namespaceprefix_ = self.name_nsprefix_ + ':' if (UseCapturedNS_ and self.name_nsprefix_) else ''
            self.name.export(outfile, level, namespaceprefix_, namespacedef_='', name_='name', pretty_print=pretty_print)
        if self.equipmentClass is not None:
            namespaceprefix_ = self.equipmentClass_nsprefix_ + ':' if (UseCapturedNS_ and self.equipmentClass_nsprefix_) else ''
            self.equipmentClass.export(outfile, level, namespaceprefix_, namespacedef_='', name_='equipmentClass', pretty_print=pretty_print)
        for description_ in self.description:
            namespaceprefix_ = self.description_nsprefix_ + ':' if (UseCapturedNS_ and self.description_nsprefix_) else ''
            description_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='description', pretty_print=pretty_print)
        for descriptionData_ in self.descriptionData:
            namespaceprefix_ = self.descriptionData_nsprefix_ + ':' if (UseCapturedNS_ and self.descriptionData_nsprefix_) else ''
            descriptionData_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='descriptionData', pretty_print=pretty_print)
        if self.manufacturer is not None:
            namespaceprefix_ = self.manufacturer_nsprefix_ + ':' if (UseCapturedNS_ and self.manufacturer_nsprefix_) else ''
            self.manufacturer.export(outfile, level, namespaceprefix_, namespacedef_='', name_='manufacturer', pretty_print=pretty_print)
        if self.model is not None:
            namespaceprefix_ = self.model_nsprefix_ + ':' if (UseCapturedNS_ and self.model_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%smodel>%s</%smodel>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.model), input_name='model')), namespaceprefix_ , eol_))
        if self.identifications is not None:
            namespaceprefix_ = self.identifications_nsprefix_ + ':' if (UseCapturedNS_ and self.identifications_nsprefix_) else ''
            self.identifications.export(outfile, level, namespaceprefix_, namespacedef_='', name_='identifications', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='itemType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{https://ptb.de/dcc}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{https://ptb.de/dcc}' + name_, nsmap=nsmap_)
        if self.id is not None:
            element.set('id', self.gds_format_string(self.id))
        if self.name is not None:
            name_ = self.name
            name_.to_etree(element, name_='name', mapping_=mapping_, nsmap_=nsmap_)
        if self.equipmentClass is not None:
            equipmentClass_ = self.equipmentClass
            equipmentClass_.to_etree(element, name_='equipmentClass', mapping_=mapping_, nsmap_=nsmap_)
        for description_ in self.description:
            description_.to_etree(element, name_='description', mapping_=mapping_, nsmap_=nsmap_)
        for descriptionData_ in self.descriptionData:
            descriptionData_.to_etree(element, name_='descriptionData', mapping_=mapping_, nsmap_=nsmap_)
        if self.manufacturer is not None:
            manufacturer_ = self.manufacturer
            manufacturer_.to_etree(element, name_='manufacturer', mapping_=mapping_, nsmap_=nsmap_)
        if self.model is not None:
            model_ = self.model
            etree_.SubElement(element, '{https://ptb.de/dcc}model').text = self.gds_format_string(model_)
        if self.identifications is not None:
            identifications_ = self.identifications
            identifications_.to_etree(element, name_='identifications', mapping_=mapping_, nsmap_=nsmap_)
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
        value = find_attr_value_('id', node)
        if value is not None and 'id' not in already_processed:
            already_processed.add('id')
            self.id = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'name':
            obj_ = textType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.name = obj_
            obj_.original_tagname_ = 'name'
        elif nodeName_ == 'equipmentClass':
            obj_ = equipmentClassType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.equipmentClass = obj_
            obj_.original_tagname_ = 'equipmentClass'
        elif nodeName_ == 'description':
            obj_ = textType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.description.append(obj_)
            obj_.original_tagname_ = 'description'
        elif nodeName_ == 'descriptionData':
            obj_ = byteDataType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.descriptionData.append(obj_)
            obj_.original_tagname_ = 'descriptionData'
        elif nodeName_ == 'manufacturer':
            obj_ = contactNotStrictType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.manufacturer = obj_
            obj_.original_tagname_ = 'manufacturer'
        elif nodeName_ == 'model':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'model')
            value_ = self.gds_validate_string(value_, node, 'model')
            self.model = value_
            self.model_nsprefix_ = child_.prefix
        elif nodeName_ == 'identifications':
            obj_ = identificationListType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.identifications = obj_
            obj_.original_tagname_ = 'identifications'
# end class itemType


class identificationListType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, identification=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = "dcc"
        if identification is None:
            self.identification = []
        else:
            self.identification = identification
        self.identification_nsprefix_ = "dcc"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, identificationListType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if identificationListType.subclass:
            return identificationListType.subclass(*args_, **kwargs_)
        else:
            return identificationListType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_identification(self):
        return self.identification
    def set_identification(self, identification):
        self.identification = identification
    def add_identification(self, value):
        self.identification.append(value)
    def insert_identification_at(self, index, value):
        self.identification.insert(index, value)
    def replace_identification_at(self, index, value):
        self.identification[index] = value
    def hasContent_(self):
        if (
            self.identification
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:dcc="https://ptb.de/dcc"', name_='identificationListType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('identificationListType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'identificationListType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='identificationListType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='identificationListType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='identificationListType'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:dcc="https://ptb.de/dcc"', name_='identificationListType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for identification_ in self.identification:
            namespaceprefix_ = self.identification_nsprefix_ + ':' if (UseCapturedNS_ and self.identification_nsprefix_) else ''
            identification_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='identification', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='identificationListType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{https://ptb.de/dcc}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{https://ptb.de/dcc}' + name_, nsmap=nsmap_)
        for identification_ in self.identification:
            identification_.to_etree(element, name_='identification', mapping_=mapping_, nsmap_=nsmap_)
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
        if nodeName_ == 'identification':
            obj_ = identificationType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.identification.append(obj_)
            obj_.original_tagname_ = 'identification'
# end class identificationListType


class identificationType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, id=None, refType=None, issuer=None, value=None, description=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = "dcc"
        self.id = _cast(None, id)
        self.id_nsprefix_ = None
        self.refType = _cast(None, refType)
        self.refType_nsprefix_ = None
        self.issuer = issuer
        self.validate_issuerType(self.issuer)
        self.issuer_nsprefix_ = "dcc"
        self.value = value
        self.value_nsprefix_ = "dcc"
        self.description = description
        self.description_nsprefix_ = "dcc"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, identificationType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if identificationType.subclass:
            return identificationType.subclass(*args_, **kwargs_)
        else:
            return identificationType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_issuer(self):
        return self.issuer
    def set_issuer(self, issuer):
        self.issuer = issuer
    def get_value(self):
        return self.value
    def set_value(self, value):
        self.value = value
    def get_description(self):
        return self.description
    def set_description(self, description):
        self.description = description
    def get_id(self):
        return self.id
    def set_id(self, id):
        self.id = id
    def get_refType(self):
        return self.refType
    def set_refType(self, refType):
        self.refType = refType
    def validate_issuerType(self, value):
        result = True
        # Validate type issuerType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['manufacturer', 'calibrationLaboratory', 'customer', 'owner', 'other']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on issuerType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_stringRefType(self, value):
        # Validate type dcc:stringRefType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_stringRefType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_stringRefType_patterns_, ))
    validate_stringRefType_patterns_ = [['^((/[A-Za-z][A-Za-z0-9]+)*)$']]
    def hasContent_(self):
        if (
            self.issuer is not None or
            self.value is not None or
            self.description is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:dcc="https://ptb.de/dcc"', name_='identificationType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('identificationType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'identificationType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='identificationType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='identificationType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='identificationType'):
        if self.id is not None and 'id' not in already_processed:
            already_processed.add('id')
            outfile.write(' id=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.id), input_name='id')), ))
        if self.refType is not None and 'refType' not in already_processed:
            already_processed.add('refType')
            outfile.write(' refType=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.refType), input_name='refType')), ))
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:dcc="https://ptb.de/dcc"', name_='identificationType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.issuer is not None:
            namespaceprefix_ = self.issuer_nsprefix_ + ':' if (UseCapturedNS_ and self.issuer_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sissuer>%s</%sissuer>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.issuer), input_name='issuer')), namespaceprefix_ , eol_))
        if self.value is not None:
            namespaceprefix_ = self.value_nsprefix_ + ':' if (UseCapturedNS_ and self.value_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%svalue>%s</%svalue>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.value), input_name='value')), namespaceprefix_ , eol_))
        if self.description is not None:
            namespaceprefix_ = self.description_nsprefix_ + ':' if (UseCapturedNS_ and self.description_nsprefix_) else ''
            self.description.export(outfile, level, namespaceprefix_, namespacedef_='', name_='description', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='identificationType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{https://ptb.de/dcc}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{https://ptb.de/dcc}' + name_, nsmap=nsmap_)
        if self.id is not None:
            element.set('id', self.gds_format_string(self.id))
        if self.refType is not None:
            element.set('refType', self.gds_format_string(self.refType))
        if self.issuer is not None:
            issuer_ = self.issuer
            etree_.SubElement(element, '{https://ptb.de/dcc}issuer').text = self.gds_format_string(issuer_)
        if self.value is not None:
            value_ = self.value
            etree_.SubElement(element, '{https://ptb.de/dcc}value').text = self.gds_format_string(value_)
        if self.description is not None:
            description_ = self.description
            description_.to_etree(element, name_='description', mapping_=mapping_, nsmap_=nsmap_)
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
        value = find_attr_value_('id', node)
        if value is not None and 'id' not in already_processed:
            already_processed.add('id')
            self.id = value
        value = find_attr_value_('refType', node)
        if value is not None and 'refType' not in already_processed:
            already_processed.add('refType')
            self.refType = value
            self.validate_stringRefType(self.refType)    # validate type stringRefType
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'issuer':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'issuer')
            value_ = self.gds_validate_string(value_, node, 'issuer')
            self.issuer = value_
            self.issuer_nsprefix_ = child_.prefix
            # validate type issuerType
            self.validate_issuerType(self.issuer)
        elif nodeName_ == 'value':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'value')
            value_ = self.gds_validate_string(value_, node, 'value')
            self.value = value_
            self.value_nsprefix_ = child_.prefix
        elif nodeName_ == 'description':
            obj_ = textType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.description = obj_
            obj_.original_tagname_ = 'description'
# end class identificationType


class calibrationLaboratoryType(GeneratedsSuper):
    """Information about the calibration laboratory"""
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, calibrationLaboratoryCode=None, contact=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = "dcc"
        self.calibrationLaboratoryCode = calibrationLaboratoryCode
        self.calibrationLaboratoryCode_nsprefix_ = "dcc"
        if contact is None:
            self.contact = []
        else:
            self.contact = contact
        self.contact_nsprefix_ = "dcc"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, calibrationLaboratoryType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if calibrationLaboratoryType.subclass:
            return calibrationLaboratoryType.subclass(*args_, **kwargs_)
        else:
            return calibrationLaboratoryType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_calibrationLaboratoryCode(self):
        return self.calibrationLaboratoryCode
    def set_calibrationLaboratoryCode(self, calibrationLaboratoryCode):
        self.calibrationLaboratoryCode = calibrationLaboratoryCode
    def get_contact(self):
        return self.contact
    def set_contact(self, contact):
        self.contact = contact
    def add_contact(self, value):
        self.contact.append(value)
    def insert_contact_at(self, index, value):
        self.contact.insert(index, value)
    def replace_contact_at(self, index, value):
        self.contact[index] = value
    def hasContent_(self):
        if (
            self.calibrationLaboratoryCode is not None or
            self.contact
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:dcc="https://ptb.de/dcc"', name_='calibrationLaboratoryType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('calibrationLaboratoryType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'calibrationLaboratoryType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='calibrationLaboratoryType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='calibrationLaboratoryType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='calibrationLaboratoryType'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:dcc="https://ptb.de/dcc"', name_='calibrationLaboratoryType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.calibrationLaboratoryCode is not None:
            namespaceprefix_ = self.calibrationLaboratoryCode_nsprefix_ + ':' if (UseCapturedNS_ and self.calibrationLaboratoryCode_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scalibrationLaboratoryCode>%s</%scalibrationLaboratoryCode>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.calibrationLaboratoryCode), input_name='calibrationLaboratoryCode')), namespaceprefix_ , eol_))
        for contact_ in self.contact:
            namespaceprefix_ = self.contact_nsprefix_ + ':' if (UseCapturedNS_ and self.contact_nsprefix_) else ''
            contact_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='contact', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='calibrationLaboratoryType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{https://ptb.de/dcc}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{https://ptb.de/dcc}' + name_, nsmap=nsmap_)
        if self.calibrationLaboratoryCode is not None:
            calibrationLaboratoryCode_ = self.calibrationLaboratoryCode
            etree_.SubElement(element, '{https://ptb.de/dcc}calibrationLaboratoryCode').text = self.gds_format_string(calibrationLaboratoryCode_)
        for contact_ in self.contact:
            contact_.to_etree(element, name_='contact', mapping_=mapping_, nsmap_=nsmap_)
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
        if nodeName_ == 'calibrationLaboratoryCode':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'calibrationLaboratoryCode')
            value_ = self.gds_validate_string(value_, node, 'calibrationLaboratoryCode')
            self.calibrationLaboratoryCode = value_
            self.calibrationLaboratoryCode_nsprefix_ = child_.prefix
        elif nodeName_ == 'contact':
            obj_ = contactType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.contact.append(obj_)
            obj_.original_tagname_ = 'contact'
# end class calibrationLaboratoryType


class respPersonListType(GeneratedsSuper):
    """List of responsible persons for the DCC"""
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, respPerson=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = "dcc"
        if respPerson is None:
            self.respPerson = []
        else:
            self.respPerson = respPerson
        self.respPerson_nsprefix_ = "dcc"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, respPersonListType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if respPersonListType.subclass:
            return respPersonListType.subclass(*args_, **kwargs_)
        else:
            return respPersonListType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_respPerson(self):
        return self.respPerson
    def set_respPerson(self, respPerson):
        self.respPerson = respPerson
    def add_respPerson(self, value):
        self.respPerson.append(value)
    def insert_respPerson_at(self, index, value):
        self.respPerson.insert(index, value)
    def replace_respPerson_at(self, index, value):
        self.respPerson[index] = value
    def hasContent_(self):
        if (
            self.respPerson
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:dcc="https://ptb.de/dcc"', name_='respPersonListType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('respPersonListType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'respPersonListType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='respPersonListType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='respPersonListType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='respPersonListType'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:dcc="https://ptb.de/dcc"', name_='respPersonListType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for respPerson_ in self.respPerson:
            namespaceprefix_ = self.respPerson_nsprefix_ + ':' if (UseCapturedNS_ and self.respPerson_nsprefix_) else ''
            respPerson_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='respPerson', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='respPersonListType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{https://ptb.de/dcc}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{https://ptb.de/dcc}' + name_, nsmap=nsmap_)
        for respPerson_ in self.respPerson:
            respPerson_.to_etree(element, name_='respPerson', mapping_=mapping_, nsmap_=nsmap_)
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
        if nodeName_ == 'respPerson':
            obj_ = respPersonType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.respPerson.append(obj_)
            obj_.original_tagname_ = 'respPerson'
# end class respPersonListType


class respPersonType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, id=None, person=None, description=None, mainSigner=None, cryptElectronicSeal=None, cryptElectronicSignature=None, cryptElectronicTimeStamp=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = "dcc"
        self.id = _cast(None, id)
        self.id_nsprefix_ = None
        self.person = person
        self.person_nsprefix_ = "dcc"
        self.description = description
        self.description_nsprefix_ = "dcc"
        self.mainSigner = mainSigner
        self.mainSigner_nsprefix_ = "dcc"
        self.cryptElectronicSeal = cryptElectronicSeal
        self.cryptElectronicSeal_nsprefix_ = "dcc"
        self.cryptElectronicSignature = cryptElectronicSignature
        self.cryptElectronicSignature_nsprefix_ = "dcc"
        self.cryptElectronicTimeStamp = cryptElectronicTimeStamp
        self.cryptElectronicTimeStamp_nsprefix_ = "dcc"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, respPersonType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if respPersonType.subclass:
            return respPersonType.subclass(*args_, **kwargs_)
        else:
            return respPersonType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_person(self):
        return self.person
    def set_person(self, person):
        self.person = person
    def get_description(self):
        return self.description
    def set_description(self, description):
        self.description = description
    def get_mainSigner(self):
        return self.mainSigner
    def set_mainSigner(self, mainSigner):
        self.mainSigner = mainSigner
    def get_cryptElectronicSeal(self):
        return self.cryptElectronicSeal
    def set_cryptElectronicSeal(self, cryptElectronicSeal):
        self.cryptElectronicSeal = cryptElectronicSeal
    def get_cryptElectronicSignature(self):
        return self.cryptElectronicSignature
    def set_cryptElectronicSignature(self, cryptElectronicSignature):
        self.cryptElectronicSignature = cryptElectronicSignature
    def get_cryptElectronicTimeStamp(self):
        return self.cryptElectronicTimeStamp
    def set_cryptElectronicTimeStamp(self, cryptElectronicTimeStamp):
        self.cryptElectronicTimeStamp = cryptElectronicTimeStamp
    def get_id(self):
        return self.id
    def set_id(self, id):
        self.id = id
    def hasContent_(self):
        if (
            self.person is not None or
            self.description is not None or
            self.mainSigner is not None or
            self.cryptElectronicSeal is not None or
            self.cryptElectronicSignature is not None or
            self.cryptElectronicTimeStamp is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:dcc="https://ptb.de/dcc"', name_='respPersonType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('respPersonType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'respPersonType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='respPersonType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='respPersonType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='respPersonType'):
        if self.id is not None and 'id' not in already_processed:
            already_processed.add('id')
            outfile.write(' id=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.id), input_name='id')), ))
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:dcc="https://ptb.de/dcc"', name_='respPersonType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.person is not None:
            namespaceprefix_ = self.person_nsprefix_ + ':' if (UseCapturedNS_ and self.person_nsprefix_) else ''
            self.person.export(outfile, level, namespaceprefix_, namespacedef_='', name_='person', pretty_print=pretty_print)
        if self.description is not None:
            namespaceprefix_ = self.description_nsprefix_ + ':' if (UseCapturedNS_ and self.description_nsprefix_) else ''
            self.description.export(outfile, level, namespaceprefix_, namespacedef_='', name_='description', pretty_print=pretty_print)
        if self.mainSigner is not None:
            namespaceprefix_ = self.mainSigner_nsprefix_ + ':' if (UseCapturedNS_ and self.mainSigner_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%smainSigner>%s</%smainSigner>%s' % (namespaceprefix_ , self.gds_format_boolean(self.mainSigner, input_name='mainSigner'), namespaceprefix_ , eol_))
        if self.cryptElectronicSeal is not None:
            namespaceprefix_ = self.cryptElectronicSeal_nsprefix_ + ':' if (UseCapturedNS_ and self.cryptElectronicSeal_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scryptElectronicSeal>%s</%scryptElectronicSeal>%s' % (namespaceprefix_ , self.gds_format_boolean(self.cryptElectronicSeal, input_name='cryptElectronicSeal'), namespaceprefix_ , eol_))
        if self.cryptElectronicSignature is not None:
            namespaceprefix_ = self.cryptElectronicSignature_nsprefix_ + ':' if (UseCapturedNS_ and self.cryptElectronicSignature_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scryptElectronicSignature>%s</%scryptElectronicSignature>%s' % (namespaceprefix_ , self.gds_format_boolean(self.cryptElectronicSignature, input_name='cryptElectronicSignature'), namespaceprefix_ , eol_))
        if self.cryptElectronicTimeStamp is not None:
            namespaceprefix_ = self.cryptElectronicTimeStamp_nsprefix_ + ':' if (UseCapturedNS_ and self.cryptElectronicTimeStamp_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scryptElectronicTimeStamp>%s</%scryptElectronicTimeStamp>%s' % (namespaceprefix_ , self.gds_format_boolean(self.cryptElectronicTimeStamp, input_name='cryptElectronicTimeStamp'), namespaceprefix_ , eol_))
    def to_etree(self, parent_element=None, name_='respPersonType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{https://ptb.de/dcc}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{https://ptb.de/dcc}' + name_, nsmap=nsmap_)
        if self.id is not None:
            element.set('id', self.gds_format_string(self.id))
        if self.person is not None:
            person_ = self.person
            person_.to_etree(element, name_='person', mapping_=mapping_, nsmap_=nsmap_)
        if self.description is not None:
            description_ = self.description
            description_.to_etree(element, name_='description', mapping_=mapping_, nsmap_=nsmap_)
        if self.mainSigner is not None:
            mainSigner_ = self.mainSigner
            etree_.SubElement(element, '{https://ptb.de/dcc}mainSigner').text = self.gds_format_boolean(mainSigner_)
        if self.cryptElectronicSeal is not None:
            cryptElectronicSeal_ = self.cryptElectronicSeal
            etree_.SubElement(element, '{https://ptb.de/dcc}cryptElectronicSeal').text = self.gds_format_boolean(cryptElectronicSeal_)
        if self.cryptElectronicSignature is not None:
            cryptElectronicSignature_ = self.cryptElectronicSignature
            etree_.SubElement(element, '{https://ptb.de/dcc}cryptElectronicSignature').text = self.gds_format_boolean(cryptElectronicSignature_)
        if self.cryptElectronicTimeStamp is not None:
            cryptElectronicTimeStamp_ = self.cryptElectronicTimeStamp
            etree_.SubElement(element, '{https://ptb.de/dcc}cryptElectronicTimeStamp').text = self.gds_format_boolean(cryptElectronicTimeStamp_)
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
        value = find_attr_value_('id', node)
        if value is not None and 'id' not in already_processed:
            already_processed.add('id')
            self.id = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'person':
            obj_ = contactNotStrictType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.person = obj_
            obj_.original_tagname_ = 'person'
        elif nodeName_ == 'description':
            obj_ = textType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.description = obj_
            obj_.original_tagname_ = 'description'
        elif nodeName_ == 'mainSigner':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'mainSigner')
            ival_ = self.gds_validate_boolean(ival_, node, 'mainSigner')
            self.mainSigner = ival_
            self.mainSigner_nsprefix_ = child_.prefix
        elif nodeName_ == 'cryptElectronicSeal':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'cryptElectronicSeal')
            ival_ = self.gds_validate_boolean(ival_, node, 'cryptElectronicSeal')
            self.cryptElectronicSeal = ival_
            self.cryptElectronicSeal_nsprefix_ = child_.prefix
        elif nodeName_ == 'cryptElectronicSignature':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'cryptElectronicSignature')
            ival_ = self.gds_validate_boolean(ival_, node, 'cryptElectronicSignature')
            self.cryptElectronicSignature = ival_
            self.cryptElectronicSignature_nsprefix_ = child_.prefix
        elif nodeName_ == 'cryptElectronicTimeStamp':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'cryptElectronicTimeStamp')
            ival_ = self.gds_validate_boolean(ival_, node, 'cryptElectronicTimeStamp')
            self.cryptElectronicTimeStamp = ival_
            self.cryptElectronicTimeStamp_nsprefix_ = child_.prefix
# end class respPersonType


class statementListType(GeneratedsSuper):
    """Elements for the statements"""
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, statement=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = "dcc"
        if statement is None:
            self.statement = []
        else:
            self.statement = statement
        self.statement_nsprefix_ = "dcc"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, statementListType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if statementListType.subclass:
            return statementListType.subclass(*args_, **kwargs_)
        else:
            return statementListType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_statement(self):
        return self.statement
    def set_statement(self, statement):
        self.statement = statement
    def add_statement(self, value):
        self.statement.append(value)
    def insert_statement_at(self, index, value):
        self.statement.insert(index, value)
    def replace_statement_at(self, index, value):
        self.statement[index] = value
    def hasContent_(self):
        if (
            self.statement
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:dcc="https://ptb.de/dcc"', name_='statementListType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('statementListType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'statementListType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='statementListType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='statementListType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='statementListType'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:dcc="https://ptb.de/dcc"', name_='statementListType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for statement_ in self.statement:
            namespaceprefix_ = self.statement_nsprefix_ + ':' if (UseCapturedNS_ and self.statement_nsprefix_) else ''
            statement_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='statement', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='statementListType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{https://ptb.de/dcc}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{https://ptb.de/dcc}' + name_, nsmap=nsmap_)
        for statement_ in self.statement:
            statement_.to_etree(element, name_='statement', mapping_=mapping_, nsmap_=nsmap_)
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
        if nodeName_ == 'statement':
            obj_ = statementMetaDataType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.statement.append(obj_)
            obj_.original_tagname_ = 'statement'
# end class statementListType


class measurementResultListType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, measurementResult=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = "dcc"
        if measurementResult is None:
            self.measurementResult = []
        else:
            self.measurementResult = measurementResult
        self.measurementResult_nsprefix_ = "dcc"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, measurementResultListType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if measurementResultListType.subclass:
            return measurementResultListType.subclass(*args_, **kwargs_)
        else:
            return measurementResultListType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_measurementResult(self):
        return self.measurementResult
    def set_measurementResult(self, measurementResult):
        self.measurementResult = measurementResult
    def add_measurementResult(self, value):
        self.measurementResult.append(value)
    def insert_measurementResult_at(self, index, value):
        self.measurementResult.insert(index, value)
    def replace_measurementResult_at(self, index, value):
        self.measurementResult[index] = value
    def hasContent_(self):
        if (
            self.measurementResult
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:dcc="https://ptb.de/dcc"', name_='measurementResultListType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('measurementResultListType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'measurementResultListType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='measurementResultListType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='measurementResultListType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='measurementResultListType'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:dcc="https://ptb.de/dcc"', name_='measurementResultListType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for measurementResult_ in self.measurementResult:
            namespaceprefix_ = self.measurementResult_nsprefix_ + ':' if (UseCapturedNS_ and self.measurementResult_nsprefix_) else ''
            measurementResult_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='measurementResult', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='measurementResultListType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{https://ptb.de/dcc}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{https://ptb.de/dcc}' + name_, nsmap=nsmap_)
        for measurementResult_ in self.measurementResult:
            measurementResult_.to_etree(element, name_='measurementResult', mapping_=mapping_, nsmap_=nsmap_)
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
        if nodeName_ == 'measurementResult':
            obj_ = measurementResultType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.measurementResult.append(obj_)
            obj_.original_tagname_ = 'measurementResult'
# end class measurementResultListType


class measurementResultType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, usedMethods=None, usedSoftware=None, measuringEquipments=None, influenceConditions=None, results=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = "dcc"
        self.usedMethods = usedMethods
        self.usedMethods_nsprefix_ = "dcc"
        self.usedSoftware = usedSoftware
        self.usedSoftware_nsprefix_ = "dcc"
        self.measuringEquipments = measuringEquipments
        self.measuringEquipments_nsprefix_ = "dcc"
        self.influenceConditions = influenceConditions
        self.influenceConditions_nsprefix_ = "dcc"
        self.results = results
        self.results_nsprefix_ = "dcc"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, measurementResultType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if measurementResultType.subclass:
            return measurementResultType.subclass(*args_, **kwargs_)
        else:
            return measurementResultType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_usedMethods(self):
        return self.usedMethods
    def set_usedMethods(self, usedMethods):
        self.usedMethods = usedMethods
    def get_usedSoftware(self):
        return self.usedSoftware
    def set_usedSoftware(self, usedSoftware):
        self.usedSoftware = usedSoftware
    def get_measuringEquipments(self):
        return self.measuringEquipments
    def set_measuringEquipments(self, measuringEquipments):
        self.measuringEquipments = measuringEquipments
    def get_influenceConditions(self):
        return self.influenceConditions
    def set_influenceConditions(self, influenceConditions):
        self.influenceConditions = influenceConditions
    def get_results(self):
        return self.results
    def set_results(self, results):
        self.results = results
    def hasContent_(self):
        if (
            self.usedMethods is not None or
            self.usedSoftware is not None or
            self.measuringEquipments is not None or
            self.influenceConditions is not None or
            self.results is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:dcc="https://ptb.de/dcc"', name_='measurementResultType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('measurementResultType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'measurementResultType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='measurementResultType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='measurementResultType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='measurementResultType'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:dcc="https://ptb.de/dcc"', name_='measurementResultType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.usedMethods is not None:
            namespaceprefix_ = self.usedMethods_nsprefix_ + ':' if (UseCapturedNS_ and self.usedMethods_nsprefix_) else ''
            self.usedMethods.export(outfile, level, namespaceprefix_, namespacedef_='', name_='usedMethods', pretty_print=pretty_print)
        if self.usedSoftware is not None:
            namespaceprefix_ = self.usedSoftware_nsprefix_ + ':' if (UseCapturedNS_ and self.usedSoftware_nsprefix_) else ''
            self.usedSoftware.export(outfile, level, namespaceprefix_, namespacedef_='', name_='usedSoftware', pretty_print=pretty_print)
        if self.measuringEquipments is not None:
            namespaceprefix_ = self.measuringEquipments_nsprefix_ + ':' if (UseCapturedNS_ and self.measuringEquipments_nsprefix_) else ''
            self.measuringEquipments.export(outfile, level, namespaceprefix_, namespacedef_='', name_='measuringEquipments', pretty_print=pretty_print)
        if self.influenceConditions is not None:
            namespaceprefix_ = self.influenceConditions_nsprefix_ + ':' if (UseCapturedNS_ and self.influenceConditions_nsprefix_) else ''
            self.influenceConditions.export(outfile, level, namespaceprefix_, namespacedef_='', name_='influenceConditions', pretty_print=pretty_print)
        if self.results is not None:
            namespaceprefix_ = self.results_nsprefix_ + ':' if (UseCapturedNS_ and self.results_nsprefix_) else ''
            self.results.export(outfile, level, namespaceprefix_, namespacedef_='', name_='results', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='measurementResultType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{https://ptb.de/dcc}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{https://ptb.de/dcc}' + name_, nsmap=nsmap_)
        if self.usedMethods is not None:
            usedMethods_ = self.usedMethods
            usedMethods_.to_etree(element, name_='usedMethods', mapping_=mapping_, nsmap_=nsmap_)
        if self.usedSoftware is not None:
            usedSoftware_ = self.usedSoftware
            usedSoftware_.to_etree(element, name_='usedSoftware', mapping_=mapping_, nsmap_=nsmap_)
        if self.measuringEquipments is not None:
            measuringEquipments_ = self.measuringEquipments
            measuringEquipments_.to_etree(element, name_='measuringEquipments', mapping_=mapping_, nsmap_=nsmap_)
        if self.influenceConditions is not None:
            influenceConditions_ = self.influenceConditions
            influenceConditions_.to_etree(element, name_='influenceConditions', mapping_=mapping_, nsmap_=nsmap_)
        if self.results is not None:
            results_ = self.results
            results_.to_etree(element, name_='results', mapping_=mapping_, nsmap_=nsmap_)
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
        if nodeName_ == 'usedMethods':
            obj_ = usedMethodListType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.usedMethods = obj_
            obj_.original_tagname_ = 'usedMethods'
        elif nodeName_ == 'usedSoftware':
            obj_ = softwareListType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.usedSoftware = obj_
            obj_.original_tagname_ = 'usedSoftware'
        elif nodeName_ == 'measuringEquipments':
            obj_ = measuringEquipmentListType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.measuringEquipments = obj_
            obj_.original_tagname_ = 'measuringEquipments'
        elif nodeName_ == 'influenceConditions':
            obj_ = influenceConditionListType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.influenceConditions = obj_
            obj_.original_tagname_ = 'influenceConditions'
        elif nodeName_ == 'results':
            obj_ = resultListType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.results = obj_
            obj_.original_tagname_ = 'results'
# end class measurementResultType


class usedMethodListType(GeneratedsSuper):
    """Clear description of the used method"""
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, usedMethod=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = "dcc"
        if usedMethod is None:
            self.usedMethod = []
        else:
            self.usedMethod = usedMethod
        self.usedMethod_nsprefix_ = "dcc"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, usedMethodListType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if usedMethodListType.subclass:
            return usedMethodListType.subclass(*args_, **kwargs_)
        else:
            return usedMethodListType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_usedMethod(self):
        return self.usedMethod
    def set_usedMethod(self, usedMethod):
        self.usedMethod = usedMethod
    def add_usedMethod(self, value):
        self.usedMethod.append(value)
    def insert_usedMethod_at(self, index, value):
        self.usedMethod.insert(index, value)
    def replace_usedMethod_at(self, index, value):
        self.usedMethod[index] = value
    def hasContent_(self):
        if (
            self.usedMethod
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:dcc="https://ptb.de/dcc"', name_='usedMethodListType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('usedMethodListType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'usedMethodListType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='usedMethodListType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='usedMethodListType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='usedMethodListType'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:dcc="https://ptb.de/dcc"', name_='usedMethodListType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for usedMethod_ in self.usedMethod:
            namespaceprefix_ = self.usedMethod_nsprefix_ + ':' if (UseCapturedNS_ and self.usedMethod_nsprefix_) else ''
            usedMethod_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='usedMethod', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='usedMethodListType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{https://ptb.de/dcc}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{https://ptb.de/dcc}' + name_, nsmap=nsmap_)
        for usedMethod_ in self.usedMethod:
            usedMethod_.to_etree(element, name_='usedMethod', mapping_=mapping_, nsmap_=nsmap_)
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
        if nodeName_ == 'usedMethod':
            obj_ = usedMethodType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.usedMethod.append(obj_)
            obj_.original_tagname_ = 'usedMethod'
# end class usedMethodListType


class usedMethodType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, id=None, name=None, description=None, norm=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = "dcc"
        self.id = _cast(None, id)
        self.id_nsprefix_ = None
        self.name = name
        self.name_nsprefix_ = "dcc"
        if description is None:
            self.description = []
        else:
            self.description = description
        self.description_nsprefix_ = "dcc"
        if norm is None:
            self.norm = []
        else:
            self.norm = norm
        self.norm_nsprefix_ = "dcc"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, usedMethodType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if usedMethodType.subclass:
            return usedMethodType.subclass(*args_, **kwargs_)
        else:
            return usedMethodType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name
    def get_description(self):
        return self.description
    def set_description(self, description):
        self.description = description
    def add_description(self, value):
        self.description.append(value)
    def insert_description_at(self, index, value):
        self.description.insert(index, value)
    def replace_description_at(self, index, value):
        self.description[index] = value
    def get_norm(self):
        return self.norm
    def set_norm(self, norm):
        self.norm = norm
    def add_norm(self, value):
        self.norm.append(value)
    def insert_norm_at(self, index, value):
        self.norm.insert(index, value)
    def replace_norm_at(self, index, value):
        self.norm[index] = value
    def get_id(self):
        return self.id
    def set_id(self, id):
        self.id = id
    def hasContent_(self):
        if (
            self.name is not None or
            self.description or
            self.norm
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:dcc="https://ptb.de/dcc"', name_='usedMethodType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('usedMethodType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'usedMethodType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='usedMethodType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='usedMethodType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='usedMethodType'):
        if self.id is not None and 'id' not in already_processed:
            already_processed.add('id')
            outfile.write(' id=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.id), input_name='id')), ))
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:dcc="https://ptb.de/dcc"', name_='usedMethodType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.name is not None:
            namespaceprefix_ = self.name_nsprefix_ + ':' if (UseCapturedNS_ and self.name_nsprefix_) else ''
            self.name.export(outfile, level, namespaceprefix_, namespacedef_='', name_='name', pretty_print=pretty_print)
        for description_ in self.description:
            namespaceprefix_ = self.description_nsprefix_ + ':' if (UseCapturedNS_ and self.description_nsprefix_) else ''
            description_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='description', pretty_print=pretty_print)
        for norm_ in self.norm:
            namespaceprefix_ = self.norm_nsprefix_ + ':' if (UseCapturedNS_ and self.norm_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%snorm>%s</%snorm>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(norm_), input_name='norm')), namespaceprefix_ , eol_))
    def to_etree(self, parent_element=None, name_='usedMethodType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{https://ptb.de/dcc}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{https://ptb.de/dcc}' + name_, nsmap=nsmap_)
        if self.id is not None:
            element.set('id', self.gds_format_string(self.id))
        if self.name is not None:
            name_ = self.name
            name_.to_etree(element, name_='name', mapping_=mapping_, nsmap_=nsmap_)
        for description_ in self.description:
            description_.to_etree(element, name_='description', mapping_=mapping_, nsmap_=nsmap_)
        for norm_ in self.norm:
            etree_.SubElement(element, '{https://ptb.de/dcc}norm').text = self.gds_format_string(norm_)
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
        value = find_attr_value_('id', node)
        if value is not None and 'id' not in already_processed:
            already_processed.add('id')
            self.id = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'name':
            obj_ = textType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.name = obj_
            obj_.original_tagname_ = 'name'
        elif nodeName_ == 'description':
            obj_ = textType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.description.append(obj_)
            obj_.original_tagname_ = 'description'
        elif nodeName_ == 'norm':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'norm')
            value_ = self.gds_validate_string(value_, node, 'norm')
            self.norm.append(value_)
            self.norm_nsprefix_ = child_.prefix
# end class usedMethodType


class influenceConditionListType(GeneratedsSuper):
    """Elements for the conditions (e.g. environmental) under which the
    calibrations were
    made that have an influence on the measurement results"""
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, influenceCondition=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = "dcc"
        if influenceCondition is None:
            self.influenceCondition = []
        else:
            self.influenceCondition = influenceCondition
        self.influenceCondition_nsprefix_ = "dcc"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, influenceConditionListType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if influenceConditionListType.subclass:
            return influenceConditionListType.subclass(*args_, **kwargs_)
        else:
            return influenceConditionListType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_influenceCondition(self):
        return self.influenceCondition
    def set_influenceCondition(self, influenceCondition):
        self.influenceCondition = influenceCondition
    def add_influenceCondition(self, value):
        self.influenceCondition.append(value)
    def insert_influenceCondition_at(self, index, value):
        self.influenceCondition.insert(index, value)
    def replace_influenceCondition_at(self, index, value):
        self.influenceCondition[index] = value
    def hasContent_(self):
        if (
            self.influenceCondition
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:dcc="https://ptb.de/dcc"', name_='influenceConditionListType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('influenceConditionListType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'influenceConditionListType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='influenceConditionListType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='influenceConditionListType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='influenceConditionListType'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:dcc="https://ptb.de/dcc"', name_='influenceConditionListType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for influenceCondition_ in self.influenceCondition:
            namespaceprefix_ = self.influenceCondition_nsprefix_ + ':' if (UseCapturedNS_ and self.influenceCondition_nsprefix_) else ''
            influenceCondition_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='influenceCondition', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='influenceConditionListType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{https://ptb.de/dcc}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{https://ptb.de/dcc}' + name_, nsmap=nsmap_)
        for influenceCondition_ in self.influenceCondition:
            influenceCondition_.to_etree(element, name_='influenceCondition', mapping_=mapping_, nsmap_=nsmap_)
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
        if nodeName_ == 'influenceCondition':
            obj_ = conditionType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.influenceCondition.append(obj_)
            obj_.original_tagname_ = 'influenceCondition'
# end class influenceConditionListType


class calibrationLocationListType(GeneratedsSuper):
    """Locations, where the calibration was done"""
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, calibrationLocation=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = "dcc"
        if calibrationLocation is None:
            self.calibrationLocation = []
        else:
            self.calibrationLocation = calibrationLocation
        self.calibrationLocation_nsprefix_ = "dcc"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, calibrationLocationListType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if calibrationLocationListType.subclass:
            return calibrationLocationListType.subclass(*args_, **kwargs_)
        else:
            return calibrationLocationListType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_calibrationLocation(self):
        return self.calibrationLocation
    def set_calibrationLocation(self, calibrationLocation):
        self.calibrationLocation = calibrationLocation
    def add_calibrationLocation(self, value):
        self.calibrationLocation.append(value)
    def insert_calibrationLocation_at(self, index, value):
        self.calibrationLocation.insert(index, value)
    def replace_calibrationLocation_at(self, index, value):
        self.calibrationLocation[index] = value
    def hasContent_(self):
        if (
            self.calibrationLocation
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:dcc="https://ptb.de/dcc"', name_='calibrationLocationListType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('calibrationLocationListType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'calibrationLocationListType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='calibrationLocationListType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='calibrationLocationListType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='calibrationLocationListType'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:dcc="https://ptb.de/dcc"', name_='calibrationLocationListType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for calibrationLocation_ in self.calibrationLocation:
            namespaceprefix_ = self.calibrationLocation_nsprefix_ + ':' if (UseCapturedNS_ and self.calibrationLocation_nsprefix_) else ''
            calibrationLocation_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='calibrationLocation', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='calibrationLocationListType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{https://ptb.de/dcc}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{https://ptb.de/dcc}' + name_, nsmap=nsmap_)
        for calibrationLocation_ in self.calibrationLocation:
            calibrationLocation_.to_etree(element, name_='calibrationLocation', mapping_=mapping_, nsmap_=nsmap_)
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
        if nodeName_ == 'calibrationLocation':
            obj_ = calibrationLocationType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.calibrationLocation.append(obj_)
            obj_.original_tagname_ = 'calibrationLocation'
# end class calibrationLocationListType


class calibrationLocationType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, id=None, calibrationLocationSite=None, beginLocationCalDateTime=None, endLocationCalDateTime=None, location=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = "dcc"
        self.id = _cast(None, id)
        self.id_nsprefix_ = None
        self.calibrationLocationSite = calibrationLocationSite
        self.calibrationLocationSite_nsprefix_ = "dcc"
        if isinstance(beginLocationCalDateTime, BaseStrType_):
            initvalue_ = datetime_.datetime.strptime(beginLocationCalDateTime, '%Y-%m-%dT%H:%M:%S')
        else:
            initvalue_ = beginLocationCalDateTime
        self.beginLocationCalDateTime = initvalue_
        self.beginLocationCalDateTime_nsprefix_ = "dcc"
        if isinstance(endLocationCalDateTime, BaseStrType_):
            initvalue_ = datetime_.datetime.strptime(endLocationCalDateTime, '%Y-%m-%dT%H:%M:%S')
        else:
            initvalue_ = endLocationCalDateTime
        self.endLocationCalDateTime = initvalue_
        self.endLocationCalDateTime_nsprefix_ = "dcc"
        self.location = location
        self.location_nsprefix_ = "dcc"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, calibrationLocationType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if calibrationLocationType.subclass:
            return calibrationLocationType.subclass(*args_, **kwargs_)
        else:
            return calibrationLocationType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_calibrationLocationSite(self):
        return self.calibrationLocationSite
    def set_calibrationLocationSite(self, calibrationLocationSite):
        self.calibrationLocationSite = calibrationLocationSite
    def get_beginLocationCalDateTime(self):
        return self.beginLocationCalDateTime
    def set_beginLocationCalDateTime(self, beginLocationCalDateTime):
        self.beginLocationCalDateTime = beginLocationCalDateTime
    def get_endLocationCalDateTime(self):
        return self.endLocationCalDateTime
    def set_endLocationCalDateTime(self, endLocationCalDateTime):
        self.endLocationCalDateTime = endLocationCalDateTime
    def get_location(self):
        return self.location
    def set_location(self, location):
        self.location = location
    def get_id(self):
        return self.id
    def set_id(self, id):
        self.id = id
    def hasContent_(self):
        if (
            self.calibrationLocationSite is not None or
            self.beginLocationCalDateTime is not None or
            self.endLocationCalDateTime is not None or
            self.location is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:dcc="https://ptb.de/dcc"', name_='calibrationLocationType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('calibrationLocationType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'calibrationLocationType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='calibrationLocationType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='calibrationLocationType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='calibrationLocationType'):
        if self.id is not None and 'id' not in already_processed:
            already_processed.add('id')
            outfile.write(' id=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.id), input_name='id')), ))
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:dcc="https://ptb.de/dcc"', name_='calibrationLocationType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.calibrationLocationSite is not None:
            namespaceprefix_ = self.calibrationLocationSite_nsprefix_ + ':' if (UseCapturedNS_ and self.calibrationLocationSite_nsprefix_) else ''
            self.calibrationLocationSite.export(outfile, level, namespaceprefix_, namespacedef_='', name_='calibrationLocationSite', pretty_print=pretty_print)
        if self.beginLocationCalDateTime is not None:
            namespaceprefix_ = self.beginLocationCalDateTime_nsprefix_ + ':' if (UseCapturedNS_ and self.beginLocationCalDateTime_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sbeginLocationCalDateTime>%s</%sbeginLocationCalDateTime>%s' % (namespaceprefix_ , self.gds_format_datetime(self.beginLocationCalDateTime, input_name='beginLocationCalDateTime'), namespaceprefix_ , eol_))
        if self.endLocationCalDateTime is not None:
            namespaceprefix_ = self.endLocationCalDateTime_nsprefix_ + ':' if (UseCapturedNS_ and self.endLocationCalDateTime_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sendLocationCalDateTime>%s</%sendLocationCalDateTime>%s' % (namespaceprefix_ , self.gds_format_datetime(self.endLocationCalDateTime, input_name='endLocationCalDateTime'), namespaceprefix_ , eol_))
        if self.location is not None:
            namespaceprefix_ = self.location_nsprefix_ + ':' if (UseCapturedNS_ and self.location_nsprefix_) else ''
            self.location.export(outfile, level, namespaceprefix_, namespacedef_='', name_='location', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='calibrationLocationType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{https://ptb.de/dcc}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{https://ptb.de/dcc}' + name_, nsmap=nsmap_)
        if self.id is not None:
            element.set('id', self.gds_format_string(self.id))
        if self.calibrationLocationSite is not None:
            calibrationLocationSite_ = self.calibrationLocationSite
            calibrationLocationSite_.to_etree(element, name_='calibrationLocationSite', mapping_=mapping_, nsmap_=nsmap_)
        if self.beginLocationCalDateTime is not None:
            beginLocationCalDateTime_ = self.beginLocationCalDateTime
            etree_.SubElement(element, '{https://ptb.de/dcc}beginLocationCalDateTime').text = self.gds_format_datetime(beginLocationCalDateTime_)
        if self.endLocationCalDateTime is not None:
            endLocationCalDateTime_ = self.endLocationCalDateTime
            etree_.SubElement(element, '{https://ptb.de/dcc}endLocationCalDateTime').text = self.gds_format_datetime(endLocationCalDateTime_)
        if self.location is not None:
            location_ = self.location
            location_.to_etree(element, name_='location', mapping_=mapping_, nsmap_=nsmap_)
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
        value = find_attr_value_('id', node)
        if value is not None and 'id' not in already_processed:
            already_processed.add('id')
            self.id = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'calibrationLocationSite':
            obj_ = textType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.calibrationLocationSite = obj_
            obj_.original_tagname_ = 'calibrationLocationSite'
        elif nodeName_ == 'beginLocationCalDateTime':
            sval_ = child_.text
            dval_ = self.gds_parse_datetime(sval_)
            self.beginLocationCalDateTime = dval_
            self.beginLocationCalDateTime_nsprefix_ = child_.prefix
        elif nodeName_ == 'endLocationCalDateTime':
            sval_ = child_.text
            dval_ = self.gds_parse_datetime(sval_)
            self.endLocationCalDateTime = dval_
            self.endLocationCalDateTime_nsprefix_ = child_.prefix
        elif nodeName_ == 'location':
            obj_ = locationType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.location = obj_
            obj_.original_tagname_ = 'location'
# end class calibrationLocationType


class conditionType(GeneratedsSuper):
    """All necessary information for one part of a measurement"""
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, id=None, refType=None, name=None, description=None, state=None, data=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = "dcc"
        self.id = _cast(None, id)
        self.id_nsprefix_ = None
        self.refType = _cast(None, refType)
        self.refType_nsprefix_ = None
        self.name = name
        self.name_nsprefix_ = "dcc"
        self.description = description
        self.description_nsprefix_ = "dcc"
        self.state = state
        self.validate_stateType(self.state)
        self.state_nsprefix_ = "dcc"
        self.data = data
        self.data_nsprefix_ = "dcc"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, conditionType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if conditionType.subclass:
            return conditionType.subclass(*args_, **kwargs_)
        else:
            return conditionType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name
    def get_description(self):
        return self.description
    def set_description(self, description):
        self.description = description
    def get_state(self):
        return self.state
    def set_state(self, state):
        self.state = state
    def get_data(self):
        return self.data
    def set_data(self, data):
        self.data = data
    def get_id(self):
        return self.id
    def set_id(self, id):
        self.id = id
    def get_refType(self):
        return self.refType
    def set_refType(self, refType):
        self.refType = refType
    def validate_stateType(self, value):
        result = True
        # Validate type stateType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['beforeAdjustment', 'afterAdjustment', 'beforeRepair', 'afterRepair']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on stateType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_stringRefType(self, value):
        # Validate type dcc:stringRefType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_stringRefType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_stringRefType_patterns_, ))
    validate_stringRefType_patterns_ = [['^((/[A-Za-z][A-Za-z0-9]+)*)$']]
    def hasContent_(self):
        if (
            self.name is not None or
            self.description is not None or
            self.state is not None or
            self.data is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:dcc="https://ptb.de/dcc"', name_='conditionType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('conditionType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'conditionType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='conditionType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='conditionType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='conditionType'):
        if self.id is not None and 'id' not in already_processed:
            already_processed.add('id')
            outfile.write(' id=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.id), input_name='id')), ))
        if self.refType is not None and 'refType' not in already_processed:
            already_processed.add('refType')
            outfile.write(' refType=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.refType), input_name='refType')), ))
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:dcc="https://ptb.de/dcc"', name_='conditionType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.name is not None:
            namespaceprefix_ = self.name_nsprefix_ + ':' if (UseCapturedNS_ and self.name_nsprefix_) else ''
            self.name.export(outfile, level, namespaceprefix_, namespacedef_='', name_='name', pretty_print=pretty_print)
        if self.description is not None:
            namespaceprefix_ = self.description_nsprefix_ + ':' if (UseCapturedNS_ and self.description_nsprefix_) else ''
            self.description.export(outfile, level, namespaceprefix_, namespacedef_='', name_='description', pretty_print=pretty_print)
        if self.state is not None:
            namespaceprefix_ = self.state_nsprefix_ + ':' if (UseCapturedNS_ and self.state_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sstate>%s</%sstate>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.state), input_name='state')), namespaceprefix_ , eol_))
        if self.data is not None:
            namespaceprefix_ = self.data_nsprefix_ + ':' if (UseCapturedNS_ and self.data_nsprefix_) else ''
            self.data.export(outfile, level, namespaceprefix_, namespacedef_='', name_='data', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='conditionType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{https://ptb.de/dcc}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{https://ptb.de/dcc}' + name_, nsmap=nsmap_)
        if self.id is not None:
            element.set('id', self.gds_format_string(self.id))
        if self.refType is not None:
            element.set('refType', self.gds_format_string(self.refType))
        if self.name is not None:
            name_ = self.name
            name_.to_etree(element, name_='name', mapping_=mapping_, nsmap_=nsmap_)
        if self.description is not None:
            description_ = self.description
            description_.to_etree(element, name_='description', mapping_=mapping_, nsmap_=nsmap_)
        if self.state is not None:
            state_ = self.state
            etree_.SubElement(element, '{https://ptb.de/dcc}state').text = self.gds_format_string(state_)
        if self.data is not None:
            data_ = self.data
            data_.to_etree(element, name_='data', mapping_=mapping_, nsmap_=nsmap_)
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
        value = find_attr_value_('id', node)
        if value is not None and 'id' not in already_processed:
            already_processed.add('id')
            self.id = value
        value = find_attr_value_('refType', node)
        if value is not None and 'refType' not in already_processed:
            already_processed.add('refType')
            self.refType = value
            self.validate_stringRefType(self.refType)    # validate type stringRefType
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'name':
            obj_ = textType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.name = obj_
            obj_.original_tagname_ = 'name'
        elif nodeName_ == 'description':
            obj_ = textType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.description = obj_
            obj_.original_tagname_ = 'description'
        elif nodeName_ == 'state':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'state')
            value_ = self.gds_validate_string(value_, node, 'state')
            self.state = value_
            self.state_nsprefix_ = child_.prefix
            # validate type stateType
            self.validate_stateType(self.state)
        elif nodeName_ == 'data':
            obj_ = dataType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.data = obj_
            obj_.original_tagname_ = 'data'
# end class conditionType


class resultType(GeneratedsSuper):
    """The result itself"""
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, id=None, refId=None, refType=None, name=None, description=None, data=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = "dcc"
        self.id = _cast(None, id)
        self.id_nsprefix_ = None
        self.refId = _cast(None, refId)
        self.refId_nsprefix_ = None
        self.refType = _cast(None, refType)
        self.refType_nsprefix_ = None
        self.name = name
        self.name_nsprefix_ = "dcc"
        self.description = description
        self.description_nsprefix_ = "dcc"
        self.data = data
        self.data_nsprefix_ = "dcc"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, resultType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if resultType.subclass:
            return resultType.subclass(*args_, **kwargs_)
        else:
            return resultType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name
    def get_description(self):
        return self.description
    def set_description(self, description):
        self.description = description
    def get_data(self):
        return self.data
    def set_data(self, data):
        self.data = data
    def get_id(self):
        return self.id
    def set_id(self, id):
        self.id = id
    def get_refId(self):
        return self.refId
    def set_refId(self, refId):
        self.refId = refId
    def get_refType(self):
        return self.refType
    def set_refType(self, refType):
        self.refType = refType
    def validate_stringRefType(self, value):
        # Validate type dcc:stringRefType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_stringRefType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_stringRefType_patterns_, ))
    validate_stringRefType_patterns_ = [['^((/[A-Za-z][A-Za-z0-9]+)*)$']]
    def hasContent_(self):
        if (
            self.name is not None or
            self.description is not None or
            self.data is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:dcc="https://ptb.de/dcc"', name_='resultType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('resultType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'resultType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='resultType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='resultType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='resultType'):
        if self.id is not None and 'id' not in already_processed:
            already_processed.add('id')
            outfile.write(' id=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.id), input_name='id')), ))
        if self.refId is not None and 'refId' not in already_processed:
            already_processed.add('refId')
            outfile.write(' refId=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.refId), input_name='refId')), ))
        if self.refType is not None and 'refType' not in already_processed:
            already_processed.add('refType')
            outfile.write(' refType=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.refType), input_name='refType')), ))
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:dcc="https://ptb.de/dcc"', name_='resultType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.name is not None:
            namespaceprefix_ = self.name_nsprefix_ + ':' if (UseCapturedNS_ and self.name_nsprefix_) else ''
            self.name.export(outfile, level, namespaceprefix_, namespacedef_='', name_='name', pretty_print=pretty_print)
        if self.description is not None:
            namespaceprefix_ = self.description_nsprefix_ + ':' if (UseCapturedNS_ and self.description_nsprefix_) else ''
            self.description.export(outfile, level, namespaceprefix_, namespacedef_='', name_='description', pretty_print=pretty_print)
        if self.data is not None:
            namespaceprefix_ = self.data_nsprefix_ + ':' if (UseCapturedNS_ and self.data_nsprefix_) else ''
            self.data.export(outfile, level, namespaceprefix_, namespacedef_='', name_='data', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='resultType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{https://ptb.de/dcc}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{https://ptb.de/dcc}' + name_, nsmap=nsmap_)
        if self.id is not None:
            element.set('id', self.gds_format_string(self.id))
        if self.refId is not None:
            element.set('refId', self.gds_format_string(self.refId))
        if self.refType is not None:
            element.set('refType', self.gds_format_string(self.refType))
        if self.name is not None:
            name_ = self.name
            name_.to_etree(element, name_='name', mapping_=mapping_, nsmap_=nsmap_)
        if self.description is not None:
            description_ = self.description
            description_.to_etree(element, name_='description', mapping_=mapping_, nsmap_=nsmap_)
        if self.data is not None:
            data_ = self.data
            data_.to_etree(element, name_='data', mapping_=mapping_, nsmap_=nsmap_)
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
        value = find_attr_value_('id', node)
        if value is not None and 'id' not in already_processed:
            already_processed.add('id')
            self.id = value
        value = find_attr_value_('refId', node)
        if value is not None and 'refId' not in already_processed:
            already_processed.add('refId')
            self.refId = value
        value = find_attr_value_('refType', node)
        if value is not None and 'refType' not in already_processed:
            already_processed.add('refType')
            self.refType = value
            self.validate_stringRefType(self.refType)    # validate type stringRefType
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'name':
            obj_ = textType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.name = obj_
            obj_.original_tagname_ = 'name'
        elif nodeName_ == 'description':
            obj_ = textType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.description = obj_
            obj_.original_tagname_ = 'description'
        elif nodeName_ == 'data':
            obj_ = dataType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.data = obj_
            obj_.original_tagname_ = 'data'
# end class resultType


class resultListType(GeneratedsSuper):
    """Elements for the measurement results"""
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, result=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = "dcc"
        if result is None:
            self.result = []
        else:
            self.result = result
        self.result_nsprefix_ = "dcc"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, resultListType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if resultListType.subclass:
            return resultListType.subclass(*args_, **kwargs_)
        else:
            return resultListType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_result(self):
        return self.result
    def set_result(self, result):
        self.result = result
    def add_result(self, value):
        self.result.append(value)
    def insert_result_at(self, index, value):
        self.result.insert(index, value)
    def replace_result_at(self, index, value):
        self.result[index] = value
    def hasContent_(self):
        if (
            self.result
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:dcc="https://ptb.de/dcc"', name_='resultListType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('resultListType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'resultListType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='resultListType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='resultListType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='resultListType'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:dcc="https://ptb.de/dcc"', name_='resultListType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for result_ in self.result:
            namespaceprefix_ = self.result_nsprefix_ + ':' if (UseCapturedNS_ and self.result_nsprefix_) else ''
            result_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='result', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='resultListType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{https://ptb.de/dcc}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{https://ptb.de/dcc}' + name_, nsmap=nsmap_)
        for result_ in self.result:
            result_.to_etree(element, name_='result', mapping_=mapping_, nsmap_=nsmap_)
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
        if nodeName_ == 'result':
            obj_ = resultType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.result.append(obj_)
            obj_.original_tagname_ = 'result'
# end class resultListType


class dataType(GeneratedsSuper):
    """In the Element "outcome", any of the elements
    "text", "formula", "byteData", "chart", "image", "data" and "xml"
    can be used multiple times in an arbitrary order. The usage of each element
    is optional. At least one of the elements must be provided."""
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, id=None, text=None, formula=None, byteData=None, xml=None, quantity=None, list=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = "dcc"
        self.id = _cast(None, id)
        self.id_nsprefix_ = None
        if text is None:
            self.text = []
        else:
            self.text = text
        self.text_nsprefix_ = "dcc"
        if formula is None:
            self.formula = []
        else:
            self.formula = formula
        self.formula_nsprefix_ = "dcc"
        if byteData is None:
            self.byteData = []
        else:
            self.byteData = byteData
        self.byteData_nsprefix_ = "dcc"
        if xml is None:
            self.xml = []
        else:
            self.xml = xml
        self.xml_nsprefix_ = "dcc"
        if quantity is None:
            self.quantity = []
        else:
            self.quantity = quantity
        self.quantity_nsprefix_ = "dcc"
        if list is None:
            self.list = []
        else:
            self.list = list
        self.list_nsprefix_ = "dcc"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, dataType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if dataType.subclass:
            return dataType.subclass(*args_, **kwargs_)
        else:
            return dataType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_text(self):
        return self.text
    def set_text(self, text):
        self.text = text
    def add_text(self, value):
        self.text.append(value)
    def insert_text_at(self, index, value):
        self.text.insert(index, value)
    def replace_text_at(self, index, value):
        self.text[index] = value
    def get_formula(self):
        return self.formula
    def set_formula(self, formula):
        self.formula = formula
    def add_formula(self, value):
        self.formula.append(value)
    def insert_formula_at(self, index, value):
        self.formula.insert(index, value)
    def replace_formula_at(self, index, value):
        self.formula[index] = value
    def get_byteData(self):
        return self.byteData
    def set_byteData(self, byteData):
        self.byteData = byteData
    def add_byteData(self, value):
        self.byteData.append(value)
    def insert_byteData_at(self, index, value):
        self.byteData.insert(index, value)
    def replace_byteData_at(self, index, value):
        self.byteData[index] = value
    def get_xml(self):
        return self.xml
    def set_xml(self, xml):
        self.xml = xml
    def add_xml(self, value):
        self.xml.append(value)
    def insert_xml_at(self, index, value):
        self.xml.insert(index, value)
    def replace_xml_at(self, index, value):
        self.xml[index] = value
    def get_quantity(self):
        return self.quantity
    def set_quantity(self, quantity):
        self.quantity = quantity
    def add_quantity(self, value):
        self.quantity.append(value)
    def insert_quantity_at(self, index, value):
        self.quantity.insert(index, value)
    def replace_quantity_at(self, index, value):
        self.quantity[index] = value
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
    def get_id(self):
        return self.id
    def set_id(self, id):
        self.id = id
    def hasContent_(self):
        if (
            self.text or
            self.formula or
            self.byteData or
            self.xml or
            self.quantity or
            self.list
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:dcc="https://ptb.de/dcc"', name_='dataType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('dataType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'dataType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='dataType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='dataType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='dataType'):
        if self.id is not None and 'id' not in already_processed:
            already_processed.add('id')
            outfile.write(' id=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.id), input_name='id')), ))
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:dcc="https://ptb.de/dcc"', name_='dataType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for text_ in self.text:
            namespaceprefix_ = self.text_nsprefix_ + ':' if (UseCapturedNS_ and self.text_nsprefix_) else ''
            text_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='text', pretty_print=pretty_print)
        for formula_ in self.formula:
            namespaceprefix_ = self.formula_nsprefix_ + ':' if (UseCapturedNS_ and self.formula_nsprefix_) else ''
            formula_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='formula', pretty_print=pretty_print)
        for byteData_ in self.byteData:
            namespaceprefix_ = self.byteData_nsprefix_ + ':' if (UseCapturedNS_ and self.byteData_nsprefix_) else ''
            byteData_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='byteData', pretty_print=pretty_print)
        for xml_ in self.xml:
            namespaceprefix_ = self.xml_nsprefix_ + ':' if (UseCapturedNS_ and self.xml_nsprefix_) else ''
            xml_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='xml', pretty_print=pretty_print)
        for quantity_ in self.quantity:
            namespaceprefix_ = self.quantity_nsprefix_ + ':' if (UseCapturedNS_ and self.quantity_nsprefix_) else ''
            quantity_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='quantity', pretty_print=pretty_print)
        for list_ in self.list:
            namespaceprefix_ = self.list_nsprefix_ + ':' if (UseCapturedNS_ and self.list_nsprefix_) else ''
            list_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='list', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='dataType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{https://ptb.de/dcc}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{https://ptb.de/dcc}' + name_, nsmap=nsmap_)
        if self.id is not None:
            element.set('id', self.gds_format_string(self.id))
        for text_ in self.text:
            text_.to_etree(element, name_='text', mapping_=mapping_, nsmap_=nsmap_)
        for formula_ in self.formula:
            formula_.to_etree(element, name_='formula', mapping_=mapping_, nsmap_=nsmap_)
        for byteData_ in self.byteData:
            byteData_.to_etree(element, name_='byteData', mapping_=mapping_, nsmap_=nsmap_)
        for xml_ in self.xml:
            xml_.to_etree(element, name_='xml', mapping_=mapping_, nsmap_=nsmap_)
        for quantity_ in self.quantity:
            quantity_.to_etree(element, name_='quantity', mapping_=mapping_, nsmap_=nsmap_)
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
        value = find_attr_value_('id', node)
        if value is not None and 'id' not in already_processed:
            already_processed.add('id')
            self.id = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'text':
            obj_ = textType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.text.append(obj_)
            obj_.original_tagname_ = 'text'
        elif nodeName_ == 'formula':
            obj_ = formulaType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.formula.append(obj_)
            obj_.original_tagname_ = 'formula'
        elif nodeName_ == 'byteData':
            obj_ = byteDataType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.byteData.append(obj_)
            obj_.original_tagname_ = 'byteData'
        elif nodeName_ == 'xml':
            obj_ = xmlType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.xml.append(obj_)
            obj_.original_tagname_ = 'xml'
        elif nodeName_ == 'quantity':
            obj_ = quantityType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.quantity.append(obj_)
            obj_.original_tagname_ = 'quantity'
        elif nodeName_ == 'list':
            obj_ = listType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.list.append(obj_)
            obj_.original_tagname_ = 'list'
# end class dataType


class quantityType(GeneratedsSuper):
    """Basic element for the statement of measurement values in a DCC.
    The measurement value, its unit and uncertainty are defined by type
    'si:real'.
    The 'unit' must be defined in the SI-system (siunitx format).
    Additional information can be made according to MRA, Ilac and external
    measurements in the 'measurementMetaData' element.
    In addition, the 'quantity' can contain a comma separated list of
    independent real quantities
    ('si:realCS').
    The 'quantity' has an optional 'name' element and it can have a unique ID.
    The 'name' element can be repeated with different languages."""
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, id=None, refId=None, refType=None, name=None, noQuantity=None, real=None, list=None, hybrid=None, usedMethods=None, usedSoftware=None, influenceConditions=None, measurementMetaData=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = "dcc"
        self.id = _cast(None, id)
        self.id_nsprefix_ = None
        self.refId = _cast(None, refId)
        self.refId_nsprefix_ = None
        self.refType = _cast(None, refType)
        self.refType_nsprefix_ = None
        self.name = name
        self.name_nsprefix_ = "dcc"
        self.noQuantity = noQuantity
        self.noQuantity_nsprefix_ = "dcc"
        self.real = real
        self.real_nsprefix_ = "si"
        self.list = list
        self.list_nsprefix_ = "si"
        self.hybrid = hybrid
        self.hybrid_nsprefix_ = "si"
        self.usedMethods = usedMethods
        self.usedMethods_nsprefix_ = "dcc"
        self.usedSoftware = usedSoftware
        self.usedSoftware_nsprefix_ = "dcc"
        self.influenceConditions = influenceConditions
        self.influenceConditions_nsprefix_ = "dcc"
        self.measurementMetaData = measurementMetaData
        self.measurementMetaData_nsprefix_ = "dcc"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, quantityType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if quantityType.subclass:
            return quantityType.subclass(*args_, **kwargs_)
        else:
            return quantityType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name
    def get_noQuantity(self):
        return self.noQuantity
    def set_noQuantity(self, noQuantity):
        self.noQuantity = noQuantity
    def get_real(self):
        return self.real
    def set_real(self, real):
        self.real = real
    def get_list(self):
        return self.list
    def set_list(self, list):
        self.list = list
    def get_hybrid(self):
        return self.hybrid
    def set_hybrid(self, hybrid):
        self.hybrid = hybrid
    def get_usedMethods(self):
        return self.usedMethods
    def set_usedMethods(self, usedMethods):
        self.usedMethods = usedMethods
    def get_usedSoftware(self):
        return self.usedSoftware
    def set_usedSoftware(self, usedSoftware):
        self.usedSoftware = usedSoftware
    def get_influenceConditions(self):
        return self.influenceConditions
    def set_influenceConditions(self, influenceConditions):
        self.influenceConditions = influenceConditions
    def get_measurementMetaData(self):
        return self.measurementMetaData
    def set_measurementMetaData(self, measurementMetaData):
        self.measurementMetaData = measurementMetaData
    def get_id(self):
        return self.id
    def set_id(self, id):
        self.id = id
    def get_refId(self):
        return self.refId
    def set_refId(self, refId):
        self.refId = refId
    def get_refType(self):
        return self.refType
    def set_refType(self, refType):
        self.refType = refType
    def validate_stringRefType(self, value):
        # Validate type dcc:stringRefType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_stringRefType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_stringRefType_patterns_, ))
    validate_stringRefType_patterns_ = [['^((/[A-Za-z][A-Za-z0-9]+)*)$']]
    def hasContent_(self):
        if (
            self.name is not None or
            self.noQuantity is not None or
            self.real is not None or
            self.list is not None or
            self.hybrid is not None or
            self.usedMethods is not None or
            self.usedSoftware is not None or
            self.influenceConditions is not None or
            self.measurementMetaData is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:dcc="https://ptb.de/dcc" xmlns:si="https://ptb.de/si" ', name_='quantityType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('quantityType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'quantityType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='quantityType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='quantityType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='quantityType'):
        if self.id is not None and 'id' not in already_processed:
            already_processed.add('id')
            outfile.write(' id=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.id), input_name='id')), ))
        if self.refId is not None and 'refId' not in already_processed:
            already_processed.add('refId')
            outfile.write(' refId=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.refId), input_name='refId')), ))
        if self.refType is not None and 'refType' not in already_processed:
            already_processed.add('refType')
            outfile.write(' refType=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.refType), input_name='refType')), ))
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:dcc="https://ptb.de/dcc" xmlns:si="https://ptb.de/si" ', name_='quantityType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.name is not None:
            namespaceprefix_ = self.name_nsprefix_ + ':' if (UseCapturedNS_ and self.name_nsprefix_) else ''
            self.name.export(outfile, level, namespaceprefix_, namespacedef_='', name_='name', pretty_print=pretty_print)
        if self.noQuantity is not None:
            namespaceprefix_ = self.noQuantity_nsprefix_ + ':' if (UseCapturedNS_ and self.noQuantity_nsprefix_) else ''
            self.noQuantity.export(outfile, level, namespaceprefix_, namespacedef_='', name_='noQuantity', pretty_print=pretty_print)
        if self.real is not None:
            namespaceprefix_ = self.real_nsprefix_ + ':' if (UseCapturedNS_ and self.real_nsprefix_) else ''
            self.real.export(outfile, level, namespaceprefix_='si:', namespacedef_='', name_='real', pretty_print=pretty_print)
        if self.list is not None:
            namespaceprefix_ = self.list_nsprefix_ + ':' if (UseCapturedNS_ and self.list_nsprefix_) else ''
            self.list.export(outfile, level, namespaceprefix_='si:', namespacedef_='', name_='list', pretty_print=pretty_print)
        if self.hybrid is not None:
            namespaceprefix_ = self.hybrid_nsprefix_ + ':' if (UseCapturedNS_ and self.hybrid_nsprefix_) else ''
            self.hybrid.export(outfile, level, namespaceprefix_='si:', namespacedef_='', name_='hybrid', pretty_print=pretty_print)
        if self.usedMethods is not None:
            namespaceprefix_ = self.usedMethods_nsprefix_ + ':' if (UseCapturedNS_ and self.usedMethods_nsprefix_) else ''
            self.usedMethods.export(outfile, level, namespaceprefix_, namespacedef_='', name_='usedMethods', pretty_print=pretty_print)
        if self.usedSoftware is not None:
            namespaceprefix_ = self.usedSoftware_nsprefix_ + ':' if (UseCapturedNS_ and self.usedSoftware_nsprefix_) else ''
            self.usedSoftware.export(outfile, level, namespaceprefix_, namespacedef_='', name_='usedSoftware', pretty_print=pretty_print)
        if self.influenceConditions is not None:
            namespaceprefix_ = self.influenceConditions_nsprefix_ + ':' if (UseCapturedNS_ and self.influenceConditions_nsprefix_) else ''
            self.influenceConditions.export(outfile, level, namespaceprefix_, namespacedef_='', name_='influenceConditions', pretty_print=pretty_print)
        if self.measurementMetaData is not None:
            namespaceprefix_ = self.measurementMetaData_nsprefix_ + ':' if (UseCapturedNS_ and self.measurementMetaData_nsprefix_) else ''
            self.measurementMetaData.export(outfile, level, namespaceprefix_, namespacedef_='', name_='measurementMetaData', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='quantityType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{https://ptb.de/dcc}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{https://ptb.de/dcc}' + name_, nsmap=nsmap_)
        if self.id is not None:
            element.set('id', self.gds_format_string(self.id))
        if self.refId is not None:
            element.set('refId', self.gds_format_string(self.refId))
        if self.refType is not None:
            element.set('refType', self.gds_format_string(self.refType))
        if self.name is not None:
            name_ = self.name
            name_.to_etree(element, name_='name', mapping_=mapping_, nsmap_=nsmap_)
        if self.noQuantity is not None:
            noQuantity_ = self.noQuantity
            noQuantity_.to_etree(element, name_='noQuantity', mapping_=mapping_, nsmap_=nsmap_)
        if self.real is not None:
            real_ = self.real
            real_.to_etree(element, name_='real', mapping_=mapping_, nsmap_=nsmap_)
        if self.list is not None:
            list_ = self.list
            list_.to_etree(element, name_='list', mapping_=mapping_, nsmap_=nsmap_)
        if self.hybrid is not None:
            hybrid_ = self.hybrid
            hybrid_.to_etree(element, name_='hybrid', mapping_=mapping_, nsmap_=nsmap_)
        if self.usedMethods is not None:
            usedMethods_ = self.usedMethods
            usedMethods_.to_etree(element, name_='usedMethods', mapping_=mapping_, nsmap_=nsmap_)
        if self.usedSoftware is not None:
            usedSoftware_ = self.usedSoftware
            usedSoftware_.to_etree(element, name_='usedSoftware', mapping_=mapping_, nsmap_=nsmap_)
        if self.influenceConditions is not None:
            influenceConditions_ = self.influenceConditions
            influenceConditions_.to_etree(element, name_='influenceConditions', mapping_=mapping_, nsmap_=nsmap_)
        if self.measurementMetaData is not None:
            measurementMetaData_ = self.measurementMetaData
            measurementMetaData_.to_etree(element, name_='measurementMetaData', mapping_=mapping_, nsmap_=nsmap_)
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
        value = find_attr_value_('id', node)
        if value is not None and 'id' not in already_processed:
            already_processed.add('id')
            self.id = value
        value = find_attr_value_('refId', node)
        if value is not None and 'refId' not in already_processed:
            already_processed.add('refId')
            self.refId = value
        value = find_attr_value_('refType', node)
        if value is not None and 'refType' not in already_processed:
            already_processed.add('refType')
            self.refType = value
            self.validate_stringRefType(self.refType)    # validate type stringRefType
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'name':
            obj_ = textType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.name = obj_
            obj_.original_tagname_ = 'name'
        elif nodeName_ == 'noQuantity':
            obj_ = textType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.noQuantity = obj_
            obj_.original_tagname_ = 'noQuantity'
        elif nodeName_ == 'real':
            obj_ = real.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.real = obj_
            obj_.original_tagname_ = 'real'
        elif nodeName_ == 'list':
            obj_ = list.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.list = obj_
            obj_.original_tagname_ = 'list'
        elif nodeName_ == 'hybrid':
            obj_ = hybrid.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.hybrid = obj_
            obj_.original_tagname_ = 'hybrid'
        elif nodeName_ == 'usedMethods':
            obj_ = usedMethodListType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.usedMethods = obj_
            obj_.original_tagname_ = 'usedMethods'
        elif nodeName_ == 'usedSoftware':
            obj_ = softwareListType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.usedSoftware = obj_
            obj_.original_tagname_ = 'usedSoftware'
        elif nodeName_ == 'influenceConditions':
            obj_ = influenceConditionListType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.influenceConditions = obj_
            obj_.original_tagname_ = 'influenceConditions'
        elif nodeName_ == 'measurementMetaData':
            obj_ = measurementMetaDataListType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.measurementMetaData = obj_
            obj_.original_tagname_ = 'measurementMetaData'
# end class quantityType


class listType(GeneratedsSuper):
    """The 'list' element allows to define a collection of measurement results
    which are subject to structures with integrity. Basic structures are
    vector quantities. A recursive usage of 'list' allows the creation of
    matrix and tensor structures as well as structures of higher dimension. The
    'list'
    may also be used to give measurement results in combination with some
    ambient conditions at the measurement.
    In this version of the data format, the 'list' supports a global definition
    of uncertainties
    that are binding for all quantities inside the 'list' element.
    For future versions it is planned to add uncertainty elements for vector
    quantities
    (e.g. covariance matrix).
    The 'list' element can have a unique ID and several name elements."""
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, id=None, name=None, dateTime=None, list=None, quantity=None, usedMethods=None, usedSoftware=None, influenceConditions=None, measurementMetaData=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = "dcc"
        self.id = _cast(None, id)
        self.id_nsprefix_ = None
        self.name = name
        self.name_nsprefix_ = "dcc"
        if isinstance(dateTime, BaseStrType_):
            initvalue_ = datetime_.datetime.strptime(dateTime, '%Y-%m-%dT%H:%M:%S')
        else:
            initvalue_ = dateTime
        self.dateTime = initvalue_
        self.dateTime_nsprefix_ = "dcc"
        if list is None:
            self.list = []
        else:
            self.list = list
        self.list_nsprefix_ = "dcc"
        if quantity is None:
            self.quantity = []
        else:
            self.quantity = quantity
        self.quantity_nsprefix_ = "dcc"
        self.usedMethods = usedMethods
        self.usedMethods_nsprefix_ = "dcc"
        self.usedSoftware = usedSoftware
        self.usedSoftware_nsprefix_ = "dcc"
        self.influenceConditions = influenceConditions
        self.influenceConditions_nsprefix_ = "dcc"
        self.measurementMetaData = measurementMetaData
        self.measurementMetaData_nsprefix_ = "dcc"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, listType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if listType.subclass:
            return listType.subclass(*args_, **kwargs_)
        else:
            return listType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name
    def get_dateTime(self):
        return self.dateTime
    def set_dateTime(self, dateTime):
        self.dateTime = dateTime
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
    def get_quantity(self):
        return self.quantity
    def set_quantity(self, quantity):
        self.quantity = quantity
    def add_quantity(self, value):
        self.quantity.append(value)
    def insert_quantity_at(self, index, value):
        self.quantity.insert(index, value)
    def replace_quantity_at(self, index, value):
        self.quantity[index] = value
    def get_usedMethods(self):
        return self.usedMethods
    def set_usedMethods(self, usedMethods):
        self.usedMethods = usedMethods
    def get_usedSoftware(self):
        return self.usedSoftware
    def set_usedSoftware(self, usedSoftware):
        self.usedSoftware = usedSoftware
    def get_influenceConditions(self):
        return self.influenceConditions
    def set_influenceConditions(self, influenceConditions):
        self.influenceConditions = influenceConditions
    def get_measurementMetaData(self):
        return self.measurementMetaData
    def set_measurementMetaData(self, measurementMetaData):
        self.measurementMetaData = measurementMetaData
    def get_id(self):
        return self.id
    def set_id(self, id):
        self.id = id
    def hasContent_(self):
        if (
            self.name is not None or
            self.dateTime is not None or
            self.list or
            self.quantity or
            self.usedMethods is not None or
            self.usedSoftware is not None or
            self.influenceConditions is not None or
            self.measurementMetaData is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:dcc="https://ptb.de/dcc"', name_='listType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('listType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'listType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='listType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='listType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='listType'):
        if self.id is not None and 'id' not in already_processed:
            already_processed.add('id')
            outfile.write(' id=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.id), input_name='id')), ))
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:dcc="https://ptb.de/dcc"', name_='listType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.name is not None:
            namespaceprefix_ = self.name_nsprefix_ + ':' if (UseCapturedNS_ and self.name_nsprefix_) else ''
            self.name.export(outfile, level, namespaceprefix_, namespacedef_='', name_='name', pretty_print=pretty_print)
        if self.dateTime is not None:
            namespaceprefix_ = self.dateTime_nsprefix_ + ':' if (UseCapturedNS_ and self.dateTime_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sdateTime>%s</%sdateTime>%s' % (namespaceprefix_ , self.gds_format_datetime(self.dateTime, input_name='dateTime'), namespaceprefix_ , eol_))
        for list_ in self.list:
            namespaceprefix_ = self.list_nsprefix_ + ':' if (UseCapturedNS_ and self.list_nsprefix_) else ''
            list_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='list', pretty_print=pretty_print)
        for quantity_ in self.quantity:
            namespaceprefix_ = self.quantity_nsprefix_ + ':' if (UseCapturedNS_ and self.quantity_nsprefix_) else ''
            quantity_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='quantity', pretty_print=pretty_print)
        if self.usedMethods is not None:
            namespaceprefix_ = self.usedMethods_nsprefix_ + ':' if (UseCapturedNS_ and self.usedMethods_nsprefix_) else ''
            self.usedMethods.export(outfile, level, namespaceprefix_, namespacedef_='', name_='usedMethods', pretty_print=pretty_print)
        if self.usedSoftware is not None:
            namespaceprefix_ = self.usedSoftware_nsprefix_ + ':' if (UseCapturedNS_ and self.usedSoftware_nsprefix_) else ''
            self.usedSoftware.export(outfile, level, namespaceprefix_, namespacedef_='', name_='usedSoftware', pretty_print=pretty_print)
        if self.influenceConditions is not None:
            namespaceprefix_ = self.influenceConditions_nsprefix_ + ':' if (UseCapturedNS_ and self.influenceConditions_nsprefix_) else ''
            self.influenceConditions.export(outfile, level, namespaceprefix_, namespacedef_='', name_='influenceConditions', pretty_print=pretty_print)
        if self.measurementMetaData is not None:
            namespaceprefix_ = self.measurementMetaData_nsprefix_ + ':' if (UseCapturedNS_ and self.measurementMetaData_nsprefix_) else ''
            self.measurementMetaData.export(outfile, level, namespaceprefix_, namespacedef_='', name_='measurementMetaData', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='listType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{https://ptb.de/dcc}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{https://ptb.de/dcc}' + name_, nsmap=nsmap_)
        if self.id is not None:
            element.set('id', self.gds_format_string(self.id))
        if self.name is not None:
            name_ = self.name
            name_.to_etree(element, name_='name', mapping_=mapping_, nsmap_=nsmap_)
        if self.dateTime is not None:
            dateTime_ = self.dateTime
            etree_.SubElement(element, '{https://ptb.de/dcc}dateTime').text = self.gds_format_datetime(dateTime_)
        for list_ in self.list:
            list_.to_etree(element, name_='list', mapping_=mapping_, nsmap_=nsmap_)
        for quantity_ in self.quantity:
            quantity_.to_etree(element, name_='quantity', mapping_=mapping_, nsmap_=nsmap_)
        if self.usedMethods is not None:
            usedMethods_ = self.usedMethods
            usedMethods_.to_etree(element, name_='usedMethods', mapping_=mapping_, nsmap_=nsmap_)
        if self.usedSoftware is not None:
            usedSoftware_ = self.usedSoftware
            usedSoftware_.to_etree(element, name_='usedSoftware', mapping_=mapping_, nsmap_=nsmap_)
        if self.influenceConditions is not None:
            influenceConditions_ = self.influenceConditions
            influenceConditions_.to_etree(element, name_='influenceConditions', mapping_=mapping_, nsmap_=nsmap_)
        if self.measurementMetaData is not None:
            measurementMetaData_ = self.measurementMetaData
            measurementMetaData_.to_etree(element, name_='measurementMetaData', mapping_=mapping_, nsmap_=nsmap_)
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
        value = find_attr_value_('id', node)
        if value is not None and 'id' not in already_processed:
            already_processed.add('id')
            self.id = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'name':
            obj_ = textType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.name = obj_
            obj_.original_tagname_ = 'name'
        elif nodeName_ == 'dateTime':
            sval_ = child_.text
            dval_ = self.gds_parse_datetime(sval_)
            self.dateTime = dval_
            self.dateTime_nsprefix_ = child_.prefix
        elif nodeName_ == 'list':
            obj_ = listType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.list.append(obj_)
            obj_.original_tagname_ = 'list'
        elif nodeName_ == 'quantity':
            obj_ = quantityType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.quantity.append(obj_)
            obj_.original_tagname_ = 'quantity'
        elif nodeName_ == 'usedMethods':
            obj_ = usedMethodListType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.usedMethods = obj_
            obj_.original_tagname_ = 'usedMethods'
        elif nodeName_ == 'usedSoftware':
            obj_ = softwareListType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.usedSoftware = obj_
            obj_.original_tagname_ = 'usedSoftware'
        elif nodeName_ == 'influenceConditions':
            obj_ = influenceConditionListType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.influenceConditions = obj_
            obj_.original_tagname_ = 'influenceConditions'
        elif nodeName_ == 'measurementMetaData':
            obj_ = measurementMetaDataListType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.measurementMetaData = obj_
            obj_.original_tagname_ = 'measurementMetaData'
# end class listType


class measurementMetaDataListType(GeneratedsSuper):
    """TODO: noch anpassen an neue Struktur
    The measurement meta data comprises optional information that lead to a
    measurement result.
    The sub-elements should reference the specific and detailed information in
    the administrative part.
    Each element is optional and the user should only provide the elements that
    are relevant
    for the measurement result."""
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, metaData=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = "dcc"
        if metaData is None:
            self.metaData = []
        else:
            self.metaData = metaData
        self.metaData_nsprefix_ = "dcc"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, measurementMetaDataListType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if measurementMetaDataListType.subclass:
            return measurementMetaDataListType.subclass(*args_, **kwargs_)
        else:
            return measurementMetaDataListType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_metaData(self):
        return self.metaData
    def set_metaData(self, metaData):
        self.metaData = metaData
    def add_metaData(self, value):
        self.metaData.append(value)
    def insert_metaData_at(self, index, value):
        self.metaData.insert(index, value)
    def replace_metaData_at(self, index, value):
        self.metaData[index] = value
    def hasContent_(self):
        if (
            self.metaData
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:dcc="https://ptb.de/dcc"', name_='measurementMetaDataListType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('measurementMetaDataListType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'measurementMetaDataListType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='measurementMetaDataListType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='measurementMetaDataListType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='measurementMetaDataListType'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:dcc="https://ptb.de/dcc"', name_='measurementMetaDataListType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for metaData_ in self.metaData:
            namespaceprefix_ = self.metaData_nsprefix_ + ':' if (UseCapturedNS_ and self.metaData_nsprefix_) else ''
            metaData_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='metaData', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='measurementMetaDataListType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{https://ptb.de/dcc}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{https://ptb.de/dcc}' + name_, nsmap=nsmap_)
        for metaData_ in self.metaData:
            metaData_.to_etree(element, name_='metaData', mapping_=mapping_, nsmap_=nsmap_)
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
        if nodeName_ == 'metaData':
            obj_ = statementMetaDataType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.metaData.append(obj_)
            obj_.original_tagname_ = 'metaData'
# end class measurementMetaDataListType


class statementMetaDataType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, id=None, countryCodeISO3166_1=None, convention=None, traceable=None, norm=None, reference=None, declaration=None, valid=None, refId=None, date=None, period=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = "dcc"
        self.id = _cast(None, id)
        self.id_nsprefix_ = None
        if countryCodeISO3166_1 is None:
            self.countryCodeISO3166_1 = []
        else:
            self.countryCodeISO3166_1 = countryCodeISO3166_1
        self.countryCodeISO3166_1_nsprefix_ = "dcc"
        self.convention = convention
        self.convention_nsprefix_ = "dcc"
        self.traceable = traceable
        self.traceable_nsprefix_ = "dcc"
        self.norm = norm
        self.norm_nsprefix_ = "dcc"
        self.reference = reference
        self.reference_nsprefix_ = "dcc"
        self.declaration = declaration
        self.declaration_nsprefix_ = "dcc"
        self.valid = valid
        self.valid_nsprefix_ = "dcc"
        self.refId = refId
        self.refId_nsprefix_ = "dcc"
        if isinstance(date, BaseStrType_):
            initvalue_ = datetime_.datetime.strptime(date, '%Y-%m-%d').date()
        else:
            initvalue_ = date
        self.date = initvalue_
        self.date_nsprefix_ = "dcc"
        self.period = period
        self.period_nsprefix_ = "dcc"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, statementMetaDataType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if statementMetaDataType.subclass:
            return statementMetaDataType.subclass(*args_, **kwargs_)
        else:
            return statementMetaDataType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_countryCodeISO3166_1(self):
        return self.countryCodeISO3166_1
    def set_countryCodeISO3166_1(self, countryCodeISO3166_1):
        self.countryCodeISO3166_1 = countryCodeISO3166_1
    def add_countryCodeISO3166_1(self, value):
        self.countryCodeISO3166_1.append(value)
    def insert_countryCodeISO3166_1_at(self, index, value):
        self.countryCodeISO3166_1.insert(index, value)
    def replace_countryCodeISO3166_1_at(self, index, value):
        self.countryCodeISO3166_1[index] = value
    def get_convention(self):
        return self.convention
    def set_convention(self, convention):
        self.convention = convention
    def get_traceable(self):
        return self.traceable
    def set_traceable(self, traceable):
        self.traceable = traceable
    def get_norm(self):
        return self.norm
    def set_norm(self, norm):
        self.norm = norm
    def get_reference(self):
        return self.reference
    def set_reference(self, reference):
        self.reference = reference
    def get_declaration(self):
        return self.declaration
    def set_declaration(self, declaration):
        self.declaration = declaration
    def get_valid(self):
        return self.valid
    def set_valid(self, valid):
        self.valid = valid
    def get_refId(self):
        return self.refId
    def set_refId(self, refId):
        self.refId = refId
    def get_date(self):
        return self.date
    def set_date(self, date):
        self.date = date
    def get_period(self):
        return self.period
    def set_period(self, period):
        self.period = period
    def get_id(self):
        return self.id
    def set_id(self, id):
        self.id = id
    def validate_stringISO3166Type(self, value):
        result = True
        # Validate type stringISO3166Type, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_stringISO3166Type_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_stringISO3166Type_patterns_, ))
                result = False
        return result
    validate_stringISO3166Type_patterns_ = [['^([A-Z]{2})$']]
    def hasContent_(self):
        if (
            self.countryCodeISO3166_1 or
            self.convention is not None or
            self.traceable is not None or
            self.norm is not None or
            self.reference is not None or
            self.declaration is not None or
            self.valid is not None or
            self.refId is not None or
            self.date is not None or
            self.period is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:dcc="https://ptb.de/dcc"', name_='statementMetaDataType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('statementMetaDataType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'statementMetaDataType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='statementMetaDataType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='statementMetaDataType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='statementMetaDataType'):
        if self.id is not None and 'id' not in already_processed:
            already_processed.add('id')
            outfile.write(' id=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.id), input_name='id')), ))
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:dcc="https://ptb.de/dcc"', name_='statementMetaDataType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for countryCodeISO3166_1_ in self.countryCodeISO3166_1:
            namespaceprefix_ = self.countryCodeISO3166_1_nsprefix_ + ':' if (UseCapturedNS_ and self.countryCodeISO3166_1_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scountryCodeISO3166_1>%s</%scountryCodeISO3166_1>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(countryCodeISO3166_1_), input_name='countryCodeISO3166_1')), namespaceprefix_ , eol_))
        if self.convention is not None:
            namespaceprefix_ = self.convention_nsprefix_ + ':' if (UseCapturedNS_ and self.convention_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sconvention>%s</%sconvention>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.convention), input_name='convention')), namespaceprefix_ , eol_))
        if self.traceable is not None:
            namespaceprefix_ = self.traceable_nsprefix_ + ':' if (UseCapturedNS_ and self.traceable_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%straceable>%s</%straceable>%s' % (namespaceprefix_ , self.gds_format_boolean(self.traceable, input_name='traceable'), namespaceprefix_ , eol_))
        if self.norm is not None:
            namespaceprefix_ = self.norm_nsprefix_ + ':' if (UseCapturedNS_ and self.norm_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%snorm>%s</%snorm>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.norm), input_name='norm')), namespaceprefix_ , eol_))
        if self.reference is not None:
            namespaceprefix_ = self.reference_nsprefix_ + ':' if (UseCapturedNS_ and self.reference_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sreference>%s</%sreference>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.reference), input_name='reference')), namespaceprefix_ , eol_))
        if self.declaration is not None:
            namespaceprefix_ = self.declaration_nsprefix_ + ':' if (UseCapturedNS_ and self.declaration_nsprefix_) else ''
            self.declaration.export(outfile, level, namespaceprefix_, namespacedef_='', name_='declaration', pretty_print=pretty_print)
        if self.valid is not None:
            namespaceprefix_ = self.valid_nsprefix_ + ':' if (UseCapturedNS_ and self.valid_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%svalid>%s</%svalid>%s' % (namespaceprefix_ , self.gds_format_boolean(self.valid, input_name='valid'), namespaceprefix_ , eol_))
        if self.refId is not None:
            namespaceprefix_ = self.refId_nsprefix_ + ':' if (UseCapturedNS_ and self.refId_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%srefId>%s</%srefId>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.refId), input_name='refId')), namespaceprefix_ , eol_))
        if self.date is not None:
            namespaceprefix_ = self.date_nsprefix_ + ':' if (UseCapturedNS_ and self.date_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sdate>%s</%sdate>%s' % (namespaceprefix_ , self.gds_format_date(self.date, input_name='date'), namespaceprefix_ , eol_))
        if self.period is not None:
            namespaceprefix_ = self.period_nsprefix_ + ':' if (UseCapturedNS_ and self.period_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%speriod>%s</%speriod>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.period), input_name='period')), namespaceprefix_ , eol_))
    def to_etree(self, parent_element=None, name_='statementMetaDataType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{https://ptb.de/dcc}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{https://ptb.de/dcc}' + name_, nsmap=nsmap_)
        if self.id is not None:
            element.set('id', self.gds_format_string(self.id))
        for countryCodeISO3166_1_ in self.countryCodeISO3166_1:
            etree_.SubElement(element, '{https://ptb.de/dcc}countryCodeISO3166_1').text = self.gds_format_string(countryCodeISO3166_1_)
        if self.convention is not None:
            convention_ = self.convention
            etree_.SubElement(element, '{https://ptb.de/dcc}convention').text = self.gds_format_string(convention_)
        if self.traceable is not None:
            traceable_ = self.traceable
            etree_.SubElement(element, '{https://ptb.de/dcc}traceable').text = self.gds_format_boolean(traceable_)
        if self.norm is not None:
            norm_ = self.norm
            etree_.SubElement(element, '{https://ptb.de/dcc}norm').text = self.gds_format_string(norm_)
        if self.reference is not None:
            reference_ = self.reference
            etree_.SubElement(element, '{https://ptb.de/dcc}reference').text = self.gds_format_string(reference_)
        if self.declaration is not None:
            declaration_ = self.declaration
            declaration_.to_etree(element, name_='declaration', mapping_=mapping_, nsmap_=nsmap_)
        if self.valid is not None:
            valid_ = self.valid
            etree_.SubElement(element, '{https://ptb.de/dcc}valid').text = self.gds_format_boolean(valid_)
        if self.refId is not None:
            refId_ = self.refId
            etree_.SubElement(element, '{https://ptb.de/dcc}refId').text = self.gds_format_string(refId_)
        if self.date is not None:
            date_ = self.date
            etree_.SubElement(element, '{https://ptb.de/dcc}date').text = self.gds_format_date(date_)
        if self.period is not None:
            period_ = self.period
            etree_.SubElement(element, '{https://ptb.de/dcc}period').text = self.gds_format_string(period_)
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
        value = find_attr_value_('id', node)
        if value is not None and 'id' not in already_processed:
            already_processed.add('id')
            self.id = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'countryCodeISO3166_1':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'countryCodeISO3166_1')
            value_ = self.gds_validate_string(value_, node, 'countryCodeISO3166_1')
            self.countryCodeISO3166_1.append(value_)
            self.countryCodeISO3166_1_nsprefix_ = child_.prefix
            # validate type stringISO3166Type
            self.validate_stringISO3166Type(self.countryCodeISO3166_1[-1])
        elif nodeName_ == 'convention':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'convention')
            value_ = self.gds_validate_string(value_, node, 'convention')
            self.convention = value_
            self.convention_nsprefix_ = child_.prefix
        elif nodeName_ == 'traceable':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'traceable')
            ival_ = self.gds_validate_boolean(ival_, node, 'traceable')
            self.traceable = ival_
            self.traceable_nsprefix_ = child_.prefix
        elif nodeName_ == 'norm':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'norm')
            value_ = self.gds_validate_string(value_, node, 'norm')
            self.norm = value_
            self.norm_nsprefix_ = child_.prefix
        elif nodeName_ == 'reference':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'reference')
            value_ = self.gds_validate_string(value_, node, 'reference')
            self.reference = value_
            self.reference_nsprefix_ = child_.prefix
        elif nodeName_ == 'declaration':
            obj_ = textType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.declaration = obj_
            obj_.original_tagname_ = 'declaration'
        elif nodeName_ == 'valid':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'valid')
            ival_ = self.gds_validate_boolean(ival_, node, 'valid')
            self.valid = ival_
            self.valid_nsprefix_ = child_.prefix
        elif nodeName_ == 'refId':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'refId')
            value_ = self.gds_validate_string(value_, node, 'refId')
            self.refId = value_
            self.refId_nsprefix_ = child_.prefix
        elif nodeName_ == 'date':
            sval_ = child_.text
            dval_ = self.gds_parse_date(sval_)
            self.date = dval_
            self.date_nsprefix_ = child_.prefix
        elif nodeName_ == 'period':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'period')
            value_ = self.gds_validate_string(value_, node, 'period')
            self.period = value_
            self.period_nsprefix_ = child_.prefix
# end class statementMetaDataType


class stringWithLangType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, lang=None, id=None, valueOf_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = "dcc"
        self.lang = _cast(None, lang)
        self.lang_nsprefix_ = None
        self.id = _cast(None, id)
        self.id_nsprefix_ = None
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, stringWithLangType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if stringWithLangType.subclass:
            return stringWithLangType.subclass(*args_, **kwargs_)
        else:
            return stringWithLangType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_lang(self):
        return self.lang
    def set_lang(self, lang):
        self.lang = lang
    def get_id(self):
        return self.id
    def set_id(self, id):
        self.id = id
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def validate_stringISO639Type(self, value):
        # Validate type dcc:stringISO639Type, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_stringISO639Type_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_stringISO639Type_patterns_, ))
    validate_stringISO639Type_patterns_ = [['^([a-z]{2})$']]
    def hasContent_(self):
        if (
            (1 if type(self.valueOf_) in [int,float] else self.valueOf_)
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:dcc="https://ptb.de/dcc"', name_='stringWithLangType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('stringWithLangType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'stringWithLangType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='stringWithLangType')
        if self.hasContent_():
            outfile.write('>')
            outfile.write(self.convert_unicode(self.valueOf_))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='stringWithLangType', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='stringWithLangType'):
        if self.lang is not None and 'lang' not in already_processed:
            already_processed.add('lang')
            outfile.write(' lang=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.lang), input_name='lang')), ))
        if self.id is not None and 'id' not in already_processed:
            already_processed.add('id')
            outfile.write(' id=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.id), input_name='id')), ))
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:dcc="https://ptb.de/dcc"', name_='stringWithLangType', fromsubclass_=False, pretty_print=True):
        pass
    def to_etree(self, parent_element=None, name_='stringWithLangType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{https://ptb.de/dcc}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{https://ptb.de/dcc}' + name_, nsmap=nsmap_)
        if self.lang is not None:
            element.set('lang', self.gds_format_string(self.lang))
        if self.id is not None:
            element.set('id', self.gds_format_string(self.id))
        if self.hasContent_():
            element.text = self.gds_format_string(self.get_valueOf_())
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
        self.valueOf_ = get_all_text_(node)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('lang', node)
        if value is not None and 'lang' not in already_processed:
            already_processed.add('lang')
            self.lang = value
            self.validate_stringISO639Type(self.lang)    # validate type stringISO639Type
        value = find_attr_value_('id', node)
        if value is not None and 'id' not in already_processed:
            already_processed.add('id')
            self.id = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class stringWithLangType


class locationType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, city=None, countryCode=None, postCode=None, postOfficeBox=None, state=None, street=None, streetNo=None, further=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = "dcc"
        if city is None:
            self.city = []
        else:
            self.city = city
        self.city_nsprefix_ = "dcc"
        if countryCode is None:
            self.countryCode = []
        else:
            self.countryCode = countryCode
        self.countryCode_nsprefix_ = "dcc"
        if postCode is None:
            self.postCode = []
        else:
            self.postCode = postCode
        self.postCode_nsprefix_ = "dcc"
        if postOfficeBox is None:
            self.postOfficeBox = []
        else:
            self.postOfficeBox = postOfficeBox
        self.postOfficeBox_nsprefix_ = "dcc"
        if state is None:
            self.state = []
        else:
            self.state = state
        self.state_nsprefix_ = "dcc"
        if street is None:
            self.street = []
        else:
            self.street = street
        self.street_nsprefix_ = "dcc"
        if streetNo is None:
            self.streetNo = []
        else:
            self.streetNo = streetNo
        self.streetNo_nsprefix_ = "dcc"
        if further is None:
            self.further = []
        else:
            self.further = further
        self.further_nsprefix_ = "dcc"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, locationType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if locationType.subclass:
            return locationType.subclass(*args_, **kwargs_)
        else:
            return locationType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_city(self):
        return self.city
    def set_city(self, city):
        self.city = city
    def add_city(self, value):
        self.city.append(value)
    def insert_city_at(self, index, value):
        self.city.insert(index, value)
    def replace_city_at(self, index, value):
        self.city[index] = value
    def get_countryCode(self):
        return self.countryCode
    def set_countryCode(self, countryCode):
        self.countryCode = countryCode
    def add_countryCode(self, value):
        self.countryCode.append(value)
    def insert_countryCode_at(self, index, value):
        self.countryCode.insert(index, value)
    def replace_countryCode_at(self, index, value):
        self.countryCode[index] = value
    def get_postCode(self):
        return self.postCode
    def set_postCode(self, postCode):
        self.postCode = postCode
    def add_postCode(self, value):
        self.postCode.append(value)
    def insert_postCode_at(self, index, value):
        self.postCode.insert(index, value)
    def replace_postCode_at(self, index, value):
        self.postCode[index] = value
    def get_postOfficeBox(self):
        return self.postOfficeBox
    def set_postOfficeBox(self, postOfficeBox):
        self.postOfficeBox = postOfficeBox
    def add_postOfficeBox(self, value):
        self.postOfficeBox.append(value)
    def insert_postOfficeBox_at(self, index, value):
        self.postOfficeBox.insert(index, value)
    def replace_postOfficeBox_at(self, index, value):
        self.postOfficeBox[index] = value
    def get_state(self):
        return self.state
    def set_state(self, state):
        self.state = state
    def add_state(self, value):
        self.state.append(value)
    def insert_state_at(self, index, value):
        self.state.insert(index, value)
    def replace_state_at(self, index, value):
        self.state[index] = value
    def get_street(self):
        return self.street
    def set_street(self, street):
        self.street = street
    def add_street(self, value):
        self.street.append(value)
    def insert_street_at(self, index, value):
        self.street.insert(index, value)
    def replace_street_at(self, index, value):
        self.street[index] = value
    def get_streetNo(self):
        return self.streetNo
    def set_streetNo(self, streetNo):
        self.streetNo = streetNo
    def add_streetNo(self, value):
        self.streetNo.append(value)
    def insert_streetNo_at(self, index, value):
        self.streetNo.insert(index, value)
    def replace_streetNo_at(self, index, value):
        self.streetNo[index] = value
    def get_further(self):
        return self.further
    def set_further(self, further):
        self.further = further
    def add_further(self, value):
        self.further.append(value)
    def insert_further_at(self, index, value):
        self.further.insert(index, value)
    def replace_further_at(self, index, value):
        self.further[index] = value
    def validate_stringISO3166Type(self, value):
        result = True
        # Validate type stringISO3166Type, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_stringISO3166Type_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_stringISO3166Type_patterns_, ))
                result = False
        return result
    validate_stringISO3166Type_patterns_ = [['^([A-Z]{2})$']]
    def hasContent_(self):
        if (
            self.city or
            self.countryCode or
            self.postCode or
            self.postOfficeBox or
            self.state or
            self.street or
            self.streetNo or
            self.further
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:dcc="https://ptb.de/dcc"', name_='locationType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('locationType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'locationType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='locationType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='locationType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='locationType'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:dcc="https://ptb.de/dcc"', name_='locationType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for city_ in self.city:
            namespaceprefix_ = self.city_nsprefix_ + ':' if (UseCapturedNS_ and self.city_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scity>%s</%scity>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(city_), input_name='city')), namespaceprefix_ , eol_))
        for countryCode_ in self.countryCode:
            namespaceprefix_ = self.countryCode_nsprefix_ + ':' if (UseCapturedNS_ and self.countryCode_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scountryCode>%s</%scountryCode>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(countryCode_), input_name='countryCode')), namespaceprefix_ , eol_))
        for postCode_ in self.postCode:
            namespaceprefix_ = self.postCode_nsprefix_ + ':' if (UseCapturedNS_ and self.postCode_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%spostCode>%s</%spostCode>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(postCode_), input_name='postCode')), namespaceprefix_ , eol_))
        for postOfficeBox_ in self.postOfficeBox:
            namespaceprefix_ = self.postOfficeBox_nsprefix_ + ':' if (UseCapturedNS_ and self.postOfficeBox_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%spostOfficeBox>%s</%spostOfficeBox>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(postOfficeBox_), input_name='postOfficeBox')), namespaceprefix_ , eol_))
        for state_ in self.state:
            namespaceprefix_ = self.state_nsprefix_ + ':' if (UseCapturedNS_ and self.state_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sstate>%s</%sstate>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(state_), input_name='state')), namespaceprefix_ , eol_))
        for street_ in self.street:
            namespaceprefix_ = self.street_nsprefix_ + ':' if (UseCapturedNS_ and self.street_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sstreet>%s</%sstreet>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(street_), input_name='street')), namespaceprefix_ , eol_))
        for streetNo_ in self.streetNo:
            namespaceprefix_ = self.streetNo_nsprefix_ + ':' if (UseCapturedNS_ and self.streetNo_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sstreetNo>%s</%sstreetNo>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(streetNo_), input_name='streetNo')), namespaceprefix_ , eol_))
        for further_ in self.further:
            namespaceprefix_ = self.further_nsprefix_ + ':' if (UseCapturedNS_ and self.further_nsprefix_) else ''
            further_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='further', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='locationType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{https://ptb.de/dcc}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{https://ptb.de/dcc}' + name_, nsmap=nsmap_)
        for city_ in self.city:
            etree_.SubElement(element, '{https://ptb.de/dcc}city').text = self.gds_format_string(city_)
        for countryCode_ in self.countryCode:
            etree_.SubElement(element, '{https://ptb.de/dcc}countryCode').text = self.gds_format_string(countryCode_)
        for postCode_ in self.postCode:
            etree_.SubElement(element, '{https://ptb.de/dcc}postCode').text = self.gds_format_string(postCode_)
        for postOfficeBox_ in self.postOfficeBox:
            etree_.SubElement(element, '{https://ptb.de/dcc}postOfficeBox').text = self.gds_format_string(postOfficeBox_)
        for state_ in self.state:
            etree_.SubElement(element, '{https://ptb.de/dcc}state').text = self.gds_format_string(state_)
        for street_ in self.street:
            etree_.SubElement(element, '{https://ptb.de/dcc}street').text = self.gds_format_string(street_)
        for streetNo_ in self.streetNo:
            etree_.SubElement(element, '{https://ptb.de/dcc}streetNo').text = self.gds_format_string(streetNo_)
        for further_ in self.further:
            further_.to_etree(element, name_='further', mapping_=mapping_, nsmap_=nsmap_)
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
        if nodeName_ == 'city':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'city')
            value_ = self.gds_validate_string(value_, node, 'city')
            self.city.append(value_)
            self.city_nsprefix_ = child_.prefix
        elif nodeName_ == 'countryCode':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'countryCode')
            value_ = self.gds_validate_string(value_, node, 'countryCode')
            self.countryCode.append(value_)
            self.countryCode_nsprefix_ = child_.prefix
            # validate type stringISO3166Type
            self.validate_stringISO3166Type(self.countryCode[-1])
        elif nodeName_ == 'postCode':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'postCode')
            value_ = self.gds_validate_string(value_, node, 'postCode')
            self.postCode.append(value_)
            self.postCode_nsprefix_ = child_.prefix
        elif nodeName_ == 'postOfficeBox':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'postOfficeBox')
            value_ = self.gds_validate_string(value_, node, 'postOfficeBox')
            self.postOfficeBox.append(value_)
            self.postOfficeBox_nsprefix_ = child_.prefix
        elif nodeName_ == 'state':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'state')
            value_ = self.gds_validate_string(value_, node, 'state')
            self.state.append(value_)
            self.state_nsprefix_ = child_.prefix
        elif nodeName_ == 'street':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'street')
            value_ = self.gds_validate_string(value_, node, 'street')
            self.street.append(value_)
            self.street_nsprefix_ = child_.prefix
        elif nodeName_ == 'streetNo':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'streetNo')
            value_ = self.gds_validate_string(value_, node, 'streetNo')
            self.streetNo.append(value_)
            self.streetNo_nsprefix_ = child_.prefix
        elif nodeName_ == 'further':
            obj_ = textType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.further.append(obj_)
            obj_.original_tagname_ = 'further'
# end class locationType


class contactType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, id=None, name=None, eMail=None, phone=None, fax=None, location=None, descriptionData=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = "dcc"
        self.id = _cast(None, id)
        self.id_nsprefix_ = None
        self.name = name
        self.name_nsprefix_ = "dcc"
        self.eMail = eMail
        self.eMail_nsprefix_ = "dcc"
        self.phone = phone
        self.phone_nsprefix_ = "dcc"
        self.fax = fax
        self.fax_nsprefix_ = "dcc"
        self.location = location
        self.location_nsprefix_ = "dcc"
        self.descriptionData = descriptionData
        self.descriptionData_nsprefix_ = "dcc"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, contactType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if contactType.subclass:
            return contactType.subclass(*args_, **kwargs_)
        else:
            return contactType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name
    def get_eMail(self):
        return self.eMail
    def set_eMail(self, eMail):
        self.eMail = eMail
    def get_phone(self):
        return self.phone
    def set_phone(self, phone):
        self.phone = phone
    def get_fax(self):
        return self.fax
    def set_fax(self, fax):
        self.fax = fax
    def get_location(self):
        return self.location
    def set_location(self, location):
        self.location = location
    def get_descriptionData(self):
        return self.descriptionData
    def set_descriptionData(self, descriptionData):
        self.descriptionData = descriptionData
    def get_id(self):
        return self.id
    def set_id(self, id):
        self.id = id
    def hasContent_(self):
        if (
            self.name is not None or
            self.eMail is not None or
            self.phone is not None or
            self.fax is not None or
            self.location is not None or
            self.descriptionData is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:dcc="https://ptb.de/dcc"', name_='contactType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('contactType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'contactType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='contactType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='contactType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='contactType'):
        if self.id is not None and 'id' not in already_processed:
            already_processed.add('id')
            outfile.write(' id=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.id), input_name='id')), ))
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:dcc="https://ptb.de/dcc"', name_='contactType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.name is not None:
            namespaceprefix_ = self.name_nsprefix_ + ':' if (UseCapturedNS_ and self.name_nsprefix_) else ''
            self.name.export(outfile, level, namespaceprefix_, namespacedef_='', name_='name', pretty_print=pretty_print)
        if self.eMail is not None:
            namespaceprefix_ = self.eMail_nsprefix_ + ':' if (UseCapturedNS_ and self.eMail_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%seMail>%s</%seMail>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.eMail), input_name='eMail')), namespaceprefix_ , eol_))
        if self.phone is not None:
            namespaceprefix_ = self.phone_nsprefix_ + ':' if (UseCapturedNS_ and self.phone_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sphone>%s</%sphone>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.phone), input_name='phone')), namespaceprefix_ , eol_))
        if self.fax is not None:
            namespaceprefix_ = self.fax_nsprefix_ + ':' if (UseCapturedNS_ and self.fax_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sfax>%s</%sfax>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.fax), input_name='fax')), namespaceprefix_ , eol_))
        if self.location is not None:
            namespaceprefix_ = self.location_nsprefix_ + ':' if (UseCapturedNS_ and self.location_nsprefix_) else ''
            self.location.export(outfile, level, namespaceprefix_, namespacedef_='', name_='location', pretty_print=pretty_print)
        if self.descriptionData is not None:
            namespaceprefix_ = self.descriptionData_nsprefix_ + ':' if (UseCapturedNS_ and self.descriptionData_nsprefix_) else ''
            self.descriptionData.export(outfile, level, namespaceprefix_, namespacedef_='', name_='descriptionData', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='contactType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{https://ptb.de/dcc}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{https://ptb.de/dcc}' + name_, nsmap=nsmap_)
        if self.id is not None:
            element.set('id', self.gds_format_string(self.id))
        if self.name is not None:
            name_ = self.name
            name_.to_etree(element, name_='name', mapping_=mapping_, nsmap_=nsmap_)
        if self.eMail is not None:
            eMail_ = self.eMail
            etree_.SubElement(element, '{https://ptb.de/dcc}eMail').text = self.gds_format_string(eMail_)
        if self.phone is not None:
            phone_ = self.phone
            etree_.SubElement(element, '{https://ptb.de/dcc}phone').text = self.gds_format_string(phone_)
        if self.fax is not None:
            fax_ = self.fax
            etree_.SubElement(element, '{https://ptb.de/dcc}fax').text = self.gds_format_string(fax_)
        if self.location is not None:
            location_ = self.location
            location_.to_etree(element, name_='location', mapping_=mapping_, nsmap_=nsmap_)
        if self.descriptionData is not None:
            descriptionData_ = self.descriptionData
            descriptionData_.to_etree(element, name_='descriptionData', mapping_=mapping_, nsmap_=nsmap_)
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
        value = find_attr_value_('id', node)
        if value is not None and 'id' not in already_processed:
            already_processed.add('id')
            self.id = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'name':
            obj_ = textType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.name = obj_
            obj_.original_tagname_ = 'name'
        elif nodeName_ == 'eMail':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'eMail')
            value_ = self.gds_validate_string(value_, node, 'eMail')
            self.eMail = value_
            self.eMail_nsprefix_ = child_.prefix
        elif nodeName_ == 'phone':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'phone')
            value_ = self.gds_validate_string(value_, node, 'phone')
            self.phone = value_
            self.phone_nsprefix_ = child_.prefix
        elif nodeName_ == 'fax':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'fax')
            value_ = self.gds_validate_string(value_, node, 'fax')
            self.fax = value_
            self.fax_nsprefix_ = child_.prefix
        elif nodeName_ == 'location':
            obj_ = locationType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.location = obj_
            obj_.original_tagname_ = 'location'
        elif nodeName_ == 'descriptionData':
            obj_ = byteDataType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.descriptionData = obj_
            obj_.original_tagname_ = 'descriptionData'
# end class contactType


class contactNotStrictType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, id=None, name=None, eMail=None, phone=None, fax=None, location=None, descriptionData=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = "dcc"
        self.id = _cast(None, id)
        self.id_nsprefix_ = None
        self.name = name
        self.name_nsprefix_ = "dcc"
        self.eMail = eMail
        self.eMail_nsprefix_ = "dcc"
        self.phone = phone
        self.phone_nsprefix_ = "dcc"
        self.fax = fax
        self.fax_nsprefix_ = "dcc"
        self.location = location
        self.location_nsprefix_ = "dcc"
        self.descriptionData = descriptionData
        self.descriptionData_nsprefix_ = "dcc"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, contactNotStrictType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if contactNotStrictType.subclass:
            return contactNotStrictType.subclass(*args_, **kwargs_)
        else:
            return contactNotStrictType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name
    def get_eMail(self):
        return self.eMail
    def set_eMail(self, eMail):
        self.eMail = eMail
    def get_phone(self):
        return self.phone
    def set_phone(self, phone):
        self.phone = phone
    def get_fax(self):
        return self.fax
    def set_fax(self, fax):
        self.fax = fax
    def get_location(self):
        return self.location
    def set_location(self, location):
        self.location = location
    def get_descriptionData(self):
        return self.descriptionData
    def set_descriptionData(self, descriptionData):
        self.descriptionData = descriptionData
    def get_id(self):
        return self.id
    def set_id(self, id):
        self.id = id
    def hasContent_(self):
        if (
            self.name is not None or
            self.eMail is not None or
            self.phone is not None or
            self.fax is not None or
            self.location is not None or
            self.descriptionData is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:dcc="https://ptb.de/dcc"', name_='contactNotStrictType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('contactNotStrictType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'contactNotStrictType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='contactNotStrictType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='contactNotStrictType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='contactNotStrictType'):
        if self.id is not None and 'id' not in already_processed:
            already_processed.add('id')
            outfile.write(' id=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.id), input_name='id')), ))
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:dcc="https://ptb.de/dcc"', name_='contactNotStrictType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.name is not None:
            namespaceprefix_ = self.name_nsprefix_ + ':' if (UseCapturedNS_ and self.name_nsprefix_) else ''
            self.name.export(outfile, level, namespaceprefix_, namespacedef_='', name_='name', pretty_print=pretty_print)
        if self.eMail is not None:
            namespaceprefix_ = self.eMail_nsprefix_ + ':' if (UseCapturedNS_ and self.eMail_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%seMail>%s</%seMail>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.eMail), input_name='eMail')), namespaceprefix_ , eol_))
        if self.phone is not None:
            namespaceprefix_ = self.phone_nsprefix_ + ':' if (UseCapturedNS_ and self.phone_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sphone>%s</%sphone>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.phone), input_name='phone')), namespaceprefix_ , eol_))
        if self.fax is not None:
            namespaceprefix_ = self.fax_nsprefix_ + ':' if (UseCapturedNS_ and self.fax_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sfax>%s</%sfax>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.fax), input_name='fax')), namespaceprefix_ , eol_))
        if self.location is not None:
            namespaceprefix_ = self.location_nsprefix_ + ':' if (UseCapturedNS_ and self.location_nsprefix_) else ''
            self.location.export(outfile, level, namespaceprefix_, namespacedef_='', name_='location', pretty_print=pretty_print)
        if self.descriptionData is not None:
            namespaceprefix_ = self.descriptionData_nsprefix_ + ':' if (UseCapturedNS_ and self.descriptionData_nsprefix_) else ''
            self.descriptionData.export(outfile, level, namespaceprefix_, namespacedef_='', name_='descriptionData', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='contactNotStrictType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{https://ptb.de/dcc}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{https://ptb.de/dcc}' + name_, nsmap=nsmap_)
        if self.id is not None:
            element.set('id', self.gds_format_string(self.id))
        if self.name is not None:
            name_ = self.name
            name_.to_etree(element, name_='name', mapping_=mapping_, nsmap_=nsmap_)
        if self.eMail is not None:
            eMail_ = self.eMail
            etree_.SubElement(element, '{https://ptb.de/dcc}eMail').text = self.gds_format_string(eMail_)
        if self.phone is not None:
            phone_ = self.phone
            etree_.SubElement(element, '{https://ptb.de/dcc}phone').text = self.gds_format_string(phone_)
        if self.fax is not None:
            fax_ = self.fax
            etree_.SubElement(element, '{https://ptb.de/dcc}fax').text = self.gds_format_string(fax_)
        if self.location is not None:
            location_ = self.location
            location_.to_etree(element, name_='location', mapping_=mapping_, nsmap_=nsmap_)
        if self.descriptionData is not None:
            descriptionData_ = self.descriptionData
            descriptionData_.to_etree(element, name_='descriptionData', mapping_=mapping_, nsmap_=nsmap_)
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
        value = find_attr_value_('id', node)
        if value is not None and 'id' not in already_processed:
            already_processed.add('id')
            self.id = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'name':
            obj_ = textType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.name = obj_
            obj_.original_tagname_ = 'name'
        elif nodeName_ == 'eMail':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'eMail')
            value_ = self.gds_validate_string(value_, node, 'eMail')
            self.eMail = value_
            self.eMail_nsprefix_ = child_.prefix
        elif nodeName_ == 'phone':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'phone')
            value_ = self.gds_validate_string(value_, node, 'phone')
            self.phone = value_
            self.phone_nsprefix_ = child_.prefix
        elif nodeName_ == 'fax':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'fax')
            value_ = self.gds_validate_string(value_, node, 'fax')
            self.fax = value_
            self.fax_nsprefix_ = child_.prefix
        elif nodeName_ == 'location':
            obj_ = locationType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.location = obj_
            obj_.original_tagname_ = 'location'
        elif nodeName_ == 'descriptionData':
            obj_ = byteDataType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.descriptionData = obj_
            obj_.original_tagname_ = 'descriptionData'
# end class contactNotStrictType


class hashType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, id=None, reference=None, referenceID=None, procedure=None, value=None, linkedReport=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = "dcc"
        self.id = _cast(None, id)
        self.id_nsprefix_ = None
        self.reference = reference
        self.reference_nsprefix_ = "dcc"
        self.referenceID = referenceID
        self.referenceID_nsprefix_ = "dcc"
        self.procedure = procedure
        self.procedure_nsprefix_ = "dcc"
        self.value = value
        self.value_nsprefix_ = "dcc"
        self.linkedReport = linkedReport
        self.linkedReport_nsprefix_ = "dcc"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, hashType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if hashType.subclass:
            return hashType.subclass(*args_, **kwargs_)
        else:
            return hashType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_reference(self):
        return self.reference
    def set_reference(self, reference):
        self.reference = reference
    def get_referenceID(self):
        return self.referenceID
    def set_referenceID(self, referenceID):
        self.referenceID = referenceID
    def get_procedure(self):
        return self.procedure
    def set_procedure(self, procedure):
        self.procedure = procedure
    def get_value(self):
        return self.value
    def set_value(self, value):
        self.value = value
    def get_linkedReport(self):
        return self.linkedReport
    def set_linkedReport(self, linkedReport):
        self.linkedReport = linkedReport
    def get_id(self):
        return self.id
    def set_id(self, id):
        self.id = id
    def hasContent_(self):
        if (
            self.reference is not None or
            self.referenceID is not None or
            self.procedure is not None or
            self.value is not None or
            self.linkedReport is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:dcc="https://ptb.de/dcc"', name_='hashType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('hashType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'hashType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='hashType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='hashType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='hashType'):
        if self.id is not None and 'id' not in already_processed:
            already_processed.add('id')
            outfile.write(' id=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.id), input_name='id')), ))
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:dcc="https://ptb.de/dcc"', name_='hashType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.reference is not None:
            namespaceprefix_ = self.reference_nsprefix_ + ':' if (UseCapturedNS_ and self.reference_nsprefix_) else ''
            self.reference.export(outfile, level, namespaceprefix_, namespacedef_='', name_='reference', pretty_print=pretty_print)
        if self.referenceID is not None:
            namespaceprefix_ = self.referenceID_nsprefix_ + ':' if (UseCapturedNS_ and self.referenceID_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sreferenceID>%s</%sreferenceID>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.referenceID), input_name='referenceID')), namespaceprefix_ , eol_))
        if self.procedure is not None:
            namespaceprefix_ = self.procedure_nsprefix_ + ':' if (UseCapturedNS_ and self.procedure_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sprocedure>%s</%sprocedure>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.procedure), input_name='procedure')), namespaceprefix_ , eol_))
        if self.value is not None:
            namespaceprefix_ = self.value_nsprefix_ + ':' if (UseCapturedNS_ and self.value_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%svalue>%s</%svalue>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.value), input_name='value')), namespaceprefix_ , eol_))
        if self.linkedReport is not None:
            namespaceprefix_ = self.linkedReport_nsprefix_ + ':' if (UseCapturedNS_ and self.linkedReport_nsprefix_) else ''
            self.linkedReport.export(outfile, level, namespaceprefix_, namespacedef_='', name_='linkedReport', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='hashType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{https://ptb.de/dcc}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{https://ptb.de/dcc}' + name_, nsmap=nsmap_)
        if self.id is not None:
            element.set('id', self.gds_format_string(self.id))
        if self.reference is not None:
            reference_ = self.reference
            reference_.to_etree(element, name_='reference', mapping_=mapping_, nsmap_=nsmap_)
        if self.referenceID is not None:
            referenceID_ = self.referenceID
            etree_.SubElement(element, '{https://ptb.de/dcc}referenceID').text = self.gds_format_string(referenceID_)
        if self.procedure is not None:
            procedure_ = self.procedure
            etree_.SubElement(element, '{https://ptb.de/dcc}procedure').text = self.gds_format_string(procedure_)
        if self.value is not None:
            value_ = self.value
            etree_.SubElement(element, '{https://ptb.de/dcc}value').text = self.gds_format_string(value_)
        if self.linkedReport is not None:
            linkedReport_ = self.linkedReport
            linkedReport_.to_etree(element, name_='linkedReport', mapping_=mapping_, nsmap_=nsmap_)
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
        value = find_attr_value_('id', node)
        if value is not None and 'id' not in already_processed:
            already_processed.add('id')
            self.id = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'reference':
            obj_ = textType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.reference = obj_
            obj_.original_tagname_ = 'reference'
        elif nodeName_ == 'referenceID':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'referenceID')
            value_ = self.gds_validate_string(value_, node, 'referenceID')
            self.referenceID = value_
            self.referenceID_nsprefix_ = child_.prefix
        elif nodeName_ == 'procedure':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'procedure')
            value_ = self.gds_validate_string(value_, node, 'procedure')
            self.procedure = value_
            self.procedure_nsprefix_ = child_.prefix
        elif nodeName_ == 'value':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'value')
            value_ = self.gds_validate_string(value_, node, 'value')
            self.value = value_
            self.value_nsprefix_ = child_.prefix
        elif nodeName_ == 'linkedReport':
            obj_ = hashType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.linkedReport = obj_
            obj_.original_tagname_ = 'linkedReport'
# end class hashType


class textType(GeneratedsSuper):
    """The textType defines the type for writing text in the DCC.
    In this Type, the element content can be used many times with different
    language definition (attribute
    lang).
    The optional attribute ID is for a unique ID."""
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, id=None, content=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = "dcc"
        self.id = _cast(None, id)
        self.id_nsprefix_ = None
        if content is None:
            self.content = []
        else:
            self.content = content
        self.content_nsprefix_ = "dcc"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, textType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if textType.subclass:
            return textType.subclass(*args_, **kwargs_)
        else:
            return textType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_content(self):
        return self.content
    def set_content(self, content):
        self.content = content
    def add_content(self, value):
        self.content.append(value)
    def insert_content_at(self, index, value):
        self.content.insert(index, value)
    def replace_content_at(self, index, value):
        self.content[index] = value
    def get_id(self):
        return self.id
    def set_id(self, id):
        self.id = id
    def hasContent_(self):
        if (
            self.content
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:dcc="https://ptb.de/dcc"', name_='textType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('textType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'textType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='textType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='textType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='textType'):
        if self.id is not None and 'id' not in already_processed:
            already_processed.add('id')
            outfile.write(' id=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.id), input_name='id')), ))
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:dcc="https://ptb.de/dcc"', name_='textType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for content_ in self.content:
            namespaceprefix_ = self.content_nsprefix_ + ':' if (UseCapturedNS_ and self.content_nsprefix_) else ''
            content_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='content', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='textType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{https://ptb.de/dcc}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{https://ptb.de/dcc}' + name_, nsmap=nsmap_)
        if self.id is not None:
            element.set('id', self.gds_format_string(self.id))
        for content_ in self.content:
            content_.to_etree(element, name_='content', mapping_=mapping_, nsmap_=nsmap_)
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
        value = find_attr_value_('id', node)
        if value is not None and 'id' not in already_processed:
            already_processed.add('id')
            self.id = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'content':
            obj_ = stringWithLangType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.content.append(obj_)
            obj_.original_tagname_ = 'content'
# end class textType


class byteDataType(GeneratedsSuper):
    """The byteDataType defines a type which allows to add
    binary encoded files to the measurement result section.
    It is a good practise to use the Base64
    Data Encodings standard (see RFC 4648).
    The file must be encoded as base64Binary, see RFC 4648.
    Examples for the content are image files or ZIP archives.
    The element fileName gives the name of the original file.
    Element mimeType is the underlying file type (e.g. zip, jpeg, png).
    Element data contains the base64Binary encoded file.
    The optional attribute ID is for a unique ID of this data block."""
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, id=None, name=None, description=None, fileName=None, mimeType=None, data=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = "dcc"
        self.id = _cast(None, id)
        self.id_nsprefix_ = None
        self.name = name
        self.name_nsprefix_ = "dcc"
        self.description = description
        self.description_nsprefix_ = "dcc"
        self.fileName = fileName
        self.fileName_nsprefix_ = "dcc"
        self.mimeType = mimeType
        self.mimeType_nsprefix_ = "dcc"
        self.data = data
        self.data_nsprefix_ = "dcc"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, byteDataType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if byteDataType.subclass:
            return byteDataType.subclass(*args_, **kwargs_)
        else:
            return byteDataType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name
    def get_description(self):
        return self.description
    def set_description(self, description):
        self.description = description
    def get_fileName(self):
        return self.fileName
    def set_fileName(self, fileName):
        self.fileName = fileName
    def get_mimeType(self):
        return self.mimeType
    def set_mimeType(self, mimeType):
        self.mimeType = mimeType
    def get_data(self):
        return self.data
    def set_data(self, data):
        self.data = data
    def get_id(self):
        return self.id
    def set_id(self, id):
        self.id = id
    def hasContent_(self):
        if (
            self.name is not None or
            self.description is not None or
            self.fileName is not None or
            self.mimeType is not None or
            self.data is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:dcc="https://ptb.de/dcc"', name_='byteDataType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('byteDataType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'byteDataType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='byteDataType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='byteDataType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='byteDataType'):
        if self.id is not None and 'id' not in already_processed:
            already_processed.add('id')
            outfile.write(' id=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.id), input_name='id')), ))
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:dcc="https://ptb.de/dcc"', name_='byteDataType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.name is not None:
            namespaceprefix_ = self.name_nsprefix_ + ':' if (UseCapturedNS_ and self.name_nsprefix_) else ''
            self.name.export(outfile, level, namespaceprefix_, namespacedef_='', name_='name', pretty_print=pretty_print)
        if self.description is not None:
            namespaceprefix_ = self.description_nsprefix_ + ':' if (UseCapturedNS_ and self.description_nsprefix_) else ''
            self.description.export(outfile, level, namespaceprefix_, namespacedef_='', name_='description', pretty_print=pretty_print)
        if self.fileName is not None:
            namespaceprefix_ = self.fileName_nsprefix_ + ':' if (UseCapturedNS_ and self.fileName_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sfileName>%s</%sfileName>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.fileName), input_name='fileName')), namespaceprefix_ , eol_))
        if self.mimeType is not None:
            namespaceprefix_ = self.mimeType_nsprefix_ + ':' if (UseCapturedNS_ and self.mimeType_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%smimeType>%s</%smimeType>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.mimeType), input_name='mimeType')), namespaceprefix_ , eol_))
        if self.data is not None:
            namespaceprefix_ = self.data_nsprefix_ + ':' if (UseCapturedNS_ and self.data_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sdata>%s</%sdata>%s' % (namespaceprefix_ , self.gds_format_base64(self.data, input_name='data'), namespaceprefix_ , eol_))
    def to_etree(self, parent_element=None, name_='byteDataType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{https://ptb.de/dcc}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{https://ptb.de/dcc}' + name_, nsmap=nsmap_)
        if self.id is not None:
            element.set('id', self.gds_format_string(self.id))
        if self.name is not None:
            name_ = self.name
            name_.to_etree(element, name_='name', mapping_=mapping_, nsmap_=nsmap_)
        if self.description is not None:
            description_ = self.description
            description_.to_etree(element, name_='description', mapping_=mapping_, nsmap_=nsmap_)
        if self.fileName is not None:
            fileName_ = self.fileName
            etree_.SubElement(element, '{https://ptb.de/dcc}fileName').text = self.gds_format_string(fileName_)
        if self.mimeType is not None:
            mimeType_ = self.mimeType
            etree_.SubElement(element, '{https://ptb.de/dcc}mimeType').text = self.gds_format_string(mimeType_)
        if self.data is not None:
            data_ = self.data
            etree_.SubElement(element, '{https://ptb.de/dcc}data').text = self.gds_format_base64(data_)
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
        value = find_attr_value_('id', node)
        if value is not None and 'id' not in already_processed:
            already_processed.add('id')
            self.id = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'name':
            obj_ = textType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.name = obj_
            obj_.original_tagname_ = 'name'
        elif nodeName_ == 'description':
            obj_ = textType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.description = obj_
            obj_.original_tagname_ = 'description'
        elif nodeName_ == 'fileName':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'fileName')
            value_ = self.gds_validate_string(value_, node, 'fileName')
            self.fileName = value_
            self.fileName_nsprefix_ = child_.prefix
        elif nodeName_ == 'mimeType':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'mimeType')
            value_ = self.gds_validate_string(value_, node, 'mimeType')
            self.mimeType = value_
            self.mimeType_nsprefix_ = child_.prefix
        elif nodeName_ == 'data':
            sval_ = child_.text
            if sval_ is not None:
                try:
                    bval_ = base64.b64decode(sval_)
                except (TypeError, ValueError) as exp:
                    raise_parse_error(child_, 'requires base64 encoded string: %s' % exp)
                bval_ = self.gds_validate_base64(bval_, node, 'data')
            else:
                bval_ = None
            self.data = bval_
            self.data_nsprefix_ = child_.prefix
# end class byteDataType


class formulaType(GeneratedsSuper):
    """This data block is used to add formulas and equations to the measurement
    result section of the DCC.
    A formula is expected to by written by means of the LaTeX ams math
    formalism. All units in the
    LaTeX expression must follow the siunitx LaTeX standard.
    The formula is written to the siunitx element.
    The optional attribute ID is for a unique ID of this block."""
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, lang=None, id=None, siunitx=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = "dcc"
        self.lang = _cast(None, lang)
        self.lang_nsprefix_ = None
        self.id = _cast(None, id)
        self.id_nsprefix_ = None
        self.siunitx = siunitx
        self.siunitx_nsprefix_ = "dcc"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, formulaType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if formulaType.subclass:
            return formulaType.subclass(*args_, **kwargs_)
        else:
            return formulaType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_siunitx(self):
        return self.siunitx
    def set_siunitx(self, siunitx):
        self.siunitx = siunitx
    def get_lang(self):
        return self.lang
    def set_lang(self, lang):
        self.lang = lang
    def get_id(self):
        return self.id
    def set_id(self, id):
        self.id = id
    def hasContent_(self):
        if (
            self.siunitx is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:dcc="https://ptb.de/dcc"', name_='formulaType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('formulaType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'formulaType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='formulaType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='formulaType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='formulaType'):
        if self.lang is not None and 'lang' not in already_processed:
            already_processed.add('lang')
            outfile.write(' lang=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.lang), input_name='lang')), ))
        if self.id is not None and 'id' not in already_processed:
            already_processed.add('id')
            outfile.write(' id=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.id), input_name='id')), ))
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:dcc="https://ptb.de/dcc"', name_='formulaType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.siunitx is not None:
            namespaceprefix_ = self.siunitx_nsprefix_ + ':' if (UseCapturedNS_ and self.siunitx_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%ssiunitx>%s</%ssiunitx>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.siunitx), input_name='siunitx')), namespaceprefix_ , eol_))
    def to_etree(self, parent_element=None, name_='formulaType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{https://ptb.de/dcc}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{https://ptb.de/dcc}' + name_, nsmap=nsmap_)
        if self.lang is not None:
            element.set('lang', self.gds_format_string(self.lang))
        if self.id is not None:
            element.set('id', self.gds_format_string(self.id))
        if self.siunitx is not None:
            siunitx_ = self.siunitx
            etree_.SubElement(element, '{https://ptb.de/dcc}siunitx').text = self.gds_format_string(siunitx_)
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
        value = find_attr_value_('lang', node)
        if value is not None and 'lang' not in already_processed:
            already_processed.add('lang')
            self.lang = value
        value = find_attr_value_('id', node)
        if value is not None and 'id' not in already_processed:
            already_processed.add('id')
            self.id = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'siunitx':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'siunitx')
            value_ = self.gds_validate_string(value_, node, 'siunitx')
            self.siunitx = value_
            self.siunitx_nsprefix_ = child_.prefix
# end class formulaType


class xmlType(GeneratedsSuper):
    """This data block is used to add user or application specific XML content
    to the
    measurement result section of the DCC.
    The optional attribute ID is for a unique ID of this block."""
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, anytypeobjs_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = "dcc"
        self.anytypeobjs_ = anytypeobjs_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, xmlType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if xmlType.subclass:
            return xmlType.subclass(*args_, **kwargs_)
        else:
            return xmlType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_anytypeobjs_(self): return self.anytypeobjs_
    def set_anytypeobjs_(self, anytypeobjs_): self.anytypeobjs_ = anytypeobjs_
    def hasContent_(self):
        if (
            self.anytypeobjs_ is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:dcc="https://ptb.de/dcc"', name_='xmlType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('xmlType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'xmlType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='xmlType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='xmlType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='xmlType'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:dcc="https://ptb.de/dcc"', name_='xmlType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if not fromsubclass_:
            if self.anytypeobjs_ is not None:
                content_ = self.anytypeobjs_
                outfile.write(content_)
    def to_etree(self, parent_element=None, name_='xmlType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{https://ptb.de/dcc}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{https://ptb.de/dcc}' + name_, nsmap=nsmap_)
        if self.anytypeobjs_ is not None:
            self.anytypeobjs_.to_etree(element, mapping_=mapping_, nsmap_=nsmap_)
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
        content_ = self.gds_build_any(child_, 'xmlType')
        self.set_anytypeobjs_(content_)
# end class xmlType


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
        self.label_nsprefix_ = None
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
        self.dateTime_nsprefix_ = None
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
    def export(self, outfile, level, namespaceprefix_='si:', namespacedef_='xmlns:si="https://ptb.de/si"', name_='real', pretty_print=True):
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
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='si:', name_='real'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='si:', namespacedef_='xmlns:si="https://ptb.de/si"', name_='real', fromsubclass_=False, pretty_print=True):
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
        self.distribution_nsprefix_ = None
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
    def export(self, outfile, level, namespaceprefix_='si:', namespacedef_='xmlns:si="https://ptb.de/si"', name_='expandedUnc', pretty_print=True):
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
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='si:', name_='expandedUnc'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='si:', namespacedef_='xmlns:si="https://ptb.de/si"', name_='expandedUnc', fromsubclass_=False, pretty_print=True):
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
        self.distribution_nsprefix_ = None
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
    def export(self, outfile, level, namespaceprefix_='si:', namespacedef_='xmlns:si="https://ptb.de/si"', name_='coverageInterval', pretty_print=True):
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
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='si:', name_='coverageInterval'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='si:', namespacedef_='xmlns:si="https://ptb.de/si"', name_='coverageInterval', fromsubclass_=False, pretty_print=True):
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
        self.label_nsprefix_ = None
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
        self.dateTime_nsprefix_ = None
        self.uncertainty = uncertainty
        self.validate_uncertaintyValueType(self.uncertainty)
        self.uncertainty_nsprefix_ = "si"
        self.distribution = distribution
        self.distribution_nsprefix_ = None
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
    def export(self, outfile, level, namespaceprefix_='si:', namespacedef_='xmlns:si="https://ptb.de/si"', name_='constant', pretty_print=True):
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
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='si:', name_='constant'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='si:', namespacedef_='xmlns:si="https://ptb.de/si"', name_='constant', fromsubclass_=False, pretty_print=True):
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
        self.label_nsprefix_ = None
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
        self.dateTime_nsprefix_ = None
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
    def export(self, outfile, level, namespaceprefix_='si:', namespacedef_='xmlns:si="https://ptb.de/si"', name_='complex', pretty_print=True):
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
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='si:', name_='complex'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='si:', namespacedef_='xmlns:si="https://ptb.de/si"', name_='complex', fromsubclass_=False, pretty_print=True):
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
        self.column_nsprefix_ = None
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
    def export(self, outfile, level, namespaceprefix_='si:', namespacedef_='xmlns:si="https://ptb.de/si"', name_='covarianceMatrix', pretty_print=True):
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
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='si:', name_='covarianceMatrix'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='si:', namespacedef_='xmlns:si="https://ptb.de/si"', name_='covarianceMatrix', fromsubclass_=False, pretty_print=True):
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
        self.distribution_nsprefix_ = None
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
    def export(self, outfile, level, namespaceprefix_='si:', namespacedef_='xmlns:si="https://ptb.de/si"', name_='ellipsoidalRegion', pretty_print=True):
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
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='si:', name_='ellipsoidalRegion'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='si:', namespacedef_='xmlns:si="https://ptb.de/si"', name_='ellipsoidalRegion', fromsubclass_=False, pretty_print=True):
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
        self.distribution_nsprefix_ = None
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
    def export(self, outfile, level, namespaceprefix_='si:', namespacedef_='xmlns:si="https://ptb.de/si"', name_='rectangularRegion', pretty_print=True):
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
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='si:', name_='rectangularRegion'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='si:', namespacedef_='xmlns:si="https://ptb.de/si"', name_='rectangularRegion', fromsubclass_=False, pretty_print=True):
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
        self.label_nsprefix_ = None
        if isinstance(dateTime, BaseStrType_):
            initvalue_ = datetime_.datetime.strptime(dateTime, '%Y-%m-%dT%H:%M:%S')
        else:
            initvalue_ = dateTime
        self.dateTime = initvalue_
        self.dateTime_nsprefix_ = None
        self.listUnit = listUnit
        self.validate_unitType(self.listUnit)
        self.listUnit_nsprefix_ = "si"
        self.listUnivariateUnc = listUnivariateUnc
        self.listUnivariateUnc_nsprefix_ = "si"
        if real is None:
            self.real = []
        else:
            self.real = real
        self.real_nsprefix_ = None
        self.listUnitPhase = listUnitPhase
        self.listUnitPhase_nsprefix_ = None
        self.listBivariateUnc = listBivariateUnc
        self.listBivariateUnc_nsprefix_ = "si"
        if complex is None:
            self.complex = []
        else:
            self.complex = complex
        self.complex_nsprefix_ = None
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
    def export(self, outfile, level, namespaceprefix_='si:', namespacedef_='xmlns:si="https://ptb.de/si"', name_='list', pretty_print=True):
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
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='si:', name_='list'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='si:', namespacedef_='xmlns:si="https://ptb.de/si"', name_='list', fromsubclass_=False, pretty_print=True):
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
    def export(self, outfile, level, namespaceprefix_='si:', namespacedef_='xmlns:si="https://ptb.de/si"', name_='listUnivariateUnc', pretty_print=True):
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
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='si:', name_='listUnivariateUnc'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='si:', namespacedef_='xmlns:si="https://ptb.de/si"', name_='listUnivariateUnc', fromsubclass_=False, pretty_print=True):
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
    def export(self, outfile, level, namespaceprefix_='si:', namespacedef_='xmlns:si="https://ptb.de/si"', name_='listBivariateUnc', pretty_print=True):
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
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='si:', name_='listBivariateUnc'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='si:', namespacedef_='xmlns:si="https://ptb.de/si"', name_='listBivariateUnc', fromsubclass_=False, pretty_print=True):
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
    def export(self, outfile, level, namespaceprefix_='si:', namespacedef_='xmlns:si="https://ptb.de/si"', name_='hybrid', pretty_print=True):
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
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='si:', name_='hybrid'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='si:', namespacedef_='xmlns:si="https://ptb.de/si"', name_='hybrid', fromsubclass_=False, pretty_print=True):
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


class commentType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, anytypeobjs_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if anytypeobjs_ is None:
            self.anytypeobjs_ = []
        else:
            self.anytypeobjs_ = anytypeobjs_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, commentType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if commentType.subclass:
            return commentType.subclass(*args_, **kwargs_)
        else:
            return commentType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
    def get_anytypeobjs_(self): return self.anytypeobjs_
    def set_anytypeobjs_(self, anytypeobjs_): self.anytypeobjs_ = anytypeobjs_
    def add_anytypeobjs_(self, value): self.anytypeobjs_.append(value)
    def insert_anytypeobjs_(self, index, value): self._anytypeobjs_[index] = value
    def hasContent_(self):
        if (
            self.anytypeobjs_
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:dcc="https://ptb.de/dcc"', name_='commentType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('commentType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'commentType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='commentType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='commentType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='commentType'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:dcc="https://ptb.de/dcc"', name_='commentType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if not fromsubclass_:
            for obj_ in self.anytypeobjs_:
                showIndent(outfile, level, pretty_print)
                outfile.write(obj_)
                outfile.write('\n')
    def to_etree(self, parent_element=None, name_='commentType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{https://ptb.de/dcc}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{https://ptb.de/dcc}' + name_, nsmap=nsmap_)
        for obj_ in self.anytypeobjs_:
            obj_.to_etree(element, mapping_=mapping_, nsmap_=nsmap_)
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
        content_ = self.gds_build_any(child_, 'commentType')
        self.add_anytypeobjs_(content_)
# end class commentType


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
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:dcc="https://ptb.de/dcc"', name_='columnType', pretty_print=True):
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
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:dcc="https://ptb.de/dcc"', name_='columnType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for covariance_ in self.covariance:
            namespaceprefix_ = self.covariance_nsprefix_ + ':' if (UseCapturedNS_ and self.covariance_nsprefix_) else ''
            covariance_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='covariance', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='columnType', mapping_=None, nsmap_=None):
        if parent_element is None:
            element = etree_.Element('{https://ptb.de/dcc}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{https://ptb.de/dcc}' + name_, nsmap=nsmap_)
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
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:dcc="https://ptb.de/dcc" xmlns:si="https://ptb.de/si" ', name_='covarianceType', pretty_print=True):
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
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:dcc="https://ptb.de/dcc" xmlns:si="https://ptb.de/si" ', name_='covarianceType', fromsubclass_=False, pretty_print=True):
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
            element = etree_.Element('{https://ptb.de/dcc}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{https://ptb.de/dcc}' + name_, nsmap=nsmap_)
        if self.value is not None:
            value_ = self.value
            etree_.SubElement(element, '{https://ptb.de/dcc}value').text = self.gds_format_double(value_)
        if self.unit is not None:
            unit_ = self.unit
            etree_.SubElement(element, '{https://ptb.de/dcc}unit').text = self.gds_format_string(unit_)
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
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:dcc="https://ptb.de/dcc" xmlns:si="https://ptb.de/si" ', name_='realType', pretty_print=True):
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
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:dcc="https://ptb.de/dcc" xmlns:si="https://ptb.de/si" ', name_='realType', fromsubclass_=False, pretty_print=True):
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
            element = etree_.Element('{https://ptb.de/dcc}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{https://ptb.de/dcc}' + name_, nsmap=nsmap_)
        if self.label is not None:
            label_ = self.label
            etree_.SubElement(element, '{https://ptb.de/dcc}label').text = self.gds_format_string(label_)
        if self.value is not None:
            value_ = self.value
            etree_.SubElement(element, '{https://ptb.de/dcc}value').text = self.gds_format_double(value_)
        if self.unit is not None:
            unit_ = self.unit
            etree_.SubElement(element, '{https://ptb.de/dcc}unit').text = self.gds_format_string(unit_)
        if self.dateTime is not None:
            dateTime_ = self.dateTime
            etree_.SubElement(element, '{https://ptb.de/dcc}dateTime').text = self.gds_format_datetime(dateTime_)
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
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:dcc="https://ptb.de/dcc" xmlns:si="https://ptb.de/si" ', name_='complexType', pretty_print=True):
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
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:dcc="https://ptb.de/dcc" xmlns:si="https://ptb.de/si" ', name_='complexType', fromsubclass_=False, pretty_print=True):
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
            element = etree_.Element('{https://ptb.de/dcc}' + name_, nsmap=nsmap_)
        else:
            element = etree_.SubElement(parent_element, '{https://ptb.de/dcc}' + name_, nsmap=nsmap_)
        if self.label is not None:
            label_ = self.label
            etree_.SubElement(element, '{https://ptb.de/dcc}label').text = self.gds_format_string(label_)
        if self.valueReal is not None:
            valueReal_ = self.valueReal
            etree_.SubElement(element, '{https://ptb.de/dcc}valueReal').text = self.gds_format_double(valueReal_)
        if self.valueImag is not None:
            valueImag_ = self.valueImag
            etree_.SubElement(element, '{https://ptb.de/dcc}valueImag').text = self.gds_format_double(valueImag_)
        if self.valueMagnitude is not None:
            valueMagnitude_ = self.valueMagnitude
            etree_.SubElement(element, '{https://ptb.de/dcc}valueMagnitude').text = self.gds_format_double(valueMagnitude_)
        if self.valuePhase is not None:
            valuePhase_ = self.valuePhase
            etree_.SubElement(element, '{https://ptb.de/dcc}valuePhase').text = self.gds_format_double(valuePhase_)
        if self.unit is not None:
            unit_ = self.unit
            etree_.SubElement(element, '{https://ptb.de/dcc}unit').text = self.gds_format_string(unit_)
        if self.unitPhase is not None:
            unitPhase_ = self.unitPhase
            etree_.SubElement(element, '{https://ptb.de/dcc}unitPhase').text = self.gds_format_string(unitPhase_)
        if self.dateTime is not None:
            dateTime_ = self.dateTime
            etree_.SubElement(element, '{https://ptb.de/dcc}dateTime').text = self.gds_format_datetime(dateTime_)
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
    'digitalCalibrationCertificate': digitalCalibrationCertificateType,
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
        rootTag = 'digitalCalibrationCertificateType'
        rootClass = digitalCalibrationCertificateType
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
        rootTag = 'digitalCalibrationCertificateType'
        rootClass = digitalCalibrationCertificateType
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
        rootTag = 'digitalCalibrationCertificateType'
        rootClass = digitalCalibrationCertificateType
    rootObj = rootClass.factory()
    rootObj.build(rootNode, gds_collector_=gds_collector)
    if not SaveElementTreeNode:
        rootNode = None
    if not silence:
        sys.stdout.write('<?xml version="1.0" ?>\n')
        rootObj.export(
            sys.stdout, 0, name_=rootTag,
            namespacedef_='xmlns:dcc="https://ptb.de/dcc"')
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
        rootTag = 'digitalCalibrationCertificateType'
        rootClass = digitalCalibrationCertificateType
    rootObj = rootClass.factory()
    rootObj.build(rootNode, gds_collector_=gds_collector)
    # Enable Python to collect the space used by the DOM.
    if not SaveElementTreeNode:
        doc = None
        rootNode = None
    if not silence:
        sys.stdout.write('#from dcc1 import *\n\n')
        sys.stdout.write('import dcc1 as model_\n\n')
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
NamespaceToDefMappings_ = {'https://ptb.de/dcc': [('stringISO3166Type',
                         '../xsd-dcc-master/dcc.xsd',
                         'ST'),
                        ('stringISO639Type', '../xsd-dcc-master/dcc.xsd', 'ST'),
                        ('stringRefType', '../xsd-dcc-master/dcc.xsd', 'ST'),
                        ('digitalCalibrationCertificateType',
                         '../xsd-dcc-master/dcc.xsd',
                         'CT'),
                        ('administrativeDataType',
                         '../xsd-dcc-master/dcc.xsd',
                         'CT'),
                        ('softwareListType', '../xsd-dcc-master/dcc.xsd', 'CT'),
                        ('softwareType', '../xsd-dcc-master/dcc.xsd', 'CT'),
                        ('measuringEquipmentListType',
                         '../xsd-dcc-master/dcc.xsd',
                         'CT'),
                        ('measuringEquipmentType',
                         '../xsd-dcc-master/dcc.xsd',
                         'CT'),
                        ('coreDataType', '../xsd-dcc-master/dcc.xsd', 'CT'),
                        ('equipmentClassType',
                         '../xsd-dcc-master/dcc.xsd',
                         'CT'),
                        ('itemListType', '../xsd-dcc-master/dcc.xsd', 'CT'),
                        ('itemType', '../xsd-dcc-master/dcc.xsd', 'CT'),
                        ('identificationListType',
                         '../xsd-dcc-master/dcc.xsd',
                         'CT'),
                        ('identificationType',
                         '../xsd-dcc-master/dcc.xsd',
                         'CT'),
                        ('calibrationLaboratoryType',
                         '../xsd-dcc-master/dcc.xsd',
                         'CT'),
                        ('respPersonListType',
                         '../xsd-dcc-master/dcc.xsd',
                         'CT'),
                        ('respPersonType', '../xsd-dcc-master/dcc.xsd', 'CT'),
                        ('statementListType',
                         '../xsd-dcc-master/dcc.xsd',
                         'CT'),
                        ('measurementResultListType',
                         '../xsd-dcc-master/dcc.xsd',
                         'CT'),
                        ('measurementResultType',
                         '../xsd-dcc-master/dcc.xsd',
                         'CT'),
                        ('usedMethodListType',
                         '../xsd-dcc-master/dcc.xsd',
                         'CT'),
                        ('usedMethodType', '../xsd-dcc-master/dcc.xsd', 'CT'),
                        ('influenceConditionListType',
                         '../xsd-dcc-master/dcc.xsd',
                         'CT'),
                        ('calibrationLocationListType',
                         '../xsd-dcc-master/dcc.xsd',
                         'CT'),
                        ('calibrationLocationType',
                         '../xsd-dcc-master/dcc.xsd',
                         'CT'),
                        ('conditionType', '../xsd-dcc-master/dcc.xsd', 'CT'),
                        ('resultType', '../xsd-dcc-master/dcc.xsd', 'CT'),
                        ('resultListType', '../xsd-dcc-master/dcc.xsd', 'CT'),
                        ('dataType', '../xsd-dcc-master/dcc.xsd', 'CT'),
                        ('quantityType', '../xsd-dcc-master/dcc.xsd', 'CT'),
                        ('listType', '../xsd-dcc-master/dcc.xsd', 'CT'),
                        ('measurementMetaDataListType',
                         '../xsd-dcc-master/dcc.xsd',
                         'CT'),
                        ('statementMetaDataType',
                         '../xsd-dcc-master/dcc.xsd',
                         'CT'),
                        ('stringWithLangType',
                         '../xsd-dcc-master/dcc.xsd',
                         'CT'),
                        ('locationType', '../xsd-dcc-master/dcc.xsd', 'CT'),
                        ('contactType', '../xsd-dcc-master/dcc.xsd', 'CT'),
                        ('contactNotStrictType',
                         '../xsd-dcc-master/dcc.xsd',
                         'CT'),
                        ('hashType', '../xsd-dcc-master/dcc.xsd', 'CT'),
                        ('textType', '../xsd-dcc-master/dcc.xsd', 'CT'),
                        ('byteDataType', '../xsd-dcc-master/dcc.xsd', 'CT'),
                        ('formulaType', '../xsd-dcc-master/dcc.xsd', 'CT'),
                        ('xmlType', '../xsd-dcc-master/dcc.xsd', 'CT')],
 'https://ptb.de/si': [('unitType',
                        'https://ptb.de/si/v1.3.1/SI_Format.xsd',
                        'ST'),
                       ('unitPhaseType',
                        'https://ptb.de/si/v1.3.1/SI_Format.xsd',
                        'ST'),
                       ('decimalType',
                        'https://ptb.de/si/v1.3.1/SI_Format.xsd',
                        'ST'),
                       ('uncertaintyValueType',
                        'https://ptb.de/si/v1.3.1/SI_Format.xsd',
                        'ST'),
                       ('kValueType',
                        'https://ptb.de/si/v1.3.1/SI_Format.xsd',
                        'ST'),
                       ('probabilityValueType',
                        'https://ptb.de/si/v1.3.1/SI_Format.xsd',
                        'ST')]}

__all__ = [
    "administrativeDataType",
    "byteDataType",
    "calibrationLaboratoryType",
    "calibrationLocationListType",
    "calibrationLocationType",
    "columnType",
    "commentType",
    "complex",
    "complexType",
    "conditionType",
    "constant",
    "contactNotStrictType",
    "contactType",
    "coreDataType",
    "covarianceMatrix",
    "covarianceType",
    "coverageInterval",
    "dataType",
    "digitalCalibrationCertificateType",
    "ellipsoidalRegion",
    "equipmentClassType",
    "expandedUnc",
    "formulaType",
    "hashType",
    "hybrid",
    "identificationListType",
    "identificationType",
    "influenceConditionListType",
    "itemListType",
    "itemType",
    "list",
    "listBivariateUnc",
    "listType",
    "listUnivariateUnc",
    "locationType",
    "measurementMetaDataListType",
    "measurementResultListType",
    "measurementResultType",
    "measuringEquipmentListType",
    "measuringEquipmentType",
    "quantityType",
    "real",
    "realType",
    "rectangularRegion",
    "respPersonListType",
    "respPersonType",
    "resultListType",
    "resultType",
    "softwareListType",
    "softwareType",
    "statementListType",
    "statementMetaDataType",
    "stringWithLangType",
    "textType",
    "usedMethodListType",
    "usedMethodType",
    "xmlType"
]
