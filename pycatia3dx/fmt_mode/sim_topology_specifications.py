"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.fmt_mode.sim_topology_specification import SimTopologySpecification
from pycatia3dx.system.collection import Collection
from pycatia3dx.types.general import CATVariant


class SimTopologySpecifications(Collection):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     SimTopologySpecifications
                | 
                | Represents the collection of Local Topology Specifications.
                | 
                | See also:
                |     SimTopologySpecification
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def add(self, i_type: str) -> SimTopologySpecification:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Add(CATBSTR iType) As SimTopologySpecification
                |     Creates a new Local Topology Specification and adds it to the Local
                |     Topology Specification collection.
                |     Postcondition: The Local Topology Specification will be created linked to
                |     the Mesh Part object.
                | 
                |     Parameters:
                | 
                |         iType:
                |             The type of Local Topology Specification to create.
                |             
                | 
                |     Returns:
                |         The created Local Topology Specification.

        :param str i_type:
        :return: SimTopologySpecification
        """
        return SimTopologySpecification(self.com_object.Add(i_type))

    def item(self, i_index: CATVariant) -> SimTopologySpecification:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Item(CATVariant iIndex) As SimTopologySpecification
                |     Returns a Local Topology Specification using its index or its name from the
                |     collection.
                | 
                |     Parameters:
                | 
                |         iIndex:
                |             The index or the name of the Local Topology Specification to
                |             retrieve from the collection.
                |             As a numeric, this index is the rank of the Local Topology
                |             Specification in the collection. The index of the first Local Topology
                |             Specification in the collection is 1, and the index of the last Local Topology
                |             Specification is Count.
                |             As a string, it is the name you assigned to the Local Topology
                |             Specification using the Name object property. 
                | 
                |     Returns:
                |         The retrieved Local Topology Specification.

        :param CATVariant i_index:
        :return: SimTopologySpecification
        """
        return SimTopologySpecification(self.com_object.Item(i_index))

    def remove(self, i_index: CATVariant) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub Remove(CATVariant iIndex)
                |     Removes a Local Topology Specification using its index or its name from the
                |     collection.
                | 
                |     Parameters:
                | 
                |         iIndex:
                |             The index or the name of the Local Topology Specification to
                |             retrieve from the collection.
                |             As a numeric, this index is the rank of the Local Topology
                |             Specification in the collection. The index of the first Local Topology
                |             Specification in the collection is 1, and the index of the last Local Topology
                |             Specification is Count.
                |             As a string, it is the name you assigned to the Local Topology
                |             Specification using the Name object property.

        :param CATVariant i_index:
        :return: None
        """
        return self.com_object.Remove(i_index)

    def __repr__(self):
        return f'SimTopologySpecifications(name="{self.name}")'
