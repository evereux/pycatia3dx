"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.sma_mat_material.sim_material_table import SimMaterialTable


class SimDepvar(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimDepvar
                | 
                | Represents the Depvar object.
                | 
                | Example:
                |     Given a SimMaterialOptions object, you can create a SimDepvar as
                |     following:
                | 
                |      Dim MyMaterialOptions As SimMaterialOptions
                |      ...
                |      Dim MyDepvar As SimDepvar
                |      Set MyDepvar = MyMaterialOptions.Add("SimDepvar")
                |      
                | 
                |     Given a SimMaterialOptions object, you can retrieve a SimDepvar named
                |     "Depvar.1" as following:
                | 
                |      Dim MyMaterialOptions As SimMaterialOptions
                |      ...
                |      Dim MyDepvar As SimDepvar
                |      Set MyDepvar = MyMaterialOptions.Item("Depvar.1")
                |      
                | 
                | Example in Python:
                |     Given a SimMaterialOptions object myMaterialOptions, you can create a
                |     SimDepvar as following:
                | 
                |      ...
                |      myDepvar = myMaterialOptions.Add("SimDepvar")
                |      
                | 
                |     Given a SimMaterialOptions object myMaterialOptions, you can retrieve a
                |     SimDepvar named "Depvar.1" as following:
                | 
                |      ...
                |      myDepvar = myMaterialOptions.Item("Depvar.1")
                |      
                | 
                | See also:
                |     SimMaterialOptions
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def number_of_solution_dependant_state_variable(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property NumberOfSolutionDependantStateVariable() As long
                |     Returns or sets the number of solution dependent state
                |     variables.
                | 
                |     Parameters:
                | 
                |         oNumDepVariables[out]
                |             The number of solution dependent state variables. 
                |         iNumDepVariables[in]
                |             The number of solution dependent state variables. 
                | 
                |     Returns:
                |         S_OK if successful. E_FAIL if failed .

        :return: int
        """

        return self.com_object.NumberOfSolutionDependantStateVariable

    @number_of_solution_dependant_state_variable.setter
    def number_of_solution_dependant_state_variable(self, value: int):
        """
        :param int value:
        """

        self.com_object.NumberOfSolutionDependantStateVariable = value

    @property
    def solution_dependent_state_variable_table(self) -> SimMaterialTable:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property SolutionDependentStateVariableTable() As SimMaterialTable (Read
                | Only)
                |     Returns the the material table.
                | 
                |     Parameters:
                | 
                |         oMaterialTable[out]
                |             The material table. 
                | 
                |     Returns:
                |         S_OK if successful. E_FAIL if failed.

        :return: SimMaterialTable
        """

        return SimMaterialTable(self.com_object.SolutionDependentStateVariableTable)

    @property
    def variable_number_controlling_element_deletion(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property VariableNumberControllingElementDeletion() As long
                |     Returns or sets the state variable number controlling the element deletion
                |     flag.
                | 
                |     Parameters:
                | 
                |         oVariableNum[out]
                |             The state variable number controlling the element deletion flag.
                |             
                |         iVariableNum[in]
                |             The state variable number controlling the element deletion flag.
                |             
                | 
                |     Returns:
                |         S_OK if successful. E_FAIL if failed .

        :return: int
        """

        return self.com_object.VariableNumberControllingElementDeletion

    @variable_number_controlling_element_deletion.setter
    def variable_number_controlling_element_deletion(self, value: int):
        """
        :param int value:
        """

        self.com_object.VariableNumberControllingElementDeletion = value

    def get_solution_dependent_state_variable_table_cell_data(self, i_row: int, i_material_table_column: int) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetSolutionDependentStateVariableTableCellData(long
                | iRow,SimDepvarMaterialTableColumn iMaterialTableColumn) As
                | CATBSTR
                |     Retrieves the solution dependent state variable name.
                | 
                |     Parameters:
                | 
                |         iRow
                |             [in] The row number. 
                |         iMaterialTableColumn[in]
                |             The specified table column. 
                |         oVariableName[out]
                |             The solution dependent state variable name. 
                | 
                |     Returns:
                |         S_OK if successful. E_FAIL if failed.

        :param int i_row:
        :param int i_material_table_column:
        :return: str
        """
        return self.com_object.GetSolutionDependentStateVariableTableCellData(i_row, i_material_table_column)

    def set_solution_dependent_state_variable_table_cell_data(self, i_row: int, i_material_table_column: int, i_variable_name: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetSolutionDependentStateVariableTableCellData(long
                | iRow,SimDepvarMaterialTableColumn iMaterialTableColumn,CATBSTR
                | iVariableName)
                |     Sets the solution dependent state variable name.
                | 
                |     Parameters:
                | 
                |         iRow[in]
                |             The row number. 
                |         iMaterialTableColumn[in]
                |             The specified table column. 
                |         iVariableName[in]
                |             The solution dependent state variable name. 
                | 
                |     Returns:
                |         S_OK if successful. E_FAIL if failed.

        :param int i_row:
        :param int i_material_table_column:
        :param str i_variable_name:
        :return: None
        """
        return self.com_object.SetSolutionDependentStateVariableTableCellData(i_row, i_material_table_column, i_variable_name)

    def __repr__(self):
        return f'SimDepvar(name="{ self.name }")'
