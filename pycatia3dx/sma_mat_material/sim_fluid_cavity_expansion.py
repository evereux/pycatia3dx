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


class SimFluidCavityExpansion(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimFluidCavityExpansion
                | 
                | Represents the Fluid Cavity Expansion object.
                | 
                | Example:
                |     Given a SimMaterialOptions object, you can create a SimFluidCavityExpansion
                |     as following:
                | 
                |      Dim MyMaterialOptions As SimMaterialOptions
                |      ...
                |      Dim MyFluidCavityExpansion As SimFluidCavityExpansion
                |      Set MyFluidCavityExpansion = MyMaterialOptions.Add("SimFluidCavityExpansion")
                |      
                | 
                |     Given a SimMaterialOptions object, you can retrieve a
                |     SimFluidCavityExpansion named "Fluid Cavity Expansion.1" as
                |     following:
                | 
                |      Dim MyMaterialOptions As SimMaterialOptions
                |      ...
                |      Dim MyFluidCavityExpansion As SimFluidCavityExpansion
                |      Set MyFluidCavityExpansion = MyMaterialOptions.Item("Fluid Cavity Expansion.1")
                |      
                | 
                | Example in Python:
                |     Given a SimMaterialOptions object myMaterialOptions, you can create a
                |     SimFluidCavityExpansion as following:
                | 
                |      ...
                |      myFluidCavityExpansion = myMaterialOptions.Add("SimFluidCavityExpansion")
                |      
                | 
                |     Given a SimMaterialOptions object myMaterialOptions, you can retrieve a
                |     SimFluidCavityExpansion named "Fluid Cavity Expansion.1" as
                |     following:
                | 
                |      ...
                |      myFluidCavityExpansion = myMaterialOptions.Item("Fluid Cavity Expansion.1")
                |      
                | 
                | See also:
                |     SimMaterialOptions
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def material_table(self) -> SimMaterialTable:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property MaterialTable() As SimMaterialTable (Read Only)
                |     Returns the material table.
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

        return SimMaterialTable(self.com_object.MaterialTable)

    @property
    def reference_temperature(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ReferenceTemperature() As double
                |     Returns or sets the reference temperature.
                | 
                |     Parameters:
                | 
                |         iReferenceTemperature[in]
                |             The reference temperature. Quantity: TEMPRTRE, Units: Kdeg In CFD
                |             analysis this parameter should be set equal to the reference temperature used
                |             for the Boussinesq approximation of buoyancy forces.
                |             
                |         oReferenceTemperature[out]
                |             The reference temperature. Quantity: TEMPRTRE, Units: Kdeg
                |             
                | 
                |     Returns:
                |         S_OK if successful. E_FAIL if failed.

        :return: float
        """

        return self.com_object.ReferenceTemperature

    @reference_temperature.setter
    def reference_temperature(self, value: float):
        """
        :param float value:
        """

        self.com_object.ReferenceTemperature = value

    def get_material_table_column(self, i_material_table_column: int) -> SimTableColumn:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetMaterialTableColumn(SimFluidCavityExpansionMaterialTableColumn
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
                |             specified column is not found in the table. 
                | 
                |     Returns:
                |         S_OK if successful. S_FALSE if the supplied MaterialTableColumn enum is
                |         valid but the column does not exist currently or exists currently but is not
                |         active. E_INVALIDARG if the supplied MaterialTableColumn enum is invalid.
                |         E_FAIL otherwise. 

        :param int i_material_table_column:
        :return: SimTableColumn
        """
        return SimTableColumn(self.com_object.GetMaterialTableColumn(i_material_table_column))

    def __repr__(self):
        return f'SimFluidCavityExpansion(name="{ self.name }")'
