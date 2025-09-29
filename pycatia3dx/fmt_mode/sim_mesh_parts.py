"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.fmt_mode.sim_mesh_part import SimMeshPart
from pycatia3dx.system.collection import Collection
from pycatia3dx.types.general import CATVariant


class SimMeshParts(Collection):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     SimMeshParts
                | 
                | Represents the collection of simulation Mesh Parts.
                | 
                | See also:
                |     SimMeshPart
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def add(self, i_type: str) -> SimMeshPart:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Add(CATBSTR iType) As SimMeshPart
                |     Creates a new Mesh Part and adds it to the collection.
                | 
                |     Parameters:
                | 
                |         iType:
                |             The type of Mesh Part to create. 
                | 
                |     Returns:
                |         The created Mesh Part.

        :param str i_type:
        :return: SimMeshPart
        """
        return SimMeshPart(self.com_object.Add(i_type))

    def item(self, i_index: CATVariant) -> SimMeshPart:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Item(CATVariant iIndex) As SimMeshPart
                |     Returns a Mesh Part using its index or its name from the
                |     collection.
                | 
                |     Parameters:
                | 
                |         iIndex:
                |             The index or the name of the Mesh Part to retrieve from the
                |             collection.
                |             As a numeric, this index is the rank of the Mesh Part in the
                |             collection. The index of the first Mesh Part in the collection is 1, and the
                |             index of the last Mesh Part is Count.
                |             As a string, it is the name you assigned to the Mesh Part using the
                |             Name object property. 
                | 
                |     Returns:
                |         The retrieved Mesh Part.

        :param CATVariant i_index:
        :return: SimMeshPart
        """
        return SimMeshPart(self.com_object.Item(i_index))

    def remove(self, i_index: CATVariant) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub Remove(CATVariant iIndex)
                |     Removes a Mesh Part using its index or its name from the
                |     collection.
                | 
                |     Parameters:
                | 
                |         iIndex:
                |             The index or the name of the Mesh Part to retrieve from the
                |             collection.
                |             As a numeric, this index is the rank of the Mesh Part in the
                |             collection. The index of the first Mesh Part in the collection is 1, and the
                |             index of the last Mesh Part is Count.
                |             As a string, it is the name you assigned to the Mesh Part using the
                |             Name object property.

        :param CATVariant i_index:
        :return: None
        """
        return self.com_object.Remove(i_index)

    def __repr__(self):
        return f'SimMeshParts(name="{self.name}")'
