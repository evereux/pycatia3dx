from enum import Enum


class DELRscDataEntityType(Enum):
    DELRscDataEntityType_Boolean = 0
    DELRscDataEntityType_Integer = 1
    DELRscDataEntityType_Double = 2
    DELRscDataEntityType_String = 3
    DELRscDataEntityType_UnknownType = 4
    DELRscDataEntityType_Number = 5


class DELRscForType(Enum):
    DELRscForType_Up = 0
    DELRscForType_Down = 1


class DELRscLoopType(Enum):
    DELRscLoopType_WhileDo = 0
    DELRscLoopType_DoWhile = 1


class DELRscMoveParameter(Enum):
    DELRscMoveParameter_Forward = 0
    DELRscMoveParameter_Backward = 1
    DELRscMoveParameter_Begin = 2
    DELRscMoveParameter_End = 3


class DELRscTaskExecutionType(Enum):
    DELRscTaskExecutionType_Internal = 0
    DELRscTaskExecutionType_Service = 1
