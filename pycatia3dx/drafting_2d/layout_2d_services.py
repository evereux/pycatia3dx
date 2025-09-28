"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class Layout2DServices(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     Layout2DServices

    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def import_from_drawing(self, i_objects: tuple, i_option: int, o_results: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Sub ImportFromDrawing(CATSafeArrayVariant iObjects,CatImportFromDrawingOption
                | iOption,CATSafeArrayVariant oResults)
                |     Import in a 2DLayout a drawing view array. Drawing views with generative
                |     behavior and detail views are not managed. Views are copied in active 2DLayout
                |     sheet. Last copied view is set as active view.
                | 
                |     Parameters:
                | 
                |         iObjects
                |             [in] The array of views to copy 
                |         iOption
                |             [in] This parameter is not used. All view content is copied and
                |             isolated. 
                |         oResults
                |             [inout] The array of views copied in 2DLayout 
                | 
                |     Example:
                |         The following example retrieves this service from
                |         2DLayout
                | 
                |          Dim myPart As CATIAPart
                |          Set myPart = CATIA.ActiveEditor.ActiveObject
                |          Dim MyRoot As Layout2DRoot
                |          Set MyRoot = myPart.GetItem("CATLayoutRoot")
                |          Dim layoutServices As Layout2DServices
                |          Set layoutServices = MyRoot.GetItem("CATLayout2DServices")

        :param tuple i_objects:
        :param int i_option:
        :param tuple o_results:
        :return: None
        """
        return self.com_object.ImportFromDrawing(i_objects, i_option, o_results)

    def __repr__(self):
        return f'Layout2DServices(name="{ self.name }")'
