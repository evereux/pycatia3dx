from enum import Enum


class KnowledgeObjectType(Enum):
    kweParametersSetObjectType = 0
    kweRelationsSetObjectType = 1
    kweOptimizationsSetObjectType = 2
    kweParameterObjectType = 3
    kweRelationObjectType = 4
    kweOptimizationObjectType = 5
    kweExpertRulebasesSetObjectType = 6
    kweExpertRulebaseObjectType = 7


class KnowledgeSetType(Enum):
    kweParametersType = 0
    kweRelationsType = 1
    kweOptimizationsType = 2
    kweRuleBasesType = 3
