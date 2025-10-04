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


class SimGasketMembraneElastic(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimGasketMembraneElastic
                | 
                | Represents the Gasket Membrane Elastic object.
                | 
                | Example:
                |     Given a SimMaterialOptions object, you can create a
                |     SimGasketMembraneElastic as following:
                | 
                |      Dim MyMaterialOptions As SimMaterialOptions
                |      ...
                |      Dim MyGasketMembraneElastic As SimGasketMembraneElastic
                |      Set MyGasketMembraneElastic = MyMaterialOptions.Add("SimGasketMembraneElastic")
                |      
                | 
                |     Given a SimMaterialOptions object, you can retrieve a
                |     SimGasketMembraneElastic named "Gasket Membrane Elastic.1" as
                |     following:
                | 
                |      Dim MyMaterialOptions As SimMaterialOptions
                |      ...
                |      Dim MyGasketMembraneElastic As SimGasketMembraneElastic
                |      Set MyGasketMembraneElastic = MyMaterialOptions.Item("Gasket Membrane Elastic.1")
                |      
                | 
                | Example in Python:
                |     Given a SimMaterialOptions object myMaterialOptions, you can create a
                |     SimGasketMembraneElastic as following:
                | 
                |      ...
                |      myGasketMembraneElastic = myMaterialOptions.Add("SimGasketMembraneElastic")
                |      
                | 
                |     Given a SimMaterialOptions object myMaterialOptions, you can retrieve a
                |     SimGasketMembraneElastic named "Gasket Membrane Elastic.1" as
                |     following:
                | 
                |      ...
                |      myGasketMembraneElastic = myMaterialOptions.Item("Gasket Membrane Elastic.1")
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

    def get_material_table_column(self, i_material_table_column: int) -> SimTableColumn:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetMaterialTableColumn(SimGasketMembraneElasticMaterialTableColumn
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

        :param int i_material_table_column:
        :return: SimTableColumn
        """
        return SimTableColumn(self.com_object.GetMaterialTableColumn(i_material_table_column))

    def __repr__(self):
        return f'SimGasketMembraneElastic(name="{ self.name }")'
