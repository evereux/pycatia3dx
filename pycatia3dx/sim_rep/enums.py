from enum import Enum


class SimMCXDuplicateMode(Enum):
    simNoMCX = 0
    simIncludedMCX = 1
    simAllMCX = 2


class SimXRepRelationType(Enum):
    SimXRepTo3DShapeRelation = 0
    SimXRepToXRepRelation = 1
    SimXRepToDocSpecRelation = 2
    SimXRepToDocResultRelation = 3
