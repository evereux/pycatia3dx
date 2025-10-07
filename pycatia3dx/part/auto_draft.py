"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.mode.reference import Reference
from pycatia3dx.mode.references import References
from pycatia3dx.todo_part.dress_up_shape import DressUpShape


class AutoDraft(DressUpShape):

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
                |                             AutoDraft
                | 
                | Represents the AutoDraft shape.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

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
                |     Returns or sets the functional faces.
                | 
                |     Example:
                |         The following example returns in FunctionalFaces the list functional
                |         faces of the AutoDraft AutoDraft, and then sets NewFunctionalFace as a
                |         functional face:
                | 
                |          Set FunctionalFaces = AutoDraft.FunctionalFace
                |          AutoDraft.FunctionalFace = NewFunctionalFace

        :return: References
        """

        return References(self.com_object.FunctionalFaces)

    @property
    def main_draft_angle(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property MainDraftAngle() As Reference
                |     Returns or sets the main draft angle.
                | 
                |     Example:
                |         The following example returns in MainDraftAngle the main draft angle of
                |         the AutoDraft AutoDraft, and then sets it to
                |         NewMainDraftAngle.:
                | 
                |          Set MainDraftAngle = AutoDraft.MainDraftAngle
                |          AutoDraft.MainDraftAngle = NewMainDraftAngle

        :return: Reference
        """

        return Reference(self.com_object.MainDraftAngle)

    @main_draft_angle.setter
    def main_draft_angle(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.MainDraftAngle = value

    @property
    def mode(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Mode() As Reference
                |     Returns or sets the draft mode.
                | 
                |     Example:
                |         The following example returns in Mode the mode of the draft AutoDraft
                |         AutoDraft, and then sets it to NewMode:
                | 
                |          Set Mode = AutoDraft.Mode
                |          AutoDraft.Mode = NewMode

        :return: Reference
        """

        return Reference(self.com_object.Mode)

    @mode.setter
    def mode(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.Mode = value

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
                |         The following example returns in PartingElement the parting element of
                |         the AutoDraft AutoDraft, and then sets it to
                |         NewpartingElement:
                | 
                |          Set PartingElement = AutoDraft.PartingElement
                |          AutoDraft.PartingElement = NewPartingElement

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
    def pulling_direction(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property PullingDirection() As Reference
                |     Returns or sets the pulling direction.
                | 
                |     Example:
                |         The following example returns in PullingDirection the pulling direction
                |         of the AutoDraft AutoDraft, and then sets it to
                |         NewPullingDirection.:
                | 
                |          Set PullingDirection = AutoDraft.PullingDirection
                |          AutoDraft.PullingDirection = NewPullingDirection

        :return: Reference
        """

        return Reference(self.com_object.PullingDirection)

    @pulling_direction.setter
    def pulling_direction(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.PullingDirection = value

    def __repr__(self):
        return f'AutoDraft(name="{ self.name }")'
