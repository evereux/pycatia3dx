"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class DrillingRivetingOperation(AnyObject):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     DrillingRivetingOperation
                | 
                | Interface defining drilling riveting operation.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def tcp(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property TCP() As CATBSTR
                |     Returns or sets the name of TCP of operation.

        :return: str
        """

        return self.com_object.TCP

    @tcp.setter
    def tcp(self, value: str):
        """
        :param str value:
        """

        self.com_object.TCP = value

    def get_fastener_offset(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetFastenerOffset() As AnyObject
                |     Returns the default fastener offset set associated with the
                |     operation.
                | 
                |     Returns:
                |         The fastener offset 
                |     See also:
                |         ManufacturingFastenerOffset

        :return: AnyObject
        """
        return AnyObject(self.com_object.GetFastenerOffset())

    def get_fastener_offset_from_position(self, i_position_index: int) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetFastenerOffsetFromPosition(long iPositionIndex) As
                | AnyObject
                |     Retrieves the local Fastener Offset of a dedicated work
                |     point.
                | 
                |     Parameters:
                | 
                |         iPositionIndex
                |             The index of fastener position (work point) 
                | 
                |     Returns:
                |         The fastener offset 
                |     See also:
                |         ManufacturingFastenerOffset

        :param int i_position_index:
        :return: AnyObject
        """
        return AnyObject(self.com_object.GetFastenerOffsetFromPosition(i_position_index))

    def get_instruction_set(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetInstructionSet() As AnyObject
                |     Returns the default instruction set associated with the
                |     operation.
                | 
                |     Returns:
                |         The instruction set 
                |     See also:
                |         ManufacturingInstructionSet

        :return: AnyObject
        """
        return AnyObject(self.com_object.GetInstructionSet())

    def get_instruction_set_from_position(self, i_position_index: int) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetInstructionSetFromPosition(long iPositionIndex) As
                | AnyObject
                |     Retrieves the local instruction set of a dedicated work
                |     point.
                | 
                |     Parameters:
                | 
                |         iPositionIndex
                |             The index of fastener position (work point) 
                | 
                |     Returns:
                |         The instruction set 
                |     See also:
                |         ManufacturingInstructionSet

        :param int i_position_index:
        :return: AnyObject
        """
        return AnyObject(self.com_object.GetInstructionSetFromPosition(i_position_index))

    def get_instruction_set_parameters(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetInstructionSetParameters() As CATSafeArrayVariant
                |     Returns the public parameters of instruction set evaluated in context of
                |     the operation.
                | 
                |     Returns:
                |         The list of parameters

        :return: tuple
        """
        return self.com_object.GetInstructionSetParameters()

    def get_instruction_set_parameters_from_position(self, i_position_index: int) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetInstructionSetParametersFromPosition(long iPositionIndex) As
                | CATSafeArrayVariant
                |     Returns the public parameters of instruction set evaluated in context of
                |     the operation and defined at a dedicated work point.
                | 
                |     Parameters:
                | 
                |         iPositionIndex
                |             The index of fastener position (work point) 
                | 
                |     Returns:
                |         The list of parameters

        :param int i_position_index:
        :return: tuple
        """
        return self.com_object.GetInstructionSetParametersFromPosition(i_position_index)

    def get_lateral_axis_direction(self, o_lateral_axis_mode: int) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetLateralAxisDirection(long oLateralAxisMode) As
                | CATSafeArrayVariant
                |     Retrieves the lateral axis direction when choosen mode is fixed. It fails
                |     when the machine is not a robotic cell.
                | 
                |     Parameters:
                | 
                |         oLateralAxisMode
                |             The mode:
                | 
                |                 1:Fixed
                |                 2:Along the path
                |                 3:From manufacturing fasteners
                | 
                |     Returns:
                |         The direction coordinates as an array of 3 values

        :param int o_lateral_axis_mode:
        :return: tuple
        """
        return self.com_object.GetLateralAxisDirection(o_lateral_axis_mode)

    def get_macro_motions_from_position(self, i_position_index: int, i_force_creation: bool) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetMacroMotionsFromPosition(long iPositionIndex,boolean iForceCreation) As
                | AnyObject
                |     Retrieves the local macro motion of a dedicated work
                |     point.
                | 
                |     Parameters:
                | 
                |         iPositionIndex
                |             The index of fastener position (work point) 
                |         iForceCreation
                |             Set TRUE if you expect to modify returned macro motion
                |             
                | 
                |     Returns:
                |         The macro motion 
                |     See also:
                |         ManufacturingMacroMotions

        :param int i_position_index:
        :param bool i_force_creation:
        :return: AnyObject
        """
        return AnyObject(self.com_object.GetMacroMotionsFromPosition(i_position_index, i_force_creation))

    def get_manufacturing_fastener_from_position(self, i_position_index: int) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetManufacturingFastenerFromPosition(long iPositionIndex) As
                | AnyObject
                |     Retrieves the manufacturing fastener of a dedicated work
                |     point.
                | 
                |     Parameters:
                | 
                |         iPositionIndex
                |             The index of fastener position (work point) 
                | 
                |     Returns:
                |         The manufacturing fastener 
                |     See also:
                |         DrManufacturingFastener

        :param int i_position_index:
        :return: AnyObject
        """
        return AnyObject(self.com_object.GetManufacturingFastenerFromPosition(i_position_index))

    def get_offset_from_position(self, i_position_index: int) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetOffsetFromPosition(long iPositionIndex) As
                | CATSafeArrayVariant
                |     Retrieves the local offset of a dedicated work point.
                | 
                |     Parameters:
                | 
                |         iPositionIndex
                |             The index of fastener position (work point) 
                | 
                |     Returns:
                |         The offset matrix as an array of 12 values

        :param int i_position_index:
        :return: tuple
        """
        return self.com_object.GetOffsetFromPosition(i_position_index)

    def set_fastener_offset(self, i_f_offset: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetFastenerOffset(AnyObject iFOffset)
                |     Sets default fastener offset to the operation.
                | 
                |     Parameters:
                | 
                |         iFOffset
                |             The fastener offset to be assigned.

        :param AnyObject i_f_offset:
        :return: None
        """
        return self.com_object.SetFastenerOffset(i_f_offset.com_object)

    def set_fastener_offset_from_position(self, i_position_index: int, i_f_offset: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetFastenerOffsetFromPosition(long iPositionIndex,AnyObject
                | iFOffset)
                |     Sets the local Fastener Offset of a dedicated work point.
                | 
                |     Parameters:
                | 
                |         iPositionIndex
                |             The index of fastener position (work point) 
                |         iFOffset
                |             The fastener offset to be assigned.

        :param int i_position_index:
        :param AnyObject i_f_offset:
        :return: None
        """
        return self.com_object.SetFastenerOffsetFromPosition(i_position_index, i_f_offset.com_object)

    def set_instruction_set(self, i_instruction_set: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetInstructionSet(AnyObject iInstructionSet)
                |     Sets default instruction set to the operation.
                | 
                |     Parameters:
                | 
                |         iInstructionSet
                |             The instruction set to be assigned

        :param AnyObject i_instruction_set:
        :return: None
        """
        return self.com_object.SetInstructionSet(i_instruction_set.com_object)

    def set_instruction_set_from_position(self, i_position_index: int, i_instruction_set: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetInstructionSetFromPosition(long iPositionIndex,AnyObject
                | iInstructionSet)
                |     Sets the local instruction set of a dedicated work point.
                | 
                |     Parameters:
                | 
                |         iPositionIndex
                |             The index of fastener position (work point) 
                |         iInstructionSet
                |             The instruction set to be assigned

        :param int i_position_index:
        :param AnyObject i_instruction_set:
        :return: None
        """
        return self.com_object.SetInstructionSetFromPosition(i_position_index, i_instruction_set.com_object)

    def set_instruction_set_parameters(self, i_parameters: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2026-02-08 14:05:01.675948))
                | Sub SetInstructionSetParameters(CATSafeArrayVariant
                | iParameters)
                |     Sets the values of public parameters of instruction set evaluated in
                |     context of the operation.
                |
                |     Parameters:
                |
                |         iParameters
                |             The list of parameters values to be set

        :param tuple i_parameters:
        :return: None
        """
        return self.com_object.SetInstructionSetParameters(i_parameters)
        # todo: check this method, does it require system service?
        # Autogenerated comment:
        # some methods require a system service call as the methods expects a vb array object
        # passed to it and there is no way to do this directly with python. In those cases the following code
        # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # vba_function_name = 'set_instruction_set_parameters'
        # vba_code = """
        # Public Function set_instruction_set_parameters(drilling_riveting_operation)
        #     Dim iParameters (2)
        #     drilling_riveting_operation.SetInstructionSetParameters iParameters
        #     set_instruction_set_parameters = iParameters
        # End Function
        # """

        # system_service = SystemService(self.application.SystemService)
        # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_instruction_set_parameters_from_position(self, i_position_index: int, i_parameters: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetInstructionSetParametersFromPosition(long
                | iPositionIndex,CATSafeArrayVariant iParameters)
                |     Sets the values of public parameters of local instruction set evaluated in
                |     context of the operation.
                | 
                |     Parameters:
                | 
                |         iPositionIndex
                |             The index of fastener position (work point) 
                |         iParameters
                |             The list of parameters values to be set

        :param int i_position_index:
        :param tuple i_parameters:
        :return: None
        """
        return self.com_object.SetInstructionSetParametersFromPosition(i_position_index, i_parameters)

    def set_lateral_axis_direction(self, i_vec_coordinates: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2026-02-08 14:05:01.675948))
                | Sub SetLateralAxisDirection(CATSafeArrayVariant
                | iVecCoordinates)
                |     Sets the lateral axis direction and forces mode to fixed. It fails when the
                |     machine is not a robotic cell.
                |
                |     Parameters:
                |
                |         iVecCoordinates
                |             The direction coordinates as an array of 3 values

        :param tuple i_vec_coordinates:
        :return: None
        """
        return self.com_object.SetLateralAxisDirection(i_vec_coordinates)
        # todo: check this method, does it require system service?
        # Autogenerated comment:
        # some methods require a system service call as the methods expects a vb array object
        # passed to it and there is no way to do this directly with python. In those cases the following code
        # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # vba_function_name = 'set_lateral_axis_direction'
        # vba_code = """
        # Public Function set_lateral_axis_direction(drilling_riveting_operation)
        #     Dim iVecCoordinates (2)
        #     drilling_riveting_operation.SetLateralAxisDirection iVecCoordinates
        #     set_lateral_axis_direction = iVecCoordinates
        # End Function
        # """

        # system_service = SystemService(self.application.SystemService)
        # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_offset_from_position(self, i_position_index: int, i_matrix_offset: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetOffsetFromPosition(long iPositionIndex,CATSafeArrayVariant
                | iMatrixOffset)
                |     Sets the local Offset matrix of a dedicated work point.
                | 
                |     Parameters:
                | 
                |         iPositionIndex
                |             The index of fastener position (work point) 
                |         iMatrixOffset
                |             The offset matrix as an array of 12 values

        :param int i_position_index:
        :param tuple i_matrix_offset:
        :return: None
        """
        return self.com_object.SetOffsetFromPosition(i_position_index, i_matrix_offset)

    def __repr__(self):
        return f'DrillingRivetingOperation(name="{self.name}")'
