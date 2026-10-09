"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.drafting.drawing_gen_view_properties import DrawingGenViewProperties
from pycatia3dx.interfaces.service import Service


class DrawingGenService(Service):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     InfInterfaces.Service
                |                         DrawingGenService
                | 
                | Interface representing the service to retrieve the generative view
                | properties.
                | Application.GetSessionService("CATDrawingGenService")
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def drawing_gen_view_prop(self) -> DrawingGenViewProperties:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property DrawingGenViewProp() As DrawingGenViewProperties (Read
                | Only)
                |     Returns a generative view properties.
                |     Role: The generative view properties contains the whole of parameters
                |     managing the generative view representation. The values are extracted from the
                |     drawing settings.

        :return: DrawingGenViewProperties
        """

        return DrawingGenViewProperties(self.com_object.DrawingGenViewProp)

    def check_view_link_integrity(self, i_info_on_view_links: tuple) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2026-02-08 14:05:01.675948))
                | Func CheckViewLinkIntegrity(CATSafeArrayVariant iInfoOnViewLinks) As
                | boolean
                |     Checks the integrity of elements to be pointed by a generative
                |     view
                |     Role: This service tests the integrity of the information contained in the
                |     list iInfoOnViewLinks: Checks if the elements will be pointed by the generative
                |     view are referenced by the same product structure. Checks if the order of the
                |     elements is respected when a link to a PartBody must be
                |     created.
                |
                |     Parameters:
                |
                |         iInfoOnViewLinks
                |             The List of links to check.

        :param tuple i_info_on_view_links:
        :return: bool
        """
        # convert to list of com_objects
        new_list = []
        for item in i_info_on_view_links:
            try:
                new_list.append(item.com_object)
            except AttributeError:
                continue
        return self.com_object.CheckViewLinkIntegrity(new_list)

    def __repr__(self):
        return f'DrawingGenService(name="{self.name}")'
