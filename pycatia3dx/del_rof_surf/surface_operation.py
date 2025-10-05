"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.system.cat_base_unknown import CATBaseUnknown


class SurfaceOperation(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SurfaceOperation
                | 
                | Interface to access and manipulate the Surface Operation.
                | Role: This interface provides methods to set/retrieve data related to Surface
                | Operation.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def type(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Type() As CATBSTR (Read Only)
                |     Gets the type of the Surface Operation
                | 
                |     Parameters:
                | 
                |         oType,
                |             gives the operation type. One of the types listed in
                |             DELApprovedOperationTypes.txt + "Weld" 
                | 
                |     Returns:
                |         S_OK on success and E_FAIL on failure.

        :return: str
        """

        return self.com_object.Type

    def get_surface_profile(self, o_surface_profile: CATBaseUnknown) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetSurfaceProfile(CATBaseUnknown oSurfaceProfile)
                |     Gets the Surface profile for the Surface operation
                | 
                |     Parameters:
                | 
                |         oSurfaceProfile,
                |             SurfaceProfile for the current SurfaceOperation.Applicable only for
                |             Servo Gun Surface Operation. 
                | 
                |     Returns:
                |         S_OK on success and E_FAIL on failure.

        :param CATBaseUnknown o_surface_profile:
        :return: None
        """
        return self.com_object.GetSurfaceProfile(o_surface_profile.com_object)

    def get_target(self, op_target: CATBaseUnknown, op_target_owner: CATBaseUnknown) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetTarget(CATBaseUnknown opTarget,CATBaseUnknown
                | opTargetOwner)
                |     Gets the Tag Target corresponding to the Surface Operation
                | 
                |     Parameters:
                | 
                |         opTagTarget,
                |             Tag Target currently set for the Surface Operation
                |             
                |         opTargetOwner,
                |             Occurrence owning the Tag Target 
                | 
                |     Returns:
                |         S_OK on success and E_FAIL on failure.

        :param CATBaseUnknown op_target:
        :param CATBaseUnknown op_target_owner:
        :return: None
        """
        return self.com_object.GetTarget(op_target.com_object, op_target_owner.com_object)

    def set_surface_profile(self, i_surface_profile: CATBaseUnknown) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetSurfaceProfile(CATBaseUnknown iSurfaceProfile)
                |     Sets the Surface profile for the Surface operation
                | 
                |     Parameters:
                | 
                |         iSurfaceProfile,
                |             SurfaceProfile to be set.Applicable only for Servo Gun Surface
                |             Operation. 
                | 
                |     Returns:
                |         S_OK on success and E_FAIL on failure.

        :param CATBaseUnknown i_surface_profile:
        :return: None
        """
        return self.com_object.SetSurfaceProfile(i_surface_profile.com_object)

    def set_target(self, ip_target: CATBaseUnknown, op_target_owner: CATBaseUnknown) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetTarget(CATBaseUnknown ipTarget,CATBaseUnknown
                | opTargetOwner)
                |     Sets the Target for the Surface Operation
                | 
                |     Parameters:
                | 
                |         ipTagTarget,
                |             Tag Target to be set 
                |         pTargetOwner,
                |             Occurrence owning the Tag Target 
                | 
                |     Returns:
                |         S_OK on success and E_FAIL on failure. 

        :param CATBaseUnknown ip_target:
        :param CATBaseUnknown op_target_owner:
        :return: None
        """
        return self.com_object.SetTarget(ip_target.com_object, op_target_owner.com_object)

    def __repr__(self):
        return f'SurfaceOperation(name="{ self.name }")'
