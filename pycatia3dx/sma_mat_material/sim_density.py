"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.sma_mat_material.sim_material_table import SimMaterialTable
from pycatia3dx.sma_mpa_base.sim_table_column import SimTableColumn


class SimDensity(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimDensity
                | 
                | Represents the Density object.
                | 
                | Example:
                |     Given a SimMaterialOptions object, you can create a SimDensity as
                |     following:
                | 
                |      Dim MyMaterialOptions As SimMaterialOptions
                |      ...
                |      Dim MyDensity As SimDensity
                |      Set MyDensity = MyMaterialOptions.Add("SimDensity")
                |      
                | 
                |     Given a SimMaterialOptions object, you can retrieve a SimDensity named
                |     "Density.1" as following:
                | 
                |      Dim MyMaterialOptions As SimMaterialOptions
                |      ...
                |      Dim MyDensity As SimDensity
                |      Set MyDensity = MyMaterialOptions.Item("Density.1")
                |      
                | 
                | Example in Python:
                |     Given a SimMaterialOptions object myMaterialOptions, you can create a
                |     SimDensity as following:
                | 
                |      ...
                |      myDensity = myMaterialOptions.Add("SimDensity")
                |      
                | 
                |     Given a SimMaterialOptions object myMaterialOptions, you can retrieve a
                |     SimDensity named "Density.1" as following:
                | 
                |      ...
                |      myDensity = myMaterialOptions.Item("Density.1")
                |      
                | 
                | See also:
                |     SimMaterialOptions
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def core_material_density(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property CoreMaterialDensity() As double (Read Only)
                |     Returns the core material density value. Quantity: DENSITY, Units: kg_m3

        :return: float
        """

        return self.com_object.CoreMaterialDensity

    @property
    def core_material_density_flag(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property CoreMaterialDensityFlag() As boolean
                |     Returns or sets the flag that determines if the core material density is
                |     used instead of the material table.
                | 
                |     TRUE: The core material density is used instead of the material
                |     table.
                | 
                |     FALSE: The material table is used instead of the core material density.

        :return: bool
        """

        return self.com_object.CoreMaterialDensityFlag

    @core_material_density_flag.setter
    def core_material_density_flag(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.CoreMaterialDensityFlag = value

    @property
    def material_table(self) -> SimMaterialTable:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property MaterialTable() As SimMaterialTable (Read Only)
                |     Returns the material table.

        :return: SimMaterialTable
        """

        return SimMaterialTable(self.com_object.MaterialTable)

    def get_material_table_column(self, i_material_table_column: int) -> SimTableColumn:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetMaterialTableColumn(SimDensityMaterialTableColumn iMaterialTableColumn)
                | As SimTableColumn
                |     Retrieves the column object for the specified table
                |     column.
                | 
                |     Parameters:
                | 
                |         iMaterialTableColumn[in]
                |             The specified table column. 
                | 
                |     Returns:
                |         The table column object. This value will be NULL_var in case the
                |         specified column is not found in the table.

        :param int i_material_table_column:
        :return: SimTableColumn
        """
        return SimTableColumn(self.com_object.GetMaterialTableColumn(i_material_table_column))

    def __repr__(self):
        return f'SimDensity(name="{ self.name }")'
