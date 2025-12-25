from enum import Enum


class APPROACH_RETRACT(Enum):
    UndefinedAppRet = 0
    First = 1
    Last = 2
    Retract = 3
    Approach = 4
    ApproachRetract = 5


class STROKE_SIDE(Enum):
    Start = 0
    End = 1
    Lefft = 2
    Right = 3


class SurfaceOperationPosition(Enum):
    BEFORE = 0
    AFTER = 1
    BEGIN = 2
    ENDD = 3
