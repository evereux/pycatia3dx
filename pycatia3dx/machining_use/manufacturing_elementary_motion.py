"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class ManufacturingElementaryMotion(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     ManufacturingElementaryMotion
                | 
                | Interface to manage the elementary motion of a macro.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def feedrate_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property FeedrateType() As long
                |     Returns or sets the feedrate type. Possible values are: 1:Machining
                |     Feedrate, 2:Approach Feedrate, 3:Retract Feedrate, 4:Rapid Feedrate,
                |     5:Local(Undefined Feedrate), 6:Finishing, 7:Air Cutting

        :return: int
        """

        return self.com_object.FeedrateType

    @feedrate_type.setter
    def feedrate_type(self, value: int):
        """
        :param int value:
        """

        self.com_object.FeedrateType = value

    @property
    def feedrate_value(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property FeedrateValue() As double
                |     Returns or sets the feedrate value when feedrate type is Local.

        :return: float
        """

        return self.com_object.FeedrateValue

    @feedrate_value.setter
    def feedrate_value(self, value: float):
        """
        :param float value:
        """

        self.com_object.FeedrateValue = value

    def add_pp_word(self, i_pp_word: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub AddPPWord(CATBSTR iPPWord)
                |     Sets the syntax of a PP Word motion.
                | 
                |     Parameters:
                | 
                |         iPPWord
                |             The PP word syntax

        :param str i_pp_word:
        :return: None
        """
        return self.com_object.AddPPWord(i_pp_word)

    def get_angular_orientation_value(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetAngularOrientationValue() As double
                |     Read AngularOrientationValue from an Elementary Motion if ElementaryMotionType = Circular.
                | 
                |     Parameters:
                | 
                |         oAngularOrientationValue
                |             The angular orientation value

        :return: float
        """
        return self.com_object.GetAngularOrientationValue()

    def get_angular_sector_value(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetAngularSectorValue() As double
                |     Read AngularSectorValue from an Elementary Motion if ElementaryMotionType = Circular.
                | 
                |     Parameters:
                | 
                |         oAngularSectorValue
                |             The angular sector value

        :return: float
        """
        return self.com_object.GetAngularSectorValue()

    def get_circle_radius_value(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetCircleRadiusValue() As double
                |     Read CircleRadiusValue from an Elementary Motion if ElementaryMotionType = Circular.
                | 
                |     Parameters:
                | 
                |         oCircleRadiusValue
                |             The circle radius value

        :return: float
        """
        return self.com_object.GetCircleRadiusValue()

    def get_distance_value(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetDistanceValue() As double
                |     Read a DistanceValue from an Elementary Motion if ElementaryMotionType = Horizontal or Axial or DeltaLnDist.
                | 
                |     Parameters:
                | 
                |         oDistanceValue
                |             The distance value

        :return: float
        """
        return self.com_object.GetDistanceValue()

    def get_elementary_motion_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetElementaryMotionType() As long
                |     Gets the type of an Elementary Motion. The Horizontal type corresponds to
                |     Tangent and Normal types of Macro User Interface in the MO edit
                |     Panel.
                | 
                |     Returns:
                | 
                |             0:MfgMacroClearanceMotion
                |             1:MfgMacroElementaryAxialMotion
                |             2:MfgMacroElementaryHorizontalMotion
                |             3:MfgMacroElementaryCircularMotion
                |             4:MfgMacroPPWord
                |             5:MfgMacroElementaryRampingMotion
                |             6:MfgMacroElementaryGoToAPlaneMotion
                |             7:MfgMacroElementaryGoToAPointMotion
                |             8:MfgMacroElementaryDeltaLnDistMotion
                |             9:MfgMacroElementaryToolAxisMotion
                |             10:MfgMacroElementaryHelixMotion
                |             11:MfgMacroElementaryGoToALineMotion
                |             12:MfgMacroElementarySimultaneousAxisMotion

        :return: int
        """
        return self.com_object.GetElementaryMotionType()

    def get_horizontal_angle_value(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetHorizontalAngleValue() As double
                |     Read a HorizontalAngleValue from an Elementary Motion if ElementaryMotionType = Horizontal.
                | 
                |     Parameters:
                | 
                |         oHorizontalAngleValue
                |             The horizontal angle value

        :return: float
        """
        return self.com_object.GetHorizontalAngleValue()

    def get_horizontal_safety_distance_value(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetHorizontalSafetyDistanceValue() As double
                |     Read HorizontalSafetyDistanceValue from an Elementary Motion if ElementaryMotionType = Ramping.
                | 
                |     Parameters:
                | 
                |         oHorizontalDistanceValue
                |             The horizontal distance value

        :return: float
        """
        return self.com_object.GetHorizontalSafetyDistanceValue()

    def get_motion_direction_vector(self, vector_x: float, vector_y: float, vector_z: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetMotionDirectionVector(double vectorX,double vectorY,double
                | vectorZ)
                |     Read DirectionVector from an Elementary Motion if ElementaryMotionType = DeltaLnDist.
                | 
                |     Parameters:
                | 
                |         oVector
                |             The direction vector

        :param float vector_x:
        :param float vector_y:
        :param float vector_z:
        :return: None
        """
        return self.com_object.GetMotionDirectionVector(vector_x, vector_y, vector_z)

    def get_motion_point(self, point_x: float, point_y: float, point_z: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetMotionPoint(double pointX,double pointY,double pointZ)
                |     Read Point from an Elementary Motion if ElementaryMotionType = GoToAPpoint.
                | 
                |     Parameters:
                | 
                |         oPoint
                |             The point

        :param float point_x:
        :param float point_y:
        :param float point_z:
        :return: None
        """
        return self.com_object.GetMotionPoint(point_x, point_y, point_z)

    def get_motion_to_plane_mode(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetMotionToPlaneMode() As long
                |     Read the way to move to the Plane from an Elementary Motion if ElementaryMotionType = GoToAPlane.
                | 
                |     Parameters:
                | 
                |         oMode
                | 
                |                 0:perpendicular to the plane move
                |                 1: axial move

        :return: int
        """
        return self.com_object.GetMotionToPlaneMode()

    def get_motion_tool_axis(self, vector_x: float, vector_y: float, vector_z: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetMotionToolAxis(double vectorX,double vectorY,double
                | vectorZ)
                |     Read DirectionVector from an Elementary Motion if ElementaryMotionType = ToolAxis.
                | 
                |     Parameters:
                | 
                |         oVector
                |             The direction vector

        :param float vector_x:
        :param float vector_y:
        :param float vector_z:
        :return: None
        """
        return self.com_object.GetMotionToolAxis(vector_x, vector_y, vector_z)

    def get_number_of_pp_word(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetNumberOfPPWord() As long
                |     Get the number of PPWords..

        :return: int
        """
        return self.com_object.GetNumberOfPPWord()

    def get_pp_word(self, index: int) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetPPWord(long index) As CATBSTR
                |     Get the index-st PPword.
                | 
                |     Parameters:
                | 
                |         index
                |             index of the wanted PPWord 
                |         oPPWord
                |             Corresponding PPWord found

        :param int index:
        :return: str
        """
        return self.com_object.GetPPWord(index)

    def get_pp_word_list(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetPPWordList() As CATBSTR
                |     Gets the syntax of a PP Word motion.
                | 
                |     Returns:
                |         The PP word syntax

        :return: str
        """
        return self.com_object.GetPPWordList()

    def get_parameter_value(self, i_name: str) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetParameterValue(CATBSTR iName) As double
                |     Gets the value of a parameter .
                | 
                |     Parameters:
                | 
                |         iName
                |             The parameter name. Authorized values are:
                | 
                |                 MfgMacroDistance: distance
                |                 MfgMacroPositionningAngleA: vertical angle
                |                 MfgMacroPositionningAngleB: horizontal angle
                |                 MfgMacroRadius: circular radius
                |                 MfgMacroCircleAngularPositionA: circular angular
                |                 sector
                |                 MfgMacroCircleAngularPositionB: circular angular
                |                 orientation
                |                 MfgMacroRampingAngle: ramping angle
                |                 MfgMacroHorizontalSafetyDistance: ramping horizontal safety
                |                 distance
                |                 MfgMacroVerticalSafetyDistance: ramping vertical safety
                |                 distance
                | 
                |     Returns:
                |         The parameter value

        :param str i_name:
        :return: float
        """
        return self.com_object.GetParameterValue(i_name)

    def get_ramping_angle_value(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetRampingAngleValue() As double
                |     Read RampingAngleValue from an Elementary Motion if ElementaryMotionType = Ramping.
                | 
                |     Parameters:
                | 
                |         oRampingAngleValue
                |             The ramping angle value

        :return: float
        """
        return self.com_object.GetRampingAngleValue()

    def get_spindle_speed_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetSpindleSpeedType() As long
                |     Read a SpindleSpeedType from an Elementary Motion.
                | 
                |     Parameters:
                | 
                |         oSpindleSpeedType
                | 
                |                 (1: Machining 2:Approach, 3: Retract , 4: Rapid, 5:Local -
                |                 Undefined Spindle Speed)

        :return: int
        """
        return self.com_object.GetSpindleSpeedType()

    def get_spindle_speed_value(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetSpindleSpeedValue() As double
                |     Read a SpindleSpeedValue from an Elementary Motion if SpindleSpeedType = Local /Undefined Spindle Speed.
                | 
                |     Parameters:
                | 
                |         oSpindle
                |             The spindle spped value

        :return: float
        """
        return self.com_object.GetSpindleSpeedValue()

    def get_vertical_angle_value(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetVerticalAngleValue() As double
                |     Read a VerticalAngleValue from an Elementary Motion if ElementaryMotionType = Horizontal.
                | 
                |     Parameters:
                | 
                |         oVerticalAngleValue
                |             The vertical angle value

        :return: float
        """
        return self.com_object.GetVerticalAngleValue()

    def get_vertical_safety_distance_value(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetVerticalSafetyDistanceValue() As double
                |     Read VerticalSafetyDistanceValue from an Elementary Motion if ElementaryMotionType = Ramping.
                | 
                |     Parameters:
                | 
                |         oVerticalDistanceValue
                |             The vertical distance value

        :return: float
        """
        return self.com_object.GetVerticalSafetyDistanceValue()

    def is_active(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func IsActive() As long
                |     Returns if an elementary motion is active or not.
                | 
                |     Parameters:
                | 
                |         oActive
                | 
                |                 0:not active
                |                 1:Active

        :return: int
        """
        return self.com_object.IsActive()

    def remove_pp_word(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub RemovePPWord()
                |     Remove all the PPWords.

        :return: None
        """
        return self.com_object.RemovePPWord()

    def set_active(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetActive()
                |     Set an Elementary Motion to Active Status

        :return: None
        """
        return self.com_object.SetActive()

    def set_angular_orientation_value(self, i_angular_orientation_value: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetAngularOrientationValue(double
                | iAngularOrientationValue)
                |     Set AngularOrientationValue of an Elementary Motion if ElementaryMotionType = Circular.
                | 
                |     Parameters:
                | 
                |         iAngularOrientationValue
                |             The angular orientation value

        :param float i_angular_orientation_value:
        :return: None
        """
        return self.com_object.SetAngularOrientationValue(i_angular_orientation_value)

    def set_angular_sector_value(self, i_angular_sector_value: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetAngularSectorValue(double iAngularSectorValue)
                |     Set AngularSectorValue of an Elementary Motion if ElementaryMotionType = Circular.
                | 
                |     Parameters:
                | 
                |         iAngularSectorValue
                |             The angular sector value

        :param float i_angular_sector_value:
        :return: None
        """
        return self.com_object.SetAngularSectorValue(i_angular_sector_value)

    def set_circle_radius_value(self, i_circle_radius_value: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetCircleRadiusValue(double iCircleRadiusValue)
                |     Set CircleRadiusValue of an Elementary Motion if ElementaryMotionType = Circular.
                | 
                |     Parameters:
                | 
                |         iCircleRadiusValue
                |             The circle radius value

        :param float i_circle_radius_value:
        :return: None
        """
        return self.com_object.SetCircleRadiusValue(i_circle_radius_value)

    def set_distance_value(self, i_distance_value: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetDistanceValue(double iDistanceValue)
                |     Set the DistanceValue of an Elementary Motion if ElementaryMotionType = Horizontal or Axial or DeltaLnDist.
                | 
                |     Parameters:
                | 
                |         iDistanceValue
                |             The distance value

        :param float i_distance_value:
        :return: None
        """
        return self.com_object.SetDistanceValue(i_distance_value)

    def set_formula_motion_plane(self, i_expression: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetFormulaMotionPlane(CATBSTR iExpression)
                |     Set a Geometrical Expression for Plane of an Elementary Motion if ElementaryMotionType = GoToAPlane.
                | 
                |     Parameters:
                | 
                |         iExpression
                |             Geometrical Expression to define.

        :param str i_expression:
        :return: None
        """
        return self.com_object.SetFormulaMotionPlane(i_expression)

    def set_formula_motion_point(self, i_expression: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetFormulaMotionPoint(CATBSTR iExpression)
                |     Set a Geometrical Expression for Point of an Elementary Motion if ElementaryMotionType = GoToAPpoint.
                | 
                |     Parameters:
                | 
                |         iExpression
                |             Geometrical Expression to define.

        :param str i_expression:
        :return: None
        """
        return self.com_object.SetFormulaMotionPoint(i_expression)

    def set_horizontal_angle_value(self, i_horizontal_angle_value: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetHorizontalAngleValue(double iHorizontalAngleValue)
                |     Set the HorizontalAngleValue of an Elementary Motion if ElementaryMotionType = Horizontal.
                | 
                |     Parameters:
                | 
                |         iHorizontalAngleValue
                |             The horizontal angle value

        :param float i_horizontal_angle_value:
        :return: None
        """
        return self.com_object.SetHorizontalAngleValue(i_horizontal_angle_value)

    def set_horizontal_safety_distance_value(self, i_horizontal_distance_value: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetHorizontalSafetyDistanceValue(double
                | iHorizontalDistanceValue)
                |     Set HorizontalSafetyDistanceValue of an Elementary Motion if ElementaryMotionType = Ramping.
                | 
                |     Parameters:
                | 
                |         iHorizontalDistanceValue
                |             The horizontal distance value

        :param float i_horizontal_distance_value:
        :return: None
        """
        return self.com_object.SetHorizontalSafetyDistanceValue(i_horizontal_distance_value)

    def set_inactive(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetInactive()
                |     Set an Elementary Motion to Inactive Status

        :return: None
        """
        return self.com_object.SetInactive()

    def set_motion_direction_vector(self, vector_x: float, vector_y: float, vector_z: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetMotionDirectionVector(double vectorX,double vectorY,double
                | vectorZ)
                |     Set DirectionVector of an Elementary Motion if ElementaryMotionType = DeltaLnDist.
                | 
                |     Parameters:
                | 
                |         iVector
                |             The direction vector

        :param float vector_x:
        :param float vector_y:
        :param float vector_z:
        :return: None
        """
        return self.com_object.SetMotionDirectionVector(vector_x, vector_y, vector_z)

    def set_motion_plane(self, i_plane: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetMotionPlane(AnyObject iPlane)
                |     Set Plane of an Elementary Motion if ElementaryMotionType = GoToAPlane.
                | 
                |     Parameters:
                | 
                |         iPlane
                |             The plane

        :param AnyObject i_plane:
        :return: None
        """
        return self.com_object.SetMotionPlane(i_plane.com_object)

    def set_motion_point(self, i_point: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetMotionPoint(AnyObject iPoint)
                |     Set Point of an Elementary Motion if ElementaryMotionType = GoToAPpoint.
                | 
                |     Parameters:
                | 
                |         iPoint
                |             The point

        :param AnyObject i_point:
        :return: None
        """
        return self.com_object.SetMotionPoint(i_point.com_object)

    def set_motion_to_plane_mode(self, i_mode: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetMotionToPlaneMode(long iMode)
                |     Set the way to move to the Plane of an Elementary Motion if ElementaryMotionType = GoToAPlane.
                | 
                |     Parameters:
                | 
                |         iMode
                | 
                |                 0:perpendicular to the plane move
                |                 1: axial move

        :param int i_mode:
        :return: None
        """
        return self.com_object.SetMotionToPlaneMode(i_mode)

    def set_motion_tool_axis(self, vector_x: float, vector_y: float, vector_z: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetMotionToolAxis(double vectorX,double vectorY,double
                | vectorZ)
                |     Set DirectionVector of an Elementary Motion if ElementaryMotionType = ToolAxis.
                | 
                |     Parameters:
                | 
                |         iVector
                |             The direction vector

        :param float vector_x:
        :param float vector_y:
        :param float vector_z:
        :return: None
        """
        return self.com_object.SetMotionToolAxis(vector_x, vector_y, vector_z)

    def set_parameter_value(self, i_name: str, i_value: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetParameterValue(CATBSTR iName,double iValue)
                |     Sets the parameter value.
                | 
                |     Parameters:
                | 
                |         iName
                |             The parameter name. Authorized values are:
                | 
                |                 MfgMacroDistance: distance
                |                 MfgMacroPositionningAngleA: vertical angle
                |                 MfgMacroPositionningAngleB: horizontal angle
                |                 MfgMacroRadius: circular radius
                |                 MfgMacroCircleAngularPositionA: circular angular
                |                 sector
                |                 MfgMacroCircleAngularPositionB: circular angular
                |                 orientation
                |                 MfgMacroRampingAngle: ramping angle
                |                 MfgMacroHorizontalSafetyDistance: ramping horizontal safety
                |                 distance
                |                 MfgMacroVerticalSafetyDistance: ramping vertical safety
                |                 distance
                | 
                |         iValue
                |             The parameter value

        :param str i_name:
        :param float i_value:
        :return: None
        """
        return self.com_object.SetParameterValue(i_name, i_value)

    def set_ramping_angle_value(self, i_ramping_angle_value: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetRampingAngleValue(double iRampingAngleValue)
                |     Set RampingAngleValue of an Elementary Motion if ElementaryMotionType = Ramping.
                | 
                |     Parameters:
                | 
                |         iRampingAngleValue
                |             The ramping angle value

        :param float i_ramping_angle_value:
        :return: None
        """
        return self.com_object.SetRampingAngleValue(i_ramping_angle_value)

    def set_spindle_speed_type(self, i_spindle_speed_type: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetSpindleSpeedType(long iSpindleSpeedType)
                |     Set the SpindleSpeedType of an Elementary Motion.
                | 
                |     Parameters:
                | 
                |         iSpindleSpeedType
                | 
                |                 (1: Machining 2:Approach, 3: Retract , 4: Rapid, 5:Local -
                |                 Undefined Spindle Speed)

        :param int i_spindle_speed_type:
        :return: None
        """
        return self.com_object.SetSpindleSpeedType(i_spindle_speed_type)

    def set_spindle_speed_value(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func SetSpindleSpeedValue() As double
                |     Set the SpindleSpeedValue of an Elementary Motion if SpindleSpeedType = Local /Undefined Spindle Speed.
                | 
                |     Parameters:
                | 
                |         iSpindle
                |             The spindle spped value

        :return: float
        """
        return self.com_object.SetSpindleSpeedValue()

    def set_vertical_angle_value(self, i_vertical_angle_value: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetVerticalAngleValue(double iVerticalAngleValue)
                |     Set the VerticalAngleValue of an Elementary Motion if ElementaryMotionType = Horizontal.
                | 
                |     Parameters:
                | 
                |         iVerticalAngleValue
                |             The vertical angle value

        :param float i_vertical_angle_value:
        :return: None
        """
        return self.com_object.SetVerticalAngleValue(i_vertical_angle_value)

    def set_vertical_safety_distance_value(self, i_vertical_distance_value: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetVerticalSafetyDistanceValue(double
                | iVerticalDistanceValue)
                |     Set VerticalSafetyDistanceValue of an Elementary Motion if ElementaryMotionType = Ramping.
                | 
                |     Parameters:
                | 
                |         iVerticalDistanceValue
                |             The vertical distance value

        :param float i_vertical_distance_value:
        :return: None
        """
        return self.com_object.SetVerticalSafetyDistanceValue(i_vertical_distance_value)

    def __repr__(self):
        return f'ManufacturingElementaryMotion(name="{ self.name }")'
