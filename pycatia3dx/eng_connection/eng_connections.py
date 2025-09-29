"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.eng_connection.eng_connection import EngConnection
from pycatia3dx.system.collection import Collection


class EngConnections(Collection):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     EngConnections
                | 
                | Collection to manage all the Engineering Connections of a Product
                | Reference.
                | 
                | Role: Allow to read/write/remove Engineering Connections.
                | 
                | Here is the way to get it:
                | Dim myEngConnections As EngConnections.
                | set myEngConnections = myPLMProductReference.GetItem("CATEngConnections").
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def add(self, i_type: int, i_impacteds: tuple) -> EngConnection:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Add(CatEngConnectionType iType,CATSafeArrayVariant iImpacteds) As
                | EngConnection
                |     Adds an Engineering Connection.
                | 
                |     Parameters:
                | 
                |         iEngCntType
                |             [in] The type of the Engineering Connection. 
                |         iListOfImpacteds
                |             [in] The list of impacted pointed by the connection. The impacted
                |             is identified by a String :
                | 
                |             Here is the different formats accepted:
                |             "ProductInstance1.1" for standard impacted.
                |             "ProductInstance1.1/ProductInstance2.1" for flexible
                |             impacted.
                |             "RepInstance1.1" for "on rep" impacted.
                | 
                |             [out] The created Engineering Connection. 
                | 
                |     Returns:
                | 
                |         The created Engineering Connection.
                |             If the operation is successful. 
                |         nothing
                |             If the operation is failed. 
                | 
                |         A VB Error is raised if the creation failed.
                | 
                |     Func AddWithContext(CatEngConnectionType iType,CATSafeArrayVariant
                |     iImpacteds,AnyObject iReferenceContext,CATBSTR iNameBSTR) As
                |     EngConnection
                |     Func Item(CATVariant iIndex) As EngConnection
                |         Return an Engineering Connection.
                | 
                |         Parameters:
                | 
                |             I
                |                 [in] The index or name of the Engineering Connection.
                |                 
                |             the index in the collection
                |                 if it is an Integer. 
                |             the name of the connection
                |                 if it is a String. 
                | 
                |     Sub Remove(CATVariant iEngCnt)
                |         Remove an Engineering Connection.
                | 
                |         Parameters:
                | 
                |             iEngCnt
                |             the index in the collection
                |                 if it is an Integer. 
                |             the name of the connection
                |                 if it is a String. 
                |             the connection to remove
                |                 if it is a EngConnection.

        :param int i_type:
        :param tuple i_impacteds:
        :return: EngConnection
        """
        return EngConnection(self.com_object.Add(i_type, i_impacteds))

    def __repr__(self):
        return f'EngConnections(name="{self.name}")'
