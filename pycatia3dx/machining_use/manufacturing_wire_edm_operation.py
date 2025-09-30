"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.knowledge_interfaces.parameter import Parameter
from pycatia3dx.system.any_object import AnyObject


class ManufacturingWireEdmOperation(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     ManufacturingWireEDMOperation
                | 
                | Interface representing Wire EDM manufacturing operation.
                | Role: This interface offers services to manage Wire EDM manufacturing
                | operation.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def get_offset_parameter(self, i_parameter_name: str, pass_index: int) -> Parameter:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetOffsetParameter(CATBSTR iParameterName,long PassIndex) As
                | Parameter
                |     Returns the Offset associated with the operation set on
                |     iParameterName.
                | 
                |     Parameters:
                | 
                |         iParameterName
                |             Name of the Parameter from which Offset parameter has to be
                |             retrieved. 
                |         PassIndex
                |             index of the Pass from which Offset parameter has to be retrieved.
                |             Only for Finishing and Seperation Pass. 
                | 
                |     Returns:
                |         oOffsetParm Retrieved Offset parameter.

        :param str i_parameter_name:
        :param int pass_index:
        :return: Parameter
        """
        return Parameter(self.com_object.GetOffsetParameter(i_parameter_name, pass_index))

    def get_techno_set_parameter(self, i_parameter_name: str, pass_index: int) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetTechnoSetParameter(CATBSTR iParameterName,long PassIndex) As
                | AnyObject
                |     Returns the Techno Set associated with the operation set on
                |     iParameterName.
                | 
                |     Parameters:
                | 
                |         iParameterName
                |             Name of the Parameter from which Techno Set has to be retrieved.
                |             
                |         PassIndex
                |             index of the Pass from which Techno Set has to be retrieved. Only
                |             for Finishing and Seperation Pass. 
                | 
                |     Returns:
                |         oTechnoSetParm Retrieved Techno Set.

        :param str i_parameter_name:
        :param int pass_index:
        :return: AnyObject
        """
        return AnyObject(self.com_object.GetTechnoSetParameter(i_parameter_name, pass_index))

    def get_wire_edm_features(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetWireEDMFeatures() As CATSafeArrayVariant
                |     Returns the WEDM features associated with the operation.
                | 
                |     Returns:
                |         oListWEDMFeatures Retrieved list of Wire EDM Features set on the
                |         Operation.

        :return: tuple
        """
        return self.com_object.GetWireEDMFeatures()

    def set_techno_set_parameter(self, i_parameter_name: str, pass_index: int, i_techno_set: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetTechnoSetParameter(CATBSTR iParameterName,long PassIndex,AnyObject
                | iTechnoSet)
                |     Sets the Techno Set on operation associated with the
                |     iParameterName.
                | 
                |     Parameters:
                | 
                |         iParameterName
                |             Name of the Parameter on which iTechnoSet has to be set.
                |             
                |         PassIndex
                |             index of the Pass on which iTechnoSet has to be set. Only for
                |             Finishing and Seperation Pass. 
                |         iTechnoSet
                |             Techno Set to be set. 
                | 
                |     Returns:
                |         Status of the method.

        :param str i_parameter_name:
        :param int pass_index:
        :param AnyObject i_techno_set:
        :return: None
        """
        return self.com_object.SetTechnoSetParameter(i_parameter_name, pass_index, i_techno_set.com_object)

    def __repr__(self):
        return f'ManufacturingWireEdmOperation(name="{ self.name }")'
