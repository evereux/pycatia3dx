"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class OLPCustomCommand(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     OlpCustomCommand
                | 
                | Native Robot Language(NRL) Teach command.
                | 
                | This interface can only be used by a translator within the Robotics Off-line
                | Programming (OLP) NRL Teach command.
                | This interface represents a command added to NRL teach which is activate by a
                | user to perform some customized action. This interface is used to control what
                | happens when they click on that command. AnyObject.Name is the label displayed
                | in the UI for this command. A new command is created with
                | OlpTeachHelper.AddCustomCommand.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def main_command(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property MainCommand() As CATBSTR
                |     The ID of the custom command for the macro.
                |     If set to "" (empty string) then MacroRunCommand is not called. Any other
                |     value is for use in MacroRunCommand to identify which command is being
                |     executed. There is nothing to prevent two commands from having the same value
                |     for MainCommand or to prevent two commands from having the same AnyObject.Name.

        :return: str
        """

        return self.com_object.MainCommand

    @main_command.setter
    def main_command(self, value: str):
        """
        :param str value:
        """

        self.com_object.MainCommand = value

    @property
    def post_command(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property PostCommand() As DELOlpTeachCommand
                |     Built-in command that is executed after MacroRunCommand.
                |     This can be changed during MacroRunCommand. If MacroRunCommand fails (does
                |     not set OlpTranslatorHelper.CallSucceeded to True), the this command will not
                |     be executed. delOlpCmdModify cannot be set for the PostCommand. This is because
                |     delOlpCmdModify will overwrite any changes to the current instruction which
                |     have been done in the MainCommand.

        :return: DELOlpTeachCommand
        """

        return self.com_object.PostCommand

    @post_command.setter
    def post_command(self, value: int):
        """
        :param int value:
        """

        self.com_object.PostCommand = value

    @property
    def pre_command(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property PreCommand() As DELOlpTeachCommand
                |     Built-in command that is executed before MacroRunCommand.
                |     If this command fails, then MacroRunCommand will not be executed.

        :return: DELOlpTeachCommand
        """

        return self.com_object.PreCommand

    @pre_command.setter
    def pre_command(self, value: int):
        """
        :param int value:
        """

        self.com_object.PreCommand = value

    def __repr__(self):
        return f'OLPCustomCommand(name="{ self.name }")'
