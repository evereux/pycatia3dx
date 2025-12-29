from enum import Enum


class CatCDHoleMode(Enum):
    catCDModeNoCountersunkDiameter = 0
    catCDModeCountersunkDiameter = 1


class CatChamferMode(Enum):
    catTwoLengthChamfer = 0
    catLengthAngleChamfer = 1


class CatChamferOrientation(Enum):
    catNoReverseChamfer = 0
    catReverseChamfer = 1


class CatChamferPropagation(Enum):
    catTangencyChamfer = 0
    catMinimalChamfer = 1


class CatCircularPatternParameters(Enum):
    catInstancesandAngularSpacing = 0
    catCompleteCrown = 1
    catUnequalAngularSpacing = 2


class CatCSHoleMode(Enum):
    catCSModeDepthAngle = 0
    catCSModeDepthDiameter = 1
    catCSModeAngleDiameter = 2


class CatDraftMode(Enum):
    catStandardDraftMode = 0
    catReflectKeepFaceDraftMode = 1
    catReflectKeepEdgeDraftMode = 2


class CatDraftMultiselectionMode(Enum):
    catNoneDraftMultiselectionMode = 0
    catDraftMultiselectionByNeutralMode = 1


class CatDraftNeutralPropagationMode(Enum):
    catNoneDraftNeutralPropagationMode = 0
    catSmoothDraftNeutralPropagationMode = 1


class CatFilletBitangencyType(Enum):
    catSphereBitangencyType = 0
    catCircleBitangencyType = 1


class CatFilletBoundaryRelimitation(Enum):
    catAutomaticFilletBoundaryRelimitation = 0
    catUVFilletBoundaryRelimitation = 1
    catConnectFilletBoundaryRelimitation = 2
    catMinimumFilletBoundaryRelimitation = 3
    catMaximumFilletBoundaryRelimitation = 4


class CatFilletEdgePropagation(Enum):
    catMinimalFilletEdgePropagation = 0
    catTangencyFilletEdgePropagation = 1


class CatFilletTrimSupport(Enum):
    catTrimFilletSupport = 0
    catNoTrimFilletSupport = 1


class CatFilletVariation(Enum):
    catLinearFilletVariation = 0
    catCubicFilletVariation = 1


class CatHoleAnchorMode(Enum):
    catExtremPointHoleAnchor = 0
    catMiddlePointHoleAnchor = 1


class CatHoleBottomType(Enum):
    catFlatHoleBottom = 0
    catVHoleBottom = 1
    catTrimmedHoleBottom = 2


class CatHoleThreadingMode(Enum):
    catThreadedHoleThreading = 0
    catSmoothHoleThreading = 1


class CatHoleThreadSide(Enum):
    catRightThreadSide = 0
    catLeftThreadSide = 1


class CatHoleThreadStandard(Enum):
    catHoleMetricThinPitch = 0
    catHoleMetricThickPitch = 1


class CatHoleType(Enum):
    catSimpleHole = 0
    catTaperedHole = 1
    catCounterboredHole = 2
    catCountersunkHole = 3
    catCounterdrilledHole = 4


class CatLimitMode(Enum):
    catOffsetLimit = 0
    catUpToNextLimit = 1
    catUpToLastLimit = 2
    catUpToPlaneLimit = 3
    catUpToSurfaceLimit = 4
    catUpThruNextLimit = 5
    catUntilLimit = 6


class CatMergeMode(Enum):
    catMergeOff = 0
    catMergeOn = 1


class CatPartitionLimitType(Enum):
    CatPartitionLimit_None = 0
    CatPartitionLimit_Infinite = 1
    CatPartitionLimit_UpToNext = 2


class CatPrismExtrusionDirection(Enum):
    catNormalToSketchDirection = 0
    catNotNormalToSketchDirection = 1


class CatPrismOrientation(Enum):
    catRegularOrientation = 0
    catInverseOrientation = 1


class CatRectangularPatternParameters(Enum):
    catInstancesandSpacing = 0
    catUnequalSpacing = 1


class CatSewingIntersectionMode(Enum):
    catSewingNoIntersect = 0
    catSewingIntersect = 1


class CatSplitSide(Enum):
    catPositiveSide = 0
    catNegativeSide = 1


class CatThreadPolarity(Enum):
    catThread = 0
    catTap = 1


class CatThreadSide(Enum):
    catRightSide = 0
    catLeftSide = 1


class CatThreadStandard(Enum):
    catMetricThinPitch = 0
    catMetricThickPitch = 1
