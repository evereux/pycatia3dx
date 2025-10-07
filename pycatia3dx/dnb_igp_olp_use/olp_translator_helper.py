"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.dnb_igp_olp_use.olp_id_fixer import OLPIdFixer
from pycatia3dx.interfaces.service import Service
from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.dnb_igp_olp_use.olp_ast_branch import OLPAstBranch
from pycatia3dx.dnb_igp_olp_use.olp_behavior import OLPBehavior
from pycatia3dx.dnb_igp_olp_use.olp_error_reporter import OLPErrorReporter
from pycatia3dx.dnb_igp_olp_use.olp_expression_fixer_download import OLPExpressionFixerDownload
from pycatia3dx.dnb_igp_olp_use.olp_expression_fixer_upload import OLPExpressionFixerUpload
from pycatia3dx.dnb_igp_olp_use.olp_motion_groups import OLPMotionGroups
from pycatia3dx.dnb_igp_olp_use.olp_parser import OLPParser
from pycatia3dx.dnb_igp_olp_use.olp_resource_control_device import OLPResourceControlDevice
from pycatia3dx.dnb_igp_olp_use.olp_simulation_options import OLPSimulationOptions
from pycatia3dx.dnb_igp_olp_use.olp_transform import OLPTransform


class OLPTranslatorHelper(Service):

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
                |                         OlpTranslatorHelper
                | 
                | Service used to get access to OLP data objects.
                | 
                | This interface can only be used by a translator within the Robotics Off-line
                | Programming (OLP) Download or Upload command.
                | This interface provides all the input arguments for the translation process,
                | access to related OLP objects needed for translation, and methods to set the
                | outputs of the translation process.
                | A VB.NET translator is expected to have these macros defined
                | 
                | MacroUpload
                |     Required. Called to upload robot programs into DELMIA.
                | MacroDownload
                |     Required. Called to generate robot programs from DELMIA
                |     procedures.
                | MacroGetTranslatorInfo
                |     Optional. Called to get information about the translator and translation
                |     options supported.
                | MacroSetConfigs
                |     Optional. Called to update the config for any created robot motions. This
                |     is called after MacroUpload.
                | MacroParse
                |     Optional. Called before MacroUpload to parse the selected files. The user
                |     is then given options to exclude tasks, select applications and other
                |     options.
                | 
                | The properties and methods below indicate in which of these macro's they are
                | intended to be called.
                | 
                | Example: (VB.NET)
                | 
                |  Dim Helper As OlpTranslatorHelper = CATIA.Application.GetSessionService("OlpTranslatorHelper")
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def ast_root(self) -> OLPAstBranch:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property AstRoot() As OlpAstBranch (Read Only)
                |     The root node of the abstract syntax tree.
                |     On upload translators should retrieve this element and append all the
                |     parsed files to it. On download translators should append your generated AST
                |     tree to this node.
                |     Used in MacroUpload and MacroDownload.

        :return: OLPAstBranch
        """

        return OLPAstBranch(self.com_object.AstRoot)

    @property
    def behavior(self) -> OLPBehavior:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Behavior() As OlpBehavior (Read Only)
                |     The resource behavior selected for download or upload.
                |     Used in MacroUpload and MacroDownload.

        :return: OLPBehavior
        """

        return OLPBehavior(self.com_object.Behavior)

    @property
    def caa_motion_types(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property CAAMotionTypes(CATSafeArrayVariant iInstructionTypes) (Write
                | Only)
                |     Set the list of CAA motion types.
                |     Any of these motion types will be uploaded as instructions customized
                |     through CAA. If the type is not in this list, it will be uploaded as a standard
                |     instruction. Each item in the list is a DELOlpInstructionType. By default the
                |     list is empty. Used in MacroGetTranslatorInfo.

        :return: None
        """

        return None

    @caa_motion_types.setter
    def caa_motion_types(self, value: tuple):
        """
        :param tuple value:
        """

        self.com_object.CAAMotionTypes = value

    @property
    def cat_nls_file_name(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property CATNlsFileName(CATBSTR iName) (Write Only)
                |     Put the name of the CATNls file to use for the NRL teach
                |     menu.
                |     Used in MacroGetTranslatorInfo.

        :return: None
        """

        return None

    @cat_nls_file_name.setter
    def cat_nls_file_name(self, value: str):
        """
        :param str value:
        """

        self.com_object.CATNlsFileName = value

    @property
    def call_succeeded(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property CallSucceeded(boolean iSucceeded) (Write Only)
                |     If the operation succeeded, the translator must set this to
                |     True.
                |     Used in MacroUpload, MacroDownload, MacroGetTranslatorInfo, and
                |     MacroSetConfigs.

        :return: None
        """

        return None

    @call_succeeded.setter
    def call_succeeded(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.CallSucceeded = value

    @property
    def debug_macro_call_string(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property DebugMacroCallString() As CATBSTR (Read Only)
                |     Get the macro call to debug
                |     Set the environment variable DELMIA_OLP_TRANSLATOR_DEBUG to enable
                |     translator debugging. When running the upload or download command select the
                |     macro(s) you want to debug. The selection will be used for your entire session.
                |     Instead of that macro being launched automatically, you will be prompted to run
                |     them from Visual Studio as needed. When that happens, this property will
                |     contain the name of the macro to execute which you can use to call that macro
                |     by name.
                | 
                |        CallByName(Me, TransHelper.DebugMacroCallString,
                |        CallType.Method)

        :return: str
        """

        return self.com_object.DebugMacroCallString

    @property
    def directory(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Directory() As CATBSTR (Read Only)
                |     The directory which contains the robot programs on upload.
                |     Used in MacroUpload.

        :return: str
        """

        return self.com_object.Directory

    @property
    def download_directory(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property DownloadDirectory() As CATBSTR
                |     Gets/Sets a temp directory used by the translator during translation. The
                |     translator can get this value and a valid temp directory will be returned
                |     during any Macro call. If the translator has a specific directory used during
                |     download where some file have been saved, it can set that directory here. For
                |     example if those files are to be transferred to the RRS-II VRC. Setting
                |     DownloadDirectory only has an meaning during MacroDownload.

        :return: str
        """

        return self.com_object.DownloadDirectory

    @download_directory.setter
    def download_directory(self, value: str):
        """
        :param str value:
        """

        self.com_object.DownloadDirectory = value

    @property
    def download_option(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property DownloadOption() As CATBSTR (Read Only)
                |     The extra option specified by the user (or in tools-options) for
                |     download.
                |     The translator can use this option any way it likes. For example, the XML
                |     translator uses this to specify the XSLT-file. It could also be used to specify
                |     a robot controller version. The translator can specify valid supported options
                |     by setting the ValidDownloadOptions.
                |     Used in MacroDownload.

        :return: str
        """

        return self.com_object.DownloadOption

    @property
    def error_reporter(self) -> OLPErrorReporter:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ErrorReporter() As OlpErrorReporter (Read Only)
                |     The object used to report errors, warnings, etc.
                |     Used in MacroUpload, MacroDownload, MacroGetTranslatorInfo, and
                |     MacroSetConfigs.

        :return: OLPErrorReporter
        """

        return OLPErrorReporter(self.com_object.ErrorReporter)

    @property
    def extension_description(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ExtensionDescription(CATBSTR iDesciption) (Write
                | Only)
                |     A description of the file type set with
                |     SupportedExtensions.
                |     For example "Kuka robot programs".
                |     Used in MacroGetTranslatorInfo.

        :return: None
        """

        return None

    @extension_description.setter
    def extension_description(self, value: str):
        """
        :param str value:
        """

        self.com_object.ExtensionDescription = value

    @property
    def file_paths(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property FilePaths() As CATSafeArrayVariant (Read Only)
                |     A list of full paths to all the files the user requested to
                |     upload.
                |     Used in MacroUpload.

        :return: tuple
        """

        return self.com_object.FilePaths

    @property
    def include_waypont_operations_in_list(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property IncludeWaypontOperationsInList(boolean iInclude) (Write
                | Only)
                |     Include the waypoint operations in the OlpInstructions list. If true, the
                |     WaypointOperations are included. If False, the waypoint motions inside the
                |     waypoint operation are directly included in the list. The default value is
                |     False for compatibility. Used in MacroGetTranslatorInfo.

        :return: None
        """

        return None

    @include_waypont_operations_in_list.setter
    def include_waypont_operations_in_list(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.IncludeWaypontOperationsInList = value

    @property
    def motion_groups(self) -> OLPMotionGroups:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property MotionGroups() As OlpMotionGroups (Read Only)
                |     The motion groups selected for download or upload.
                |     Used in MacroUpload, MacroSetConfigs and MacroDownload.

        :return: OLPMotionGroups
        """

        return OLPMotionGroups(self.com_object.MotionGroups)

    @property
    def olp_version_string(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property OLPVersionString() As CATBSTR (Read Only)
                |     Get version of the OLP APIs
                |     Translators can use this property to detect if they have been updated to
                |     support the latest version of the OLP APIs. For example, if a new API has been
                |     added or modified the translator can check to see if it should use the old or
                |     new way. This way translators can be backported to earlier FPs before the API
                |     was available.

        :return: str
        """

        return self.com_object.OLPVersionString

    @property
    def position_variable_robot_language_length_units(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property PositionVariableRobotLanguageLengthUnits(CATBSTR iUnits) (Write
                | Only)
                |     Set the units used by the robot language for position variable data members
                |     of type length.
                |     Valid values are "mm" (millimeters) or "m" (meters). "m" is the default
                |     value. If the value is "mm" units conversion functions will automatically be
                |     added and removed when getting and setting expressions using the DELOlp APIs.
                |     These will be added when a position variable data member of type length (e.g.
                |     x, y, z, or linear joint value) is assigned or used in an expression. For
                |     example
                | 
                |         PV1.x := 100.0
                |      
                | 
                |     will be converted to
                | 
                |         PV1.x := 100.0 / MM_PER_METER
                |      
                | 
                |     when the expression is set as the destination of the assignment and back
                |     again when the expression is retrieved. Used in MacroGetTranslatorInfo.

        :return: False
        """

        return None

    @position_variable_robot_language_length_units.setter
    def position_variable_robot_language_length_units(self, value: str):
        """
        :param str value:
        """

        self.com_object.PositionVariableRobotLanguageLengthUnits = value

    @property
    def position_variable_robot_language_rotation_units(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property PositionVariableRobotLanguageRotationUnits(CATBSTR iUnits) (Write
                | Only)
                |     Set the units used by the robot language for position variable data members
                |     of type rotation.
                |     Valid values are "deg" (degrees) or "rad" (radians). "rad" is the default
                |     value. If the value is "deg" units conversion functions will automatically be
                |     added and removed when getting and setting expressions using the DELOlp APIs.
                |     These will be added when a position variable data member of type rotation (e.g.
                |     w, p, r, or rotational joint value) is assigned or used in an expression. For
                |     example
                | 
                |         PV1.w := 60.0
                |      
                | 
                |     will be converted to
                | 
                |         PV1.w := toradian(60.0)
                |      
                | 
                |     when the expression is set as the destination of the assignment and back
                |     again when the expression is retrieved. Used in MacroGetTranslatorInfo.

        :return: None
        """

        return None

    @position_variable_robot_language_rotation_units.setter
    def position_variable_robot_language_rotation_units(self, value: str):
        """
        :param str value:
        """

        self.com_object.PositionVariableRobotLanguageRotationUnits = value

    @property
    def resource_control_device(self) -> OLPResourceControlDevice:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ResourceControlDevice() As OlpResourceControlDevice (Read
                | Only)
                |     The resource control device for download or upload.
                |     Used in MacroUpload and MacroDownload.

        :return: OLPResourceControlDevice
        """

        return OLPResourceControlDevice(self.com_object.ResourceControlDevice)

    @property
    def simulation_options(self) -> OLPSimulationOptions:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property SimulationOptions() As OlpSimulationOptions (Read
                | Only)
                |     Gets the simulation options handle, which can be used to access values of
                |     simulation options by their names.

        :return: OLPSimulationOptions
        """

        return OLPSimulationOptions(self.com_object.SimulationOptions)

    @property
    def supported_extensions(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property SupportedExtensions(CATBSTR iExtensions) (Write Only)
                |     The list of supported file extensions, separated by a semicolon
                |     (;).
                |     For example "*.src;*.dat".
                |     Used in MacroGetTranslatorInfo.

        :return: None
        """

        return None

    @supported_extensions.setter
    def supported_extensions(self, value: str):
        """
        :param False value:
        """

        self.com_object.SupportedExtensions = value

    @property
    def supported_motion_types(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property SupportedMotionTypes(CATSafeArrayVariant iInstructionTypes) (Write
                | Only)
                |     Set the list of supported motion types.
                |     Each item in the list is a DELOlpInstructionType. By default the list
                |     contains delOlpSpotOperation, delOlpArcOperation, delOlpSeamSearchOperation,
                |     and delOlpRobotMotion. Used in MacroGetTranslatorInfo.

        :return: None
        """

        return None

    @supported_motion_types.setter
    def supported_motion_types(self, value: tuple):
        """
        :param tuple value:
        """

        self.com_object.SupportedMotionTypes = value

    @property
    def supports_mulitiple_motion_groups(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property SupportsMulitpleMotionGroups(boolean iSupportsMMG) (Write
                | Only)
                |     Set whether tasks which control multiple motion groups are supported by
                |     this translator.
                |     If not supported, the tasks are exposed to the translators as single motion
                |     group tasks. Default values is FALSE. Used in MacroGetTranslatorInfo.

        :return: None
        """

        return None

    @supports_mulitiple_motion_groups.setter
    def supports_mulitiple_motion_groups(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.SupportsMulitpleMotionGroups = value

    @property
    def supports_multiple_robots(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property SupportsMultipleRobots(boolean iSupportsMultiRobot) (Write
                | Only)
                |     Set whether controller which control multiple robots are supported by this
                |     translator.
                |     If not supported, only tasks which control a single robot and all control
                |     the same robot will be able to be downloaded. Used in MacroGetTranslatorInfo.

        :return: None
        """

        return None

    @supports_multiple_robots.setter
    def supports_multiple_robots(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.SupportsMultipleRobots = value

    @property
    def supports_templates(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property SupportsTemplates(boolean iUseTemplates) (Write Only)
                |     Set whether templates are used by this translator.
                |     Used in MacroGetTranslatorInfo.

        :return: None
        """

        return None

    @supports_templates.setter
    def supports_templates(self, value: str):
        """
        :param str value:
        """

        self.com_object.SupportsTemplates = value

    @property
    def tasks(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Tasks() As CATSafeArrayVariant (Read Only)
                |     All the tasks the user requested to download or all the tasks that have
                |     been created so far on upload.
                |     Primarily used in MacroDownload but also available in MacroUpload and
                |     MacroSetConfigs.

        :return: tuple
        """

        return self.com_object.Tasks

    @property
    def tasks_to_upload(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property TasksToUpload() As CATSafeArrayVariant (Read Only)
                |     The task names the user has selected for uploading.
                |     This is a subset of the tasks added with AddTaskToUpload. Each item in the
                |     returns list is a string. Used in MacroUpload.

        :return: tuple
        """

        return self.com_object.TasksToUpload

    @property
    def template_directory(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property TemplateDirectory() As CATBSTR (Read Only)
                |     The directory which contains the template files on
                |     download.
                |     Used in MacroDownload.

        :return: str
        """

        return self.com_object.TemplateDirectory

    @property
    def trig_function_robot_language_rotation_units(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property TrigFunctionRobotLanguageRotationUnits(CATBSTR iUnits) (Write
                | Only)
                |     Set the units used by the robot language for trigenometry
                |     functions.
                |     Valid values are "deg" (degrees) or "rad" (radians). "rad" is the default
                |     value. If the value is "deg" units conversion functions will automatically be
                |     added and removed when getting and setting expressions using the DELOlp APIs.
                |     These will be added when a trig fuction (e.g. sin, cos, tan, asin, acos, atan,
                |     atan2) is used in an expression. For example
                | 
                |         x := sin(60.0)
                |      
                | 
                |     will be converted to
                | 
                |         x := sin(toradian(60.0))
                |      
                | 
                |     when the expression is set as the destination of the assignment and back
                |     again when the expression is retrieved. Used in MacroGetTranslatorInfo.

        :return: None
        """

        return None

    @trig_function_robot_language_rotation_units.setter
    def trig_function_robot_language_rotation_units(self, value: str):
        """
        :param str value:
        """

        self.com_object.TrigFunctionRobotLanguageRotationUnits = value

    @property
    def upload_application_option_string(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property UploadApplicationOptionString() As CATBSTR (Read
                | Only)
                |     The application type the user choose to upload.
                |     This is one of the options passed into UploadApplicationOptions. If a
                |     DELOlpInstructionType was used, the equivalent string value is returned. For
                |     example "SpotOperation" is returned for delOlpSpotOperation. Used in
                |     MacroUpload.

        :return: str
        """

        return self.com_object.UploadApplicationOptionString

    @property
    def upload_application_options(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property UploadApplicationOptions(CATSafeArrayVariant iOptions) (Write
                | Only)
                |     List of possible applications that could be uploaded.
                |     The user is presented with this list of options and can pick one. The one
                |     they picked is returned by UploadApplicationOptionString. The list is a list of
                |     DELOlpInstructionType and/or strings. Used in MacroUpload.

        :return: None
        """

        return None

    @upload_application_options.setter
    def upload_application_options(self, value: str):
        """
        :param str value:
        """

        self.com_object.UploadApplicationOptions = value

    @property
    def upload_option(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property UploadOption() As CATBSTR (Read Only)
                |     The extra option specified by the user (or in tools-options) for
                |     upload.
                |     The translator can use this option any way it likes. For example, the XML
                |     translator uses this to specify the JAR-file. It could also be used to specify
                |     a robot controller version. The translator can specify valid supported options
                |     by setting the ValidUploadOptions.
                |     Used in MacroUpload.

        :return: str
        """

        return self.com_object.UploadOption

    @property
    def upload_path_operation_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property UploadPathOperationType() As DELOlpInstructionType (Read
                | Only)
                |     The robot's application type for path operations.
                |     Translators which cannot differenciate between delOlpPathAdhesiveOperation
                |     and delOlpSealantOperation can call this function to determine which type to
                |     create during upload. Used in MacroUpload.

        :return: DELOlpInstructionType
        """

        return self.com_object.UploadPathOperationType

    @property
    def valid_download_options(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ValidDownloadOptions(CATSafeArrayVariant iOptions) (Write
                | Only)
                |     Set the list of valid values for DownloadOption.
                |     Used in MacroGetTranslatorInfo.

        :return: None
        """

        return None

    @valid_download_options.setter
    def valid_download_options(self, value: tuple):
        """
        :param tuple value:
        """

        self.com_object.ValidDownloadOptions = value

    @property
    def valid_upload_options(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ValidUploadOptions(CATSafeArrayVariant iOptions) (Write
                | Only)
                |     Set the list of valid values for UploadOption.
                |     Used in MacroGetTranslatorInfo.

        :return: None
        """

        return None

    @valid_upload_options.setter
    def valid_upload_options(self, value: tuple):
        """
        :param tuple value:
        """

        self.com_object.ValidUploadOptions = value

    def add_supported_template(self, i_template_lib: str, i_template_name: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub AddSupportedTemplate(CATBSTR iTemplateLib,CATBSTR
                | iTemplateName)
                |     Enable special handling of a template instruction.
                |     By default, the OLP APIs expose only the instructions inside a template to
                |     the translator. This way all templates are supported, even new templates create
                |     by users. If the translator needs to handle the download in a special way, for
                |     example to download the entire template as a single instruction, it can call
                |     this method. OlpInstruction.Type will return delOlpTemplate for all supported
                |     templates. You can specify "all" for the library and template name to enable
                |     support for all types of templates. Used in MacroGetTranslatorInfo.

        :param str i_template_lib:
        :param str i_template_name:
        :return: None
        """
        return self.com_object.AddSupportedTemplate(i_template_lib, i_template_name)

    def add_task_to_not_upload(self, i_task_name: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub AddTaskToNotUpload(CATBSTR iTaskName)
                |     Adds a task name to the translator's upload list in the unselected column
                |     of the upload dialog.
                |     This list can be retrieved later using @see
                |     DELMIAOlpTranslatorHelper#GetTasksToUpload.
                | 
                |     Parameters:
                | 
                |         The
                |             task name to add to the translator's upload list

        :param str i_task_name:
        :return: None
        """
        return self.com_object.AddTaskToNotUpload(i_task_name)

    def add_task_to_upload(self, i_task_name: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub AddTaskToUpload(CATBSTR iTaskName)
                |     Add a task name to the list of tasks that could be uploaded based on the
                |     files the user selected to upload.
                |     If tasks have been added, the user is give the option to exclude some from
                |     the upload. See TasksToUpload. Used in MacroParse.
                | 
                |     Parameters:
                | 
                |         iParserName
                |             The name of the parser to create.

        :param str i_task_name:
        :return: None
        """
        return self.com_object.AddTaskToUpload(i_task_name)

    def create_expr_fixer_download(self) -> OLPExpressionFixerDownload:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func CreateExprFixerDownload() As OlpExpressionFixerDownload
                |     Creates a new expression fixer for download.
                | 
                |     Returns:
                |         The fixer.

        :return: OLPExpressionFixerDownload
        """
        return OLPExpressionFixerDownload(self.com_object.CreateExprFixerDownload())

    def create_expr_fixer_upload(self) -> OLPExpressionFixerUpload:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func CreateExprFixerUpload() As OlpExpressionFixerUpload
                |     Creates a new expression fixer for upload.
                | 
                |     Returns:
                |         The fixer.

        :return: OLPExpressionFixerUpload
        """
        return OLPExpressionFixerUpload(self.com_object.CreateExprFixerUpload())

    # todo:
    def create_id_fixer(self) -> OLPIdFixer:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func CreateIDFixer() As OlpIDFixer
                |     Creates a new id fixer.
                | 
                |     Returns:
                |         The fixer.

        :return: OLPIdFixer
        """
        return OLPIdFixer(self.com_object.CreateIDFixer())

    def create_parser(self, i_parser_name: str) -> OLPParser:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func CreateParser(CATBSTR iParserName) As OlpParser
                |     Creates a new robot program parser.
                | 
                |     Parameters:
                | 
                |         iParserName
                |             The name of the parser to create. Some of the parser names
                |             are
                | 
                |             DNBOlpFanucParser
                |                 Parser for FANUC TP programs.
                |             DNBOlpKukaParser
                |                 Parser for Kuka KRL .src and .dat files.
                |             DNBOlpRapidParser
                |                 Parser for ABB Rapid .mod files.
                | 
                |     Returns:
                |         The parser.

        :param str i_parser_name:
        :return: OLPParser
        """
        return OLPParser(self.com_object.CreateParser(i_parser_name))

    def create_transform(self) -> OLPTransform:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func CreateTransform() As OlpTransform
                |     Creates a new transform.
                | 
                |     Returns:
                |         The transform.

        :return: OLPTransform
        """
        return OLPTransform(self.com_object.CreateTransform())

    def get_feature_enabled(self, i_feature_name: str) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetFeatureEnabled(CATBSTR iFeatureName) As boolean
                |     Query if an LA feature is enabled in the current session.
                |     Use this instead of quering an environment variable.
                | 
                |     Parameters:
                | 
                |         iFeatureName
                |             The name of the feature.
                | 
                |             ARRAYS_ALL
                |                 Full array variable support. GA in R2022x
                |                 FD04.
                |             ARRAYS_VAR_SCOPE
                |                 Array variable support for everything except external IOs. GA
                |                 in R2022x FD04.
                |             MAPPING
                |                 Device, Motion Group, DOF, and Tool mapping enabled. GA in
                |                 R2022x FD02.
                |             PULSECOUNT
                |                 Pulse count parameters in the DOF mapping. GA in R2022x
                |                 FD02.
                |             POSITIONVARIABLE
                |                 Position Variables. GA in R2023x FD02.
                | 
                |     Returns:
                |         TRUE if the feature is enabled.

        :param str i_feature_name:
        :return: bool
        """
        return self.com_object.GetFeatureEnabled(i_feature_name)

    def get_rrsii_context(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetRRSIIContext() As CATBSTR
                |     Gets the translator's RRSII Context.
                |     For a standard download, the context is blank. For an RRS-II simulation
                |     download the context is "Simulation Run".
                | 
                |     Returns:
                |         The RRSII Context

        :return: str
        """
        return self.com_object.GetRRSIIContext()

    def get_rrs_virtual_robot_directory(self, i_share_name: str) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetRRSVirtualRobotDirectory(CATBSTR iShareName) As
                | CATBSTR
                |     Get the RRS virtual robot directory to look in for system variable files
                |     during upload or download.
                |     Used in any macro.

        :param str i_share_name:
        :return: str
        """
        return self.com_object.GetRRSVirtualRobotDirectory(i_share_name)

    def is_same(self, i_obj1: AnyObject, i_obj2: AnyObject) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func IsSame(CATBaseDispatch iObj1,CATBaseDispatch iObj2) As
                | boolean
                |     Tests if 2 objects are the same.
                |     This returns true if the underlying objects are the same. The interface
                |     pointers need not be of the same type. You cannot use the VB equality tests on
                |     interface pointers. That test may say the objects are not equal even if the
                |     underlying objects are the same.
                | 
                |     Parameters:
                | 
                |         iObj1
                |             The 1st object. Can be NULL. 
                |         iObj2
                |             The 2nd object. Can be NULL. 
                | 
                |     Returns:
                |         True if the iObj1 and iObj2 are interfaces of the same underlying
                |         object or if both are NULL.

        :param AnyObject i_obj1:
        :param AnyObject i_obj2:
        :return: bool
        """
        return self.com_object.IsSame(i_obj1.com_object, i_obj2.com_object)

    def set_supported_feature(self, i_feature_name: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetSupportedFeature(CATBSTR iFeatureName)
                |     Enable a translator feature.
                |     Translators can call this to enable LA features. Used in
                |     MacroGetTranslatorInfo. 

        :param str i_feature_name:
        :return: None
        """
        return self.com_object.SetSupportedFeature(i_feature_name)

    def __repr__(self):
        return f'OLPTranslatorHelper(name="{ self.name }")'
