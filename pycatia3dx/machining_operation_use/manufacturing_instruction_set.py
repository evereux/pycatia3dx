"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class ManufacturingInstructionSet(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     ManufacturingInstructionSet
                | 
                | Interface defining drilling riveting instruction set.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def insert_mode(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property InsertMode() As long
                |     Returns or sets insert mode of local instruction set.
                | 
                |         0: Replace
                |         1: Insert After
                |         2: Insert Before

        :return: int
        """

        return self.com_object.InsertMode

    @insert_mode.setter
    def insert_mode(self, value: int):
        """
        :param int value:
        """

        self.com_object.InsertMode = value

    @property
    def usage(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Usage() As long
                |     Returns or sets scope of usage.
                | 
                |         0: Any
                |         1: Local
                |         2: Global

        :return: int
        """

        return self.com_object.Usage

    @usage.setter
    def usage(self, value: int):
        """
        :param int value:
        """

        self.com_object.Usage = value

    def add_action(self, i_mode: int, i_action_type: str) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func AddAction(long iMode,CATBSTR iActionType) As AnyObject
                |     Adds an action.
                | 
                |     Parameters:
                | 
                |         iActionType
                |             Authorized values are :
                | 
                |                 MfgInstructionSetMotionMove
                |                 MfgInstructionSetMotionVisibility
                |                 MfgInstructionSetMotionDwell
                |                 MfgInstructionSetMotionTCP
                |                 MfgInstructionSetMotionPP
                | 
                |     Returns:
                |         The created action

        :param int i_mode:
        :param str i_action_type:
        :return: AnyObject
        """
        return AnyObject(self.com_object.AddAction(i_mode, i_action_type))

    def add_parameter(self, i_type: int) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func AddParameter(long iType) As AnyObject
                |     Adds a parameter.
                | 
                |     Parameters:
                | 
                |         iType
                |             Authorized values are:
                | 
                |                 0:Boolean
                |                 1:Integer
                |                 2:Real
                |                 3:String
                |                 4:Length
                |                 5:Angle
                |                 6:Time
                |                 7:LinearFeedRate
                |                 8:AngularFeedRate
                | 
                |     Returns:
                |         The created parameter

        :param int i_type:
        :return: AnyObject
        """
        return AnyObject(self.com_object.AddParameter(i_type))

    def delete_action(self, i_mode: int, i_position: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub DeleteAction(long iMode,long iPosition)
                |     Deletes an action.
                | 
                |     Parameters:
                | 
                |         iPosition
                |             The index of action to delete

        :param int i_mode:
        :param int i_position:
        :return: None
        """
        return self.com_object.DeleteAction(i_mode, i_position)

    def delete_parameter(self, i_position: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub DeleteParameter(long iPosition)
                |     Deletes a parameter.
                | 
                |     Parameters:
                | 
                |         iPosition
                |             The index of parameter to delete

        :param int i_position:
        :return: None
        """
        return self.com_object.DeleteParameter(i_position)

    def get_action(self, i_mode: int, i_position: int) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetAction(long iMode,long iPosition) As AnyObject
                |     Gets an action.
                | 
                |     Parameters:
                | 
                |         iPosition
                |             The index of action to access. 
                | 
                |     Returns:
                |         The corresponding action

        :param int i_mode:
        :param int i_position:
        :return: AnyObject
        """
        return AnyObject(self.com_object.GetAction(i_mode, i_position))

    def get_number_of_actions(self, i_mode: int) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetNumberOfActions(long iMode) As long
                |     Returns the number of actions.
                | 
                |     Parameters:
                | 
                |         oNumber
                |             The number of actions

        :param int i_mode:
        :return: int
        """
        return self.com_object.GetNumberOfActions(i_mode)

    def get_number_of_parameters(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetNumberOfParameters() As long
                |     Returns the number of parameters.
                | 
                |     Returns:
                |         The number of parameters

        :return: int
        """
        return self.com_object.GetNumberOfParameters()

    def get_parameter(self, i_position: int) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetParameter(long iPosition) As AnyObject
                |     Gets a parameter.
                | 
                |     Parameters:
                | 
                |         iPosition
                |             The index of parameter to access. 
                | 
                |     Returns:
                |         The corresponding parameter

        :param int i_position:
        :return: AnyObject
        """
        return AnyObject(self.com_object.GetParameter(i_position))

    def __repr__(self):
        return f'ManufacturingInstructionSet(name="{ self.name }")'
