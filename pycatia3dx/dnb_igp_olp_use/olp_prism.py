"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.dnb_igp_olp_use.olp_shape import OLPShape
from pycatia3dx.dnb_igp_olp_use.olp_transform import OLPTransform


class OLPPrism(OLPShape):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     DNBIgpOlpUseItf.OlpShape
                |                         OlpPrism
                | 
                | A 3D prism.
                | 
                | This interface can only be used by a translator within the Robotics Off-line
                | Programming (OLP) Download or Upload command.
                | The prism is constructed of 2 identical parallel polygons, joined by
                | rectangular faces. This object is used with OlpCartesianSafetyZone and
                | OlpToolVolume
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def height(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Height() As double
                |     Get/Set the height in meters.

        :return: float
        """

        return self.com_object.Height

    @height.setter
    def height(self, value: float):
        """
        :param float value:
        """

        self.com_object.Height = value

    @property
    def num_base_points(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property NumBasePoints() As long (Read Only)
                |     Get the number of base points.

        :return: int
        """

        return self.com_object.NumBasePoints

    def add_base_point(self, i_origin: int) -> OLPTransform:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func AddBasePoint(DELOlpPositionRef iOrigin) As OlpTransform
                |     Append a corner point of the base polygon.
                | 
                |     Parameters:
                | 
                |         iOrigin
                |             The origin of the coordinate system being used by the translator.
                |             For tool volumes, this should be delOlpMount, for Cartesian Safety Zones it
                |             should be one of delOlpWorld, delOlpStation, or delOlpRailOrigin
                |             
                | 
                |     Returns:
                |         The location.

        :param int i_origin:
        :return: OLPTransform
        """
        return OLPTransform(self.com_object.AddBasePoint(i_origin))

    def get_base_point(self, i_index: int, i_origin: int) -> OLPTransform:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetBasePoint(long iIndex,DELOlpPositionRef iOrigin) As
                | OlpTransform
                |     Get a corner of the base polygon.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index of the point. 
                |         iOrigin
                |             The origin of the coordinate system being used by the translator.
                |             For tool volumes, this should be delOlpMount, for Cartesian Safety Zones it
                |             should be one of delOlpWorld, delOlpStation, or delOlpRailOrigin
                |             
                | 
                |     Returns:
                |         The location.

        :param int i_index:
        :param int i_origin:
        :return: OLPTransform
        """
        return OLPTransform(self.com_object.GetBasePoint(i_index, i_origin))

    def remove_base_point(self, i_index: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub RemoveBasePoint(long iIndex)
                |     Remove a corner of the base polygon.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index of the point.

        :param int i_index:
        :return: None
        """
        return self.com_object.RemoveBasePoint(i_index)

    def set_base_point(self, i_index: int, i_origin: int, i_location: OLPTransform) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetBasePoint(long iIndex,DELOlpPositionRef iOrigin,OlpTransform
                | iLocation)
                |     Set a corner of the base polygon.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index of the point. 
                |         iOrigin
                |             The origin of the coordinate system being used by the translator.
                |             For tool volumes, this should be delOlpMount, for Cartesian Safety Zones it
                |             should be one of delOlpWorld, delOlpStation, or delOlpRailOrigin
                |             
                |         iLocation
                |             The location. 

        :param int i_index:
        :param int i_origin:
        :param OLPTransform i_location:
        :return: None
        """
        return self.com_object.SetBasePoint(i_index, i_origin, i_location.com_object)

    def __repr__(self):
        return f'OLPPrism(name="{ self.name }")'
