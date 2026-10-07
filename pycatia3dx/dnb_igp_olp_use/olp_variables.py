"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from typing import Iterator

from pycatia3dx.system.collection import Collection
from pycatia3dx.dnb_igp_olp_use.olp_variable import OLPVariable
from pycatia3dx.types.general import CATVariant


class OLPVariables(Collection):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     OlpVariables
                | 
                | A list of variables.
                | 
                | This interface can only be used by a translator within the Robotics Off-line
                | Programming (OLP) Download or Upload command.
                | A variable can be an external IO, a procedure argument, a constant, or a
                | regular variable.
                | This can be retrieved from OlpProcedure.LocalVariables or from
                | OlpBehavior.GlobalVariables
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=OLPVariable)
        self.com_object = com_object

    @property
    def filter(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Filter() As DELOlpVariableType
                |     Filter the collection to only contain variables of a specific
                |     type.

        :return: DELOlpVariableType
        """

        return self.com_object.Filter

    @filter.setter
    def filter(self, value: int):
        """
        :param int value:
        """

        self.com_object.Filter = value

    @property
    def filter_in_string(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property FilterInString() As CATBSTR
                |     This is an extended version of the Filter property, whose enum type does
                |     not include Alias and any future types. Use "Alias" to filter the new alias
                |     type of variables
                |     Given the name of the aliased object, an alias named "iName" will be
                |     retrieved if existing, or created otherwise. The alias variable is returned in
                |     either case.
                | 
                |     Parameters:
                | 
                |         iName
                |             The name of the alias to be retrieved or created. 
                |         iAliasOf
                |             The name of the aliased variable Use string "Position" to create a
                |             position constant

        :return: str
        """

        return self.com_object.FilterInString

    @filter_in_string.setter
    def filter_in_string(self, value: str):
        """
        :param str value:
        """

        self.com_object.FilterInString = value

    def get_or_create_alias(self, i_name: str, i_alias_of: str) -> OLPVariable:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetOrCreateAlias(CATBSTR iName,CATBSTR iAliasOf) As
                | OlpVariable
                |     Create or retrieve an alias variable.
                |     Given the name of the aliased object, an alias named "iName" will be
                |     retrieved if existing, or created otherwise. The alias variable is returned in
                |     either case.
                | 
                |     Parameters:
                | 
                |         iName
                |             The name of the alias to be retrieved or created. 
                |         iAliasOf
                |             The name of the aliased variable Use string "Position" to create a
                |             position constant

        :param str i_name:
        :param str i_alias_of:
        :return: OLPVariable
        """
        return OLPVariable(self.com_object.GetOrCreateAlias(i_name, i_alias_of))

    def get_or_create_const(self, i_name: str, i_data_type: int, i_value: str) -> OLPVariable:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetOrCreateConst(CATBSTR iName,DELOlpDataType iDataType,CATBSTR iValue) As
                | OlpVariable
                |     Create a constant.
                |     If a variable with this name already exists at this scope, it will be used
                |     instead of creating a new variable. If that variable does not match the other
                |     parameters specified, a warning will be issued, but the variable will still be
                |     returned.

        :param str i_name:
        :param int i_data_type:
        :param str i_value:
        :return: OLPVariable
        """
        return OLPVariable(self.com_object.GetOrCreateConst(i_name, i_data_type, i_value))

    def get_or_create_const_in_string_type(self, i_name: str, i_data_type: str, i_value: str) -> OLPVariable:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetOrCreateConstInStringType(CATBSTR iName,CATBSTR iDataType,CATBSTR
                | iValue) As OlpVariable
                |     Create a constant.
                |     If a variable with this name already exists at this scope, it will be used
                |     instead of creating a new variable. If that variable does not match the other
                |     parameters specified, a warning will be issued, but the variable will still be
                |     returned.
                | 
                |     Parameters:
                | 
                |         iDataType
                |             The string type of constant to get or create. The type is the same
                |             as the DELOlpDataType enum but without the delOlp prefix. For example if the
                |             intended type is delOlpInteger, use string "Integer". Use string "Position" to
                |             create a position constant

        :param str i_name:
        :param str i_data_type:
        :param str i_value:
        :return: OLPVariable
        """
        return OLPVariable(self.com_object.GetOrCreateConstInStringType(i_name, i_data_type, i_value))

    def get_or_create_io(self, i_name: str, i_data_type: int, i_direction: int) -> OLPVariable:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetOrCreateIO(CATBSTR iName,DELOlpDataType iDataType,DELOlpIODirection
                | iDirection) As OlpVariable
                |     Create an IO variable.
                |     If this is the variables collection for a OlpProcedure, then the IO is a
                |     procedure argument. The order the procedure arguments are created in must match
                |     the calling order in the OlpRun instruction. If this is the variables
                |     collection for a OlpBehavior then the IO is an external
                |     IO.
                |     If a variable with this name already exists at this scope, it will be used
                |     instead of creating a new variable. If that variable does not match the other
                |     parameters specified, a warning will be issued, but the variable will still be
                |     returned.

        :param str i_name:
        :param int i_data_type:
        :param int i_direction:
        :return: OLPVariable
        """
        return OLPVariable(self.com_object.GetOrCreateIO(i_name, i_data_type, i_direction))

    def get_or_create_io_in_string_type(self, i_name: str, i_data_type: str, i_direction: int) -> OLPVariable:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetOrCreateIOInStringType(CATBSTR iName,CATBSTR
                | iDataType,DELOlpIODirection iDirection) As OlpVariable
                |     Create an IO variable.
                |     If this is the variables collection for a OlpProcedure, then the IO is a
                |     procedure argument. The order the procedure arguments are created in must match
                |     the calling order in the OlpRun instruction. If this is the variables
                |     collection for a OlpBehavior then the IO is an external
                |     IO.
                |     If a variable with this name already exists at this scope, it will be used
                |     instead of creating a new variable. If that variable does not match the other
                |     parameters specified, a warning will be issued, but the variable will still be
                |     returned.
                | 
                |     Parameters:
                | 
                |         iDataType
                |             The string type of IO to get or create. The type is the same as the
                |             DELOlpDataType enum but without the delOlp prefix. For example if the intended
                |             type is delOlpInteger, use string "Integer". Use string "Position" to create a
                |             position IO

        :param str i_name:
        :param str i_data_type:
        :param int i_direction:
        :return: OLPVariable
        """
        return OLPVariable(self.com_object.GetOrCreateIOInStringType(i_name, i_data_type, i_direction))

    def get_or_create_local_var(self, i_name: str, i_data_type: int) -> OLPVariable:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetOrCreateLocalVar(CATBSTR iName,DELOlpDataType iDataType) As
                | OlpVariable
                |     Create a local variable.
                |     If a variable with this name already exists at this scope, it will be used
                |     instead of creating a new variable. If that variable does not match the other
                |     parameters specified, a warning will be issued, but the variable will still be
                |     returned.

        :param str i_name:
        :param int i_data_type:
        :return: OLPVariable
        """
        return OLPVariable(self.com_object.GetOrCreateLocalVar(i_name, i_data_type))

    def get_or_create_local_var_in_string_type(self, i_name: str, i_data_type: str) -> OLPVariable:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetOrCreateLocalVarInStringType(CATBSTR iName,CATBSTR iDataType) As
                | OlpVariable
                |     Create a local variable.
                |     If a variable with this name already exists at this scope, it will be used
                |     instead of creating a new variable. If that variable does not match the other
                |     parameters specified, a warning will be issued, but the variable will still be
                |     returned.
                | 
                |     Parameters:
                | 
                |         iDataType
                |             The string type of local variable to get or create. The type is the
                |             same as the DELOlpDataType enum but without the delOlp prefix. For example if
                |             the intended type is delOlpInteger, use string "Integer". Use string "Position"
                |             to create a position variable

        :param str i_name:
        :param str i_data_type:
        :return: OLPVariable
        """
        return OLPVariable(self.com_object.GetOrCreateLocalVarInStringType(i_name, i_data_type))

    def get_or_create_subscripted_variable(self, i_array_variable: OLPVariable) -> OLPVariable:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetOrCreateSubscriptedVariable(OlpVariable iArrayVariable) As
                | OlpVariable
                |     Create a subscripted variable.
                |     A subscripted variable is the combination of the array name and a
                |     subscript. You can use a subscripted variable anyplace an ordinary variable can
                |     go. For example x[3] is a subscripted variable. Subscripted variables are not
                |     saved or stored anywhere until they are set on an instruction either as the
                |     target of an assignment or in an expression.

        :param OLPVariable i_array_variable:
        :return: OLPVariable
        """
        return OLPVariable(self.com_object.GetOrCreateSubscriptedVariable(i_array_variable.com_object))

    def get_or_create_timer(self, i_name: str) -> OLPVariable:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetOrCreateTimer(CATBSTR iName) As OlpVariable
                |     Create a timer variable.
                |     If a timer with this name already exists at this scope, it will be used
                |     instead of creating a new variable.

        :param str i_name:
        :return: OLPVariable
        """
        return OLPVariable(self.com_object.GetOrCreateTimer(i_name))

    def item(self, i_index: CATVariant) -> OLPVariable:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Item(CATVariant iIndex) As OlpVariable
                |     Retrieve a variable by its name or index.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             If iIndex is a string, then a variable with that name is returned,
                |             regardless of the current filter. If the index is a number, it is the index of
                |             the variable in the collection with the current filter applied. The index of
                |             the first parameter in the collection is 1, and the index of the last parameter
                |             is Count. 
                | 
                |     Returns:
                |         The variable retrieved. If the variable name was not found, Nothing is
                |         returned but the function succeeds. If the index is out of bounds, the function
                |         fails. 

        :param CATVariant i_index:
        :return: OLPVariable
        """
        return OLPVariable(self.com_object.Item(i_index))

    def __getitem__(self, n: int) -> OLPVariable:
        if (n + 1) > self.count:
            raise StopIteration

        return OLPVariable(self.com_object.Item(n + 1))

    def __iter__(self) -> Iterator[OLPVariable]:
        for i in range(self.count):
            yield OLPVariable(self.com_object.Item(i + 1))

    def __repr__(self):
        return f'OLPVariables(name="{self.name}")'
