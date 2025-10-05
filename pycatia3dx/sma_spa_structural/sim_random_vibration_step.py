"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.sma_mpa_base.sim_table import SimTable
from pycatia3dx.sma_mpa_base.sim_table_column import SimTableColumn
from pycatia3dx.sma_mpa_foundation.sim_step import SimStep
from pycatia3dx.sma_spa_structural.sim_frequency_based_damping import SimFrequencyBasedDamping
from pycatia3dx.sma_spa_structural.sim_mode_based_damping import SimModeBasedDamping
from pycatia3dx.sma_spa_structural.sim_random_global_damping import SimRandomGlobalDamping


class SimRandomVibrationStep(SimStep):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SMAMpaFoundationIDLItf.SimStep
                |                         SimRandomVibrationStep
                | 
                | Represents the Random Vibration Step object.
                | 
                | Example:
                |     Given a SimSteps object, you can create a SimRandomVibrationStep as
                |     following:
                | 
                |      Dim MySteps As SimSteps
                |      ...
                |      Dim MyRandomVibrationStep As SimRandomVibrationStep
                |      Set MyRandomVibrationStep = MySteps.Add("SimRandomVibrationStep")
                |      
                | 
                |     Given a SimSteps object, you can retrieve a SimRandomVibrationStep named
                |     "Random Vibration Step.1" as following:
                | 
                |      Dim MySteps As SimSteps
                |      ...
                |      Dim MyRandomVibrationStep As SimRandomVibrationStep
                |      Set MyRandomVibrationStep = MySteps.Item("Random Vibration Step.1")
                |      
                | 
                | Example in Python:
                |     Given a SimSteps object mySteps, you can create a SimRandomVibrationStep as
                |     following:
                | 
                |      ...
                |      myRandomVibrationStep = mySteps.Add("SimRandomVibrationStep")
                |      
                | 
                |     Given a SimSteps object mySteps, you can retrieve a SimRandomVibrationStep
                |     named "Random Vibration Step.1" as following:
                | 
                |      ...
                |      myRandomVibrationStep = mySteps.Item("Random Vibration Step.1")
                |      
                | 
                | See also:
                |     SimSteps
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def activated(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Activated() As boolean
                |     Returns or sets the activation status.

        :return: bool
        """

        return self.com_object.Activated

    @activated.setter
    def activated(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.Activated = value

    @property
    def damping_definition(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property DampingDefinition() As
                | SimRandomVibrationStepDampingDefinition
                |     Returns or sets the damping definition.

        :return: SimRandomVibrationStepDampingDefinition
        """

        return self.com_object.DampingDefinition

    @damping_definition.setter
    def damping_definition(self, value: int):
        """
        :param int value:
        """

        self.com_object.DampingDefinition = value

    @property
    def frequency_based_damping(self) -> SimFrequencyBasedDamping:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property FrequencyBasedDamping() As SimFrequencyBasedDamping (Read
                | Only)
                |     Returns the frequency based damping.

        :return: SimFrequencyBasedDamping
        """

        return SimFrequencyBasedDamping(self.com_object.FrequencyBasedDamping)

    @property
    def mode_based_damping(self) -> SimModeBasedDamping:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ModeBasedDamping() As SimModeBasedDamping (Read Only)
                |     Returns the mode based damping.

        :return: SimModeBasedDamping
        """

        return SimModeBasedDamping(self.com_object.ModeBasedDamping)

    @property
    def random_global_damping(self) -> SimRandomGlobalDamping:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property RandomGlobalDamping() As SimRandomGlobalDamping (Read
                | Only)
                |     Returns the random global damping.

        :return: SimRandomGlobalDamping
        """

        return SimRandomGlobalDamping(self.com_object.RandomGlobalDamping)

    @property
    def table(self) -> SimTable:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Table() As SimTable (Read Only)
                |     Returns the table that determines the random vibration step behavior.

        :return: SimTable
        """

        return SimTable(self.com_object.Table)

    def get_table_column(self, i_table_column_name: int) -> SimTableColumn:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetTableColumn(SimRandomVibrationStepTableColumn iTableColumnName) As
                | SimTableColumn
                |     Retrieves a specific column of the table that determines the random
                |     vibration step behavior.
                | 
                |     Parameters:
                | 
                |         iTableColumnName[in]
                |             The table column name. 
                | 
                |     Returns:
                |         The table column. 

        :param int i_table_column_name:
        :return: SimTableColumn
        """
        return SimTableColumn(self.com_object.GetTableColumn(i_table_column_name))

    def __repr__(self):
        return f'SimRandomVibrationStep(name="{ self.name }")'
