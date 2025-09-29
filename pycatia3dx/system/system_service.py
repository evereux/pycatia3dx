#! usr/bin/python3.9
"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-13 15:35:27.265802

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.types.general import CATVariant


class SystemService(AnyObject):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SystemService
                | 
                | Represents an object which provides system services.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def environ(self, i_env_string: str) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Func Environ(CATBSTR iEnvString) As CATBSTR
                |     Returns the value of an environment variable.
                | 
                |     Parameters:
                | 
                |         iEnvString
                |             The name of the environment variable 
                | 
                |     Example:
                |         This example retrieves the value of the PATH variable in the Value
                |         string.
                | 
                |          Value = CATIA.SystemService.Environ("PATH")

        :param str i_env_string:
        :return: str
        """
        return self.com_object.Environ(i_env_string)

    def evaluate(self, i_script_text: str, i_language: int, i_function_name: str,
                 i_parameters: tuple) -> CATVariant:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Func Evaluate(CATBSTR iScriptText,CATScriptLanguage iLanguage,CATBSTR
                | iFunctionName,CATSafeArrayVariant iParameters) As CATVariant
                |     Evaluates a scripted function.
                | 
                |     Parameters:
                | 
                |         iScriptText
                |             The program text 
                |         iLanguage
                |             The language the program is written in 
                |         iFunctionName
                |             The name of the function to invoke 
                |         iParameters
                |             An array of parameters for the function 
                |         oResult
                |             The value returned by the function (if any) 
                | 
                |     Example:
                |         This example executes the function CATMain from the CodeToEvaluate
                |         string
                | 
                |          Dim params()
                |          Dim codeToEvaluate
                |          CodeToEvaluate = "Sub CATMain()" & vbNewLine & _
                |                           "MsgBox " & chr(34) & "Hello World" & chr(34) &
                |                           vbNewLine & _
                |                           "End Sub"
                |          CATIA.SystemService.Evaluate CodeToEvaluate, CATVBScriptLanguage,
                |          "CATMain", params

        :param str i_script_text:
        :param int i_language:
        :param str i_function_name:
        :param tuple i_parameters:
        :return: CATVariant
        """
        return self.com_object.Evaluate(i_script_text, i_language, i_function_name, i_parameters)

    def execute_background_processus(self, i_executable_path: str) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Func ExecuteBackgroundProcessus(CATBSTR iExecutablePath) As
                | long
                |     Executes an asynchronous process. This process is launched in background
                |     and ExecuteBackgroundProcess doesn't wait for it to complete. If the executable
                |     to run needs a specific environment to works correctly (for example environment
                |     variables like PATH or LD_LIBRARY_PATH correctly set), this environment must
                |     have been set in order to make this method succeed. If this executable needs to
                |     be launched from a window, this method will fail.
                | 
                |     Parameters:
                | 
                |         iExecutablePath
                |             The path of the executable to run and its arguments
                |             If the executable is not present in the PATH environment
                |             variable, you must specify its complete absolute path.
                |             If this path contains blanks, you must enclose it
                |             with the simple quote character ''' : for example
                |             CATIA.SystemService.ExecuteBackgroundProcess
                |             "'C:\\Program Files\\myApp\\myApp.exe' myArg".
                | 
                |     Returns:
                |         Non significative return code. It's never the asynchronous process
                |         return code 
                | 
                | Example:
                |     This example executes the command located at
                | 
                |     and doesn't wait the end of its execution.
                | 
                |      CATIA.SystemService.ExecuteBackgroundProcessus ""

        :param str i_executable_path:
        :return: int
        """
        return self.com_object.ExecuteBackgroundProcessus(i_executable_path)

    def execute_processus(self, i_executable_path: str) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Func ExecuteProcessus(CATBSTR iExecutablePath) As long
                |     Executes a synchronous process. If this process is succesfully launched,
                |     ExecuteProcessus waits for it to terminate and returns the process return code.
                |     If the executable to run needs a specific environment to works correctly (for
                |     example environment variables like PATH or LD_LIBRARY_PATH correctly set), this
                |     environment must have been set in order to make this method succeed. If this
                |     executable needs to be launched from a window, this method will
                |     fail.
                | 
                |     Parameters:
                | 
                |         iExecutablePath
                |             The path of the executable to run and its arguments.
                |             If the executable is not present in the PATH environment
                |             variable, you must specify its complete absolute path.
                |             If this executable path contains blanks, you must
                |             enclose it with the simple quote character ''' :
                |             for example CATIA.SystemService.ExecuteProcessus
                |             "'C:\\Program Files\\myApp\\myApp.exe' myArg". On Windows,
                |             to run a batch file you must execute the command interpreter :
                |             set the executable to cmd.exe set the arguments to
                |             the following ones : /c plus the name of the batch file.
                |             For example CATIA.SystemService.ExecuteProcessus
                |             "cmd.exe /c E:\\MyBatchFile.bat" On Windows, an argument
                |             that contains a blank must be doubly enclosed ; first
                |             with the single quote character then, inside the single
                |             enclosing quote, with the double quote character.
                |             For example CATIA.SystemService.ExecuteProcessus
                |             "cmd.exe /c '" & Chr$(34) & "E:\\My Bat File.bat" & Chr$(34) & "'"
                | 
                |     Returns:
                |         The synchronous process return code 
                | 
                | Example:
                |     This example executes the command located at
                | 
                |     waits for it to end, and returns its return code.
                | 
                |      ReturnCode = CATIA.SystemService.ExecuteProcessus("")

        :param str i_executable_path:
        :return: int
        """
        return self.com_object.ExecuteProcessus(i_executable_path)

    def get_message(self, i_catalog_name: str, i_message_key: str, i_msg_parameters: tuple, i_default_msg: str) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Func GetMessage(CATBSTR iCatalogName,CATBSTR iMessageKey,CATSafeArrayVariant
                | iMsgParameters,CATBSTR iDefaultMsg) As CATBSTR
                |     Computes a alphanumeric string from a message from a message catalog using
                |     the catalog name, the message key, the message parameters and a default NLS
                |     message.
                | 
                |     Parameters:
                | 
                |         iCatalogName
                |             Name of the catalog containing the message, without the .CATNls
                |             suffix. This catalog will be searched in the directories from the environment
                |             variable CATMsgCatalogPath. 
                |         iMessageKey
                |             Key of the message to be retrieved 
                |         iMsgParameters
                |             Array giving to the method possible parameter values which the
                |             method will integrate into the parameterized message. The parameter value count
                |             should correspond to the message parameter highest index (this is not exactly
                |             the parameter count: the software authorizes parameter indices that are not
                |             consecutive, which would distinguish the message parameters highest index from
                |             the parameter count). If the input parameter value count is not sufficient, a
                |             default behaviour is foreseen: "?" characters are introduced into the computed
                |             output resource string. 
                |         iDefaultMsg
                |             Message to be used if a problem occured while accessing the message
                |             catalog file or the key. You may, for example, put in this message an
                |             information about an access problem. 
                |         oMessage
                |             The built message. 
                |         Example:
                |             This example computes in MyErrorMessage the message associated to
                |             the couple catalog CATSysCommunication / key
                |             CATSysComReentranceError_152005.Request
                | 
                |              Dim MsgParams()
                |              Dim MyErrorMessage
                |              MyErrorMessage = CATIA.SystemService.GetMessage("CATSysCommunication", "CATSysComReentranceError_152005.Request", MsgParams, "MsgCatalogError")

        :param str i_catalog_name:
        :param str i_message_key:
        :param tuple i_msg_parameters:
        :param str i_default_msg:
        :return: str
        """
        return self.com_object.GetMessage(i_catalog_name, i_message_key, i_msg_parameters, i_default_msg)

    def print(self, i_string: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Sub Print(CATBSTR iString)
                | 
                |     Deprecated:
                |         R213 Use SystemService.PrintToStdout instead.
                |         Precondition: Print is a reserved keyword of VBA then this method
                |         cannot be used in a VBA macro. Prints a string on stdout.
                |         
                |     Parameters:
                | 
                |         iString
                |             The string to print 
                | 
                |     Example:
                |         This example prints the string "Hello world!".
                | 
                |          CATIA.SystemService.Print("Hello world!")

        :param str i_string:
        :return: None
        """
        return self.com_object.Print(i_string)

    def print_to_stdout(self, i_string: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Sub PrintToStdout(CATBSTR iString)
                |     Prints a string on stdout.
                | 
                |     Parameters:
                | 
                |         iString
                |             The string to print 
                | 
                |     Example:
                |         This example prints the string "Hello world!".
                | 
                |          CATIA.SystemService.PrintToStdout("Hello world!")

        :param str i_string:
        :return: None
        """
        return self.com_object.PrintToStdout(i_string)

    def __repr__(self):
        return f'SystemService(name="{self.name}")'
