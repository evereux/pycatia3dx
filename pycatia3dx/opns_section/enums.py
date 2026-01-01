from enum import IntEnum


class CatSectionBehavior(IntEnum):
    catSectionBehaviorAutomatic = 0
    catSectionBehaviorFreeze = 1
    catSectionBehaviorManual = 2


class CATSectioningMode(IntEnum):
    CatSectionCrossView = 0
    CatSectionCutView = 1


class CATSectioningPlaneVisuMode(IntEnum):
    CatSectionContourAndPlane = 0
    CatSectionOnlyContour = 1
    CatSectionContourAndGridPlane = 2


class CatSectionType(IntEnum):
    catSectionTypePlane = 0
    catSectionTypeSlice = 1
    catSectionTypeBox = 2
