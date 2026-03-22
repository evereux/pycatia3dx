"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.system.collection import Collection
from pycatia3dx.plm_validation.val_concern import VALConcern
from pycatia3dx.types.general import CATVariant


class VALConcerns(Collection):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     VALConcerns
                | 
                | A collection of Concerns.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=VALConcern)
        self.com_object = com_object

    def add(self) -> VALConcern:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Add() As VALConcern
                |     Creates a Concern and adds it to the Concern collection.
                | 
                |     Returns:
                |         The created Concern 
                |     Example:
                | 
                |             This example creates a new Concern in the cConcerns
                |             collection.
                |             
                | 
                |             Dim oNewConcernText As Concern
                |             Set oNewConcernText = cConcerns.Add

        :return: VALConcern
        """
        return VALConcern(self.com_object.Add())

    def item(self, i_index: CATVariant) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Item(CATVariant iIndex) As CATBaseDispatch
                |     Returns a Concern using its index from the Concerns
                |     collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the Concern to retrieve from the
                |             collection of Concerns. As a numerics, this index is the rank of the Concern in
                |             the collection. The index of the first Concern in the collection is 1, and the
                |             index of the last Concern is Count. As a string, it is the name you assigned to
                |             the Concern. 
                | 
                |     Returns:
                |         The retrieved Concern 
                |     Example:
                | 
                |             This example retrieves in oConcern1 the ninth
                |             Concern,
                |             and in oConcern2 the Concern named
                |             Concern3 from the cConcerns collection. 
                |             
                | 
                |             Dim oConcern1 As Concern
                |             Set oConcern1 = cConcerns.Item(9)
                |             Dim oConcern2 As Concern
                |             Set oConcern2 = cConcerns.Item("Concern3")

        :param CATVariant i_index:
        :return: AnyObject
        """
        return self.com_object.Item(i_index)

    def remove(self, i_index: CATVariant) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub Remove(CATVariant iIndex)
                |     Removes a Concern from the Concerns collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the Concern to retrieve from the
                |             collection of Concerns. As a numerics, this index is the rank of the Concern in
                |             the collection. The index of the first Concern in the collection is 1, and the
                |             index of the last Concern is Count. As a string, it is the name you assigned to
                |             the Concern. 
                | 
                |     Example:
                | 
                |             The following example removes the tenth Concern and the Concern
                |             named
                |             Concern2 from the cConcerns collection.
                |             
                | 
                |             cConcerns.Remove(10)
                |             cConcerns.Remove("Concern2")

        :param CATVariant i_index:
        :return: None
        """
        return self.com_object.Remove(i_index)

    def __repr__(self):
        return f'ValConcerns(name="{self.name}")'
