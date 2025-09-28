"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-27 14:29:47.477239

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.hybrid_shapes.hybrid_shape_direction import HybridShapeDirection
from pycatia3dx.knowledge_interfaces.length import Length
from pycatia3dx.knowledge_interfaces.real_param import RealParam
from pycatia3dx.mmr_automation_interfaces.hybrid_shape import HybridShape
from pycatia3dx.mode.reference import Reference


class HybridShapeSpline(HybridShape):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     CATMmrAutomationInterfaces.HybridShape
                |                         HybridShapeSpline
                | 
                | Represents the hybrid shape spline feature object.
                | Role: To access the data of the hybrid shape spline feature object. This data
                | includes:
                | 
                |     The support surface
                |     The control points
                |     The tension at each control point
                |     The curvature radius at each control point
                | 
                | Use the CATIAHybridShapeFactory to create a HybridShapeAffinity
                | object.
                | 
                | See also:
                |     HybridShapeFactory
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def add_point(self, ip_ia_point: Reference) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub AddPoint(Reference ipIAPoint)
                |     Add a new point .
                | 
                |     Parameters:
                | 
                |         iPoint
                |             Point element.

        :param Reference ip_ia_point:
        :return: None
        """
        return self.com_object.AddPoint(ip_ia_point.com_object)

    def add_point_with_constraint_explicit(self, ip_ia_point: Reference, ip_ia_dir_tangency: HybridShapeDirection, i_tangency_norm: float, i_inverse_tangency: int, ip_ia_dir_curvature: HybridShapeDirection, i_curvature_radius: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub AddPointWithConstraintExplicit(Reference ipIAPoint,HybridShapeDirection
                | ipIADirTangency,double iTangencyNorm,long iInverseTangency,HybridShapeDirection
                | ipIADirCurvature,double iCurvatureRadius)
                |     Add a new point with explicit tangency and curvature.
                | 
                |     Parameters:
                | 
                |         ipIAPoint
                |             Point element. 
                |         ipIADirTangency
                |             Tangent direction. 
                |         iTangencyNorm
                |             Tension. 
                |         iInverseTangency
                |             Flag to reverse tangent direction (value can be 1 or -1).
                |             
                |         ipIADirCurvature
                |             Curvature direction. 
                |         iCurvatureRadius
                |             Curvature radius value.

        :param Reference ip_ia_point:
        :param HybridShapeDirection ip_ia_dir_tangency:
        :param float i_tangency_norm:
        :param int i_inverse_tangency:
        :param HybridShapeDirection ip_ia_dir_curvature:
        :param float i_curvature_radius:
        :return: None
        """
        return self.com_object.AddPointWithConstraintExplicit(ip_ia_point.com_object, ip_ia_dir_tangency.com_object, i_tangency_norm, i_inverse_tangency, ip_ia_dir_curvature.com_object, i_curvature_radius)

    def add_point_with_constraint_from_curve(self, ip_ia_point: Reference, ip_ia_curve_cst: Reference, i_tangency_norm: float, i_invert_value: int, i_crv_cst_type: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub AddPointWithConstraintFromCurve(Reference ipIAPoint,Reference
                | ipIACurveCst,double iTangencyNorm,long iInvertValue,long
                | iCrvCstType)
                |     Add a new point with tangency/curvature from a curve.
                | 
                |     Parameters:
                | 
                |         ipIAPoint
                |             Point element. 
                |         ipIACurveCst
                |             Curvature direction. 
                |         iTangencyNorm
                |             tension factor for tangency. 
                |         iInvertValue
                |             Orientation for tangent 
                |         iCrvCstType
                |             Continuity type for Curve Constraint (1=Tangency , 2-= Curvature).

        :param Reference ip_ia_point:
        :param Reference ip_ia_curve_cst:
        :param float i_tangency_norm:
        :param int i_invert_value:
        :param int i_crv_cst_type:
        :return: None
        """
        return self.com_object.AddPointWithConstraintFromCurve(ip_ia_point.com_object, ip_ia_curve_cst.com_object, i_tangency_norm, i_invert_value, i_crv_cst_type)

    def get_closure(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Func GetClosure() As long
                |     Gets whether the curve is closed.
                | 
                |     Parameters:
                | 
                |         oClosed
                |             Closing flag
                | 
                |             1
                |                 for a closed curve
                |             0
                |                 for an open curve

        :return: int
        """
        return self.com_object.GetClosure()

    def get_constraint_type(self, i_pos: int) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Func GetConstraintType(long iPos) As long
                |     Returns the ControlPoint type at the given position.
                | 
                |     Parameters:
                | 
                |         iPos
                |             The position of the point to retrieve 
                |         oCstType
                |             Type of Control point (CstType=0 : not defined / CstType=1 : Explicit / CstType=2 : FromCurve)

        :param int i_pos:
        :return: int
        """
        return self.com_object.GetConstraintType(i_pos)

    def get_curvature_radius(self, i_pos: int) -> Length:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Func GetCurvatureRadius(long iPos) As Length
                |     Returns the curvature radius value for each point of the
                |     spline.
                | 
                |     Parameters:
                | 
                |         iPos
                |             The position of the point in the spline.
                |             Legal values: first position is 1. The position cannot be 0.
                |             
                |         oRadius
                |             The curvature radius value at this point

        :param int i_pos:
        :return: Length
        """
        return Length(self.com_object.GetCurvatureRadius(i_pos))

    def get_direction_inversion(self, i_pos: int) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Func GetDirectionInversion(long iPos) As long
                |     Gets the orientation of the tangent direction .
                | 
                |     Parameters:
                | 
                |         oInvertFlag
                |             invert flag = 1 No Inversion = -1 Invert 
                |         iPos
                |             Position of point in spline First Position is 1 Position 0 return
                |             E_FAIL

        :param int i_pos:
        :return: int
        """
        return self.com_object.GetDirectionInversion(i_pos)

    def get_nb_control_point(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Func GetNbControlPoint() As long
                |     Returns the number of control points.
                | 
                |     Parameters:
                | 
                |         oNbCtrPt
                |             The number of control points.

        :return: int
        """
        return self.com_object.GetNbControlPoint()

    def get_point(self, i_pos: int) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Func GetPoint(long iPos) As Reference
                |     Returns the Point at the given position.
                | 
                |     Parameters:
                | 
                |         iPos
                |             The position of the point to retrieve 
                |         opIAPoint
                |             Type of Control point (TypeCtrPoint =1 : Explicit / TypeCtrPoint =2 : FromCurve)

        :param int i_pos:
        :return: Reference
        """
        return Reference(self.com_object.GetPoint(i_pos))

    def get_point_constraint_explicit(self, i_pos: int, op_ia_dir_tangency: HybridShapeDirection, o_tangency_norm: float, o_inverse_tangency: int, op_ia_dir_curvature: HybridShapeDirection, o_curvature_radius: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub GetPointConstraintExplicit(long iPos,HybridShapeDirection
                | opIADirTangency,double oTangencyNorm,long oInverseTangency,HybridShapeDirection
                | opIADirCurvature,double oCurvatureRadius)
                |     Returns the Constraint of the point at iPos.
                |     Available for Explicit Point Constraint type (CstType =1 from
                |     GetContraintType)
                | 
                |     Parameters:
                | 
                |         iPos
                |             The position of the point to retrieve 
                |         opIADirTangency
                |             Tangent direction. 
                |         oTangencyNorm
                |             Tension. 
                |         oInverseTangency
                |             Flag to reverse tangent direction (value can be 1 or -1).
                |             
                |         opIADirCurvature
                |             Curvature direction. 
                |         oCurvatureRadius
                |             Curvature radius value.

        :param int i_pos:
        :param HybridShapeDirection op_ia_dir_tangency:
        :param float o_tangency_norm:
        :param int o_inverse_tangency:
        :param HybridShapeDirection op_ia_dir_curvature:
        :param float o_curvature_radius:
        :return: None
        """
        return self.com_object.GetPointConstraintExplicit(i_pos, op_ia_dir_tangency.com_object, o_tangency_norm, o_inverse_tangency, op_ia_dir_curvature.com_object, o_curvature_radius)

    def get_point_constraint_from_curve(self, i_pos: int, op_ia_curve_cst: Reference, o_tangency_norm: float, o_invert_value: int, o_crv_cst_type: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub GetPointConstraintFromCurve(long iPos,Reference opIACurveCst,double
                | oTangencyNorm,long oInvertValue,long oCrvCstType)
                |     Returns the Constraint of the point at iPos.
                |     Available for FromCurve Point Constraint type (CstType =2 from
                |     GetContraintType)
                | 
                |     Parameters:
                | 
                |         iPos
                |             The position of the point to retrieve 
                |         opIACurveCst
                |             Curvature direction. 
                |         oTangencyNorm
                |             tension factor for tangency. 
                |         oInvertValue
                |             Orientation for tangent 
                |         oCrvCstType
                |             Continuity type for Curve Constraint (1=Tangency , 2-= Curvature).

        :param int i_pos:
        :param Reference op_ia_curve_cst:
        :param float o_tangency_norm:
        :param int o_invert_value:
        :param int o_crv_cst_type:
        :return: None
        """
        return self.com_object.GetPointConstraintFromCurve(i_pos, op_ia_curve_cst.com_object, o_tangency_norm, o_invert_value, o_crv_cst_type)

    def get_point_position(self, ip_ia_point: Reference) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Func GetPointPosition(Reference ipIAPoint) As long
                |     Returns the position of a given point.
                | 
                |     Parameters:
                | 
                |         ipIAPoint
                |             Point 
                |         oPos
                |             The position of the point (=0 Point Not in Spline)

        :param Reference ip_ia_point:
        :return: int
        """
        return self.com_object.GetPointPosition(ip_ia_point.com_object)

    def get_spline_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Func GetSplineType() As long
                |     Gets the spline type.
                | 
                |     Parameters:
                | 
                |         oType
                |             = 0 : Cubic Type Spline. = 1 : WilsonFowler Type Spline.

        :return: int
        """
        return self.com_object.GetSplineType()

    def get_support(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Func GetSupport() As Reference
                |     Gets the support surface.
                | 
                |     Parameters:
                | 
                |         oSupport
                |             Supporting surface for spline (if exist)

        :return: Reference
        """
        return Reference(self.com_object.GetSupport())

    def get_tangent_norm(self, i_pos: int) -> RealParam:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Func GetTangentNorm(long iPos) As RealParam
                |     Returns the tension for each point of the spline.
                |     The tension is the tangent norm at the given point.
                | 
                |     Parameters:
                | 
                |         iPos
                |             The position of the point in the spline.
                |             Legal values: first position is 1. The position cannot be 0.
                |             
                |         oTension
                |             The tension at this point

        :param int i_pos:
        :return: RealParam
        """
        return RealParam(self.com_object.GetTangentNorm(i_pos))

    def invert_direction(self, i_pos: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub InvertDirection(long iPos)
                |     Inverts the orientation of the tangent direction .
                | 
                |     Parameters:
                | 
                |         iPos
                |             Position of point in spline First Position is 1 Position 0 return
                |             E_FAIL

        :param int i_pos:
        :return: None
        """
        return self.com_object.InvertDirection(i_pos)

    def remove_all(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub RemoveAll()
                |     Removes all elements in the list of points.

        :return: None
        """
        return self.com_object.RemoveAll()

    def remove_control_point(self, i_pos: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub RemoveControlPoint(long iPos)
                |     Removes a point at the given position.
                | 
                |     Parameters:
                | 
                |         iPos
                |             The position of the point to remove

        :param int i_pos:
        :return: None
        """
        return self.com_object.RemoveControlPoint(i_pos)

    def remove_curvature_radius_direction(self, i_pos: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub RemoveCurvatureRadiusDirection(long iPos)
                |     Removes Curvature Radius Direction for the given point of the
                |     spline.
                | 
                |     Parameters:
                | 
                |         iPos
                |             Position of point in spline First Position is 1 Position 0 return
                |             E_FAIL

        :param int i_pos:
        :return: None
        """
        return self.com_object.RemoveCurvatureRadiusDirection(i_pos)

    def remove_curvature_radius_value(self, i_pos: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub RemoveCurvatureRadiusValue(long iPos)
                |     Removes Curvature Radius Value for the given point of the
                |     spline.
                | 
                |     Parameters:
                | 
                |         iPos
                |             Position of point in spline First Position is 1 Position 0 return
                |             E_FAIL

        :param int i_pos:
        :return: None
        """
        return self.com_object.RemoveCurvatureRadiusValue(i_pos)

    def remove_support(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub RemoveSupport()
                |     Removes the support surface.

        :return: None
        """
        return self.com_object.RemoveSupport()

    def remove_tangent_direction(self, i_pos: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub RemoveTangentDirection(long iPos)
                |     Removes tangent Direction for the given point of the
                |     spline.
                | 
                |     Parameters:
                | 
                |         iPos
                |             Position of point in spline First Position is 1 Position 0 return
                |             E_FAIL

        :param int i_pos:
        :return: None
        """
        return self.com_object.RemoveTangentDirection(i_pos)

    def remove_tension(self, i_pos: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub RemoveTension(long iPos)
                |     Removes the Tension for the given point of the spline.
                | 
                |     Parameters:
                | 
                |         iPos
                |             Position of point in spline First Position is 1 Position 0 return
                |             E_FAIL

        :param int i_pos:
        :return: None
        """
        return self.com_object.RemoveTension(i_pos)

    def replace_point_at_position(self, i_pos: int, i_point: Reference) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub ReplacePointAtPosition(long iPos,Reference iPoint)
                |     Replaces a point in the list at the given position.
                | 
                |     Parameters:
                | 
                |         oPoint
                |             Point 
                |         iPos
                |             Replace position

        :param int i_pos:
        :param Reference i_point:
        :return: None
        """
        return self.com_object.ReplacePointAtPosition(i_pos, i_point.com_object)

    def set_closing(self, i_closing_type: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub SetClosing(long iClosingType)
                |     Activates the closing option of the spline.
                | 
                |     Parameters:
                | 
                |         iClosingType
                |             The spline closing option

        :param int i_closing_type:
        :return: None
        """
        return self.com_object.SetClosing(i_closing_type)

    def set_point_after(self, i_pos: int, ip_ia_point: Reference) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub SetPointAfter(long iPos,Reference ipIAPoint)
                |     Sets the Point After a given position.
                | 
                |     Parameters:
                | 
                |         iPos
                |             The position reference (0 < position < Nbpt) 
                |         ipIAPoint
                |             Point

        :param int i_pos:
        :param Reference ip_ia_point:
        :return: None
        """
        return self.com_object.SetPointAfter(i_pos, ip_ia_point.com_object)

    def set_point_before(self, i_pos: int, ip_ia_point: Reference) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub SetPointBefore(long iPos,Reference ipIAPoint)
                |     Sets the Point Before a given position.
                | 
                |     Parameters:
                | 
                |         iPos
                |             The position reference (1 < position < Nbpt+1) 
                |         ipIAPoint
                |             Point

        :param int i_pos:
        :param Reference ip_ia_point:
        :return: None
        """
        return self.com_object.SetPointBefore(i_pos, ip_ia_point.com_object)

    def set_point_constraint_explicit(self, i_pos: int, ip_ia_dir_tangency: HybridShapeDirection, i_tangency_norm: float, i_inverse_tangency: int, ip_ia_dir_curvature: HybridShapeDirection, i_curvature_radius: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub SetPointConstraintExplicit(long iPos,HybridShapeDirection
                | ipIADirTangency,double iTangencyNorm,long iInverseTangency,HybridShapeDirection
                | ipIADirCurvature,double iCurvatureRadius)
                |     Sets the Constraint of the point at iPos.
                |     Available for Explicit Point Constraint type (CstType =1 from
                |     GetContraintType)
                | 
                |     Parameters:
                | 
                |         iPos
                |             The position of the point to retrieve 
                |         ipIADirTangency
                |             Tangent direction. 
                |         iTangencyNorm
                |             Tension. 
                |         iInverseTangency
                |             Flag to reverse tangent direction (value can be 1 or -1).
                |             
                |         ipIADirCurvature
                |             Curvature direction. 
                |         iCurvatureRadius
                |             Curvature radius value.

        :param int i_pos:
        :param HybridShapeDirection ip_ia_dir_tangency:
        :param float i_tangency_norm:
        :param int i_inverse_tangency:
        :param HybridShapeDirection ip_ia_dir_curvature:
        :param float i_curvature_radius:
        :return: None
        """
        return self.com_object.SetPointConstraintExplicit(i_pos, ip_ia_dir_tangency.com_object, i_tangency_norm, i_inverse_tangency, ip_ia_dir_curvature.com_object, i_curvature_radius)

    def set_point_constraint_from_curve(self, i_pos: int, ip_ia_curve_cst: Reference, i_tangency_norm: float, i_invert_value: int, i_crv_cst_type: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub SetPointConstraintFromCurve(long iPos,Reference ipIACurveCst,double
                | iTangencyNorm,long iInvertValue,long iCrvCstType)
                |     Sets the Constraint of the point at iPos.
                |     Available for From Curve Point Constraint type (CstType =2 from
                |     GetContraintType)
                | 
                |     Parameters:
                | 
                |         iPos
                |             The position of the point to retrieve 
                |         ipIACurveCst
                |             Curvature direction. 
                |         iTangencyNorm
                |             tension factor for tangency. 
                |         iInvertValue
                |             Orientation for tangent 
                |         iCrvCstType
                |             Continuity type for Curve Constraint (1=Tangency , 2-= Curvature).

        :param int i_pos:
        :param Reference ip_ia_curve_cst:
        :param float i_tangency_norm:
        :param int i_invert_value:
        :param int i_crv_cst_type:
        :return: None
        """
        return self.com_object.SetPointConstraintFromCurve(i_pos, ip_ia_curve_cst.com_object, i_tangency_norm, i_invert_value, i_crv_cst_type)

    def set_spline_type(self, i_spline_type: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub SetSplineType(long iSplineType)
                |     Sets the spline type.
                | 
                |     Parameters:
                | 
                |         iSplineType
                |             The spline type
                |             Legal values: Cubic spline (0) or WilsonFowler (1)

        :param int i_spline_type:
        :return: None
        """
        return self.com_object.SetSplineType(i_spline_type)

    def set_support(self, i_support: Reference) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub SetSupport(Reference iSupport)
                |     Sets the spline support surface.
                |     Have your "tangent direction" tangent to this support is
                |     recommended.
                | 
                |     Parameters:
                | 
                |         iSupport
                |             The spline support surface.
                |             Sub-element(s) supported (see Boundary object): Face.

        :param Reference i_support:
        :return: None
        """
        return self.com_object.SetSupport(i_support.com_object)

    def __repr__(self):
        return f'HybridShapeSpline(name="{ self.name }")'
