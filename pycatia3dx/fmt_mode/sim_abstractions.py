"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.system.collection import Collection
from pycatia3dx.types.general import CATVariant


class SimAbstractions(Collection):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     SimAbstractions

    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def add(self, i_type: str) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Add(CATBSTR iType) As CATBaseDispatch
                |     Creates a new abstraction and adds it to the collection.
                | 
                |     Parameters:
                | 
                |         iType
                |             The type of abstraction to create. 
                | 
                |     Returns:
                |         The created abstraction.

        :param str i_type:
        :return: AnyObject
        """
        return self.com_object.Add(i_type)

    def item(self, i_index: CATVariant) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Item(CATVariant iIndex) As CATBaseDispatch
                |     Returns an abstraction using its index or its name from the
                |     collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the abstraction to retrieve from the
                |             collection of abstractions.
                |             As a numeric, this index is the rank of the abstraction in the
                |             collection. The index of the first abstraction in the collection is 1, and the
                |             index of the last abstraction is Count.
                |             As a string, it is the name you assigned to the abstraction using
                |             the Name object property. 
                | 
                |     Returns:

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
                |     Removes an abstraction using its index or its name from the
                |     collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the abstraction to retrieve from the
                |             collection of abstractions.
                |             As a numeric, this index is the rank of the abstraction in the
                |             collection. The index of the first abstraction in the collection is 1, and the
                |             index of the last abstraction is Count.
                |             As a string, it is the name you assigned to the abstraction using
                |             the Name object property.

        :param CATVariant i_index:
        :return: None
        """
        return self.com_object.Remove(i_index)

    def __repr__(self):
        return f'SimAbstractions(name="{self.name}")'
