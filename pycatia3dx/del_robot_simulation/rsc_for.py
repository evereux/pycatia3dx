"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.del_robot_simulation.rsc_data_entity import RscDataEntity
from pycatia3dx.del_robot_simulation.rsc_instruction import RscInstruction


class RscFor(RscInstruction):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     DELRobotSimulationIDLItf.RscInstruction
                |                         RscFor
                | 
                | Interface representing a Resource For Loop Instruction.
                | 
                | Role: This interface represents a RscFor Instruction in a Resource
                | Task
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def for_index(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ForIndex() As CATBSTR
                |     Get/Set index identifier name (Default identifier is i). This identifier
                |     can be used in expressions.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             For index 
                | 
                |     Returns:
                |         oIndex For index 
                |     Example:
                | 
                |            
                | 
                |            Dim oResourceTask As ResourceTask2
                |            ......
                |            Dim ResourceSequence As RscSequence
                |            Set ResourceSequence = oResourceTask.MainRscSequence
                |            ......
                |            Dim iIndex
                |            iIndex=-1
                |            Dim iForIndex As String
                |            Dim iForFrom As String
                |            Dim iForTo As String
                |            DELRscForType iForLoopType
                |            ......
                |            Set  iForLoopType = DELRscForType_Up
                |            Dim oForInstr As RscFor
                |            Set oForInstr = ResourceSequence.CreateRscFor(iIndex, iForLoopType, iForIndex, iForFrom, iForTo)
                |            Dim Index 
                |            Index = oForInstr.ForIndex
                |            ......
                |            oForInstr.ForIndex = Index

        :return: str
        """

        return self.com_object.ForIndex

    @for_index.setter
    def for_index(self, value: str):
        """
        :param str value:
        """

        self.com_object.ForIndex = value

    @property
    def from_(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property From() As CATBSTR
                |     Get/Set the FROM expression (Default is 1).
                | 
                |     Returns:
                |         oFrom the from expression. 
                |     Parameters:
                | 
                |         iFrom
                |             the from expression. 
                | 
                |     Example:
                | 
                |            
                | 
                |            Dim oResourceTask As ResourceTask2
                |            ......
                |            Dim ResourceSequence As RscSequence
                |            ResourceSequence = oResourceTask.RscSequence
                |            ......
                |            Dim iIndex
                |            iIndex=-1
                |            Dim iForIndex As String
                |            Dim iForFrom As String
                |            Dim iForTo As String
                |            DELRscForType iForLoopType
                |            ......
                |            Set  iForLoopType = DELRscForType_Up
                |            Dim oForInstr As RscFor
                |            Set oForInstr = ResourceSequence.CreateRscFor(iIndex, iForLoopType, iForIndex, iForFrom, iForTo)
                |            Dim From
                |            From = oForInstr.From
                |            ......
                |            oForInstr.From = From

        :return: str
        """

        return self.com_object.From

    @from_.setter
    def from_(self, value: str):
        """
        :param str value:
        """

        self.com_object.From = value

    @property
    def to(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property To() As CATBSTR
                |     Get/Set the TO expression (Default is 10).
                | 
                |     Returns:
                |         oTo the to expression. 
                |     Parameters:
                | 
                |         iTo
                |             the to expression. 
                | 
                |     Example:
                | 
                |            
                | 
                |            Dim oResourceTask As ResourceTask2
                |            ......
                |            Dim ResourceSequence As RscSequence
                |            Set ResourceSequence = oResourceTask.MainRscSequence
                |            ......
                |            Dim iIndex
                |            iIndex=-1
                |            Dim iForIndex As String
                |            Dim iForFrom As String
                |            Dim iForTo As String
                |            DELRscForType iForLoopType
                |            ......
                |            Set  iForLoopType = DELRscForType_Up
                |            Dim oForInstr As RscFor
                |            Set oForInstr = ResourceSequence.CreateRscFor(iIndex, iForLoopType, iForIndex, iForFrom, iForTo)
                |            Dim To
                |            To = oForInstr.To
                |            ......
                |            oForInstr.To = To

        :return: str
        """

        return self.com_object.To

    @to.setter
    def to(self, value: str):
        """
        :param str value:
        """

        self.com_object.To = value

    @property
    def type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Type() As DELRscForType
                |     Get/Set for-loop type (Default is DELRscForType_Up).
                | 
                |     Parameters:
                | 
                |         iForType
                |             for-loop type 
                | 
                |     Returns:
                |         oForType for-loop type 
                |     Example:
                | 
                |            
                | 
                |            Dim oResourceTask As ResourceTask2
                |            ......
                |            Dim ResourceSequence As RscSequence
                |            Set ResourceSequence = oResourceTask.MainRscSequence
                |            ......
                |            Dim iIndex
                |            iIndex=-1
                |            Dim iForIndex As String
                |            Dim iForFrom As String
                |            Dim iForTo As String
                |            DELRscForType iForLoopType
                |            ......
                |            Set  iForLoopType = DELRscForType_Up
                |            Dim oForInstr As RscFor
                |            Set oForInstr = ResourceSequence.CreateRscFor(iIndex, iForLoopType, iForIndex, iForFrom, iForTo)
                |            Dim oForType As DELRscForType
                |            oForType = oForInstr.Type
                |            ......
                |            oForInstr.Type = oForType
                |            
                | 
                | 
                |          
                |          
                | 
                |     See also:
                |         DELRscForType

        :return: DELRscForType
        """

        return self.com_object.Type

    @type.setter
    def type(self, value: int):
        """
        :param int value:
        """

        self.com_object.Type = value

    def get_index(self) -> RscDataEntity:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetIndex() As RscDataEntity
                |     Get index as RscDataEntity
                | 
                |     Returns:
                |         oIndex For Index 
                |     Example:
                | 
                |            
                | 
                |            Dim oResourceTask As ResourceTask2
                |            ......
                |            Dim ResourceSequence As RscSequence
                |            Set ResourceSequence = oResourceTask.MainRscSequence
                |            ......
                |            Dim iIndex
                |            iIndex=-1
                |            Dim iForIndex As String
                |            Dim iForFrom As String
                |            Dim iForTo As String
                |            DELRscForType iForLoopType
                |            ......
                |            Set  iForLoopType = DELRscForType_Up
                |            Dim oForInstr As RscFor
                |            Set oForInstr = ResourceSequence.CreateRscFor(iIndex, iForLoopType, iForIndex, iForFrom, iForTo)
                |            Dim Index as RscDataEntity
                |            Set hIndex = oForInstr.GetIndex()

        :return: RscDataEntity
        """
        return RscDataEntity(self.com_object.GetIndex())

    def __repr__(self):
        return f'RscFor(name="{ self.name }")'
