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


class SimViscoelasticity(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimViscoelasticity
                | 
                | Represents the Viscoelasticity object.
                | 
                | Example:
                |     Given a SimMaterialOptions object, you can create a SimViscoelasticity as
                |     following:
                | 
                |      Dim MyMaterialOptions As SimMaterialOptions
                |      ...
                |      Dim MyViscoelasticity As SimViscoelasticity
                |      Set MyViscoelasticity = MyMaterialOptions.Add("SimViscoelasticity")
                |      
                | 
                |     Given a SimMaterialOptions object, you can retrieve a SimViscoelasticity
                |     named "Viscoelasticity.1" as following:
                | 
                |      Dim MyMaterialOptions As SimMaterialOptions
                |      ...
                |      Dim MyViscoelasticity As SimViscoelasticity
                |      Set MyViscoelasticity = MyMaterialOptions.Item("Viscoelasticity.1")
                |      
                | 
                | Example in Python:
                |     Given a SimMaterialOptions object myMaterialOptions, you can create a
                |     SimViscoelasticity as following:
                | 
                |      ...
                |      myViscoelasticity = myMaterialOptions.Add("SimViscoelasticity")
                |      
                | 
                |     Given a SimMaterialOptions object myMaterialOptions, you can retrieve a
                |     SimViscoelasticity named "Viscoelasticity.1" as following:
                | 
                |      ...
                |      myViscoelasticity = myMaterialOptions.Item("Viscoelasticity.1")
                |      
                | 
                | See also:
                |     SimMaterialOptions
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def error_tolerance(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ErrorTolerance() As double
                |     Returns or sets the error tolerance for time domain viscoelasticity with
                |     frequency-dependent test data.

        :return: float
        """

        return self.com_object.ErrorTolerance

    @error_tolerance.setter
    def error_tolerance(self, value: float):
        """
        :param float value:
        """

        self.com_object.ErrorTolerance = value

    @property
    def frequency_domain_sub_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property FrequencyDomainSubType() As
                | SimViscoelasticityFrequencyType
                |     Returns or sets the type of frequency domain viscoelasticity.

        :return: int
        """

        return self.com_object.FrequencyDomainSubType

    @frequency_domain_sub_type.setter
    def frequency_domain_sub_type(self, value: int):
        """
        :param int value:
        """

        self.com_object.FrequencyDomainSubType = value

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
    def nmax(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Nmax() As long
                |     Returns or sets the number of terms in Prony series for time domain
                |     viscoelasticity with frequency-dependent test data.

        :return: int
        """

        return self.com_object.Nmax

    @nmax.setter
    def nmax(self, value: int):
        """
        :param int value:
        """

        self.com_object.Nmax = value

    @property
    def preload(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Preload() As SimViscoelasticityPreloadType
                |     Returns or sets the type of preload used for frequency domain
                |     viscoelasticity with tabular data.

        :return: int
        """

        return self.com_object.Preload

    @preload.setter
    def preload(self, value: int):
        """
        :param int value:
        """

        self.com_object.Preload = value

    @property
    def tabular_sub_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property TabularSubType() As SimViscoelasticityTabularSubType
                |     Returns or sets the type of tabular data for frequency domain
                |     viscoelasticity.

        :return: int
        """

        return self.com_object.TabularSubType

    @tabular_sub_type.setter
    def tabular_sub_type(self, value: int):
        """
        :param int value:
        """

        self.com_object.TabularSubType = value

    @property
    def time_domain_sub_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property TimeDomainSubType() As SimViscoelasticityTimeType
                |     Returns or sets the type of time domain viscoelasticity.

        :return: int
        """

        return self.com_object.TimeDomainSubType

    @time_domain_sub_type.setter
    def time_domain_sub_type(self, value: int):
        """
        :param int value:
        """

        self.com_object.TimeDomainSubType = value

    @property
    def viscoelasticity_domain(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ViscoelasticityDomain() As
                | SimViscoelasticityViscoelasticityDomain
                |     Returns or sets the type of viscoelasticity domain.

        :return: int
        """

        return self.com_object.ViscoelasticityDomain

    @viscoelasticity_domain.setter
    def viscoelasticity_domain(self, value: int):
        """
        :param int value:
        """

        self.com_object.ViscoelasticityDomain = value

    def get_material_table_column(self, i_material_table_column: int) -> SimTableColumn:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetMaterialTableColumn(SimViscoelasticityMaterialTableColumn
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
        return f'SimViscoelasticity(name="{ self.name }")'
