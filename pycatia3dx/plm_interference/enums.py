from enum import Enum


class CatInterferenceComparison(Enum):
    catInterferenceComparisonDeleteOutOfScope = 0
    catInterferenceComparisonRecomputeModify = 1
    catInterferenceComparisonNone = 2


class CatInterferenceComputeQuantifier(Enum):
    catInterferenceComputeQuantifierMinimumDistance = 0
    catInterferenceComputeQuantifierPenetrationVector = 1


class CatInterferenceGroupComputationType2(Enum):
    catInterferenceGroupComputationTypeAllAgainstAllInGroup = 0
    catInterferenceGroupComputationTypeAllAgainstAllInContext = 1
    catInterferenceGroupComputationTypeGroupAgainstGroup = 2
    catInterferenceGroupComputationTypeGroupAgainstContext = 3


class CatInterferenceGroupComputationType(Enum):
    catInterferenceGroupComputationTypeGroup1AgainstGroup2 = 0
    catInterferenceGroupComputationTypeAllAgainstAllInGroup1 = 1


class CatInterferenceIntermediateRepresentation(Enum):
    catInterferenceInterRepComputeBetween = 0
    catInterferenceInterRepNone = 1
    catInterferenceInterRepAppend = 2


class CatInterferenceResultStatus(Enum):
    catInterferenceResultStatusNotAnalyzed = 0
    catInterferenceResultStatusKO = 1
    catInterferenceResultStatusOK = 2


class CatInterferenceResultType(Enum):
    catInterferenceResultTypeNoInterference = 0
    catInterferenceResultTypeUndefined = 1
    catInterferenceResultTypeClash = 2
    catInterferenceResultTypeClearance = 3
    catInterferenceResultTypeContact = 4


class CatInterferenceResultUserType(Enum):
    catInterferenceResultUserTypeClash = 0
    catInterferenceResultUserTypeNoInterference = 1
    catInterferenceResultUserTypeUndefined = 2
    catInterferenceResultUserTypeContact = 3
    catInterferenceResultUserTypeClearance = 4


class CatInterferenceSpecificationTypeEngCnx(Enum):
    catInterferenceSpecificationTypeEngCnxCheckNoClash = 0
    catInterferenceSpecificationTypeEngCnxNoCheck = 1
    catInterferenceSpecificationTypeEngCnxCheckClearance = 2
    catInterferenceSpecificationTypeEngCnxCheckNone = 3
    catInterferenceSpecificationTypeEngCnxCheckContact = 4


class CatInterferenceSpecificationType(Enum):
    catInterferenceSpecificationTypeClearance = 0
    catInterferenceSpecificationTypeClash = 1
    catInterferenceSpecificationTypeClashWithoutContact = 2
    catInterferenceSpecificationTypeNone = 3


