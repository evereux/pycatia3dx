"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class MachineInstruction(AnyObject):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MachineInstruction
                | 
                | Interface dedicated to machine instructions.
                | Role: This interface offers services to manage machine instruction
                | parameters.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def compute_axis_values(self, isp_surf: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub ComputeAxisValues(AnyObject ispSurf)
                |     Compute Axis Values for Accessory (Universal Holding
                |     Fixture).
                | 
                |     Parameters:
                | 
                |         ispSurf
                |             The handle to the Surface for which the Axis Values have to be
                |             computed.

        :param AnyObject isp_surf:
        :return: None
        """
        return self.com_object.ComputeAxisValues(isp_surf.com_object)

    def get_available_components_to_instruct(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetAvailableComponentsToInstruct() As CATSafeArrayVariant
                |     Returns device components which can be instructed.
                | 
                |     Returns:
                |         The list of available components.

        :return: tuple
        """
        return self.com_object.GetAvailableComponentsToInstruct()

    def get_axis_involved(self, i_index: int, o_axis_involvement: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetAxisInvolved(long iIndex,long oAxisInvolvement)
                |     Get axis involved in machine instruction.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             DOF Index (starts from 0). 
                |         oAxisInvolvement
                |             The integer indicating the axis involvement.
                | 
                |                 0: Axis is not involved.
                |                 1: Axis is involved, state is Free.
                |                 2: Axis is involved, state is Locked.

        :param int i_index:
        :param int o_axis_involvement:
        :return: None
        """
        return self.com_object.GetAxisInvolved(i_index, o_axis_involvement)

    def get_axis_involvement(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetAxisInvolvement() As CATSafeArrayVariant
                |     Gets axes involved in machine instruction.
                | 
                |     Returns:
                |         The list of integers indicating the axis involvement, the length of the
                |         list is same than the Number of DOFs on the instructed
                |         component.
                | 
                |             0: Axis is not involved.
                |             1: Axis is involved, state is Free.
                |             2: Axis is involved, state is Locked.

        :return: tuple
        """
        return self.com_object.GetAxisInvolvement()

    def get_axis_value(self, i_index: int, o_axis_value: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetAxisValue(long iIndex,double oAxisValue)
                |     Get the axis value of instructed component.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             DOF Index (starts from 0). 
                |         oAxisValue
                |             Axis value. Units are meters for linear axis and radians for rotary
                |             axis.

        :param int i_index:
        :param float o_axis_value:
        :return: None
        """
        return self.com_object.GetAxisValue(i_index, o_axis_value)

    def get_axis_values(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetAxisValues() As CATSafeArrayVariant
                |     Gets the axis values of instructed component.
                | 
                |     Returns:
                |         List of axis values. Units are meters for linear axis and radians for
                |         rotary axis.

        :return: tuple
        """
        return self.com_object.GetAxisValues()

    def get_device_axis_involved(self, i_device_component: AnyObject, i_index: int, o_axis_involvement: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetDeviceAxisInvolved(AnyObject iDeviceComponent,long iIndex,long
                | oAxisInvolvement)
                |     Get the Axis involvement of a specific axis of a specfic component in the
                |     Machine Instruction activity.
                | 
                |     Parameters:
                | 
                |         iDeviceComponent
                |             The handle to the device/component for which the axis involvement
                |             is required 
                |         iIndex
                |             DOF Index (starts from 0). 
                |         oAxisInvolvement
                |             The integer indicating the axis involvement.
                | 
                |                 0: Axis is not involved.
                |                 1: Axis is involved, state is Free.
                |                 2: Axis is involved, state is Locked.

        :param AnyObject i_device_component:
        :param int i_index:
        :param int o_axis_involvement:
        :return: None
        """
        return self.com_object.GetDeviceAxisInvolved(i_device_component.com_object, i_index, o_axis_involvement)

    def get_device_axis_involvement(self, i_device_component: AnyObject) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetDeviceAxisInvolvement(AnyObject iDeviceComponent) As
                | CATSafeArrayVariant
                |     Get the Axis involvement of the specific component involved in the Machine
                |     Instruction activity.
                | 
                |     Parameters:
                | 
                |         iDeviceComponent
                |             The instructed component for which the axis involvement is required
                |             
                |         oAxisInvolvement
                |             List of integer indicating the Axis involvement, the length of the
                |             list is same as the Number of DOFs of
                |             iDeviceComponent
                | 
                |                 0: Axis is not involved.
                |                 1: Axis is involved, state is Free.
                |                 2: Axis is involved, state is Locked.

        :param AnyObject i_device_component:
        :return: tuple
        """
        return self.com_object.GetDeviceAxisInvolvement(i_device_component.com_object)

    def get_device_axis_priority(self, i_device_component: AnyObject, i_index: int, o_axis_priority: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetDeviceAxisPriority(AnyObject iDeviceComponent,long iIndex,long
                | oAxisPriority)
                |     Get the Axis Priority of a specific axis of a specfic component in the
                |     Machine Instruction activity.
                | 
                |     Parameters:
                | 
                |         iDeviceComponent
                |             The component for which the axis priority is required
                |             
                |         iIndex
                |             DOF Index (starts from 0). 
                |         oAxisPriority
                |             Axis Priority

        :param AnyObject i_device_component:
        :param int i_index:
        :param int o_axis_priority:
        :return: None
        """
        return self.com_object.GetDeviceAxisPriority(i_device_component.com_object, i_index, o_axis_priority)

    def get_device_axis_prioritys(self, i_device_component: AnyObject) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetDeviceAxisPrioritys(AnyObject iDeviceComponent) As
                | CATSafeArrayVariant
                |     Get the Axis Priority of the specific component involved in the Machine
                |     Instruction activity.
                | 
                |     Parameters:
                | 
                |         iDeviceComponent
                |             The component for which the axis priority is required
                |             
                |         oAxisPriority
                |             List of integer indicating the Axis priority, the length of the
                |             list is equal to the Number of DOFs of ispComponent

        :param AnyObject i_device_component:
        :return: tuple
        """
        return self.com_object.GetDeviceAxisPrioritys(i_device_component.com_object)

    def get_device_axis_value(self, i_device_component: AnyObject, i_index: int, o_axis_value: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetDeviceAxisValue(AnyObject iDeviceComponent,long iIndex,double
                | oAxisValue)
                |     Get the Axis Values of a specific axis of a specfic component in the
                |     Machine Instruction activity.
                | 
                |     Parameters:
                | 
                |         iDeviceComponent
                |             The component for which the axis value is required
                |             
                |         iIndex
                |             DOF Index (starts from 0). 
                |         oAxisValue
                |             Axis value. Units are meters for linear axis and radians for rotary
                |             axis.

        :param AnyObject i_device_component:
        :param int i_index:
        :param float o_axis_value:
        :return: None
        """
        return self.com_object.GetDeviceAxisValue(i_device_component.com_object, i_index, o_axis_value)

    def get_device_axis_values(self, i_device_component: AnyObject) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetDeviceAxisValues(AnyObject iDeviceComponent) As
                | CATSafeArrayVariant
                |     Get the Axis Values of the specific component involved in the Machine
                |     Instruction activity.
                | 
                |     Parameters:
                | 
                |         iDeviceComponent
                |             The component for which the axis values is required
                |             
                |         oAxisValues
                |             List of axis values. Units are meters for linear axis and radians
                |             for rotary axis.

        :param AnyObject i_device_component:
        :return: tuple
        """
        return self.com_object.GetDeviceAxisValues(i_device_component.com_object)

    def get_feedrate_mode(self, o_feedrate_mode: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetFeedrateMode(long oFeedrateMode)
                |     Get the feed rate mode of the Machine Instruction
                |     activity.
                | 
                |     Parameters:
                | 
                |         oFeedrateMode
                |             The integer indicating the feed rate mode.
                | 
                |                 0: By Value.
                |                 1: Rapid.

        :param int o_feedrate_mode:
        :return: None
        """
        return self.com_object.GetFeedrateMode(o_feedrate_mode)

    def get_feedrate_values(self, o_linear_feedrate: float, o_angular_feedrate: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetFeedrateValues(double oLinearFeedrate,double
                | oAngularFeedrate)
                |     Get the feed rate values of the Machine Instruction
                |     activity.
                | 
                |     Parameters:
                | 
                |         oLinearFeedrate
                |             Linear feedrate value. Units is Metre/Second 
                |         oAngularFeedrate
                |             Angular feedrate value. Unit is Radian/Second

        :param float o_linear_feedrate:
        :param float o_angular_feedrate:
        :return: None
        """
        return self.com_object.GetFeedrateValues(o_linear_feedrate, o_angular_feedrate)

    def get_instructed_component(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetInstructedComponent() As AnyObject
                |     Returns the machine component on which machine instruction is
                |     applied.
                | 
                |     Returns:
                |         The device component.

        :return: AnyObject
        """
        return AnyObject(self.com_object.GetInstructedComponent())

    def get_list_of_instructed_component(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetListOfInstructedComponent() As CATSafeArrayVariant

        :return: tuple
        """
        return self.com_object.GetListOfInstructedComponent()

    def set_axis_involved(self, i_index: int, i_axis_involvement: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetAxisInvolved(long iIndex,long iAxisInvolvement)
                |     Set the axis involved in machine instruction.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             DOF Index (starts from 0). 
                |         iAxisInvolvement
                |             The integer indicating the axis involvement.
                | 
                |                 0: Axis is not involved.
                |                 1: Axis is involved, state is Free.
                |                 2: Axis is involved, state is Locked.

        :param int i_index:
        :param int i_axis_involvement:
        :return: None
        """
        return self.com_object.SetAxisInvolved(i_index, i_axis_involvement)

    def set_axis_involvement(self, i_axis_involvement: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2026-02-08 14:05:01.675948))
                | Sub SetAxisInvolvement(CATSafeArrayVariant iAxisInvolvement)
                |     Sets the axes involved in machine instruction.
                |
                |     Parameters:
                |
                |         iAxisInvolvement
                |             The list of integers indicating the axis involvement, the length of
                |             the list should be same than the Number of DOFs on the instructed
                |             component.
                |
                |                 0: Axis is not involved.
                |                 1: Axis is involved, state is Free.
                |                 2: Axis is involved, state is Locked.

        :param tuple i_axis_involvement:
        :return: None
        """
        return self.com_object.SetAxisInvolvement(i_axis_involvement)
        # todo: check this method, does it require system service?
        # Autogenerated comment:
        # some methods require a system service call as the methods expects a vb array object
        # passed to it and there is no way to do this directly with python. In those cases the following code
        # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # vba_function_name = 'set_axis_involvement'
        # vba_code = """
        # Public Function set_axis_involvement(machine_instruction)
        #     Dim iAxisInvolvement (2)
        #     machine_instruction.SetAxisInvolvement iAxisInvolvement
        #     set_axis_involvement = iAxisInvolvement
        # End Function
        # """

        # system_service = SystemService(self.application.SystemService)
        # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_axis_priorities(self, i_axis_priority: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2026-02-08 14:05:01.675948))
                | Sub SetAxisPrioritys(CATSafeArrayVariant iAxisPriority)
                |     Set the Axis Priority of all the components involved in the Machine
                |     Instruction activity.
                |
                |     Parameters:
                |
                |         iAxisPriority
                |             List of integer indicating the Axis priority, the length of the
                |             list is equal to the sum of the Number of DOFs of all the instructed
                |             device/components

        :param tuple i_axis_priority:
        :return: None
        """
        return self.com_object.SetAxisPrioritys(i_axis_priority)
        # todo: check this method, does it require system service?
        # Autogenerated comment:
        # some methods require a system service call as the methods expects a vb array object
        # passed to it and there is no way to do this directly with python. In those cases the following code
        # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # vba_function_name = 'set_axis_prioritys'
        # vba_code = """
        # Public Function set_axis_prioritys(machine_instruction)
        #     Dim iAxisPriority (2)
        #     machine_instruction.SetAxisPrioritys iAxisPriority
        #     set_axis_prioritys = iAxisPriority
        # End Function
        # """

        # system_service = SystemService(self.application.SystemService)
        # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_axis_value(self, i_index: int, i_axis_value: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetAxisValue(long iIndex,double iAxisValue)
                |     Set the axis value of instructed component.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             DOF Index (starts from 0). 
                |         iAxisValue
                |             Axis value. Units are meters for linear axis and radians for rotary
                |             axis.

        :param int i_index:
        :param float i_axis_value:
        :return: None
        """
        return self.com_object.SetAxisValue(i_index, i_axis_value)

    def set_axis_values(self, i_axis_values: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2026-02-08 14:05:01.675948))
                | Sub SetAxisValues(CATSafeArrayVariant iAxisValues)
                |     Sets the axis values of instructed component.
                |
                |     Parameters:
                |
                |         iAxisValues
                |             List of axis values. Units are meters for linear axis and radians
                |             for rotary axis.

        :param tuple i_axis_values:
        :return: None
        """
        return self.com_object.SetAxisValues(i_axis_values)
        # todo: check this method, does it require system service?
        # Autogenerated comment:
        # some methods require a system service call as the methods expects a vb array object
        # passed to it and there is no way to do this directly with python. In those cases the following code
        # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # vba_function_name = 'set_axis_values'
        # vba_code = """
        # Public Function set_axis_values(machine_instruction)
        #     Dim iAxisValues (2)
        #     machine_instruction.SetAxisValues iAxisValues
        #     set_axis_values = iAxisValues
        # End Function
        # """

        # system_service = SystemService(self.application.SystemService)
        # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_device_axis_involved(self, i_device_component: AnyObject, i_index: int, i_axis_involvement: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetDeviceAxisInvolved(AnyObject iDeviceComponent,long iIndex,long
                | iAxisInvolvement)
                |     Set the Axis involvement of a specific axis of a specfic component in the
                |     Machine Instruction activity.
                | 
                |     Parameters:
                | 
                |         iDeviceComponent
                |             The instructed component for which the specific axis involvement is
                |             to be set 
                |         iIndex
                |             DOF Index (starts from 0). 
                |         iAxisInvolvement
                |             The integer indicating the axis involvement.
                | 
                |                 0: Axis is not involved.
                |                 1: Axis is involved, state is Free.
                |                 2: Axis is involved, state is Locked.

        :param AnyObject i_device_component:
        :param int i_index:
        :param int i_axis_involvement:
        :return: None
        """
        return self.com_object.SetDeviceAxisInvolved(i_device_component.com_object, i_index, i_axis_involvement)

    def set_device_axis_priority(self, i_device_component: AnyObject, i_index: int, i_axis_priority: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetDeviceAxisPriority(AnyObject iDeviceComponent,long iIndex,long
                | iAxisPriority)
                |     Set the Axis Priority of a specific axis of a specfic component in the
                |     Machine Instruction activity.
                | 
                |     Parameters:
                | 
                |         iDeviceComponent
                |             The component for which the axis priority is to be set
                |             
                |         iIndex
                |             DOF Index (starts from 0). 
                |         iAxisPriority
                |             Axis Priority

        :param AnyObject i_device_component:
        :param int i_index:
        :param int i_axis_priority:
        :return: None
        """
        return self.com_object.SetDeviceAxisPriority(i_device_component.com_object, i_index, i_axis_priority)

    def set_device_axis_value(self, i_device_component: AnyObject, i_index: int, i_axis_value: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetDeviceAxisValue(AnyObject iDeviceComponent,long iIndex,double
                | iAxisValue)
                |     Set the Axis Value of a specific axis of a specfic component in the Machine
                |     Instruction activity.
                | 
                |     Parameters:
                | 
                |         iDeviceComponent
                |             The component for which the axis value is to be set
                |             
                |         iIndex
                |             DOF Index (starts from 0). 
                |         iAxisValue
                |             Axis value. Units are meters for linear axis and radians for rotary
                |             axis.

        :param AnyObject i_device_component:
        :param int i_index:
        :param float i_axis_value:
        :return: None
        """
        return self.com_object.SetDeviceAxisValue(i_device_component.com_object, i_index, i_axis_value)

    def set_feedrate_mode(self, i_feedrate_mode: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetFeedrateMode(long iFeedrateMode)
                |     Set the feed rate mode of the Machine Instruction
                |     activity.
                | 
                |     Parameters:
                | 
                |         iFeedrateMode
                |             The integer indicating the feed rate mode.
                | 
                |                 0: By Value.
                |                 1: Rapid.

        :param int i_feedrate_mode:
        :return: None
        """
        return self.com_object.SetFeedrateMode(i_feedrate_mode)

    def set_feedrate_values(self, i_linear_feedrate: float, i_angular_feedrate: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetFeedrateValues(double iLinearFeedrate,double
                | iAngularFeedrate)
                |     Set the feed rate values of the Machine Instruction
                |     activity.
                | 
                |     Parameters:
                | 
                |         iLinearFeedrate
                |             Linear feedrate value. Units is Metre/Second 
                |         iAngularFeedrate
                |             Angular feedrate value. Unit is Radian/Second

        :param float i_linear_feedrate:
        :param float i_angular_feedrate:
        :return: None
        """
        return self.com_object.SetFeedrateValues(i_linear_feedrate, i_angular_feedrate)

    def set_instructed_component(self, i_device_component: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetInstructedComponent(AnyObject iDeviceComponent)
                |     Sets the machine component on which machine instruction is
                |     applied.
                | 
                |     Parameters:
                | 
                |         iDeviceComponent
                |             The handle to the device/component that is being instructed.

        :param AnyObject i_device_component:
        :return: None
        """
        return self.com_object.SetInstructedComponent(i_device_component.com_object)

    def set_list_of_instructed_component(self, i_list_components: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2026-02-08 14:05:01.675948))
                | Sub SetListOfInstructedComponent(CATSafeArrayVariant
                | iListComponents)
                |
                | Copyright © 1999-2024, Dassault Systèmes. All rights reserved.

        :param tuple i_list_components:
        :return: None
        """
        return self.com_object.SetListOfInstructedComponent(i_list_components)
        # todo: check this method, does it require system service?
        # Autogenerated comment:
        # some methods require a system service call as the methods expects a vb array object
        # passed to it and there is no way to do this directly with python. In those cases the following code
        # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # vba_function_name = 'set_list_of_instructed_component'
        # vba_code = """
        # Public Function set_list_of_instructed_component(machine_instruction)
        #     Dim iListComponents (2)
        #     machine_instruction.SetListOfInstructedComponent iListComponents
        #     set_list_of_instructed_component = iListComponents
        # End Function
        # """

        # system_service = SystemService(self.application.SystemService)
        # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'MachineInstruction(name="{self.name}")'
