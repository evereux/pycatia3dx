"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.dnb_igp_olp_use.olp_shape import OLPShape
from pycatia3dx.dnb_igp_olp_use.olp_transform import OLPTransform


class OLPCapsule(OLPShape):

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
                |                         OlpCapsule
                | 
                | A 3D Capsule shape.
                | 
                | This interface can only be used by a translator within the Robotics Off-line
                | Programming (OLP) Download or Upload command.
                | A capsule is a cylinder with hemispheres on the ends. This object is used with
                | OlpCartesianSafetyZone and OlpToolVolume
    
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
                |     The height is the distance between the centers of the spheres at either
                |     end.

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
    def radius(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Radius() As double
                |     Get/Set the radius capsule in meters.

        :return: float
        """

        return self.com_object.Radius

    @radius.setter
    def radius(self, value: float):
        """
        :param float value:
        """

        self.com_object.Radius = value

    def get_base_center(self, i_origin: int) -> OLPTransform:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetBaseCenter(DELOlpPositionRef iOrigin) As OlpTransform
                |     Get the center of the sphere at the base of the cylinder.
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
        return OLPTransform(self.com_object.GetBaseCenter(i_origin))

    def set_base_center(self, i_origin: int, i_location: OLPTransform) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetBaseCenter(DELOlpPositionRef iOrigin,OlpTransform
                | iLocation)
                |     Set the center of the circle at the base of the cylinder.
                | 
                |     Parameters:
                | 
                |         iOrigin
                |             The origin of the coordinate system being used by the translator.
                |             For tool volumes, this should be delOlpMount, for Cartesian Safety Zones it
                |             should be one of delOlpWorld, delOlpStation, or delOlpRailOrigin
                |             
                |         iLocation
                |             The location. 

        :param int i_origin:
        :param OlpTransform i_location:
        :return: None
        """
        return self.com_object.SetBaseCenter(i_origin, i_location.com_object)

    def __repr__(self):
        return f'OLPCapsule(name="{ self.name }")'
