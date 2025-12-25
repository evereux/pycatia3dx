from enum import Enum


class SimMeshEntityType(Enum):
    simMeshEdgeEntity = 0
    simMeshElementEntity = 1
    simMeshFaceEntity = 2
    simMeshUnknownEntity = 3
    simMeshNodeEntity = 4


class SimMeshingRuleAttr(Enum):
    simMeshingRuleRevision = 0
    simMeshingRuleName = 1
    simMeshingRuleExtension = 2


