"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class SpotDrManufacturingPattern(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SpotDrManufacturingPattern

    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def add_mft(self, i_mft: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub AddMFT(AnyObject iMFT)
                |     Adds a MFT to the Manufacturing Pattern.
                | 
                |     Parameters:
                | 
                |         iMFT
                |             The MFT to be added.

        :param AnyObject i_mft:
        :return: None
        """
        return self.com_object.AddMFT(i_mft.com_object)

    def get_mft(self, i_position: int) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetMFT(short iPosition) As AnyObject
                |     Retrieve the MFT at the given index in the Manufacturing
                |     Pattern.
                | 
                |     Parameters:
                | 
                |         iPosition
                |             Index of the position to consider. 
                |         oMFT
                |             MFT found.

        :param int i_position:
        :return: AnyObject
        """
        return AnyObject(self.com_object.GetMFT(i_position))

    def get_mf_ts(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetMFTs() As CATSafeArrayVariant
                |     Retrieve all the MFTs in the Manufacturing Pattern.
                | 
                |     Parameters:
                | 
                |         oPositions,
                |             Array of CATIABase pointers MFTs in the pattern.

        :return: tuple
        """
        return self.com_object.GetMFTs()

    def get_name(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetName() As CATBSTR
                |     Gets the name of the Manufacturing Pattern.
                | 
                |     Parameters:
                | 
                |         oName
                |             Manufacturing Pattern Name.

        :return: str
        """
        return self.com_object.GetName()

    def get_owner(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetOwner() As AnyObject
                |     Gets the owner of the Manufacturing Pattern.
                | 
                |     Parameters:
                | 
                |         ospParentProduct
                |             Manufacturing Patter Owner.

        :return: AnyObject
        """
        return AnyObject(self.com_object.GetOwner())

    def remove_mft(self, i_position: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub RemoveMFT(short iPosition)
                |     Adds an MFT to the Manufacturing Pattern.
                | 
                |     Parameters:
                | 
                |         iPosition
                |             Index of the position to be removed. 

        :param int i_position:
        :return: None
        """
        return self.com_object.RemoveMFT(i_position)

    def __repr__(self):
        return f'SpotDrManufacturingPattern(name="{ self.name }")'
