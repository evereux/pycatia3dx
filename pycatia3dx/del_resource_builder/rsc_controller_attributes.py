"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class RscControllerAttributes(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     RscControllerAttributes
                | 
                | Interface to access the controller attributes.
                | Role: This interface provides methods to access the controller
                | parameters.
                | This API retrieves the default attributes of the controller. There are used
                | before any simulation and must be modified before the simulation
                | starts.
                | 
                | Example:
                |     Let assume there is a robot opened as a root entity in a given
                |     editor.
                | 
                |      Dim MainResource As Variant
                |      Set MainResource = CATIA.ActiveEditor.ActiveObject
                | 
                |      Dim MySelectedResource As RscControllerAttributesAccess
                |      Set MySelectedResource = MainResource.GetItem("CAARscControllerAttributesAccess")
                |      
                |      If Not MySelectedResource Is Nothing Then
                |        Dim MyControllerData As RscControllerAttributes
                |        MyControllerData = MySelectedResource.RetrieveControllerAttributesObject
                |      End If
                | 
                | See also:
                |     RscControllerAttributesAccess
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def acceleration_mode(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property AccelerationMode() As long
                |     Indicates the accelration scaling mode mode.
                | 
                |         0: variable acceleration time
                |         1: constant acceleration time
                | 
                |     Example:
                | 
                |      Dim MyMode As Integer
                |      MyMode = MyControllerData.AccelerationMode

        :return: int
        """

        return self.com_object.AccelerationMode

    @acceleration_mode.setter
    def acceleration_mode(self, value: int):
        """
        :param int value:
        """

        self.com_object.AccelerationMode = value

    @property
    def acceleration_scaling(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property AccelerationScaling() As long
                |     Indicates the accelration scaling mode mode.
                | 
                |         0: variable time
                |         1: constant time
                | 
                |     Example:
                | 
                |      Dim MyMode As Integer
                |      MyMode = MyControllerData.AccelerationScaling

        :return: int
        """

        return self.com_object.AccelerationScaling

    @acceleration_scaling.setter
    def acceleration_scaling(self, value: int):
        """
        :param int value:
        """

        self.com_object.AccelerationScaling = value

    @property
    def controller_type(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ControllerType() As CATBSTR
                |     Indicates the controller type.
                | 
                |     Example:
                | 
                |      Dim MyControllerType As String
                |      MyControllerType = MyControllerData.ControllerType

        :return: str
        """

        return self.com_object.ControllerType

    @controller_type.setter
    def controller_type(self, value: str):
        """
        :param str value:
        """

        self.com_object.ControllerType = value

    @property
    def heart_beat(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property HeartBeat() As double
                |     Indicates the resource sampling rate.
                | 
                |     Example:
                | 
                |      Dim MyValue As Double
                |      MyValue = MyControllerData.HeartBeat

        :return: float
        """

        return self.com_object.HeartBeat

    @heart_beat.setter
    def heart_beat(self, value: float):
        """
        :param float value:
        """

        self.com_object.HeartBeat = value

    @property
    def joint_interpolation_mode(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property JointInterpolationMode() As long
                |     Indicates the joint interpolation mode.
                | 
                |         0: shortest angle
                |         1: solution angle
                |         2: turn numbers
                |         3: absolute shortest angle
                |         4: turn signs
                | 
                |     Example:
                | 
                |      Dim MyMode As Integer
                |      MyMode = MyControllerData.JointInterpolationMode

        :return: int
        """

        return self.com_object.JointInterpolationMode

    @joint_interpolation_mode.setter
    def joint_interpolation_mode(self, value: int):
        """
        :param int value:
        """

        self.com_object.JointInterpolationMode = value

    @property
    def response_delay(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ResponseDelay() As double
                |     Indicates the resource response delay.
                | 
                |     Example:
                | 
                |      Dim MyValue As Double
                |      MyValue = MyControllerData.ResponseDelay

        :return: float
        """

        return self.com_object.ResponseDelay

    @response_delay.setter
    def response_delay(self, value: float):
        """
        :param float value:
        """

        self.com_object.ResponseDelay = value

    @property
    def settle_time(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property SettleTime() As double
                |     Indicates the resource settle time.
                | 
                |     Example:
                | 
                |      Dim MyValue As Double
                |      MyValue = MyControllerData.SettleTime

        :return: float
        """

        return self.com_object.SettleTime

    @settle_time.setter
    def settle_time(self, value: float):
        """
        :param float value:
        """

        self.com_object.SettleTime = value

    @property
    def singularity_tolerance(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property SingularityTolerance() As double
                |     Indicates the singularity tolerance. A 0 value will deactivate the
                |     singularity check.
                | 
                |     Example:
                | 
                |      Dim MyValue As Double
                |      MyValue = MyControllerData.SingularityTolerance

        :return: float
        """

        return self.com_object.SingularityTolerance

    @singularity_tolerance.setter
    def singularity_tolerance(self, value: float):
        """
        :param float value:
        """

        self.com_object.SingularityTolerance = value

    @property
    def time_based_motion(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property TimeBasedMotion() As long
                |     Indicates the time based motion mode.
                | 
                |         0: exact
                |         1: constrained
                | 
                |     Example:
                | 
                |      Dim MyMode As Integer
                |      MyMode = MyControllerData.TimeBasedMotion

        :return: int
        """

        return self.com_object.TimeBasedMotion

    @time_based_motion.setter
    def time_based_motion(self, value: int):
        """
        :param int value:
        """

        self.com_object.TimeBasedMotion = value

    def __repr__(self):
        return f'RscControllerAttributes(name="{ self.name }")'
