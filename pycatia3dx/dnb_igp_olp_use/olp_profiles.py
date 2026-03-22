"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.collection import Collection
from pycatia3dx.dnb_igp_olp_use.olp_profile import OLPProfile
from pycatia3dx.types.general import CATVariant


class OLPProfiles(Collection):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     OlpProfiles
                | 
                | A collection of 1 type of profile.
                | 
                | This interface can only be used by a translator within the Robotics Off-line
                | Programming (OLP) Download or Upload command.
                | This object can be retrieved from a OlpController.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=OLPProfile)
        self.com_object = com_object

    @property
    def current_profile(self) -> OLPProfile:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property CurrentProfile() As OlpProfile
                |     The current active profile.

        :return: OLPProfile
        """

        return OLPProfile(self.com_object.CurrentProfile)

    @current_profile.setter
    def current_profile(self, value: OLPProfile):
        """
        :param OLPProfile value:
        """

        self.com_object.CurrentProfile = value

    def exists_profile(self, i_name: str, o_profile: OLPProfile) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func ExistsProfile(CATBSTR iName,OlpProfile oProfile) As
                | boolean
                |     Get a profile by name.
                | 
                |     Parameters:
                | 
                |         iName
                |             The name of the profile. 
                |         oProfile
                |             The retrieved profile. 
                | 
                |     Returns:
                |         True if the profile was found.

        :param str i_name:
        :param OLPProfile o_profile:
        :return: bool
        """
        return self.com_object.ExistsProfile(i_name, o_profile.com_object)

    def get_default_parameter(self, i_profile_type: str, i_parameter_name: str) -> CATVariant:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetDefaultParameter(CATBSTR iProfileType,CATBSTR iParameterName) As
                | CATVariant
                |     Get a default applicative profile parameter value for this profile type or
                |     a profile scoped to this profile.
                | 
                |     Parameters:
                | 
                |         iProfileType
                |             The applicative profile type. If blank than this profile is
                |             assumed. 
                |         iParameterName
                |             The parameter name. 
                | 
                |     Returns:
                |         The parameter value.

        :param str i_profile_type:
        :param str i_parameter_name:
        :return: CATVariant
        """
        return self.com_object.GetDefaultParameter(i_profile_type, i_parameter_name)

    def get_or_create_by_match(self, i_skip_if_defaults: bool) -> OLPProfile:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetOrCreateByMatch(boolean iSkipIfDefaults) As OlpProfile
                |     Create a new profile or get an existing one.
                |     Using the matching feature of the set methods you can use the returned
                |     object to find an existing profile based on its parameter values and then
                |     update other parameter values. If no matching profile exists, then a new one
                |     will automatically be created with the set parameter
                |     values.
                | 
                |     Parameters:
                | 
                |         iSkipIfDefaults
                |             If TRUE then a new profile will not be created if all non-matching
                |             parameters are set to default values. This can be used to reduce the number of
                |             meaningless profiles. For example if you set the index for matching, set
                |             several parameters for not-matching, and set the name for not-matching, then if
                |             all the non-matching parameters are default value and no matching profile is
                |             found based on the index then no new profile will be created. The name is
                |             ignored and will not impact whether a new profile is created or not when this
                |             option is TRUE. 
                | 
                |     Returns:
                |         The profile.

        :param bool i_skip_if_defaults:
        :return: OLPProfile
        """
        return OLPProfile(self.com_object.GetOrCreateByMatch(i_skip_if_defaults))

    def get_or_create_profile(self, i_name: str) -> OLPProfile:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetOrCreateProfile(CATBSTR iName) As OlpProfile
                |     Create a new profile.
                |     If the profile exists, the existing instance is returned.
                | 
                |     Parameters:
                | 
                |         iName
                |             The name of the profile. 
                | 
                |     Returns:
                |         The created profile.

        :param str i_name:
        :return: OLPProfile
        """
        return OLPProfile(self.com_object.GetOrCreateProfile(i_name))

    def get_parameter_names(self, i_profile_type: str) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetParameterNames(CATBSTR iProfileType) As
                | CATSafeArrayVariant
                |     Get all applicative and user profile parameter names for this profile
                |     type.
                |     This returns an empty list for the application (spot, arc, paint, etc) and
                |     standard profiles (motion, accuracy, tool, object frame).
                | 
                |     Parameters:
                | 
                |         iProfileType
                |             The applicative profile type. To get the parameter names for this
                |             direct profile this value is optional. They type can be specified to get any
                |             applicative parameters added to an application or stardard profile.
                |             
                | 
                |     Returns:
                |         The list of parameter names as strings. 

        :param str i_profile_type:
        :return: tuple
        """
        return self.com_object.GetParameterNames(i_profile_type)

    def __repr__(self):
        return f'OLPProfiles(name="{self.name}")'
