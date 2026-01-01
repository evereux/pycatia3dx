from enum import IntEnum


class SimAxisAxisType(IntEnum):
    SimAxisGeometric = 0
    SimAxisExplicit = 1


class SimAxisSystemCoordinateType(IntEnum):
    SimAxisSystemNoAxis = 0
    SimAxisSystemCartesian = 1
    SimAxisSystemCylindrical = 2
    SimAxisSystemSpherical = 3


class SimAxisSystemDefinitionMode(IntEnum):
    SimAxisSystemGlobal = 0
    SimAxisSystemLocal = 1
    SimAxisSystemSpecify = 2


class SimDof(IntEnum):
    SimInvalidDOF = 0
    SimTranslation1 = 1
    SimTranslation2 = 2
    SimTranslation3 = 3
    SimRotation1 = 4
    SimRotation2 = 5
    SimRotation3 = 6


class SimMappedFieldDataDataSourceType(IntEnum):
    SimMappedFieldDataTable = 0
    SimMappedFieldDataVPMDocument = 1


class SimMappedFieldDataTableColumn(IntEnum):
    SimMappedFieldDataX = 0
    SimMappedFieldDataY = 1
    SimMappedFieldDataZ = 2
    SimMappedFieldDataValue = 3


class SimMappedFieldDataToleranceType(IntEnum):
    SimMappedFieldDataRelative = 0
    SimMappedFieldDataAbsolute = 1


class SimPointDefinitionMode(IntEnum):
    SimPointCoordinates = 0
    SimPointPicked = 1
