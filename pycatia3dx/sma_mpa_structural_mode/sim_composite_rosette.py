"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.sma_mpa_structural_mode.sim_composite_rosette_type import SimCompositeRosetteType


class SimCompositeRosette(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimCompositeRosette
                | 
                | Represents the Composite Rosette object.
                | Given a SimCompositeParameters object, you can create/retrieve a SimCompositeRosette as below: Refer SMAIAMpaCompositeParameters.idl to see how a SimCompositeParameters is created. .... Dim myCompositeParameters As SimCompositeParameters .... Dim myCompositeRosette As SimCompositeRosette Set myCompositeRosette = myCompositeParameters.CreateRosette or Dim myCompositeRosette As SimCompositeRosette Set myCompositeRosette = myCompositeParameters.GetRosetteByIndex 1 or Dim myCompositeRosette As SimCompositeRosette Set myCompositeRosette = myCompositeParameters.GetRosetteByName "Rosette.1" or Dim myCompositeRosettelist myCompositeRosettelist = myCompositeParameters.GetListOfRosettes ...Loop for listSize = UBound(myCompositeRosettelist) - LBound(myCompositeRosettelist) + 1 if needed.. myCompositeRosette = myCompositeRosettelist(0)
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def get_main_axis(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetMainAxis() As CATBaseDispatch
                |     Retrieves Rosette's Main Axis.
                | 
                |     Returns:
                |         Rosette's Main Axis.

        :return: AnyObject
        """
        return self.com_object.GetMainAxis()

    def get_rosette_cylinderical_transfer(self) -> SimCompositeRosetteType:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetRosetteCylindericalTransfer() As
                | SimCompositeRosetteType
                |     Retrieves the Rosette type for this Rosette.
                | 
                |     Returns:
                |         Rosette transfer type.

        :return: SimCompositeRosetteType
        """
        return SimCompositeRosetteType(self.com_object.GetRosetteCylindericalTransfer())

    def get_rosette_transfer_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetRosetteTransferType() As
                | SimCompositeRosetteTransferType
                |     Retrieves the Rosette type for this Rosette.
                | 
                |     Returns:
                |         Rosette transfer type.

        :return: int
        """
        return self.com_object.GetRosetteTransferType()

    def set_main_axis(self, i_axis_system: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetMainAxis(CATBaseDispatch iAxisSystem)
                |     Sets the Main axis for this Rosette.
                | 
                |     Parameters:
                | 
                |         iAxisSystem
                |             [in] Main Axis for Rosette.

        :param AnyObject i_axis_system:
        :return: None
        """
        return self.com_object.SetMainAxis(i_axis_system.com_object)

    def set_rosette_transfer_type(self, i_rosette_type: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetRosetteTransferType(SimCompositeRosetteTransferType
                | iRosetteType)
                |     Set the Rosette type for this Rosette.
                | 
                |     Parameters:
                | 
                |         iRosetteType
                |             [in] Rosette transfer type. 

        :param SimCompositeRosetteTransferType i_rosette_type:
        :return: None
        """
        return self.com_object.SetRosetteTransferType(i_rosette_type)

    def __repr__(self):
        return f'SimCompositeRosette(name="{ self.name }")'
