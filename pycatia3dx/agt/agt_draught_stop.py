"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.agt.agt_category_mngt import AGTCategoryMngt
from pycatia3dx.agt.agt_material_mngt import AGTMaterialMngt
from pycatia3dx.system.any_object import AnyObject


class AGTDraughtStop(AnyObject):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     AGTDraughtStop
                | 
                | The interface to access a DraughtStop.
                | To return the management object.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def agt_category_mngt(self) -> AGTCategoryMngt:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property AGTCategoryMngt() As AGTCategoryMngt (Read Only)
                |     Returns the AGTCategoryMngt object.
                | 
                |     Example:
                | 
                |          
                | 
                |              This example retrieves in ObjCategoryMngt the AGTCategoryMngt
                |              object of the AGTDraughtStop.
                |              
                | 
                |              Dim ObjCategoryMngt As AGTCategoryMngt 
                |              Set ObjCategoryMngt = ObjAGTDraughtStop.AGTCategoryMngt

        :return: AGTCategoryMngt
        """

        return AGTCategoryMngt(self.com_object.AGTCategoryMngt)

    @property
    def agt_material_mngt(self) -> AGTMaterialMngt:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property AGTMaterialMngt() As AGTMaterialMngt (Read Only)
                |     Returns the AGTMaterialMngt object.
                | 
                |     Example:
                | 
                |          
                | 
                |              This example retrieves in ObjMaterialMngt the AGTMaterialMngt
                |              object of the AGTDraughtStop.
                |              
                | 
                |              Dim ObjMaterialMngt As AGTMaterialMngt 
                |              Set ObjMaterialMngt = ObjAGTDraughtStop.AGTMaterialMngt

        :return: AGTMaterialMngt
        """

        return AGTMaterialMngt(self.com_object.AGTMaterialMngt)

    def __repr__(self):
        return f'AgtDraughtStop(name="{self.name}")'
