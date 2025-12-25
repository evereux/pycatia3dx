from enum import Enum


class CatDescriptionLengthType(Enum):
    ShortText = 0
    LongText = 1


class CatOutPutFormatType(Enum):
    KWEHtml = 0
    KWEText = 1
    KWEPrint = 2
    KWEEmail = 3


class CatShowResultType(Enum):
    ByRule = 0
    ByObject = 1
    ByState = 2


class CatSolveType(Enum):
    ManualSolveType = 0
    AutomaticOptimizedSolveType = 1
    AutomaticCompleteSolveType = 2


class CatVisualizationType(Enum):
    Passed = 0
    Failed = 1
    Both = 2


class CatWorkingMode(Enum):
    WholeObjects = 0
    OccurenceObjects = 1
    PLMObjects = 2
    AllOccurenceObjects = 3
