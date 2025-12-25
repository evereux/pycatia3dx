from enum import Enum


class SimAxisAxisType(Enum):
    SimAxisGeometric = 0
    SimAxisExplicit = 1


class SimAxisSystemCoordinateType(Enum):
    SimAxisSystemNoAxis = 0
    SimAxisSystemCartesian = 1
    SimAxisSystemCylindrical = 2
    SimAxisSystemSpherical = 3


class SimAxisSystemDefinitionMode(Enum):
    SimAxisSystemGlobal = 0
    SimAxisSystemLocal = 1
    SimAxisSystemSpecify = 2


class SimDof(Enum):
    SimInvalidDOF = 0
    SimTranslation1 = 1
    SimTranslation2 = 2
    SimTranslation3 = 3
    SimRotation1 = 4
    SimRotation2 = 5
    SimRotation3 = 6


class SimMappedFieldDataDataSourceType(Enum):
    SimMappedFieldDataTable = 0
    SimMappedFieldDataVPMDocument = 1


class SimMappedFieldDataTableColumn(Enum):
    SimMappedFieldDataX = 0
    SimMappedFieldDataY = 1
    SimMappedFieldDataZ = 2
    SimMappedFieldDataValue = 3


class SimMappedFieldDataToleranceType(Enum):
    SimMappedFieldDataRelative = 0
    SimMappedFieldDataAbsolute = 1


class SimPointDefinitionMode(Enum):
    SimPointCoordinates = 0
    SimPointPicked = 1
