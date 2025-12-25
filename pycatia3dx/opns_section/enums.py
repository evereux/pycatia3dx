from enum import Enum


class CatSectionBehavior(Enum):
    catSectionBehaviorAutomatic = 0
    catSectionBehaviorFreeze = 1
    catSectionBehaviorManual = 2


class CATSectioningMode(Enum):
    CatSectionCrossView = 0
    CatSectionCutView = 1


class CATSectioningPlaneVisuMode(Enum):
    CatSectionContourAndPlane = 0
    CatSectionOnlyContour = 1
    CatSectionContourAndGridPlane = 2


class CatSectionType(Enum):
    catSectionTypePlane = 0
    catSectionTypeSlice = 1
    catSectionTypeBox = 2
