"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.knowledge_interfaces.length import Length
from pycatia3dx.mode.reference import Reference
from pycatia3dx.part.fillet import Fillet


class FaceFillet(Fillet):

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
                |                             CATPartIDLItf.Fillet
                |                                 FaceFillet
                | 
                | Represents the face fillet shape.
                | A face fillet shape is built between two faces with a fillet
                | radius.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def first_face(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property FirstFace() As Reference
                |     Returns or sets the first limiting face.
                |     To set the property, you can use the following Boundary object:
                |     Face.
                | 
                |     Example:
                |         The following example returns in face1 the first limiting face of the
                |         face fillet firstFaceFillet, and then sets it to
                |         NewFace1:
                | 
                |          Set face1 = firstFaceFillet.FirstFace
                |          firstFaceFillet.FirstFace = NewFace1

        :return: Reference
        """

        return Reference(self.com_object.FirstFace)

    @first_face.setter
    def first_face(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.FirstFace = value

    @property
    def radius(self) -> Length:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Radius() As Length (Read Only)
                |     Returns the face fillet radius.
                | 
                |     Example:
                |         The following example returns in radius the fillet radius of the face
                |         fillet firstFaceFillet:
                | 
                |          Set radius = firstFaceFillet.Radius

        :return: Length
        """

        return Length(self.com_object.Radius)

    @property
    def second_face(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property SecondFace() As Reference
                |     Returns or sets the second limiting face.
                |     To set the property, you can use the following Boundary object:
                |     Face.
                | 
                |     Example:
                |         The following example returns in face2 the second limiting face of the
                |         face fillet firstFaceFillet, and then sets it to
                |         NewFace2:
                | 
                |          Set face2 = firstFaceFillet.SecondFace
                |          firstFaceFillet.SecondFace = NewFace2

        :return: Reference
        """

        return Reference(self.com_object.SecondFace)

    @second_face.setter
    def second_face(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.SecondFace = value

    def __repr__(self):
        return f'FaceFillet(name="{ self.name }")'
