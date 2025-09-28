"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-27 14:29:47.477239

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.hybrid_shapes.hybrid_shape_direction import HybridShapeDirection
from pycatia3dx.mmr_automation_interfaces.hybrid_shape import HybridShape
from pycatia3dx.mode.reference import Reference


class HybridShapeProject(HybridShape):

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
                |                         HybridShapeProject
                | 
                | Represents the hybrid shape project feature object.
                | Role: To access data of the hybrid shape project feature. The data
                | includes:
                | 
                |     The element to project which is a point or a curve
                |     The support element which is a curve or a surface
                |     The projection type ( normal or along a direction)
                |     The projection direction if needed
                |     The option to have either the nearest solution or all
                |     solutions
                | 
                | Use the CATIAHybridShapeFactory to create HybridShapeFeatures
                | objects.
                | 
                | See also:
                |     HybridShapeFactory
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def direction(self) -> HybridShapeDirection:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property Direction() As HybridShapeDirection
                |     Returns or sets the projection direction.
                | 
                |     Example: This example retrieves in Dir the direction for the Project hybrid
                |     shape feature.
                | 
                |      Dim Dir As Reference
                |      Set Dir = Project.Direction

        :return: HybridShapeDirection
        """

        return HybridShapeDirection(self.com_object.Direction)

    @direction.setter
    def direction(self, value: HybridShapeDirection):
        """
        :param HybridShapeDirection value:
        """

        self.com_object.Direction = value

    @property
    def elem_to_project(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property ElemToProject() As Reference
                |     Returns or sets the element to project.This element can be a point or a
                |     curve.
                |     Sub-element(s) supported (see Boundary object): TriDimFeatEdge,
                |     BiDimFeatEdge or Vertex.
                | 
                |     Example: This example retrieves in Elem the element to project for the
                |     Project hybrid shape feature.
                | 
                |      Dim Elem As Reference
                |      Set Elem = Project.ElemToProject

        :return: Reference
        """

        return Reference(self.com_object.ElemToProject)

    @elem_to_project.setter
    def elem_to_project(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.ElemToProject = value

    @property
    def extrapolation_mode(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property ExtrapolationMode() As long
                |     Returns or sets the extrapolation mode. The extrapolation mode is overriden
                |     when the solution type is 'Nearest solution' (0) or when the extrapolation mode
                |     being set is 'None' (0), otherwise the method fails. Role: None (0), Tangency
                |     (1) or Curvature (2).
                | 
                |     Example: This example retrieves in ExtrapolMode the solution type for the
                |     Project hybrid shape feature.
                | 
                |      Dim ExtrapolMode As long
                |      Set ExtrapolMode = Project.ExtrapolationMode

        :return: int
        """

        return self.com_object.ExtrapolationMode

    @extrapolation_mode.setter
    def extrapolation_mode(self, value: int):
        """
        :param int value:
        """

        self.com_object.ExtrapolationMode = value

    @property
    def maximum_deviation_value(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property MaximumDeviationValue() As double
                |     Sets or Gets the maximum deviation allowed for smoothing
                |     operation.
                |     Sets in distance unit, it corresponds to the radius of a pipe around the
                |     input curve in which the result is allowed to be. This value must be set in SI
                |     unit (m).
                | 
                |     Example: This example retrieves in DeviationValue the maximum deviation
                |     value for the Project hybrid shape feature.
                | 
                |      Dim DeviationValue As CATIALength
                |      Set DeviationValue = Project.MaximumDeviationValue

        :return: float
        """

        return self.com_object.MaximumDeviationValue

    @maximum_deviation_value.setter
    def maximum_deviation_value(self, value: float):
        """
        :param float value:
        """

        self.com_object.MaximumDeviationValue = value

    @property
    def normal(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property Normal() As boolean
                |     Returns or sets the direction option. Role: To define the type of
                |     projection. Normal is set to TRUE if the projection is a normal
                |     projection.Otherwise, the projection is defined along a specified
                |     direction.
                | 
                |     Example: This example retrieves in NormalOption the support for the Project
                |     hybrid shape feature.
                | 
                |      Dim NormalOption As boolean
                |      Set NormalOption = Project.Normal

        :return: bool
        """

        return self.com_object.Normal

    @normal.setter
    def normal(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.Normal = value

    @property
    def smoothing_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property SmoothingType() As long
                |     Sets or Gets Smoothing Type.
                |     Role: Smoothing type
                |     : 0 -> No Smoothing
                |     : 2 -> G1 Smoothing : Enhance current continuity to tangent continuity
                |     : 3 -> G2 Smoothing : Enhance current continuity to curvature continuity
                | 
                |     Example: This example retrieves in SType the smoothing type for the Project
                |     hybrid shape feature.
                | 
                |      Dim SType As long
                |      Set SType = Project.SmoothingType

        :return: int
        """

        return self.com_object.SmoothingType

    @smoothing_type.setter
    def smoothing_type(self, value: int):
        """
        :param int value:
        """

        self.com_object.SmoothingType = value

    @property
    def solution_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property SolutionType() As long
                |     Returns or sets the solution type. When the solution type being set is 'All
                |     solutions' (1), the extrapolation mode gets overriden to 'None' (0). Role: All
                |     solutions (1) or Nearest solution (0) (only nearest projection is kept when
                |     more than one solution is possible).
                | 
                |     Example: This example retrieves in SolType the solution type for the
                |     Project hybrid shape feature.
                | 
                |      Dim SolType As long
                |      Set SolType = Project.SolutionType

        :return: int
        """

        return self.com_object.SolutionType

    @solution_type.setter
    def solution_type(self, value: int):
        """
        :param int value:
        """

        self.com_object.SolutionType = value

    @property
    def support(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property Support() As Reference
                |     Returns or sets the support element.This element can be a plane or a
                |     surface.
                |     Sub-element(s) supported (see Boundary object): Face, TriDimFeatEdge or
                |     BiDimFeatEdge.
                | 
                |     Example: This example retrieves in SupportElem the support for the Project
                |     hybrid shape feature.
                | 
                |      Dim SupportElem As Reference
                |      Set SupportElem = Project.Support

        :return: Reference
        """

        return Reference(self.com_object.Support)

    @support.setter
    def support(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.Support = value

    @property
    def p_3d_smoothing(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property p3DSmoothing() As boolean
                |     Returns or sets the '3D Smoothing' option. Role: To activate or not the 3D smoothing option Available only for tangent or curvature smoothing type TRUE : Smoothing performed without specifying support FALSE : Smoothing performed with specific support
                | 
                |     Example: This example retrieves in 3DSmoothingOption the support for the
                |     Project hybrid shape feature.
                | 
                |      Dim 3DSmoothingOption As boolean
                |      Set 3DSmoothingOption = Project.p3DSmoothing

        :return: bool
        """

        return self.com_object.p3DSmoothing

    @p_3d_smoothing.setter
    def p_3d_smoothing(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.p3DSmoothing = value

    def __repr__(self):
        return f'HybridShapeProject(name="{ self.name }")'
