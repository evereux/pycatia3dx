from enum import IntEnum


class CatCompareOccurrenceResult(IntEnum):
    catDifferentObjects = 0
    catIdenticalOccurrence = 1
    catIdenticalReference = 2
