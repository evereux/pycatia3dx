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


class StrConnections(Collection):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     StrConnections
                | 
                | Object for StrConnections
    
    """

    def __init__(self, com_object):
        # todo: what is the child_object for this Collection?
        super().__init__(com_object)
        self.com_object = com_object

    def item(self, i_index: CATVariant) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Item(CATVariant iIndex) As AnyObject
                |     Retrieves a connection object
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index of connection object 
                | 
                |     Example:
                | 
                | 
                |              This example retrieves  the first item from the list of
                |              StrConnections.
                |              
                | 
                |               Dim ObjStrConnections As ObjSfdConnectionSet
                |               Set ObjStrConnections = ObjSfdConnectionSet.GetConnections
                |               Set ObjConnection = ObjStrConnections.Item(1)

        :param CATVariant i_index:
        :return: AnyObject
        """
        return AnyObject(self.com_object.Item(i_index))

    def __repr__(self):
        return f'StrConnections(name="{self.name}")'
