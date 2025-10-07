"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.dnb_igp_olp_use.olp_shape import OLPShape
from pycatia3dx.dnb_igp_olp_use.olp_transform import OLPTransform


class OLPSphere(OLPShape):

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
                |                         OlpSphere
                | 
                | A 3D sphere.
                | 
                | This interface can only be used by a translator within the Robotics Off-line
                | Programming (OLP) Download or Upload command.
                | This object is used with OlpCartesianSafetyZone and
                | OlpToolVolume
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def radius(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Radius() As double
                |     Get/Set the radius in meters.

        :return: float
        """

        return self.com_object.Radius

    @radius.setter
    def radius(self, value: float):
        """
        :param float value:
        """

        self.com_object.Radius = value

    def get_center(self, i_origin: int) -> OLPTransform:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetCenter(DELOlpPositionRef iOrigin) As OlpTransform
                |     Get the center of the sphere.
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
        return OLPTransform(self.com_object.GetCenter(i_origin))

    def set_center(self, i_origin: int, i_location: OLPTransform) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetCenter(DELOlpPositionRef iOrigin,OlpTransform
                | iLocation)
                |     Set the center of the sphere.
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
        :param OLPTransform i_location:
        :return: None
        """
        return self.com_object.SetCenter(i_origin, i_location.com_object)

    def __repr__(self):
        return f'OLPSphere(name="{ self.name }")'
