"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.sma_mpa_foundation.sim_feature_history import SimFeatureHistory
from pycatia3dx.system.any_object import AnyObject


class SimMassScaling(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimMassScaling
                | 
                | Represents the Mass Scaling object.
                | 
                | Example:
                |     Given a SimFeatures object, you can create a SimMassScaling as
                |     following:
                | 
                |      Dim MyFeatures As SimFeatures
                |      ...
                |      Dim MyMassScaling As SimMassScaling
                |      Set MyMassScaling = MyFeatures.Add("SimMassScaling")
                |      
                | 
                |     Given a SimFeatures object, you can retrieve a SimMassScaling named "Mass
                |     Scaling.1" as following:
                | 
                |      Dim MyFeatures As SimFeatures
                |      ...
                |      Dim MyMassScaling As SimMassScaling
                |      Set MyMassScaling = MyFeatures.Item("Mass Scaling.1")
                |      
                | 
                | Example in Python:
                |     Given a SimFeatures object myFeatures, you can create a SimMassScaling as
                |     following:
                | 
                |      ...
                |      myMassScaling = myFeatures.Add("SimMassScaling")
                |      
                | 
                |     Given a SimFeatures object myFeatures, you can retrieve a SimMassScaling
                |     named "Mass Scaling.1" as following:
                | 
                |      ...
                |      myMassScaling = myFeatures.Item("Mass Scaling.1")
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
    def factor(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Factor() As double
                |     Returns or sets the scaling factor value. Quantity: DIMENSIONLESS, units:
                |     None

        :return: float
        """

        return self.com_object.Factor

    @factor.setter
    def factor(self, value: float):
        """
        :param float value:
        """

        self.com_object.Factor = value

    @property
    def factor_flag(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property FactorFlag() As boolean
                |     Returns or sets the flag that determines if the scaling factor is
                |     specified.
                |     TRUE: the scaling factor is specified.
                |     FALSE: the scaling factor is not specified.

        :return: bool
        """

        return self.com_object.FactorFlag

    @factor_flag.setter
    def factor_flag(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.FactorFlag = value

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
    def frequency(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Frequency() As long
                |     Returns or sets the frequency value. Quantity: Integer, units: None

        :return: int
        """

        return self.com_object.Frequency

    @frequency.setter
    def frequency(self, value: int):
        """
        :param int value:
        """

        self.com_object.Frequency = value

    @property
    def frequency_flag(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property FrequencyFlag() As boolean
                |     Returns or sets the flag that determines if the Mass Scaling Timing Mode is
                |     Frequency.
                |     TRUE: the Mass Scaling Timing Mode is Frequency.
                |     FALSE: the Mass Scaling Timing Mode is Number interval.

        :return: bool
        """

        return self.com_object.FrequencyFlag

    @frequency_flag.setter
    def frequency_flag(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.FrequencyFlag = value

    @property
    def mass_scaling_behavior(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property MassScalingBehavior() As
                | SimMassScalingMassScalingBehavior
                |     Returns or sets the mass scaling action.

        :return: SimMassScalingMassScalingBehavior
        """

        return self.com_object.MassScalingBehavior

    @mass_scaling_behavior.setter
    def mass_scaling_behavior(self, value: int):
        """
        :param int value:
        """

        self.com_object.MassScalingBehavior = value

    @property
    def mass_scaling_method(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property MassScalingMethod() As
                | SimMassScalingMassScalingMethod
                |     Returns or sets the mass scaling type value.

        :return: SimMassScalingMassScalingMethod
        """

        return self.com_object.MassScalingMethod

    @mass_scaling_method.setter
    def mass_scaling_method(self, value: int):
        """
        :param int value:
        """

        self.com_object.MassScalingMethod = value

    @property
    def number_interval(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property NumberInterval() As long
                |     Returns or sets the the number interval value. Quantity: Integer, units:
                |     None

        :return: int
        """

        return self.com_object.NumberInterval

    @number_interval.setter
    def number_interval(self, value: int):
        """
        :param int value:
        """

        self.com_object.NumberInterval = value

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
    def target_time_increment(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property TargetTimeIncrement() As double
                |     Returns or sets the target time increment value. Quantity: TIME, units: s

        :return: float
        """

        return self.com_object.TargetTimeIncrement

    @target_time_increment.setter
    def target_time_increment(self, value: float):
        """
        :param float value:
        """

        self.com_object.TargetTimeIncrement = value

    @property
    def target_time_increment_flag(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property TargetTimeIncrementFlag() As boolean
                |     Returns or sets the flag that determines if the target time increment is
                |     specified.
                |     TRUE: the target time increment is specified.
                |     FALSE: the target time increment is not specified. 

        :return: bool
        """

        return self.com_object.TargetTimeIncrementFlag

    @target_time_increment_flag.setter
    def target_time_increment_flag(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.TargetTimeIncrementFlag = value

    def __repr__(self):
        return f'SimMassScaling(name="{ self.name }")'
