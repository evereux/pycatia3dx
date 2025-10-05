"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.todo_del_robot_simulation.rsc_data_entity import RscDataEntity


class RscLocalVar(RscDataEntity):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     DELRobotSimulationIDLItf.RscDataEntity
                |                         RscLocalVar
                | 
                | Interface representing a Local Variable.
                | 
                | Role: This interface represents a RscLocalVar in a Resource
                | Task
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def default_value(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property DefaultValue() As CATBSTR
                |     Get/Set default value.
                | 
                |     Returns:
                |         oDefaultValue The default value. 
                |     Parameters:
                | 
                |         iDefaultValue
                |             The new default value. 
                | 
                |     Example:
                | 
                |            
                | 
                |            Dim oResourceTask As ResourceTask2
                |            ......
                |            Dim iName As String
                |            iName = "MyLocalVar"
                |            Dim oLocalVar As RscLocalVar
                |            Dim iType As DELRscDataEntityType
                |            iType = DELRscDataEntityType_Integer
                |            Set oLocalVar = oResourceTask.CreateRscLocalVar(iName, iType)
                |            Dim DefaultValue
                |            DefaultValue = oLocalVar.DefaultValue
                |            ......
                |            oLocalVar.DefaultValue = DefaultValue

        :return: str
        """

        return self.com_object.DefaultValue

    @default_value.setter
    def default_value(self, value: str):
        """
        :param str value:
        """

        self.com_object.DefaultValue = value

    def unset_default_value(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub UnsetDefaultValue()
                |     Unset default value.
                | 
                |     Example:
                | 
                |            
                | 
                |            Dim oResourceTask As ResourceTask2
                |            ......
                |            Dim iName As String
                |            iName = "MyLocalVar"
                |            Dim oLocalVar As RscLocalVar
                |            Dim iType As DELRscDataEntityType
                |            iType = DELRscDataEntityType_Integer
                |            Set oLocalVar = oResourceTask.CreateRscLocalVar(iName, iType)
                |            Call oLocalVar.UnsetDefaultValue()

        :return: None
        """
        return self.com_object.UnsetDefaultValue()

    def __repr__(self):
        return f'RscLocalVar(name="{ self.name }")'
