"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.sma_mat_material.sim_damage_stabilization import SimDamageStabilization
from pycatia3dx.sma_mat_material.sim_material_table import SimMaterialTable
from pycatia3dx.sma_mpa_base.sim_table_column import SimTableColumn


class SimHashinDamageEvolution(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimHashinDamageEvolution
                | 
                | Represents the Hashin Damage Evolution object.
                | 
                | Example:
                |     Given a SimMaterialOptions object, you can create a
                |     SimHashinDamageEvolution as following:
                | 
                |      Dim MyMaterialOptions As SimMaterialOptions
                |      ...
                |      Dim MyHashinDamageEvolution As SimHashinDamageEvolution
                |      Set MyHashinDamageEvolution = MyMaterialOptions.Add("SimHashinDamageEvolution")
                |      
                | 
                |     Given a SimMaterialOptions object, you can retrieve a
                |     SimHashinDamageEvolution named "Hashin Damage Evolution.1" as
                |     following:
                | 
                |      Dim MyMaterialOptions As SimMaterialOptions
                |      ...
                |      Dim MyHashinDamageEvolution As SimHashinDamageEvolution
                |      Set MyHashinDamageEvolution = MyMaterialOptions.Item("Hashin Damage Evolution.1")
                |      
                | 
                | Example in Python:
                |     Given a SimMaterialOptions object myMaterialOptions, you can create a
                |     SimHashinDamageEvolution as following:
                | 
                |      ...
                |      myHashinDamageEvolution = myMaterialOptions.Add("SimHashinDamageEvolution")
                |      
                | 
                |     Given a SimMaterialOptions object myMaterialOptions, you can retrieve a
                |     SimHashinDamageEvolution named "Hashin Damage Evolution.1" as
                |     following:
                | 
                |      ...
                |      myHashinDamageEvolution = myMaterialOptions.Item("Hashin Damage Evolution.1")
                |      
                | 
                | See also:
                |     SimMaterialOptions
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def damage_stabilization(self) -> SimDamageStabilization:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property DamageStabilization() As SimDamageStabilization (Read
                | Only)
                |     Returns the damage stabilization material option.
                | 
                |     Parameters:
                | 
                |         oDamageStabilization[out]
                |             The damage stabilization. 
                | 
                |     Returns:
                |         S_OK if successful.

        :return: SimDamageStabilization
        """

        return SimDamageStabilization(self.com_object.DamageStabilization)

    @property
    def damage_stabilization_flag(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property DamageStabilizationFlag() As boolean
                |     Returns or sets damage stabilization flag.
                | 
                |     Parameters:
                | 
                |         oDamageStabilizationFlag[out]
                |             The damage stabilization flag.
                |             TRUE: the damage stabilization is true when damage stabiization is
                |             present.
                |             FALSE: the damage stabilization is false when damage stabiization
                |             is absent 
                |         iDamageStabilizationFlag[in]
                |             The damage stabilization flag.
                |             TRUE: the damage stabilization will set to true and damage
                |             stabiization sub-option will be created.
                |             FALSE: the damage stabilization will be set false and damage
                |             stabiization sub-option will be deleted. 
                | 
                |     Returns:
                |         S_OK if successful. E_FAIL if failed.

        :return: bool
        """

        return self.com_object.DamageStabilizationFlag

    @damage_stabilization_flag.setter
    def damage_stabilization_flag(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.DamageStabilizationFlag = value

    @property
    def evolution_condition(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property EvolutionCondition() As
                | SimHashinDamageEvolutionCondition
                |     Returns or sets the evolution condition for hashin damage for
                |     fiber-reinforced composites.
                | 
                |     Parameters:
                | 
                |         oEvolutionCondition[out]
                |             The evolution. 
                |         iEvolutionCondition[in]
                |             The evolution. 
                | 
                |     Returns:
                |         S_OK if successful.

        :return: int
        """

        return self.com_object.EvolutionCondition

    @evolution_condition.setter
    def evolution_condition(self, value: int):
        """
        :param int value:
        """

        self.com_object.EvolutionCondition = value

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
                |         S_OK if successful.

        :return: SimMaterialTable
        """

        return SimMaterialTable(self.com_object.MaterialTable)

    @property
    def softening_response(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property SofteningResponse() As
                | SimHashinDamageEvolutionSofteningResponse
                |     Returns or sets the softening response during hashin damage evolution in
                |     fiber-reinforced composites.
                | 
                |     Parameters:
                | 
                |         oSofteningResponse[out]
                |             The softening stress-strain response. 
                |         iSofteningResponse[in]
                |             The softening stress-strain response. 
                | 
                |     Returns:
                |         S_OK if successful.

        :return: int
        """

        return self.com_object.SofteningResponse

    @softening_response.setter
    def softening_response(self, value: int):
        """
        :param int value:
        """

        self.com_object.SofteningResponse = value

    def get_material_table_column(self, i_material_table_column: int) -> SimTableColumn:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetMaterialTableColumn(SimHashinDamageEvolutionMaterialTableColumn
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
                |         SimHashinDamageEvolutionMaterialTableColumn enum is valid but the column does
                |         not exist currently or exists currently but is not active. E_INVALIDARG if the
                |         supplied SimHashinDamageEvolutionMaterialTableColumn enum is invalid. E_FAIL
                |         otherwise. 

        :param int i_material_table_column:
        :return: SimTableColumn
        """
        return SimTableColumn(self.com_object.GetMaterialTableColumn(i_material_table_column))

    def __repr__(self):
        return f'SimHashinDamageEvolution(name="{ self.name }")'
