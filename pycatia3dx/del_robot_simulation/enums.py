from enum import Enum


class DELRscDataEntityType(Enum):
    DELRscDataEntityType_Double = 0
    DELRscDataEntityType_UnknownType = 1
    DELRscDataEntityType_Number = 2
    DELRscDataEntityType_String = 3
    DELRscDataEntityType_Boolean = 4
    DELRscDataEntityType_Integer = 5


class DELRscForType(Enum):
    DELRscForType_Up = 0
    DELRscForType_Down = 1


class DELRscLoopType(Enum):
    DELRscLoopType_DoWhile = 0
    DELRscLoopType_WhileDo = 1


class DELRscMoveParameter(Enum):
    DELRscMoveParameter_End = 0
    DELRscMoveParameter_Backward = 1
    DELRscMoveParameter_Forward = 2
    DELRscMoveParameter_Begin = 3


class DELRscTaskExecutionType(Enum):
    DELRscTaskExecutionType_Service = 0
    DELRscTaskExecutionType_Internal = 1


