"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class SpotDrAction(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SpotDrAction

    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def drill_rivet_profile(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property DrillRivetProfile() As AnyObject
                |     Get the assigned Drill-Rivet Profile
                | 
                |     Parameters:
                | 
                |         oDRProfile
                |             Assigned Drill-Rivet Profile 
                | 
                |     Returns:
                |         S_OK = Success. E_FAIL = Error

        :return: AnyObject
        """

        return AnyObject(self.com_object.DrillRivetProfile)

    @drill_rivet_profile.setter
    def drill_rivet_profile(self, value: AnyObject):
        """
        :param AnyObject value:
        """

        self.com_object.DrillRivetProfile = value

    @property
    def object_profile(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ObjectProfile(AnyObject iObjectProfile)
                |     Set the Object Frame Profile
                | 
                |     Parameters:
                | 
                |         iObjectProfile
                |             Object Frame Profile to Assign 
                | 
                |     Returns:
                |         S_OK = Success. E_FAIL = Error

        :return: AnyObject
        """

        return AnyObject(self.com_object.ObjectProfile)

    @object_profile.setter
    def object_profile(self, value: AnyObject):
        """
        :param AnyObject value:
        """

        self.com_object.ObjectProfile = value

    @property
    def tool_profile(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ToolProfile(AnyObject iToolProfile)
                |     Set the Tool Profile
                | 
                |     Parameters:
                | 
                |         iToolProfile
                |             Tool Profile to Assign 
                | 
                |     Returns:
                |         S_OK = Success. E_FAIL = Error

        :return: AnyObject
        """

        return AnyObject(self.com_object.ToolProfile)

    @tool_profile.setter
    def tool_profile(self, value: AnyObject):
        """
        :param AnyObject value:
        """

        self.com_object.ToolProfile = value

    def add_instruction(self, ih_instruction: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub AddInstruction(AnyObject ihInstruction)
                |     This method adds the passed instruction to the Drill-Rivet
                |     Action
                | 
                |     Parameters:
                | 
                |         ihInstruction,
                |             instruction to be created 
                | 
                |     Returns:
                |         S_OK on success and E_FAIL on failure. 
                |     Example:
                | 
                |          
                | 
                |            Dim oResourceTask As ResourceTask2
                |            Dim DRAction As SpotDrAction
                |            ......
                |            Dim ResourceSequence As RscSequence
                |            Set ResourceSequence = oResourceTask.MainRscSequence
                |            ......
                |            Dim iIndex
                |            iIndex=-1
                |            Dim oCreatedCustom As RscCustomInstruction
                |            Set oCreatedCustom = ResourceSequence.CreateRscCustomInstruction(iIndex)
                |            ......
                |            DRAction.AddInstruction(oCreatedCustom)

        :param AnyObject ih_instruction:
        :return: None
        """
        return self.com_object.AddInstruction(ih_instruction.com_object)

    def get_manufacturing_fastener(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetManufacturingFastener() As AnyObject
                |     Get the Fastener associated to the DR Action.
                | 
                |     Parameters:
                | 
                |         opFastener
                |             Manufacturing Fastener. 
                | 
                |     Returns:
                |         S_OK = Successfully get the handle to Manufacturing Fastener. E_FAIL = Failed to get the associated Manufacturing Fastener.

        :return: AnyObject
        """
        return AnyObject(self.com_object.GetManufacturingFastener())

    def get_position_coordinates(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetPositionCoordinates() As CATSafeArrayVariant
                |     Gets the position coordinates(like X, Y, Z, Y, P, R) associated to the DR
                |     Action.
                | 
                |     Parameters:
                | 
                |         oFastenerPosCoords
                |             The X, Y, Z, Y, P, R values of Fastener position The position are
                |             of double type. The values get via CATSafeArrayVariant for oFastenerPosCoords
                |             is array of double pointers, having 6 position values.
                |             
                | 
                |     Returns:
                |         An HRESULT.
                |         Legal values:
                | 
                |         S_OK
                |             Cartesian target successfully set
                |         E_FAIL
                |             Cartesian target could not be set successfully

        :return: tuple
        """
        return self.com_object.GetPositionCoordinates()

    def list_instructions(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func ListInstructions() As CATSafeArrayVariant
                |     List all instructions present in this Sequence.
                | 
                |     Parameters:
                | 
                |         oListInstructions
                |             The list of instructions to complete (Previous list content is not
                |             removed). 
                | 
                |     Returns:
                |         Legal values:
                | 
                |             S_OK : The method has succeeded
                |             E_FAIL : if an error occurs.

        :return: tuple
        """
        return self.com_object.ListInstructions()

    def remove_instruction(self, ih_instruction: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub RemoveInstruction(AnyObject ihInstruction)
                |     This method removes the passed instruction to the Drill-Rivet
                |     Action
                | 
                |     Parameters:
                | 
                |         ihInstruction,
                |             instruction to be removed 
                | 
                |     Returns:
                |         S_OK on success and E_FAIL on failure.

        :param AnyObject ih_instruction:
        :return: None
        """
        return self.com_object.RemoveInstruction(ih_instruction.com_object)

    def set_position_coordinates(self, i_fastener_pos_coords: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetPositionCoordinates(CATSafeArrayVariant
                | iFastenerPosCoords)
                |     Sets the position coordinates(like X, Y, Z, Y, P, R) associated to the DR
                |     Action.
                | 
                |     Parameters:
                | 
                |         iFastenerPosCoords
                |             The X, Y, Z, Y, P, R values of Fastener position The position are
                |             of double type. The values get via CATSafeArrayVariant for oFastenerPosCoords
                |             is array of double pointers, having 6 position values.
                |             
                | 
                |     Returns:
                |         An HRESULT.
                |         Legal values:
                | 
                |         S_OK
                |             Cartesian target successfully set
                |         E_FAIL
                |             Cartesian target could not be set successfully

        :param tuple i_fastener_pos_coords:
        :return: None
        """
        return self.com_object.SetPositionCoordinates(i_fastener_pos_coords)

    def __repr__(self):
        return f'SpotDrAction(name="{ self.name }")'
