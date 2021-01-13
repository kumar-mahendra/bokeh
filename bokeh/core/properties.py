#-----------------------------------------------------------------------------
# Copyright (c) 2012 - 2021, Anaconda, Inc., and Bokeh Contributors.
# All rights reserved.
#
# The full license is in the file LICENSE.txt, distributed with this software.
#-----------------------------------------------------------------------------
''' Provide property types for Bokeh models

Properties are objects that can be assigned as class attributes on Bokeh
models, to provide automatic serialization, validation, and documentation.

This documentation is broken down into the following sections:

.. contents::
    :local:

Overview
--------

There are many property types defined in the module, for example ``Int`` to
represent integral values, ``Seq`` to represent sequences (e.g. lists or
tuples, etc.). Properties can also be combined: ``Seq(Float)`` represents
a sequence of floating point values.

For example, the following defines a model that has integer, string, and
list[float] properties:

.. code-block:: python

    class SomeModel(Model):
        foo = Int
        bar = String(default="something")
        baz = List(Float, help="docs for baz prop")

As seen, properties can be declared as just the property type, e.g.
``foo = Int``, in which case the properties are automatically instantiated
on new Model objects. Or the property can be instantiated on the class,
and configured with default values and help strings.

The properties of this class can be initialized by specifying keyword
arguments to the initializer:

.. code-block:: python

    m = SomeModel(foo=10, bar="a str", baz=[1,2,3,4])

But also by setting the attributes on an instance:

.. code-block:: python

    m.foo = 20

Attempts to set a property to a value of the wrong type will
result in a ``ValueError`` exception:

.. code-block:: python

    >>> m.foo = 2.3
    Traceback (most recent call last):

      << traceback omitted >>

    ValueError: expected a value of type Integral, got 2.3 of type float

Models with properties know how to serialize themselves, to be understood
by BokehJS. Additionally, any help strings provided on properties can be
easily and automatically extracted with the Sphinx extensions in the
:ref:`bokeh.sphinxext` module.


Basic Properties
----------------

.. autoclass:: Alpha
.. autoclass:: Angle
.. autoclass:: Any
.. autoclass:: AnyRef
.. autoclass:: Auto
.. autoclass:: Bool
.. autoclass:: Byte
.. autoclass:: Color
.. autoclass:: Complex
.. autoclass:: DashPattern
.. autoclass:: Date
.. autoclass:: Datetime
.. autoclass:: Either
.. autoclass:: Enum
.. autoclass:: Float
.. autoclass:: FontSize
.. autoclass:: Image
.. autoclass:: Instance
.. autoclass:: Int
.. autoclass:: Interval
.. autoclass:: JSON
.. autoclass:: MarkerType
.. autoclass:: MinMaxBounds
.. autoclass:: NonNegativeInt
.. autoclass:: Percent
.. autoclass:: PositiveInt
.. autoclass:: RGB
.. autoclass:: Regex
.. autoclass:: Size
.. autoclass:: String
.. autoclass:: Struct
.. autoclass:: TimeDelta

Container Properties
--------------------

.. autoclass:: Array
.. autoclass:: ColumnData
.. autoclass:: Dict
.. autoclass:: List
.. autoclass:: RelativeDelta
.. autoclass:: Seq
.. autoclass:: Tuple
.. autoclass:: RestrictedDict

DataSpec Properties
-------------------

.. autoclass:: AlphaSpec
.. autoclass:: AngleSpec
.. autoclass:: ColorSpec
.. autoclass:: DataDistanceSpec
.. autoclass:: DataSpec
.. autoclass:: DistanceSpec
.. autoclass:: FontSizeSpec
.. autoclass:: MarkerSpec
.. autoclass:: NumberSpec
.. autoclass:: PropertyUnitsSpec
.. autoclass:: ScreenDistanceSpec
.. autoclass:: StringSpec
.. autoclass:: UnitsSpec

Helpers
~~~~~~~

.. autofunction:: expr
.. autofunction:: field
.. autofunction:: value

Special Properties
------------------

.. autoclass:: Include
.. autoclass:: Override

Validation-only Properties
--------------------------

.. autoclass:: PandasDataFrame
.. autoclass:: PandasGroupBy

Validation Control
------------------

By default, Bokeh properties perform type validation on values. This helps to
ensure the consistency of any data exchanged between Python and JavaScript, as
well as provide detailed and immediate feedback to users if they attempt to
set values of the wrong type. However, these type checks incur some overhead.
In some cases it may be desirable to turn off validation in specific places,
or even entirely, in order to boost performance. The following API is available
to control when type validation occurs.

.. autoclass:: validate
.. autofunction:: without_property_validation

'''
#-----------------------------------------------------------------------------
# Boilerplate
#-----------------------------------------------------------------------------
import logging # isort:skip
log = logging.getLogger(__name__)

#-----------------------------------------------------------------------------
# Imports
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
# Globals and constants
#-----------------------------------------------------------------------------

__all__ = (
    'Alpha',
    'AlphaSpec',
    'Angle',
    'AngleSpec',
    'Any',
    'AnyRef',
    'Array',
    'Auto',
    'Base64String',
    'Bool',
    'Byte',
    'Color',
    'ColorHex',
    'ColorSpec',
    'ColumnData',
    'Complex',
    'DashPattern',
    'DataDistanceSpec',
    'DataSpec',
    'Date',
    'Datetime',
    'Dict',
    'DistanceSpec',
    'Either',
    'Enum',
    'Factor',
    'Float',
    'FontSize',
    'FontSizeSpec',
    'HatchPatternSpec',
    'HatchPatternType',
    'Image',
    'Include',
    'Instance',
    'Int',
    'Interval',
    'JSON',
    'List',
    'MarkerSpec',
    'MarkerType',
    'MinMaxBounds',
    'NonNegativeInt',
    'Null',
    'NullStringSpec',
    'Nullable',
    'NumberSpec',
    'Override',
    'PandasDataFrame',
    'PandasGroupBy',
    'Percent',
    'PositiveInt',
    'PropertyUnitsSpec',
    'RGB',
    'Regex',
    'RelativeDelta',
    'RestrictedDict',
    'ScreenDistanceSpec',
    'Seq',
    'Size',
    'String',
    'StringSpec',
    'Struct',
    'TimeDelta',
    'Tuple',
    'UnitsSpec',
    'expr',
    'field',
    'validate',
    'value',
    'without_property_validation'
)

#-----------------------------------------------------------------------------
# General API
#-----------------------------------------------------------------------------

from .property.any import Any; Any
from .property.any import AnyRef; AnyRef

from .property.auto import Auto; Auto

from .property.color import Alpha; Alpha
from .property.color import Color; Color
from .property.color import RGB; RGB
from .property.color import ColorHex; ColorHex

from .property.container import Array; Array
from .property.container import ColumnData; ColumnData
from .property.container import Dict; Dict
from .property.container import List; List
from .property.container import Seq; Seq
from .property.container import Tuple; Tuple
from .property.container import RelativeDelta; RelativeDelta
from .property.container import RestrictedDict; RestrictedDict

from .property.dataspec import AlphaSpec; AlphaSpec
from .property.dataspec import AngleSpec; AngleSpec
from .property.dataspec import ColorSpec; ColorSpec
from .property.dataspec import DashPatternSpec; DashPatternSpec
from .property.dataspec import DataSpec; DataSpec
from .property.dataspec import DataDistanceSpec; DataDistanceSpec
from .property.dataspec import DistanceSpec; DistanceSpec
from .property.dataspec import expr; expr
from .property.dataspec import field; field
from .property.dataspec import FontSizeSpec; FontSizeSpec
from .property.dataspec import FontStyleSpec; FontStyleSpec
from .property.dataspec import HatchPatternSpec; HatchPatternSpec
from .property.dataspec import IntSpec; IntSpec
from .property.dataspec import LineCapSpec; LineCapSpec
from .property.dataspec import LineJoinSpec; LineJoinSpec
from .property.dataspec import MarkerSpec; MarkerSpec
from .property.dataspec import NullStringSpec; NullStringSpec
from .property.dataspec import NumberSpec; NumberSpec
from .property.dataspec import PropertyUnitsSpec; PropertyUnitsSpec
from .property.dataspec import ScreenDistanceSpec; ScreenDistanceSpec
from .property.dataspec import StringSpec; StringSpec
from .property.dataspec import TextAlignSpec; TextAlignSpec
from .property.dataspec import TextBaselineSpec; TextBaselineSpec
from .property.dataspec import UnitsSpec; UnitsSpec
from .property.dataspec import value; value

from .property.datetime import Date; Date
from .property.datetime import Datetime; Datetime
from .property.datetime import TimeDelta; TimeDelta

from .property.either import Either; Either
from .property.either import Nullable; Nullable

from .property.enum import Enum; Enum

from .property.include import Include ; Include

from .property.instance import Instance; Instance

from .property.json import JSON; JSON

from .property.numeric import Angle; Angle
from .property.numeric import Byte; Byte
from .property.numeric import Interval; Interval
from .property.numeric import NonNegativeInt; NonNegativeInt
from .property.numeric import Percent; Percent
from .property.numeric import PositiveInt; PositiveInt
from .property.numeric import Size; Size

from .property.override import Override ; Override

from .property.pandas import PandasDataFrame ; PandasDataFrame
from .property.pandas import PandasGroupBy ; PandasGroupBy

from .property.primitive import Bool; Bool
from .property.primitive import Complex; Complex
from .property.primitive import Int; Int
from .property.primitive import Float; Float
from .property.primitive import Null; Null
from .property.primitive import String; String

from .property.string import Base64String; Base64String
from .property.string import Regex; Regex

from .property.struct import Struct; Struct

from .property.visual import DashPattern; DashPattern
from .property.visual import FontSize; FontSize
from .property.visual import HatchPatternType; HatchPatternType
from .property.visual import Image; Image
from .property.visual import MinMaxBounds; MinMaxBounds
from .property.visual import MarkerType; MarkerType

from .property.validation import validate; validate
from .property.validation import without_property_validation; without_property_validation

Factor = Either(String, Tuple(String, String), Tuple(String, String, String))

#-----------------------------------------------------------------------------
# Dev API
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
# Private API
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
# Code
#-----------------------------------------------------------------------------
