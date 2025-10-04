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


class SimDuctDamageEvolution(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimDuctDamageEvolution
                | 
                | Represents the Damage Evolution object.
                | 
                | Example:
                |     Given a SimMaterialOptions object, you can create a SimDamageEvolution as
                |     following:
                | 
                |      Dim MyMaterialOptions As SimMaterialOptions
                |      ...
                |      Dim MyDamageEvolution As SimDamageEvolution
                |      Set MyDamageEvolution = MyMaterialOptions.Add("SimDamageEvolution")
                |      
                | 
                |     Given a SimMaterialOptions object, you can retrieve a SimDamageEvolution
                |     named "Damage Evolution.1" as following:
                | 
                |      Dim MyMaterialOptions As SimMaterialOptions
                |      ...
                |      Dim MyDamageEvolution As SimDamageEvolution
                |      Set MyDamageEvolution = MyMaterialOptions.Item("Damage Evolution.1")
                |      
                | 
                | Example in Python:
                |     Given a SimMaterialOptions object myMaterialOptions, you can create a
                |     SimDamageEvolution as following:
                | 
                |      ...
                |      myDamageEvolution = myMaterialOptions.Add("SimDamageEvolution")
                |      
                | 
                |     Given a SimMaterialOptions object myMaterialOptions, you can retrieve a
                |     SimDamageEvolution named "Damage Evolution.1" as
                |     following:
                | 
                |      ...
                |      myDamageEvolution = myMaterialOptions.Item("Damage Evolution.1")
                |      
                | 
                | See also:
                |     SimMaterialOptions
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def degradation(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Degradation() As SimDamageEvolutionDegradation
                |     Returns or sets the degradation type.

        :return: int
        """

        return self.com_object.Degradation

    @degradation.setter
    def degradation(self, value: int):
        """
        :param int value:
        """

        self.com_object.Degradation = value

    @property
    def evolution_category(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property EvolutionCategory() As SimDamageEvolutionCategory
                |     Returns or sets the evolution type.

        :return: int
        """

        return self.com_object.EvolutionCategory

    @evolution_category.setter
    def evolution_category(self, value: int):
        """
        :param int value:
        """

        self.com_object.EvolutionCategory = value

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
    def softening(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Softening() As SimDamageEvolutionSoftening
                |     Returns or sets the softening type.

        :return: SimDamageEvolutionSoftening
        """

        return self.com_object.Softening

    @softening.setter
    def softening(self, value: int):
        """
        :param int value:
        """

        self.com_object.Softening = value

    def get_material_table_column(self, i_material_table_column: int) -> SimTableColumn:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetMaterialTableColumn(SimDamageEvolutionMaterialTableColumn
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
                |         S_OK if successful. S_FALSE if the supplied TableColumn enum is valid
                |         but the column does not exist currently or exists currently but is not active.
                |         E_INVALIDARG if the supplied TableColumn enum is invalid. E_FAIL otherwise.

        :param int i_material_table_column:
        :return: SimTableColumn
        """
        return SimTableColumn(self.com_object.GetMaterialTableColumn(i_material_table_column))

    def __repr__(self):
        return f'SimDuctDamageEvolution(name="{ self.name }")'
