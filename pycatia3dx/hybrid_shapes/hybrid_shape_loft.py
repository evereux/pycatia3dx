"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-27 14:29:47.477239

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.knowledge_interfaces.length import Length
from pycatia3dx.mmr_automation_interfaces.hybrid_shape import HybridShape
from pycatia3dx.mode.reference import Reference


class HybridShapeLoft(HybridShape):

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
                |                         HybridShapeLoft
                | 
                | Represents the hybrid shape loft surface feature object.
                | Role: To access the data of the hybrid shape loft surface feature
                | object.
                | This data includes:
                | 
                |     The spine
                |     The tangent surfaces to the start and end sections
                |     Guide curves, sections, and couplings
                | 
                | Use the CATIAHybridShapeFactory to create a HybridShapeLoft
                | object.
                | 
                | LICENSING INFORMATION: Creation of volume result requires GSO
                | License
                | if GSO License is not granted , setting of Volume context has not
                | effect
                | 
                | Use the CATIAHybridShapeFactory to create a HybridShapeLoft
                | object.
                | 
                | See also:
                |     HybridShapeFactory
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def area_law(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property AreaLaw() As Reference
                |     Gets or sets the optional area law for multi-sections element definition.
                |     The law is a length law.

        :return: Reference
        """

        return Reference(self.com_object.AreaLaw)

    @area_law.setter
    def area_law(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.AreaLaw = value

    @property
    def area_law_tolerance(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property AreaLawTolerance() As double
                |     Gets or sets the tolerance applied to area law. The value is in mm.

        :return: float
        """

        return self.com_object.AreaLawTolerance

    @area_law_tolerance.setter
    def area_law_tolerance(self, value: float):
        """
        :param float value:
        """

        self.com_object.AreaLawTolerance = value

    @property
    def boolean_operation(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property BooleanOperation() As long
                |     Gets or sets the boolean operation for closed lofted surface. TO BE USED ONLY for Part Loft (closed loft). BooleanOperation = 1 : No boolean operation. = 2 : Union boolean operation. = 3 : Removal boolean operation. This example retrieves in BoolOp the type of boolean operation for the Loft hybrid shape feature.
                | 
                |      Dim BoolOp
                |      BoolOp = Loft.BooleanOperation

        :return: int
        """

        return self.com_object.BooleanOperation

    @boolean_operation.setter
    def boolean_operation(self, value: int):
        """
        :param int value:
        """

        self.com_object.BooleanOperation = value

    @property
    def canonical_detection(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property CanonicalDetection() As long
                |     Returns or sets whether canonical surfaces of the lofted surface are
                |     detected.
                |     Legal values:
                | 
                |     0
                |         No detection of canonical surface is performed
                |     1
                |         Detection of planar surfaces only is performed
                |     2
                |         Detection of canonical surfaces is performed

        :return: int
        """

        return self.com_object.CanonicalDetection

    @canonical_detection.setter
    def canonical_detection(self, value: int):
        """
        :param int value:
        """

        self.com_object.CanonicalDetection = value

    @property
    def comp_end_section_tangent(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property CompEndSectionTangent() As long
                |     Returns or sets whether the tangent surface to the end section of the
                |     lofted surface is computed.
                |     Legal values:
                | 
                |     1
                |         The tangent to the end section is computed
                |     2
                |         The tangent to the end section is not computed

        :return: int
        """

        return self.com_object.CompEndSectionTangent

    @comp_end_section_tangent.setter
    def comp_end_section_tangent(self, value: int):
        """
        :param int value:
        """

        self.com_object.CompEndSectionTangent = value

    @property
    def comp_start_section_tangent(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property CompStartSectionTangent() As long
                |     Returns or sets whether the tangent surface to the start section of the
                |     lofted surface is computed.
                |     Legal values:
                | 
                |     1
                |         The tangent to the start section is computed
                |     2
                |         The tangent to the start section is not computed

        :return: int
        """

        return self.com_object.CompStartSectionTangent

    @comp_start_section_tangent.setter
    def comp_start_section_tangent(self, value: int):
        """
        :param int value:
        """

        self.com_object.CompStartSectionTangent = value

    @property
    def context(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property Context() As long
                |     Returns or sets the context on Loft feature.
                |     Legal values:
                | 
                |         0 This option creates Lofted surface.
                |         1 This option creates Lofted volume.
                | 
                | 
                |     Note: Setting volume result requires GSO License.
                | 
                |     Example:
                |         This example retrieves in oContext the context for the Loft hybrid
                |         shape feature.
                | 
                |          Dim oContext
                |          Set oContext = Loft.Context

        :return: int
        """

        return self.com_object.Context

    @context.setter
    def context(self, value: int):
        """
        :param int value:
        """

        self.com_object.Context = value

    @property
    def relimitation(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property Relimitation() As long
                |     Returns or sets the relimitation type between sections of the
                |     loft.
                |     NOT YET IMPLEMENTED.
                |     Legal values:
                | 
                |     1
                |         The loft will be swept along the spine, then relimited by the start
                |         section and the end section
                |     2
                |         The loft will be swept along the spine.
                | 
                |             If the spine is a user spine, then the loft is limited by the spine
                |             extremities
                |             If the spine is a computed spine, then the loft is
                |             limited:
                |                 By the start section and the end section, if there is no
                |                 guide
                |                 By the guides extremities, if there are guides
                | 
                |     3
                |         The loft will be swept along the spine, then relimited by the first
                |         section,
                | 
                |             If the spine is a user spine, then the loft is limited by the spine
                |             extremity opposite to the first section
                |             If the spine is a computed spine, then the loft is
                |             limited:
                |                 By the last section, if there is no guide
                |                 By the guides extremities opposite to the first section, if
                |                 there are guides
                | 
                |     4
                |         The loft will be swept along the spine, then relimited by the last
                |         section,
                | 
                |             If the spine is a user spine, then the loft is limited by the spine
                |             extremity opposite to the last section
                |             If the spine is a computed spine, then the loft is
                |             limited:
                |                 By the first section, if there is no guide
                |                 By the guides extremities opposite to the last section, if
                |                 there are guides

        :return: int
        """

        return self.com_object.Relimitation

    @relimitation.setter
    def relimitation(self, value: int):
        """
        :param int value:
        """

        self.com_object.Relimitation = value

    @property
    def section_coupling(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property SectionCoupling() As long
                |     Returns or sets the type of coupling between sections of the
                |     loft.
                |     Legal values:
                | 
                |     1
                |         The curves will be coupled according to the curvilinear abscissa
                |         ratio
                |     2
                |         if each curve has the same number of tangency discontinuity points,
                |         then these points will be coupled, otherwise an error message is
                |         displayed
                |     3
                |         if each curve has the same number of tangency and curvature
                |         discontinuity points, then tangency discontinuity points will be coupled, and
                |         after curvature discontinuity points will be coupled, otherwise an error
                |         message is displayed
                |     4
                |         if each curve has the same number of vertices, then these points will
                |         be coupled, otherwise an error message is displayed

        :return: int
        """

        return self.com_object.SectionCoupling

    @section_coupling.setter
    def section_coupling(self, value: int):
        """
        :param int value:
        """

        self.com_object.SectionCoupling = value

    @property
    def smooth_angle_threshold(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property SmoothAngleThreshold() As double
                |     Returns or sets the angular threshold under which discontinuities (moving
                |     frame, tangency net on reference surface) will be smoothed.

        :return: float
        """

        return self.com_object.SmoothAngleThreshold

    @smooth_angle_threshold.setter
    def smooth_angle_threshold(self, value: float):
        """
        :param float value:
        """

        self.com_object.SmoothAngleThreshold = value

    @property
    def smooth_angle_threshold_activity(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property SmoothAngleThresholdActivity() As boolean
                |     Returns or sets whether a angular threshold is allowed or not during
                |     lofting operation in order to smooth it.
                |     Legal values:
                | 
                |     TRUE
                |         The angular threshold value is used during the lofting
                |         operation
                |     FALSE
                |         The angular threshold value is not used during the lofting
                |         operation

        :return: bool
        """

        return self.com_object.SmoothAngleThresholdActivity

    @smooth_angle_threshold_activity.setter
    def smooth_angle_threshold_activity(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.SmoothAngleThresholdActivity = value

    @property
    def smooth_deviation(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property SmoothDeviation() As double
                |     Returns or sets the deviation value (length) allowed during lofting
                |     operation in order to smooth it.

        :return: float
        """

        return self.com_object.SmoothDeviation

    @smooth_deviation.setter
    def smooth_deviation(self, value: float):
        """
        :param float value:
        """

        self.com_object.SmoothDeviation = value

    @property
    def smooth_deviation_activity(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property SmoothDeviationActivity() As boolean
                |     Returns or sets whether a deviation is allowed or not during lofting
                |     operation in order to smooth it.
                |     Legal values:
                | 
                |     TRUE
                |         The deviation value is used during the lofting
                |         operation
                |     FALSE
                |         The deviation value is not used during the lofting
                |         operation

        :return: bool
        """

        return self.com_object.SmoothDeviationActivity

    @smooth_deviation_activity.setter
    def smooth_deviation_activity(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.SmoothDeviationActivity = value

    def add_guide(self, i_guide: Reference) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub AddGuide(Reference iGuide)
                |     Adds a guide curve to the lofted surface.
                | 
                |     Parameters:
                | 
                |         iGuide
                |             The guide curve to be added
                | 
                |             Sub-element(s) supported (see Boundary object): TriDimFeatEdge and
                |             BiDimFeatEdge.

        :param Reference i_guide:
        :return: None
        """
        return self.com_object.AddGuide(i_guide.com_object)

    def add_guide_with_tangent(self, i_guide: Reference, i_tangent: Reference) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub AddGuideWithTangent(Reference iGuide,Reference iTangent)
                |     Adds a guide curve and a tangent surface to the lofted
                |     surface.
                | 
                |     Parameters:
                | 
                |         iGuide
                |             The guide curve to be added
                | 
                |             Sub-element(s) supported (see Boundary object): TriDimFeatEdge and
                |             BiDimFeatEdge. 
                |         iTangent
                |             The tangent surface to be added. The guide curve must be layed on
                |             the tangent
                | 
                |             Sub-element(s) supported (see Boundary object): Face.

        :param Reference i_guide:
        :param Reference i_tangent:
        :return: None
        """
        return self.com_object.AddGuideWithTangent(i_guide.com_object, i_tangent.com_object)

    def add_section_to_loft(self, i_crv: Reference, i_ori: int, i_point: Reference) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub AddSectionToLoft(Reference iCrv,long iOri,Reference
                | iPoint)
                |     Retrieves a loft section.
                | 
                |     Parameters:
                | 
                |         iCrv
                |             Reference to the curve 
                |         iOri
                |             Orientation 
                |         iPoint
                |             Reference to the Closing Point

        :param Reference i_crv:
        :param int i_ori:
        :param Reference i_point:
        :return: None
        """
        return self.com_object.AddSectionToLoft(i_crv.com_object, i_ori, i_point.com_object)

    def get_area_law_tolerance_parameter(self) -> Length:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Func GetAreaLawToleranceParameter() As Length
                |     Gets the tolerance parameter applied to area law.

        :return: Length
        """
        return Length(self.com_object.GetAreaLawToleranceParameter())

    def get_faces_for_closing(self, o_start_face: Reference, o_end_face: Reference) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub GetFacesForClosing(Reference oStartFace,Reference
                | oEndFace)
                |     Gets start and end faces if the tangent is a computed tangent surface to
                |     the start section or end section, from the lofted surface. The section must
                |     have been set as a face.
                | 
                |     Parameters:
                | 
                |         oStartFace
                |             start face used to close the loft. 
                |         oEndFace
                |             end face used to close the loft.

        :param Reference o_start_face:
        :param Reference o_end_face:
        :return: None
        """
        return self.com_object.GetFacesForClosing(o_start_face.com_object, o_end_face.com_object)

    def get_guide(self, i_pos: int, o_guide: Reference, o_guide_tangent: Reference) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub GetGuide(long iPos,Reference oGuide,Reference
                | oGuideTangent)
                |     Gets informations about the guide at a specified position in the list of
                |     the lofted surface.
                | 
                |     Parameters:
                | 
                |         iPos
                |             position of the guide in the list where the information is
                |             retrieved. 
                |         oGuide
                |             the guide curve. 
                |         oGuideTangent
                |             the tangent corresponding to the guide curve.

        :param int i_pos:
        :param Reference o_guide:
        :param Reference o_guide_tangent:
        :return: None
        """
        return self.com_object.GetGuide(i_pos, o_guide.com_object, o_guide_tangent.com_object)

    def get_nb_of_guides(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Func GetNbOfGuides() As long
                |     Returns the number of guides in the loft object.
                | 
                |     Parameters:
                | 
                |         oSize
                |             Number of guides in the loft.
                | 
                |             Example:
                |                 This example retrieves the number of guides in the hybShpLoft
                |                 hybrid shape Loft.
                | 
                |                  Dim oSize As  long
                |                  oSize = hybShpLoft.GetNbOfGuides

        :return: int
        """
        return self.com_object.GetNbOfGuides()

    def get_section_from_loft(self, i_rank: int, o_crv: Reference, o_ori: int, o_point: Reference) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub GetSectionFromLoft(long iRank,Reference oCrv,long oOri,Reference
                | oPoint)
                |     Retrieves a loft section information.
                | 
                |     Parameters:
                | 
                |         iRank
                |             The index of the section 
                |         oCrv
                |             The reference to the curve 
                |         oOri
                |             The orientation value 
                |         oPoint
                |             The reference to the point

        :param int i_rank:
        :param Reference o_crv:
        :param int o_ori:
        :param Reference o_point:
        :return: None
        """
        return self.com_object.GetSectionFromLoft(i_rank, o_crv.com_object, o_ori, o_point.com_object)

    def get_spine(self, o_spine_type: int, o_spine: Reference) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub GetSpine(long oSpineType,Reference oSpine)
                |     Gets the spine of the lofted surface.
                | 
                |     Parameters:
                | 
                |         oSpineType
                |             type of spine = 1 : User defined spine. = 2 : Automatically computed spine. 
                |         oSpine
                |             curve used as a spine, if the spine is user defined one.

        :param int o_spine_type:
        :param Reference o_spine:
        :return: None
        """
        return self.com_object.GetSpine(o_spine_type, o_spine.com_object)

    def get_start_and_end_section_tangent(self, o_start_section_tangent: Reference, o_end_section_tangent: Reference) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub GetStartAndEndSectionTangent(Reference oStartSectionTangent,Reference
                | oEndSectionTangent)
                |     Gets the start and end section tangents of the lofted
                |     surface.
                | 
                |     Parameters:
                | 
                |         oStartSectionTangent
                |             tangent surface at start section. 
                |         oEndSectionTangent
                |             tangent surface at end section.

        :param Reference o_start_section_tangent:
        :param Reference o_end_section_tangent:
        :return: None
        """
        return self.com_object.GetStartAndEndSectionTangent(o_start_section_tangent.com_object, o_end_section_tangent.com_object)

    def insert_coupling(self, i_position: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub InsertCoupling(long iPosition)
                |     Inserts a coupling to the loft.
                | 
                |     Parameters:
                | 
                |         iPosition
                |             The position of the coupling in the list of couplings. If 0 is
                |             specified, the coupling is inserted at the end of the
                |             list.
                |             Sub-element(s) supported (see Boundary object): Vertex.

        :param int i_position:
        :return: None
        """
        return self.com_object.InsertCoupling(i_position)

    def insert_coupling_point(self, i_coupling_index: int, i_position: int, i_point: Reference) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub InsertCouplingPoint(long iCouplingIndex,long iPosition,Reference
                | iPoint)
                |     Inserts a coupling point to a coupling of the lofted
                |     surface.
                | 
                |     Parameters:
                | 
                |         iCouplingIndex
                |             The index of the coupling in the list of coupling where the point
                |             wil be inserted. 
                |         iPosition
                |             The position of the coupling point in the list of coupling points.
                |             If 0 is specified, the coupling point is inserted at the end of the list.
                |             
                |         iPoint
                |             The point to be inserted. The point must be layed on the section
                |             with the same position.
                |             Sub-element(s) supported (see Boundary object): ScVertex.

        :param int i_coupling_index:
        :param int i_position:
        :param Reference i_point:
        :return: None
        """
        return self.com_object.InsertCouplingPoint(i_coupling_index, i_position, i_point.com_object)

    def insert_section_to_loft(self, i_type: bool, i_crv: Reference, i_ori: int, i_point: Reference, i_section_ref: Reference) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub InsertSectionToLoft(boolean iType,Reference iCrv,long iOri,Reference
                | iPoint,Reference iSectionRef)
                |     Inserts a loft section.
                | 
                |     Parameters:
                | 
                |         iType
                |             iType if set to true section is added After and iType if set to
                |             false section is added Before iSectionRef 
                |         iCrv
                |             Reference to the curve 
                |         iOri
                |             Orientation 
                |         iPoint
                |             Reference to the Closing Point 
                |         iSectionRef
                |             iSectionRef is the section before and after which section is added.

        :param bool i_type:
        :param Reference i_crv:
        :param int i_ori:
        :param Reference i_point:
        :param Reference i_section_ref:
        :return: None
        """
        return self.com_object.InsertSectionToLoft(i_type, i_crv.com_object, i_ori, i_point.com_object, i_section_ref.com_object)

    def modify_guide_curve(self, i_guide: Reference, i_new_guide: Reference) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub ModifyGuideCurve(Reference iGuide,Reference iNewGuide)
                |     Modifies the curve of a guide from the lofted surface.
                | 
                |     Parameters:
                | 
                |         iGuide
                |             guide curve to be replaced. 
                |         iNewGuide
                |             new guide curve, will replace iGuide.

        :param Reference i_guide:
        :param Reference i_new_guide:
        :return: None
        """
        return self.com_object.ModifyGuideCurve(i_guide.com_object, i_new_guide.com_object)

    def modify_section_curve(self, i_section: Reference, i_new_section: Reference, o_curve_section: Reference, o_closing_point: Reference, o_pt_diag: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub ModifySectionCurve(Reference iSection,Reference iNewSection,Reference
                | oCurveSection,Reference oClosingPoint,long oPtDiag)
                |     Modifies the curve of section from the lofted surface.
                | 
                |     Parameters:
                | 
                |         iSection
                |             section curve to be replaced. 
                |         iNewSection
                |             section will replace iSection, can be a curve or a face
                |             
                |         oCurveSection
                |             if iSection is a face, oCurveSection is the boundary of the face.
                |             oCurveSection is used as section curve. if Part design, the face is used to
                |             close the Loft. 
                |         oClosingPoint
                |             if iSection is a closed curve, oClosingPoint is a new closing point
                |             of iSection. if iSection is a face, oClosingPoint is a new closing point the
                |             boundary of iSection. 
                |         oPtDiag
                |             Information on closing point = 0 : No closing point has been created nor retrieved. = 1 : A closing point has been created as a vertex. = 2 : A closing point has been created as an extremum. = 3 : A closing point has been retrieved as an extremum.

        :param Reference i_section:
        :param Reference i_new_section:
        :param Reference o_curve_section:
        :param Reference o_closing_point:
        :param int o_pt_diag:
        :return: None
        """
        return self.com_object.ModifySectionCurve(i_section.com_object, i_new_section.com_object, o_curve_section.com_object, o_closing_point.com_object, o_pt_diag)

    def modify_section_orient(self, i_section: Reference, i_orient: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub ModifySectionOrient(Reference iSection,long iOrient)
                |     Modifies the orientation of the curve of a section from the lofted
                |     surface.
                | 
                |     Parameters:
                | 
                |         iSection
                |             section curve to be modified. 
                |         iOrient
                |             orientation of the section curve = 1 : same orientation. = -1 : inverted orientation. = 2 : ko orientation.

        :param Reference i_section:
        :param int i_orient:
        :return: None
        """
        return self.com_object.ModifySectionOrient(i_section.com_object, i_orient)

    def remove_face_for_closing(self, i_section: Reference) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub RemoveFaceForClosing(Reference iSection)
                |     Removes face used to close the lofted surface.
                | 
                |     Parameters:
                | 
                |         iSection
                |             section curve.

        :param Reference i_section:
        :return: None
        """
        return self.com_object.RemoveFaceForClosing(i_section.com_object)

    def remove_guide(self, i_guide: Reference) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub RemoveGuide(Reference iGuide)
                |     Removes a guide curve from the lofted surface.
                | 
                |     Parameters:
                | 
                |         iGuide
                |             The guide curve to be removed
                | 
                |             Sub-element(s) supported (see Boundary object): TriDimFeatEdge and
                |             BiDimFeatEdge.

        :param Reference i_guide:
        :return: None
        """
        return self.com_object.RemoveGuide(i_guide.com_object)

    def remove_guide_tangent(self, i_guide: Reference) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub RemoveGuideTangent(Reference iGuide)
                |     Removes a tangent surface of a guide from the lofted
                |     surface.
                | 
                |     Parameters:
                | 
                |         iGuide
                |             guide curve of the guide from which the tangent will be removed.

        :param Reference i_guide:
        :return: None
        """
        return self.com_object.RemoveGuideTangent(i_guide.com_object)

    def remove_section(self, i_section: Reference) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub RemoveSection(Reference iSection)
                |     Removes a loft section from the lofted surface.
                | 
                |     Parameters:
                | 
                |         iSection
                |             The loft section to remove
                | 
                |             Sub-element(s) supported (see Boundary object): TriDimFeatEdge and
                |             BiDimFeatEdge.

        :param Reference i_section:
        :return: None
        """
        return self.com_object.RemoveSection(i_section.com_object)

    def remove_section_point(self, i_section: Reference) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub RemoveSectionPoint(Reference iSection)
                |     Removes a closing point of a section from the lofted surface. The curve
                |     section must be closed curve.
                | 
                |     Parameters:
                | 
                |         iSection
                |             section curve of the section from which the point will be removed.

        :param Reference i_section:
        :return: None
        """
        return self.com_object.RemoveSectionPoint(i_section.com_object)

    def remove_section_tangent(self, i_section: Reference) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub RemoveSectionTangent(Reference iSection)
                |     Removes the tangent surface of a section from the lofted surface. The
                |     section must be the start section or the end section of the
                |     loft.
                | 
                |     Parameters:
                | 
                |         iSection
                |             section curve of the section from which the tangent will be
                |             removed.

        :param Reference i_section:
        :return: None
        """
        return self.com_object.RemoveSectionTangent(i_section.com_object)

    def set_end_face_for_closing(self, i_face: Reference) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub SetEndFaceForClosing(Reference iFace)
                |     Sets a face to the end section from the lofted surface.
                | 
                |     Parameters:
                | 
                |         iFace
                |             The face to close the loft (Part design only).
                |             Sub-element(s) supported (see Boundary object): Face.

        :param Reference i_face:
        :return: None
        """
        return self.com_object.SetEndFaceForClosing(i_face.com_object)

    def set_end_section_tangent(self, i_tangent_section: Reference) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub SetEndSectionTangent(Reference iTangentSection)
                |     Sets a tangent surface to the end section from the lofted
                |     surface.
                | 
                |     Parameters:
                | 
                |         iTangentSection
                |             The tangent surface to be added. The end curve section must lay on
                |             the surface.
                |             Sub-element(s) supported (see Boundary object): Face.

        :param Reference i_tangent_section:
        :return: None
        """
        return self.com_object.SetEndSectionTangent(i_tangent_section.com_object)

    def set_spine(self, i_spine: Reference) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub SetSpine(Reference iSpine)
                |     Sets the spine to the lofted surface.
                | 
                |     Parameters:
                | 
                |         iSpine
                |             The curve to be added as a spine.
                |             Sub-element(s) supported (see Boundary object): TriDimFeatEdge and
                |             BiDimFeatEdge.

        :param Reference i_spine:
        :return: None
        """
        return self.com_object.SetSpine(i_spine.com_object)

    def set_start_face_for_closing(self, i_face: Reference) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub SetStartFaceForClosing(Reference iFace)
                |     Sets a face to the start section from the lofted surface.
                | 
                |     Parameters:
                | 
                |         iFace
                |             The face to close the loft (Part design only).
                |             Sub-element(s) supported (see Boundary object): Face.

        :param Reference i_face:
        :return: None
        """
        return self.com_object.SetStartFaceForClosing(i_face.com_object)

    def set_start_section_tangent(self, i_tangent_section: Reference) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub SetStartSectionTangent(Reference iTangentSection)
                |     Sets a tangent surface to the start section from the lofted
                |     surface.
                | 
                |     Parameters:
                | 
                |         iTangentSection
                |             The tangent surface to be added. The start curve section must lay
                |             on the surface.
                |             Sub-element(s) supported (see Boundary object): Face.

        :param Reference i_tangent_section:
        :return: None
        """
        return self.com_object.SetStartSectionTangent(i_tangent_section.com_object)

    def __repr__(self):
        return f'HybridShapeLoft(name="{ self.name }")'
