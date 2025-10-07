"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.mode.reference import Reference
from pycatia3dx.mode.references import References
from pycatia3dx.todo_part.surface_based_shape import SurfaceBasedShape


class ReplaceFace(SurfaceBasedShape):

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
                |                         CATPartIDLItf.SurfaceBasedShape
                |                             ReplaceFace
                | 
                | Represents the Replace Face operation.
                | It replaces a face or a set of faces obtained by tangency continuity by a
                | replacing element, such as a surface or a face or a skin.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def remove_face(self) -> References:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property RemoveFace() As References (Read Only)
                |     Returns the face to be removed.

        :return: References
        """

        return References(self.com_object.RemoveFace)

    @property
    def splitting_side(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property SplittingSide() As CatSplitSide
                |     Returns or sets the splitting side . The splitting side is the side of the
                |     body kept after the splitting. A positive side refers to the same orientation
                |     than the splitting element normal vector.

        :return: CatSplitSide
        """

        return self.com_object.SplittingSide

    @splitting_side.setter
    def splitting_side(self, value: int):
        """
        :param int value:
        """

        self.com_object.SplittingSide = value

    def add_remove_face(self, i_remove_face: Reference) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub AddRemoveFace(Reference iRemoveFace)
                |     Sets the face to be removed.

        :param Reference i_remove_face:
        :return: None
        """
        return self.com_object.AddRemoveFace(i_remove_face.com_object)

    def add_split_plane(self, i_split_plane: Reference) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub AddSplitPlane(Reference iSplitPlane)
                |     Sets the replacing element.

        :param Reference i_split_plane:
        :return: None
        """
        return self.com_object.AddSplitPlane(i_split_plane.com_object)

    def delete_remove_face(self, i_remove_face: Reference) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub DeleteRemoveFace(Reference iRemoveFace)
                |     Remove the face to be removed. 

        :param Reference i_remove_face:
        :return: None
        """
        return self.com_object.DeleteRemoveFace(i_remove_face.com_object)

    def __repr__(self):
        return f'ReplaceFace(name="{ self.name }")'
