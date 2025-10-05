"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.sma_mpa_foundation.sim_feature_history import SimFeatureHistory
from pycatia3dx.system.any_object import AnyObject


class SimRadiationAmbient(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimRadiationAmbient
                | 
                | Represents the Radiation Ambient object.
                | 
                | Example:
                |     Given a SimFeatures object, you can create a SimRadiationAmbient as
                |     following:
                | 
                |      Dim MyFeatures As SimFeatures
                |      ...
                |      Dim MyRadiationAmbient As SimRadiationAmbient
                |      Set MyRadiationAmbient = MyFeatures.Add("SimRadiationAmbient")
                |      
                | 
                |     Given a SimFeatures object, you can retrieve a SimRadiationAmbient named
                |     "Radiation Ambient.1" as following:
                | 
                |      Dim MyFeatures As SimFeatures
                |      ...
                |      Dim MyRadiationAmbient As SimRadiationAmbient
                |      Set MyRadiationAmbient = MyFeatures.Item("Radiation Ambient.1")
                |      
                | 
                | Example in Python:
                |     Given a SimFeatures object myFeatures, you can create a SimRadiationAmbient
                |     as following:
                | 
                |      ...
                |      myRadiationAmbient = myFeatures.Add("SimRadiationAmbient")
                |      
                | 
                |     Given a SimFeatures object myFeatures, you can retrieve a
                |     SimRadiationAmbient named "Radiation Ambient.1" as
                |     following:
                | 
                |      ...
                |      myRadiationAmbient = myFeatures.Item("Radiation Ambient.1")
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
    def emissivity(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Emissivity() As double
                |     Returns or sets the emissivity of the radiation to ambient. Quantity:
                |     DIMENSIONLESS, units: None

        :return: float
        """

        return self.com_object.Emissivity

    @emissivity.setter
    def emissivity(self, value: float):
        """
        :param float value:
        """

        self.com_object.Emissivity = value

    @property
    def feature_history(self) -> SimFeatureHistory:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property FeatureHistory() As SimFeatureHistory (Read Only)
                |     Returns the feature history.

        :return: SimFeatureHistory
        """

        return SimFeatureHistory(self.com_object.FeatureHistory)

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
    def temperature(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Temperature() As double
                |     Returns or sets the temperature of the radiation to ambient. Quantity:
                |     TEMPRTRE, units: Kdeg 

        :return: float
        """

        return self.com_object.Temperature

    @temperature.setter
    def temperature(self, value: float):
        """
        :param float value:
        """

        self.com_object.Temperature = value

    def __repr__(self):
        return f'SimRadiationAmbient(name="{ self.name }")'
