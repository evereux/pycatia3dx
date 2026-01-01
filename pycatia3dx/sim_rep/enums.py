from enum import IntEnum


class SimMCXDuplicateMode(IntEnum):
    simNoMCX = 0
    simIncludedMCX = 1
    simAllMCX = 2


class SimXRepRelationType(IntEnum):
    SimXRepTo3DShapeRelation = 0
    SimXRepToXRepRelation = 1
    SimXRepToDocSpecRelation = 2
    SimXRepToDocResultRelation = 3
