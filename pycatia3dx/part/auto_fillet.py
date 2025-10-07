"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.knowledge_interfaces.length import Length
from pycatia3dx.mode.reference import Reference
from pycatia3dx.mode.references import References
from pycatia3dx.part.dress_up_shape import DressUpShape


class AutoFillet(DressUpShape):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     CATMmrAutomationInterfaces.Shape
                |                         CATPartIDLItf.DressUpShape
                |                             AutoFillet
                | 
                | Represents the AutoFillet shape.
                | A AutoFillet fillets all the edges of Solid
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def curvature_radius(self) -> Length:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property CurvatureRadius() As Length (Read Only)
                |     Returns the Curvature radius.
                | 
                |     Example:
                |         The following example returns in Curvature radius the Curvature radius
                |         of the AutoFillet Autofillet:
                | 
                |          Set Curvatureradius = Autofillet.Radius

        :return: Length
        """

        return Length(self.com_object.CurvatureRadius)

    @property
    def faces_to_fillet(self) -> References:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property FacesToFillet() As References (Read Only)
                |     Returns or sets the faces to fillet.
                | 
                |     Example:
                |         The following example returns in facestofillet the faces required for
                |         autofillet autoFillet, and then sets it to
                |         NewFacestofillet:
                | 
                |          Set Facestofillet = autoFillet.Facestofillet
                |          autofillet.Facestofillet = NewFacestofillet

        :return: References
        """

        return References(self.com_object.FacesToFillet)

    @property
    def faces_to_fillets(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property FacesToFillets(Reference iFace) (Write Only)

        :return: None
        """

        return None

    @faces_to_fillets.setter
    def faces_to_fillets(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.FacesToFillets = value

    @property
    def fillet_radius(self) -> Length:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property FilletRadius() As Length (Read Only)
                |     Returns the Fillet radius.
                | 
                |     Example:
                |         The following example returns in fillet radius the fillet radius of the
                |         AutoFillet Autofillet:
                | 
                |          Set Filletradius = Autofillet.Radius

        :return: Length
        """

        return Length(self.com_object.FilletRadius)

    @property
    def functional_face(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property FunctionalFace(Reference iFace) (Write Only)

        :return: None
        """

        return None

    @functional_face.setter
    def functional_face(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.FunctionalFace = value

    @property
    def functional_faces(self) -> References:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property FunctionalFaces() As References (Read Only)
                |     Returns or sets the functional face.
                | 
                |     Example:
                |         The following example returns in functionalface the functional face of
                |         the autofillet autoFillet, and then sets it to
                |         NewfunctionalFace:
                | 
                |          Set functionalFace = autoFillet.FunctionalFace
                |          autofillet.FunctionalFace = NewfunctionalFace

        :return: References
        """

        return References(self.com_object.FunctionalFaces)

    @property
    def parting_element(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property PartingElement() As Reference
                |     Returns or sets the parting element.
                | 
                |     Example:
                |         The following example returns in partingelement the parting element of
                |         the autofillet autoFillet, and then sets it to Newparting
                |         element:
                | 
                |          Set Parting element = autoFillet.PartingElement
                |          autofillet.PartingElement = NewPartingElement

        :return: Reference
        """

        return Reference(self.com_object.PartingElement)

    @parting_element.setter
    def parting_element(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.PartingElement = value

    @property
    def round_radius(self) -> Length:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property RoundRadius() As Length (Read Only)
                |     Returns the Round radius.
                | 
                |     Example:
                |         The following example returns in round radius the round radius of the
                |         AutoFillet Autofillet:
                | 
                |          Set roundradius = Autofillet.Radius

        :return: Length
        """

        return Length(self.com_object.RoundRadius)

    @property
    def round_radius_activation(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property RoundRadiusActivation() As boolean
                |     Returns the AutoFillet RoundRadiusActivation flag (for AutoFillet
                |     only).
                |     It returns 1 if RoundRadius is activated, 0 if not.
                | 
                |     Returns:
                |         oRoundRadActivation The RoundRadActivation flag as an
                |         int
                | 
                |         Example:

        :return: bool
        """

        return self.com_object.RoundRadiusActivation

    @round_radius_activation.setter
    def round_radius_activation(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.RoundRadiusActivation = value

    @property
    def slivers_and_crack(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property SliversAndCrack(Reference iSlivers) (Write Only)

        :return: None
        """

        return None

    @slivers_and_crack.setter
    def slivers_and_crack(self, value: Reference):
        """
        :param False value:
        """

        self.com_object.SliversAndCrack = value

    @property
    def slivers_and_cracks(self) -> References:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property SliversAndCracks() As References (Read Only)
                |     Returns or sets the slivers face.
                | 
                |     Example:
                |         The following example returns in slivers the sliver face of the
                |         autofillet autoFillet, and then sets it to Newsliver:
                | 
                |          Set sliversFace = autoFillet.SliversFace
                |          autofillet.SliversFace = NewsliversFace

        :return: References
        """

        return References(self.com_object.SliversAndCracks)

    @property
    def support_surface(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property SupportSurface() As Reference
                |     Returns or sets the support surface.
                | 
                |     Example:
                |         The following example returns in SupportSurface the support surface
                |         required for autofillet autoFillet, and then sets it to
                |         NewSupportSurface:
                | 
                |          Set SupportSurface = autoFillet.SupportSurface
                |          autofillet.SupportSurface = NewSupportSurface

        :return: Reference
        """

        return Reference(self.com_object.SupportSurface)

    @support_surface.setter
    def support_surface(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.SupportSurface = value

    def __repr__(self):
        return f'AutoFillet(name="{ self.name }")'
