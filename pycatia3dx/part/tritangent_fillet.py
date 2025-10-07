"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.mode.reference import Reference
from pycatia3dx.part.fillet import Fillet


class TritangentFillet(Fillet):

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
                |                                 TritangentFillet
                | 
                | The Tritangent Fillet feature : a fillet is built between 3 faces,
                | 2 faces will be relimited, the third one ("face to remove")
                | will
                | be used for fillet tangency ; this face will disappear within the resulting
                | shape.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def face_to_remove(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property FaceToRemove() As Reference
                |     Returns the face to be removed by the tritangent fillet.
                | 
                |     Returns:
                |         oFaceToRemove The face to be removed by the fillet (@see CATIAReference
                |         for more information)
                | 
                |         Example:
                |             The following example returns in removedFace the face to be removed
                |             of
                |             tritangent fillet firstTritangentFillet:
                | 
                |              Set removedFace = firstTritangentFillet.FaceToRemove

        :return: Reference
        """

        return Reference(self.com_object.FaceToRemove)

    @face_to_remove.setter
    def face_to_remove(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.FaceToRemove = value

    @property
    def first_face(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property FirstFace() As Reference
                |     Returns the first face limiting the tritangent fillet.
                | 
                |     Returns:
                |         oFirstFace The limiting face (@see CATIAReference for more
                |         information)
                | 
                |         Example:
                |             The following example returns in face1 the first limiting face
                |             of
                |             tritangent fillet firstTritangentFillet:
                | 
                |              Set face1 = firstTritangentFillet.FirstFace

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
    def second_face(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property SecondFace() As Reference
                |     Returns the second face limiting the tritangent fillet.
                | 
                |     Returns:
                |         oSecondFace The limiting face (@see CATIAReference for more
                |         information)
                | 
                |         Example:
                |             The following example returns in face2 the second limiting face
                |             of
                |             tritangent fillet firstTritangentFillet:
                | 
                |              Set face2 = firstTritangentFillet.SecondFace

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
        return f'TritangentFillet(name="{ self.name }")'
