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


class SimFluidCapacity(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimFluidCapacity
                | 
                | Represents the Fluid Capacity object.
                | 
                | Example:
                |     Given a SimMaterialOptions object, you can create a SimFluidCapacity as
                |     following:
                | 
                |      Dim MyMaterialOptions As SimMaterialOptions
                |      ...
                |      Dim MyFluidCapacity As SimFluidCapacity
                |      Set MyFluidCapacity = MyMaterialOptions.Add("SimFluidCapacity")
                |      
                | 
                |     Given a SimMaterialOptions object, you can retrieve a SimFluidCapacity
                |     named "Fluid Capacity.1" as following:
                | 
                |      Dim MyMaterialOptions As SimMaterialOptions
                |      ...
                |      Dim MyFluidCapacity As SimFluidCapacity
                |      Set MyFluidCapacity = MyMaterialOptions.Item("Fluid Capacity.1")
                |      
                | 
                | Example in Python:
                |     Given a SimMaterialOptions object myMaterialOptions, you can create a
                |     SimFluidCapacity as following:
                | 
                |      ...
                |      myFluidCapacity = myMaterialOptions.Add("SimFluidCapacity")
                |      
                | 
                |     Given a SimMaterialOptions object myMaterialOptions, you can retrieve a
                |     SimFluidCapacity named "Fluid Capacity.1" as following:
                | 
                |      ...
                |      myFluidCapacity = myMaterialOptions.Item("Fluid Capacity.1")
                |      
                | 
                | See also:
                |     SimMaterialOptions
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def fluid_capacity_input(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property FluidCapacityInput() As SimFluidCapacityInput
                |     Returns or sets the fluid capacity input.
                | 
                |     Parameters:
                | 
                |         oFluidCapacityInput[out]
                |             The input to the fluid capacity. 
                |         iFluidCapacityInput[in]
                |             The input to the fluid capacity. 
                | 
                |     Returns:
                |         S_OK if successful. E_FAIL if failed.

        :return: SimFluidCapacityInput
        """

        return self.com_object.FluidCapacityInput

    @fluid_capacity_input.setter
    def fluid_capacity_input(self, value: int):
        """
        :param int value:
        """

        self.com_object.FluidCapacityInput = value

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

    def get_material_table_column(self, i_material_table_column: int) -> SimTableColumn:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetMaterialTableColumn(SimFluidCapacityMaterialTableColumn
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
                |         S_OK if successful. S_FALSE if the supplied
                |         SimFluidCapacityMaterialTableColumn enum is valid but the column does not exist
                |         currently or exists currently but is not active. E_INVALIDARG if the supplied
                |         SimFluidCapacityMaterialTableColumn enum is invalid. E_FAIL otherwise.

        :param int i_material_table_column:
        :return: SimTableColumn
        """
        return SimTableColumn(self.com_object.GetMaterialTableColumn(i_material_table_column))

    def __repr__(self):
        return f'SimFluidCapacity(name="{ self.name }")'
