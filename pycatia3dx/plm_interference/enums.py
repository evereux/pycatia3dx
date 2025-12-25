from enum import Enum


class CatInterferenceComparison(Enum):
    catInterferenceComparisonNone = 0
    catInterferenceComparisonRecomputeModify = 1
    catInterferenceComparisonDeleteOutOfScope = 2


class CatInterferenceComputeQuantifier(Enum):
    catInterferenceComputeQuantifierMinimumDistance = 0
    catInterferenceComputeQuantifierPenetrationVector = 1


class CatInterferenceGroupComputationType2(Enum):
    catInterferenceGroupComputationTypeAllAgainstAllInGroup = 0
    catInterferenceGroupComputationTypeGroupAgainstGroup = 1
    catInterferenceGroupComputationTypeGroupAgainstContext = 2
    catInterferenceGroupComputationTypeAllAgainstAllInContext = 3


class CatInterferenceGroupComputationType(Enum):
    catInterferenceGroupComputationTypeAllAgainstAllInGroup1 = 0
    catInterferenceGroupComputationTypeGroup1AgainstGroup2 = 1


class CatInterferenceIntermediateRepresentation(Enum):
    catInterferenceInterRepNone = 0
    catInterferenceInterRepAppend = 1
    catInterferenceInterRepComputeBetween = 2


class CatInterferenceResultStatus(Enum):
    catInterferenceResultStatusOK = 0
    catInterferenceResultStatusKO = 1
    catInterferenceResultStatusNotAnalyzed = 2


class CatInterferenceResultType(Enum):
    catInterferenceResultTypeClash = 0
    catInterferenceResultTypeContact = 1
    catInterferenceResultTypeClearance = 2
    catInterferenceResultTypeNoInterference = 3
    catInterferenceResultTypeUndefined = 4


class CatInterferenceResultUserType(Enum):
    catInterferenceResultUserTypeClash = 0
    catInterferenceResultUserTypeContact = 1
    catInterferenceResultUserTypeClearance = 2
    catInterferenceResultUserTypeNoInterference = 3
    catInterferenceResultUserTypeUndefined = 4


class CatInterferenceSpecificationTypeEngCnx(Enum):
    catInterferenceSpecificationTypeEngCnxCheckNone = 0
    catInterferenceSpecificationTypeEngCnxCheckNoClash = 1
    catInterferenceSpecificationTypeEngCnxCheckContact = 2
    catInterferenceSpecificationTypeEngCnxCheckClearance = 3
    catInterferenceSpecificationTypeEngCnxNoCheck = 4


class CatInterferenceSpecificationType(Enum):
    catInterferenceSpecificationTypeNone = 0
    catInterferenceSpecificationTypeClash = 1
    catInterferenceSpecificationTypeClearance = 2
    catInterferenceSpecificationTypeClashWithoutContact = 3
