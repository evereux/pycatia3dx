"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.dnb_igp_olp_use.olp_variable import OLPVariable
from pycatia3dx.types.general import CATVariant


class OLPProfile(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     OlpProfile
                | 
                | A profile.
                | 
                | This interface can only be used by a translator within the Robotics Off-line
                | Programming (OLP) Download or Upload command.
                | 
                | The behavior of this object depends on where it was retrieved from. If the
                | object was retrieved from an OlpRobotMotion or OlpRobotMotionTarget then this
                | object is used to configure the properties of that motion. The parameters
                | specified with the iMatch input equal to TRUE will be used to find an existing
                | profile to reuse for this motion. If no matching profile is found a new one
                | will be created. If the object was retrieved from OlpProfiles then any
                | modifications to this object will change an existing or new profile's values
                | directly.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def index(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Index() As long
                |     Get/Set the profile index.
                |     In some robot languages an index is used to identify the profile. If the
                |     Index property is not set (IndexIsSet returns FALSE), then getting the Index
                |     will fail. If you set the Index, IndexIsSet will automatically return TRUE.

        :return: int
        """

        return self.com_object.Index

    @index.setter
    def index(self, value: int):
        """
        :param int value:
        """

        self.com_object.Index = value

    @property
    def index_set(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property IndexSet() As boolean
                |     Get/Set whether an index is set for the profile.
                |     If not set, then getting the Index property will fail. If you set this
                |     property to TRUE, Index will be initialized to 0.

        :return: bool
        """

        return self.com_object.IndexSet

    @index_set.setter
    def index_set(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.IndexSet = value

    @property
    def is_variable(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property IsVariable() As boolean (Read Only)
                |     Get whether this profile is a variable.

        :return: bool
        """

        return self.com_object.IsVariable

    @property
    def variable(self) -> OLPVariable:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Variable() As OlpVariable (Read Only)
                |     Get the variable this proifle is associated with.
                | 
                |     If the profile is an element of an array the variable with have the
                |     subscripts set.

        :return: OLPVariable
        """

        return OLPVariable(self.com_object.Variable)

    def get_parameter(self, i_profile_type: str, i_parameter_name: str) -> CATVariant:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetParameter(CATBSTR iProfileType,CATBSTR iParameterName) As
                | CATVariant
                |     Get applicative profile parameter value.
                | 
                |     Parameters:
                | 
                |         iProfileType
                |             The applicative profile type 
                |         iParameterName
                |             The parameter name 
                | 
                |     Returns:
                |         The parameter value.

        :param str i_profile_type:
        :param str i_parameter_name:
        :return: CATVariant
        """
        return self.com_object.GetParameter(i_profile_type, i_parameter_name)

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

    def is_profile_set(self, i_profile_type: str) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func IsProfileSet(CATBSTR iProfileType) As boolean
                |     Identify if profile type is set as a child of this
                |     profile.
                | 
                |     Parameters:
                | 
                |         iProfileType
                |             The applicative profile type 
                | 
                |     Returns:
                |         TRUE if profile has be set.

        :param str i_profile_type:
        :return: bool
        """
        return self.com_object.IsProfileSet(i_profile_type)

    def matching_profile_exists(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func MatchingProfileExists() As boolean
                |     Query if a profile already exists.
                |     Compares all parameters set with iMatch=TRUE against existing profiles.
                |     Returns TRUE if a matching profile is found.
                | 
                |     Returns:
                |         TRUE if a match is found.

        :return: bool
        """
        return self.com_object.MatchingProfileExists()

    def set_index(self, i_index: int, i_match: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetIndex(long iIndex,boolean iMatch)
                |     SetIndex and match for a profile.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             the profile index value 
                |         iMatch
                |             determines if the index should be used in finding an existing
                |             profile

        :param int i_index:
        :param bool i_match:
        :return: None
        """
        return self.com_object.SetIndex(i_index, i_match)

    def set_name(self, i_name: str, i_match: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetName(CATBSTR iName,boolean iMatch)
                |     SetName and match for a profile.
                | 
                |     Parameters:
                | 
                |         iName
                |             the profile name 
                |         iMatch
                |             determines if the name should be used in finding an existing
                |             profile

        :param str i_name:
        :param bool i_match:
        :return: None
        """
        return self.com_object.SetName(i_name, i_match)

    def set_parameter(self, i_profile_type: str, i_parameter_name: str, i_value: CATVariant, i_match: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetParameter(CATBSTR iProfileType,CATBSTR iParameterName,CATVariant
                | iValue,boolean iMatch)
                |     Set applicative profile parameter value.
                | 
                |     Parameters:
                | 
                |         iProfileType
                |             The applicative profile type 
                |         iParameterName
                |             The parameter name 
                |         iValue
                |             The parameter value. 
                |         iMatch
                |             If TRUE use parameter to find existing applicative profile

        :param str i_profile_type:
        :param str i_parameter_name:
        :param CATVariant i_value:
        :param bool i_match:
        :return: None
        """
        return self.com_object.SetParameter(i_profile_type, i_parameter_name, i_value, i_match)

    def set_parameters_to_nothing(self, i_profile_type: str, i_match: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetParametersToNothing(CATBSTR iProfileType,boolean
                | iMatch)
                |     Unset or remove all parameters from a child profile type.
                |     In some cases, having the parameters not set (set to Nothing) has a
                |     different meaning than set to a Default value. In this case, you should set all
                |     parameters to nothing for a profile type which should not be set. If no
                |     parameters are set and SetParametersToNothing is NOT called, then the profiles
                |     parameter values are ignored for matching and any value is
                |     valid.
                | 
                |     Parameters:
                | 
                |         iProfileType
                |             The applicative profile type 
                |         iMatch
                |             If TRUE then this profile type must not be linked to an existing
                |             profile for it to match. However if the profile is mandatory or the default
                |             values of the profile have the same meaning as having the profile unset, then a
                |             profile set with default values will also match. 

        :param str i_profile_type:
        :param bool i_match:
        :return: None
        """
        return self.com_object.SetParametersToNothing(i_profile_type, i_match)

    def __repr__(self):
        return f'OLPProfile(name="{ self.name }")'
