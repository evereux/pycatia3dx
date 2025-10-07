"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class ToleranceUnitBasisValue(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     ToleranceUnitBasisValue
                | 
                | Interface for accessing values of the tolerance unit basis on a
                | TPS.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def set_values(self, i_value1: float, i_value2: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetValues(double iValue1,double iValue2)
                |     Set tolerance unit basis values (in millimeters).
                | 
                |     Parameters:
                | 
                |         oValue1
                |             Positive or equal to -1 which means not valuated. 
                |         oValue2
                |             Positive or equal to -1 which means not valuated.

        :param float i_value1:
        :param float i_value2:
        :return: None
        """
        return self.com_object.SetValues(i_value1, i_value2)

    def values(self, o_value1: float, o_value2: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub Values(double oValue1,double oValue2)
                |     Retrieves tolerance unit basis values (in millimeters).
                | 
                |     Parameters:
                | 
                |         oValue1
                |             Positive or equal to -1 which means not valuated. 
                |         oValue2
                |             Positive or equal to -1 which means not valuated. 

        :param float o_value1:
        :param float o_value2:
        :return: None
        """
        return self.com_object.Values(o_value1, o_value2)

    def __repr__(self):
        return f'ToleranceUnitBasisValue(name="{ self.name }")'
