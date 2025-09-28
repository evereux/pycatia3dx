"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-27 14:29:47.477239

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.mmr_automation_interfaces.hybrid_shape import HybridShape
from pycatia3dx.mode.reference import Reference


class HybridShapeSweep(HybridShape):

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
                |                         HybridShapeSweep
                | 
                | Represents the hybrid shape Sweep feature object.
                | Role: Declare hybrid shape Sweep root feature object. All interfaces for
                | different type of sweep derives HybridShapeSweep.
                | 
                | Use the CATIAHybridShapeFactory to create a HybridShapeSweep
                | objects.
                | 
                | See also:
                |     HybridShapeFactory
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def c0_vertices_mode(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property C0VerticesMode() As boolean
                |     Returns or sets the management mode of C0 vertices as twisted
                |     areas.
                |     TRUE or FALSE.

        :return: bool
        """

        return self.com_object.C0VerticesMode

    @c0_vertices_mode.setter
    def c0_vertices_mode(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.C0VerticesMode = value

    @property
    def fill_twisted_areas(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property FillTwistedAreas() As long
                |     Returns or sets the fill twisted areas mode.

        :return: int
        """

        return self.com_object.FillTwistedAreas

    @fill_twisted_areas.setter
    def fill_twisted_areas(self, value: int):
        """
        :param int value:
        """

        self.com_object.FillTwistedAreas = value

    @property
    def setback_value(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property SetbackValue() As double
                |     Returns or sets the setback value.

        :return: float
        """

        return self.com_object.SetbackValue

    @setback_value.setter
    def setback_value(self, value: float):
        """
        :param float value:
        """

        self.com_object.SetbackValue = value

    def add_cut_points(self, i_element1: Reference, i_element2: Reference) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub AddCutPoints(Reference iElement1,Reference iElement2)
                |     Sets two cut points on the master guide. These points define a zone to be
                |     kept on the final swept surface.
                | 
                |     Parameters:
                | 
                |         iElement1
                |             First / start cut point. 
                |         iElement2
                |             Second / end cut point.

        :param Reference i_element1:
        :param Reference i_element2:
        :return: None
        """
        return self.com_object.AddCutPoints(i_element1.com_object, i_element2.com_object)

    def add_fill_points(self, i_element1: Reference, i_element2: Reference) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub AddFillPoints(Reference iElement1,Reference iElement2)
                |     Sets two fill points on the master guide. These points define a zone to be
                |     filled on the final swept surface.
                | 
                |     Parameters:
                | 
                |         iElement1
                |             First / start fill point. 
                |         iElement2
                |             Second / end fill point.

        :param Reference i_element1:
        :param Reference i_element2:
        :return: None
        """
        return self.com_object.AddFillPoints(i_element1.com_object, i_element2.com_object)

    def get_cut_point(self, i_rank: int) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Func GetCutPoint(long iRank) As Reference

        :param int i_rank:
        :return: Reference
        """
        return Reference(self.com_object.GetCutPoint(i_rank))

    def get_fill_point(self, i_rank: int) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Func GetFillPoint(long iRank) As Reference

        :param int i_rank:
        :return: Reference
        """
        return Reference(self.com_object.GetFillPoint(i_rank))

    def remove_all_cut_points(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub RemoveAllCutPoints()
                |     Removes all cut points.

        :return: None
        """
        return self.com_object.RemoveAllCutPoints()

    def remove_all_fill_points(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub RemoveAllFillPoints()
                |     Removes all fill points.

        :return: None
        """
        return self.com_object.RemoveAllFillPoints()

    def __repr__(self):
        return f'HybridShapeSweep(name="{ self.name }")'
