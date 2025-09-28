"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-27 12:30:08.885021

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class Unit(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     Unit
                | 
                | Represents CATIAUnit object.
                | This interface allows convertion.
                | 
                | See also:
                |     Units.Item, Dimension.Unit
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def magnitude(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Property Magnitude() As CATBSTR (Read Only)
                |     Returns the magnitude associated to the unit.

        :return: str
        """

        return self.com_object.Magnitude

    @property
    def symbol(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Property Symbol() As CATBSTR (Read Only)
                |     Returns the symbol associated to the unit.

        :return: str
        """

        return self.com_object.Symbol

    def convert_from_mks(self, i_value_in_mks: float) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Func ConvertFromMKS(double iValueInMKS) As double
                |     Convert the initial value (expressed in MKS unit) in its equivalent in the
                |     current unit.
                | 
                |     Parameters:
                | 
                |         iValueInMKS
                |             The initial value in MKS unit. 
                | 
                |     Returns:
                |         The final value in the current unit.

        :param float i_value_in_mks:
        :return: float
        """
        return self.com_object.ConvertFromMKS(i_value_in_mks)

    def convert_from_storage_unit(self, i_value_in_storage_unit: float) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Func ConvertFromStorageUnit(double iValueInStorageUnit) As
                | double
                |     Convert the initial value (expressed in storage unit) in its equivalent in
                |     the current unit.
                | 
                |     Parameters:
                | 
                |         iValueInStorageUnit
                |             The initial value in storage unit. 
                | 
                |     Returns:
                |         oValueInThisUnit The final value in the current unit.

        :param float i_value_in_storage_unit:
        :return: float
        """
        return self.com_object.ConvertFromStorageUnit(i_value_in_storage_unit)

    def convert_to_mks(self, i_value_in_this_unit: float) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Func ConvertToMKS(double iValueInThisUnit) As double
                |     Convert the initial value in its equivalent in MKS unit.
                | 
                |     Parameters:
                | 
                |         iValueInThisUnit
                |             The initial value in the current unit. 
                | 
                |     Returns:
                |         oValueInMKS The final value in the corresponding MKS unit.

        :param float i_value_in_this_unit:
        :return: float
        """
        return self.com_object.ConvertToMKS(i_value_in_this_unit)

    def convert_to_storage_unit(self, i_value_in_this_unit: float) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Func ConvertToStorageUnit(double iValueInThisUnit) As double
                |     Convert the initial value in its equivalent in storage
                |     unit.
                | 
                |     Parameters:
                | 
                |         iValueInThisUnit
                |             The initial value in the current unit. 
                | 
                |     Returns:
                |         oValueInStorageUnit The final value in the corresponding storage unit.

        :param float i_value_in_this_unit:
        :return: float
        """
        return self.com_object.ConvertToStorageUnit(i_value_in_this_unit)

    def __repr__(self):
        return f'Unit(name="{ self.name }")'
