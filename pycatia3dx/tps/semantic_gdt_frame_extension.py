"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.tps.datum_simple import DatumSimple


class SemanticGDTFrameExtension(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SemanticGDTFrameExtension
                | 
                | Interface to parse Semantic GDT auxiliary feature.
                | 
                | Its allows getting information of Intersection Plane, Orientation Plane,
                | Collection Plane or Direction Feature. (ISO Standard only).
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def direction_specification(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property DirectionSpecification() As CATBSTR (Read Only)
                |     Gets the direction specification.
                | 
                |     Parameters:
                | 
                |         oDirSpec
                |             The Direction of Specification.
                |             List of legal values are the same as the ones obtained using
                |             SuperType property (equals to "FTA_Orientation") from Annotation2 augmented by
                |             specific type "FTA_Symmetry":
                |             oDirSpec = "FTA_Parallelism"
                |             oDirSpec = "FTA_Perpendicularity"
                |             oDirSpec = "FTA_Angularity"
                |             oDirSpec = "FTA_Symmetry"

        :return: str
        """

        return self.com_object.DirectionSpecification

    @property
    def type(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Type() As CATBSTR (Read Only)
                |     Gets the Type.
                | 
                |     Parameters:
                | 
                |         oType
                |             The Type.
                |             List of types available:
                |             Type = "FTA_IntersectionPlane"
                |             Type = "FTA_OrientationPlane"
                |             Type = "FTA_CollectionPlane"
                |             Type = "FTA_DirectionFeature"

        :return: str
        """

        return self.com_object.Type

    def direction_reference(self) -> DatumSimple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func DirectionReference() As DatumSimple
                |     Returns the Datum Feature used as reference to specify auxiliary
                |     feature.
                | 
                |     Parameters:
                | 
                |         oDatumFeature
                |             The Datum Feature.

        :return: DatumSimple
        """
        return DatumSimple(self.com_object.DirectionReference())

    def orientation(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Orientation() As double
                |     Retrieves orientation angle when DirectionSpecification is
                |     "FTA_Angularity".
                |     These values are expressed in degrees.
                | 
                |     Parameters:
                | 
                |         oOrientation
                |             The orientation value with respect to Datum Feature reference.

        :return: float
        """
        return self.com_object.Orientation()

    def __repr__(self):
        return f'SemanticGdtFrameExtension(name="{ self.name }")'
