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


class RemoveFace(DressUpShape):

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
                |                             RemoveFace
                | 
                | Represents the Remove Face operation.
                | It removes a face or a set of faces.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def keep_face(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property KeepFace(Reference iKeepFace) (Write Only)
                |     Adds a new face to be Kept.
                | 
                |     Parameters:
                | 
                |         iKeepFace
                |             The new face to process
                |             The following Boundary object is supported: Face.

        :return: None
        """

        return None

    @keep_face.setter
    def keep_face(self, value: Reference) -> None:
        """
        :param Reference value:
        """

        self.com_object.KeepFace = value

    @property
    def keep_faces(self) -> References:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property KeepFaces() As References (Read Only)
                |     Get the specified faces to be kept.

        :return: References
        """

        return References(self.com_object.KeepFaces)

    @property
    def propagation(self) -> References:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Propagation() As References (Read Only)
                |     Get the faces that will be removed.

        :return: References
        """

        return References(self.com_object.Propagation)

    @property
    def remove_face(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property RemoveFace(Reference iRemoveFace) (Write Only)
                |     Adds a new face to be removed.
                | 
                |     Parameters:
                | 
                |         iRemoveFace
                |             The new face to process
                |             The following Boundary object is supported: Face.

        :return: None
        """

        return None

    @remove_face.setter
    def remove_face(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.RemoveFace = value

    @property
    def remove_faces(self) -> References:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property RemoveFaces() As References (Read Only)
                |     Get the specified faces to be removed.

        :return: References
        """

        return References(self.com_object.RemoveFaces)

    def remove_keep_face(self, i_keep_face: Reference) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub remove_KeepFace(Reference iKeepFace)
                |     Removes a face to be Kept.
                | 
                |     Parameters:
                | 
                |         iKeepFace
                |             The new face to process
                |             The following Boundary object is supported: Face.

        :param Reference i_keep_face:
        :return: None
        """
        return self.com_object.remove_KeepFace(i_keep_face.com_object)

    def remove_remove_face(self, i_remove_face: Reference) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub remove_RemoveFace(Reference iRemoveFace)
                |     Removes a face to be removed.
                | 
                |     Parameters:
                | 
                |         iRemoveFace
                |             The new face to process
                |             The following Boundary object is supported: Face. 

        :param Reference i_remove_face:
        :return: None
        """
        return self.com_object.remove_RemoveFace(i_remove_face.com_object)

    def __repr__(self):
        return f'RemoveFace(name="{ self.name }")'
