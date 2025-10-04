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


class SimCastIronPlasticity(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimCastIronPlasticity
                | 
                | Represents the Cast Iron Plasticity object.
                | 
                | Example:
                |     Given a SimMaterialOptions object, you can create a SimCastIronPlasticity
                |     as following:
                | 
                |      Dim MyMaterialOptions As SimMaterialOptions
                |      ...
                |      Dim MyCastIronPlasticity As SimCastIronPlasticity
                |      Set MyCastIronPlasticity = MyMaterialOptions.Add("SimCastIronPlasticity")
                |      
                | 
                |     Given a SimMaterialOptions object, you can retrieve a SimCastIronPlasticity
                |     named "Cast Iron Plasticity.1" as following:
                | 
                |      Dim MyMaterialOptions As SimMaterialOptions
                |      ...
                |      Dim MyCastIronPlasticity As SimCastIronPlasticity
                |      Set MyCastIronPlasticity = MyMaterialOptions.Item("Cast Iron Plasticity.1")
                |      
                | 
                | Example in Python:
                |     Given a SimMaterialOptions object myMaterialOptions, you can create a
                |     SimCastIronPlasticity as following:
                | 
                |      ...
                |      myCastIronPlasticity = myMaterialOptions.Add("SimCastIronPlasticity")
                |      
                | 
                |     Given a SimMaterialOptions object myMaterialOptions, you can retrieve a
                |     SimCastIronPlasticity named "Cast Iron Plasticity.1" as
                |     following:
                | 
                |      ...
                |      myCastIronPlasticity = myMaterialOptions.Item("Cast Iron Plasticity.1")
                |      
                | 
                | See also:
                |     SimMaterialOptions
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def compression_hardening_material_table(self) -> SimMaterialTable:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property CompressionHardeningMaterialTable() As SimMaterialTable (Read
                | Only)
                |     Returns the compression hardening material table.

        :return: SimMaterialTable
        """

        return SimMaterialTable(self.com_object.CompressionHardeningMaterialTable)

    @property
    def plasticity_material_table(self) -> SimMaterialTable:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property PlasticityMaterialTable() As SimMaterialTable (Read
                | Only)
                |     Returns the plastic material table.

        :return: SimMaterialTable
        """

        return SimMaterialTable(self.com_object.PlasticityMaterialTable)

    @property
    def tension_hardening_material_table(self) -> SimMaterialTable:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property TensionHardeningMaterialTable() As SimMaterialTable (Read
                | Only)
                |     Returns the tension hardening material table.

        :return: SimMaterialTable
        """

        return SimMaterialTable(self.com_object.TensionHardeningMaterialTable)

    def get_compression_hardening_material_table_column(self, i_material_table_column: int) -> SimTableColumn:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func
                | GetCompressionHardeningMaterialTableColumn(SimCastIronPlasticityCompressionHardeningMaterialTableColumn iMaterialTableColumn) As SimTableColum
                | n
                |     Retrieves the column object for the Compression Hardening table
                |     column.
                | 
                |     Parameters:
                | 
                |         iMaterialTableColumn[in]
                |             The Compression Hardening table column. 
                | 
                |     Returns:
                |         The table column object. This value will be NULL_var in case the
                |         specified column is not found in the table.

        :param int i_material_table_column:
        :return: SimTableColumn
        """
        return SimTableColumn(self.com_object.GetCompressionHardeningMaterialTableColumn(i_material_table_column))

    def get_plasticity_material_table_column(self, i_material_table_column: int) -> SimTableColumn:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func
                | GetPlasticityMaterialTableColumn(SimCastIronPlasticityPlasticityMaterialTableColumn iMaterialTableColumn) As SimTableColum
                | n
                |     Retrieves the column object for the plasticity table
                |     column.
                | 
                |     Parameters:
                | 
                |         iMaterialTableColumn[in]
                |             The plasticity table column. 
                | 
                |     Returns:
                |         The table column object. This value will be NULL_var in case the
                |         specified column is not found in the table.

        :param int i_material_table_column:
        :return: SimTableColumn
        """
        return SimTableColumn(self.com_object.GetPlasticityMaterialTableColumn(i_material_table_column))

    def get_tension_hardening_material_table_column(self, i_material_table_column: int) -> SimTableColumn:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func
                | GetTensionHardeningMaterialTableColumn(SimCastIronPlasticityTensionHardeningMaterialTableColumn iMaterialTableColumn) As SimTableColum
                | n
                |     Retrieves the column object for the Tension Hardening table
                |     column.
                | 
                |     Parameters:
                | 
                |         iMaterialTableColumn[in]
                |             The Tension Hardening table column. 
                | 
                |     Returns:
                |         The table column object. This value will be NULL_var in case the
                |         specified column is not found in the table.

        :param SimCastIronPlasticityTensionHardeningMaterialTableColumn i_material_table_column:
        :return: SimTableColumn
        """
        return SimTableColumn(self.com_object.GetTensionHardeningMaterialTableColumn(i_material_table_column))

    def __repr__(self):
        return f'SimCastIronPlasticity(name="{ self.name }")'
