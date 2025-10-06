"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.del_resource_builder.rsc_applicative_profile import RscApplicativeProfile
from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.dnb_igp_arc_welding_use.arc_weld_csp_profiles import ArcWeldCSPProfiles


class ArcWeldProfileSection(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     ArcWeldProfileSection
                | 
                | Represents an object that is a collection of welding parameters for a section
                | of arc weld.
                | Role: A Section interface allows access to weld parameters that are specific
                | for a particular section of weld trajectory. There are three such sections -
                | Start Weld, Weld and End Weld section. Each section contains a reference to a
                | particular set of weld parameters.
                | 
                | See also:
                |     ArcWeldProfile, ArcWeldCSPProfiles
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def delay_parameter_name(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property DelayParameterName() As CATBSTR (Read Only)
                |     Returns the name of a delay parameter associated with this particular
                |     section of arc weld profile
                | 
                |     Parameters:
                | 
                |         String
                |             delay parameter name
                | 
                |             Example:
                |                 The following example returns the name of a parameter of a
                |                 linked delay profile:
                | 
                |                  String ParamValue = ArcWeldProfile.StartWeld.DelayParameterName

        :return: str
        """

        return self.com_object.DelayParameterName

    @property
    def delay_parameter_value(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property DelayParameterValue() As double (Read Only)
                |     Returns the value of a delay parameter associated with this particular
                |     section of arc weld profile
                | 
                |     Parameters:
                | 
                |         double
                |             delay parameter value
                | 
                |             Example:
                |                 The following example returns a parameter value of a linked
                |                 delay profile:
                | 
                |                  double ParamValue = ArcWeldProfile.StartWeld.DelayParameterValue

        :return: float
        """

        return self.com_object.DelayParameterValue

    @property
    def delay_profile(self) -> RscApplicativeProfile:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property DelayProfile() As RscApplicativeProfile (Read Only)
                |     Returns a delay profile associated with this particular section of arc weld
                |     profile
                | 
                |     Parameters:
                | 
                |         DELMIARscApplicativeProfile
                |             an applicative profile
                | 
                |             Example:
                |                 The following example returns a linked Delay
                |                 profile
                | 
                |                  DELMIARRscApplicativeProfile DelayLinked = ArcWeldProfile.StartWeld.DelayProfile

        :return: RscApplicativeProfile
        """

        return RscApplicativeProfile(self.com_object.DelayProfile)

    @property
    def is_delay_parameter_linked(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property IsDelayParameterLinked() As boolean (Read Only)
                |     Returns a flag that reveals whether a delay parameter is linked or
                |     not.
                | 
                |     Parameters:
                | 
                |         boolean
                |             a flag
                | 
                |             Example:
                |                 The following example returns a collection of
                |                 profiles:
                | 
                |                  boolean DelayLinked = ArcWeldProfile.StartWeld.IsDelayParameterLinked

        :return: bool
        """

        return self.com_object.IsDelayParameterLinked

    @property
    def is_speed_parameter_linked(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property IsSpeedParameterLinked() As boolean (Read Only)
                |     Returns a flag that reveals whether a speed parameter is linked or
                |     not.
                | 
                |     Parameters:
                | 
                |         boolean
                |             a flag
                | 
                |             Example:
                |                 The following example returns a flag that tells whether or not
                |                 a speed parameter is linked:
                | 
                |                  boolean SpeedLinked = ArcWeldProfile.StartWeld.IsSpeedParameterLinked

        :return: bool
        """

        return self.com_object.IsSpeedParameterLinked

    @property
    def profiles(self) -> ArcWeldCSPProfiles:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Profiles() As ArcWeldCSPProfiles (Read Only)
                |     Return a collection of controller-specific profiles.
                | 
                |     Parameters:
                | 
                |         DELMIAArcWeldCSPProfiles
                |             Collection of CSP profiles
                | 
                |             Example:
                |                 The following example returns a collection of
                |                 profiles:
                | 
                |                  DELMIAArcWeldCSPProfiles MyProfiles = ArcWeldProfile.StartWeld.Profiles

        :return: ArcWeldCSPProfiles
        """

        return ArcWeldCSPProfiles(self.com_object.Profiles)

    @property
    def speed_parameter_name(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property SpeedParameterName() As CATBSTR (Read Only)
                |     Returns the name of a speed parameter associated with this particular
                |     section of arc weld profile
                | 
                |     Parameters:
                | 
                |         String
                |             speed parameter name
                | 
                |             Example:
                |                 The following example returns the name of a parameter of a
                |                 linked speed profile:
                | 
                |                  String ParamValue = ArcWeldProfile.StartWeld.SpeedParameterName

        :return: str
        """

        return self.com_object.SpeedParameterName

    @property
    def speed_parameter_value(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property SpeedParameterValue() As double (Read Only)
                |     Returns the value of a speed parameter associated with this particular
                |     section of arc weld profile
                | 
                |     Parameters:
                | 
                |         double
                |             speed parameter value
                | 
                |             Example:
                |                 The following example returns a parameter value of a linked
                |                 speed profile:
                | 
                |                  double ParamValue = ArcWeldProfile.StartWeld.SpeedParameterValue

        :return: float
        """

        return self.com_object.SpeedParameterValue

    @property
    def speed_profile(self) -> RscApplicativeProfile:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property SpeedProfile() As RscApplicativeProfile (Read Only)
                |     Returns a speed profile associated with this particular section of arc weld
                |     profile
                | 
                |     Parameters:
                | 
                |         DELMIARscApplicativeProfile
                |             an applicative profile
                | 
                |             Example:
                |                 The following example returns a linked speed
                |                 profile
                | 
                |                  DELMIARRscApplicativeProfile SpeedLinked = ArcWeldProfile.StartWeld.SpeedProfile

        :return: RscApplicativeProfile
        """

        return RscApplicativeProfile(self.com_object.SpeedProfile)

    def link_delay_profile(self, i_profile: RscApplicativeProfile, i_parameter_name: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub LinkDelayProfile(RscApplicativeProfile iProfile,CATBSTR
                | iParameterName)
                |     Creates a link between the delay value for this section and the delay
                |     parameter of a selected controller specific profile
                | 
                |     Parameters:
                | 
                |         DELMIARscApplicativeProfile
                |             controller specific profile to be used as a link 
                |         CATBSTR
                |             name of the parameter that belongs to the CSP profile, of type
                |             TIME, whose value will be used as a reference
                |             delay.
                | 
                |             Example:
                |                 The following example establishes a link between the reference
                |                 delay and the controller selected profile (CSP) that is associated with this
                |                 section of the arc profile
                | 
                |                   ArcWeldProfile.StartWeld.LinkDelayProfile MyCSPProfile,
                |                   "DelayParameterName"

        :param RscApplicativeProfile i_profile:
        :param str i_parameter_name:
        :return: None
        """
        return self.com_object.LinkDelayProfile(i_profile.com_object, i_parameter_name)

    def link_speed_profile(self, i_profile: RscApplicativeProfile, i_parameter_name: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub LinkSpeedProfile(RscApplicativeProfile iProfile,CATBSTR
                | iParameterName)
                |     Creates a link between the speed value for this section and the speed
                |     parameter of a selected controller specific profile
                | 
                |     Parameters:
                | 
                |         DELMIARscApplicativeProfile
                |             controller specific profile to be used as a link 
                |         CATBSTR
                |             name of the parameter that belongs to the CSP profile, of type
                |             SPEED, whose value will be used as a reference
                |             speed.
                | 
                |             Example:
                |                 The following example establishes a link between the reference
                |                 speed and the controller selected profile (CSP) that is associated with this
                |                 section of the arc profile
                | 
                |                   ArcWeldProfile.StartWeld.LinkSpeedProfile MyCSPProfile,
                |                   "SpeedParameterName"

        :param RscApplicativeProfile i_profile:
        :param str i_parameter_name:
        :return: None
        """
        return self.com_object.LinkSpeedProfile(i_profile.com_object, i_parameter_name)

    def __repr__(self):
        return f'ArcWeldProfileSection(name="{ self.name }")'
