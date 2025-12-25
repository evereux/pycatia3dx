from enum import Enum


class CatCDHoleMode(Enum):
    catCDModeCountersunkDiameter = 0
    catCDModeNoCountersunkDiameter = 1


class CatChamferMode(Enum):
    catLengthAngleChamfer = 0
    catTwoLengthChamfer = 1


class CatChamferOrientation(Enum):
    catReverseChamfer = 0
    catNoReverseChamfer = 1


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
    catReflectKeepFaceDraftMode = 0
    catReflectKeepEdgeDraftMode = 1
    catStandardDraftMode = 2


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
    catMinimumFilletBoundaryRelimitation = 0
    catAutomaticFilletBoundaryRelimitation = 1
    catMaximumFilletBoundaryRelimitation = 2
    catUVFilletBoundaryRelimitation = 3
    catConnectFilletBoundaryRelimitation = 4


class CatFilletEdgePropagation(Enum):
    catTangencyFilletEdgePropagation = 0
    catMinimalFilletEdgePropagation = 1


class CatFilletTrimSupport(Enum):
    catNoTrimFilletSupport = 0
    catTrimFilletSupport = 1


class CatFilletVariation(Enum):
    catCubicFilletVariation = 0
    catLinearFilletVariation = 1


class CatHoleAnchorMode(Enum):
    catExtremPointHoleAnchor = 0
    catMiddlePointHoleAnchor = 1


class CatHoleBottomType(Enum):
    catTrimmedHoleBottom = 0
    catFlatHoleBottom = 1
    catVHoleBottom = 2


class CatHoleThreadingMode(Enum):
    catSmoothHoleThreading = 0
    catThreadedHoleThreading = 1


class CatHoleThreadSide(Enum):
    catLeftThreadSide = 0
    catRightThreadSide = 1


class CatHoleThreadStandard(Enum):
    catHoleMetricThinPitch = 0
    catHoleMetricThickPitch = 1


class CatHoleType(Enum):
    catCounterboredHole = 0
    catCounterdrilledHole = 1
    catCountersunkHole = 2
    catTaperedHole = 3
    catSimpleHole = 4


class CatLimitMode(Enum):
    catUpToLastLimit = 0
    catUpToNextLimit = 1
    catUpThruNextLimit = 2
    catOffsetLimit = 3
    catUntilLimit = 4
    catUpToPlaneLimit = 5
    catUpToSurfaceLimit = 6


class CatMergeMode(Enum):
    catMergeOn = 0
    catMergeOff = 1


class CatPartitionLimitType(Enum):
    CatPartitionLimit_Infinite = 0
    CatPartitionLimit_UpToNext = 1
    CatPartitionLimit_None = 2


class CatPrismExtrusionDirection(Enum):
    catNormalToSketchDirection = 0
    catNotNormalToSketchDirection = 1


class CatPrismOrientation(Enum):
    catRegularOrientation = 0
    catInverseOrientation = 1


class CatRectangularPatternParameters(Enum):
    catUnequalSpacing = 0
    catInstancesandSpacing = 1


class CatSewingIntersectionMode(Enum):
    catSewingNoIntersect = 0
    catSewingIntersect = 1


class CatSplitSide(Enum):
    catNegativeSide = 0
    catPositiveSide = 1


class CatThreadPolarity(Enum):
    catTap = 0
    catThread = 1


class CatThreadSide(Enum):
    catLeftSide = 0
    catRightSide = 1


class CatThreadStandard(Enum):
    catMetricThickPitch = 0
    catMetricThinPitch = 1


