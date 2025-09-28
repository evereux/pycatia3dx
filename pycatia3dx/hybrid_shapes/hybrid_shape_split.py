"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-27 14:29:47.477239

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.mmr_automation_interfaces.hybrid_shape import HybridShape
from pycatia3dx.mode.reference import Reference


class HybridShapeSplit(HybridShape):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     CATMmrAutomationInterfaces.HybridShape
                |                         HybridShapeSplit
                | 
                | Represents the hybrid shape split feature object.
                | Role: To access data of the hybrid shape split feature. This data
                | includes:
                | 
                |     The element to be cut (surface or curve)
                |     The cutting element ( surface, curve or point)
                |     An orientation to specify which side has to be kept
                | 
                | LICENSING INFORMATION: Creation of volume result requires GSO
                | License
                | if GSO License is not granted , setting of Volume context has not
                | effect
                | Use the CATIAHybridShapeFactory to create HybridShapeFeature
                | object.
                | 
                | See also:
                |     HybridShapeFactory
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def automatic_extrapolation_mode(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property AutomaticExtrapolationMode() As boolean
                |     Gets or sets the automatic extrapolation mode status. AutomaticExtrapolationMode = TRUE : Automatic extrapolation mode is on. = FALSE : Automatic extrapolation mode is off. This example retrieves in AutoExtrapolMode the automatic extrapolation mode status for the Split hybrid shape feature.
                | 
                |      Dim AutoExtrapolMode As boolean
                |      AutoExtrapolMode = Split.AutomaticExtrapolationMode

        :return: bool
        """

        return self.com_object.AutomaticExtrapolationMode

    @automatic_extrapolation_mode.setter
    def automatic_extrapolation_mode(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.AutomaticExtrapolationMode = value

    @property
    def both_sides_mode(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property BothSidesMode() As boolean
                |     Gets or sets both sides computation mode. BothSidesMode = TRUE : Both sides are computed. = FALSE : Both sides are not computed. This example retrieves in BothSides the both sides computation mode for the Split hybrid shape feature.
                | 
                |      Dim BothSides As boolean
                |      BothSides = Split.BothSidesMode

        :return: bool
        """

        return self.com_object.BothSidesMode

    @both_sides_mode.setter
    def both_sides_mode(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.BothSidesMode = value

    @property
    def cutting_elem(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property CuttingElem() As Reference
                |     Returns or sets the cutting element.
                |     Sub-element(s) supported (see Boundary object): Face, TriDimFeatEdge,
                |     BiDimFeatEdge or Vertex.
                | 
                |     Example:
                |         This example retrieves in CuttingElement the cutting element for the
                |         Split hybrid shape feature.
                | 
                |          Dim CuttingElement As Reference
                |          Set CuttingElement = Split.CuttingElem

        :return: Reference
        """

        return Reference(self.com_object.CuttingElem)

    @cutting_elem.setter
    def cutting_elem(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.CuttingElem = value

    @property
    def elem_to_cut(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property ElemToCut() As Reference
                |     Returns or sets the element to cut.
                | 
                |     Example:
                |         This example retrieves in Element the element to cut for the Split
                |         hybrid shape feature.
                | 
                |          Dim Element As Reference
                |          Set Element = Split.ElemToCut

        :return: Reference
        """

        return Reference(self.com_object.ElemToCut)

    @elem_to_cut.setter
    def elem_to_cut(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.ElemToCut = value

    @property
    def extrapolation_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property ExtrapolationType() As long
                |     Gets or sets the extrapolation type. ExtrapolationType = CATGSMExtrapolationType_None(0). = CATGSMExtrapolationType_Tangent(1). = CATGSMExtrapolationType_Curvature(2). This example retrieves in ExtrapolateType the extrapolation type for the Split hybrid shape feature.

        :return: int
        """

        return self.com_object.ExtrapolationType

    @extrapolation_type.setter
    def extrapolation_type(self, value: int):
        """
        :param int value:
        """

        self.com_object.ExtrapolationType = value

    @property
    def intersection_computation(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property IntersectionComputation() As boolean
                |     Gets or sets Intersection computation mode. IntersectionComputation = TRUE : Intersection is computed. = FALSE : Intersection is not computed. This example retrieves in Intersection the Intersection computation mode for the Split hybrid shape feature.
                | 
                |      Dim Intersection As boolean
                |      Intersection = Split.IntersectionComputation

        :return: bool
        """

        return self.com_object.IntersectionComputation

    @intersection_computation.setter
    def intersection_computation(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.IntersectionComputation = value

    @property
    def orientation(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property Orientation() As long
                |     Returns or sets the orientation used to compute the split.
                |     Role:
                |     Orientation specifies kept parts of cut feature.
                | 
                |     When splitting a surface by a surface :
                |     - If orientation value is 1: kept parts are specified by the "natural"
                |     normal to the cutting feature
                |     - If orientation value -1: kept parts are specified by the inverse of the
                |     "natural" normal to the cutting feature
                | 
                |     When splitting a surface by a curve :
                |     - If orientation value is 1: kept parts are specified by the result of the cross product : normal(surface)^tangent(curve)
                |     - If orientation value is -1: Kept parts are specified by the inverse of the result of the cross product : normal(surface)^tangent(curve)
                | 
                |     When splitting a curve by a point or a curve (without support specified)
                |     :
                |     - If orientation value is 1: Kept parts are from beginning of the curve to
                |     the first intersection,
                |     and, if there is one, from the second to the third intersection and so on
                |     until the end of the curve.
                |     - If orientation value is -1: Kept parts are from the first intersection to
                |     the second (if there is one),
                |     and, if there is one, from the third to the fourth and so on until the end
                |     of the curve.
                | 
                |     When splitting a curve on support:
                |     - If orientation value is 1: Kept parts are specified by the result of the cross product : normal(support surface)^tangent(cutting curve)
                |     - If orientation value is -1: Kept parts are specified by the inverse of the result of the cross product : normal(support surface)^tangent(cutting curve)
                | 
                |     When splitting a curve by a surface:
                |     - If orientation value is 1: Kept parts are specified by the inverse of the
                |     normal to the surface
                |     - If orientation value is -1: Kept parts are specified by the normal to the
                |     surface
                | 
                |     Example
                |         This example retrieves in OrientValue the orientation value for the
                |         Split hybrid shape feature.
                | 
                |          Dim OrientValue As long
                |          Set OrientValue = Split.Orientation

        :return: int
        """

        return self.com_object.Orientation

    @orientation.setter
    def orientation(self, value: int):
        """
        :param int value:
        """

        self.com_object.Orientation = value

    @property
    def support(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property Support() As Reference
                |     Returns or sets the support element.
                |     This support element may not exist.
                |     Sub-element(s) supported (see Boundary object): Face.
                | 
                |     Example:
                |         This example retrieves in Element the support element for the Split
                |         hybrid shape feature.
                | 
                |          Dim Element As Reference
                |          Set Element = Split.Support

        :return: Reference
        """

        return Reference(self.com_object.Support)

    @support.setter
    def support(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.Support = value

    @property
    def volume_result(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property VolumeResult() As long
                |     Returns or sets the Result Type.
                |     Result type:
                | 
                |         : 0 -> Surface
                |         : 1 -> Volume
                |         , The resultant split will be volume. If input is element to cut is
                |         volume. 
                | 
                | 
                |     Note: Setting volume result requires GSO License.
                | 
                |     Example: This example retrieves in ResultType the result type for the Split
                |     hybrid shape feature.
                | 
                |      Dim RType As long
                |      Set RType = Split.ResultType

        :return: int
        """

        return self.com_object.VolumeResult

    @volume_result.setter
    def volume_result(self, value: int):
        """
        :param int value:
        """

        self.com_object.VolumeResult = value

    def add_cutting_elem(self, i_elem: Reference, i_orientation: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub AddCuttingElem(Reference iElem,long iOrientation)
                |     Adds a cutting feature.
                | 
                |     Parameters:
                | 
                |         iElem
                |             cutting feature 
                |         iOrientation
                |             Orientation iOrientation = 1 : SameOrientation = -1 : InvertOrientation = 2 : KoOrientation

        :param Reference i_elem:
        :param int i_orientation:
        :return: None
        """
        return self.com_object.AddCuttingElem(i_elem.com_object, i_orientation)

    def add_element_to_keep(self, i_element: Reference) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub AddElementToKeep(Reference iElement)
                |     Adds an element to specifications. This element will be
                |     kept.
                | 
                |     Parameters:
                | 
                |         iElement
                |             Element to keep.

        :param Reference i_element:
        :return: None
        """
        return self.com_object.AddElementToKeep(i_element.com_object)

    def add_element_to_remove(self, i_element: Reference) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub AddElementToRemove(Reference iElement)
                |     Adds an element to specifications. This element will be
                |     removed.
                | 
                |     Parameters:
                | 
                |         iElement
                |             Element to remove.

        :param Reference i_element:
        :return: None
        """
        return self.com_object.AddElementToRemove(i_element.com_object)

    def get_cutting_elem(self, i_rank: int) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Func GetCuttingElem(long iRank) As Reference
                |     Gets the cutting feature at a given index (a point, a curve or a
                |     surface).
                | 
                |     Parameters:
                | 
                |         oElem
                |             cutting feature 
                |         iRank
                |             Index of one of the cutting features

        :param int i_rank:
        :return: Reference
        """
        return Reference(self.com_object.GetCuttingElem(i_rank))

    def get_intersection(self, i_rank: int) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Func GetIntersection(long iRank) As Reference
                |     Gets the intersection at a given index.
                | 
                |     Parameters:
                | 
                |         oElem
                |             Intersection 
                |         iRank
                |             Index of one of the intersection features

        :param int i_rank:
        :return: Reference
        """
        return Reference(self.com_object.GetIntersection(i_rank))

    def get_kept_elem(self, i_rank: int) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Func GetKeptElem(long iRank) As Reference
                |     Gets the kept feature at a given index.
                | 
                |     Parameters:
                | 
                |         oElem
                |             Kept feature 
                |         iRank
                |             Index of one of the kept features

        :param int i_rank:
        :return: Reference
        """
        return Reference(self.com_object.GetKeptElem(i_rank))

    def get_nb_cutting_elem(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Func GetNbCuttingElem() As long
                |     Gets the number of cutting features.
                | 
                |     Parameters:
                | 
                |         oNbCuttingElem
                |             Number of cutting features

        :return: int
        """
        return self.com_object.GetNbCuttingElem()

    def get_nb_elements_to_keep(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Func GetNbElementsToKeep() As long
                |     Gets the number of elements to keep.
                | 
                |     Parameters:
                | 
                |         oNbElementsToKeep
                |             Number of elements to keep

        :return: int
        """
        return self.com_object.GetNbElementsToKeep()

    def get_nb_elements_to_remove(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Func GetNbElementsToRemove() As long
                |     Gets the number of elements to remove.
                | 
                |     Parameters:
                | 
                |         oNbElementsToRemove
                |             Number of elements to remove

        :return: int
        """
        return self.com_object.GetNbElementsToRemove()

    def get_orientation(self, i_rank: int) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Func GetOrientation(long iRank) As long
                |     Gets Orientation used to compute the split.
                | 
                |     Parameters:
                | 
                |         oOrientation
                |             Orientation 
                |         iRank
                |             index of the cutting feature oOrientation = 1 : SameOrientation = -1 : InvertOrientation = 2 : KoOrientation

        :param int i_rank:
        :return: int
        """
        return self.com_object.GetOrientation(i_rank)

    def get_other_side(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Func GetOtherSide() As Reference
                |     Gets the other side.
                | 
                |     Parameters:
                | 
                |         oElem
                |             Other side

        :return: Reference
        """
        return Reference(self.com_object.GetOtherSide())

    def get_removed_elem(self, i_rank: int) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Func GetRemovedElem(long iRank) As Reference
                |     Gets the removed feature at a given index.
                | 
                |     Parameters:
                | 
                |         oElem
                |             Removed feature 
                |         iRank
                |             Index of one of the removed features

        :param int i_rank:
        :return: Reference
        """
        return Reference(self.com_object.GetRemovedElem(i_rank))

    def invert_orientation(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub InvertOrientation()
                |     Inverts the orientation used to compute the split.

        :return: None
        """
        return self.com_object.InvertOrientation()

    def remove_cutting_elem(self, i_elem: Reference) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub RemoveCuttingElem(Reference iElem)
                |     Removes a cutting feature.
                | 
                |     Parameters:
                | 
                |         iElem
                |             cutting feature

        :param Reference i_elem:
        :return: None
        """
        return self.com_object.RemoveCuttingElem(i_elem.com_object)

    def remove_element_to_keep(self, i_rank: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub RemoveElementToKeep(long iRank)
                |     Removes an element from specifications.
                | 
                |     Parameters:
                | 
                |         iRank
                |             Index of the kept element.

        :param int i_rank:
        :return: None
        """
        return self.com_object.RemoveElementToKeep(i_rank)

    def remove_element_to_remove(self, i_rank: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub RemoveElementToRemove(long iRank)
                |     Removes an element from specifications.
                | 
                |     Parameters:
                | 
                |         iRank
                |             Index of the removed element.

        :param int i_rank:
        :return: None
        """
        return self.com_object.RemoveElementToRemove(i_rank)

    def set_orientation(self, i_rank: int, i_orientation: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub SetOrientation(long iRank,long iOrientation)
                |     Sets the orientation used to compute the split.
                | 
                |     Parameters:
                | 
                |         iOrientation
                |             Orientation 
                |         iRank
                |             index of the cutting feature iOrientation = 1 : SameOrientation = -1 : InvertOrientation = 2 : KoOrientation

        :param int i_rank:
        :param int i_orientation:
        :return: None
        """
        return self.com_object.SetOrientation(i_rank, i_orientation)

    def __repr__(self):
        return f'HybridShapeSplit(name="{ self.name }")'
