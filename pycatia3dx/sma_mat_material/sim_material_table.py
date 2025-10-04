"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.todo_sma_mpa_base.sim_table import SimTable
from pycatia3dx.todo_sma_mpa_base.sim_table_column import SimTableColumn


class SimMaterialTable(SimTable):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SMAMpaBaseIDLItf.SimTable
                |                         SimMaterialTable
                | 
                | Represents the Material Table object.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def number_of_field_variables(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property NumberOfFieldVariables() As long
                |     Returns or sets the number of field variable columns.

        :return: int
        """

        return self.com_object.NumberOfFieldVariables

    @number_of_field_variables.setter
    def number_of_field_variables(self, value: int):
        """
        :param int value:
        """

        self.com_object.NumberOfFieldVariables = value

    def get_field_variable_column(self, i_field_variable_column_index: int) -> SimTableColumn:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetFieldVariableColumn(long iFieldVariableColumnIndex) As
                | SimTableColumn
                |     Retrieves the field variable column object for the specified field variable
                |     column index.
                | 
                |     Parameters:
                | 
                |         iFieldVariableColumnIndex[in]
                |             The index of field variable column. 
                | 
                |     Returns:
                |         The field variable column in the material table.

        :param int i_field_variable_column_index:
        :return: SimTableColumn
        """
        return SimTableColumn(self.com_object.GetFieldVariableColumn(i_field_variable_column_index))

    def get_field_variables_supported_flag(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetFieldVariablesSupportedFlag() As boolean
                |     Retrieves whether the field variables are supported by the
                |     table.
                | 
                |     Returns:
                |         The boolean will be TRUE if field variables are supported by the table,
                |         FALSE otherwise.

        :return: bool
        """
        return self.com_object.GetFieldVariablesSupportedFlag()

    def get_optional_column(self, i_optional_column: int) -> SimTableColumn:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetOptionalColumn(SimMaterialTableOptionalColumn iOptionalColumn) As
                | SimTableColumn
                |     Retrieves the column corresponding to the specified optional column. This
                |     column can be used with methods such as GetData and
                |     SetData.
                | 
                |     Parameters:
                | 
                |         iOptionalColumn[in]
                |             The optional column used in the material table. 
                | 
                |     Returns:
                |         The optional column in the material table.

        :param int i_optional_column:
        :return: SimTableColumn
        """
        return SimTableColumn(self.com_object.GetOptionalColumn(i_optional_column))

    def get_optional_column_activation_flag(self, i_optional_column: int) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetOptionalColumnActivationFlag(SimMaterialTableOptionalColumn
                | iOptionalColumn) As boolean
                |     Retrieves whether the optional column iOptionalColumn in the table is
                |     active or not.
                | 
                |     Parameters:
                | 
                |         iOptionalColumn[in]
                |             The optional column used in the material table. 
                | 
                |     Returns:
                |         The boolean will be TRUE if data is optional column dependent, FALSE
                |         otherwise.

        :param SimMaterialTableOptionalColumn i_optional_column:
        :return: bool
        """
        return self.com_object.GetOptionalColumnActivationFlag(i_optional_column)

    def get_optional_column_supported_flag(self, i_optional_column: int) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetOptionalColumnSupportedFlag(SimMaterialTableOptionalColumn
                | iOptionalColumn) As boolean
                |     Retrieves whether the optional column iOptionalColumn is supported for the
                |     data in the table.
                | 
                |     Parameters:
                | 
                |         iOptionalColumn[in]
                |             The optional column used in the material table. 
                | 
                |     Returns:
                |         The boolean will be TRUE if optional column iOptionalColumn is
                |         supported for the table, FALSE otherwise.

        :param int i_optional_column:
        :return: bool
        """
        return self.com_object.GetOptionalColumnSupportedFlag(i_optional_column)

    def set_optional_column_activation_flag(self, i_optional_column: int, i_optional_column_activation: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetOptionalColumnActivationFlag(SimMaterialTableOptionalColumn
                | iOptionalColumn,boolean iOptionalColumnActivation)
                |     Activates or deactivates the optional column
                |     iOptionalColumn.
                | 
                |     Parameters:
                | 
                |         iOptionalColumn[in]
                |             The optional column used in the material table. 
                |         iOptionalColumnActivation[in]
                |             The boolean input TRUE if the optional column iOptionalColumn
                |             should be activated. FALSE if the optional column iOptionalColumn should be
                |             deactivated. 

        :param SimMaterialTableOptionalColumn i_optional_column:
        :param bool i_optional_column_activation:
        :return: None
        """
        return self.com_object.SetOptionalColumnActivationFlag(i_optional_column, i_optional_column_activation)

    def __repr__(self):
        return f'SimMaterialTable(name="{ self.name }")'
