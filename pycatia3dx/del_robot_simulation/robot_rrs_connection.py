"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class RobotRrsConnection(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     RobotRRSConnection
                | 
                | Interface to manage the RRS connection capabilities.
                | Role: This interface provides methods to deal with the industrial robot
                | connection through the RRS standards.
                | 
                | Example:
                |     Let assume there is a robot opened as a root entity in a given
                |     editor.
                | 
                |      Dim MainResource As Variant
                |      Set MainResource = CATIA.ActiveEditor.ActiveObject
                | 
                |      Dim MySimulatedResource As RobotRRSConnection
                |      Set MySimulatedResource = MainResource.GetItem("CAARobotRRSConnection")
                |      
                |      If Not MySimulatedResource Is Nothing Then
                | 
                |      End If
                | 
                | Note:API documentation will include sample code referring to:
                | 
                |     MySimulatedResource as a variable of type
                |     RobotRRSConnection.
                |     MainResource as the resource to be simulated (can be obtained through
                |     selection or model scanning.
                | 
                | Remark:All API will not work if the Initialize has not been
                | performed.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def is_rrs_connected(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property IsRRSConnected() As boolean (Read Only)
                |     Checks if RRS is enabled for the robot.
                | 
                |     Example:
                | 
                |      Dim bRRSConnected As Boolean
                |      bRRSConnected = MySimulatedResource.IsRRSConnected

        :return: bool
        """

        return self.com_object.IsRRSConnected

    @property
    def rrs_controller_type(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property RRSControllerType() As CATBSTR (Read Only)
                |     Gets the RRS controller type used for communication with the RRS
                |     server.
                | 
                |     Example:
                | 
                |      Dim MyRRSControllerType As String
                |      MyRRSControllerType = MySimulatedResource.RRSControllerType

        :return: str
        """

        return self.com_object.RRSControllerType

    @property
    def rrs_server_decorated_names(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property RRSServerDecoratedNames() As CATSafeArrayVariant (Read
                | Only)
                |     Gets the complete list of RRS server decorated names. Name is obtained from
                |     the "rrs.servers" file. Decorated names also contain host and TCP port/RPC
                |     program number besides the raw RRS server name.
                | 
                |     Example:
                | 
                |      Dim MyRRSServerNames As String
                |      Dim MyListRRSServerNames
                |      MyListRRSServerNames = MySimulatedResource.RRSServerDecoratedNames
                |      For II = LBound(MyListRRSServerNames) To UBound(MyListRRSServerNames)
                |        Set MyRRSServerNames = MyListRRSServerNames(II)
                |        'uncomment next line to display value
                |        'MsgBox ("Decorated server name:" & MyRRSServerNames)
                |      Next

        :return: tuple
        """

        return self.com_object.RRSServerDecoratedNames

    @property
    def rrs_server_name(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property RRSServerName() As CATBSTR (Read Only)
                |     Gets the name of the RRS server robot is connected to.
                | 
                |     Example:
                | 
                |      Dim MyRRSServerName As String
                |      MyRRSServerName = MySimulatedResource.RRSServerName

        :return: str
        """

        return self.com_object.RRSServerName

    @property
    def using_rrs2_server(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property UsingRRS2Server() As boolean (Read Only)
                |     Checks if an RRS-II (as opposed to RRS-I) connection is enabled for the
                |     robot.
                | 
                |     Example:
                | 
                |      Dim MyRRS2Server As Boolean
                |      MyRRS2Server = MySimulatedResource.UsingRRS2Server

        :return: bool
        """

        return self.com_object.UsingRRS2Server

    def auto_rrs_connect(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func AutoRRSConnect() As long
                |     Automatically RRS (RRS-I) connects robots using RRS attributes stored in
                |     persistent store (based on previous RRS connection).
                | 
                |     Parameters:
                | 
                |         oConnectionSuccess
                |             0 if RRS-I connection attempt was successful(otherwise 1).

        :return: int
        """
        return self.com_object.AutoRRSConnect()

    def chk_rrs_server_type(self, i_rrs_server_decorated_name: str) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func ChkRRSServerType(CATBSTR iRRSServerDecoratedName) As
                | boolean
                |     Checks if given rrs_server_decorated_name corresponds to an RRS-I server
                |     (as opposed to an RRS-II server). Decorated names also contain host and TCP
                |     port/RPC program number besides the raw RRS server name.
                | 
                |     Example:
                | 
                |      Dim MyRRSServerDecoratedName As String
                |      'valuation of the server decorated name
                |      Dim MyRRS1Status As Boolean
                |      MyRRS1Status = MySimulatedResource.ChkRRSServerType(MyRRSServerDecoratedName)

        :param str i_rrs_server_decorated_name:
        :return: bool
        """
        return self.com_object.ChkRRSServerType(i_rrs_server_decorated_name)

    def rrs1_connect_step1(self, i_rrs_server_decorated_name: str, o_default_robot_number: int, o_min_robot_number: int, o_max_robot_number: int, o_rrs_server_host_name: str, o_rcs_home_directory: str, o_rcs_list_home_directory: tuple, o_default_rcs_home_dir_index: int, o_default_robot_relative_path: str, o_manipulator_list_id: tuple, o_default_manipulator_index: int, o_manipulator_user_selectable: bool) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func RRS1ConnectStep1(CATBSTR iRRSServerDecoratedName,long
                | oDefaultRobotNumber,long oMinRobotNumber,long oMaxRobotNumber,CATBSTR
                | oRRSServerHostName,CATBSTR oRCSHomeDirectory,CATSafeArrayVariant
                | oRCSListHomeDirectory,long oDefaultRCSHomeDirIndex,CATBSTR
                | oDefaultRobotRelativePath,CATSafeArrayVariant oManipulatorListID,long
                | oDefaultManipulatorIndex,boolean oManipulatorUserSelectable) As
                | long
                |     First call to establish RRS-I connection to given RRS-I RCS server using
                |     given connection parameters.
                | 
                |     Parameters:
                | 
                |         iRRSServerDecoratedName
                |             Decorated name of RRS server. Note that, decorated names also
                |             contain host and TCP port/RPC program number besides the raw RRS server name.
                |             
                |         oDefaultRobotNumber
                |             Returned default RRS-I robot number. 
                |         oMinRobotNumber
                |             Returned minimum acceptable RRS-I robot number. 
                |         oMaxRobotNumber
                |             Returned maximum acceptable RRS-I robot number. 
                |         oRRSServerHostName
                |             Returned RRS server host machine name. 
                |         oRCSHomeDirectory
                |             Returned RCS home directory. 
                |         oDefaultRCSHomeDirIndex
                |             Returned index for default data home directory list.
                |             
                |         oDefaultRobotRelativePath
                |             Returned default relative robot path. 
                |         oDefaultRobotRelativePath
                |             Returned default relative robot path. 
                |         oManipulatorListID
                |             Returned supported RRS-I manipulator strings list.
                |             
                |         oDefaultManipulatorIndex
                |             Returned index of the default manipulator in manipulator_list with
                |             a 1 corresponding to first item in the list. 
                |         oManipulatorUserSelectable
                |             Returned indication of whether or not manipulator string is user
                |             selectable. 
                |         oConnectionSuccess
                |             0 if RRS-I connection attempt was successful(otherwise 1).

        :param str i_rrs_server_decorated_name:
        :param int o_default_robot_number:
        :param int o_min_robot_number:
        :param int o_max_robot_number:
        :param str o_rrs_server_host_name:
        :param str o_rcs_home_directory:
        :param tuple o_rcs_list_home_directory:
        :param int o_default_rcs_home_dir_index:
        :param str o_default_robot_relative_path:
        :param tuple o_manipulator_list_id:
        :param int o_default_manipulator_index:
        :param bool o_manipulator_user_selectable:
        :return: int
        """
        return self.com_object.RRS1ConnectStep1(i_rrs_server_decorated_name, o_default_robot_number, o_min_robot_number, o_max_robot_number, o_rrs_server_host_name, o_rcs_home_directory, o_rcs_list_home_directory, o_default_rcs_home_dir_index, o_default_robot_relative_path, o_manipulator_list_id, o_default_manipulator_index, o_manipulator_user_selectable)

    def rrs1_connect_step2(self, i_robot_number: int, i_rrs_data_home_directory: str, i_relative_robot_path: str, i_manipulator_id: str, ib_initialization_debug_enabled: bool) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func RRS1ConnectStep2(long iRobotNumber,CATBSTR iRRSDataHomeDirectory,CATBSTR
                | iRelativeRobotPath,CATBSTR iManipulatorID,boolean ibInitializationDebugEnabled)
                | As long
                |     Second (and final) call to establish RRS-I connection to given RRS-I RCS
                |     server using given connection parameters.
                | 
                |     Parameters:
                | 
                |         iRobotNumber
                |             The RRS-I robot number to use. 
                |         iRRSDataHomeDirectory
                |             The RRS-I RCS data home directory to use. 
                |         iRelativeRobotPath
                |             The RRS-I robot path directory to use (when combined with
                |             rcs_data_home_directory). 
                |         iManipulatorID
                |             The RRS-I manipulator string to use. 
                |         ibInitializationDebugEnabled
                |             Indicates if RRS-I initialization debugging should be enabled or
                |             not (set it to FALSE by default). 
                |         oConnectionSuccess
                |             0 if RRS-I connection attempt was successful(otherwise 1).

        :param int i_robot_number:
        :param str i_rrs_data_home_directory:
        :param str i_relative_robot_path:
        :param str i_manipulator_id:
        :param bool ib_initialization_debug_enabled:
        :return: int
        """
        return self.com_object.RRS1ConnectStep2(i_robot_number, i_rrs_data_home_directory, i_relative_robot_path, i_manipulator_id, ib_initialization_debug_enabled)

    def rrs2_connect_step1(self, i_rrs_server_decorated_name: str, o_list_controller_software_version: tuple, o_default_controller_software_version_index: int) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func RRS2ConnectStep1(CATBSTR iRRSServerDecoratedName,CATSafeArrayVariant
                | oListControllerSoftwareVersion,long oDefaultControllerSoftwareVersionIndex) As
                | long
                |     First call to establish RRS-II connection to given RRS-II VRC module using
                |     given connection parameters.
                | 
                |     Parameters:
                | 
                |         iRRSServerDecoratedName
                |             Decorated name of RRS server. Note that, decorated names also
                |             contain host and TCP port/RPC program number besides the raw RRS server name.
                |             
                |         oListControllerSoftwareVersion
                |             Returned supported VRC controller software versions list.
                |             
                |         oDefaultControllerSoftwareVersionIndex
                |             Returned index of the default controller software version in
                |             controller_sw_version_list with a 1 corresponding to first item in the list.
                |             
                |         oConnectionSuccess
                |             0 if RRS-II connection attempt was successful(otherwise 1).

        :param str i_rrs_server_decorated_name:
        :param tuple o_list_controller_software_version:
        :param int o_default_controller_software_version_index:
        :return: int
        """
        return self.com_object.RRS2ConnectStep1(i_rrs_server_decorated_name, o_list_controller_software_version, o_default_controller_software_version_index)

    def rrs2_connect_step2(self, i_controller_software_version: str, o_list_user_language: tuple, o_default_user_language_index: int, o_list_controller_config: tuple, o_default_controller_config_index: int) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func RRS2ConnectStep2(CATBSTR iControllerSoftwareVersion,CATSafeArrayVariant
                | oListUserLanguage,long oDefaultUserLanguageIndex,CATSafeArrayVariant
                | oListControllerConfig,long oDefaultControllerConfigIndex) As
                | long
                |     Second call to establish RRS-II connection to given RRS-II VRC module using
                |     given connection parameters.
                | 
                |     Parameters:
                | 
                |         iControllerSoftwareVersion
                |             The VRC controller software version to use. 
                |         oListUserLanguage
                |             Returned supported VRC user languages list. 
                |         oDefaultUserLanguageIndex
                |             Returned index of the default VRC user language in
                |             user_language_list with a 1 corresponding to first item in the list.
                |             
                |         oListControllerConfig
                |             Returned supported VRC controller configurations list.
                |             
                |         oDefaultControllerConfigIndex
                |             Returned index of the default VRC controller configuration in
                |             controller_config_list with a 1 corresponding to first item in the list.
                |             
                |         oConnectionSuccess
                |             0 if RRS-II connection attempt was successful(otherwise 1).

        :param str i_controller_software_version:
        :param tuple o_list_user_language:
        :param int o_default_user_language_index:
        :param tuple o_list_controller_config:
        :param int o_default_controller_config_index:
        :return: int
        """
        return self.com_object.RRS2ConnectStep2(i_controller_software_version, o_list_user_language, o_default_user_language_index, o_list_controller_config, o_default_controller_config_index)

    def rrs2_connect_step3(self, i_user_language: str, i_controller_config: str, i_file_system_full_path: str) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func RRS2ConnectStep3(CATBSTR iUserLanguage,CATBSTR iControllerConfig,CATBSTR
                | iFileSystemFullPath) As long
                |     Third (and final) call to establish RRS-II connection to given RRS-II VRC
                |     module using given connection parameters.
                | 
                |     Parameters:
                | 
                |         iUserLanguage
                |             The VRC user language to use. 
                |         iControllerConfig
                |             The VRC controller configuration to use. 
                |         iFileSystemFullPath
                |             The full path of VRC file system to use in initializing the VRC
                |             instance. Note that, for controller_config-based initialization, this parameter
                |             should be set to an empty string. 
                |         oConnectionSuccess
                |             0 if RRS-II connection attempt was successful(otherwise 1).

        :param str i_user_language:
        :param str i_controller_config:
        :param str i_file_system_full_path:
        :return: int
        """
        return self.com_object.RRS2ConnectStep3(i_user_language, i_controller_config, i_file_system_full_path)

    def rrs_disconnect(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func RRSDisconnect() As long
                |     Disconnects RRS (RRS-I) for robot.
                | 
                |     Parameters:
                | 
                |         oConnectionSuccess
                |             0 if RRS-I connection attempt was successful(otherwise 1).

        :return: int
        """
        return self.com_object.RRSDisconnect()

    def __repr__(self):
        return f'RobotRrsConnection(name="{ self.name }")'
