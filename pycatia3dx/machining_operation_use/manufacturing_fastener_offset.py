"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class ManufacturingFastenerOffset(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     ManufacturingFastenerOffset
                | 
                | Interface defining fastener offsets.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def get_offset_values(self, i_index: int, o_value: float, o_param_name: str, o_param_sign: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetOffsetValues(long iIndex,double oValue,CATBSTR oParamName,long
                | oParamSign)
                |     Gets the offset value of a given index. (from 1 to 6
                |     x.y.z.rx.ry.rz).
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index from 1 to 6: x.y.z.rx.ry.rz 
                |         oValue
                |             The returned value expressed in meters or radians 
                |         oParamName
                |             The mapping parameter 
                |         oParamSign
                |             The mapping sign (-1 or +1)

        :param int i_index:
        :param float o_value:
        :param str o_param_name:
        :param int o_param_sign:
        :return: None
        """
        return self.com_object.GetOffsetValues(i_index, o_value, o_param_name, o_param_sign)

    def set_offset_param(self, i_index: int, i_param_name: str, i_param_sign: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetOffsetParam(long iIndex,CATBSTR iParamName,long
                | iParamSign)
                |     Sets the mapping parameter of a given index.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index from 1 to 6: x.y.z.rx.ry.rz 
                |         iParamName
                |             The mapping parameter name of manufacturing fasteners
                |             
                |         iParamSign
                |             The mapping sign (-1 or +1)

        :param int i_index:
        :param str i_param_name:
        :param int i_param_sign:
        :return: None
        """
        return self.com_object.SetOffsetParam(i_index, i_param_name, i_param_sign)

    def set_offset_value(self, i_index: int, i_value: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetOffsetValue(long iIndex,double iValue)
                |     Sets the offset value of a given index.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index from 1 to 6: x.y.z.rx.ry.rz 
                |         iValue
                |             The value expressed in meters or radians

        :param int i_index:
        :param float i_value:
        :return: None
        """
        return self.com_object.SetOffsetValue(i_index, i_value)

    def __repr__(self):
        return f'ManufacturingFastenerOffset(name="{ self.name }")'
