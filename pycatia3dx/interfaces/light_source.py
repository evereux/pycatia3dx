"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-13 15:35:27.265802

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class LightSource(AnyObject):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     LightSource
                | 
                | Represents the light source.
                | The light source is the object that stores lighting data used by a viewer to
                | display a scene where a document is presented. Two kinds of light sources are
                | available: an infinite light source and a neon lighting system simulating a set
                | of parallel neon tubes.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def get_direction(self, o_direction: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Sub GetDirection(CATSafeArrayVariant oDirection)
                |     Returns the lighting direction as an array of 3 variants. This value is
                |     available with an infinite light source only.
                | 
                |     Example:
                |         This example gets the lighting direction of the LightSource light
                |         source to the direction with components (5,8,-2).
                | 
                |          Dim direction(2)
                |          LightSource.GetDirection direction

        :param tuple o_direction:
        :return: None
        """
        return self.com_object.GetDirection(o_direction)

    def put_direction(self, o_direction: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Sub PutDirection(CATSafeArrayVariant oDirection)
                |     Defines the lighting direction as an array of 3 variants. This value can be
                |     set with an infinite light source only.
                | 
                |     Example:
                |         This example defines the lighting direction of the LightSource light
                |         source to the direction with components (5,8,-2).
                | 
                |          LightSource.PutDirection Array(5,8,-2)


        :param tuple o_direction:
        :return: None
        """
        return self.com_object.PutDirection(o_direction)

    def __repr__(self):
        return f'LightSource(name="{self.name}")'
