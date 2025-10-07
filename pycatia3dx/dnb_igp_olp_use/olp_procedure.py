"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.del_resource_builder.rsc_applicative_profile import RscApplicativeProfile
from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.dnb_igp_olp_use.olp_ast_node import OLPAstNode
from pycatia3dx.dnb_igp_olp_use.olp_instructions import OLPInstructions
from pycatia3dx.dnb_igp_olp_use.olp_motion_groups import OLPMotionGroups
from pycatia3dx.dnb_igp_olp_use.olp_profile import OLPProfile
from pycatia3dx.dnb_igp_olp_use.olp_variables import OLPVariables
from pycatia3dx.types.general import CATVariant


class OLPProcedure(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     OlpProcedure
                | 
                | Represents a robot task or other procedure.
                | 
                | This interface can only be used by a translator within the Robotics Off-line
                | Programming (OLP) Download or Upload command.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def ast(self) -> OLPAstNode:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property AST() As OlpAstNode
                |     The AST corresponding to this procedure.
                |     Used to identify which portion of the robot program(s) correspond to this
                |     procedure.

        :return: OLPAstNode
        """

        return OLPAstNode(self.com_object.AST)

    @ast.setter
    def ast(self, value: OLPAstNode):
        """
        :param OLPAstNode value:
        """

        self.com_object.AST = value

    @property
    def header(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Header() As CATBSTR
                |     The task header.
                |     This is used to store any header from an uploaded program.

        :return: str
        """

        return self.com_object.Header

    @header.setter
    def header(self, value: str):
        """
        :param str value:
        """

        self.com_object.Header = value

    @property
    def instructions(self) -> OLPInstructions:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Instructions() As OlpInstructions (Read Only)
                |     The instructions contained in the task.
                |     The collection of instructions is in execution order. The logic of the task
                |     is represented as a tree. For example an "IF" instruction contains 2 sub-lists
                |     of instructions: one for the main branch and one for the else branch. In the
                |     following task, Instructions would contain 3 instructions: RobotMotion.1, the
                |     "if", and RobotMotion.4
                | 
                |         Task
                |             RobotMotion.1
                |             if (in1=TRUE)
                |                 RobotMotion.2
                |                 out1=TRUE
                |             else
                |                 RobotMotion.3
                |             RobotMotion.4

        :return: OLPInstructions
        """

        return OLPInstructions(self.com_object.Instructions)

    @property
    def local_variables(self) -> OLPVariables:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property LocalVariables() As OlpVariables (Read Only)
                |     The variables, IO, and constants defined in this
                |     procedure.

        :return: OLPVariables
        """

        return OLPVariables(self.com_object.LocalVariables)

    @property
    def motion_groups(self) -> OLPMotionGroups:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property MotionGroups() As OlpMotionGroups (Read Only)
                |     The motion groups that are controlled by this task.

        :return: OLPMotionGroups
        """

        return OLPMotionGroups(self.com_object.MotionGroups)

    @property
    def nrl_name(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property NRLName() As CATBSTR
                |     The name of the native robot langage procedure.
                |     Translators should set this during download to enable mapping of simulation
                |     tasks to the corresponding native program. If unset, this is inferred from the
                |     OlpIDFixer if used for fixing the NRL program name.

        :return: str
        """

        return self.com_object.NRLName

    @nrl_name.setter
    def nrl_name(self, value: str):
        """
        :param str value:
        """

        self.com_object.NRLName = value

    @property
    def profiles(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Profiles() As CATSafeArrayVariant (Read Only)
                |     Get all applicative and user profiles used for this
                |     procedure.

        :return: tuple
        """

        return self.com_object.Profiles

    @property
    def program_id(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ProgramID() As CATBSTR
                |     The program ID.
                |     This is a string value stored on the task. If a BCD Number is used, this
                |     property should be used to store it.

        :return: str
        """

        return self.com_object.ProgramID

    @program_id.setter
    def program_id(self, value: str):
        """
        :param str value:
        """

        self.com_object.ProgramID = value

    @property
    def program_type(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ProgramType() As CATBSTR
                |     The program type.
                |     This is stored as a string value, but functionality is limited to valid
                |     values. A list of valid values can be retrieved with GetValidTypes.

        :return: str
        """

        return self.com_object.ProgramType

    @program_type.setter
    def program_type(self, value: str):
        """
        :param str value:
        """

        self.com_object.ProgramType = value

    @property
    def task_description(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property TaskDescription() As CATBSTR
                |     The task description.
                |     This is used to store any task information from an uploaded program to be
                |     displayed as the task's description.

        :return: str
        """

        return self.com_object.TaskDescription

    @task_description.setter
    def task_description(self, value: str):
        """
        :param str value:
        """

        self.com_object.TaskDescription = value

    @property
    def template_file_name(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property TemplateFileName() As CATBSTR
                |     The template file name.
                |     This is used to store the file name (without a path) to the file to be used
                |     for a template download.

        :return: str
        """

        return self.com_object.TemplateFileName

    @template_file_name.setter
    def template_file_name(self, value: str):
        """
        :param str value:
        """

        self.com_object.TemplateFileName = value

    def add_profile(self, i_profile: RscApplicativeProfile) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub AddProfile(RscApplicativeProfile iProfile)
                |     Add an applicative or user profile.
                | 
                |     Any profile instances of this type already set on this procedure are
                |     removed, so that only 1 instance of a given profile type is ever set on a
                |     procedure.
                | 
                |     Parameters:
                | 
                |         iProfile
                |             The profile instance to add.

        :param RscApplicativeProfile i_profile:
        :return: None
        """
        return self.com_object.AddProfile(i_profile.com_object)

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

    def get_valid_program_types(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetValidProgramTypes() As CATSafeArrayVariant
                |     Get the list of valid Program Types for ProgramType. This will return a
                |     list of strings.

        :return: tuple
        """
        return self.com_object.GetValidProgramTypes()

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
        return f'OLPProcedure(name="{ self.name }")'
