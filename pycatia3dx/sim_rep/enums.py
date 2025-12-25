from enum import Enum


class SimMCXDuplicateMode(Enum):
    simAllMCX = 0
    simNoMCX = 1
    simIncludedMCX = 2


class SimXRepRelationType(Enum):
    SimXRepToDocSpecRelation = 0
    SimXRepTo3DShapeRelation = 1
    SimXRepToXRepRelation = 2
    SimXRepToDocResultRelation = 3


