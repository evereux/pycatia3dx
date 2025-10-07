"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class TolerancePerUnitBasisRestrictiveValue(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     TolerancePerUnitBasisRestrictiveValue
                | 
                | Interface for accessing tolerance per unit basis restrictive value on a
                | TPS.
                | (ASME norm only)
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def value(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Value() As double
                |     Retrieves value (in millimeters).
                | 
                |     Parameters:
                | 
                |         oValue
                |             Positive or equal to -1 which means not valuated. 

        :return: float
        """

        return self.com_object.Value

    @value.setter
    def value(self, value: float):
        """
        :param float value:
        """

        self.com_object.Value = value

    def __repr__(self):
        return f'TolerancePerUnitBasisRestrictiveValue(name="{ self.name }")'
