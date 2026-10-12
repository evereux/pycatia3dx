from pycatia3dx.knowledge_interfaces.angle import Angle
from pycatia3dx.knowledge_interfaces.bool_param import BoolParam
from pycatia3dx.knowledge_interfaces.check import Check
from pycatia3dx.knowledge_interfaces.design_table import DesignTable
from pycatia3dx.knowledge_interfaces.dimension import Dimension
from pycatia3dx.knowledge_interfaces.enum_param import EnumParam
from pycatia3dx.knowledge_interfaces.formula import Formula
from pycatia3dx.knowledge_interfaces.int_param import IntParam
from pycatia3dx.knowledge_interfaces.knowledge_activate_object import KnowledgeActivateObject
from pycatia3dx.knowledge_interfaces.law import Law
from pycatia3dx.knowledge_interfaces.length import Length
from pycatia3dx.knowledge_interfaces.list import List
from pycatia3dx.knowledge_interfaces.list_parameter import ListParameter
from pycatia3dx.knowledge_interfaces.parameter import Parameter
from pycatia3dx.knowledge_interfaces.real_param import RealParam
from pycatia3dx.knowledge_interfaces.rule import Rule
from pycatia3dx.knowledge_interfaces.set_of_equation import SetOfEquation
from pycatia3dx.knowledge_interfaces.str_param import StrParam

parameter_and_relation_types = {
    'Angle': Angle,
    'BoolParam': BoolParam,
    'Check': Check,
    'DesignTable': DesignTable,
    'Dimension': Dimension,
    'EnumParam': EnumParam,
    'Formula': Formula,
    'IntParam': IntParam,
    'KnowledgeActivateObject': KnowledgeActivateObject,
    'Law': Law,
    'Length': Length,
    'List': List,
    'ListParameter': ListParameter,
    'Parameter': Parameter,
    'RealParam': RealParam,
    'Rule': Rule,
    'SetOfEquation': SetOfEquation,
    'StrParam': StrParam,
}
