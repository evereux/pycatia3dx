"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.dnb_igp_olp_use.olp_shape import OLPShape


class OLPToolVolume(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     OlpToolVolume
                | 
                | A simplified tool volume.
                | 
                | This interface can only be used by a translator within the Robotics Off-line
                | Programming (OLP) Download or Upload command.
                | This object can be retrieved using OlpToolVolumes
    
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
    def num_shapes(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property NumShapes() As long (Read Only)
                |     Get the number of shapes.

        :return: int
        """

        return self.com_object.NumShapes

    def add_shape(self, i_type: str) -> OLPShape:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func AddShape(CATBSTR iType) As OlpShape
                |     Append a new shape.
                | 
                |     Parameters:
                | 
                |         iType
                |             Can be one of "Sphere", "Box", or "Capsule". 
                | 
                |     Returns:
                |         The new shape.

        :param str i_type:
        :return: OLPShape
        """
        return OLPShape(self.com_object.AddShape(i_type))

    def get_shape(self, i_index: int) -> OLPShape:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetShape(long iIndex) As OlpShape
                |     Get one of the shapes.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index of the shape. 
                | 
                |     Returns:
                |         The shape.

        :param int i_index:
        :return: OLPShape
        """
        return OLPShape(self.com_object.GetShape(i_index))

    def remove_shape(self, i_index: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub RemoveShape(long iIndex)
                |     Remove shape.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index of the shape. 

        :param int i_index:
        :return: None
        """
        return self.com_object.RemoveShape(i_index)

    def __repr__(self):
        return f'OLPToolVolume(name="{ self.name }")'
