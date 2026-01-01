from enum import IntEnum


class SimMeshEntityType(IntEnum):
    simMeshUnknownEntity = 0
    simMeshNodeEntity = 1
    simMeshEdgeEntity = 2
    simMeshFaceEntity = 3
    simMeshElementEntity = 4


class SimMeshingRuleAttr(IntEnum):
    simMeshingRuleName = 0
    simMeshingRuleRevision = 1
    simMeshingRuleExtension = 2
