"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.dnb_igp_arc_welding_use.arc_weld_profile_section import ArcWeldProfileSection


class ArcWeldProfile(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     ArcWeldProfile
                | 
                | Represents an object that is Arc Welding profile Role: Arc Welding profile
                | contains description of arc welding parameters associated with a particular arc
                | welding trajectory.
                | Each arc weld profile consists of three weld sections (Start Weld, Weld and End
                | Weld) and of a flag that defines the Flying Start status.
                | 
                | See also:
                |     DELMIAArcWeldSection, ArcWeldCSPProfiles
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def controller_name(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ControllerName() As CATBSTR (Read Only)
                |     Returns the name of robot controller that the profile is associated
                |     with
                | 
                |     Parameters:
                | 
                |         CATBSTR
                |             The name of the robot controller
                | 
                |             Example:
                |                 The following example returns a collection of
                |                 profiles:
                | 
                |                   String MyProfiles = ArcWeldProfile.StartWeld.Profiles

        :return: str
        """

        return self.com_object.ControllerName

    @property
    def end_weld(self) -> ArcWeldProfileSection:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property EndWeld() As ArcWeldProfileSection (Read Only)
                |     Returns a reference to End Weld section of Arc Welding
                |     profile.
                | 
                |     Parameters:
                | 
                |         DELMIAArcWeldProfileSection
                |             Reference to End Weld Section
                | 
                |             Example:
                |                 The following example returns a reference to an
                 |                End Weld Section
                |
                |                   DELMIAArcWeldProfileSection MySection = ArcWeldProfile.EndWeld

        :return: ArcWeldProfileSection
        """

        return ArcWeldProfileSection(self.com_object.EndWeld)

    @property
    def flying_start(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property FlyingStart() As boolean
                |     Returns a Flying Start flag.
                | 
                |     Parameters:
                | 
                |         boolean
                |             Flag
                | 
                |             Example:
                |                 The following example returns Flying Start
                |                 flag
                | 
                |                   boolean MyFlag = ArcWeldProfile.FlyingStart

        :return: bool
        """

        return self.com_object.FlyingStart

    @flying_start.setter
    def flying_start(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.FlyingStart = value

    @property
    def start_weld(self) -> ArcWeldProfileSection:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property StartWeld() As ArcWeldProfileSection (Read Only)
                |     Returns a reference to Start Weld section of Arc Welding
                |     profile.
                | 
                |     Parameters:
                | 
                |         DELMIAArcWeldProfileSection
                |             Reference to Start Weld Section
                | 
                |             Example:
                |                 The following example returns a reference to a Start Weld
                |                 Section
                | 
                |                   DELMIAArcWeldProfileSection MySection = ArcWeldProfile.StartWeld

        :return: ArcWeldProfileSection
        """

        return ArcWeldProfileSection(self.com_object.StartWeld)

    @property
    def weld(self) -> ArcWeldProfileSection:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Weld() As ArcWeldProfileSection (Read Only)
                |     Returns a reference to Weld section of Arc Welding
                |     profile.
                | 
                |     Parameters:
                | 
                |         DELMIAArcWeldProfileSection
                |             Reference to Weld Section
                | 
                |             Example:
                |                 The following example returns a reference to a Weld
                |                 Section
                | 
                |                   DELMIAArcWeldProfileSection MySection = ArcWeldProfile.Weld

        :return: ArcWeldProfileSection
        """

        return ArcWeldProfileSection(self.com_object.Weld)

    def __repr__(self):
        return f'ArcWeldProfile(name="{ self.name }")'
