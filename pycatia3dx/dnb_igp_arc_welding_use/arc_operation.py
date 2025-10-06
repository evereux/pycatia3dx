"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.system.cat_base_unknown import CATBaseUnknown


class ArcOperation(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     ArcOperation

    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def arc_profile(self) -> CATBaseUnknown:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ArcProfile() As CATBaseUnknown
                |     Gets the Arc profile for the ArcOperation
                | 
                |     Parameters:
                | 
                |         oArcProfile,
                |             ArcProfile for the current ArcOperation [out, IUnknown#Release]
                |             
                | 
                |     Returns:
                |         S_OK on success and E_FAIL on failure. 

        :return: CATBaseUnknown
        """

        return CATBaseUnknown(self.com_object.ArcProfile)

    @arc_profile.setter
    def arc_profile(self, value: CATBaseUnknown):
        """
        :param CATBaseUnknown value:
        """

        self.com_object.ArcProfile = value

    def __repr__(self):
        return f'ArcOperation(name="{ self.name }")'
