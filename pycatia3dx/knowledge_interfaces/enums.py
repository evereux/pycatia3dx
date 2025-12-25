from enum import Enum


class KnowledgeObjectType(Enum):
    kweParameterObjectType = 0
    kweOptimizationObjectType = 1
    kweRelationsSetObjectType = 2
    kweRelationObjectType = 3
    kweParametersSetObjectType = 4
    kweOptimizationsSetObjectType = 5
    kweExpertRulebasesSetObjectType = 6
    kweExpertRulebaseObjectType = 7


class KnowledgeSetType(Enum):
    kweRelationsType = 0
    kweRuleBasesType = 1
    kweOptimizationsType = 2
    kweParametersType = 3


