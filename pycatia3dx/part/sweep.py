"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.mode.reference import Reference
from pycatia3dx.sketcher.sketch import Sketch
from pycatia3dx.todo_part.sketch_based_shape import SketchBasedShape


class Sweep(SketchBasedShape):

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
                |                             Sweep
                | 
                | Represents the sweep shape.
                | It is the base object for ribs and slots.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def anchor_dir_reverse(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property AnchorDirReverse() As boolean
                |     Returns the Sweep AnchorDirReverse flag (for Sweep Move Profile
                |     only).
                |     It returns TRUE if Anchor reverse direction is required , FALSE if
                |     not.
                | 
                |     Returns:
                |         oAnchorDirReverse The oAnchorDirReverse flag as a
                |         boolean
                | 
                |         Example:

        :return: bool
        """

        return self.com_object.AnchorDirReverse

    @anchor_dir_reverse.setter
    def anchor_dir_reverse(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.AnchorDirReverse = value

    @property
    def center_curve(self) -> Sketch:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property CenterCurve() As Sketch (Read Only)
                |     Returns the sketch used as the sweep center curve. The sweep is built along
                |     this sketch.
                | 
                |     Example:
                |         The following example returns in centerCurve the sketch used as center
                |         curve by the firstSweep sweep object:
                | 
                |          Set centerCurve = firstSweep.CenterCurve

        :return: Sketch
        """

        return Sketch(self.com_object.CenterCurve)

    @property
    def center_curve_element(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property CenterCurveElement() As Reference
                |     Returns or sets the center curve .
                |     To set the property, you can use the following Boundary object:
                |     TriDimFeatEdge.

        :return: Reference
        """

        return Reference(self.com_object.CenterCurveElement)

    @center_curve_element.setter
    def center_curve_element(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.CenterCurveElement = value

    @property
    def is_thin(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property IsThin() As boolean
                |     Returns the Sweep thin flag.
                |     It returns TRUE if the Sweep is a thin Sweep , FALSE if
                |     not.
                | 
                |     Returns:
                |         oIsThin The thin flag as a boolean
                | 
                |         Example:
                |             The following example saves in thinFlag the thin flag of Sweep
                |             firstSweep, and then sets it so that it will be now thin
                |             :
                | 
                |              Set thinFlag = firstSweep.IsThin
                |              firstSweep.IsThin = TRUE

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
                |     Returns the Sweep merge end flag (for thin Sweep only).
                |     It returns TRUE if merge ends is required , FALSE if not.
                | 
                |     Returns:
                |         oIsMergeEnd The merge end flag as a boolean
                | 
                |         Example:
                |             The following example saves in MergeEndFlag the merge end flag of
                |             Sweep firstSweep, and then sets it so that merge end will be required
                |             :
                | 
                |              Set MergeEndFlag = firstSweep.IsMergeEnd
                |              firstSweep.IsMergeEnd = TRUE

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
    def merge_mode(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property MergeMode() As CatMergeMode
                |     Returns or sets the end mode .

        :return: CatMergeMode
        """

        return self.com_object.MergeMode

    @merge_mode.setter
    def merge_mode(self, value: int):
        """
        :param int value:
        """

        self.com_object.MergeMode = value

    @property
    def move_profile_to_path(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property MoveProfileToPath() As boolean
                |     Returns the Sweep MoveProfileToPath flag (for Sweep Move Profile
                |     only).
                |     It returns TRUE if move profile is required , FALSE if
                |     not.
                | 
                |     Returns:
                |         oIsMoveProfileToPath The MoveProfileToPath flag as a
                |         boolean
                | 
                |         Example:

        :return: bool
        """

        return self.com_object.MoveProfileToPath

    @move_profile_to_path.setter
    def move_profile_to_path(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.MoveProfileToPath = value

    @property
    def neutral_fiber(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property NeutralFiber() As boolean
                |     Returns the Sweep neutral fiber flag (for thin Sweep
                |     only).
                |     It returns TRUE if the Sweep is a neutral fiber Sweep , FALSE if
                |     not.
                | 
                |     Returns:
                |         oIsNeutralFiber The neutral fiber flag as a boolean
                | 
                |         Example:
                |             The following example saves in NeutralFiberFlag the neutral fiber
                |             flag of Sweep firstSweep, and then sets it so that it will be now neutral fiber
                |             :
                | 
                |              Set NeutralFiberFlag = firstSweep.IsNeutralFiber
                |              firstSweep.IsNeutralFiber = TRUE

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
    def normal_axis_dir_reverse(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property NormalAxisDirReverse() As boolean
                |     Returns the Sweep NormalAxisDirReverse flag (for Sweep Move Profile
                |     only).
                |     It returns TRUE if Normal Axis reverse direction is required , FALSE if
                |     not.
                | 
                |     Returns:
                |         oNormalAxisDirReverse The oNormalAxisDirReverse flag as a
                |         boolean
                | 
                |         Example:

        :return: bool
        """

        return self.com_object.NormalAxisDirReverse

    @normal_axis_dir_reverse.setter
    def normal_axis_dir_reverse(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.NormalAxisDirReverse = value

    @property
    def pulling_dir_element(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property PullingDirElement() As Reference
                |     Returns or sets the pulling direction .
                |     To set the property, you can use one of the following Boundary objects:
                |     PlanarFace, RectilinearTriDimFeatEdge, RectilinearBiDimFeatEdge,
                |     RectilinearMonoDimFeatEdge.

        :return: Reference
        """

        return Reference(self.com_object.PullingDirElement)

    @pulling_dir_element.setter
    def pulling_dir_element(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.PullingDirElement = value

    @property
    def reference_surface_element(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ReferenceSurfaceElement() As Reference
                |     Returns or sets the reference surface .
                |     To set the property, you can use the following Boundary object: Face.

        :return: Reference
        """

        return Reference(self.com_object.ReferenceSurfaceElement)

    @reference_surface_element.setter
    def reference_surface_element(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.ReferenceSurfaceElement = value

    def set_keep_angle_option(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetKeepAngleOption()
                |     Actives KeepAngleOption. 

        :return: None
        """
        return self.com_object.SetKeepAngleOption()

    def __repr__(self):
        return f'Sweep(name="{ self.name }")'
