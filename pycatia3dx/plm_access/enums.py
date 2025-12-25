from enum import Enum


class SearchCondition(Enum):
    SearchCondition_AND = 0
    SearchCondition_OR = 1


class SearchMode(Enum):
    SearchMode_Extended = 0
    SearchMode_Predefined = 1
    SearchMode_Easy = 2
    SearchMode_Expert = 3


class SearchOperator(Enum):
    SearchOperator_GT_EQ = 0
    SearchOperator_BETWEEN = 1
    SearchOperator_NULL = 2
    SearchOperator_NOT_EQ = 3
    SearchOperator_NOT_LIKE = 4
    SearchOperator_LT = 5
    SearchOperator_NOT_NULL = 6
    SearchOperator_GT = 7
    SearchOperator_EQ = 8
    SearchOperator_LT_EQ = 9
    SearchOperator_NOT_BETWEEN = 10
    SearchOperator_LIKE = 11


class SearchSortOrder(Enum):
    SearchSortOrder_Descending = 0
    SearchSortOrder_Ascending = 1


