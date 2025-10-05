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


class SimGasketTransverseShearElastic(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimGasketTransverseShearElastic
                | 
                | Represents the Gasket Transverse Shear Elastic object.
                | 
                | Example:
                |     Given a SimMaterialOptions object, you can create a
                |     SimGasketTransverseShearElastic as following:
                | 
                |      Dim MyMaterialOptions As SimMaterialOptions
                |      ...
                |      Dim MyGasketTransverseShearElastic As
                |      SimGasketTransverseShearElastic
                |      Set MyGasketTransverseShearElastic = MyMaterialOptions.Add("SimGasketTransverseShearElastic")
                |      
                | 
                |     Given a SimMaterialOptions object, you can retrieve a
                |     SimGasketTransverseShearElastic named "Gasket Transverse Shear Elastic.1" as
                |     following:
                | 
                |      Dim MyMaterialOptions As SimMaterialOptions
                |      ...
                |      Dim MyGasketTransverseShearElastic As
                |      SimGasketTransverseShearElastic
                |      Set MyGasketTransverseShearElastic = MyMaterialOptions.Item("Gasket Transverse Shear Elastic.1")
                |      
                | 
                | Example in Python:
                |     Given a SimMaterialOptions object myMaterialOptions, you can create a
                |     SimGasketTransverseShearElastic as following:
                | 
                |      ...
                |      myGasketTransverseShearElastic = myMaterialOptions.Add("SimGasketTransverseShearElastic")
                |      
                | 
                |     Given a SimMaterialOptions object myMaterialOptions, you can retrieve a
                |     SimGasketTransverseShearElastic named "Gasket Transverse Shear Elastic.1" as
                |     following:
                | 
                |      ...
                |      myGasketTransverseShearElastic = myMaterialOptions.Item("Gasket Transverse Shear Elastic.1")
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

        :return: SimMaterialTable
        """

        return SimMaterialTable(self.com_object.MaterialTable)

    @property
    def unit_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property UnitType() As SimGasketTransverseShearElasticUnitType
                |     Returns or sets the unit type.

        :return: SimGasketTransverseShearElasticUnitType
        """

        return self.com_object.UnitType

    @unit_type.setter
    def unit_type(self, value: int):
        """
        :param int value:
        """

        self.com_object.UnitType = value

    def get_material_table_column(self, i_material_table_column: int) -> SimTableColumn:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetMaterialTableColumn(SimGasketTransverseShearElasticMaterialTableColumn
                | iMaterialTableColumn) As SimTableColumn
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

        :param i_material_table_column:
        :return: SimTableColumn
        """
        return SimTableColumn(self.com_object.GetMaterialTableColumn(i_material_table_column))

    def __repr__(self):
        return f'SimGasketTransverseShearElastic(name="{ self.name }")'
