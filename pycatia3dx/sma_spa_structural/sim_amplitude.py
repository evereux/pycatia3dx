"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.sma_spa_structural.sim_periodic_amplitude import SimPeriodicAmplitude
from pycatia3dx.sma_spa_structural.sim_smooth_step_amplitude import SimSmoothStepAmplitude
from pycatia3dx.sma_spa_structural.sim_tabular_amplitude import SimTabularAmplitude
from pycatia3dx.sma_spa_structural.sim_user_amplitude import SimUserAmplitude


class SimAmplitude(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimAmplitude
                | 
                | Represents the Amplitude object.
                | 
                | Example:
                |     Given a SimFeatures object, you can create a SimAmplitude as
                |     following:
                | 
                |      Dim MyFeatures As SimFeatures
                |      ...
                |      Dim MyAmplitude As SimAmplitude
                |      Set MyAmplitude = MyFeatures.Add("SimAmplitude")
                |      
                | 
                |     Given a SimFeatures object, you can retrieve a SimAmplitude named
                |     "Amplitude.1" as following:
                | 
                |      Dim MyFeatures As SimFeatures
                |      ...
                |      Dim MyAmplitude As SimAmplitude
                |      Set MyAmplitude = MyFeatures.Item("Amplitude.1")
                |      
                | 
                | Example in Python:
                |     Given a SimFeatures object myFeatures, you can create a SimAmplitude as
                |     following:
                | 
                |      ...
                |      myAmplitude = myFeatures.Add("SimAmplitude")
                |      
                | 
                |     Given a SimFeatures object myFeatures, you can retrieve a SimAmplitude
                |     named "Amplitude.1" as following:
                | 
                |      ...
                |      myAmplitude = myFeatures.Item("Amplitude.1")
                |      
                | 
                | See also:
                |     SimFeatures
    
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
    def definition_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property DefinitionType() As SimAmplitudeDefinitionType
                |     Returns or sets the definition type.

        :return: int
        """

        return self.com_object.DefinitionType

    @definition_type.setter
    def definition_type(self, value: int):
        """
        :param int value:
        """

        self.com_object.DefinitionType = value

    @property
    def periodic_amplitude(self) -> SimPeriodicAmplitude:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property PeriodicAmplitude() As SimPeriodicAmplitude (Read
                | Only)
                |     Returns the periodic amplitude.

        :return: SimPeriodicAmplitude
        """

        return SimPeriodicAmplitude(self.com_object.PeriodicAmplitude)

    @property
    def smooth_step_amplitude(self) -> SimSmoothStepAmplitude:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property SmoothStepAmplitude() As SimSmoothStepAmplitude (Read
                | Only)
                |     Returns the smooth step amplitude.

        :return: SimSmoothStepAmplitude
        """

        return SimSmoothStepAmplitude(self.com_object.SmoothStepAmplitude)

    @property
    def spec_tree_category(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property SpecTreeCategory() As CATBSTR (Read Only)
                |     Returns a string representing the specification tree category of the
                |     feature. See SimFeatures.GetSpecTreeCategory for usage.

        :return: str
        """

        return self.com_object.SpecTreeCategory

    @property
    def tabular_amplitude(self) -> SimTabularAmplitude:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property TabularAmplitude() As SimTabularAmplitude (Read Only)
                |     Returns the tabular amplitude.

        :return: SimTabularAmplitude
        """

        return SimTabularAmplitude(self.com_object.TabularAmplitude)

    @property
    def time_span_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property TimeSpanType() As SimAmplitudeTimeSpanType
                |     Returns or sets the time span type.

        :return: int
        """

        return self.com_object.TimeSpanType

    @time_span_type.setter
    def time_span_type(self, value: int):
        """
        :param int value:
        """

        self.com_object.TimeSpanType = value

    @property
    def user_amplitude(self) -> SimUserAmplitude:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property UserAmplitude() As SimUserAmplitude (Read Only)
                |     Returns the user amplitude. 

        :return: SimUserAmplitude
        """

        return SimUserAmplitude(self.com_object.UserAmplitude)

    def __repr__(self):
        return f'SimAmplitude(name="{ self.name }")'
