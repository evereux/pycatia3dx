"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.todo_del_robot_simulation.rsc_data_entity import RscDataEntity
from pycatia3dx.todo_del_robot_simulation.rsc_instruction import RscInstruction


class RscPulse(RscInstruction):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     DELRobotSimulationIDLItf.RscInstruction
                |                         RscPulse
                | 
                | Interface representing a Resource Pulse Instruction.
                | 
                | Role: This interface represents a RscPulse Instruction in a Resource
                | Task
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def delay(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Delay() As double
                |     Get/Set the pulse's delay.
                | 
                |     Returns:
                |         oDelay The returned delay. 
                |     Parameters:
                | 
                |         iDelay
                |             The delay before pulse. 
                | 
                |     Example:
                | 
                |            
                | 
                |            Dim oResourceTask As ResourceTask2
                |            ......
                |            Dim ResourceSequence As RscSequence
                |            Set ResourceSequence = oResourceTask.MainRscSequence
                |            ......
                |            Dim iIndex
                |            iIndex=-1
                |            Dim oCreatedPulse As RscPulse
                |            Set oCreatedPulse = ResourceSequence.CreateRscPulse(iIndex)
                |            Dim Delay
                |            Delay = oCreatedPulse.Delay
                |            ......
                |            oCreatedPulse.Delay = Delay

        :return: float
        """

        return self.com_object.Delay

    @delay.setter
    def delay(self, value: float):
        """
        :param float value:
        """

        self.com_object.Delay = value

    @property
    def duration(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Duration() As double
                |     Get/Set the pulse's duration.
                | 
                |     Returns:
                |         oDuration The returned duration. 
                |     Parameters:
                | 
                |         iDuration
                |             The pulse duration. Duration value has to be different from zero.
                |             
                | 
                |     Example:
                | 
                |            
                | 
                |            Dim oResourceTask As ResourceTask2
                |            ......
                |            Dim ResourceSequence As RscSequence
                |            Set ResourceSequence = oResourceTask.MainRscSequence
                |            ......
                |            Dim iIndex
                |            iIndex=-1
                |            Dim oCreatedPulse As RscPulse
                |            Set oCreatedPulse = ResourceSequence.CreateRscPulse(iIndex)
                |            Dim oDuration
                |            oDuration = oCreatedPulse.Duration
                |            ......
                |            oCreatedPulse.Duration = oDuration

        :return: float
        """

        return self.com_object.Duration

    @duration.setter
    def duration(self, value: float):
        """
        :param float value:
        """

        self.com_object.Duration = value

    @property
    def pulse_data_entity(self) -> RscDataEntity:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property PulseDataEntity() As RscDataEntity
                |     Get/Set the pulsed Data Entity.
                | 
                |     Returns:
                |         oPulseDataEntity The returned pulsed entity. 
                |     Parameters:
                | 
                |         iPulseDataEntity
                |             The new pulsed entity. 
                | 
                |     Example:
                | 
                |            
                | 
                |            Dim oResourceTask As ResourceTask2
                |            ......
                |            Dim ResourceSequence As RscSequence
                |            Set ResourceSequence = oResourceTask.MainRscSequence
                |            ......
                |            Dim iIndex
                |            iIndex=-1
                |            Dim oCreatedPulse As RscPulse
                |            Set oCreatedPulse = ResourceSequence.CreateRscPulse(iIndex)
                |            Dim PulseDataEntity As RscDataEntity
                |            Set PulseDataEntity = oCreatedPulse.PulseDataEntity
                |            ......
                |            oCreatedPulse.PulseDataEntity = PulseDataEntity

        :return: RscDataEntity
        """

        return RscDataEntity(self.com_object.PulseDataEntity)

    @pulse_data_entity.setter
    def pulse_data_entity(self, value: RscDataEntity):
        """
        :param RscDataEntity value:
        """

        self.com_object.PulseDataEntity = value

    @property
    def value(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Value() As CATBSTR
                |     Get/Set the Value pulsed to this Data Entity.
                | 
                |     Returns:
                |         oValue The returned pulsed value. 
                |     Parameters:
                | 
                |         iValue
                |             The new pulsed value. 
                | 
                |     Example:
                | 
                |            
                | 
                |            Dim oResourceTask As ResourceTask2
                |            ......
                |            Dim ResourceSequence As RscSequence
                |            Set ResourceSequence = oResourceTask.MainRscSequence
                |            ......
                |            Dim iIndex
                |            iIndex=-1
                |            Dim oCreatedPulse As RscPulse
                |            Set oCreatedPulse = ResourceSequence.CreateRscPulse(iIndex)
                |            Dim Value
                |            Value = oCreatedPulse.Value
                |            ......
                |            oCreatedPulse.Value = Value

        :return: str
        """

        return self.com_object.Value

    @value.setter
    def value(self, value: str):
        """
        :param str value:
        """

        self.com_object.Value = value

    def activate_invert_mode(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub ActivateInvertMode()
                |     Activates invert mode. With this mode, the value is no more a required
                |     parameter. Pulse values are evaluated at the time the instruction is executed.
                |     The first change inverts the value. The second change restores the previous
                |     value (If duration is not infinite).
                | 
                |     Example:
                | 
                |            
                | 
                |            Dim oResourceTask As ResourceTask2
                |            ......
                |            Dim ResourceSequence As RscSequence
                |            ResourceSequence = oResourceTask.MainRscSequence
                |            ......
                |            Dim iIndex
                |            iIndex=-1
                |            Dim oCreatedPulse As RscPulse
                |            Call ResourceSequence.CreateRscPulse(iIndex,oCreatedPulse)
                |            Call  oCreatedPulse.ActivateInvertMode()

        :return: None
        """
        return self.com_object.ActivateInvertMode()

    def de_activate_invert_mode(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub DeActivateInvertMode()
                |     Deactivates invert mode.
                | 
                |     Example:
                | 
                |            
                | 
                |            Dim oResourceTask As ResourceTask2
                |            ......
                |            Dim ResourceSequence As RscSequence
                |            Set ResourceSequence = oResourceTask.MainRscSequence
                |            ......
                |            Dim iIndex
                |            iIndex=-1
                |            Dim oCreatedPulse As RscPulse
                |            Set oCreatedPulse = ResourceSequence.CreateRscPulse(iIndex)
                |            Call  oCreatedPulse.DeActivateInvertMode()

        :return: None
        """
        return self.com_object.DeActivateInvertMode()

    def has_infinite_duration(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func HasInfiniteDuration() As boolean
                |     Returns if pulse has infinite duration.
                | 
                |     Returns:
                |         oInfiniteDurationStatus Returns if pulse has infinite duration. Legal
                |         values:
                | 
                |             TRUE : Infinite duration
                |             FALSE : Finite duration
                | 
                |     Example:
                | 
                |            
                | 
                |            Dim oResourceTask As ResourceTask2
                |            ......
                |            Dim ResourceSequence As RscSequence
                |            Set ResourceSequence = oResourceTask.MainRscSequence
                |            ......
                |            Dim iIndex
                |            iIndex=-1
                |            Dim oCreatedPulse As RscPulse
                |            Set oCreatedPulse = ResourceSequence.CreateRscPulse(iIndex)
                |            Dim oInfiniteDurationStatus
                |            oInfiniteDurationStatus = oCreatedPulse.HasInfiniteDuration()

        :return: bool
        """
        return self.com_object.HasInfiniteDuration()

    def is_invert_mode_activated(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func IsInvertModeActivated() As boolean
                |     Returns if invert mode is activated.
                | 
                |     Returns:
                |         oInvertModeActivationStatus Returns if invert mode is activated. Legal
                |         values:
                | 
                |             TRUE : Invert mode activated
                |             FALSE : Invert mode deactivated - Value is required.
                | 
                |     Example:
                | 
                |            
                | 
                |            Dim oResourceTask As ResourceTask2
                |            ......
                |            Dim ResourceSequence As RscSequence
                |            Set ResourceSequence = oResourceTask.MainRscSequence
                |            ......
                |            Dim iIndex
                |            iIndex=-1
                |            Dim oCreatedPulse As RscPulse
                |            Set oCreatedPulse = ResourceSequence.CreateRscPulse(iIndex)
                |            Dim oInvertModeActivationStatus
                |            oInvertModeActivationStatus = oCreatedPulse.IsInvertModeActivated()

        :return: bool
        """
        return self.com_object.IsInvertModeActivated()

    def set_infinite_duration(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetInfiniteDuration()
                |     Set infinite duration.
                | 
                |     Example:
                | 
                |            
                | 
                |            Dim oResourceTask As ResourceTask2
                |            ......
                |            Dim ResourceSequence As RscSequence
                |            Set ResourceSequence = oResourceTask.MainRscSequence
                |            ......
                |            Dim iIndex
                |            iIndex=-1
                |            Dim oCreatedPulse As RscPulse
                |            Set oCreatedPulse = ResourceSequence.CreateRscPulse(iIndex)
                |            Call  oCreatedPulse.SetInfiniteDuration()

        :return: None
        """
        return self.com_object.SetInfiniteDuration()

    def un_set_delay(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub UnSetDelay()
                |     Unset delay.
                | 
                |     Example:
                | 
                |            
                | 
                |            Dim oResourceTask As ResourceTask2
                |            ......
                |            Dim ResourceSequence As RscSequence
                |            Set ResourceSequence = oResourceTask.MainRscSequence
                |            ......
                |            Dim iIndex
                |            iIndex=-1
                |            Dim oCreatedPulse As RscPulse
                |            Set oCreatedPulse = ResourceSequence.CreateRscPulse(iIndex)
                |            Call  oCreatedPulse.UnSetDelay()

        :return: None
        """
        return self.com_object.UnSetDelay()

    def __repr__(self):
        return f'RscPulse(name="{ self.name }")'
