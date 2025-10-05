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


class SimConnectorDampings(Collection):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     SimConnectorDampings
                | 
                | Represents the Connector Dampings collection.
                | 
                | Example:
                |     Given a SimConnectorBehavior object you can retrieve a SimConnectorDampings
                |     collection as following:
                | 
                |      Dim MyConnectorBehavior As SimConnectorBehavior
                |      ...
                |      Dim MyConnectorDampings As SimConnectorDampings
                |      Set MyConnectorDampings = MyConnectorBehavior.ConnectorDampings
                |      
                | 
                | Example in Python:
                |     Given a SimConnectorBehavior object you can retrieve a SimConnectorDampings
                |     collection as following:
                | 
                |      ...
                |      myConnectorDampings = myConnectorBehavior.ConnectorDampings
                |      
                | 
                | See also:
                |     SimConnectorBehavior
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def add(self, i_degree_of_freedom: int) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Add(SimDof iDegreeOfFreedom) As CATBaseDispatch
                |     Creates a Connector Damping object and returns it.
                | 
                |     Parameters:
                | 
                |         iDegreeOfFreedom[in]
                |             The degree of freedom for which the Connector Damping will be
                |             created. 
                |         ospConnectorDamping[out]
                |             The created Connector Damping. 
                | 
                |     Returns:
                |         The SimConnectorDamping object

        :param int i_degree_of_freedom:
        :return: AnyObject
        """
        return self.com_object.Add(i_degree_of_freedom)

    def item(self, i_index: CATVariant) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Item(CATVariant iIndex) As CATBaseDispatch
                |     Returns a Connector Damping from the collection of Connector
                |     Dampings.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index of the Connector Damping. 
                | 
                |     Returns:
                |         The SimConnectorDamping object

        :param CATVariant i_index:
        :return: AnyObject
        """
        return self.com_object.Item(i_index)

    def remove(self, i_degree_of_freedom: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub Remove(SimDof iDegreeOfFreedom)
                |     Removes the specified Connector Damping.
                | 
                |     Parameters:
                | 
                |         iDegreeOfFreedom[in]
                |             The degree of freedom for which the Connector Damping will be
                |             removed.

        :param int i_degree_of_freedom:
        :return: None
        """
        return self.com_object.Remove(i_degree_of_freedom)

    def remove_all(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub RemoveAll()
                |     Removes all Connector Dampings. 

        :return: None
        """
        return self.com_object.RemoveAll()

    def __repr__(self):
        return f'SimConnectorDampings(name="{ self.name }")'
