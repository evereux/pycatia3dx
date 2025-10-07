"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.del_robot_simulation.rsc_data_entity import RscDataEntity


class RscConst(RscDataEntity):

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
                |                         RscConst
                | 
                | Interface representing a Constant.
                | 
                | Role: This interface represents a RscConst entity in a Resource
                | Task
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def value(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Value() As CATBSTR
                |     Get/Set the Value of the RscConst.
                | 
                |     Returns:
                |         oValue The const value. 
                |     Parameters:
                | 
                |         iVal
                |             The const value. 
                | 
                |     Example:
                | 
                |            
                | 
                |            Dim oResourceTask As ResourceTask2
                |            ......
                |            Dim iName As String
                |            iName = "MyConst"
                |            Dim iVal As String 
                |            iVal = "MyVal"
                |            Dim oConst As RscConst
                |            Dim iType As DELRscDataEntityType
                |            iType = DELRscDataEntityType_Integer
                |            Set oConst = oResourceTask.CreateRscConst(iName, iType, iVal)
                |            Dim Val 
                |            Val=oConst.Value
                |            ......
                |            oConst.Value=Val

        :return: str
        """

        return self.com_object.Value

    @value.setter
    def value(self, value: str):
        """
        :param str value:
        """

        self.com_object.Value = value

    def __repr__(self):
        return f'RscConst(name="{ self.name }")'
