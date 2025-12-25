from enum import Enum


class SimMeshEntityType(Enum):
    simMeshUnknownEntity = 0
    simMeshNodeEntity = 1
    simMeshEdgeEntity = 2
    simMeshFaceEntity = 3
    simMeshElementEntity = 4


class SimMeshingRuleAttr(Enum):
    simMeshingRuleName = 0
    simMeshingRuleRevision = 1
    simMeshingRuleExtension = 2
