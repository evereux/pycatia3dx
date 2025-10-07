"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.mode.reference import Reference
from pycatia3dx.todo_part.draft_domains import DraftDomains
from pycatia3dx.todo_part.dress_up_shape import DressUpShape


class Draft(DressUpShape):

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
                |                             Draft
                | 
                | Represents the draft shape.
                | A draft shape is made up of draft domains (at least one) and of a parting
                | element.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def draft_domains(self) -> DraftDomains:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property DraftDomains() As DraftDomains (Read Only)
                |     Returns the collection of draft domains.
                | 
                |     Example:
                |         The following example returns in list the collection of draft domains
                |         of the firstDraft draft:
                | 
                |          Set list = firstDraft.DraftDomains

        :return: DraftDomains
        """

        return DraftDomains(self.com_object.DraftDomains)

    @property
    def mode(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Mode() As CatDraftMode
                |     Returns or sets the draft mode.
                | 
                |     Example:
                |         The following example returns in mode the draft mode of the firstDraft
                |         draft, and then sets it to
                |         CatReflectKeepFaceDraftMode:
                | 
                |          Set mode = firstDraft.Mode
                |          Set firstDraft.Mode = CatReflectKeepFaceDraftMode

        :return: CatDraftMode
        """

        return self.com_object.Mode

    @mode.setter
    def mode(self, value: int):
        """
        :param int value:
        """

        self.com_object.Mode = value

    @property
    def parting_element(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property PartingElement() As Reference
                |     Returns or sets the draft parting element.
                |     To set the property, you can use the following Boundary object:
                |     PlanarFace.
                | 
                |     Example:
                |         The following example returns in element the parting element of the
                |         firstDraft draft, and then sets it to the element2 geometrical
                |         element:
                | 
                |          Set element = firstDraft.PartingElement
                |          Set firstDraft.PartingElement = element2

        :return: Reference
        """

        return Reference(self.com_object.PartingElement)

    @parting_element.setter
    def parting_element(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.PartingElement = value

    def __repr__(self):
        return f'Draft(name="{ self.name }")'
