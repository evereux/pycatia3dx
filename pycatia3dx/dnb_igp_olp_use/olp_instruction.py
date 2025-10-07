"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.del_resource_builder.rsc_applicative_profile import RscApplicativeProfile
from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.dnb_igp_olp_use.olp_procedure import OLPProcedure
from pycatia3dx.dnb_igp_olp_use.olp_profile import OLPProfile
from pycatia3dx.dnb_igp_olp_use.olp_variable import OLPVariable
from pycatia3dx.types.general import CATVariant


class OLPInstruction(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     OlpInstruction
                | 
                | Represents a single instruction in a task.
                | 
                | This interface can only be used by a translator within the Robotics Off-line
                | Programming (OLP) Download or Upload command.
                | 
                | Example: (VB.NET)
                | 
                |  Dim Instructions As OlpInstructions
                |  Dim Instruction As OlpInstruction = Instructions.Item(1)
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def custom_nrl_text(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property CustomNRLText() As CATBSTR
                |     The custom NRL text for the instruction.
                |     For custom activities and some other activity types, this should be copied
                |     verbatim to the output program on download.

        :return: str
        """

        return self.com_object.CustomNRLText

    @custom_nrl_text.setter
    def custom_nrl_text(self, value: str):
        """
        :param str value:
        """

        self.com_object.CustomNRLText = value

    @property
    def custom_nrl_text_for_convert(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property CustomNRLTextForConvert(CATBSTR iText) (Write Only)
                |     The custom NRL text to use if converted to a custom
                |     instruction.
                |     If the instruction is converted to a custom instruction, (for example due
                |     to parameter CommentWaitSignal) this text will be set as the CustomNRLText.
                |     Otherwise this text is ignored.

        :return: str
        """

        return self.com_object.CustomNRLTextForConvert

    @custom_nrl_text_for_convert.setter
    def custom_nrl_text_for_convert(self, value: str):
        """
        :param str value:
        """

        self.com_object.CustomNRLTextForConvert = value

    @property
    def label(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Label() As CATBSTR
                |     Add a label for the target of a goto instruction.
                | 
                |     This is NOT the name of the instruction, it is the target of a goto
                |     instruction. See OlpGoto.TargetInstruction.

        :return: str
        """

        return self.com_object.Label

    @label.setter
    def label(self, value: str):
        """
        :param str value:
        """

        self.com_object.Label = value

    @property
    def parent_procedure(self) -> OLPProcedure:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ParentProcedure() As OlpProcedure (Read Only)
                |     The procedure this instruction is in.

        :return: OLPProcedure
        """

        return OLPProcedure(self.com_object.ParentProcedure)

    @property
    def profiles(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Profiles() As CATSafeArrayVariant (Read Only)
                |     Get all applicative and user profiles used for this
                |     instruction.

        :return: tuple
        """

        return self.com_object.Profiles

    @property
    def sequence_name(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property SequenceName() As CATBSTR (Read Only)
                |     Get the name of the sequence this instruction is in, if
                |     any.
                |     A sequence is a MoveAlong, Drill-Rivet Sequence, or Paint Sequence. If not
                |     in a sequence, the name is blank.

        :return: str
        """

        return self.com_object.SequenceName

    @property
    def type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Type() As DELOlpInstructionType (Read Only)
                |     The type of the instruction.

        :return: DELOlpInstructionType
        """

        return self.com_object.Type

    @property
    def type_string(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property TypeString() As CATBSTR (Read Only)
                |     The type of the instruction as a string.
                |     Returns the same string as the enum but without the delOlp prefix. For
                |     example if the type is delOlpRobotMotion, this property returns "RobotMotion"

        :return: str
        """

        return self.com_object.TypeString

    def add_profile(self, i_profile: RscApplicativeProfile) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub AddProfile(RscApplicativeProfile iProfile)
                |     Add an applicative or user profile.
                | 
                |     Any profile instances of this type already set on this instruction are
                |     removed, so that only 1 instance of a given profile type is ever set on a
                |     instruction.
                | 
                |     Parameters:
                | 
                |         iProfile
                |             The profile instance to add.

        :param RscApplicativeProfile i_profile:
        :return: None
        """
        return self.com_object.AddProfile(i_profile.com_object)

    def find_variable(self, i_name: str) -> OLPVariable:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func FindVariable(CATBSTR iName) As OlpVariable
                |     Retrieves a variable by name.
                |     The variable must be visible from this instruction. The variable can be an
                |     IO, a local variable, or a constant.
                | 
                |     Parameters:
                | 
                |         iName
                |             The name of the variable to find. 
                | 
                |     Returns:
                |         The variable or NULL if not found.

        :param str i_name:
        :return: OLPVariable
        """
        return OLPVariable(self.com_object.FindVariable(i_name))

    def find_variable_by_address(self, i_addr: str, i_type: int, i_data_type: int, i_direction: int) -> OLPVariable:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func FindVariableByAddress(CATBSTR iAddr,DELOlpVariableType
                | iType,DELOlpDataType iDataType,DELOlpIODirection iDirection) As
                | OlpVariable
                |     Retrieves a variable by address.
                |     The variable must be visible from this instruction. The variable can be an
                |     IO, a local variable, or a constant. If the variable type, data type or
                |     direction don't match, nothing is returned. This way, for example, an input and
                |     an output variable can have the same address.
                | 
                |     Parameters:
                | 
                |         iName
                |             The name of the variable to find. 
                |         iType
                |             The type of variable to find. 
                |         iDataType
                |             The data type of the variable to find. 
                |         iDirection
                |             The direction (in, out) of the variable to find. This is only used
                |             if the variable type is external or procudure IO. 
                | 
                |     Returns:
                |         The variable or NULL if not found.

        :param str i_addr:
        :param int i_type:
        :param int i_data_type:
        :param int i_direction:
        :return: OLPVariable
        """
        return OLPVariable(self.com_object.FindVariableByAddress(i_addr, i_type, i_data_type, i_direction))

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

    def get_parameter_from_parent(self, i_profile_type: str, i_parameter_name: str) -> CATVariant:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetParameterFromParent(CATBSTR iProfileType,CATBSTR iParameterName) As
                | CATVariant
                |     Get a parameter from a profile set on the multi-move sequence that contains
                |     this motion.
                | 
                |     This function will return the value of a specified parameter on a profile
                |     set on the multi-move sequence this motion instruction is contained within. If
                |     no profile type is specified, this function will fail. If no parameter is
                |     specified, this function will fail.
                | 
                |     Parameters:
                | 
                |         iProfileType
                |             The type of profile to check for this parameter. 
                |         iParameterName
                |             The the parameter to get the value of. 
                | 
                |     Returns:
                |         The value.

        :param str i_profile_type:
        :param str i_parameter_name:
        :return: CATVariant
        """
        return self.com_object.GetParameterFromParent(i_profile_type, i_parameter_name)

    def get_parameter_names(self, i_profile_type: str) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetParameterNames(CATBSTR iProfileType) As
                | CATSafeArrayVariant
                |     Get all applicative and user profile parameter names for a profile
                |     type.
                | 
                |     Parameters:
                | 
                |         iProfileType
                |             The applicative profile type. 
                | 
                |     Returns:
                |         The list of parameter names as strings.

        :param str i_profile_type:
        :return: tuple
        """
        return self.com_object.GetParameterNames(i_profile_type)

    def get_profile(self, i_profile_type: str) -> RscApplicativeProfile:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetProfile(CATBSTR iProfileType) As RscApplicativeProfile
                |     Get the applicative or user profile of a specific type.
                | 
                |     Parameters:
                | 
                |         iProfileType
                |             The profile group type as returned by
                |             RscApplicativeProfilesGroup.ProfileType 
                | 
                |     Returns:
                |         The profile. If no profile of this type is set then this value is NULL
                |         (or Nothing) but function succeeds.

        :param str i_profile_type:
        :return: RscApplicativeProfile
        """
        return RscApplicativeProfile(self.com_object.GetProfile(i_profile_type))

    def get_profile_name(self, i_profile_type: str) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetProfileName(CATBSTR iProfileType) As CATBSTR
                |     Get applicative profile instance name.
                | 
                |     Parameters:
                | 
                |         iProfileType
                |             The applicative profile type 
                | 
                |     Returns:
                |         The profile instance name

        :param str i_profile_type:
        :return: str
        """
        return self.com_object.GetProfileName(i_profile_type)

    def get_profile_name_from_parent(self, i_profile_type: str) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetProfileNameFromParent(CATBSTR iProfileType) As CATBSTR
                |     Get the name of the profile of a specified type on the multi-move sequence
                |     that contains this motion.
                | 
                |     This function will return the name of the profile of a specified type on
                |     the multi-move sequence that contains this motion. If there is no profile of
                |     the specified type set on the sequence, or if there is no sequence associated
                |     with the target, it will return "".
                | 
                |     Parameters:
                | 
                |         iProfileType
                |             The type of profile to find the name of. 
                | 
                |     Returns:
                |         The name of the profile set on the parent sequence.

        :param str i_profile_type:
        :return: str
        """
        return self.com_object.GetProfileNameFromParent(i_profile_type)

    def get_profile_olp(self, i_profile_type: str) -> OLPProfile:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetProfileOlp(CATBSTR iProfileType) As OlpProfile
                |     Get a applicative or user profile.
                | 
                |     Parameters:
                | 
                |         iProfileType
                |             The type of profile to return. 
                | 
                |     Returns:
                |         The profile. Only 1 instance of a profile can be assigned to a motion.

        :param str i_profile_type:
        :return: OLPProfile
        """
        return OLPProfile(self.com_object.GetProfileOlp(i_profile_type))

    def is_profile_set(self, i_profile_type: str) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func IsProfileSet(CATBSTR iProfileType) As boolean
                |     Identify if profile type is set.
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

    def is_profile_set_on_parent(self, i_profile_type: str) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func IsProfileSetOnParent(CATBSTR iProfileType) As boolean
                |     Check whether a profile is active on the multi-move sequence that contains
                |     this motion.
                | 
                |     This function will return True if the profile type specified is set on the
                |     multi-move sequence this motion instruction is contained within. It will return
                |     False if the profile type is not set or if there is no multi-move sequence
                |     associated with the motion.
                | 
                |     Parameters:
                | 
                |         iProfileType
                |             The type of profile to check for. 
                | 
                |     Returns:
                |         the boolean for whether or not the profile is set.

        :param str i_profile_type:
        :return: bool
        """
        return self.com_object.IsProfileSetOnParent(i_profile_type)

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

    def set_profile_name(self, i_profile_type: str, i_profile_name: str, i_match: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetProfileName(CATBSTR iProfileType,CATBSTR iProfileName,boolean
                | iMatch)
                |     Get applicative profile instance name.
                | 
                |     Parameters:
                | 
                |         iProfileType
                |             The applicative profile type 
                |         iProfileName
                |             The profile instance name 
                |         iMatch
                |             If TRUE use name to find existing applicative profile

        :param str i_profile_type:
        :param str i_profile_name:
        :param bool i_match:
        :return: None
        """
        return self.com_object.SetProfileName(i_profile_type, i_profile_name, i_match)

    def set_profile_olp(self, i_profile: OLPProfile) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetProfileOlp(OlpProfile iProfile)
                |     Set a applicative or user profile.
                | 
                |     Parameters:
                | 
                |         iProfile
                |             The profile. 

        :param OLPProfile i_profile:
        :return: None
        """
        return self.com_object.SetProfileOlp(i_profile.com_object)

    def __repr__(self):
        return f'OLPInstruction(name="{ self.name }")'
