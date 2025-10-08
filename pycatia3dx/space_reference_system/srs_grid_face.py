"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.mode.reference import Reference
from pycatia3dx.space_reference_system.srs_grid_set import SrsGridSet
from pycatia3dx.system.any_object import AnyObject


class SrsGridFace(AnyObject):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SrsGridFace
                | 
                | Role: Allows accessing of Plane Face's data.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def category(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Category() As CATBSTR
                |     Returns or Sets the Category.
                | 
                |     Example:
                | 
                | 
                |              This example retrieves the category of the grid
                |              face.
                |              
                | 
                |               CategoryName = ObjSrsGridFace.Category

        :return: str
        """

        return self.com_object.Category

    @category.setter
    def category(self, value: str):
        """
        :param str value:
        """

        self.com_object.Category = value

    @property
    def orientation(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Orientation() As boolean (Read Only)
                |     Returns the Orientation.
                | 
                |     Returns:
                |         The orientation of the grid face 
                |     Example:
                | 
                | 
                |              This example retrieves orientation of the Grid
                |              Face.
                |              
                | 
                |               oOrient = ObjSrsGridFace.Orientation

        :return: bool
        """

        return self.com_object.Orientation

    @property
    def short_name(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ShortName() As CATBSTR
                |     Returns or Sets the short name.
                | 
                |     Example:
                | 
                | 
                |              This example retrieves short name for Grid Face.
                |              
                | 
                |               ShortName = ObjSrsGridFace.ShortName

        :return: str
        """

        return self.com_object.ShortName

    @short_name.setter
    def short_name(self, value: str):
        """
        :param str value:
        """

        self.com_object.ShortName = value

    def get_abs_offset(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetAbsOffset() As double
                |     Returns the absolute offset of the grid face.
                | 
                |     Returns:
                |         The absolute offset of the grid face 
                |     Example:
                | 
                | 
                |              This example retrieves the absolute offset of the grid
                |              face.
                |              
                | 
                |               Dim AbsOffset As double
                |               AbsOffset = ObjSrsGridFace.GetAbsOffset

        :return: float
        """
        return self.com_object.GetAbsOffset()

    def get_grid_set(self) -> SrsGridSet:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetGridSet() As SrsGridSet
                |     Returns the Grid set of this Grid Face.
                | 
                |     Returns:
                |         The grid set to which this grid face belongs 
                |     Example:
                | 
                | 
                |              This example retrieves grid set of the grid face.
                |              
                | 
                |               Dim ObjSrsGridSet As SrsGridSet
                |               ObjSrsGridSet = ObjSrsGridFace.GetGridSet

        :return: SrsGridSet
        """
        return SrsGridSet(self.com_object.GetGridSet())

    def get_reference(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetReference() As Reference
                |     Returns the reference object of the grid face.
                | 
                |     Returns:
                |         The reference object of the grid face 
                |     Example:
                | 
                | 
                |              This example retrieves the reference object of the grid
                |              face.
                |              
                | 
                |               Dim ObjGridFaceReference As Reference
                |               ObjGridFaceReference = ObjSrsGridFace.GetReference

        :return: Reference
        """
        return Reference(self.com_object.GetReference())

    def get_rel_offset(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetRelOffset() As double
                |     Returns the relative offset of the grid face.
                | 
                |     Returns:
                |         The relative offset of the grid face 
                |     Example:
                | 
                | 
                |              This example retrieves the relative offset of the grid
                |              face.
                |              
                | 
                |               Dim RelOffset As double
                |               RelOffset = ObjSrsGridFace.GetRelOffset

        :return: float
        """
        return self.com_object.GetRelOffset()

    def is_origin_face(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func IsOriginFace() As boolean
                |     Returns whether the grid face is the origin face of the grid
                |     set.
                | 
                |     Returns:
                |         Boolean whether this grid face is the origin face or not (TRUE means
                |         that the grid face is the origin face). 
                |     Example:
                | 
                | 
                |              This example retrieves whether the grid face is the origin face of
                |              the grid set.
                |              
                | 
                |               Dim IsOriginFace As Boolean
                |               IsOriginFace = ObjSrsGridFace.IsAftAtOrigin

        :return: bool
        """
        return self.com_object.IsOriginFace()

    def reset_category(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub ResetCategory()
                |     Resets the category of the grid face.
                | 
                |     Example:
                | 
                | 
                |              This example resets the category of the grid
                |              face.
                |              
                | 
                |               ObjSrsGridFace.ResetCategory

        :return: None
        """
        return self.com_object.ResetCategory()

    def __repr__(self):
        return f'SrsGridFace(name="{self.name}")'
