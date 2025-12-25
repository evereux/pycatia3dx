from enum import Enum


class CatDescriptionLengthType(Enum):
    LongText = 0
    ShortText = 1


class CatOutPutFormatType(Enum):
    KWEPrint = 0
    KWEText = 1
    KWEEmail = 2
    KWEHtml = 3


class CatShowResultType(Enum):
    ByRule = 0
    ByState = 1
    ByObject = 2


class CatSolveType(Enum):
    AutomaticCompleteSolveType = 0
    AutomaticOptimizedSolveType = 1
    ManualSolveType = 2


class CatVisualizationType(Enum):
    Failed = 0
    Passed = 1
    Both = 2


class CatWorkingMode(Enum):
    OccurenceObjects = 0
    AllOccurenceObjects = 1
    WholeObjects = 2
    PLMObjects = 3


