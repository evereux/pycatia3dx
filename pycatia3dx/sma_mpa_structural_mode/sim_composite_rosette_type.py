"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class SimCompositeRosetteType(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimCompositeRosetteType
                | 
                | Represents the Composite Rosette Type object.
                | Given a SimCompositeRosette object, you can retrieve a SimCompositeRosetteType as below: Refer SMAIAMpaCompositeRosette.idl to create/retrieve a SimCompositeRosette. .... Dim myCompositeRosette As SimCompositeRosette .... Dim myCompositeRosetteType As SimCompositeRosetteType Set myCompositeRosetteType = myCompositeRosette.GetRosetteType
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def get_cylindrical_rosette_tranfer_curve(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetCylindricalRosetteTranferCurve() As CATBaseDispatch
                |     Returns the curve used (neutral fiber) in the cylindrical rosette
                |     transfer.
                | 
                |     Returns:
                |         The feature corresponding to the curve used in rosette transfer.

        :return: AnyObject
        """
        return self.com_object.GetCylindricalRosetteTranferCurve()

    def get_cylindrical_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetCylindricalType() As
                | SimCompositeRosetteTransferCylindricalType
                |     Returns the type of the cylindrical rosette transfer.
                | 
                |     Returns:
                |         The type of the rosette transfer.

        :return: int
        """
        return self.com_object.GetCylindricalType()

    def set_cylindrical_rosette_tranfer_curve(self, i_curve: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetCylindricalRosetteTranferCurve(CATBaseDispatch iCurve)
                |     Sets the curve used (neutral fiber) in the cylindrical rosette
                |     transfer.
                | 
                |     Parameters:
                | 
                |         iCurve
                |             [in] The feature corresponding to the curve to be used in rosette
                |             transfer.

        :param AnyObject i_curve:
        :return: None
        """
        return self.com_object.SetCylindricalRosetteTranferCurve(i_curve.com_object)

    def set_cylindrical_type(self, isp_cylindrical_rosette_transfer_type: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetCylindricalType(SimCompositeRosetteTransferCylindricalType
                | ispCylindricalRosetteTransferType)
                |     Sets the type of cylindrical transfer.
                | 
                |     Parameters:
                | 
                |         ispCylindricalRosetteTranferType
                |             [in] The type of the rosette transfer. 

        :param int isp_cylindrical_rosette_transfer_type:
        :return: None
        """
        return self.com_object.SetCylindricalType(isp_cylindrical_rosette_transfer_type)

    def __repr__(self):
        return f'SimCompositeRosetteType(name="{ self.name }")'
