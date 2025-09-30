"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class ManufacturingToolCompensation(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     ManufacturingToolCompensation
                | 
                | Interface dedicated to Compensation management on Tool
                | objects.
                | Role: This interface offers services to manage mainly the compensation
                | parameters.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def add_corrector(self, i_point: str, i_number: int, i_length_number: int, i_radius_number: int, i_diameter: float, i_unit: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub AddCorrector(CATBSTR iPoint,long iNumber,long iLengthNumber,long
                | iRadiusNumber,double iDiameter,long iUnit)
                |     Create and add a corrector on compensation parameters

        :param str i_point:
        :param int i_number:
        :param int i_length_number:
        :param int i_radius_number:
        :param float i_diameter:
        :param int i_unit:
        :return: None
        """
        return self.com_object.AddCorrector(i_point, i_number, i_length_number, i_radius_number, i_diameter, i_unit)

    def add_corrector_object(self, i_corrector: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub AddCorrectorObject(AnyObject iCorrector)
                |     Add the defined corrector on the compensation parameters Returns
                |     HRESULT.
                | 
                |     Parameters:
                | 
                |         iCorrector
                |             : Corrector to add

        :param AnyObject i_corrector:
        :return: None
        """
        return self.com_object.AddCorrectorObject(i_corrector.com_object)

    def get_corrector_from_corrector_number(self, i_number: int) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetCorrectorFromCorrectorNumber(long iNumber) As
                | AnyObject
                |     Read corrector from a corrector number Returns HRESULT.
                | 
                |     Parameters:
                | 
                |         iNumber
                |             : Corrector number as Integer 
                |         oCorrector
                |             : Associated Corrector

        :param int i_number:
        :return: AnyObject
        """
        return AnyObject(self.com_object.GetCorrectorFromCorrectorNumber(i_number))

    def get_correctors(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetCorrectors() As CATSafeArrayVariant
                |     Get the list of defined correctors on the compensation parameters Returns
                |     HRESULT.
                | 
                |     Parameters:
                | 
                |         oListCorrectors
                |             : List of correctors

        :return: tuple
        """
        return self.com_object.GetCorrectors()

    def get_diameter_value_from_corrector_number(self, i_number: int) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetDiameterValueFromCorrectorNumber(long iNumber) As
                | double
                |     Read Diameter corrector value from a corrector number Returns
                |     HRESULT.
                | 
                |     Parameters:
                | 
                |         iNumber
                |             : Corrector number as Integer 
                |         oDiameter
                |             : Diameter value as Double

        :param int i_number:
        :return: float
        """
        return self.com_object.GetDiameterValueFromCorrectorNumber(i_number)

    def get_distance_from_corrector_number(self, i_number: int) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetDistanceFromCorrectorNumber(long iNumber) As double
                |     Get Distance from Tool Tip to compensated Point from a corrector number
                |     along Tool Axis Returns HRESULT.
                | 
                |     Parameters:
                | 
                |         iNumber
                |             : Corrector number as Integer 
                |         oDistance
                |             : Distance between tool tip and corrector point as Double

        :param int i_number:
        :return: float
        """
        return self.com_object.GetDistanceFromCorrectorNumber(i_number)

    def get_length_number_from_corrector_number(self, i_number: int) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetLengthNumberFromCorrectorNumber(long iNumber) As long
                |     Read length corrector Number from a corrector number Returns
                |     HRESULT.
                | 
                |     Parameters:
                | 
                |         iNumber
                |             : Corrector number as Integer 
                |         oLengthNumber
                |             : Length corrector number as Integer

        :param int i_number:
        :return: int
        """
        return self.com_object.GetLengthNumberFromCorrectorNumber(i_number)

    def get_point_from_corrector_number(self, i_number: int) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetPointFromCorrectorNumber(long iNumber) As CATBSTR
                |     Read corrector point from a corrector number Returns
                |     HRESULT.
                | 
                |     Parameters:
                | 
                |         iNumber
                |             : Corrector number as Integer 
                |         oPoint
                |             : Point type as CATUnicodeString (Example : P1)

        :param int i_number:
        :return: str
        """
        return self.com_object.GetPointFromCorrectorNumber(i_number)

    def get_radius_number_from_corrector_number(self, i_number: int) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetRadiusNumberFromCorrectorNumber(long iNumber) As long
                |     Read radius corrector Number from a corrector number Returns
                |     HRESULT.
                | 
                |     Parameters:
                | 
                |         iNumber
                |             : Corrector number as Integer 
                |         oRadiusNumber
                |             : Radius corrector number as Integer

        :param int i_number:
        :return: int
        """
        return self.com_object.GetRadiusNumberFromCorrectorNumber(i_number)

    def remove_corrector(self, i_corrector: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub RemoveCorrector(AnyObject iCorrector)
                |     Remove the defined corrector from the compensation parameters Returns
                |     HRESULT.
                | 
                |     Parameters:
                | 
                |         iCorrector
                |             : Corrector to remove

        :param AnyObject i_corrector:
        :return: None
        """
        return self.com_object.RemoveCorrector(i_corrector.com_object)

    def remove_correctors(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub RemoveCorrectors()
                |     Remove all the defined correctors from the compensation parameters Returns
                |     HRESULT.

        :return: None
        """
        return self.com_object.RemoveCorrectors()

    def set_default_corrector(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetDefaultCorrector()
                |     Set the default corrector on the Tool. Returns HRESULT.

        :return: None
        """
        return self.com_object.SetDefaultCorrector()

    def __repr__(self):
        return f'ManufacturingToolCompensation(name="{ self.name }")'
