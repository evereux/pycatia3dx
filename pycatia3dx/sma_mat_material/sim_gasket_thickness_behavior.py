"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.sma_mat_material.sim_material_table import SimMaterialTable
from pycatia3dx.todo_sma_mpa_base.sim_table_column import SimTableColumn


class SimGasketThicknessBehavior(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimGasketThicknessBehavior
                | 
                | Represents the Gasket Thickness Behavior object.
                | 
                | Example:
                |     Given a SimMaterialOptions object, you can create a
                |     SimGasketThicknessBehavior as following:
                | 
                |      Dim MyMaterialOptions As SimMaterialOptions
                |      ...
                |      Dim MyGasketThicknessBehavior As
                |      SimGasketThicknessBehavior
                |      Set MyGasketThicknessBehavior = MyMaterialOptions.Add("SimGasketThicknessBehavior")
                |      
                | 
                |     Given a SimMaterialOptions object, you can retrieve a
                |     SimGasketThicknessBehavior named "Gasket Thickness Behavior.1" as
                |     following:
                | 
                |      Dim MyMaterialOptions As SimMaterialOptions
                |      ...
                |      Dim MyGasketThicknessBehavior As
                |      SimGasketThicknessBehavior
                |      Set MyGasketThicknessBehavior = MyMaterialOptions.Item("Gasket Thickness Behavior.1")
                |      
                | 
                | Example in Python:
                |     Given a SimMaterialOptions object myMaterialOptions, you can create a
                |     SimGasketThicknessBehavior as following:
                | 
                |      ...
                |      myGasketThicknessBehavior = myMaterialOptions.Add("SimGasketThicknessBehavior")
                |      
                | 
                |     Given a SimMaterialOptions object myMaterialOptions, you can retrieve a
                |     SimGasketThicknessBehavior named "Gasket Thickness Behavior.1" as
                |     following:
                | 
                |      ...
                |      myGasketThicknessBehavior = myMaterialOptions.Item("Gasket Thickness Behavior.1")
                |      
                | 
                | See also:
                |     SimMaterialOptions
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def behavior_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property BehaviorType() As
                | SimGasketThicknessBehaviorBehaviorType
                |     Returns or sets the behavior type.

        :return: int
        """

        return self.com_object.BehaviorType

    @behavior_type.setter
    def behavior_type(self, value: int):
        """
        :param int value:
        """

        self.com_object.BehaviorType = value

    @property
    def loading_material_table(self) -> SimMaterialTable:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property LoadingMaterialTable() As SimMaterialTable (Read
                | Only)
                |     Returns the material loading table.

        :return: SimMaterialTable
        """

        return SimMaterialTable(self.com_object.LoadingMaterialTable)

    @property
    def tensile_stiffness_factor(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property TensileStiffnessFactor() As double
                |     Returns or sets the tensile stiffness factor. Quantity: Real, Units: None

        :return: float
        """

        return self.com_object.TensileStiffnessFactor

    @tensile_stiffness_factor.setter
    def tensile_stiffness_factor(self, value: float):
        """
        :param float value:
        """

        self.com_object.TensileStiffnessFactor = value

    @property
    def unloading_material_table(self) -> SimMaterialTable:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property UnloadingMaterialTable() As SimMaterialTable (Read
                | Only)
                |     Returns the material unloading table.

        :return: SimMaterialTable
        """

        return SimMaterialTable(self.com_object.UnloadingMaterialTable)

    @property
    def user_unloading_curve_flag(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property UserUnloadingCurveFlag() As boolean
                |     This boolean will be TRUE if an unloading curve is specified, FALSE
                |     otherwise.

        :return: bool
        """

        return self.com_object.UserUnloadingCurveFlag

    @user_unloading_curve_flag.setter
    def user_unloading_curve_flag(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.UserUnloadingCurveFlag = value

    @property
    def yield_onset_value(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property YieldOnsetValue() As double
                |     Returns or sets the yield onset value. Quantity: Real, Units: None

        :return: float
        """

        return self.com_object.YieldOnsetValue

    @yield_onset_value.setter
    def yield_onset_value(self, value: float):
        """
        :param float value:
        """

        self.com_object.YieldOnsetValue = value

    def get_loading_material_table_column(self, i_material_table_column: int) -> SimTableColumn:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func
                | GetLoadingMaterialTableColumn(SimGasketThicknessBehaviorLoadingMaterialTableColumn iMaterialTableColumn) As SimTableColum
                | n
                |     Retrieves the column object for the loading material table
                |     column.
                | 
                |     Parameters:
                | 
                |         iMaterialTableColumn[in]
                |             The loading material table column. 
                | 
                |     Returns:
                |         The table column object. This value will be NULL_var in case the
                |         specified column is not found in the table.

        :param int i_material_table_column:
        :return: SimTableColumn
        """
        return SimTableColumn(self.com_object.GetLoadingMaterialTableColumn(i_material_table_column))

    def get_unloading_material_table_column(self, i_material_table_column: int) -> SimTableColumn:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func
                | GetUnloadingMaterialTableColumn(SimGasketThicknessBehaviorUnloadingMaterialTableColumn iMaterialTableColumn) As SimTableColum
                | n
                |     Retrieves the column object for the unloading material table
                |     column.
                | 
                |     Parameters:
                | 
                |         iMaterialTableColumn[in]
                |             The unloading material table table column. 
                | 
                |     Returns:
                |         The table column object. This value will be NULL_var in case the
                |         specified column is not found in the table. 

        :param int i_material_table_column:
        :return: SimTableColumn
        """
        return SimTableColumn(self.com_object.GetUnloadingMaterialTableColumn(i_material_table_column))

    def __repr__(self):
        return f'SimGasketThicknessBehavior(name="{ self.name }")'
