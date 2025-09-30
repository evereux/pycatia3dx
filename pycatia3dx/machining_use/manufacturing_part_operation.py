"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.todo_machining_use.manufacturing_activity import ManufacturingActivity


class ManufacturingPartOperation(ManufacturingActivity):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MachiningUseItf.ManufacturingActivity
                |                         ManufacturingPartOperation
                | 
                | Interface to manage Part Operation (Setup).
                | Role: Manage the information related to the Part Operation object like
                | associated resource, product and machining axis system.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def get_actual_stock_mode(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetActualStockMode() As long
                |     Gets the actual stock computation mode.
                | 
                |     Parameters:
                | 
                |         oMode
                |             the actual stock mode.
                |             Legal values: 1 if the stock is recomputed automatically for each
                |             Machining Operation, 0 otherwise.

        :return: int
        """
        return self.com_object.GetActualStockMode()

    def get_machine(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetMachine() As AnyObject
                |     Retrieves the machine. There can be only one machine.
                | 
                |     Parameters:
                | 
                |         oMachine
                |             The instance of machine associated.

        :return: AnyObject
        """
        return AnyObject(self.com_object.GetMachine())

    def get_machine_local_parameters(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetMachineLocalParameters() As AnyObject
                |     Retrieves the local parameters of machine.
                | 
                |     Parameters:
                | 
                |         oMachine
                |             The instance of machine associated.

        :return: AnyObject
        """
        return AnyObject(self.com_object.GetMachineLocalParameters())

    def get_machining_axis(self, o_origin: tuple, o_vector_x: tuple, o_vector_y: tuple, o_vector_z: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetMachiningAxis(CATSafeArrayVariant oOrigin,CATSafeArrayVariant
                | oVectorX,CATSafeArrayVariant oVectorY,CATSafeArrayVariant
                | oVectorZ)
                |     Retrieves the Machining Axis System feature associated to the Part
                |     Operation.
                | 
                |     Parameters:
                | 
                |         oOrigin
                |             Origin point 
                |         oVectorX
                |             Direction on X axis 
                |         oVectorY
                |             Direction on Y axis 
                |         oVectorZ
                |             Direction on Z axis

        :param tuple o_origin:
        :param tuple o_vector_x:
        :param tuple o_vector_y:
        :param tuple o_vector_z:
        :return: None
        """
        return self.com_object.GetMachiningAxis(o_origin, o_vector_x, o_vector_y, o_vector_z)

    def get_programs(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetPrograms() As CATSafeArrayVariant
                |     Retrieves Programs of the Part Operation
                | 
                |     Parameters:
                | 
                |         oListPrograms
                |             List of Programs

        :return: tuple
        """
        return self.com_object.GetPrograms()

    def get_tool_change_location(self, o_from_machine: bool) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetToolChangeLocation(boolean oFromMachine) As
                | CATSafeArrayVariant
                |     Gets the setup parameters defining the Tool Change point.
                |     WARNING : The values of these parameters are defined in the Part Operation axis system.
                | 
                |     Parameters:
                | 
                |         oToolChangeXYZListParms
                |             List of 3 CATICkeParm refering to the X, Y, Z coordinates of tool
                |             change point. 
                |         oFromMachine
                |             TRUE if the parameters have been copied from the machine. In this
                |             case the tool length is NOT take into account in the point
                |             definition.
                |             FALSE otherwise, and the tool change point is the tip point.

        :param bool o_from_machine:
        :return: tuple
        """
        return self.com_object.GetToolChangeLocation(o_from_machine)

    def insert_new_program(self, i_insertion_level: AnyObject) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func InsertNewProgram(AnyObject iInsertionLevel) As AnyObject
                |     Creates and insert a Program in the Part Operation.
                | 
                |     Parameters:
                | 
                |         oProgram
                |             The new created Program 
                |         iInsertionLevel
                |             The Program after which the new program is inserted. If NULL_var,
                |             the Program is inserted at the beginning of the Part Operation (default
                |             behaviour). 
                | 
                |     Returns:
                |         E_FAIL If the insertion program does not belong to the Part
                |         Operation.
                |         S_OK, if the program has been correctly created.

        :param AnyObject i_insertion_level:
        :return: AnyObject
        """
        return AnyObject(self.com_object.InsertNewProgram(i_insertion_level.com_object))

    def move_program_after(self, i_program_to_move: AnyObject, i_insertion_level: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub MoveProgramAfter(AnyObject iProgramToMove,AnyObject
                | iInsertionLevel)
                |     Moves a Program inside the Part Operation.
                | 
                |     Parameters:
                | 
                |         iProgramToMove
                |             The Program to be moved 
                |         iInsertionLevel
                |             The Program after which the program is moved. If NULL_var, the
                |             Program is moved at the beginning of the Part Operation (default behaviour).
                |             
                | 
                |     Returns:
                |         E_FAIL If the program to move or the insertion program do not belong to
                |         the Part Operation.
                |         S_OK, if the program has been correctly moved.

        :param AnyObject i_program_to_move:
        :param AnyObject i_insertion_level:
        :return: None
        """
        return self.com_object.MoveProgramAfter(i_program_to_move.com_object, i_insertion_level.com_object)

    def set_machine(self, i_machine: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetMachine(AnyObject iMachine)
                |     Replace current machine. There can be only one machine.
                | 
                |     Parameters:
                | 
                |         iMachine
                |             The instance of machine

        :param AnyObject i_machine:
        :return: None
        """
        return self.com_object.SetMachine(i_machine.com_object)

    def set_machining_axis(self, i_machining_axis: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetMachiningAxis(AnyObject iMachiningAxis)
                |     Associates a Machining Axis System feature to the Part
                |     Operation.
                | 
                |     Parameters:
                | 
                |         iMachiningAxis
                |             The Machining Axis System to be associated

        :param AnyObject i_machining_axis:
        :return: None
        """
        return self.com_object.SetMachiningAxis(i_machining_axis.com_object)

    def set_tool_change_location(self, i_x: int, i_y: int, i_z: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetToolChangeLocation(long iX,long iY,long iZ)
                |     Set the mathematical definition of the Tool Change point.
                | 
                |     Parameters:
                | 
                |         iX
                |             [in] X coordonate 
                |         iY
                |             [in] Y coordonate 
                |         iZ
                |             [in] Z coordonate 
                | 
                |     Returns:
                |         S_OK if succeeded

        :param int i_x:
        :param int i_y:
        :param int i_z:
        :return: None
        """
        return self.com_object.SetToolChangeLocation(i_x, i_y, i_z)

    def __repr__(self):
        return f'ManufacturingPartOperation(name="{ self.name }")'
