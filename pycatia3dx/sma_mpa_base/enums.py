from enum import Enum


class SimAxisAxisType(Enum):
    SimAxisExplicit = 0
    SimAxisGeometric = 1


class SimAxisSystemCoordinateType(Enum):
    SimAxisSystemCylindrical = 0
    SimAxisSystemSpherical = 1
    SimAxisSystemCartesian = 2
    SimAxisSystemNoAxis = 3


class SimAxisSystemDefinitionMode(Enum):
    SimAxisSystemGlobal = 0
    SimAxisSystemLocal = 1
    SimAxisSystemSpecify = 2


class SimDof(Enum):
    SimInvalidDOF = 0
    SimTranslation1 = 1
    SimTranslation3 = 2
    SimRotation1 = 3
    SimRotation3 = 4
    SimRotation2 = 5
    SimTranslation2 = 6


class SimMappedFieldDataDataSourceType(Enum):
    SimMappedFieldDataVPMDocument = 0
    SimMappedFieldDataTable = 1


class SimMappedFieldDataTableColumn(Enum):
    SimMappedFieldDataX = 0
    SimMappedFieldDataValue = 1
    SimMappedFieldDataY = 2
    SimMappedFieldDataZ = 3


class SimMappedFieldDataToleranceType(Enum):
    SimMappedFieldDataRelative = 0
    SimMappedFieldDataAbsolute = 1


class SimPointDefinitionMode(Enum):
    SimPointCoordinates = 0
    SimPointPicked = 1


