"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-27 14:29:47.477239

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.mmr_automation_interfaces.hybrid_shape import HybridShape
from pycatia3dx.mode.reference import Reference


class HybridShapeSection(HybridShape):

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
                |                         HybridShapeSection
                | 
                | Interface to hybrid shape section feature.
                | Role: Allows you to access data of the Hybrid Shape Section
                | feature.
                | 
                | See also:
                |     HybridShapeFactory.AddNewSection
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def section_plane(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property SectionPlane() As Reference
                |     Returns or sets the section plane..
                | 
                |     Parameters:
                | 
                |         oPlane
                |             The section oPlane
                | 
                |             Example:
                |                 This example retrieves in RefPlane the plane of the
                |                 section
                | 
                |                  Dim RefPlane As Reference 
                |                  Set RefPlane = HybridShapeSection.SectionPlane

        :return: Reference
        """

        return Reference(self.com_object.SectionPlane)

    @section_plane.setter
    def section_plane(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.SectionPlane = value

    def __repr__(self):
        return f'HybridShapeSection(name="{ self.name }")'
