"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.mode.reference import Reference
from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.srs.srs_bounding_box import SrsBoundingBox
from pycatia3dx.srs.srs_centre_line import SrsCentreLine
from pycatia3dx.srs.srs_grid_sets import SrsGridSets
from pycatia3dx.srs.srs_mid_ship import SrsMidShip


class SrsPart(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SrsPart
                | 
                | Role: Allows accessing of Part's data.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def bounding_box(self) -> SrsBoundingBox:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property BoundingBox() As SrsBoundingBox (Read Only)

        :return: SrsBoundingBox
        """

        return SrsBoundingBox(self.com_object.BoundingBox)

    @property
    def centre_line(self) -> SrsCentreLine:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property CentreLine() As SrsCentreLine (Read Only)

        :return: SrsCentreLine
        """

        return SrsCentreLine(self.com_object.CentreLine)

    @property
    def mid_ship(self) -> SrsMidShip:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property MidShip() As SrsMidShip (Read Only)

        :return: SrsMidShip
        """

        return SrsMidShip(self.com_object.MidShip)

    @property
    def reference_surface(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ReferenceSurface() As Reference (Read Only)

        :return: Reference
        """

        return Reference(self.com_object.ReferenceSurface)

    @property
    def srs_grid_sets(self) -> SrsGridSets:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property SrsGridSets() As SrsGridSets (Read Only)

        :return: SrsGridSets
        """

        return SrsGridSets(self.com_object.SrsGridSets)

    def __repr__(self):
        return f'SrsPart(name="{ self.name }")'
