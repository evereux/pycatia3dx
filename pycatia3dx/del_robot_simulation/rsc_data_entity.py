"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class RscDataEntity(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     RscDataEntity
                | 
                | Interface representing a Data Entity.
                | 
                | Role: This interface represents a RscDataEntity in a Resource
                | Task
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Type() As DELRscDataEntityType
                |     Get/Set the type of the data entity.
                | 
                |     Returns:
                |         oDataType The data entity type. 
                |     Parameters:
                | 
                |         iDataType
                |             The data entity type. 
                | 
                |     Example:
                | 
                |            
                | 
                |            Dim oResourceTask As ResourceTask2
                |            ......
                |            Dim ResourceSequence As RscSequence
                |            ResourceSequence = oResourceTask.MainRscSequence
                |            ......
                |            Dim iIndex
                |            iIndex=-1
                |            Dim iAssignedEntity As RscDataEntity
                |            Dim iAssignedValue
                |            ......
                |            Dim oCreatedAssignment As RscAssignment
                |            Call ResourceSequence.CreateRscAssignment(iIndex,iAssignedEntity,iAssignedValue,oCreatedAssignment)
                |            Dim AssignedDataEntity As RscDataEntity
                |            AssignedDataEntity = oCreatedAssignment.AssignedDataEntity
                |            Dim oDataType As DELRscDataEntityType
                |            oDataType=AssignedDataEntity.Type
                |            ......
                |            oDataType=DELRscDataEntityType_String
                |            AssignedDataEntity.Type = oDataType
                |            
                |     See also:
                |         DELRscDataEntityType

        :return: DELRscDataEntityType
        """

        return self.com_object.Type

    @type.setter
    def type(self, value: int):
        """
        :param int value:
        """

        self.com_object.Type = value

    def __repr__(self):
        return f'RscDataEntity(name="{ self.name }")'
