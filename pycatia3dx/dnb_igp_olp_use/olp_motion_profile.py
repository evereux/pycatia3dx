"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.dnb_igp_olp_use.olp_profile import OLPProfile


class OLPMotionProfile(OLPProfile):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     DNBIgpOlpUseItf.OlpProfile
                |                         OlpMotionProfile
                | 
                | A motion profile used for translating a robot program.
                | 
                | This interface can only be used by a translator within the Robotics Off-line
                | Programming (OLP) Download or Upload command.
                | 
                | The behavior of this object depends on where it was retrieved from. If the
                | object was retrieved from an OlpRobotMotion or OlpRobotMotionTarget then this
                | object is used to configure the speed properties of that motion. The parameters
                | specified with the iMatch input equal to TRUE will be used to find an existing
                | profile to reuse for this motion. If no matching profile is found a new one
                | will be created. If the object was retrieved from
                | OlpController.MotionProfileList then any modifications to this object will
                | change an existing or new profile's values directly.
                | 
                | There are 2 types of methods on this object. Some methods provide direct access
                | to the motion profile parameters as available in the dialog. Other methods,
                | called Template Methods, get and set all the speed/acceleration parameters as a
                | group. Each template assumes there are fixed values for some of the parameters.
                | The get template methods generate messages if the parameters which would have
                | fixed values are not correct. The set template methods set all the fixed values
                | in addition to the input arguments.
                | 
                | You cannot call methods which Get values for the incorrect Basis. For example,
                | if IsTimeBasis returns FALSE, then GetTime will fail. You should also not call
                | a template method like GetTCPAngular if TimeLinearAngularBasis returned
                | delOlpLinearBasis.
                | 
                | You cannot call Get methods for profiles retrieved from a new OlpRobotMotion or
                | OlpRobotMotionTarget until values have been set.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def get_joint_as_percent(self, o_speed_percent: float, o_accel_percent: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetJointAsPercent(double oSpeedPercent,double
                | oAccelPercent)
                |     Template Method: Get the joint speed and acceleration as a
                |     percentage.
                |     Joint speed/acceleration is equal to the linear TCP speed/acceleration. The
                |     following rules are checked for other parameters of the motion
                |     profile.
                | 
                |         Linear Speed and Acceleration are specified as a percentage. (Notice
                |         message posted if specified in absolute units)
                |         Linear Acceleration is equal to Linear Deceleration. (Warning message
                |         posted if different)
                |         Angular Speed, Angular Acceleration, Angular Deceleration are all 100%
                |         or device maximum (Warning message posted if
                |         different)
                |         Basis is Speed/Acceleration (Error if different). You should check
                |         IsTimeBasis before calling this method.
                | 
                |     Parameters:
                | 
                |         oSpeedPercent
                |             Joint speed as a percentage (1.0 is 100%). 
                |         oAccelPercent
                |             Joint acceleration as a percentage (1.0 is 100%).

        :param float o_speed_percent:
        :param float o_accel_percent:
        :return: None
        """
        return self.com_object.GetJointAsPercent(o_speed_percent, o_accel_percent)

    def get_joint_as_percent_with_decel(self, o_speed_percent: float, o_accel_percent: float, o_decel_percent: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetJointAsPercentWithDecel(double oSpeedPercent,double oAccelPercent,double
                | oDecelPercent)
                |     Template Method: Get the joint speed, acceleration and deceleration as a
                |     percentage.
                |     Joint speed/acceleration is equal to the linear TCP speed/acceleration. The
                |     following rules are checked for other parameters of the motion
                |     profile.
                | 
                |         Linear Speed and Acceleration are specified as a percentage. (Notice
                |         message posted if specified in absolute units)
                |         Angular Speed, Angular Acceleration, Angular Deceleration are all 100%
                |         or device maximum (Warning message posted if
                |         different)
                |         Basis is Speed/Acceleration (Error if different). You should check
                |         IsTimeBasis before calling this method.
                | 
                |     Parameters:
                | 
                |         oSpeed
                |             Joint speed as a percentage (1.0 is 100%). 
                |         oAccel
                |             Joint acceleration as a percentage (1.0 is 100%). 
                |         oDecel
                |             Joint deceleration as a percentage (1.0 is 100%).

        :param float o_speed_percent:
        :param float o_accel_percent:
        :param float o_decel_percent:
        :return: None
        """
        return self.com_object.GetJointAsPercentWithDecel(o_speed_percent, o_accel_percent, o_decel_percent)

    def get_tcp_accel_angular(self, i_units: int) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetTCPAccelAngular(DELOlpMotionProfileUnits iUnits) As
                | double
                |     Get TCP angular acceleration.
                |     This fails if IsTimeBasis returns TRUE.
                | 
                |     Parameters:
                | 
                |         iUnits
                |             The units to get the value in. 1.0 is 100% if Percent is specified.
                |             Value is in rad/s^2 if Absolute is specified. 
                | 
                |     Returns:
                |         The acceleration in the specified units, converted if needed, but no
                |         messages are reported.

        :param int i_units:
        :return: float
        """
        return self.com_object.GetTCPAccelAngular(i_units)

    def get_tcp_accel_linear(self, i_units: int) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetTCPAccelLinear(DELOlpMotionProfileUnits iUnits) As
                | double
                |     Get TCP linear acceleration.
                |     This fails if IsTimeBasis returns TRUE.
                | 
                |     Parameters:
                | 
                |         iUnits
                |             The units to get the value in. 1.0 is 100% if Percent is specified.
                |             Value is in m/s^2 if Absolute is specified. 
                | 
                |     Returns:
                |         The acceleration in the specified units, converted if needed, but no
                |         messages are reported.

        :param int i_units:
        :return: float
        """
        return self.com_object.GetTCPAccelLinear(i_units)

    def get_tcp_angular(self, o_tcp_speed_abs: float, o_tcp_accel_percent: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetTCPAngular(double oTCPSpeedAbs,double oTCPAccelPercent)
                |     Template Method: Get the TCP angular speed and
                |     acceleration.
                |     The following rules are checked for other parameters of the motion
                |     profile.
                | 
                |         Angular Speed is specified in absolute units. (Notice message posted if
                |         specified as a percentage)
                |         Angular Acceleration is specified as a percentage. (Notice message
                |         posted if specified in absolute units)
                |         Angular Acceleration is equal to Angular Deceleration. (Warning message
                |         posted if different)
                |         Linear Speed, Linear Acceleration, Linear Deceleration are all 100% or
                |         device maximum (Warning message posted if different)
                |         Basis is Speed/Acceleration (Error if different). You should check
                |         IsTimeBasis before calling this method.
                | 
                |     Parameters:
                | 
                |         oTCPSpeedAbs
                |             Angular TCP speed in absolute units (rad/s). 
                |         oTCPAccelPercent
                |             Angular TCP acceleration as a percentage (1.0 is 100%).

        :param float o_tcp_speed_abs:
        :param float o_tcp_accel_percent:
        :return: None
        """
        return self.com_object.GetTCPAngular(o_tcp_speed_abs, o_tcp_accel_percent)

    def get_tcp_angular_with_decel(self, o_tcp_speed_abs: float, o_tcp_accel_percent: float, o_tcp_decel_percent: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetTCPAngularWithDecel(double oTCPSpeedAbs,double oTCPAccelPercent,double
                | oTCPDecelPercent)
                |     Template Method: Get the TCP angular speed, acceleration and
                |     deceleration.
                |     The following rules are checked for other parameters of the motion
                |     profile.
                | 
                |         Angular Speed is specified in absolute units. (Notice message posted if
                |         specified as a percentage)
                |         Angular Acceleration is specified as a percentage. (Notice message
                |         posted if specified in absolute units)
                |         Linear Speed, Linear Acceleration, Linear Deceleration are all 100% or
                |         device maximum (Warning message posted if different)
                |         Basis is Speed/Acceleration (Error if different). You should check
                |         IsTimeBasis before calling this method.
                | 
                |     Parameters:
                | 
                |         oTCPSpeedAbs
                |             Angular TCP speed in absolute units (rad/s). 
                |         oTCPAccelPercent
                |             Angular TCP acceleration as a percentage (1.0 is 100%).
                |             
                |         oTCPDecelPercent
                |             Angular TCP deceleration as a percentage (1.0 is 100%).

        :param float o_tcp_speed_abs:
        :param float o_tcp_accel_percent:
        :param float o_tcp_decel_percent:
        :return: None
        """
        return self.com_object.GetTCPAngularWithDecel(o_tcp_speed_abs, o_tcp_accel_percent, o_tcp_decel_percent)

    def get_tcp_decel_angular(self, i_units: int) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetTCPDecelAngular(DELOlpMotionProfileUnits iUnits) As
                | double
                |     Get TCP angular deceleration.
                |     This fails if IsTimeBasis returns TRUE.
                | 
                |     Parameters:
                | 
                |         iUnits
                |             The units to get the value in. 1.0 is 100% if Percent is specified.
                |             Value is in rad/s^2 if Absolute is specified. 
                | 
                |     Returns:
                |         The deceleration in the specified units, converted if needed, but no
                |         messages are reported.

        :param int i_units:
        :return: float
        """
        return self.com_object.GetTCPDecelAngular(i_units)

    def get_tcp_decel_linear(self, i_units: int) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetTCPDecelLinear(DELOlpMotionProfileUnits iUnits) As
                | double
                |     Get TCP linear deceleration.
                |     This fails if IsTimeBasis returns TRUE.
                | 
                |     Parameters:
                | 
                |         iUnits
                |             The units to get the value in. 1.0 is 100% if Percent is specified.
                |             Value is in m/s^2 if Absolute is specified. 
                | 
                |     Returns:
                |         The deceleration in the specified units, converted if needed, but no
                |         messages are reported.

        :param int i_units:
        :return: float
        """
        return self.com_object.GetTCPDecelLinear(i_units)

    def get_tcp_linear(self, o_tcp_speed_abs: float, o_tcp_accel_percent: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetTCPLinear(double oTCPSpeedAbs,double oTCPAccelPercent)
                |     Template Method: Get the TCP linear speed and
                |     acceleration.
                |     The following rules are checked for other parameters of the motion
                |     profile.
                | 
                |         Linear Speed is specified in absolute units. (Notice message posted if
                |         specified as a percentage)
                |         Linear Acceleration is specified as a percentage. (Notice message
                |         posted if specified in absolute units)
                |         Linear Acceleration is equal to Linear Deceleration. (Warning message
                |         posted if different)
                |         Angular Speed, Angular Acceleration, Angular Deceleration are all 100%
                |         or device maximum (Warning message posted if
                |         different)
                |         Basis is Speed/Acceleration (Error if different). You should check
                |         IsTimeBasis before calling this method.
                | 
                |     Parameters:
                | 
                |         oTCPSpeedAbs
                |             Linear TCP speed in absolute units (m/s). 
                |         oTCPAccelPercent
                |             Linear TCP acceleration as a percentage (1.0 is 100%).

        :param float o_tcp_speed_abs:
        :param float o_tcp_accel_percent:
        :return: None
        """
        return self.com_object.GetTCPLinear(o_tcp_speed_abs, o_tcp_accel_percent)

    def get_tcp_linear_no_accel(self, o_tcp_speed_abs: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetTCPLinearNoAccel(double oTCPSpeedAbs)
                |     Template Method: Get the TCP linear speed.
                |     The following rules are checked for other parameters of the motion
                |     profile.
                | 
                |         Linear Speed is specified in absolute units. (Notice message posted if
                |         specified as a percentage)
                |         Linear Acceleration, Linear Deceleration, Angular Speed, Angular
                |         Acceleration, and Angular Deceleration are all 100% or device maximum (Warning
                |         message posted if different)
                |         Basis is Speed/Acceleration (Error if different). You should check
                |         IsTimeBasis before calling this method.
                | 
                |     Parameters:
                | 
                |         oTCPSpeedAbs
                |             Linear TCP speed in absolute units (m/s).

        :param float o_tcp_speed_abs:
        :return: None
        """
        return self.com_object.GetTCPLinearNoAccel(o_tcp_speed_abs)

    def get_tcp_linear_no_accel_with_units(self, o_tcp_speed: float, o_units: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetTCPLinearNoAccelWithUnits(double oTCPSpeed,DELOlpMotionProfileUnits
                | oUnits)
                |     Template Method: Get the TCP linear speed and the units it is specified
                |     in.
                |     The following rules are checked for other parameters of the motion
                |     profile.
                | 
                |         Linear Acceleration, Linear Deceleration, Angular Speed, Angular
                |         Acceleration, and Angular Deceleration are all 100% or device maximum (Warning
                |         message posted if different)
                |         Basis is Speed/Acceleration (Error if different). You should check
                |         IsTimeBasis before calling this method.
                | 
                |     Parameters:
                | 
                |         oTCPSpeed
                |             Linear TCP speed either as percentage or in absolute units.
                |             
                |         oUnits
                |             Indicates if the speed is in percent (1.0 is 100%) or in absolute
                |             units (m/s).

        :param float o_tcp_speed:
        :param int o_units:
        :return: None
        """
        return self.com_object.GetTCPLinearNoAccelWithUnits(o_tcp_speed, o_units)

    def get_tcp_linear_with_decel(self, o_tcp_speed_abs: float, o_tcp_accel_percent: float, o_tcp_decel_percent: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetTCPLinearWithDecel(double oTCPSpeedAbs,double oTCPAccelPercent,double
                | oTCPDecelPercent)
                |     Template Method: Get the TCP linear speed, acceleration and
                |     deceleration.
                |     The following rules are checked for other parameters of the motion
                |     profile.
                | 
                |         Linear Speed is specified in absolute units. (Notice message posted if
                |         specified as a percentage)
                |         Linear Acceleration is specified as a percentage. (Notice message
                |         posted if specified in absolute units)
                |         Angular Speed, Angular Acceleration, Angular Deceleration are all 100%
                |         or device maximum (Warning message posted if
                |         different)
                |         Basis is Speed/Acceleration (Error if different). You should check
                |         IsTimeBasis before calling this method.
                | 
                |     Parameters:
                | 
                |         oTCPSpeedAbs
                |             Linear TCP speed in absolute units (m/s). 
                |         oTCPAccelPercent
                |             Linear TCP acceleration as a percentage (1.0 is 100%).
                |             
                |         oTCPDecelPercent
                |             Linear TCP deceleration as a percentage (1.0 is 100%).

        :param float o_tcp_speed_abs:
        :param float o_tcp_accel_percent:
        :param float o_tcp_decel_percent:
        :return: None
        """
        return self.com_object.GetTCPLinearWithDecel(o_tcp_speed_abs, o_tcp_accel_percent, o_tcp_decel_percent)

    def get_tcp_linear_with_units(self, o_tcp_speed: float, o_units: int, o_tcp_accel_percent: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetTCPLinearWithUnits(double oTCPSpeed,DELOlpMotionProfileUnits
                | oUnits,double oTCPAccelPercent)
                |     Template Method: Get the TCP linear speed and the units it is specified in
                |     and acceleration as a percentage.
                |     The following rules are checked for other parameters of the motion
                |     profile.
                | 
                |         Linear Acceleration is specified as a percentage. (Notice message
                |         posted if specified in absolute units)
                |         Linear Acceleration is equal to Linear Deceleration. (Warning message
                |         posted if different)
                |         Angular Speed, Angular Acceleration, and Angular Deceleration are all
                |         100% or device maximum (Warning message posted if
                |         different)
                |         Basis is Speed/Acceleration (Error if different). You should check
                |         IsTimeBasis before calling this method.
                | 
                |     Parameters:
                | 
                |         oTCPSpeed
                |             Linear TCP speed either as percentage or in absolute units.
                |             
                |         oUnits
                |             Indicates if the speed is in percent (1.0 is 100%) or in absolute
                |             units (m/s). 
                |         oTCPAccelPercent
                |             Linear TCP acceleration as a percentage (1.0 is 100%).

        :param float o_tcp_speed:
        :param int o_units:
        :param float o_tcp_accel_percent:
        :return: None
        """
        return self.com_object.GetTCPLinearWithUnits(o_tcp_speed, o_units, o_tcp_accel_percent)

    def get_tcp_speed_angular(self, i_units: int) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetTCPSpeedAngular(DELOlpMotionProfileUnits iUnits) As
                | double
                |     Get TCP angular speed.
                |     This fails if IsTimeBasis returns TRUE.
                | 
                |     Parameters:
                | 
                |         iUnits
                |             The units to get the value in. 1.0 is 100% if Percent is specified.
                |             Value is in rad/s if Absolute is specified. 
                | 
                |     Returns:
                |         The speed in the specified units, converted if needed, but no messages
                |         are reported.

        :param int i_units:
        :return: float
        """
        return self.com_object.GetTCPSpeedAngular(i_units)

    def get_tcp_speed_linear(self, i_units: int) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetTCPSpeedLinear(DELOlpMotionProfileUnits iUnits) As
                | double
                |     Get TCP linear speed.
                |     This fails if IsTimeBasis returns TRUE.
                | 
                |     Parameters:
                | 
                |         iUnits
                |             The units to get the value in. 1.0 is 100% if Percent is specified.
                |             Value is in m/s if Absolute is specified. 
                | 
                |     Returns:
                |         The speed in the specified units, converted if needed, but no messages
                |         are reported.

        :param int i_units:
        :return: float
        """
        return self.com_object.GetTCPSpeedLinear(i_units)

    def get_tcp_speed_with_decel_with_accel_units(self, o_tcp_lin_speed_abs: float, o_tcp_ang_speed_abs: float, o_tcp_lin_accel: float, o_tcp_lin_decel: float, o_accel_decel_units: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetTCPSpeedWithDecelWithAccelUnits(double oTCPLinSpeedAbs,double
                | oTCPAngSpeedAbs,double oTCPLinAccel,double
                | oTCPLinDecel,DELOlpMotionProfileUnits oAccelDecelUnits)
                |     Template Method: Get the TCP linear and angular speed, acceleration,
                |     deceleration, and acceleration units.
                |     The following rules are checked for other parameters of the motion
                |     profile.
                | 
                |         Linear Speed is specified in absolute units. (Notice message posted if
                |         specified as a percentage)
                |         Angular Speed is specified in absolute units. (Notice message posted if
                |         specified as a percentage)
                |         Linear Acceleration and Deceleration both use the same units. (Notice
                |         message posted if different and the acceleration units are
                |         used.)
                |         Angular Acceleration and Angular Deceleration are 100% or device
                |         maximum (Warning message posted if different)
                |         Basis is Speed/Acceleration (Error if different). You should check
                |         IsTimeBasis before calling this method.
                | 
                |     Parameters:
                | 
                |         oTCPLinSpeedAbs
                |             Linear TCP speed in absolute units (m/s). 
                |         oTCPAngSpeedAbs
                |             Angular TCP speed in absolute units (rad/s). 
                |         oTCPAccel
                |             Linear TCP acceleration in units specified by oAccelDecelUnits.
                |             
                |         oTCPDecel
                |             Linear TCP deceleration in units specified by oAccelDecelUnits.
                |             
                |         oAccelDecelUnits
                |             Indicates if the acceleration and deceleration is in percent (1.0
                |             is 100%) or in absolute units (m/s2).

        :param float o_tcp_lin_speed_abs:
        :param float o_tcp_ang_speed_abs:
        :param float o_tcp_lin_accel:
        :param float o_tcp_lin_decel:
        :param int o_accel_decel_units:
        :return: None
        """
        return self.com_object.GetTCPSpeedWithDecelWithAccelUnits(o_tcp_lin_speed_abs, o_tcp_ang_speed_abs, o_tcp_lin_accel, o_tcp_lin_decel, o_accel_decel_units)

    def get_tcp_speed_with_decel_with_speed_units(self, o_tcp_lin_speed: float, o_lin_speed_units: int, o_tcp_ang_speed: float, o_ang_speed_units: int, o_tcp_lin_accel_percent: float, o_tcp_lin_decel_percent: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetTCPSpeedWithDecelWithSpeedUnits(double
                | oTCPLinSpeed,DELOlpMotionProfileUnits oLinSpeedUnits,double
                | oTCPAngSpeed,DELOlpMotionProfileUnits oAngSpeedUnits,double
                | oTCPLinAccelPercent,double oTCPLinDecelPercent)
                |     Template Method: Get the TCP linear speed, angular speed, acceleration,
                |     deceleration, linear speed units, and angular speed units.
                |     The following rules are checked for other parameters of the motion
                |     profile.
                | 
                |         Linear Acceleration is specified as a percentage. (Notice message
                |         posted if specified in absolute units)
                |         Linear Deceleration is specified as a percentage. (Notice message
                |         posted if specified in absolute units)
                |         Angular Acceleration and Angular Deceleration are 100% or device
                |         maximum (Warning message posted if different)
                |         Basis is Speed/Acceleration (Error if different). You should check
                |         IsTimeBasis before calling this method.
                | 
                |     Parameters:
                | 
                |         oTCPLinSpeed
                |             Linear TCP speed in units specified by oLinSpeedUnits.
                |             
                |         oLinSpeedUnits
                |             Indicates if the linear speed is in percent (1.0 is 100%) or in
                |             absolute units (m/s2). 
                |         oTCPAngSpeed
                |             Angular TCP speed in units specified by oAngSpeedUnits.
                |             
                |         oAngSpeedUnits
                |             Indicates if the angular speed is in percent (1.0 is 100%) or in
                |             absolute units (m/s2). 
                |         oTCPLinAccelPercent
                |             Linear TCP acceleration as a percentage (1.0 is 100%).
                |             
                |         oTCPLinDecelPercent
                |             Linear TCP deceleration as a percentage (1.0 is 100%).

        :param float o_tcp_lin_speed:
        :param int o_lin_speed_units:
        :param float o_tcp_ang_speed:
        :param int o_ang_speed_units:
        :param float o_tcp_lin_accel_percent:
        :param float o_tcp_lin_decel_percent:
        :return: None
        """
        return self.com_object.GetTCPSpeedWithDecelWithSpeedUnits(o_tcp_lin_speed, o_lin_speed_units, o_tcp_ang_speed, o_ang_speed_units, o_tcp_lin_accel_percent, o_tcp_lin_decel_percent)

    def get_time(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetTime() As double
                |     Get motion speed as a time.
                |     This fails if IsTimeBasis returns FALSE.
                | 
                |     Returns:
                |         The time in seconds.

        :return: float
        """
        return self.com_object.GetTime()

    def set_joint_as_percent(self, i_speed_percent: float, i_accel_percent: float, i_match: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetJointAsPercent(double iSpeedPercent,double iAccelPercent,boolean
                | iMatch)
                |     Template Method: Set the joint speed and acceleration as a
                |     percentage.
                |     Joint speed/acceleration is equal to the linear TCP speed/acceleration. The
                |     other parameters of the motion profile are set as follows.
                | 
                |         Linear Deceleration and Linear Acceleration are both set to
                |         iAccelPercent as a percentage.
                |         Angular Speed, Angular Acceleration, Angular Deceleration are all set
                |         to 100%.
                |         Basis is set to Speed/Acceleration
                | 
                |     Parameters:
                | 
                |         iSpeedPercent
                |             Joint speed as a percentage (1.0 is 100%). 
                |         iAccelPercent
                |             Joint acceleration as a percentage (1.0 is 100%). 
                |         iMatch
                |             If true, these parameters must match the values on an existing
                |             profile for that profile to be re-used.

        :param float i_speed_percent:
        :param float i_accel_percent:
        :param bool i_match:
        :return: None
        """
        return self.com_object.SetJointAsPercent(i_speed_percent, i_accel_percent, i_match)

    def set_joint_as_percent_with_decel(self, i_speed_percent: float, i_accel_percent: float, i_decel_percent: float, i_match: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetJointAsPercentWithDecel(double iSpeedPercent,double iAccelPercent,double
                | iDecelPercent,boolean iMatch)
                |     Template Method: Set the joint speed, acceleration and deceleration as a
                |     percentage.
                |     Joint speed/acceleration is equal to the linear TCP speed/acceleration. The
                |     other parameters of the motion profile are set as follows.
                | 
                |         Angular Speed, Angular Acceleration, Angular Deceleration are all set
                |         to 100%.
                |         Basis is set to Speed/Acceleration
                | 
                |     Parameters:
                | 
                |         iSpeed
                |             Joint speed as a percentage (1.0 is 100%). 
                |         iAccel
                |             Joint acceleration as a percentage (1.0 is 100%). 
                |         iDecel
                |             Joint deceleration as a percentage (1.0 is 100%). 
                |         iMatch
                |             If true, these parameters must match the values on an existing
                |             profile for that profile to be re-used.

        :param float i_speed_percent:
        :param float i_accel_percent:
        :param float i_decel_percent:
        :param bool i_match:
        :return: None
        """
        return self.com_object.SetJointAsPercentWithDecel(i_speed_percent, i_accel_percent, i_decel_percent, i_match)

    def set_tcp_accel_angular(self, i_units: int, i_accel: float, i_match: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetTCPAccelAngular(DELOlpMotionProfileUnits iUnits,double iAccel,boolean
                | iMatch)
                |     Set TCP angular acceleration.
                |     This fails if IsTimeBasis returns TRUE.
                | 
                |     Parameters:
                | 
                |         iUnits
                |             The units the value is being set in. The units are also set. Value
                |             is between 0.0 and 1.0 if Percent is specified. Value must be in rad/s^2 if
                |             Absolute is specified. 
                |         iAccel
                |             The acceleration value. 
                |         iMatch
                |             If true, this parameter must match the values on an existing
                |             profile for that profile to be re-used.

        :param int i_units:
        :param float i_accel:
        :param bool i_match:
        :return: None
        """
        return self.com_object.SetTCPAccelAngular(i_units, i_accel, i_match)

    def set_tcp_accel_linear(self, i_units: int, i_accel: float, i_match: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetTCPAccelLinear(DELOlpMotionProfileUnits iUnits,double iAccel,boolean
                | iMatch)
                |     Set TCP linear acceleration.
                | 
                |     Parameters:
                | 
                |         iUnits
                |             The units the value is being set in. The units are also set. Value
                |             is between 0.0 and 1.0 if Percent is specified. Value must be in m/s^2 if
                |             Absolute is specified. 
                |         iAccel
                |             The acceleration value. 
                |         iMatch
                |             If true, this parameter must match the values on an existing
                |             profile for that profile to be re-used.

        :param int i_units:
        :param float i_accel:
        :param bool i_match:
        :return: None
        """
        return self.com_object.SetTCPAccelLinear(i_units, i_accel, i_match)

    def set_tcp_angular(self, i_tcp_speed_abs: float, i_tcp_accel_percent: float, i_match: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetTCPAngular(double iTCPSpeedAbs,double iTCPAccelPercent,boolean
                | iMatch)
                |     Template Method: Set the TCP angular speed and
                |     acceleration.
                |     The other parameters of the motion profile are set as
                |     follows.
                | 
                |         Angular Deceleration and Angular Acceleration are both set to
                |         iTCPAccelPercent as a percentage.
                |         Linear Speed, Linear Acceleration, Linear Deceleration are all set to
                |         100%.
                |         Basis is set to Speed/Acceleration
                | 
                |     Parameters:
                | 
                |         iTCPSpeedAbs
                |             Angular TCP speed in absolute units (rad/s). 
                |         iTCPAccelPercent
                |             Angular TCP acceleration as a percentage (1.0 is 100%).
                |             
                |         iMatch
                |             If true, these parameters must match the values on an existing
                |             profile for that profile to be re-used.

        :param float i_tcp_speed_abs:
        :param float i_tcp_accel_percent:
        :param bool i_match:
        :return: None
        """
        return self.com_object.SetTCPAngular(i_tcp_speed_abs, i_tcp_accel_percent, i_match)

    def set_tcp_angular_with_decel(self, i_tcp_speed_abs: float, i_tcp_accel_percent: float, i_tcp_decel_percent: float, i_match: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetTCPAngularWithDecel(double iTCPSpeedAbs,double iTCPAccelPercent,double
                | iTCPDecelPercent,boolean iMatch)
                |     Template Method: Set the TCP angular speed, acceleration and
                |     deceleration.
                |     The other parameters of the motion profile are set as
                |     follows.
                | 
                |         Linear Speed, Linear Acceleration, Linear Deceleration are all set to
                |         100%.
                |         Basis is set to Speed/Acceleration
                | 
                |     Parameters:
                | 
                |         iTCPSpeedAbs
                |             Angular TCP speed in absolute units (rad/s). 
                |         iTCPAccelPercent
                |             Angular TCP acceleration as a percentage (1.0 is 100%).
                |             
                |         iTCPDecelPercent
                |             Angular TCP deceleration as a percentage (1.0 is 100%).
                |             
                |         iMatch
                |             If true, these parameters must match the values on an existing
                |             profile for that profile to be re-used.

        :param float i_tcp_speed_abs:
        :param float i_tcp_accel_percent:
        :param float i_tcp_decel_percent:
        :param bool i_match:
        :return: None
        """
        return self.com_object.SetTCPAngularWithDecel(i_tcp_speed_abs, i_tcp_accel_percent, i_tcp_decel_percent, i_match)

    def set_tcp_decel_angular(self, i_units: int, i_decel: float, i_match: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetTCPDecelAngular(DELOlpMotionProfileUnits iUnits,double iDecel,boolean
                | iMatch)
                |     Set TCP angular deceleration.
                | 
                |     Parameters:
                | 
                |         iUnits
                |             The units the value is being set in. The units are also set. Value
                |             is between 0.0 and 1.0 if Percent is specified. Value must be in rad/s^2 if
                |             Absolute is specified. 
                |         iDecel
                |             The deceleration value. 
                |         iMatch
                |             If true, this parameter must match the values on an existing
                |             profile for that profile to be re-used.

        :param int i_units:
        :param float i_decel:
        :param bool i_match:
        :return: None
        """
        return self.com_object.SetTCPDecelAngular(i_units, i_decel, i_match)

    def set_tcp_decel_linear(self, i_units: int, i_decel: float, i_match: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetTCPDecelLinear(DELOlpMotionProfileUnits iUnits,double iDecel,boolean
                | iMatch)
                |     Set TCP linear deceleration.
                | 
                |     Parameters:
                | 
                |         iUnits
                |             The units the value is being set in. The units are also set. Value
                |             is between 0.0 and 1.0 if Percent is specified. Value must be in m/s^2 if
                |             Absolute is specified. 
                |         iDecel
                |             The deceleration value. 
                |         iMatch
                |             If true, this parameter must match the values on an existing
                |             profile for that profile to be re-used.

        :param int i_units:
        :param float i_decel:
        :param bool i_match:
        :return: None
        """
        return self.com_object.SetTCPDecelLinear(i_units, i_decel, i_match)

    def set_tcp_linear(self, i_tcp_speed_abs: float, i_tcp_accel_percent: float, i_match: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetTCPLinear(double iTCPSpeedAbs,double iTCPAccelPercent,boolean
                | iMatch)
                |     Template Method: Set the TCP linear speed and
                |     acceleration.
                |     The other parameters of the motion profile are set as
                |     follows.
                | 
                |         Linear Deceleration and Linear Acceleration are both set to
                |         iTCPAccelPercent as a percentage.
                |         Angular Speed, Angular Acceleration, Angular Deceleration are all set
                |         to 100%.
                |         Basis is set to Speed/Acceleration
                | 
                |     Parameters:
                | 
                |         iTCPSpeedAbs
                |             Linear TCP speed in absolute units (m/s). 
                |         iTCPAccelPercent
                |             Linear TCP acceleration as a percentage (1.0 is 100%).
                |             
                |         iMatch
                |             If true, these parameters must match the values on an existing
                |             profile for that profile to be re-used.

        :param float i_tcp_speed_abs:
        :param float i_tcp_accel_percent:
        :param bool i_match:
        :return: None
        """
        return self.com_object.SetTCPLinear(i_tcp_speed_abs, i_tcp_accel_percent, i_match)

    def set_tcp_linear_no_accel(self, i_tcp_speed_abs: float, i_match: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetTCPLinearNoAccel(double iTCPSpeedAbs,boolean iMatch)
                |     Template Method: Set the TCP linear speed.
                |     The other parameters of the motion profile are set as
                |     follows.
                | 
                |         Linear Acceleration, Linear Deceleration, Angular Speed, Angular
                |         Acceleration, and Angular Deceleration are all set to
                |         100%.
                |         Basis is set to Speed/Acceleration
                | 
                |     Parameters:
                | 
                |         iTCPSpeedAbs
                |             Linear TCP speed in absolute units (m/s). 
                |         iMatch
                |             If true, these parameters must match the values on an existing
                |             profile for that profile to be re-used.

        :param float i_tcp_speed_abs:
        :param bool i_match:
        :return: None
        """
        return self.com_object.SetTCPLinearNoAccel(i_tcp_speed_abs, i_match)

    def set_tcp_linear_no_accel_with_units(self, i_tcp_speed: float, i_units: int, i_match: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetTCPLinearNoAccelWithUnits(double iTCPSpeed,DELOlpMotionProfileUnits
                | iUnits,boolean iMatch)
                |     Template Method: Set the TCP linear speed and the units it is specified
                |     in.
                |     The other parameters of the motion profile are set as
                |     follows.
                | 
                |         Linear Acceleration, Linear Deceleration, Angular Speed, Angular
                |         Acceleration, and Angular Deceleration are all set to
                |         100%.
                |         Basis is set to Speed/Acceleration
                | 
                |     Parameters:
                | 
                |         iTCPSpeed
                |             Linear TCP speed either as percentage or in absolute units.
                |             
                |         iUnits
                |             Indicates if the speed is in percent (1.0 is 100%) or in absolute
                |             units (m/s). 
                |         iMatch
                |             If true, these parameters must match the values on an existing
                |             profile for that profile to be re-used.

        :param float i_tcp_speed:
        :param int i_units:
        :param bool i_match:
        :return: None
        """
        return self.com_object.SetTCPLinearNoAccelWithUnits(i_tcp_speed, i_units, i_match)

    def set_tcp_linear_with_decel(self, i_tcp_speed_abs: float, i_tcp_accel_percent: float, i_tcp_decel_percent: float, i_match: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetTCPLinearWithDecel(double iTCPSpeedAbs,double iTCPAccelPercent,double
                | iTCPDecelPercent,boolean iMatch)
                |     Template Method: Set the TCP linear speed, acceleration and
                |     deceleration.
                |     The other parameters of the motion profile are set as
                |     follows.
                | 
                |         Angular Speed, Angular Acceleration, Angular Deceleration are all set
                |         to 100%.
                |         Basis is set to Speed/Acceleration
                | 
                |     Parameters:
                | 
                |         iTCPSpeedAbs
                |             Linear TCP speed in absolute units (m/s). 
                |         iTCPAccelPercent
                |             Linear TCP acceleration as a percentage (1.0 is 100%).
                |             
                |         iTCPDecelPercent
                |             Linear TCP deceleration as a percentage (1.0 is 100%).
                |             
                |         iMatch
                |             If true, these parameters must match the values on an existing
                |             profile for that profile to be re-used.

        :param float i_tcp_speed_abs:
        :param float i_tcp_accel_percent:
        :param float i_tcp_decel_percent:
        :param bool i_match:
        :return: None
        """
        return self.com_object.SetTCPLinearWithDecel(i_tcp_speed_abs, i_tcp_accel_percent, i_tcp_decel_percent, i_match)

    def set_tcp_linear_with_units(self, i_tcp_speed: float, i_units: int, i_tcp_accel_percent: float, i_match: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetTCPLinearWithUnits(double iTCPSpeed,DELOlpMotionProfileUnits
                | iUnits,double iTCPAccelPercent,boolean iMatch)
                |     Template Method: Set the TCP linear speed and the units it is specified in
                |     and acceleration as a percentage.
                |     The other parameters of the motion profile are set as
                |     follows.
                | 
                |         Linear Deceleration and Linear Acceleration are both set to
                |         iTCPAccelPercent as a percentage.
                |         Angular Speed, Angular Acceleration, Angular Deceleration are all set
                |         to 100%.
                |         Basis is set to Speed/Acceleration
                | 
                |     Parameters:
                | 
                |         iTCPSpeed
                |             Linear TCP speed either as percentage or in absolute units.
                |             
                |         iUnits
                |             Indicates if the speed is in percent (1.0 is 100%) or in absolute
                |             units (m/s). 
                |         iTCPAccelPercent
                |             Linear TCP acceleration as a percentage (1.0 is 100%).
                |             
                |         iMatch
                |             If true, these parameters must match the values on an existing
                |             profile for that profile to be re-used.

        :param float i_tcp_speed:
        :param int i_units:
        :param float i_tcp_accel_percent:
        :param bool i_match:
        :return: None
        """
        return self.com_object.SetTCPLinearWithUnits(i_tcp_speed, i_units, i_tcp_accel_percent, i_match)

    def set_tcp_speed_angular(self, i_units: int, i_speed: float, i_match: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetTCPSpeedAngular(DELOlpMotionProfileUnits iUnits,double iSpeed,boolean
                | iMatch)
                |     Set TCP angular speed.
                | 
                |     Parameters:
                | 
                |         iUnits
                |             The units the value is being set in. The units are also set. Value
                |             is between 0.0 and 1.0 if Percent is specified. Value must be in rad/s if
                |             Absolute is specified. 
                |         iSpeed
                |             The speed value. 
                |         iMatch
                |             If true, this parameter must match the values on an existing
                |             profile for that profile to be re-used.

        :param int i_units:
        :param float i_speed:
        :param bool i_match:
        :return: None
        """
        return self.com_object.SetTCPSpeedAngular(i_units, i_speed, i_match)

    def set_tcp_speed_linear(self, i_units: int, i_speed: float, i_match: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetTCPSpeedLinear(DELOlpMotionProfileUnits iUnits,double iSpeed,boolean
                | iMatch)
                |     Set TCP linear speed.
                | 
                |     Parameters:
                | 
                |         iUnits
                |             The units the value is being set in. The units are also set. Value
                |             is between 0.0 and 1.0 if Percent is specified. Value must be in m/s if
                |             Absolute is specified. 
                |         iSpeed
                |             The speed value. 
                |         iMatch
                |             If true, this parameter must match the values on an existing
                |             profile for that profile to be re-used.

        :param int i_units:
        :param float i_speed:
        :param bool i_match:
        :return: None
        """
        return self.com_object.SetTCPSpeedLinear(i_units, i_speed, i_match)

    def set_tcp_speed_with_decel_with_accel_units(self, i_tcp_lin_speed_abs: float, i_tcp_ang_speed_abs: float, i_tcp_lin_accel: float, i_tcp_lin_decel: float, i_accel_decel_units: int, i_match: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetTCPSpeedWithDecelWithAccelUnits(double iTCPLinSpeedAbs,double
                | iTCPAngSpeedAbs,double iTCPLinAccel,double
                | iTCPLinDecel,DELOlpMotionProfileUnits iAccelDecelUnits,boolean
                | iMatch)
                |     Template Method: Set the TCP linear and angular speed, acceleration,
                |     deceleration, and acceleration units.
                |     The other parameters of the motion profile are set as
                |     follows.
                | 
                |         Angular Acceleration and Angular Deceleration are set to
                |         100%.
                |         Basis is set to Speed/Acceleration
                | 
                |     Parameters:
                | 
                |         iTCPLinSpeedAbs
                |             Linear TCP speed in absolute units (m/s). 
                |         iTCPAngSpeedAbs
                |             Angular TCP speed in absolute units (rad/s). 
                |         iTCPAccelAbs
                |             Linear TCP acceleration in absolute units (m/s2). 
                |         iTCPDecelAbs
                |             Linear TCP deceleration in absolute units (m/s2). 
                |         iAccelDecelUnits
                |             Indicates if the acceleration and deceleration is in percent (1.0
                |             is 100%) or in absolute units (m/s2). 
                |         iMatch
                |             If true, these parameters must match the values on an existing
                |             profile for that profile to be re-used.

        :param float i_tcp_lin_speed_abs:
        :param float i_tcp_ang_speed_abs:
        :param float i_tcp_lin_accel:
        :param float i_tcp_lin_decel:
        :param int i_accel_decel_units:
        :param bool i_match:
        :return: None
        """
        return self.com_object.SetTCPSpeedWithDecelWithAccelUnits(i_tcp_lin_speed_abs, i_tcp_ang_speed_abs, i_tcp_lin_accel, i_tcp_lin_decel, i_accel_decel_units, i_match)

    def set_tcp_speed_with_decel_with_speed_units(self, i_tcp_lin_speed: float, i_lin_speed_units: int, i_tcp_ang_speed: float, i_ang_speed_units: int, i_tcp_lin_accel_percent: float, i_tcp_lin_decel_percent: float, i_match: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetTCPSpeedWithDecelWithSpeedUnits(double
                | iTCPLinSpeed,DELOlpMotionProfileUnits iLinSpeedUnits,double
                | iTCPAngSpeed,DELOlpMotionProfileUnits iAngSpeedUnits,double
                | iTCPLinAccelPercent,double iTCPLinDecelPercent,boolean iMatch)
                |     Template Method: Set the TCP linear speed, angular speed, acceleration,
                |     deceleration, linear speed units, and angular speed units.
                |     The other parameters of the motion profile are set as
                |     follows.
                | 
                |         Angular Acceleration and Angular Deceleration are set to
                |         100%.
                |         Basis is set to Speed/Acceleration
                | 
                |     Parameters:
                | 
                |         iTCPLinSpeed
                |             Linear TCP speed in units specified by oLinSpeedUnits.
                |             
                |         iLinSpeedUnits
                |             Indicates if the linear speed is in percent (1.0 is 100%) or in
                |             absolute units (m/s2). 
                |         iTCPAngSpeed
                |             Angular TCP speed in units specified by oAngSpeedUnits.
                |             
                |         iAngSpeedUnits
                |             Indicates if the angular speed is in percent (1.0 is 100%) or in
                |             absolute units (m/s2). 
                |         iTCPLinAccelPercent
                |             Linear TCP acceleration as a percentage (1.0 is 100%).
                |             
                |         iTCPLinDecelPercent
                |             Linear TCP deceleration as a percentage (1.0 is 100%).
                |             
                |         iMatch
                |             If true, these parameters must match the values on an existing
                |             profile for that profile to be re-used.

        :param float i_tcp_lin_speed:
        :param int i_lin_speed_units:
        :param float i_tcp_ang_speed:
        :param int i_ang_speed_units:
        :param float i_tcp_lin_accel_percent:
        :param float i_tcp_lin_decel_percent:
        :param bool i_match:
        :return: None
        """
        return self.com_object.SetTCPSpeedWithDecelWithSpeedUnits(i_tcp_lin_speed, i_lin_speed_units, i_tcp_ang_speed, i_ang_speed_units, i_tcp_lin_accel_percent, i_tcp_lin_decel_percent, i_match)

    def set_time(self, i_time: float, i_match: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetTime(double iTime,boolean iMatch)
                |     Set motion speed as a time.
                |     On set, the motion basis is set to time.
                | 
                |     Parameters:
                | 
                |         iTime
                |             The time in seconds. 
                |         iMatch
                |             If true, this parameter must match the values on an existing
                |             profile for that profile to be re-used. 

        :param float i_time:
        :param bool i_match:
        :return: None
        """
        return self.com_object.SetTime(i_time, i_match)

    def __repr__(self):
        return f'OLPMotionProfile(name="{ self.name }")'
