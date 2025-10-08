"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.structure.str_opening import StrOpening


class StrOpeningOnProfile(AnyObject):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     StrOpeningOnProfile
                | 
                | Object to manage Openings on a profile.
                | Role: Allows accessing of opening's data. An opening is created, deleted and
                | retrieved using the CATIAStrOpeningsOnProfile interface, which is implemented
                | for profile object.
                | 
                | See also:
                |     StrOpeningsOnProfile
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def str_opening(self) -> StrOpening:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property StrOpening() As StrOpening (Read Only)
                |     Gets the Structure Opening. (@see CATIAStrOpening)
                | 
                |     Parameters:
                | 
                |         oStrOpening
                |             Opening. 
                | 
                |     Example:
                | 
                |          
                | 
                |               This example Gets the Structure opening.
                |               
                | 
                |               Dim ObjStrOpening As StrOpening
                |               Set ObjStrOpening = oObjSfdOpeningOnProfile.StrOpening

        :return: StrOpening
        """

        return StrOpening(self.com_object.StrOpening)

    def inst_and_spac_for_spacing_offset_std_oop(self, i_instances: int, i_spacing: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub InstAndSpacForSpacingOffsetStdOOP(long iInstances,CATBSTR
                | iSpacing)
                |     Sets the Instances and Spacing for Spacing/Offset Position Strategy of
                |     standard opening on profile.
                | 
                |     Parameters:
                | 
                |         iInstances
                |             Number of instances. 
                |         iSpacing
                |             Spacing between the instances. 
                | 
                |     Example:
                | 
                |          
                | 
                |               This example sets the Instances and spacing for spacing/offset
                |               position strategy of standard opening for
                |               profile.
                |               
                | 
                |               oObjSfdOpeningOnProfile.InstAndSpacForSpacingOffsetStdOOP 2,
                |               "500mm"

        :param int i_instances:
        :param str i_spacing:
        :return: None
        """
        return self.com_object.InstAndSpacForSpacingOffsetStdOOP(i_instances, i_spacing)

    def __repr__(self):
        return f'StrOpeningOnProfile(name="{self.name}")'
