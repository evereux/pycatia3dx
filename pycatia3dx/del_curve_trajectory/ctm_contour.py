"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class CtmContour(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     CtmContour
                | 
                | Interface representing a Contour.
                | 
                | Role: This interface is used to create a sampler, orienter, and to get and set
                | attributes for contour parameters.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def base_offset(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property BaseOffset() As double
                |     Returns or sets the curve offset from the base surface. The curve can be
                |     offset from the selected geometry with this parameter. The base offset raises
                |     the curve off the base surface and is positive along the base surface
                |     normal.
                | 
                |     Parameters:
                | 
                |         BaseOffset
                |             The base offset - in mm. 
                | 
                |     Returns:
                |         The Base offset

        :return: float
        """

        return self.com_object.BaseOffset

    @base_offset.setter
    def base_offset(self, value: float):
        """
        :param float value:
        """

        self.com_object.BaseOffset = value

    @property
    def base_orientation(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property BaseOrientation() As boolean
                |     Returns or sets the orientation of the base surface. The normal to some
                |     surfaces may be pointing into the product or just in the wrong direction. If
                |     true, it reverses the normal direction.
                | 
                |     Parameters:
                | 
                |         oIsFlipped
                |             The orientation. TRUE means that the orientation of the underlying
                |             geometry will be flipped. FALSE means that the orientation of the underlying
                |             geometry will be used.

        :return: bool
        """

        return self.com_object.BaseOrientation

    @base_orientation.setter
    def base_orientation(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.BaseOrientation = value

    @property
    def break_angle(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property BreakAngle() As double
                |     Returns or sets stored contour break angle. The curve contour is being
                |     generated with certain value of Break Angle. To reproduce the original contour
                |     wire breakage the angle value should be used.
                | 
                |     Parameters:
                | 
                |         oBreakAngle
                |             The break angle in Radians.

        :return: float
        """

        return self.com_object.BreakAngle

    @break_angle.setter
    def break_angle(self, value: float):
        """
        :param float value:
        """

        self.com_object.BreakAngle = value

    @property
    def closure_param(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ClosureParam() As double
                |     Returns or sets the Param on a closed wire that defined the start and end
                |     point.
                | 
                |     Parameters:
                | 
                |         oStart
                |             The closure point param in relation to the input wire.

        :return: float
        """

        return self.com_object.ClosureParam

    @closure_param.setter
    def closure_param(self, value: float):
        """
        :param float value:
        """

        self.com_object.ClosureParam = value

    @property
    def contour_inverted(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ContourInverted(boolean iIsInverted) (Write Only)
                |     Set the orientation parameter used by this contour. A contour has a
                |     direction which detemines the order of the generated points. The direction with
                |     respect to the underlying geometry can be reversed by setting the orientation
                |     to TRUE.
                | 
                |     Parameters:
                | 
                |         iIsInverted
                |             The orientation parameter. TRUE means that the orientation with
                |             underlying geometry will be reversed. FALSE means that the orientation of the
                |             underlying geometry will be used.

        :return: bool
        """

        return self.com_object.ContourInverted

    @contour_inverted.setter
    def contour_inverted(self, value: bool):
        """
        :param False value:
        """

        self.com_object.ContourInverted = value

    @property
    def gap_tolerance(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property GapTolerance() As double
                |     Returns or sets stored contour Gap tolerance. The curve contour is being
                |     generated with certain value of Gap tolerance.
                | 
                |     Parameters:
                | 
                |         oGapTolerance
                |             The Gap tolerance in mm.

        :return: float
        """

        return self.com_object.GapTolerance

    @gap_tolerance.setter
    def gap_tolerance(self, value: float):
        """
        :param float value:
        """

        self.com_object.GapTolerance = value

    @property
    def wall_offset(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property WallOffset() As double
                |     Returns or sets the curve offset from the wall surface. The curve can be
                |     offset from the selected geometry with this parameter. The wall offset moves
                |     the curve out from the wall surface.
                | 
                |     Parameters:
                | 
                |         iWallOffset
                |             The wall offset - in mm.

        :return: float
        """

        return self.com_object.WallOffset

    @wall_offset.setter
    def wall_offset(self, value: float):
        """
        :param float value:
        """

        self.com_object.WallOffset = value

    @property
    def wall_orientation(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property WallOrientation() As boolean
                |     Get the orientation of the wall surface. The normal to some surfaces may be
                |     pointing into the product or just in the wrong direction. If true, it reverses
                |     the normal direction.
                | 
                |     Parameters:
                | 
                |         oIsFlipped
                |             The orientation. TRUE means that the orientation of the underlying
                |             geometry will be flipped. FALSE means that the orientation of the underlying
                |             geometry will be used.

        :return: bool
        """

        return self.com_object.WallOrientation

    @wall_orientation.setter
    def wall_orientation(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.WallOrientation = value

    def create_orienter_ypr(self, osp_orienter: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub CreateOrienterYPR(AnyObject ospOrienter)
                |     Create a new default orienter. The new orienter will replace the existing
                |     sampler.
                | 
                |     See also:
                |         CtmCurveOrienter
                |     Parameters:
                | 
                |         ospOrienter
                |             The new orienter. 
                | 
                |     Returns:
                |         The created orienter 
                |     Example:
                | 
                |          Dim objContour As CtmContour
                |                ........
                |          Dim objCurveOrienter As CtmCurveOrienter
                |          Call objContour.CreateOrienterYPR(objCurveOrienter)

        :param AnyObject osp_orienter:
        :return: None
        """
        return self.com_object.CreateOrienterYPR(osp_orienter.com_object)

    def create_sampler_fixed_distance(self, osp_sampler: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub CreateSamplerFixedDistance(AnyObject ospSampler)
                |     Create a new fixed distance sampler. The new sampler will replace the
                |     existing sampler.
                | 
                |     See also:
                |         CtmCurveSamplerDistance
                |     Parameters:
                | 
                |         ospSampler
                |             The new sampler. 
                | 
                |     Returns:
                |         A fixed speed sampler 
                |     Example:
                | 
                |          Dim objContour As CtmContour
                |                ........
                |          Dim objDistanceSampler As CtmCurveSamplerDistance
                |          Call
objContour.CreateSamplerFixedDistance(objDistanceSampler)

        :param AnyObject osp_sampler:
        :return: None
        """
        return self.com_object.CreateSamplerFixedDistance(osp_sampler.com_object)

    def create_sampler_fixed_number(self, osp_sampler: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub CreateSamplerFixedNumber(AnyObject ospSampler)
                |     Create a new fixed number of samples sampler. The new sampler will replace
                |     the existing sampler.
                | 
                |     See also:
                |         CtmCurveSamplerNumber
                |     Parameters:
                | 
                |         ospSampler
                |             The new sampler. 
                | 
                |     Returns:
                |         A fixed number sampler 
                |     Example:
                | 
                |          Dim objContour As CtmContour
                |                ........
                |          Dim objNumberSampler As CtmCurveSamplerNumber
                |          Call
                |          objContour.CreateSamplerFixedNumber(objNumberSampler)

        :param AnyObject osp_sampler:
        :return: None
        """
        return self.com_object.CreateSamplerFixedNumber(osp_sampler.com_object)

    def create_sampler_fixed_speed(self, osp_sampler: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub CreateSamplerFixedSpeed(AnyObject ospSampler)
                |     Create a new fixed speed sampler. The new sampler will replace the existing
                |     sampler.
                | 
                |     See also:
                |         CtmCurveSamplerSpeed
                |     Parameters:
                | 
                |         ospSampler
                |             The new sampler. 
                | 
                |     Returns:
                |         A fixed speed sampler 
                |     Example:
                | 
                |          Dim objContour As CtmContour
                |                ........
                |          Dim objSpeedSampler As CtmCurveSamplerSpeed
                |          Call
                |          objContour.CreateSamplerFixedSpeed(objSpeedSampler)

        :param AnyObject osp_sampler:
        :return: None
        """
        return self.com_object.CreateSamplerFixedSpeed(osp_sampler.com_object)

    def get_base_list(self, o_base_list: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetBaseList(CATSafeArrayVariant oBaseList)
                |     Get the base surfaces used in the intersection.
                | 
                |     Parameters:
                | 
                |         oBaseSO
                |             The paths to the base surfaces. Pass in valid SO. Empty after
                |             usage. 
                | 
                |     Returns:
                |         An HRESULT value.
                |         Legal values:
                | 
                |         S_OK
                |             The bases were returned succefully.
                |         E_UNEXPECTED
                |             An unexpected error occured.

        :param tuple o_base_list:
        :return: None
        """
        return self.com_object.GetBaseList(o_base_list)

    def get_orienter(self, osp_orienter: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetOrienter(AnyObject ospOrienter)
                |     Get the orienter object. If no orienter has been created yet, then the
                |     orienter will be set to NULL_var but the return value will be
                |     S_OK.
                | 
                |     See also:
                |         CtmCurveOrienter
                |     Parameters:
                | 
                |         ospOrienter
                |             The orienter. 
                |         Example:
                | 
                |              Dim objContour As CtmContour
                |                    ........
                |              Dim objOrienter As CtmCurveOrienter
                |              Call objContour.GetOrienter(objOrienter)

        :param AnyObject osp_orienter:
        :return: None
        """
        return self.com_object.GetOrienter(osp_orienter.com_object)

    def get_referenced_parts(self, olsp_parts_bu: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetReferencedParts(CATSafeArrayVariant olspPartsBU)
                |     Get the list of Parts which contain the reference geometry
                | 
                |     Parameters:
                | 
                |         olspPartsBU
                |             The list of parts. 
                | 
                |     Returns:
                |         An HRESULT value.
                |         Legal values:
                | 
                |         S_OK
                |             The list is filled.
                |         E_UNEXPECTED
                |             An unexpected error occured.

        :param tuple olsp_parts_bu:
        :return: None
        """
        return self.com_object.GetReferencedParts(olsp_parts_bu)

    def get_sampler(self, osp_sampler: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetSampler(AnyObject ospSampler)
                |     Get the sampler object. If no sampler has been created yet, then the
                |     sampler will be set to NULL_var but the return value will be
                |     S_OK.
                | 
                |     See also:
                |         CtmCurveSampler
                |     Parameters:
                | 
                |         ospSampler
                |             The sampler. 
                | 
                |     Returns:
                |         Retrieves the sampler object. 
                |     Example:
                | 
                |          Dim objContour As CtmContour
                |                ........
                |          Dim objSampler As CtmCurveSampler
                |          Call objContour.GetSampler(objSampler)

        :param AnyObject osp_sampler:
        :return: None
        """
        return self.com_object.GetSampler(osp_sampler.com_object)

    def get_start_and_end_point(self, o_start: float, o_end: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetStartAndEndPoint(double oStart,double oEnd)
                |     Get the start and end points of the curve. A selected or generated curve
                |     may be longer than the desired path. Limits of the curve can be adjusted with
                |     these parameters. The values represent the proportion of the curve to the
                |     point. For example to have the start point be 1/4 of the way through the curve,
                |     set iStart=0.25. Start is always less than or equal to end. You whould check
                |     IsContourInverted to see if you want the curve direction
                |     reversed.
                | 
                |     Parameters:
                | 
                |         oStart
                |             The start point as a proportion of the total curve length.
                |             
                |         oEnd
                |             The end point as a proportion of the total curve length.
                |             
                | 
                |     Returns:
                |         The Start and End point. 
                |     Example:
                | 
                |          Dim objContour As CtmContour
                |                ........
                |          Dim oStart As Double
                |          Dim oEnd As Double
                |          Call objContour.GetStartAndEndPoint(oStart, oEnd)

        :param float o_start:
        :param float o_end:
        :return: None
        """
        return self.com_object.GetStartAndEndPoint(o_start, o_end)

    def get_wall_list(self, o_wall_bu: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetWallList(CATSafeArrayVariant oWallBU)
                |     Get the wall surfaces used in the intersection.
                | 
                |     Parameters:
                | 
                |         oWallSO
                |             The paths to the wall surfaces. Pass in valid SO. Empty after
                |             usage. 
                | 
                |     Returns:
                |         An HRESULT value.
                |         Legal values:
                | 
                |         S_OK
                |             The walls were returned succefully.
                |         E_UNEXPECTED
                |             An unexpected error occured.

        :param tuple o_wall_bu:
        :return: None
        """
        return self.com_object.GetWallList(o_wall_bu)

    def is_contour_inverted(self, o_is_inverted: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub IsContourInverted(boolean oIsInverted)
                |     Get the orientation parameter used by this contour. A contour has a
                |     direction which detemines the order of the generated points. The direction with
                |     respect to the underlying geometry can be reversed by setting the orientation
                |     to TRUE.
                | 
                |     Parameters:
                | 
                |         oIsInverted
                |             The orientation parameter. TRUE means that the orientation with the
                |             underlying geometry will be reversed. FALSE means that the orientation of the
                |             underlying geometry will be used. 
                |         Example:
                | 
                |              Dim objContour As CtmContour
                |                    ........
                |              Dim oBool As boolean
                |              Call objContour.IsContourInverted(oBool)

        :param bool o_is_inverted:
        :return: None
        """
        return self.com_object.IsContourInverted(o_is_inverted)

    def set_base_list(self, i_base_list: tuple, i_base_prod: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetBaseList(CATSafeArrayVariant iBaseList,CATSafeArrayVariant
                | iBaseProd)
                |     Set the base surfaces used in the intersection. The base surfaces are also
                |     used to define the product this contour is attached to.
                | 
                |     Parameters:
                | 
                |         iBaseList
                |             The paths to the base surfaces. 
                |         iBaseProd
                |             Base surface Product

        :param tuple i_base_list:
        :param tuple i_base_prod:
        :return: None
        """
        return self.com_object.SetBaseList(i_base_list, i_base_prod)

    def set_start_and_end_point(self, i_start: float, i_end: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetStartAndEndPoint(double iStart,double iEnd)
                |     Set the start and end points of the curve. A selected or generated curve
                |     may be longer than the desired path. Limits of the curve can be adjusted with
                |     these parameters. The values represent the proportion of the curve to the
                |     point. For example to have the start point be 1/4 of the way through the curve,
                |     set iStart=0.25. Start is always less than or equal to end. If you want to
                |     reverse the direction of the curve see the SetContourInverted funtion
                |     above.
                | 
                |     Parameters:
                | 
                |         iStart
                |             The start point as a proportion of the total curve length.
                |             
                |         iEnd
                |             The end point as a proportion of the total curve length.
                |             
                |         Example:
                | 
                |              Dim objContour As CtmContour
                |                    ........
                |              Call objContour.SetStartAndEndPoint(0.25, 0.50)

        :param float i_start:
        :param float i_end:
        :return: None
        """
        return self.com_object.SetStartAndEndPoint(i_start, i_end)

    def set_wall_list(self, i_wall_list: tuple, i_wall_prod: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetWallList(CATSafeArrayVariant iWallList,CATSafeArrayVariant
                | iWallProd)
                |     Set the wall surfaces used in the intersection. The wall surfaces are also
                |     used to define the product this contour is attached to.
                | 
                |     Parameters:
                | 
                |         iWallList
                |             The paths to the wall surfaces. 
                |         iWallProd
                |             Wall surface product 

        :param tuple i_wall_list:
        :param tuple i_wall_prod:
        :return: None
        """
        return self.com_object.SetWallList(i_wall_list, i_wall_prod)

    def __repr__(self):
        return f'CtmContour(name="{ self.name }")'
