"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.agt.covering import Covering
from pycatia3dx.system.collection import Collection
from pycatia3dx.types.general import CATVariant


class Coverings(Collection):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     Coverings
                | 
                | Object for Coverings.
                | To retrieve a Covering from collection.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=Covering)
        self.com_object = com_object

    def item(self, i_index: CATVariant) -> Covering:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Item(CATVariant iIndex) As Covering
                |     Retrieves a Covering from the collection of Covering.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index of Covering 
                | 
                |     Example:
                | 
                | 
                |              This example retrieves Covering from the list of
                |              Coverings
                |              
                | 
                |              Dim myPart as CATIAPart
                |              Set myPart = CATIA.ActiveEditor.ActievObject
                |              Dim MyAGTRoot As AGTRoot
                |              Set MyAGTRoot = myPart.GetItem("CATAGTRoot")
                |              'Get a second Covering from the list of Covering by
                |              index
                |              Dim CoveringByIndex As AGTCoverings
                |              Set CoveringByIndex = MyAGTRoot.Coverings.Item(2)
                |              'Get a Covering named "MyCovering.2" from the list of Covering by
                |              name
                |              Dim CoveringByName As AGTCoverings
                |              Set CoveringByName = MyAGTRoot.Coverings.Item("MyCovering.2")

        :param CATVariant i_index:
        :return: Covering
        """
        return Covering(self.com_object.Item(i_index))

    def __repr__(self):
        return f'Coverings(name="{self.name}")'
