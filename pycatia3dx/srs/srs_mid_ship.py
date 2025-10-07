"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.srs.srs_grid_face import SrsGridFace


class SrsMidShip(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SrsMidShip
                | 
                | Role: Allows accessing of MidShip's data.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def reference_plane(self) -> SrsGridFace:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ReferencePlane() As SrsGridFace (Read Only)

        :return: SrsGridFace
        """

        return SrsGridFace(self.com_object.ReferencePlane)

    def get_front_orientation_direction(self, o_direction: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetFrontOrientationDirection(CATSafeArrayVariant
                | oDirection)

        :param tuple o_direction:
        :return: None
        """
        return self.com_object.GetFrontOrientationDirection(o_direction)

    def __repr__(self):
        return f'SrsMidShip(name="{ self.name }")'
