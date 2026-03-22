"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.agt.agt_sill import AGTSill
from pycatia3dx.system.collection import Collection
from pycatia3dx.types.general import CATVariant


class AGTSills(Collection):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     AGTSills
                | 
                | Object for AGTSills.
                | To retrieve Sill from collection.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=AGTSill)
        self.com_object = com_object

    def item(self, i_index: CATVariant) -> AGTSill:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Item(CATVariant iIndex) As AGTSill
                |     Retrieves a Sill from the collection of Sill.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index of AGTSill 
                | 
                |     Example:
                |
                |              This example retrieves in ThisSill the second Sill,
                |              
                |              and in ThisSill the Sill named MySill.2 in the Sill collection.
                |              
                |              Dim myPart as CATIAPart
                |              Set myPart = CATIA.ActiveEditor.ActievObject
                |              Dim ThisAGTRoot As AGTRoot
                |              Set ThisAGTRoot = myPart.GetItem("CATAGTRoot")
                |              Dim ThisSill As AGTSill
                |              Set ThisSill = ThisAGTRoot.Sills.Item(2)
                |              Dim ThisSill As AGTSill
                |              Set ThisSill = ThisAGTRoot.Sills.Item("MySill.2")

        :param CATVariant i_index:
        :return: AGTSill
        """
        return AGTSill(self.com_object.Item(i_index))

    def __repr__(self):
        return f'AgtSills(name="{self.name}")'
