"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.fmt_mode.sim_mesh_specification import SimMeshSpecification
from pycatia3dx.system.collection import Collection
from pycatia3dx.types.general import CATVariant


class SimMeshSpecifications(Collection):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     SimMeshSpecifications
                | 
                | Represents the collection of Local Mesh Specifications.
                | 
                | See also:
                |     SimMeshSpecification
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def add(self, i_type: str) -> SimMeshSpecification:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Add(CATBSTR iType) As SimMeshSpecification
                |     Creates a new Local Mesh Specification and adds it to the
                |     collection.
                |     Postcondition: The Local Mesh Specification will be created linked to the
                |     Mesh Part object.
                | 
                |     Parameters:
                | 
                |         iType
                |             The type of Local Mesh Specification to create. 
                | 
                |     Returns:
                |         The created Local Mesh Specification

        :param str i_type:
        :return: SimMeshSpecification
        """
        return SimMeshSpecification(self.com_object.Add(i_type))

    def item(self, i_index: CATVariant) -> SimMeshSpecification:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Item(CATVariant iIndex) As SimMeshSpecification
                |     Returns a Local Mesh Specification using its index or its name from the
                |     collection.
                | 
                |     Parameters:
                | 
                |         iIndex:
                |             The index or the name of the Local Mesh Specification to retrieve
                |             from the collection.
                |             As a numeric, this index is the rank of the Local Mesh
                |             Specification in the collection. The index of the first Local Mesh
                |             Specification in the collection is 1, and the index of the last Local Mesh
                |             Specification is Count.
                |             As a string, it is the name you assigned to the Local Mesh
                |             Specification using the Name object property. 
                | 
                |     Returns:
                |         The retrieved Local Mesh Specification.

        :param CATVariant i_index:
        :return: SimMeshSpecification
        """
        return SimMeshSpecification(self.com_object.Item(i_index))

    def remove(self, i_index: CATVariant) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub Remove(CATVariant iIndex)
                |     Removes a Local Mesh Specification using its index or its name from the
                |     collection.
                | 
                |     Parameters:
                | 
                |         iIndex:
                |             The index or the name of the Local Mesh Specification to retrieve
                |             from the collection.
                |             As a numeric, this index is the rank of the Local Mesh
                |             Specification in the collection. The index of the first Local Mesh
                |             Specification in the collection is 1, and the index of the last Local Mesh
                |             Specification is Count.
                |             As a string, it is the name you assigned to the Local Mesh
                |             Specification using the Name object property.

        :param CATVariant i_index:
        :return: None
        """
        return self.com_object.Remove(i_index)

    def __repr__(self):
        return f'SimMeshSpecifications(name="{self.name}")'
