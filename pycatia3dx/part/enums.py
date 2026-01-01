from enum import IntEnum


class CatCDHoleMode(IntEnum):
    catCDModeNoCountersunkDiameter = 0
    catCDModeCountersunkDiameter = 1


class CatChamferMode(IntEnum):
    catTwoLengthChamfer = 0
    catLengthAngleChamfer = 1


class CatChamferOrientation(IntEnum):
    catNoReverseChamfer = 0
    catReverseChamfer = 1


class CatChamferPropagation(IntEnum):
    catTangencyChamfer = 0
    catMinimalChamfer = 1


class CatCircularPatternParameters(IntEnum):
    catInstancesandAngularSpacing = 0
    catCompleteCrown = 1
    catUnequalAngularSpacing = 2


class CatCSHoleMode(IntEnum):
    catCSModeDepthAngle = 0
    catCSModeDepthDiameter = 1
    catCSModeAngleDiameter = 2


class CatDraftMode(IntEnum):
    catStandardDraftMode = 0
    catReflectKeepFaceDraftMode = 1
    catReflectKeepEdgeDraftMode = 2


class CatDraftMultiselectionMode(IntEnum):
    catNoneDraftMultiselectionMode = 0
    catDraftMultiselectionByNeutralMode = 1


class CatDraftNeutralPropagationMode(IntEnum):
    catNoneDraftNeutralPropagationMode = 0
    catSmoothDraftNeutralPropagationMode = 1


class CatFilletBitangencyType(IntEnum):
    catSphereBitangencyType = 0
    catCircleBitangencyType = 1


class CatFilletBoundaryRelimitation(IntEnum):
    catAutomaticFilletBoundaryRelimitation = 0
    catUVFilletBoundaryRelimitation = 1
    catConnectFilletBoundaryRelimitation = 2
    catMinimumFilletBoundaryRelimitation = 3
    catMaximumFilletBoundaryRelimitation = 4


class CatFilletEdgePropagation(IntEnum):
    catMinimalFilletEdgePropagation = 0
    catTangencyFilletEdgePropagation = 1


class CatFilletTrimSupport(IntEnum):
    catTrimFilletSupport = 0
    catNoTrimFilletSupport = 1


class CatFilletVariation(IntEnum):
    catLinearFilletVariation = 0
    catCubicFilletVariation = 1


class CatHoleAnchorMode(IntEnum):
    catExtremPointHoleAnchor = 0
    catMiddlePointHoleAnchor = 1


class CatHoleBottomType(IntEnum):
    catFlatHoleBottom = 0
    catVHoleBottom = 1
    catTrimmedHoleBottom = 2


class CatHoleThreadingMode(IntEnum):
    catThreadedHoleThreading = 0
    catSmoothHoleThreading = 1


class CatHoleThreadSide(IntEnum):
    catRightThreadSide = 0
    catLeftThreadSide = 1


class CatHoleThreadStandard(IntEnum):
    catHoleMetricThinPitch = 0
    catHoleMetricThickPitch = 1


class CatHoleType(IntEnum):
    catSimpleHole = 0
    catTaperedHole = 1
    catCounterboredHole = 2
    catCountersunkHole = 3
    catCounterdrilledHole = 4


class CatLimitMode(IntEnum):
    catOffsetLimit = 0
    catUpToNextLimit = 1
    catUpToLastLimit = 2
    catUpToPlaneLimit = 3
    catUpToSurfaceLimit = 4
    catUpThruNextLimit = 5
    catUntilLimit = 6


class CatMergeMode(IntEnum):
    catMergeOff = 0
    catMergeOn = 1


class CatPartitionLimitType(IntEnum):
    CatPartitionLimit_None = 0
    CatPartitionLimit_Infinite = 1
    CatPartitionLimit_UpToNext = 2


class CatPrismExtrusionDirection(IntEnum):
    catNormalToSketchDirection = 0
    catNotNormalToSketchDirection = 1


class CatPrismOrientation(IntEnum):
    catRegularOrientation = 0
    catInverseOrientation = 1


class CatRectangularPatternParameters(IntEnum):
    catInstancesandSpacing = 0
    catUnequalSpacing = 1


class CatSewingIntersectionMode(IntEnum):
    catSewingNoIntersect = 0
    catSewingIntersect = 1


class CatSplitSide(IntEnum):
    catPositiveSide = 0
    catNegativeSide = 1


class CatThreadPolarity(IntEnum):
    catThread = 0
    catTap = 1


class CatThreadSide(IntEnum):
    catRightSide = 0
    catLeftSide = 1


class CatThreadStandard(IntEnum):
    catMetricThinPitch = 0
    catMetricThickPitch = 1
