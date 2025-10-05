"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.sma_mpa_foundation.sim_feature_history import SimFeatureHistory
from pycatia3dx.system.any_object import AnyObject


class SimBoltTorque(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimBoltTorque
                | 
                | Represents the Bolt Torque object.
                | 
                | Example:
                |     Given a SimFeatures object, you can create a SimBoltTorque as
                |     following:
                | 
                |      Dim MyFeatures As SimFeatures
                |      ...
                |      Dim MyBoltTorque As SimBoltTorque
                |      Set MyBoltTorque = MyFeatures.Add("SimBoltTorque")
                |      
                | 
                |     Given a SimFeatures object, you can retrieve a SimBoltTorque named "Bolt
                |     Torque.1" as following:
                | 
                |      Dim MyFeatures As SimFeatures
                |      ...
                |      Dim MyBoltTorque As SimBoltTorque
                |      Set MyBoltTorque = MyFeatures.Item("Bolt Torque.1")
                |      
                | 
                | Example in Python:
                |     Given a SimFeatures object myFeatures, you can create a SimBoltTorque as
                |     following:
                | 
                |      ...
                |      myBoltTorque = myFeatures.Add("SimBoltTorque")
                |      
                | 
                |     Given a SimFeatures object myFeatures, you can retrieve a SimBoltTorque
                |     named "Bolt Torque.1" as following:
                | 
                |      ...
                |      myBoltTorque = myFeatures.Item("Bolt Torque.1")
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
    def magnitude(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Magnitude() As double
                |     Returns or sets the magnitude. Quantity: TORQUE, units: N_m

        :return: float
        """

        return self.com_object.Magnitude

    @magnitude.setter
    def magnitude(self, value: float):
        """
        :param float value:
        """

        self.com_object.Magnitude = value

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
    def torque_coefficient(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property TorqueCoefficient() As double
                |     Returns or sets the torque coefficient. Quantity: DIMENSIONLESS, units:
                |     None 

        :return: float
        """

        return self.com_object.TorqueCoefficient

    @torque_coefficient.setter
    def torque_coefficient(self, value: float):
        """
        :param float value:
        """

        self.com_object.TorqueCoefficient = value

    def __repr__(self):
        return f'SimBoltTorque(name="{ self.name }")'
