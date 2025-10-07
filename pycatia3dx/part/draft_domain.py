"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.knowledge_interfaces.angle import Angle
from pycatia3dx.mode.reference import Reference
from pycatia3dx.mode.references import References
from pycatia3dx.system.any_object import AnyObject


class DraftDomain(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     DraftDomain
                | 
                | Represents the draft domain.
                | A draft domain is a basic object used by a draft shape. It contains objects
                | such as an angle, a pulling direction, and a collection of faces to be
                | drafted.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def draft_angle(self) -> Angle:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property DraftAngle() As Angle (Read Only)
                |     Returns the draft angle.
                | 
                |     Example:
                |         The following example returns in angle the draft angle of the draft
                |         domain firstDraftDomain:
                | 
                |          Set angle = firstDraftDomain.DraftAngle

        :return: Angle
        """

        return Angle(self.com_object.DraftAngle)

    @property
    def faces_to_draft(self) -> References:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property FacesToDraft() As References (Read Only)
                |     Returns the faces to be drafted. They are returned as a collection of
                |     reference geometric elements.
                | 
                |     Example:
                |         The following example returns the collection of faces to be drafted of
                |         the draft domain firstDraftDomain in list:
                | 
                |          Set list = firstDraftDomain.FacesToDraft

        :return: References
        """

        return References(self.com_object.FacesToDraft)

    @property
    def multiselection_mode(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property MultiselectionMode() As CatDraftMultiselectionMode
                |     Changes the multiselection mode.
                | 
                |     Parameters:
                | 
                |         iMultiselectionMode.
                |             The elements to be drafted can be selected explicitly
                |             (CATNoneDraftMultiselectionMode) or can implicitly selected as neighbors of the
                |             neutral face (CATMultiselectionByNeutralMode)
                | 
                |             Example:
                |                 The following example returns in MultiselMode the
                |                 multiselection mode of the draft domain firstDraftDomain, and then sets it to
                |                 CATMultiselectionByNeutralMode
                | 
                |                  Set MultiselMode = firstDraftDomain.MultiselectionMode
                |                  firstDraftDomain.MultiselectionMode = CATMultiselectionByNeutralMode

        :return: CatDraftMultiselectionMode
        """

        return self.com_object.MultiselectionMode

    @multiselection_mode.setter
    def multiselection_mode(self, value: int):
        """
        :param int value:
        """

        self.com_object.MultiselectionMode = value

    @property
    def neutral_element(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property NeutralElement() As Reference
                |     Returns or sets the draft neutral element.
                |     To set the property, you can use the following Boundary object:
                |     PlanarFace.
                | 
                |     Example:
                |         The following example returns in neutral the neutral element of the
                |         draft domain firstDraftDomain, and then sets it to
                |         newNeutral:
                | 
                |          Set neutral = firstDraftDomain.NeutralElement
                |          firstDraftDomain.NeutralElement = newNeutral

        :return: Reference
        """

        return Reference(self.com_object.NeutralElement)

    @neutral_element.setter
    def neutral_element(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.NeutralElement = value

    @property
    def neutral_propagation_mode(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property NeutralPropagationMode() As
                | CatDraftNeutralPropagationMode
                |     Returns or sets the neutral element propagation mode. This mode is used
                |     when computing the needed neutral elements.
                | 
                |     Example:
                |         The following example returns in propMode the neutral propagation mode
                |         of the draft domain firstDraftDomain, and then sets it to
                |         CATSmoothDraftNeutralPropagationMode so that the neutral propagation will now
                |         be smooth:
                | 
                |          Set propMode = firstDraftDomain.NeutralPropagationMode
                |          firstDraftDomain.NeutralPropagationMode = CATSmoothDraftNeutralPropagationMode

        :return: CatDraftNeutralPropagationMode
        """

        return self.com_object.NeutralPropagationMode

    @neutral_propagation_mode.setter
    def neutral_propagation_mode(self, value: int):
        """
        :param int value:
        """

        self.com_object.NeutralPropagationMode = value

    @property
    def pulling_direction_element(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property PullingDirectionElement() As Reference
                |     Returns or sets the draft pulling direction element.
                |     To set the property, you can use one of the following Boundary objects:
                |     PlanarFace or RectilinearTriDimFeatEdge.
                | 
                |     Example:
                |         The following example returns in pullingdirection the pulling direction
                |         element of the draft domain firstDraftDomain, and then sets it to
                |         newPullingDirection:
                | 
                |          Set pullingdirection = firstDraftDomain.NeutralElement
                |          firstDraftDomain.PullingDirectionElement = newPullingDirection

        :return: Reference
        """

        return Reference(self.com_object.PullingDirectionElement)

    @pulling_direction_element.setter
    def pulling_direction_element(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.PullingDirectionElement = value

    def add_face_to_draft(self, i_face: Reference) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub AddFaceToDraft(Reference iFace)
                |     Adds a face to those to be drafted.
                | 
                |     Parameters:
                | 
                |         iFace
                |             The face to add to those to be drafted
                |             The following Boundary object is supported: ScFace.
                |             
                | 
                |     Example:
                |         The following example adds the face NewFaceToDraft to the draft domain
                |         CurrentDraftDomain:
                | 
                |          CurrentDraftDomain.AddFaceToDraft(NewFaceToDraft)

        :param Reference i_face:
        :return: None
        """
        return self.com_object.AddFaceToDraft(i_face.com_object)

    def get_pulling_direction(self, io_pulling_direction: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetPullingDirection(CATSafeArrayVariant
                | ioPullingDirection)
                |     Returns the draft pulling direction. The pulling direction is returned as
                |     an array containing the pulling direction vector components. Assume this array
                |     is PullDir. It contains:
                | 
                |     PullDir[0],PullDir[1],PullDir[2]
                |         The X, Y, and Z pulling direction vector components 
                | 
                |     Example:
                |         The following example returns in PullDir the pulling direction vector
                |         components of the draft domain firstDraftDomain:
                | 
                |          Set PullDir = firstDraftDomain.PullingDirection
                |          Set x = PullDir[0]
                |          Set y = PullDir[1]
                |          Set z = PullDir[2]

        :param tuple io_pulling_direction:
        :return: None
        """
        return self.com_object.GetPullingDirection(io_pulling_direction)

    def remove_face_to_draft(self, i_face: Reference) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub RemoveFaceToDraft(Reference iFace)
                |     Removes a face from those to be drafted.
                | 
                |     Parameters:
                | 
                |         iFace
                |             The face to be removed from those to be drafted
                |             The following Boundary object is supported: Face. 
                | 
                |     Example:
                |         The following example removes the face FaceToRemove from the draft
                |         domain CurrentDraftDomain:
                | 
                |          CurrentDraftDomain.RemoveFaceToDraft(FaceToRemove)

        :param Reference i_face:
        :return: None
        """
        return self.com_object.RemoveFaceToDraft(i_face.com_object)

    def set_pulling_direction(self, i_x: float, i_y: float, i_z: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetPullingDirection(double iX,double iY,double iZ)
                |     Sets the draft pulling direction.
                | 
                |     Parameters:
                | 
                |         iX,iY,iZ
                |             The X, Y, and Z pulling direction vector components
                |             
                | 
                |     Example:
                |         The following example sets the draft pulling direction of the draft
                |         domain firstDraftDomain to the direction with the vector components 10, -5,
                |         10:
                | 
                |          firstDraftDomain.PullingDirection 10, -5, 10

        :param float i_x:
        :param float i_y:
        :param float i_z:
        :return: None
        """
        return self.com_object.SetPullingDirection(i_x, i_y, i_z)

    def set_volume_support(self, i_volume_support: Reference) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetVolumeSupport(Reference iVolumeSupport)
                |     Value the support of draft.
                | 
                |     Parameters:
                | 
                |         iVolumeSupport

        :param Reference i_volume_support:
        :return: None
        """
        return self.com_object.SetVolumeSupport(i_volume_support.com_object)

    def __repr__(self):
        return f'DraftDomain(name="{ self.name }")'
