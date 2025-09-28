"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-27 12:30:08.885021

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.knowledge_interfaces.bool_param import BoolParam
from pycatia3dx.knowledge_interfaces.dimension import Dimension
from pycatia3dx.knowledge_interfaces.int_param import IntParam
from pycatia3dx.knowledge_interfaces.knowledge_factory import KnowledgeFactory
from pycatia3dx.knowledge_interfaces.list_parameter import ListParameter
from pycatia3dx.knowledge_interfaces.parms_set import ParmsSet
from pycatia3dx.knowledge_interfaces.real_param import RealParam
from pycatia3dx.knowledge_interfaces.str_param import StrParam
from pycatia3dx.system.any_object import AnyObject


class ParametersFactory(KnowledgeFactory):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     KnowledgeIDLItf.KnowledgeFactory
                |                         ParametersFactory
                | 
                | Factory for creating parameters and parameters sets.
                | 
                | See also:
                |     ParmsSet.Factory
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def create_boolean(self, i_name: str, i_value: bool) -> BoolParam:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Func CreateBoolean(CATBSTR iName,boolean iValue) As BoolParam
                |     Creates a boolean parameter.
                | 
                |     Parameters:
                | 
                |         iName
                |             Name of the parameter 
                |         iValue
                |             Value to set the parameter with 
                | 
                |     Returns:
                |         the created parameter

        :param str i_name:
        :param bool i_value:
        :return: BoolParam
        """
        return BoolParam(self.com_object.CreateBoolean(i_name, i_value))

    def create_dimension(self, i_name: str, i_magnitude: str, i_value: float) -> Dimension:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Func CreateDimension(CATBSTR iName,CATBSTR iMagnitude,double iValue) As
                | Dimension
                |     Creates a dimension parameter.
                | 
                |     Parameters:
                | 
                |         iName
                |             Name of the parameter 
                |         iMagnitude
                |             Magnitude of the parameter 
                |         iValue
                |             Value to set the parameter with 
                | 
                |     Returns:
                |         the created parameter

        :param str i_name:
        :param str i_magnitude:
        :param float i_value:
        :return: Dimension
        """
        return Dimension(self.com_object.CreateDimension(i_name, i_magnitude, i_value))

    def create_integer(self, i_name: str, i_value: int) -> IntParam:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Func CreateInteger(CATBSTR iName,long iValue) As IntParam
                |     Creates an integer parameter.
                | 
                |     Parameters:
                | 
                |         iName
                |             Name of the parameter 
                |         iValue
                |             Value to set the parameter with 
                | 
                |     Returns:
                |         the created parameter

        :param str i_name:
        :param int i_value:
        :return: IntParam
        """
        return IntParam(self.com_object.CreateInteger(i_name, i_value))

    def create_list(self, i_name: str) -> ListParameter:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Func CreateList(CATBSTR iName) As ListParameter
                |     Creates a list parameter.
                | 
                |     Parameters:
                | 
                |         iName
                |             Name of the parameter 
                | 
                |     Returns:
                |         the created parameter

        :param str i_name:
        :return: ListParameter
        """
        return ListParameter(self.com_object.CreateList(i_name))

    def create_parameters_set(self, i_name: str) -> ParmsSet:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Func CreateParametersSet(CATBSTR iName) As ParmsSet
                |     Creates a parameters set.
                | 
                |     Parameters:
                | 
                |         iName
                |             Name of the parameters set 
                | 
                |     Returns:
                |         the created parameters set

        :param str i_name:
        :return: ParmsSet
        """
        return ParmsSet(self.com_object.CreateParametersSet(i_name))

    def create_real(self, i_name: str, i_value: float) -> RealParam:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Func CreateReal(CATBSTR iName,double iValue) As RealParam
                |     Creates a real parameter.
                | 
                |     Parameters:
                | 
                |         iName
                |             Name of the parameter 
                |         iValue
                |             Value to set the parameter with 
                | 
                |     Returns:
                |         the created parameter

        :param str i_name:
        :param float i_value:
        :return: RealParam
        """
        return RealParam(self.com_object.CreateReal(i_name, i_value))

    def create_string(self, i_name: str, i_value: str) -> StrParam:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Func CreateString(CATBSTR iName,CATBSTR iValue) As StrParam
                |     Creates a string parameter.
                | 
                |     Parameters:
                | 
                |         iName
                |             Name of the parameter 
                |         iValue
                |             Value to set the parameter with 
                | 
                |     Returns:
                |         the created parameter

        :param str i_name:
        :param str i_value:
        :return: StrParam
        """
        return StrParam(self.com_object.CreateString(i_name, i_value))

    def get_name_to_use_in_relation(self, i_object: AnyObject) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Func GetNameToUseInRelation(AnyObject iObject) As CATBSTR
                |     Returns a correct name of a feature to use it in a
                |     relation.
                | 
                |     Parameters:
                | 
                |         iObject
                |             An object 
                | 
                |     Returns:
                |         The name for that object when used in a relation

        :param AnyObject i_object:
        :return: str
        """
        return self.com_object.GetNameToUseInRelation(i_object.com_object)

    def __repr__(self):
        return f'ParametersFactory(name="{ self.name }")'
