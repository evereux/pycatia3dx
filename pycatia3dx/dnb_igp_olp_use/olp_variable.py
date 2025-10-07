"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.dnb_igp_olp_use.olp_ast_branch import OLPAstBranch


class OLPVariable(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     OlpVariable
                | 
                | A variable.
                | 
                | This interface can only be used by a translator within the Robotics Off-line
                | Programming (OLP) Download or Upload command.
                | A variable can be an external IO, a procedure argument, a constant, or a
                | regular variable.
                | The name of a variable is accessed through the AnyObject.Name parameter. The
                | name can contain any Unicode character, including spaces.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def alias_of(self) -> 'OLPVariable':
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property AliasOf() As OlpVariable (Read Only)
                |     If this variable is an alias of another variable, get that aliased
                |     variable.
                | 
                |     Parameters:
                | 
                |         oVariable
                |             If this variable is not an alias, this method fails. If it is an
                |             alias, the aliased variable is returned.

        :return: OLPVariable
        """

        return OLPVariable(self.com_object.AliasOf)

    @property
    def all_aliases(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property AllAliases() As CATSafeArrayVariant (Read Only)
                |     All aliases of this variable. The same results will be returned whether it
                |     is called on the underlying variable, or any alias that may exist

        :return: tuple
        """

        return self.com_object.AllAliases

    @property
    def array_dimensions(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ArrayDimensions() As CATSafeArrayVariant
                |     For an array variable, the dimensions of the array.
                |     This is an empty list if the variable is not an array. Arrays can have a
                |     maximum of 3 dimensions so the property is a list of 0 to 3 integers. Each
                |     integer is the size of that dimension. A value of -1 is used for conformant
                |     (variable length) arrays (e.g. [*]). -1 is only valid for procedure inputs and
                |     outputs.

        :return: tuple
        """

        return self.com_object.ArrayDimensions

    @array_dimensions.setter
    def array_dimensions(self, value: tuple):
        """
        :param tuple value:
        """

        self.com_object.ArrayDimensions = value

    @property
    def array_indexing(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ArrayIndexing() As CATSafeArrayVariant
                |     For an array variable, the index of the lower bound of the array for each
                |     dimension.
                |     Use ArrayIndexingAll except in exceptional circumstances. This is an empty
                |     list if the variable is not an array. Arrays can have a maximum of 3 dimensions
                |     so the property is a list of 0 to 3 integers. Each integer is the index of the
                |     1st element of that dimension The default indexing is 1 for each dimension.
                |     Usually all dimensions have the same indexing so you should use
                |     ArrayIndexingAll instead of this property.

        :return: tuple
        """

        return self.com_object.ArrayIndexing

    @array_indexing.setter
    def array_indexing(self, value: tuple):
        """
        :param tuple value:
        """

        self.com_object.ArrayIndexing = value

    @property
    def array_indexing_all(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ArrayIndexingAll() As long
                |     For an array variable, the index of the first element of the array (usually
                |     1 or 0).
                |     The default value is 1. Set to 0 if the robot language uses 0 based arrays.
                |     DELMIA arrays support having a different starting index for each dimension. You
                |     can use ArrayIndexing if you require, but that should only be used in
                |     exceptional circumstances. A warning will be posted if each dimension does not
                |     use the same indexing. You must call ArrayDimensions before setting the
                |     indexing individually for each dimension

        :return: int
        """

        return self.com_object.ArrayIndexingAll

    @array_indexing_all.setter
    def array_indexing_all(self, value: int):
        """
        :param int value:
        """

        self.com_object.ArrayIndexingAll = value

    @property
    def associated_object(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property AssociatedObject() As AnyObject (Read Only)
                |     The 3DExperience object associated with this variable.
                |     Could be a OlpController in the case of a Conveyor or an
                |     OlpConveyorTrackingProfile.

        :return: AnyObject
        """

        return AnyObject(self.com_object.AssociatedObject)

    @property
    def associated_object_type(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property AssociatedObjectType() As CATBSTR (Read Only)
                |     The type of 3DExperience object associated with this
                |     variable.
                |     Examples are Conveyor and ConveyorTrackingProfileInbound.

        :return: str
        """

        return self.com_object.AssociatedObjectType

    @property
    def connection_count(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ConnectionCount() As long (Read Only)
                |     Get the number of IOs on other resources this IO is connected
                |     to.
                |     Only variables of type External IO can be connected. All other variable
                |     types will return 0.

        :return: int
        """

        return self.com_object.ConnectionCount

    @property
    def data_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property DataType() As DELOlpDataType (Read Only)
                |     The data type of the variable.

        :return: DELOlpDataType
        """

        return self.com_object.DataType

    @property
    def data_type_in_string(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property DataTypeInString() As CATBSTR (Read Only)
                |     Get the data type in string format.
                |     This is the property to be used for any variable. The other property,
                |     DataType, does NOT work for any position variable due to the enum used as
                |     return value.
                | 
                |     Parameters:
                | 
                |         oType
                |             The string data type of the variable object. It is "Position" for a
                |             position variable. Otherwise, it is the same as the DELOlpDataType enum but
                |             without the delOlp prefix. For example if the type is delOlpInteger, "Integer"
                |             would be returned.

        :return: str
        """

        return self.com_object.DataTypeInString

    @property
    def default_value(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property DefaultValue() As CATBSTR
                |     Get/Set the default value.
                |     For constants this is the permanent, unchanging value. For other variables,
                |     this is the value used before any other value has been assigned using an assign
                |     instruction.

        :return: str
        """

        return self.com_object.DefaultValue

    @default_value.setter
    def default_value(self, value: str):
        """
        :param str value:
        """

        self.com_object.DefaultValue = value

    @property
    def description(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Description() As CATBSTR
                |     The variable description or comment.

        :return: str
        """

        return self.com_object.Description

    @description.setter
    def description(self, value: str):
        """
        :param str value:
        """

        self.com_object.Description = value

    @property
    def has_default_value(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property HasDefaultValue() As boolean (Read Only)
                |     Get whether this variable has a default value specified.
                |     For constants, this is always True.

        :return: bool
        """

        return self.com_object.HasDefaultValue

    @property
    def io_address(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property IOAddress() As CATBSTR
                |     The address of the variable on the robot controller.
                |     For some robots this may be just a port number (e.g. 32). For other robots
                |     this may be a full alpha numeric address (e.g. DI[1]). Please see the
                |     translator documentation for each robot to know what format the translator is
                |     expecting. This address can also be used for local variables and constants.

        :return: str
        """

        return self.com_object.IOAddress

    @io_address.setter
    def io_address(self, value: str):
        """
        :param str value:
        """

        self.com_object.IOAddress = value

    @property
    def io_direction(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property IODirection() As DELOlpIODirection (Read Only)
                |     The direction of the variable.
                |     This only applies to IO variables. For constants this always returns "in"
                |     (read only) and for local variables it returns "out" (read/write).

        :return: DELOlpIODirection
        """

        return self.com_object.IODirection

    @property
    def is_alias(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property IsAlias() As boolean (Read Only)
                |     Get the alias status of this variable.
                | 
                |     Parameters:
                | 
                |         oIsAlias
                |             True if this variable is an alias of some other variable. False
                |             otherwise.

        :return: bool
        """

        return self.com_object.IsAlias

    @property
    def scope(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Scope() As AnyObject (Read Only)
                |     The scope of the variable.
                |     This is either a OlpProcedure, a OlpBehavior, or a OlpInstructions.

        :return: AnyObject
        """

        return AnyObject(self.com_object.Scope)

    @property
    def sub_type(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property SubType() As CATBSTR (Read Only)
                |     The data sub-type Can be empty or one of the following when the data type
                |     is position variable. The sub type is inferred from the type of object linked
                |     to the variable so it cannot be set directly.
                | 
                |         Target: Position variables that are used as a target or an
                |         offset.
                |         Tool: Position variables that are used as a TCP value and associated
                |         with a tool profile.
                |         ObjectFrame: Position variables that are used as a object frame and
                |         associated with a profile.

        :return: str
        """

        return self.com_object.SubType

    @property
    def subscript_constant(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property SubscriptConstant() As CATSafeArrayVariant
                |     Get/Set constant subscripts.
                |     All values in the array are integers. This property fails if this is not a
                |     subscripted variable. Use SubscriptedVariable to check if this is a subscripted
                |     variable. A warning is generated if the subscripts are not constant if the
                |     value of this property is retrieved. Use SubscriptConstant to determine if the
                |     subscripts are constant.

        :return: tuple
        """

        return self.com_object.SubscriptConstant

    @subscript_constant.setter
    def subscript_constant(self, value: tuple):
        """
        :param tuple value:
        """

        self.com_object.SubscriptConstant = value

    @property
    def subscript_is_constant(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property SubscriptIsConstant() As boolean (Read Only)
                |     Get whether the subscript is a constant.
                |     For example x[3] has a constant subscript but x[i] does not.

        :return: bool
        """

        return self.com_object.SubscriptIsConstant

    @property
    def subscripted_array(self) -> 'OLPVariable':
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property SubscriptedArray() As OlpVariable (Read Only)
                |     The array used in the subscripted variable.
                |     This function fails if it is not a subscripted variable. Use
                |     SubscriptedVariable to check if this is a subscripted variable.

        :return: OLPVariable
        """

        return OLPVariable(self.com_object.SubscriptedArray)

    @property
    def subscripted_variable(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property SubscriptedVariable() As boolean (Read Only)
                |     Get whether this is a subscripted variable.
                |     A subscripted variable is the combination of the array name and a
                |     subscript. You can use a subscripted variable anyplace an ordinary variable can
                |     go. For example x[3] is a subscripted variable. You can create a subscripted
                |     variable using OlpVariables.GetOrCreateSubscriptedVariable A subscripted
                |     variable may be an array variable if the subscripts only cover 1 dimension. For
                |     example, if y is a 2 dimensional array [10,10], then y[3] is a 1 dimensional
                |     array of 10 elements. You can use ArrayDimensions to check if this is an array.

        :return: bool
        """

        return self.com_object.SubscriptedVariable

    @property
    def subscripts(self) -> OLPAstBranch:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Subscripts() As OlpAstBranch
                |     Get/Set subscripts.
                |     This property fails if this is not a subscripted variable. The AST format
                |     is an "Arguments" node with the following format:
                | 
                |      <Arguments>
                |        <BinaryExp id="Subscript1">
                |          <Identifier id="Operand1">i</Identifier>
                |          <Operator>+</Operator>
                |          <ConstInteger id="Operand2">1</ConstInteger>
                |        </BinaryExp>
                |        <Operator>,</Operator>
                |        <ConstInteger id="Subscript2">2</ConstInteger>
                |      </Arguments>
                |      
                | 
                |     Use SubscriptedVariable to check if this is a subscripted variable.

        :return: OLPAstBranch
        """

        return OLPAstBranch(self.com_object.Subscripts)

    @subscripts.setter
    def subscripts(self, value: OLPAstBranch):
        """
        :param OLPAstBranch value:
        """

        self.com_object.Subscripts = value

    @property
    def variable_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property VariableType() As DELOlpVariableType (Read Only)
                |     The type of variable (For Example IO, constant, regular variable).

        :return: DELOlpVariableType
        """

        return self.com_object.VariableType

    @property
    def variable_type2(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property VariableType2() As CATBSTR (Read Only)
                |     The type of variable.
                |     Valid values are ExternalIO, ProcedureIO, Local, Constant, Timer.

        :return: str
        """

        return self.com_object.VariableType2

    def get_connection(self, i_index: int, o_resource_type: str, o_resource_name: str, o_io_name: str, o_io_direction: int, o_io_address: str, o_io_description: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetConnection(long iIndex,CATBSTR oResourceType,CATBSTR
                | oResourceName,CATBSTR oIOName,DELOlpIODirection oIODirection,CATBSTR
                | oIOAddress,CATBSTR oIODescription)
                |     Get information about the final resource the IO is connected
                |     to.
                |     For example if
                |     -RobotA\OUT1 is connected to to its parent CellA\OUT1 and -CELLA\OUT1 is
                |     connected to CELLB\IN1 and -CELLB\IN1 is connected to ROBOTB\IN1 The connection
                |     information is returned for ROBOTB\IN1. In many cases, if the connection
                |     information is returned for a resource of type Cell, this may mean the mapping
                |     is incomplete or the final resource is not loaded in session. You can check the
                |     oIODirection, if it is the same direction as this variable then the IO has been
                |     propagated to its parent cell, but no futher connection information is
                |     available.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             Connection index. First connection is index 1. Use ConnectionCount
                |             to get the number of connections. The function fails if iIndex is not a valid
                |             connection index. 
                |         oResourceType
                |             The resource type that the IO is connected to. Valid options are
                |             :
                | 
                |                 Cell
                |                 Robot
                |                 Worker
                |                 NCMachine
                |                 Inspect
                |                 ToolDevice
                |                 Storage
                |                 Transport
                |                 Conveyor
                |                 ControlEquiptment
                |                 UserDefined
                |                 LogicController
                |                 Sensor
                |                 IndustrialMachine
                |                 Area
                |                 ManufacturingProduct
                |                 Pathway
                |                 WorkCenter
                |                 Pool
                | 
                |         oResourceName
                |             The instance name of the resource the IO is connected to. If
                |             connected to a cell and the cell is the root object opened, the reference name
                |             is returned. 
                |         oIOName
                |             The name of the variable this is connected to. 
                |         oIODirection
                |             The direction of the IO this is connected to. If this variable has
                |             the same direction as the connected one (both input or both output) that means
                |             the IO has been propagated to its parent cell, but no futher connection
                |             information is available, either because the mapping is incomplete or because
                |             the other resources are not loaded in session. 
                |         oIOAddress
                |             The IO address (port number) of the variable this is connected to.
                |             
                |         oIODescription
                |             The description of the variable this is connected to.

        :param int i_index:
        :param str o_resource_type:
        :param str o_resource_name:
        :param str o_io_name:
        :param int o_io_direction:
        :param str o_io_address:
        :param str o_io_description:
        :return: None
        """
        return self.com_object.GetConnection(i_index, o_resource_type, o_resource_name, o_io_name, o_io_direction, o_io_address, o_io_description)

    def has_alias_relation_with(self, i_variable: 'OLPVariable') -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func HasAliasRelationWith(OlpVariable iVariable) As boolean
                |     Either this object is an alias of iVariable, or the other way around,
                |     useful if whichever variable is alias of the other does not matter

        :param OLPVariable i_variable:
        :return: bool
        """
        return self.com_object.HasAliasRelationWith(i_variable.com_object)

    def __repr__(self):
        return f'OLPVariable(name="{ self.name }")'
