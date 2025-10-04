"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.todo_sma_mpa_base.sim_table_column import SimTableColumn


class SimUserDefined(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimUserDefined
                | 
                | Represents the User Defined object.
                | 
                | Example:
                |     Given a SimMaterialOptions object, you can create a SimUserDefined as
                |     following:
                | 
                |      Dim MyMaterialOptions As SimMaterialOptions
                |      ...
                |      Dim MyUserDefined As SimUserDefined
                |      Set MyUserDefined = MyMaterialOptions.Add("SimUserDefined")
                |      
                | 
                |     Given a SimMaterialOptions object, you can retrieve a SimUserDefined named
                |     "User Defined.1" as following:
                | 
                |      Dim MyMaterialOptions As SimMaterialOptions
                |      ...
                |      Dim MyUserDefined As SimUserDefined
                |      Set MyUserDefined = MyMaterialOptions.Item("User Defined.1")
                |      
                | 
                | Example in Python:
                |     Given a SimMaterialOptions object myMaterialOptions, you can create a
                |     SimUserDefined as following:
                | 
                |      ...
                |      myUserDefined = myMaterialOptions.Add("SimUserDefined")
                |      
                | 
                |     Given a SimMaterialOptions object myMaterialOptions, you can retrieve a
                |     SimUserDefined named "User Defined.1" as following:
                | 
                |      ...
                |      myUserDefined = myMaterialOptions.Item("User Defined.1")
                |      
                | 
                | See also:
                |     SimMaterialOptions
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def hybrid_formulation(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property HybridFormulation() As
                | SimUserDefinedHybridFormulation
                |     Returns or sets hybrid formulation.
                | 
                |     Parameters:
                | 
                |         oHybrid[out]
                |             The hybrid formulation. 
                |         iHybrid[in]
                |             The hybrid formulation. 
                | 
                |     Returns:
                |         S_OK if successful. E_FAIL if failed.

        :return: int
        """

        return self.com_object.HybridFormulation

    @hybrid_formulation.setter
    def hybrid_formulation(self, value: int):
        """
        :param int value:
        """

        self.com_object.HybridFormulation = value

    @property
    def unsymmetric_stiffness_matrix_flag(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property UnsymmetricStiffnessMatrixFlag() As boolean
                |     Returns or sets the unsymmetric stiffness matrix flag.
                | 
                |     Parameters:
                | 
                |         oUnsymmetricStiffnessMatrixFlag[out]
                |             The unsymmetric stiffness matrix flag. 
                |         iUnsymmetricStiffnessMatrixFlag[in]
                |             The unsymmetric stiffness matrix flag. 
                | 
                |     Returns:
                |         S_OK if successful. E_FAIL if failed.

        :return: bool
        """

        return self.com_object.UnsymmetricStiffnessMatrixFlag

    @unsymmetric_stiffness_matrix_flag.setter
    def unsymmetric_stiffness_matrix_flag(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.UnsymmetricStiffnessMatrixFlag = value

    @property
    def user_defined_physics(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property UserDefinedPhysics() As SimUserDefinedPhysics
                |     Returns or sets the user defined physics of the material.
                | 
                |     Parameters:
                | 
                |         oPhysics[out]
                |             The user defined physics. 
                |         iPhysics[in]
                |             The user defined physics. 
                | 
                |     Returns:
                |         S_OK if successful. E_FAIL if failed.

        :return: int
        """

        return self.com_object.UserDefinedPhysics

    @user_defined_physics.setter
    def user_defined_physics(self, value: int):
        """
        :param int value:
        """

        self.com_object.UserDefinedPhysics = value

    @property
    def user_subroutine_configurable_flag(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property UserSubroutineConfigurableFlag() As boolean
                |     Returns or sets the user subroutine configurable feature used
                |     flag.
                | 
                |     Parameters:
                | 
                |         oUserSubroutineFlag[out]
                |             TRUE: The configurable feature is used for user
                |             subroutine.
                |             FALSE: The configurable feature is not used for user subroutine.
                |             
                |         iUserSubroutineFlag[in]
                |             TRUE: The configurable feature will be used for user
                |             subroutine.
                |             FALSE: The configurable feature will not be used for user
                |             subroutine. 
                | 
                |     Returns:
                |         S_OK if successful.

        :return: bool
        """

        return self.com_object.UserSubroutineConfigurableFlag

    @user_subroutine_configurable_flag.setter
    def user_subroutine_configurable_flag(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.UserSubroutineConfigurableFlag = value

    def get_material_table_column(self, i_material_table_column: int) -> SimTableColumn:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetMaterialTableColumn(SimUserDefinedMaterialTableColumn
                | iMaterialTableColumn) As SimTableColumn
                |     Retrieves the column object for the specified table
                |     column.
                | 
                |     Parameters:
                | 
                |         iMaterialTableColumn[in]
                |             The specified table column. 
                |         oMaterialTableColumn[out]
                |             The table column object. This value will be NULL_var in case the
                |             specified column is not found in the table. Number of rows entered is equal to
                |             the number of constants being entered. 
                | 
                |     Returns:
                |         S_OK if successful. S_FALSE if the supplied
                |         SimUserDefinedMaterialTableColumn enum is valid but the column does not exist
                |         currently or exists currently but is not active. E_INVALIDARG if the supplied
                |         SimUserDefinedMaterialTableColumn enum is invalid. E_FAIL otherwise.

        :param int i_material_table_column:
        :return: SimTableColumn
        """
        return SimTableColumn(self.com_object.GetMaterialTableColumn(i_material_table_column))

    def __repr__(self):
        return f'SimUserDefined(name="{ self.name }")'
