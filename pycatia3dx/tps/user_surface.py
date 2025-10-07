"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.mode.reference import Reference
from pycatia3dx.system.any_object import AnyObject


class UserSurface(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     UserSurface

    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def add_reference(self, i_support: Reference) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub AddReference(Reference iSupport)
                |     Add a surface in a User Surface Support
                | 
                |     Parameters:
                | 
                |         iSupport
                |             The surface that you want to add in the User Surface.

        :param Reference i_support:
        :return: None
        """
        return self.com_object.AddReference(i_support.com_object)

    def add_user_surface(self, i_user_surf: 'UserSurface') -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub AddUserSurface(UserSurface iUserSurf)
                |     Add a User Surface Support in a User Surface Node
                | 
                |     Parameters:
                | 
                |         iUserSurf
                |             The User Surface Support that you want to add in the User Surface.

        :param UserSurface i_user_surf:
        :return: None
        """
        return self.com_object.AddUserSurface(i_user_surf.com_object)

    def __repr__(self):
        return f'UserSurface(name="{ self.name }")'
