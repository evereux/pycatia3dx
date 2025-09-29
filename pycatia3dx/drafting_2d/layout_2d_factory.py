"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.drafting_2d.layout_2d_root import Layout2DRoot
from pycatia3dx.system.any_object import AnyObject


class Layout2DFactory(AnyObject):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     Layout2DFactory

    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def create_2d_layout(self, i_standard_name: str) -> Layout2DRoot:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Create2DLayout(CATBSTR iStandardName) As Layout2DRoot
                |     Create the 2DLayout associated to the 3D mechanical feature tha implement
                |     this interface. E.g. a Mechanical Part.
                | 
                |     Parameters:
                | 
                |         CATBSTR
                |             iStandardName The standard name to apply to the new layout.
                |             
                |         oLayout
                |             The created 2DLayout. This feature is unique for a given 3D context
                |             feature. Consequently requesting this interface on a 3D feature that is already
                |             associated to a 2DLayout feature will fail. You must first request for any
                |             existing 2DLayout via AnyObject.GetItem method using CATLayoutRoot key
                |             parameter to check for 2DLayout pre-existing feature as follow
                |             :
                | 
                |              Dim myPart As CATIAPart
                |              Set myPart = CATIA.ActiveEditor.ActiveObject
                |              Dim MyRoot As Layout2DRoot
                |              Set MyRoot = myPart.GetItem("CATLayoutRoot")
                |              if MyRoot Is Nothing then
                |                Dim MyRootFact As Layout2DFactory
                |                Set MyRootFact = myPart.GetItem("CATLayoutRootFactory")
                |                Set MyRoot = MyRootFact.Create2DLayout("ISO_3D")
                |              end if

        :param str i_standard_name:
        :return: Layout2DRoot
        """
        return Layout2DRoot(self.com_object.Create2DLayout(i_standard_name))

    def __repr__(self):
        return f'Layout2DFactory(name="{self.name}")'
