"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.sma_mpa_base.sim_table import SimTable
from pycatia3dx.sma_mpa_base.sim_table_column import SimTableColumn
from pycatia3dx.system.any_object import AnyObject


class SimPeriodicAmplitude(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimPeriodicAmplitude
                | 
                | Represents the Periodic Amplitude object.
                | 
                | Given a SimFeatures object, you can create SimAmplitude and retrieve the
                | SimPeriodicAmplitude. The following example demonstrates this.
                | 
                | Example:
                |     Given a SimFeatures object, you can create a SimAmplitude and retrieve the
                |     SimPeriodicAmplitude as following:
                | 
                |      Dim MyFeatures As SimFeatures
                |      ...
                |      Dim MyAmplitude As SimAmplitude
                |      Set MyAmplitude = MyFeatures.Add("SimAmplitude")
                |      MyAmplitude.DefinitionType = SimAmplitudePeriodicDefinition
                |      Dim MyPeriodicAmplitude As SimPeriodicAmplitude
                |      Set MyPeriodicAmplitude = MyAmplitude.PeriodicAmplitude
                |      
                | 
                | Example in Python:
                |     Given a SimFeatures object, you can create a SimAmplitude and retrieve the
                |     SimPeriodicAmplitude as following:
                | 
                |      ...
                |      myAmplitude = myFeatures.Add("SimAmplitude")
                |      myAmplitude.DefinitionType = SimAmplitudePeriodicDefinition
                |      myPeriodicAmplitude = myAmplitude.PeriodicAmplitude
                |      
                | 
                | See also:
                |     SimFeatures, SimAmplitude
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def circular_frequency(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property CircularFrequency() As double
                |     Returns or sets the circular frequency. Quantity: ANGULAR_VELOCITY, units:
                |     rad_s.

        :return: float
        """

        return self.com_object.CircularFrequency

    @circular_frequency.setter
    def circular_frequency(self, value: float):
        """
        :param float value:
        """

        self.com_object.CircularFrequency = value

    @property
    def initial_amplitude(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property InitialAmplitude() As double
                |     Returns or sets the initial amplitude. Quantity: DIMENSIONLESS, units:
                |     None.

        :return: float
        """

        return self.com_object.InitialAmplitude

    @initial_amplitude.setter
    def initial_amplitude(self, value: float):
        """
        :param float value:
        """

        self.com_object.InitialAmplitude = value

    @property
    def starting_time(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property StartingTime() As double
                |     Returns or sets the starting time. Quantity: TIME, units: s.

        :return: float
        """

        return self.com_object.StartingTime

    @starting_time.setter
    def starting_time(self, value: float):
        """
        :param float value:
        """

        self.com_object.StartingTime = value

    @property
    def table(self) -> SimTable:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Table() As SimTable (Read Only)
                |     Returns the table.

        :return: SimTable
        """

        return SimTable(self.com_object.Table)

    def get_table_column(self, i_table_column_name: int) -> SimTableColumn:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetTableColumn(SimPeriodicAmplitudeColumnType iTableColumnName) As
                | SimTableColumn
                |     Retrieves a specific column of the table that determines the periodic
                |     amplitude behavior.
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
        return f'SimPeriodicAmplitude(name="{ self.name }")'
