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


class SimUltimateStrength(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimUltimateStrength
                | 
                | Represents the Ultimate Strength object.
                | 
                | Example:
                |     Given a SimMaterialOptions object, you can create a SimUltimateStrength as
                |     following:
                | 
                |      Dim MyMaterialOptions As SimMaterialOptions
                |      ...
                |      Dim MyUltimateStrength As SimUltimateStrength
                |      Set MyUltimateStrength = MyMaterialOptions.Add("SimUltimateStrength")
                |      
                | 
                |     Given a SimMaterialOptions object, you can retrieve a SimUltimateStrength
                |     named "Ultimate Strength.1" as following:
                | 
                |      Dim MyMaterialOptions As SimMaterialOptions
                |      ...
                |      Dim MyUltimateStrength As SimUltimateStrength
                |      Set MyUltimateStrength = MyMaterialOptions.Item("Ultimate Strength.1")
                |      
                | 
                | Example in Python:
                |     Given a SimMaterialOptions object myMaterialOptions, you can create a
                |     SimUltimateStrength as following:
                | 
                |      ...
                |      myUltimateStrength = myMaterialOptions.Add("SimUltimateStrength")
                |      
                | 
                |     Given a SimMaterialOptions object myMaterialOptions, you can retrieve a
                |     SimUltimateStrength named "Ultimate Strength.1" as
                |     following:
                | 
                |      ...
                |      myUltimateStrength = myMaterialOptions.Item("Ultimate Strength.1")
                |      
                | 
                | See also:
                |     SimMaterialOptions
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def material_compressive_table(self) -> SimMaterialTable:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property MaterialCompressiveTable() As SimMaterialTable (Read
                | Only)
                |     Returns the compressive material table.

        :return: SimMaterialTable
        """

        return SimMaterialTable(self.com_object.MaterialCompressiveTable)

    @property
    def material_tensile_table(self) -> SimMaterialTable:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property MaterialTensileTable() As SimMaterialTable (Read
                | Only)
                |     Returns the tensile material table.

        :return: SimMaterialTable
        """

        return SimMaterialTable(self.com_object.MaterialTensileTable)

    def get_material_compressive_table_column(self, i_material_compressive_table_column: int) -> SimTableColumn:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func
                | GetMaterialCompressiveTableColumn(SimUltimateStrengthMaterialCompressiveTableColumn iMaterialCompressiveTableColumn) As SimTableColum
                | n
                |     Retrieves the column object for the specified table column in compressive
                |     table.
                | 
                |     Parameters:
                | 
                |         iMaterialCompressiveTableColumn[in]
                |             The compressive table column. 
                | 
                |     Returns:
                |         The table column object. This value will be NULL_var in case the
                |         specified column is not found in the table.

        :param int i_material_compressive_table_column:
        :return: SimTableColumn
        """
        return SimTableColumn(self.com_object.GetMaterialCompressiveTableColumn(i_material_compressive_table_column))

    def get_material_tensile_table_column(self, i_material_tensile_table_column: int) -> SimTableColumn:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func
                | GetMaterialTensileTableColumn(SimUltimateStrengthMaterialTensileTableColumn
                | iMaterialTensileTableColumn) As SimTableColumn
                |     Retrieves the column object for the specified table column in tensile
                |     table.
                | 
                |     Parameters:
                | 
                |         iMaterialTensileTableColumn[in]
                |             The tensile table column. 
                | 
                |     Returns:
                |         The table column object. This value will be NULL_var in case the
                |         specified column is not found in the table. 

        :param int i_material_tensile_table_column:
        :return: SimTableColumn
        """
        return SimTableColumn(self.com_object.GetMaterialTensileTableColumn(i_material_tensile_table_column))

    def __repr__(self):
        return f'SimUltimateStrength(name="{ self.name }")'
