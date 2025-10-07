"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.knowledge_interfaces.length import Length
from pycatia3dx.todo_part.sketch_based_shape import SketchBasedShape


class Stiffener(SketchBasedShape):

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
                |                         CATPartIDLItf.SketchBasedShape
                |                             Stiffener
                | 
                | Represents the stiffener shape.
                | A stiffener is made up of a sketch used as the stiffener profile, that is
                | extruded (offset) and that fills the nearest shape. This is a "positive" shape:
                | it adds material to the body it belongs to.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def is_from_top(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property IsFromTop() As boolean
                |     Returns or sets whether the stiffener is From Side or From
                |     Top.
                |     True if the stiffener is From Top stiffener with respect to the base
                |     sketch. False if the stiffener is From Side stiffener with respect to the base
                |     sketch.
                | 
                |     Example:
                |         The following example returns in FromTopFlag whether the firstStiffener
                |         stiffener is From Top, and then sets it as From Top stiffener with respect to
                |         its base sketch:
                | 
                |          Set FromTopFlag = firstStiffener.IsFromTop
                |          firstStiffener.IsFromTop  = True

        :return: bool
        """

        return self.com_object.IsFromTop

    @is_from_top.setter
    def is_from_top(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.IsFromTop = value

    @property
    def is_symmetric(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property IsSymmetric() As boolean
                |     Returns or sets whether the stiffener is symmetric.
                |     True if the stiffener is symmetric with respect to the base
                |     sketch.
                | 
                |     Example:
                |         The following example returns in symFlag whether the firstStiffener
                |         stiffener is symmetric, and then sets it as symmetric with respect to its base
                |         sketch:
                | 
                |          Set symFlag = firstStiffener.IsSymmetric
                |          firstStiffener.IsSymmetric  = True

        :return: bool
        """

        return self.com_object.IsSymmetric

    @is_symmetric.setter
    def is_symmetric(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.IsSymmetric = value

    @property
    def thickness(self) -> Length:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Thickness() As Length (Read Only)
                |     Returns the stiffener thickness. This is half of the thickness if the
                |     stiffener is symmetrical, and the thickness otherwise.
                | 
                |     Example:
                |         The following example returns in thickness the thickness of the
                |         firstStiffener stiffener:
                | 
                |          Set thickness = firstStiffener.Thickness

        :return: Length
        """

        return Length(self.com_object.Thickness)

    @property
    def thickness_from_top(self) -> Length:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ThicknessFromTop() As Length (Read Only)
                |     Returns the stiffener thickness top in case of From Top stiffener. This is
                |     equal to first thickness if the stiffener is symmetrical,
                | 
                |     Example:
                |         The following example returns in thicknessfromtop the thickness of the
                |         firstStiffener stiffener:
                | 
                |          Set thicknessfromtop = firstStiffener.ThicknessFromTop

        :return: Length
        """

        return Length(self.com_object.ThicknessFromTop)

    def reverse_depth(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub ReverseDepth()
                |     Reverses the stiffener direction. This is useful for finding the shape to
                |     reach.
                | 
                |     Example:
                |         The following example reverses the current direction of the
                |         firstStiffener stiffener:
                | 
                |          firstStiffener.ReverseDepth

        :return: None
        """
        return self.com_object.ReverseDepth()

    def reverse_thickness(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub ReverseThickness()
                |     Reverses the stiffener thickness direction. The stiffener thickness is
                |     swapped with respect to the base sketch.
                | 
                |     Example:
                |         The following example reverses the current direction of the
                |         firstStiffener stiffener:
                | 
                |          firstStiffener.ReverseThickness

        :return: None
        """
        return self.com_object.ReverseThickness()

    def __repr__(self):
        return f'Stiffener(name="{ self.name }")'
