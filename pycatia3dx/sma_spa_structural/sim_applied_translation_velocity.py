"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.sma_mpa_base.sim_axis_system import SimAxisSystem
from pycatia3dx.sma_mpa_foundation.sim_feature_history import SimFeatureHistory
from pycatia3dx.system.any_object import AnyObject


class SimAppliedTranslationVelocity(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimAppliedTranslationVelocity
                | 
                | Represents the Applied Translation Velocity object.
                | 
                | Example:
                |     Given a SimFeatures object, you can create a SimAppliedTranslationVelocity
                |     as following:
                | 
                |      Dim MyFeatures As SimFeatures
                |      ...
                |      Dim MyAppliedTranslationVelocity As
                |      SimAppliedTranslationVelocity
                |      Set MyAppliedTranslationVelocity = MyFeatures.Add("SimAppliedTranslationVelocity")
                |      
                | 
                |     Given a SimFeatures object, you can retrieve a
                |     SimAppliedTranslationVelocity named "Applied Translation Velocity.1" as
                |     following:
                | 
                |      Dim MyFeatures As SimFeatures
                |      ...
                |      Dim MyAppliedTranslationVelocity As
                |      SimAppliedTranslationVelocity
                |      Set MyAppliedTranslationVelocity = MyFeatures.Item("Applied Translation Velocity.1")
                |      
                | 
                | Example in Python:
                |     Given a SimFeatures object myFeatures, you can create a
                |     SimAppliedTranslationVelocity as following:
                | 
                |      ...
                |      myAppliedTranslationVelocity = myFeatures.Add("SimAppliedTranslationVelocity")
                |      
                | 
                |     Given a SimFeatures object myFeatures, you can retrieve a
                |     SimAppliedTranslationVelocity named "Applied Translation Velocity.1" as
                |     following:
                | 
                |      ...
                |      myAppliedTranslationVelocity = myFeatures.Item("Applied Translation Velocity.1")
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
    def axis_system(self) -> SimAxisSystem:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property AxisSystem() As SimAxisSystem (Read Only)
                |     Returns the axis system.

        :return: SimAxisSystem
        """

        return SimAxisSystem(self.com_object.AxisSystem)

    @property
    def dof(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Dof() As SimDof
                |     Returns or sets the degree of freedom on which the translation is applied.

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
    def translational_velocity(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property TranslationalVelocity() As double
                |     Translational velocity of the applied translation velocity. Quantity:
                |     SPEED, units: m_s1 

        :return: float
        """

        return self.com_object.TranslationalVelocity

    @translational_velocity.setter
    def translational_velocity(self, value: float):
        """
        :param float value:
        """

        self.com_object.TranslationalVelocity = value

    def __repr__(self):
        return f'SimAppliedTranslationVelocity(name="{ self.name }")'
