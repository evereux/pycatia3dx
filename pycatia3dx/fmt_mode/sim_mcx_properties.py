"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.fmt_mode.sim_fem_root import SimFemRoot
from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.system.collection import Collection
from pycatia3dx.types.general import CATVariant


class SimMcxProperties(Collection):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     SimMCXProperties
                | 
                | Represents the collection of MCX properties.
                | 
                | Example:
                | 
                |      This example shows how to retrieve the collection of MCX properties from
                |      an engineering connection.
                |
                |      Dim myMCXConnection As EngConnection
                |      Set myMCXConnection = ...
                |      Dim myMCXProperties As SimMCXProperties
                |      Set myMCXProperties = myMCXConnection.GetItem("SimMCXProperties")
                |
                | See also:
                |     EngConnections, EngConnection
    
    """

    def __init__(self, com_object):
        # todo: what is the child_object of this collection?
        super().__init__(com_object)
        self.com_object = com_object

    def add(self, i_type: str, i_fem_root: SimFemRoot) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Add(CATBSTR iType,SimFemRoot iFemRoot) As CATBaseDispatch
                |     Creates a new MCX property and adds it to the collection.
                | 
                |     Parameters:
                | 
                |         iType:
                |             The type of MCX property to create. 
                | 
                |     Returns:
                |         The created MCX property.

        :param str i_type:
        :param SimFemRoot i_fem_root:
        :return: AnyObject
        """
        return self.com_object.Add(i_type, i_fem_root.com_object)

    def item(self, i_index: CATVariant) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Item(CATVariant iIndex) As CATBaseDispatch
                |     Returns a MCX property using its index or its name from the
                |     collection.
                | 
                |     Parameters:
                | 
                |         iIndex:
                |             The index or the name of the MCX property to retrieve from the
                |             collection of MCX connection.
                |             As a numeric, this index is the rank of the MCX property in the
                |             collection. The index of the first MCX property in the collection is 1, and the
                |             index of the last MCX property is Count.
                |             As a string, it is the name you assigned to the MCX property using
                |             the Name object property. 
                | 
                |     Returns:
                |         The retrieved MCX property.

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
                |     Removes a MCX Property using its index or its name from the
                |     collection.
                | 
                |     Parameters:
                | 
                |         iIndex:
                |             The index or the name of the MCX property to retrieve from the
                |             collection.
                |             As a numeric, this index is the rank of the MCX property in the
                |             collection. The index of the first MCX property in the collection is 1, and the
                |             index of the last MCX property is Count.
                |             As a string, it is the name you assigned to the MCX property using
                |             the Name object property.

        :param CATVariant i_index:
        :return: None
        """
        return self.com_object.Remove(i_index)

    def __repr__(self):
        return f'SimMcxProperties(name="{self.name}")'
