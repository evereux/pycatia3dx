"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.dnb_igp_olp_use.olp_shape import OLPShape


class OLPCartesianSafetyZone(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     OlpCartesianSafetyZone
                | 
                | A Cartesian safety zone.
                | 
                | This interface can only be used by a translator within the Robotics Off-line
                | Programming (OLP) Download or Upload command.
                | This object can be retrieved using OlpCartesianSafetyZones
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def active(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Active() As boolean
                |     Get/Set whether the zone is active.

        :return: bool
        """

        return self.com_object.Active

    @active.setter
    def active(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.Active = value

    @property
    def index(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Index() As long
                |     Get the zone index.
                |     In some robot languages an index is used to identify the zone. If the Index
                |     property is not set (IndexIsSet returns FALSE), then getting the Index will
                |     fail.

        :return: int
        """

        return self.com_object.Index

    @index.setter
    def index(self, value: int):
        """
        :param int value:
        """

        self.com_object.Index = value

    @property
    def index_set(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property IndexSet() As boolean
                |     Get whether an index is set for the zone.
                |     If not set, then getting the Index property will fail.

        :return: bool
        """

        return self.com_object.IndexSet

    @index_set.setter
    def index_set(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.IndexSet = value

    @property
    def safe_inside(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property SafeInside() As boolean
                |     Get/Set whether the safe state is when the robot is inside or outside the
                |     zone.

        :return: bool
        """

        return self.com_object.SafeInside

    @safe_inside.setter
    def safe_inside(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.SafeInside = value

    @property
    def shape_type(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ShapeType() As CATBSTR
                |     Get/Set the zone shape type.
                |     Can be one of "Prism" or "Cylinder". When set, the existing shape (if any)
                |     is deleted and a the new shape of this type is created.

        :return: str
        """

        return self.com_object.ShapeType

    @shape_type.setter
    def shape_type(self, value: str):
        """
        :param str value:
        """

        self.com_object.ShapeType = value

    def get_shape(self) -> OLPShape:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetShape() As OlpShape
                |     Get the zone shape.
                |     Shape is NULL during upload until ShapeType is set. 

        :return: OLPShape
        """
        return OLPShape(self.com_object.GetShape())

    def __repr__(self):
        return f'OLPCartesianSafetyZone(name="{ self.name }")'
