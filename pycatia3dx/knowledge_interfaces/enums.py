from enum import IntEnum


class KnowledgeObjectType(IntEnum):
    kweParametersSetObjectType = 0
    kweRelationsSetObjectType = 1
    kweOptimizationsSetObjectType = 2
    kweParameterObjectType = 3
    kweRelationObjectType = 4
    kweOptimizationObjectType = 5
    kweExpertRulebasesSetObjectType = 6
    kweExpertRulebaseObjectType = 7


class KnowledgeSetType(IntEnum):
    kweParametersType = 0
    kweRelationsType = 1
    kweOptimizationsType = 2
    kweRuleBasesType = 3
