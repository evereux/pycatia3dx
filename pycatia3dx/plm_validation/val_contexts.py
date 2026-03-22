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


class VALContexts(Collection):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     VALContexts
                | 
                | A collection of Contexts.
    
    """

    def __init__(self, com_object):
        # todo: What is the child_object for the Collection?
        super().__init__(com_object)
        self.com_object = com_object

    def add(self, i_context: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub Add(AnyObject iContext)
                |     Creates a Context and adds it to the Context collection.
                | 
                |     Parameters:
                | 
                |         iContext
                |             The Context 
                | 
                |     Example:
                | 
                |             This example creates a new Context in the cContexts
                |             collection.
                |
                |             Dim oNewContextText As Context
                |             Set oNewContextText = cContexts.Add

        :param AnyObject i_context:
        :return: None
        """
        return self.com_object.Add(i_context.com_object)

    def item(self, i_index: CATVariant) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Item(CATVariant iIndex) As CATBaseDispatch
                |     Returns a Context using its index from the Contexts
                |     collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the Context to retrieve from the
                |             collection of Contexts. As a numerics, this index is the rank of the Context in
                |             the collection. The index of the first Context in the collection is 1, and the
                |             index of the last Context is Count. As a string, it is the name you assigned to
                |             the Context. 
                | 
                |     Returns:
                |         The retrieved Context 
                |     Example:
                | 
                |             This example retrieves in oContext1 the ninth
                |             Context,
                |             and in oContext2 the Context named
                |             Context3 from the cContexts collection. 
                |             
                | 
                |             Dim oContext1 As Context
                |             Set oContext1 = cContexts.Item(9)
                |             Dim oContext2 As Context
                |             Set oContext2 = cContexts.Item("Context3")

        :param CATVariant i_index:
        :return: AnyObject
        """
        return self.com_object.Item(i_index)

    def load(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub Load()
                |     Loads all Contexts from the Contexts collection.
                | 
                |     Example:
                | 
                |             The following example loads all Contexts from the cContexts
                |             collection.
                |             
                | 
                |             cContexts.Load

        :return: None
        """
        return self.com_object.Load()

    def remove(self, i_index: CATVariant) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub Remove(CATVariant iIndex)
                |     Removes a Context from the Contexts collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the Context to retrieve from the
                |             collection of Contexts. As a numerics, this index is the rank of the Context in
                |             the collection. The index of the first Context in the collection is 1, and the
                |             index of the last Context is Count. As a string, it is the name you assigned to
                |             the Context. 
                | 
                |     Example:
                | 
                |             The following example removes the tenth Context and the Context
                |             named
                |             Context2 from the cContexts collection.
                |
                |             cContexts.Remove(10)
                |             cContexts.Remove("Context2")

        :param CATVariant i_index:
        :return: None
        """
        return self.com_object.Remove(i_index)

    def __repr__(self):
        return f'ValContexts(name="{self.name}")'
