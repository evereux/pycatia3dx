from enum import Enum


class CatSectionBehavior(Enum):
    catSectionBehaviorAutomatic = 0
    catSectionBehaviorFreeze = 1
    catSectionBehaviorManual = 2


class CATSectioningMode(Enum):
    CatSectionCrossView = 0
    CatSectionCutView = 1


class CATSectioningPlaneVisuMode(Enum):
    CatSectionOnlyContour = 0
    CatSectionContourAndPlane = 1
    CatSectionContourAndGridPlane = 2


class CatSectionType(Enum):
    catSectionTypeBox = 0
    catSectionTypeSlice = 1
    catSectionTypePlane = 2


