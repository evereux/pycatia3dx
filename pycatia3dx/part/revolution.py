"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.knowledge_interfaces.angle import Angle
from pycatia3dx.mode.reference import Reference
from pycatia3dx.todo_part.sketch_based_shape import SketchBasedShape


class Revolution(SketchBasedShape):

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
                |                             Revolution
                | 
                | Represents the revolution-based shapes.
                | It is the base objects for shaft and grooves.
                | 
                | See also:
                |     Shaft, Groove
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def first_angle(self) -> Angle:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property FirstAngle() As Angle (Read Only)
                |     Returns the revolution first angle. This angle is computed around the
                |     revolution axis, starting from the sketch plane trace on the plane
                |     perpendicular to the revolution axis, and is counted positive clockwise when
                |     looking at this plane in the revolution axis direction.
                | 
                |     Example:
                |         The following example returns in firstAngle the first angle of the
                |         MyRevolution revolution object:
                | 
                |          Set firstAngle = MyRevolution.FirstAngle

        :return: Angle
        """

        return Angle(self.com_object.FirstAngle)

    @property
    def is_thin(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property IsThin() As boolean
                |     Returns the Revol thin flag.
                |     It returns TRUE if the Revol is a thin Revol , FALSE if
                |     not.
                | 
                |     Returns:
                |         oIsThin The thin flag as a boolean
                | 
                |         Example:
                |             The following example saves in thinFlag the thin flag of Revol
                |             firstRevol, and then sets it so that it will be now thin
                |             :
                | 
                |              Set thinFlag = firstRevol.IsThin
                |              firstRevol.IsThin = TRUE

        :return: bool
        """

        return self.com_object.IsThin

    @is_thin.setter
    def is_thin(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.IsThin = value

    @property
    def merge_end(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property MergeEnd() As boolean
                |     Returns the Revol merge end flag (for thin Revol only).
                |     It returns TRUE if merge ends is required , FALSE if not.
                | 
                |     Returns:
                |         oIsMergeEnd The merge end flag as a boolean
                | 
                |         Example:
                |             The following example saves in MergeEndFlag the merge end flag of
                |             Revol firstRevol, and then sets it so that merge end will be required
                |             :
                | 
                |              Set MergeEndFlag = firstRevol.IsMergeEnd
                |              firstRevol.IsMergeEnd = TRUE

        :return: bool
        """

        return self.com_object.MergeEnd

    @merge_end.setter
    def merge_end(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.MergeEnd = value

    @property
    def neutral_fiber(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property NeutralFiber() As boolean
                |     Returns the Revol neutral fiber flag (for thin Revol
                |     only).
                |     It returns TRUE if the Revol is a neutral fiber Revol , FALSE if
                |     not.
                | 
                |     Returns:
                |         oIsNeutralFiber The neutral fiber flag as a boolean
                | 
                |         Example:
                |             The following example saves in NeutralFiberFlag the neutral fiber
                |             flag of Revol firstRevol, and then sets it so that it will be now neutral fiber
                |             :
                | 
                |              Set NeutralFiberFlag = firstRevol.IsNeutralFiber
                |              firstRevol.IsNeutralFiber = TRUE

        :return: bool
        """

        return self.com_object.NeutralFiber

    @neutral_fiber.setter
    def neutral_fiber(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.NeutralFiber = value

    @property
    def revolute_axis(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property RevoluteAxis() As Reference
                |     Returns or sets the rotation axis for Revol.
                |     To set the property, you can use one of the following Boundary objects:
                |     RectilinearTriDimFeatEdge, RectilinearBiDimFeatEdge or
                |     RectilinearMonoDimFeatEdge.
                | 
                |     Example: This example retrieves in RevoluteAxis the rotation axis for the Rotate axis of the Revol feature Dim RevoluteAxis As Reference Set RevoluteAxis = Rotate.Axis

        :return: Reference
        """

        return Reference(self.com_object.RevoluteAxis)

    @revolute_axis.setter
    def revolute_axis(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.RevoluteAxis = value

    @property
    def second_angle(self) -> Angle:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property SecondAngle() As Angle (Read Only)
                |     Returns the revolution second angle. This angle is computed around the
                |     revolution axis, starting from the sketch plane trace on the plane
                |     perpendicular to the revolution axis, and is counted positive counterclockwise
                |     when looking at this plane in the revolution axis direction. Its default value
                |     is 0.
                | 
                |     Example:
                |         The following example returns in secondAngle the second angle of the
                |         MyRevolution revolution object:
                | 
                |          Set secondAngle = MyRevolution.SecondAngle

        :return: Angle
        """

        return Angle(self.com_object.SecondAngle)

    def __repr__(self):
        return f'Revolution(name="{ self.name }")'
