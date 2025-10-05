"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.sma_mpa_foundation.sim_feature_history import SimFeatureHistory
from pycatia3dx.system.any_object import AnyObject


class SimVelocityBaseMotion(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimVelocityBaseMotion
                | 
                | Represents the Velocity Base Motion object.
                | 
                | Example:
                |     Given a SimFeatures object, you can create a SimVelocityBaseMotion as
                |     following:
                | 
                |      Dim MyFeatures As SimFeatures
                |      ...
                |      Dim MyVelocityBaseMotion As SimVelocityBaseMotion
                |      Set MyVelocityBaseMotion = MyFeatures.Add("SimVelocityBaseMotion")
                |      
                | 
                |     Given a SimFeatures object, you can retrieve a SimVelocityBaseMotion named
                |     "Velocity Base Motion.1" as following:
                | 
                |      Dim MyFeatures As SimFeatures
                |      ...
                |      Dim MyVelocityBaseMotion As SimVelocityBaseMotion
                |      Set MyVelocityBaseMotion = MyFeatures.Item("Velocity Base Motion.1")
                |      
                | 
                | Example in Python:
                |     Given a SimFeatures object myFeatures, you can create a
                |     SimVelocityBaseMotion as following:
                | 
                |      ...
                |      myVelocityBaseMotion = myFeatures.Add("SimVelocityBaseMotion")
                |      
                | 
                |     Given a SimFeatures object myFeatures, you can retrieve a
                |     SimVelocityBaseMotion named "Velocity Base Motion.1" as
                |     following:
                | 
                |      ...
                |      myVelocityBaseMotion = myFeatures.Item("Velocity Base Motion.1")
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
    def dof(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Dof() As SimDof
                |     Returns or sets the degree of freedom on which the base motion is applied.

        :return: int
        """

        return self.com_object.Dof

    @dof.setter
    def dof(self, value: int):
        """
        :param int value:
        """

        self.com_object.Dof = value

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
                |     Returns or sets the magnitude value. If the base motion is a displacement base motion then the unit is : Quantity: LENGTH, units: m.
                |     If the base motion is a velocity base motion then the unit is : Quantity: SPEED, units: m_s1.
                |     If the base motion is an acceleration base motion then the unit is : Quantity: ACCELRTN, units: m_s2.

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

    def __repr__(self):
        return f'SimVelocityBaseMotion(name="{ self.name }")'
