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


class SimPlastic(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimPlastic
                | 
                | Represents the Plastic object.
                | 
                | Example:
                |     Given a SimMaterialOptions object, you can create a SimPlastic as
                |     following:
                | 
                |      Dim MyMaterialOptions As SimMaterialOptions
                |      ...
                |      Dim MyPlastic As SimPlastic
                |      Set MyPlastic = MyMaterialOptions.Add("SimPlastic")
                |      
                | 
                |     Given a SimMaterialOptions object, you can retrieve a SimPlastic named
                |     "Plastic.1" as following:
                | 
                |      Dim MyMaterialOptions As SimMaterialOptions
                |      ...
                |      Dim MyPlastic As SimPlastic
                |      Set MyPlastic = MyMaterialOptions.Item("Plastic.1")
                |      
                | 
                | Example in Python:
                |     Given a SimMaterialOptions object myMaterialOptions, you can create a
                |     SimPlastic as following:
                | 
                |      ...
                |      myPlastic = myMaterialOptions.Add("SimPlastic")
                |      
                | 
                |     Given a SimMaterialOptions object myMaterialOptions, you can retrieve a
                |     SimPlastic named "Plastic.1" as following:
                | 
                |      ...
                |      myPlastic = myMaterialOptions.Item("Plastic.1")
                |      
                | 
                | See also:
                |     SimMaterialOptions
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def isotropic_material_table(self) -> SimMaterialTable:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property IsotropicMaterialTable() As SimMaterialTable (Read
                | Only)
                |     Returns the material table pointer to Isotropic table.

        :return: SimMaterialTable
        """

        return SimMaterialTable(self.com_object.IsotropicMaterialTable)

    @property
    def kinematic_material_table(self) -> SimMaterialTable:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property KinematicMaterialTable() As SimMaterialTable (Read
                | Only)
                |     Returns the material table pointer to kinematic table.

        :return: SimMaterialTable
        """

        return SimMaterialTable(self.com_object.KinematicMaterialTable)

    @property
    def number_of_back_stresses(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property NumberOfBackStresses() As long
                |     Returns or sets the number of backstresses.

        :return: int
        """

        return self.com_object.NumberOfBackStresses

    @number_of_back_stresses.setter
    def number_of_back_stresses(self, value: int):
        """
        :param int value:
        """

        self.com_object.NumberOfBackStresses = value

    @property
    def plastic_hardening(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property PlasticHardening() As SimPlasticPlasticHardening
                |     Returns or sets the type of hardening.

        :return: int
        """

        return self.com_object.PlasticHardening

    @plastic_hardening.setter
    def plastic_hardening(self, value: int):
        """
        :param int value:
        """

        self.com_object.PlasticHardening = value

    @property
    def plastic_yield_criterion(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property PlasticYieldCriterion() As
                | SimPlasticPlasticYieldCriteria
                |     Returns or sets the type of plastic yield criteria.

        :return: SimPlasticPlasticYieldCriteria
        """

        return self.com_object.PlasticYieldCriterion

    @plastic_yield_criterion.setter
    def plastic_yield_criterion(self, value: int):
        """
        :param int value:
        """

        self.com_object.PlasticYieldCriterion = value

    @property
    def potential_material_table(self) -> SimMaterialTable:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property PotentialMaterialTable() As SimMaterialTable (Read
                | Only)
                |     Returns the material table pointer to potential table.

        :return: SimMaterialTable
        """

        return SimMaterialTable(self.com_object.PotentialMaterialTable)

    def get_isotropic_material_table_column(self, i_isotropic_material_table_column: int) -> SimTableColumn:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetIsotropicMaterialTableColumn(SimPlasticIsotropicMaterialTableColumn
                | iIsotropicMaterialTableColumn) As SimTableColumn
                |     Retrieves the column object for the Isotropic table
                |     column.
                | 
                |     Parameters:
                | 
                |         iIsotropicMaterialTableColumn[in]
                |             The Isotropic table column. 
                | 
                |     Returns:
                |         The table column object. This value will be NULL_var in case the
                |         specified column is not found in the table.

        :param int i_isotropic_material_table_column:
        :return: SimTableColumn
        """
        return SimTableColumn(self.com_object.GetIsotropicMaterialTableColumn(i_isotropic_material_table_column))

    def get_kinematic_material_table_column(self, i_kinematic_material_table_column: int) -> SimTableColumn:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetKinematicMaterialTableColumn(SimPlasticKinematicMaterialTableColumn
                | iKinematicMaterialTableColumn) As SimTableColumn
                |     Retrieves the column object for the Kinematic table
                |     column.
                | 
                |     Parameters:
                | 
                |         iKinematicMaterialTableColumn[in]
                |             The Kinematic table column. 
                | 
                |     Returns:
                |         The table column object. This value will be NULL_var in case the
                |         specified column is not found in the table.

        :param int i_kinematic_material_table_column:
        :return: SimTableColumn
        """
        return SimTableColumn(self.com_object.GetKinematicMaterialTableColumn(i_kinematic_material_table_column))

    def get_potential_material_table_column(self, i_potential_material_table_column: int) -> SimTableColumn:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetPotentialMaterialTableColumn(SimPlasticPotentialMaterialTableColumn
                | iPotentialMaterialTableColumn) As SimTableColumn
                |     Retrieves the column object for the Potential table
                |     column.
                | 
                |     Parameters:
                | 
                |         iPotentialMaterialTableColumn[in]
                |             The Potential table column. 
                | 
                |     Returns:
                |         The table column object. This value will be NULL_var in case the
                |         specified column is not found in the table. 

        :param int i_potential_material_table_column:
        :return: SimTableColumn
        """
        return SimTableColumn(self.com_object.GetPotentialMaterialTableColumn(i_potential_material_table_column))

    def __repr__(self):
        return f'SimPlastic(name="{ self.name }")'
