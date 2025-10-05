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


class SimBearingLoad(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimBearingLoad
                | 
                | Represents the Bearing Load object.
                | 
                | Example:
                |     Given a SimFeatures object, you can create a SimBearingLoad as
                |     following:
                | 
                |      Dim MyFeatures As SimFeatures
                |      ...
                |      Dim MyBearingLoad As SimBearingLoad
                |      Set MyBearingLoad = MyFeatures.Add("SimBearingLoad")
                |      
                | 
                |     Given a SimFeatures object, you can retrieve a SimBearingLoad named
                |     "Bearing Load.1" as following:
                | 
                |      Dim MyFeatures As SimFeatures
                |      ...
                |      Dim MyBearingLoad As SimBearingLoad
                |      Set MyBearingLoad = MyFeatures.Item("Bearing Load.1")
                |      
                | 
                | Example in Python:
                |     Given a SimFeatures object myFeatures, you can create a SimBearingLoad as
                |     following:
                | 
                |      ...
                |      myBearingLoad = myFeatures.Add("SimBearingLoad")
                |      
                | 
                |     Given a SimFeatures object myFeatures, you can retrieve a SimBearingLoad
                |     named "Bearing Load.1" as following:
                | 
                |      ...
                |      myBearingLoad = myFeatures.Item("Bearing Load.1")
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
    def angle(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Angle() As double
                |     Angle of the bearing load. Quantity: ANGLE, units: deg

        :return: float
        """

        return self.com_object.Angle

    @angle.setter
    def angle(self, value: float):
        """
        :param float value:
        """

        self.com_object.Angle = value

    @property
    def axis_system(self) -> SimAxisSystem:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property AxisSystem() As SimAxisSystem (Read Only)
                |     Returns the axis system used for the bearing load.

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
    def interaction_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property InteractionType() As SimBearingLoadInteractionType
                |     Interaction type of the bearing load.

        :return: int
        """

        return self.com_object.InteractionType

    @interaction_type.setter
    def interaction_type(self, value: int):
        """
        :param int value:
        """

        self.com_object.InteractionType = value

    @property
    def orientation_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property OrientationType() As SimBearingLoadOrientationType
                |     Orientation type of the bearing load.

        :return: int
        """

        return self.com_object.OrientationType

    @orientation_type.setter
    def orientation_type(self, value: int):
        """
        :param int value:
        """

        self.com_object.OrientationType = value

    @property
    def profile_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ProfileType() As SimBearingLoadProfileType
                |     Profile type of the bearing load.

        :return: int
        """

        return self.com_object.ProfileType

    @profile_type.setter
    def profile_type(self, value: int):
        """
        :param int value:
        """

        self.com_object.ProfileType = value

    @property
    def x_magnitude(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property XMagnitude() As double
                |     X component of the bearing load. Quantity: FORCE, units: N

        :return: float
        """

        return self.com_object.XMagnitude

    @x_magnitude.setter
    def x_magnitude(self, value: float):
        """
        :param float value:
        """

        self.com_object.XMagnitude = value

    @property
    def y_magnitude(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property YMagnitude() As double
                |     Y component of the bearing load. Quantity: FORCE, units: N

        :return: float
        """

        return self.com_object.YMagnitude

    @y_magnitude.setter
    def y_magnitude(self, value: float):
        """
        :param float value:
        """

        self.com_object.YMagnitude = value

    def __repr__(self):
        return f'SimBearingLoad(name="{ self.name }")'
