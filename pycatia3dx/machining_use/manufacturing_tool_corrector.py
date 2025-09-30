"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class ManufacturingToolCorrector(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     ManufacturingToolCorrector
                | 
                | Interface dedicated to Tool Corrector objects management.
                | Role: This interface offers services to manage mainly the tools
                | parameters.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def get_values(self, o_point: str, o_number: int, o_length_number: int, o_radius_number: int, o_diameter: float, i_unit: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetValues(CATBSTR oPoint,long oNumber,long oLengthNumber,long
                | oRadiusNumber,double oDiameter,long iUnit)
                |     Get the values according to a Corrector. Returns HRESULT.
                | 
                |     Parameters:
                | 
                |         oPoint
                |             : Type point as CATUnicodeString (Ex: P1, ..., P9) 
                |         oNumber
                |             : Corrector number as Integer 
                |         oLengthNumber
                |             : Length Corrector number as Integer 
                |         oRadiusNumber
                |             : Radius Corrector number as Integer 
                |         oDiameter
                |             : Tool diameter for this point as Double

        :param str o_point:
        :param int o_number:
        :param int o_length_number:
        :param int o_radius_number:
        :param float o_diameter:
        :param int i_unit:
        :return: None
        """
        return self.com_object.GetValues(o_point, o_number, o_length_number, o_radius_number, o_diameter, i_unit)

    def set_values(self, i_point: str, i_list_numbers: tuple, i_list_length_numbers: tuple, i_list_radius_numbers: tuple, i_list_diameters: tuple, i_unit: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetValues(CATBSTR iPoint,CATSafeArrayVariant
                | iListNumbers,CATSafeArrayVariant iListLengthNumbers,CATSafeArrayVariant
                | iListRadiusNumbers,CATSafeArrayVariant iListDiameters,long
                | iUnit)
                |     Set the values according to a Corrector. Returns HRESULT.
                | 
                |     Parameters:
                | 
                |         iPoint
                |             : Type point as CATUnicodeString (Ex: P1,... P9) 
                |         iListNumbers
                |             : List of corrector numbers as CATListOfInt 
                |         iListLengthNumbers
                |             : List of corrector numbers as CATListOfInt

        :param str i_point:
        :param tuple i_list_numbers:
        :param tuple i_list_length_numbers:
        :param tuple i_list_radius_numbers:
        :param tuple i_list_diameters:
        :param int i_unit:
        :return: None
        """
        return self.com_object.SetValues(i_point, i_list_numbers, i_list_length_numbers, i_list_radius_numbers, i_list_diameters, i_unit)

    def __repr__(self):
        return f'ManufacturingToolCorrector(name="{ self.name }")'
