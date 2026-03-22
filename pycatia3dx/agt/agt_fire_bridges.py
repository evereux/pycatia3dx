"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.agt.agt_fire_bridge import AGTFireBridge
from pycatia3dx.system.collection import Collection
from pycatia3dx.types.general import CATVariant


class AGTFireBridges(Collection):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     AGTFireBridges
                | 
                | Object for AGTFireBridges.
                | To retrieve FireBridge from collection.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=AGTFireBridge)
        self.com_object = com_object

    def item(self, i_index: CATVariant) -> AGTFireBridge:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Item(CATVariant iIndex) As AGTFireBridge
                |     Retrieves a FireBridge from the collection of FireBridge.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index of FireBridge 
                | 
                |     Example:
                | 
                | 
                |              This example retrieves in ThisFireBridge the second FireBridge,
                |              
                |              and in ThisFireBridge the FireBridge named MyFireBridge.2 in the
                |              FireBridge collection. 
                |              
                | 
                |              Dim myPart as CATIAPart
                |              Set myPart = CATIA.ActiveEditor.ActievObject
                |              Dim ThisAGTRoot As AGTRoot
                |              Set ThisAGTRoot = myPart.GetItem("CATAGTRoot")
                |              Dim ThisFireBridge As AGTFireBridge
                |              Set ThisFireBridge = ThisAGTRoot.FireBridges.Item(2)
                |              Dim ThisFireBridge As AGTFireBridge
                |              Set ThisFireBridge = ThisAGTRoot.FireBridges.Item("MyFireBridge.2")

        :param CATVariant i_index:
        :return: AGTFireBridge
        """
        return AGTFireBridge(self.com_object.Item(i_index))

    def __repr__(self):
        return f'AgtFireBridges(name="{self.name}")'
