from enum import Enum


class APPROACH_RETRACT(Enum):
    Retract = 0
    Approach = 1
    First = 2
    Last = 3
    UndefinedAppRet = 4
    ApproachRetract = 5


class STROKE_SIDE(Enum):
    Right = 0
    End = 1
    Lefft = 2
    Start = 3


class SurfaceOperationPosition(Enum):
    ENDD = 0
    BEFORE = 1
    BEGIN = 2
    AFTER = 3


