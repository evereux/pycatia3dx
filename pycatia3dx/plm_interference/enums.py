from enum import IntEnum


class CatInterferenceComparison(IntEnum):
    catInterferenceComparisonNone = 0
    catInterferenceComparisonRecomputeModify = 1
    catInterferenceComparisonDeleteOutOfScope = 2


class CatInterferenceComputeQuantifier(IntEnum):
    catInterferenceComputeQuantifierMinimumDistance = 0
    catInterferenceComputeQuantifierPenetrationVector = 1


class CatInterferenceGroupComputationType2(IntEnum):
    catInterferenceGroupComputationTypeAllAgainstAllInGroup = 0
    catInterferenceGroupComputationTypeGroupAgainstGroup = 1
    catInterferenceGroupComputationTypeGroupAgainstContext = 2
    catInterferenceGroupComputationTypeAllAgainstAllInContext = 3


class CatInterferenceGroupComputationType(IntEnum):
    catInterferenceGroupComputationTypeAllAgainstAllInGroup1 = 0
    catInterferenceGroupComputationTypeGroup1AgainstGroup2 = 1


class CatInterferenceIntermediateRepresentation(IntEnum):
    catInterferenceInterRepNone = 0
    catInterferenceInterRepAppend = 1
    catInterferenceInterRepComputeBetween = 2


class CatInterferenceResultStatus(IntEnum):
    catInterferenceResultStatusOK = 0
    catInterferenceResultStatusKO = 1
    catInterferenceResultStatusNotAnalyzed = 2


class CatInterferenceResultType(IntEnum):
    catInterferenceResultTypeClash = 0
    catInterferenceResultTypeContact = 1
    catInterferenceResultTypeClearance = 2
    catInterferenceResultTypeNoInterference = 3
    catInterferenceResultTypeUndefined = 4


class CatInterferenceResultUserType(IntEnum):
    catInterferenceResultUserTypeClash = 0
    catInterferenceResultUserTypeContact = 1
    catInterferenceResultUserTypeClearance = 2
    catInterferenceResultUserTypeNoInterference = 3
    catInterferenceResultUserTypeUndefined = 4


class CatInterferenceSpecificationTypeEngCnx(IntEnum):
    catInterferenceSpecificationTypeEngCnxCheckNone = 0
    catInterferenceSpecificationTypeEngCnxCheckNoClash = 1
    catInterferenceSpecificationTypeEngCnxCheckContact = 2
    catInterferenceSpecificationTypeEngCnxCheckClearance = 3
    catInterferenceSpecificationTypeEngCnxNoCheck = 4


class CatInterferenceSpecificationType(IntEnum):
    catInterferenceSpecificationTypeNone = 0
    catInterferenceSpecificationTypeClash = 1
    catInterferenceSpecificationTypeClearance = 2
    catInterferenceSpecificationTypeClashWithoutContact = 3
