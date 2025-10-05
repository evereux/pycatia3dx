"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.sma_mpa_base.sim_axis_system import SimAxisSystem
from pycatia3dx.system.any_object import AnyObject


class SimInitialRotationVelocity(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimInitialRotationVelocity
                | 
                | Represents the Initial Rotation Velocity object.
                | 
                | Example:
                |     Given a SimFeatures object, you can create a SimInitialRotationVelocity as
                |     following:
                | 
                |      Dim MyFeatures As SimFeatures
                |      ...
                |      Dim MyInitialRotationVelocity As
                |      SimInitialRotationVelocity
                |      Set MyInitialRotationVelocity = MyFeatures.Add("SimInitialRotationVelocity")
                |      
                | 
                |     Given a SimFeatures object, you can retrieve a SimInitialRotationVelocity
                |     named "Initial Rotation Velocity.1" as following:
                | 
                |      Dim MyFeatures As SimFeatures
                |      ...
                |      Dim MyInitialRotationVelocity As
                |      SimInitialRotationVelocity
                |      Set MyInitialRotationVelocity = MyFeatures.Item("Initial Rotation Velocity.1")
                |      
                | 
                | Example in Python:
                |     Given a SimFeatures object myFeatures, you can create a
                |     SimInitialRotationVelocity as following:
                | 
                |      ...
                |      myInitialRotationVelocity = myFeatures.Add("SimInitialRotationVelocity")
                |      
                | 
                |     Given a SimFeatures object myFeatures, you can retrieve a
                |     SimInitialRotationVelocity named "Initial Rotation Velocity.1" as
                |     following:
                | 
                |      ...
                |      myInitialRotationVelocity = myFeatures.Item("Initial Rotation Velocity.1")
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
                |     Returns or sets the degree of freedom on which the rotation is applied.

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
    def rotational_velocity(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property RotationalVelocity() As double
                |     Rotational velocity of the applied rotation velocity. Quantity:
                |     ANGULAR_VELOCITY, units: turn_mn

        :return: float
        """

        return self.com_object.RotationalVelocity

    @rotational_velocity.setter
    def rotational_velocity(self, value: float):
        """
        :param float value:
        """

        self.com_object.RotationalVelocity = value

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
        return f'SimInitialRotationVelocity(name="{ self.name }")'
