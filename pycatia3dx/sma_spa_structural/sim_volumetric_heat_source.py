"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.sma_mpa_foundation.sim_feature_history import SimFeatureHistory
from pycatia3dx.system.any_object import AnyObject


class SimVolumetricHeatSource(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimVolumetricHeatSource
                | 
                | Represents the Volumetric Heat Source object.
                | 
                | Example:
                |     Given a SimFeatures object, you can create a SimVolumetricHeatSource as
                |     following:
                | 
                |      Dim MyFeatures As SimFeatures
                |      ...
                |      Dim MyVolumetricHeatSource As SimVolumetricHeatSource
                |      Set MyVolumetricHeatSource = MyFeatures.Add("SimVolumetricHeatSource")
                |      
                | 
                |     Given a SimFeatures object, you can retrieve a SimVolumetricHeatSource
                |     named "Volumetric Heat Source.1" as following:
                | 
                |      Dim MyFeatures As SimFeatures
                |      ...
                |      Dim MyVolumetricHeatSource As SimVolumetricHeatSource
                |      Set MyVolumetricHeatSource = MyFeatures.Item("Volumetric Heat Source.1")
                |      
                | 
                | Example in Python:
                |     Given a SimFeatures object myFeatures, you can create a
                |     SimVolumetricHeatSource as following:
                | 
                |      ...
                |      myVolumetricHeatSource = myFeatures.Add("SimVolumetricHeatSource")
                |      
                | 
                |     Given a SimFeatures object myFeatures, you can retrieve a
                |     SimVolumetricHeatSource named "Volumetric Heat Source.1" as
                |     following:
                | 
                |      ...
                |      myVolumetricHeatSource = myFeatures.Item("Volumetric Heat Source.1")
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
    def heat_source_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property HeatSourceType() As
                | SimVolumetricHeatSourceHeatSourceType
                |     Returns or sets the heat source type.

        :return: SimVolumetricHeatSourceHeatSourceType
        """

        return self.com_object.HeatSourceType

    @heat_source_type.setter
    def heat_source_type(self, value: int):
        """
        :param int value:
        """

        self.com_object.HeatSourceType = value

    @property
    def uniform_magnitude(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property UniformMagnitude() As double
                |     Returns or sets the heat power value. If the heat source type is set to PerUnitVolume then the unit is : Quantity: HEAT_GENERATION_RATE, units: W_m3. If the heat source type is set to Total then the unit is : Quantity: HEAT_RATE, units: W. 

        :return: float
        """

        return self.com_object.UniformMagnitude

    @uniform_magnitude.setter
    def uniform_magnitude(self, value: float):
        """
        :param float value:
        """

        self.com_object.UniformMagnitude = value

    def __repr__(self):
        return f'SimVolumetricHeatSource(name="{ self.name }")'
