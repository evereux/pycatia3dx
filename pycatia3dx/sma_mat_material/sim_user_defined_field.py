"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.sma_mat_material.sim_material_table import SimMaterialTable
from pycatia3dx.sma_mpa_base.sim_table import SimTable
from pycatia3dx.sma_mpa_base.sim_table_column import SimTableColumn


class SimUserDefinedField(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimUserDefinedField
                | 
                | Represents the User Defined Field object.
                | 
                | Example:
                |     Given a SimMaterialOptions object, you can create a SimUserDefinedField as
                |     following:
                | 
                |      Dim MyMaterialOptions As SimMaterialOptions
                |      ...
                |      Dim MyUserDefinedField As SimUserDefinedField
                |      Set MyUserDefinedField = MyMaterialOptions.Add("SimUserDefinedField")
                |      
                | 
                |     Given a SimMaterialOptions object, you can retrieve a SimUserDefinedField
                |     named "User Defined Field.1" as following:
                | 
                |      Dim MyMaterialOptions As SimMaterialOptions
                |      ...
                |      Dim MyUserDefinedField As SimUserDefinedField
                |      Set MyUserDefinedField = MyMaterialOptions.Item("User Defined Field.1")
                |      
                | 
                | Example in Python:
                |     Given a SimMaterialOptions object myMaterialOptions, you can create a
                |     SimUserDefinedField as following:
                | 
                |      ...
                |      myUserDefinedField = myMaterialOptions.Add("SimUserDefinedField")
                |      
                | 
                |     Given a SimMaterialOptions object myMaterialOptions, you can retrieve a
                |     SimUserDefinedField named "User Defined Field.1" as
                |     following:
                | 
                |      ...
                |      myUserDefinedField = myMaterialOptions.Item("User Defined Field.1")
                |      
                | 
                | See also:
                |     SimMaterialOptions
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def direct_specification_redefinition_table(self) -> SimTable:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property DirectSpecificationRedefinitionTable() As SimTable (Read
                | Only)
                |     Retrieves the table when when resource for redefinition of field variables
                |     is by direct specification.
                | 
                |     Parameters:
                | 
                |         oDirectSpecificationTable[out]
                |             The direct specification redefinition table. 
                | 
                |     Returns:
                |         S_OK if successful.

        :return: SimTable
        """

        return SimTable(self.com_object.DirectSpecificationRedefinitionTable)

    @property
    def redefinition_resource(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property RedefinitionResource() As
                | SimUserDefinedFieldRedefinitionResource
                |     Retrieves the nature of resource for redefinition of field
                |     variables.
                | 
                |     Parameters:
                | 
                |         iRedefinitionResource[in]
                |             The nature of resource for redefinition of field variables.
                |             
                |         oRedefinitionResource[out]
                |             The nature of resource for redefinition of field variables.
                |             
                | 
                |     Returns:
                |         S_OK if successful.

        :return: int
        """

        return self.com_object.RedefinitionResource

    @redefinition_resource.setter
    def redefinition_resource(self, value: int):
        """
        :param int value:
        """

        self.com_object.RedefinitionResource = value

    @property
    def user_subroutine_redefinition_table(self) -> SimMaterialTable:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property UserSubroutineRedefinitionTable() As SimMaterialTable (Read
                | Only)
                |     Retrieves the table when resource for redefinition of field variables is a
                |     user subroutine.
                | 
                |     Parameters:
                | 
                |         oUserTable[out]
                |             The user subroutine redefinition table. 
                | 
                |     Returns:
                |         S_OK if successful.

        :return: SimMaterialTable
        """

        return SimMaterialTable(self.com_object.UserSubroutineRedefinitionTable)

    @property
    def user_subroutine_redefinition_table_column(self) -> SimTableColumn:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property UserSubroutineRedefinitionTableColumn() As SimTableColumn (Read
                | Only)
                |     Retrieves the column object of the table when resource for redefinition of
                |     field variables is a user subroutine.
                | 
                |     Parameters:
                | 
                |         oUserSubroutineTableColumn[out]
                |             The table column object. 
                | 
                |     Returns:
                |         S_OK if successful.

        :return: SimTableColumn
        """

        return SimTableColumn(self.com_object.UserSubroutineRedefinitionTableColumn)

    def get_direct_specification_redefinition_table_column(self, i_direct_specification_table_column: int) -> SimTableColumn:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func
                | GetDirectSpecificationRedefinitionTableColumn(SimUserDefinedFieldDirectSpecificationTableColumn iDirectSpecificationTableColumn) As SimTableColum
                | n
                |     Retrieves the column object of the table when resource for redefinition of
                |     field variables is by direct specification.
                | 
                |     Parameters:
                | 
                |         iDirectSpecificationTableColumn[in]
                |             The direct specification table column. 
                |         oDirectSpecificationColumn[out]
                |             The table column object. This value will be NULL_var in case the
                |             specified column is not found in the table. 
                | 
                |     Returns:
                |         S_OK if successful. S_FALSE if the supplied TableColumn enum is valid
                |         but the column does not exist currently or exists currently but is not active.
                |         E_INVALIDARG if the supplied TableColumn enum is invalid. E_FAIL otherwise.

        :param int i_direct_specification_table_column:
        :return: SimTableColumn
        """
        return SimTableColumn(self.com_object.GetDirectSpecificationRedefinitionTableColumn(i_direct_specification_table_column))

    def __repr__(self):
        return f'SimUserDefinedField(name="{ self.name }")'
