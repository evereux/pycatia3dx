"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class CtmCurveOrienter(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     CtmCurveOrienter
                | 
                | Interface representing the orientation for a curve
                | Role: This interface is used to get and set global YPR and rake
                | angles.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def get_base_axis_mode(self, o_base_axis_mode: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Sub GetBaseAxisMode(CtmBaseAxisOrientation oBaseAxisMode)
                |     Retrieves the value of the BaseAxis mode.
                | 
                |     Parameters:
                | 
                |         oBaseAxisMode
                |             Base Axis Mode. 
                | 
                |     Returns:
                |     Example:
                | 
                |          Dim objOrienter As CtmCurveOrienter
                |                ........
                |          Dim oBaseAxisMode As CtmReferenceOrientation
                |          Call oOrienter.GetBaseAxisMode(oBaseAxisMode)

        :param int o_base_axis_mode:
        :return: None
        """
        return self.com_object.GetBaseAxisMode(o_base_axis_mode)

    def get_global_brr(self, o_base_angle: float, o_rake_angle: float, o_roll_angle: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Sub GetGlobalBRR(double oBaseAngle,double oRakeAngle,double
                | oRollAngle)
                |     Retrieves the value of the GLOBAL angles.
                | 
                |     Parameters:
                | 
                |         oBaseAngle
                |         oRakeAngle
                |         oRollAngle
                |             Rotation angle in radians. 
                | 
                |     Returns:
                |     Example:
                | 
                |          Dim objOrienter As CtmCurveOrienter
                |                ........
                |          Dim oBaseAngle, oRakeAngle, oRollAngle As Double
                |          Call oOrienter.GetGlobalYPR(oBaseAngle, oRakeAngle,
                |          oRollAngle)

        :param float o_base_angle:
        :param float o_rake_angle:
        :param float o_roll_angle:
        :return: None
        """
        return self.com_object.GetGlobalBRR(o_base_angle, o_rake_angle, o_roll_angle)

    def get_global_ypr(self, o_yaw_angle: float, o_pitch_angle: float, o_roll_angle: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Sub GetGlobalYPR(double oYawAngle,double oPitchAngle,double
                | oRollAngle)
                |     Retrieves the value of the GLOBAL angles.
                | 
                |     Parameters:
                | 
                |         oYawAngle
                |         oPitchAngle
                |         oRollAngle
                |             Rotation angle in radians. 
                | 
                |     Returns:
                |     Example:
                | 
                |          Dim objOrienter As CtmCurveOrienter
                |                ........
                |          Dim oYawAngle, oPitchAngle, oRollAngle As Double
                |          Call oOrienter.GetGlobalYPR(oYawAngle, oPitchAngle,
                |          oRollAngle)

        :param float o_yaw_angle:
        :param float o_pitch_angle:
        :param float o_roll_angle:
        :return: None
        """
        return self.com_object.GetGlobalYPR(o_yaw_angle, o_pitch_angle, o_roll_angle)

    def get_rake_angle(self, i_angle_loc: int, o_rake_angle: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Sub GetRakeAngle(CtmRakeLocation iAngleLoc,double oRakeAngle)
                |     Retrieves the value Rake on either start or end tag.
                | 
                |     Parameters:
                | 
                |         oRakeAngle
                |             Rotation angle in radians. 
                |         iAngleLoc
                |             CtmRakeLocation 
                | 
                |     Returns:
                |     Example:
                | 
                |          Dim objOrienter As CtmCurveOrienter
                |                ........
                |          Dim oRakeAngle As Double
                |          Call oOrienter.GetRakeAngle(FLAREEND, oRakeAngle)

        :param int i_angle_loc:
        :param float o_rake_angle:
        :return: None
        """
        return self.com_object.GetRakeAngle(i_angle_loc, o_rake_angle)

    def set_base_axis_mode(self, i_base_axis_mode: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Sub SetBaseAxisMode(CtmBaseAxisOrientation iBaseAxisMode)
                |     Sets the value of the BaseAxis mode.
                | 
                |     Parameters:
                | 
                |         iBaseAxisMode
                |             Base Axis Mode. 
                | 
                |     Returns:
                |     Example:
                | 
                |          Dim objOrienter As CtmCurveOrienter
                |                ........
                |          Dim iBaseAxisMode As CtmReferenceOrientation
                |          Call oOrienter.SetBaseAxisMode(iBaseAxisMode)

        :param int i_base_axis_mode:
        :return: None
        """
        return self.com_object.SetBaseAxisMode(i_base_axis_mode)

    def set_global_brr(self, i_base_angle: float, i_rake_angle: float, i_roll_angle: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Sub SetGlobalBRR(double iBaseAngle,double iRakeAngle,double
                | iRollAngle)
                |     Set the value of the GLOBAL angles.
                | 
                |     Parameters:
                | 
                |         iBaseAngle
                |         iRakeAngle
                |         iRollAngle
                |             Rotation angle in radians. 
                | 
                |     Returns:
                |     Example:
                | 
                |          Dim objOrienter As CtmCurveOrienter
                |                ........
                |          Call oOrienter.SetGlobalYPR(2.5, 1.9, 3.1)

        :param float i_base_angle:
        :param float i_rake_angle:
        :param float i_roll_angle:
        :return: None
        """
        return self.com_object.SetGlobalBRR(i_base_angle, i_rake_angle, i_roll_angle)

    def set_global_ypr(self, i_yaw_angle: float, i_pitch_angle: float, i_roll_angle: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Sub SetGlobalYPR(double iYawAngle,double iPitchAngle,double
                | iRollAngle)
                |     Set the value of the GLOBAL angles.
                | 
                |     Parameters:
                | 
                |         iYawAngle
                |         iPitchAngle
                |         iRollAngle
                |             Rotation angle in radians. 
                | 
                |     Returns:
                |     Example:
                | 
                |          Dim objOrienter As CtmCurveOrienter
                |                ........
                |          Call oOrienter.SetGlobalYPR(2.5, 1.9, 3.1)

        :param float i_yaw_angle:
        :param float i_pitch_angle:
        :param float i_roll_angle:
        :return: None
        """
        return self.com_object.SetGlobalYPR(i_yaw_angle, i_pitch_angle, i_roll_angle)

    def set_rake_angle(self, i_rake_angle: float, i_angle_loc: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Sub SetRakeAngle(double iRakeAngle,CtmRakeLocation iAngleLoc)
                |     Set the value Rake on either start or end tag.
                | 
                |     Parameters:
                | 
                |         iRakeAngle
                |             Rotation angle in radians. 
                |         iAngleLoc
                |         Example:
                | 
                |              Dim objOrienter As CtmCurveOrienter
                |                    ........
                |              Call oOrienter.SetRakeAngle(2.5, FLARESTART);

        :param float i_rake_angle:
        :param int i_angle_loc:
        :return: None
        """
        return self.com_object.SetRakeAngle(i_rake_angle, i_angle_loc)

    def __repr__(self):
        return f'CtmCurveOrienter(name="{ self.name }")'
