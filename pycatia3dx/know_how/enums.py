from enum import IntEnum


class CatDescriptionLengthType(IntEnum):
    ShortText = 0
    LongText = 1


class CatOutPutFormatType(IntEnum):
    KWEHtml = 0
    KWEText = 1
    KWEPrint = 2
    KWEEmail = 3


class CatShowResultType(IntEnum):
    ByRule = 0
    ByObject = 1
    ByState = 2


class CatSolveType(IntEnum):
    ManualSolveType = 0
    AutomaticOptimizedSolveType = 1
    AutomaticCompleteSolveType = 2


class CatVisualizationType(IntEnum):
    Passed = 0
    Failed = 1
    Both = 2


class CatWorkingMode(IntEnum):
    WholeObjects = 0
    OccurenceObjects = 1
    PLMObjects = 2
    AllOccurenceObjects = 3
