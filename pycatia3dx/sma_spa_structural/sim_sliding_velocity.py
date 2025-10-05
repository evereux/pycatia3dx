"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.sma_mpa_base.sim_axis import SimAxis
from pycatia3dx.sma_mpa_base.sim_axis_system import SimAxisSystem
from pycatia3dx.sma_mpa_foundation.sim_feature_history import SimFeatureHistory
from pycatia3dx.system.any_object import AnyObject


class SimSlidingVelocity(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimSlidingVelocity
                | 
                | Represents the Sliding Velocity object.
                | 
                | Example:
                |     Given a SimFeatures object, you can create a SimSlidingVelocity as
                |     following:
                | 
                |      Dim MyFeatures As SimFeatures
                |      ...
                |      Dim MySlidingVelocity As SimSlidingVelocity
                |      Set MySlidingVelocity = MyFeatures.Add("SimSlidingVelocity")
                |      
                | 
                |     Given a SimFeatures object, you can retrieve a SimSlidingVelocity named
                |     "Sliding Velocity.1" as following:
                | 
                |      Dim MyFeatures As SimFeatures
                |      ...
                |      Dim MySlidingVelocity As SimSlidingVelocity
                |      Set MySlidingVelocity = MyFeatures.Item("Sliding Velocity.1")
                |      
                | 
                | Example in Python:
                |     Given a SimFeatures object myFeatures, you can create a SimSlidingVelocity
                |     as following:
                | 
                |      ...
                |      mySlidingVelocity = myFeatures.Add("SimSlidingVelocity")
                |      
                | 
                |     Given a SimFeatures object myFeatures, you can retrieve a
                |     SimSlidingVelocity named "Sliding Velocity.1" as
                |     following:
                | 
                |      ...
                |      mySlidingVelocity = myFeatures.Item("Sliding Velocity.1")
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
    def angular_velocity(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property AngularVelocity() As double
                |     Returns or sets the value of rotational sliding velocity.

        :return: float
        """

        return self.com_object.AngularVelocity

    @angular_velocity.setter
    def angular_velocity(self, value: float):
        """
        :param float value:
        """

        self.com_object.AngularVelocity = value

    @property
    def axis_system(self) -> SimAxisSystem:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property AxisSystem() As SimAxisSystem (Read Only)
                |     Returns the local axis system.

        :return: SimAxisSystem
        """

        return SimAxisSystem(self.com_object.AxisSystem)

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
    def line(self) -> SimAxis:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Line() As SimAxis (Read Only)
                |     Returns the axis of rotation.

        :return: SimAxis
        """

        return SimAxis(self.com_object.Line)

    @property
    def translational_dof(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property TranslationalDof() As
                | SimSlidingVelocityTranslationalDof
                |     Returns or sets the type of translational DOF.

        :return: SimSlidingVelocityTranslationalDof
        """

        return self.com_object.TranslationalDof

    @translational_dof.setter
    def translational_dof(self, value: int):
        """
        :param int value:
        """

        self.com_object.TranslationalDof = value

    @property
    def translational_velocity(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property TranslationalVelocity() As double
                |     Returns or sets the value of translational sliding velocity.

        :return: float
        """

        return self.com_object.TranslationalVelocity

    @translational_velocity.setter
    def translational_velocity(self, value: float):
        """
        :param float value:
        """

        self.com_object.TranslationalVelocity = value

    @property
    def type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Type() As SimSlidingVelocityType
                |     Returns or sets the type of sliding velocity. 
                | 
                | Copyright © 1999-2024, Dassault Systèmes. All rights reserved.

        :return: SimSlidingVelocityType
        """

        return self.com_object.Type

    @type.setter
    def type(self, value: int):
        """
        :param int value:
        """

        self.com_object.Type = value

    def __repr__(self):
        return f'SimSlidingVelocity(name="{ self.name }")'
