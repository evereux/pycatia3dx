"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.agt.agt_connector import AGTConnector
from pycatia3dx.system.collection import Collection
from pycatia3dx.types.general import CATVariant


class AGTConnectors(Collection):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     AGTConnectors
                | 
                | Object for Connectors.
                | To retrieve a Connector from collection.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def item(self, i_index: CATVariant) -> AGTConnector:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Func Item(CATVariant iIndex) As AGTConnector
                |     Retrieves a Connector from the collection of Connector.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index of Connector 
                | 
                |     Example:
                | 
                | 
                |              This example retrieves Connector from the list of
                |              Connectors
                |              
                | 
                |              Dim myPart as CATIAPart
                |              Set myPart = CATIA.ActiveEditor.ActievObject
                |              Dim MyAGTRoot As AGTRoot
                |              Set MyAGTRoot = myPart.GetItem("CATAGTRoot")
                |              'Get a second Connector from the list of Connector by
                |              index
                |              Dim ConnectorByIndex As AGTConnectors
                |              Set ConnectorByIndex = MyAGTRoot.Connectors.Item(2)
                |              'Get a Connector named "MyConnector.2" from the list of Connector
                |              by name
                |              Dim ConnectorByName As AGTConnectors
                |              Set ConnectorByName = MyAGTRoot.Connectors.Item("MyConnector.2")

        :param CATVariant i_index:
        :return: AGTConnector
        """
        return AGTConnector(self.com_object.Item(i_index))

    def __repr__(self):
        return f'AgtConnectors(name="{self.name}")'
