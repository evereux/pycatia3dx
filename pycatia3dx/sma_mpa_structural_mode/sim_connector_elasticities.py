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


class SimConnectorElasticities(Collection):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     SimConnectorElasticities
                | 
                | Represents the Connector Elasticities collection.
                | 
                | Example:
                |     Given a SimConnectorBehavior object you can retrieve a
                |     SimConnectorElasticities collection as following:
                | 
                |      Dim MyConnectorBehavior As SimConnectorBehavior
                |      ...
                |      Dim MyConnectorDampings As SimConnectorElasticities
                |      Set MyConnectorDampings = MyConnectorBehavior.ConnectorElasticities
                |      
                | 
                | Example in Python:
                |     Given a SimConnectorBehavior object you can retrieve a
                |     SimConnectorElasticities collection as following:
                | 
                |      ...
                |      myConnectorDampings = myConnectorBehavior.ConnectorElasticities
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
                |     Creates a connector elasticity object and returns it.
                | 
                |     Parameters:
                | 
                |         iDegreeOfFreedom[in]
                |             The degree of freedom for which the connector elasticity will be
                |             created. 
                |         ospConnectorElasticity[out]
                |             The created connector elasticity. 
                | 
                |     Returns:
                |         The SimConnectorElasticity object

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
                |     Returns a Connector Elasticity from the collection of Connector
                |     Elasticities.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index of the Connector Elasticity. 
                | 
                |     Returns:
                |         The SimConnectorElasticity object

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
                |     Removes the specified connector elasticity.
                | 
                |     Parameters:
                | 
                |         iDegreeOfFreedom[in]
                |             The degree of freedom for which the connector elasticity will be
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
                |     Removes all connector elasticities. 

        :return: None
        """
        return self.com_object.RemoveAll()

    def __repr__(self):
        return f'SimConnectorElasticities(name="{ self.name }")'
