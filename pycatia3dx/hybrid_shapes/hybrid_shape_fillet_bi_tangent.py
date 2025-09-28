"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-27 14:29:47.477239

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.hybrid_shapes.hybrid_shape_integrated_law import HybridShapeIntegratedLaw
from pycatia3dx.knowledge_interfaces.length import Length
from pycatia3dx.mmr_automation_interfaces.hybrid_shape import HybridShape
from pycatia3dx.mode.reference import Reference


class HybridShapeFilletBiTangent(HybridShape):

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
                |                         HybridShapeFilletBiTangent
                | 
                | Fillet Bi-Tangent feature.
                | Role: Manipulation of Fillet Bi-Tangent feature Allows to access data of the
                | Fillet Bi-Tangent feature created by using two support surfaces, their
                | orientation, a radius, and options (supports trimming and fillet extremities
                | type)
                | 
                | See also:
                |     HybridShapeFactory
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def conical_section_parameter(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property ConicalSectionParameter() As double
                |     Returns or Sets parameter for conical section.

        :return: float
        """

        return self.com_object.ConicalSectionParameter

    @conical_section_parameter.setter
    def conical_section_parameter(self, value: float):
        """
        :param float value:
        """

        self.com_object.ConicalSectionParameter = value

    @property
    def first_elem(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property FirstElem() As Reference
                |     Returns or Sets the first support surface feature.

        :return: Reference
        """

        return Reference(self.com_object.FirstElem)

    @first_elem.setter
    def first_elem(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.FirstElem = value

    @property
    def first_law_relimiter(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property FirstLawRelimiter() As Reference
                |     Gets or sets Law first relimiter for variable shape fillet with law
                |     management.
                |     Relimiters must be point on spine.
                |     The input law will be mapped between first and second relimiters. This
                |     example retrieves in HybLaw the first law relimiter for the Fillet hybrid shape
                |     feature.
                | 
                |      Dim HybLaw As Reference
                |      HybLaw = Fillet.FirstLawRelimiter

        :return: Reference
        """

        return Reference(self.com_object.FirstLawRelimiter)

    @first_law_relimiter.setter
    def first_law_relimiter(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.FirstLawRelimiter = value

    @property
    def first_orientation(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property FirstOrientation() As long
                |     Returns or Setsthe first orientation used to specify fillet center
                |     position.
                |     Orientation is same or inverse than the normal to the first surface support

        :return: int
        """

        return self.com_object.FirstOrientation

    @first_orientation.setter
    def first_orientation(self, value: int):
        """
        :param int value:
        """

        self.com_object.FirstOrientation = value

    @property
    def hold_curve(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property HoldCurve() As Reference
                |     Returns or Sets the Hold Curve feature.

        :return: Reference
        """

        return Reference(self.com_object.HoldCurve)

    @hold_curve.setter
    def hold_curve(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.HoldCurve = value

    @property
    def integrated_law(self) -> HybridShapeIntegratedLaw:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property IntegratedLaw() As HybridShapeIntegratedLaw
                |     Gets or sets Integrated Law to manage Variable Shape Fillet with
                |     law.
                | 
                |     Parameters:
                | 
                |         oILaw
                |             Integrated law This example retrieves in HybridIntegratedLaw the
                |             IntegratedLaw for the Fillet hybrid shape feature.
                | 
                |              Dim HybridIntegratedLaw
                |              Set HybridIntegratedLaw = Fillet.IntegratedLaw

        :return: HybridShapeIntegratedLaw
        """

        return HybridShapeIntegratedLaw(self.com_object.IntegratedLaw)

    @integrated_law.setter
    def integrated_law(self, value: HybridShapeIntegratedLaw):
        """
        :param HybridShapeIntegratedLaw value:
        """

        self.com_object.IntegratedLaw = value

    @property
    def radius(self) -> Length:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property Radius() As Length (Read Only)
                |     Returns fillet radius in a CATIALength.

        :return: Length
        """

        return Length(self.com_object.Radius)

    @property
    def radius_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property RadiusType() As long
                |     Returns or Sets fillet radius type.
                |     Fillet radius type :
                |     - CATGSMRadiusDefault (0)
                |     - CATGSMRadiusChordLength(1)

        :return: int
        """

        return self.com_object.RadiusType

    @radius_type.setter
    def radius_type(self, value: int):
        """
        :param int value:
        """

        self.com_object.RadiusType = value

    @property
    def radius_value(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property RadiusValue() As double
                |     Returns or Sets fillet radius value.

        :return: float
        """

        return self.com_object.RadiusValue

    @radius_value.setter
    def radius_value(self, value: float):
        """
        :param float value:
        """

        self.com_object.RadiusValue = value

    @property
    def ribbon_relimitation_mode(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property RibbonRelimitationMode() As long
                |     Returns or Sets fillet ribbon relimitation mode (or fillet extremities
                |     mode).
                |     Fillet extremities mode :
                |     - CATGSMSmooth (0)
                |     - CATGSMStraight(1)
                |     - CATGSMMaximum (2)
                |     - CATGSMMinimum (3)

        :return: int
        """

        return self.com_object.RibbonRelimitationMode

    @ribbon_relimitation_mode.setter
    def ribbon_relimitation_mode(self, value: int):
        """
        :param int value:
        """

        self.com_object.RibbonRelimitationMode = value

    @property
    def second_elem(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property SecondElem() As Reference
                |     Returns or sets the Second support surface feature.

        :return: Reference
        """

        return Reference(self.com_object.SecondElem)

    @second_elem.setter
    def second_elem(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.SecondElem = value

    @property
    def second_law_relimiter(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property SecondLawRelimiter() As Reference
                |     Gets or sets Law second relimiter for variable shape fillet with law
                |     management.
                |     Relimiters must be point on spine.
                |     The input law will be mapped between first and second relimiters. This
                |     example retrieves in HybLaw the second law relimiter for the Fillet hybrid
                |     shape feature.
                | 
                |      Dim HybLaw As Reference
                |      HybLaw = Fillet.SecondLawRelimiter

        :return: Reference
        """

        return Reference(self.com_object.SecondLawRelimiter)

    @second_law_relimiter.setter
    def second_law_relimiter(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.SecondLawRelimiter = value

    @property
    def second_orientation(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property SecondOrientation() As long
                |     Returns or Sets the Second orientation used to specify fillet center
                |     position.
                |     Orientation is same or inverse than the normal to the Second surface
                |     support

        :return: int
        """

        return self.com_object.SecondOrientation

    @second_orientation.setter
    def second_orientation(self, value: int):
        """
        :param int value:
        """

        self.com_object.SecondOrientation = value

    @property
    def section_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property SectionType() As long
                |     Returns or Sets fillet section type.
                |     Fillet radius type :
                |     - CATGSMCircularSection(0)
                |     - CATGSMConicalSection (1)

        :return: int
        """

        return self.com_object.SectionType

    @section_type.setter
    def section_type(self, value: int):
        """
        :param int value:
        """

        self.com_object.SectionType = value

    @property
    def spine(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property Spine() As Reference
                |     Returns or Sets the spine feature.

        :return: Reference
        """

        return Reference(self.com_object.Spine)

    @spine.setter
    def spine(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.Spine = value

    @property
    def supports_trim_mode(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property SupportsTrimMode() As long
                |     Returns or Sets whether support surfaces are trimmed or not. Possible values of SupportsTrimMode = 0 : No trim of fillet supports. = 1 : Trim of both fillet supports. = 2 : Trim of fillet support 1. = 3 : Trim of fillet support 2.

        :return: int
        """

        return self.com_object.SupportsTrimMode

    @supports_trim_mode.setter
    def supports_trim_mode(self, value: int):
        """
        :param int value:
        """

        self.com_object.SupportsTrimMode = value

    def append_new_face_to_keep(self, i_face: Reference) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub AppendNewFaceToKeep(Reference iFace)
                |     Append a new face to keep.
                | 
                |     Parameters:
                | 
                |         iFace

        :param Reference i_face:
        :return: None
        """
        return self.com_object.AppendNewFaceToKeep(i_face.com_object)

    def get_face_to_keep(self, i_pos: int) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Func GetFaceToKeep(long iPos) As Reference
                |     Gets the face to keep for fillet operation.
                | 
                |     Parameters:
                | 
                |         oFace
                |             The face to keep for fillet operation. 
                |         iPos
                |             Position of the face to be retrieved.

        :param int i_pos:
        :return: Reference
        """
        return Reference(self.com_object.GetFaceToKeep(i_pos))

    def invert_first_orientation(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub InvertFirstOrientation()
                |     Inverts first orientation used to specify fillet center position.

        :return: None
        """
        return self.com_object.InvertFirstOrientation()

    def invert_second_orientation(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub InvertSecondOrientation()
                |     Inverts second orientation used to specify fillet center position.

        :return: None
        """
        return self.com_object.InvertSecondOrientation()

    def remove_all_faces_to_keep(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub RemoveAllFacesToKeep()
                |     Remove all the faces to keep.

        :return: None
        """
        return self.com_object.RemoveAllFacesToKeep()

    def remove_face_to_keep(self, i_face: Reference) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub RemoveFaceToKeep(Reference iFace)
                |     Remove a face to keep.
                | 
                |     Parameters:
                | 
                |         iFace

        :param Reference i_face:
        :return: None
        """
        return self.com_object.RemoveFaceToKeep(i_face.com_object)

    def __repr__(self):
        return f'HybridShapeFilletBiTangent(name="{ self.name }")'
