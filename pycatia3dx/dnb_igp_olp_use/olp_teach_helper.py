"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.interfaces.service import Service
from pycatia3dx.dnb_igp_olp_use.olp_ast_branch import OLPAstBranch
from pycatia3dx.dnb_igp_olp_use.olp_ast_node import OLPAstNode
from pycatia3dx.dnb_igp_olp_use.olp_custom_command import OLPCustomCommand
from pycatia3dx.dnb_igp_olp_use.olp_instruction import OLPInstruction
from pycatia3dx.dnb_igp_olp_use.olp_procedure import OLPProcedure


class OLPTeachHelper(Service):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     InfInterfaces.Service
                |                         OlpTeachHelper
                | 
                | Native Robot Language(NRL) Teach customization.
                | 
                | This interface can only be used by a translator within the Robotics Off-line
                | Programming (OLP) NRL Teach command.
                | This interface is used to customize the commands available in NRL teach and to
                | retrieve information about the state of NRL teach when one of those commands is
                | executed.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def current_ast_instruction(self) -> OLPAstNode:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property CurrentAstInstruction() As OlpAstNode (Read Only)
                |     The AST node for the current line selected in NRL teach.
                |     This will return NULL if there is no instruction selected.

        :return: OLPAstNode
        """

        return OLPAstNode(self.com_object.CurrentAstInstruction)

    @property
    def current_ast_procedure(self) -> OLPAstBranch:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property CurrentAstProcedure() As OLPAstBranch (Read Only)
                |     The AST node for the current task selected in NRL teach.

        :return: OLPAstBranch
        """

        return OLPAstBranch(self.com_object.CurrentAstProcedure)

    @property
    def current_command(self) -> OLPCustomCommand:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property CurrentCommand() As OlpCustomCommand (Read Only)
                |     The command currently being executed.
                |     This will only return a valid value during the call to MacroRunCommand.
                |     Otherwise, a NULL value is returned.

        :return: OLPCustomCommand
        """

        return OLPCustomCommand(self.com_object.CurrentCommand)

    @property
    def current_instruction(self) -> OLPInstruction:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property CurrentInstruction() As OlpInstruction (Read Only)
                |     The instruction selected in Teach.
                |     This will return NULL if there is no instruction selected.

        :return: OLPInstruction
        """

        return OLPInstruction(self.com_object.CurrentInstruction)

    @property
    def current_procedure(self) -> OLPProcedure:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property CurrentProcedure() As OlpProcedure (Read Only)
                |     The task displayed in Teach.

        :return: OLPProcedure
        """

        return OLPProcedure(self.com_object.CurrentProcedure)

    @property
    def edited_ast_nodes_new(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property EditedAstNodesNew() As CATSafeArrayVariant (Read
                | Only)
                |     The value of the AST node(s) after they were edited by the user. All
                |     objects in the list are of type OlpAstNode.

        :return: tuple
        """

        return self.com_object.EditedAstNodesNew

    @property
    def edited_ast_nodes_previous(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property EditedAstNodesPrevious() As CATSafeArrayVariant (Read
                | Only)
                |     The value of the AST node(s) before they were edited by the user. All
                |     objects in the list are of type OlpAstNode.

        :return: tuple
        """

        return self.com_object.EditedAstNodesPrevious

    @property
    def is_teach_active(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property IsTeachActive() As boolean (Read Only)
                |     Returns TRUE when teach is active. For example when the current download is
                |     performed for display in NRL Teach. Used in MacroDownload.

        :return: bool
        """

        return self.com_object.IsTeachActive

    @property
    def logical_keywords(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property LogicalKeywords(CATSafeArrayVariant iKeywords) (Write
                | Only)
                |     Set the list logical keywords to be highlighted in NRL
                |     teach.
                |     Each value must be a string. Normally this is keywords like IF, WHILE, FOR,
                |     etc. which are colored in blue. These words are only colored if the
                |     OlpAstLeaf.Type is delAstKEYWORD. Used in MacroGetTranslatorInfo.

        :return: None
        """

        return None

    @logical_keywords.setter
    def logical_keywords(self, value: tuple):
        """
        :param tuple value:
        """

        self.com_object.LogicalKeywords = value

    @property
    def new_instruction(self) -> OLPInstruction:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property NewInstruction() As OlpInstruction (Read Only)
                |     The newly created instruction in Teach.
                |     This will return NULL if no new instruction was created.

        :return: OLPInstruction
        """

        return OLPInstruction(self.com_object.NewInstruction)

    @property
    def position_access_mode(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property PositionAccessMode() As DELOlpAccessMode
                |     Set the type of position access mode Must be set during
                |     MacroGetTranslatorInfo. Enabling Get or GetAndSet may cause slightly slower
                |     performance in NRL teach. Valid values are:
                | 
                |     delOlpNoAccess
                |         Translators cannot use any method or property related to robot motion
                |         positions in NRL teach. This is the default value.
                |     delOlpGetAccess
                |         Translators can get position related property values or call methods
                |         that return position related values but cannot call methods or properties that
                |         modify positions or related values.
                |     delOlpGetAndSetAccess
                |         Translator can call any methods, including ones that modify robot
                |         motion positions and related properties.

        :return: int
        """

        return self.com_object.PositionAccessMode

    @position_access_mode.setter
    def position_access_mode(self, value: int):
        """
        :param int value:
        """

        self.com_object.PositionAccessMode = value

    @property
    def refresh_mode(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property RefreshMode(CATBSTR iRefreshMode) (Write Only)
                |     Set the type of refresh needed on the task after an edit operation.
                |     Valid values are:
                |     - Download : Full download of task is performed. This will
                |       ensure everything is up to date but takes the most time.
                |       This is the default value if RefreshMode is not set.
                |     - AstInstruction : Only the AST nodes for the modified
                |       instruction have been changed. This just refreshes the UI
                |       for the current AST instruction. The AST must already have
                |       been updated by the translator.
                |     - AstTask : Some AST nodes throughout the task have been changed.
                |       This refreshed the entire task display UI. The AST must
                |       have already been updated by the translator.
                |     - None : No refresh is needed.

        :return: None
        """

        return None

    @refresh_mode.setter
    def refresh_mode(self, value: str):
        """
        :param str value:
        """

        self.com_object.RefreshMode = value

    @property
    def supports_nrl_view(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property SupportsNRLView(boolean iSupportsNRLView) (Write
                | Only)
                |     Set whether the translator supports the NRL view feature of NRL
                |     teach.
                |     Used in MacroGetTranslatorInfo.

        :return: None
        """

        return None

    @supports_nrl_view.setter
    def supports_nrl_view(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.SupportsNRLView = value

    def add_combo(self, i_editor_id: str, i_values: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub AddCombo(CATBSTR iEditorID,CATSafeArrayVariant iValues)
                |     Declare a combo for an NRL teach editor.
                | 
                |     Parameters:
                | 
                |         iEditorID
                |             The editor ID to add the combo for. 
                |         iValues
                |             The list of values the user can pick from when editing a combo
                |             or editablecombo with the given editor ID. All objects in the list are of type
                |             OlpAstNode.

        :param str i_editor_id:
        :param tuple i_values:
        :return: None
        """
        return self.com_object.AddCombo(i_editor_id, i_values)

    def add_custom_column(self, i_editor_id: str, i_column_title: str, i_applicable_applications: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub AddCustomColumn(CATBSTR iEditorID,CATBSTR iColumnTitle,CATSafeArrayVariant
                | iApplicableApplications)
                |     Declare a NRL teach editor as available as a teach table
                |     column.
                | 
                |     Parameters:
                | 
                |         iEditorID
                |             The editor ID to enable as a custom column. 
                |         iColumnTitle
                |             Title to display for the column. 
                |         iApplicableApplications
                |             Applications to show this column for. This is a list of strings.
                |             Each value should correspond to a value in the Robot Applications preference.
                |             If the list is blank the column will be available to be added for all
                |             applications.

        :param str i_editor_id:
        :param str i_column_title:
        :param tuple i_applicable_applications:
        :return: None
        """
        return self.com_object.AddCustomColumn(i_editor_id, i_column_title, i_applicable_applications)

    def add_custom_command(self, i_group: str, i_command_name: str) -> OLPCustomCommand:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func AddCustomCommand(CATBSTR iGroup,CATBSTR iCommandName) As
                | OlpCustomCommand
                |     Add a new command to Teach.
                | 
                |     Parameters:
                | 
                |         iGroup
                |             The name of the group to place the command in.
                |             This is the name displayed for the group and also the identifier
                |             for the group. The group is created automatically when a new ID is specified
                |             here. 
                |         iCommandName
                |             The name of the command to add.
                |             The command's Name and OlpCustomCommand.MainCommand properties are
                |             both initialized to this value. 
                | 
                |     Returns:
                |         The created command. 

        :param str i_group:
        :param str i_command_name:
        :return: OLPCustomCommand
        """
        return OLPCustomCommand(self.com_object.AddCustomCommand(i_group, i_command_name))

    def __repr__(self):
        return f'OLPTeachHelper(name="{ self.name }")'
