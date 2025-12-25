from enum import Enum


class CatBlankingMode(Enum):
    catBlankingOnGeom = 0
    catBlankingInactive = 1
    catBlankingActive = 2


class CatDftWeldFinishSymbol(Enum):
    catDftLetterXWelding = 0
    catFinishWeldingNone = 1
    catDftLetterMWelding = 2
    catDftLetterGWelding = 3
    catDftLetterCWelding = 4
    catDftLetterPWelding = 5
    catDftLetterRWelding = 6
    catDftEqualWelding = 7
    catDftLetterUWelding = 8
    catDftPerpendicularWelding = 9
    catDftLetterFWelding = 10
    catDftLetterHWelding = 11


class CatDftWeldingTail(Enum):
    catDftWeldingTailNO = 0
    catDftWeldingTailYES = 1


class CatDimAnalyse(Enum):
    cat3DDrivedDim = 0
    catDrivingDim = 1
    catDimOnHideGeom = 2
    catFakeDim = 3
    catUnUpdatableDim = 4
    catIsolatedDim = 5
    catBrokenDim = 6
    catTrueDim = 7
    catBasic = 8
    cat3DFeatureDim = 9
    catDimOnGenItems = 10
    cat3DDrivableDim = 11


class CatDimDualDisplay(Enum):
    catDualFractional = 0
    catDualSideBySide = 1
    catDualNone = 2
    catDualBellow = 3


class CatDimFake(Enum):
    catDimFakeText = 0
    catDimFakeNumValue = 1
    catDimFakeNone = 2


class CatDimFrame(Enum):
    catFraRightTriangle = 0
    catFraCircle = 1
    catFraDiamondShaped = 2
    catFraOblong = 3
    catFraRectangle = 4
    catFraSquare = 5
    catFraScoredCircle = 6
    catFraNone = 7
    catFraRightFlag = 8


class CatDimFramedElement(Enum):
    catFraValue = 0
    catFraValueTol = 1
    catFraValueTolText = 2


class CatDimFramedGroup(Enum):
    catFraMain = 0
    catFraBoth = 1
    catFraMainAndDual = 2
    catFraDual = 3


class CatDimLineGraphRep(Enum):
    catDimLine1Part = 0
    catDimLineLeader1Part = 1
    catDimLineLeader2Part = 2
    catDimLine2Parts = 3


class CatDimLineRep(Enum):
    catDimAuto = 0
    catDimUserDefined = 1
    catDimOffset = 2
    catDimUndef = 3
    catDimParallel = 4
    catDimTrueDim = 5
    catDimHoriz = 6
    catDimVert = 7


class CatDimMode(Enum):
    catDimHalfDimSystem = 0
    catDimClassical = 1
    catDimHalfDim = 2
    catDimStacked = 3
    catDimChained = 4
    catDimCumulate = 5
    catDimCumulatesystem = 6


class CatDimOrientation(Enum):
    catParallel = 0
    catHorizontal = 1
    catVertical = 2
    catPerpandicular = 3
    catAngle = 4


class CatDimReference(Enum):
    catView = 0
    catScreen = 1
    catDimLine = 2


class CatDimScore(Enum):
    catDimUnderScored = 0
    catCATDrwDimOverScored = 1
    catDimScored = 2
    catDimScoreNone = 3


class CatDimSymbols(Enum):
    catDimSymbFilledArrow = 0
    catDimSymbTriangle = 1
    catDimSymbScoredCircle = 2
    catDimSymbCircle = 3
    catDimSymbClosedArrow = 4
    catDimSymbXCross = 5
    catDimSymbSlash = 6
    catDimSymbNone = 7
    catDimSymbOpenArrow = 8
    catDimSymbCircledCross = 9
    catDimSymbFilledCircle = 10
    catDimSymbFilledTriangle = 11
    catDimSymbCross = 12
    catDimSymbSymArrow = 13


class CatDimType(Enum):
    catDimDiameterCylinder = 0
    catDimRadiusEdge = 1
    catDimAngle = 2
    catDimDiameterCone = 3
    catDimRadiusCylinder = 4
    catDimDiameterTangent = 5
    catDimRadiusTangent = 6
    catDimLengthCircular = 7
    catDimDiameter = 8
    catDimDistanceOffset = 9
    catDimDiameterTorus = 10
    catDimChamfer = 11
    catDimLengthCurvilinear = 12
    catDimLength = 13
    catDimRadiusTorus = 14
    catDimRadiusFillet = 15
    catDimSlope = 16
    catDimDistance = 17
    catDimRadius = 18
    catDimDistanceMin = 19
    catDimDiameterEdge = 20


class CatJustification(Enum):
    catCenter = 0
    catRight = 1
    catLeft = 2


class CatSymbolType(Enum):
    catBlankedSquare = 0
    catPlus = 1
    catFilledArrow = 2
    catManipulatorTriangle = 3
    catConcentric = 4
    catUnfilledCircle = 5
    catMisc2 = 6
    catCross = 7
    catCrossedCircle = 8
    catFilledCircle = 9
    catDot = 10
    catSmallDot = 11
    catMamipulatorDiamond = 12
    catNotUsed = 13
    catFullCircle2 = 14
    catBlankedArrow = 15
    catFilledTriangle = 16
    catCoincident = 17
    catBlankedCircle = 18
    catFullSquare2 = 19
    catBlankedTriangle = 20
    catStar = 21
    catWave = 22
    catMisc1 = 23
    catFullCircle = 24
    catFilledSquare = 25
    catFullSquare = 26
    catUnfilledArrow = 27
    catManipulatorSquare = 28
    catOpenArrow = 29
    catManipulatorCircle = 30
    catDoubleOpenArrow = 31


class CatTableBorderType(Enum):
    CatTableVerStrikedOut = 0
    CatTableSlashed = 1
    CatTableBackSlashed = 2
    CatTableRight = 3
    CatTableOutLine = 4
    CatTableInside = 5
    CatTableLeft = 6
    CatTableCross = 7
    CatTableTop = 8
    CatTableHorStrikedOut = 9
    CatTableNone = 10
    CatTableBottom = 11


class CatTableComputeMode(Enum):
    CatTableComputeON = 0
    CatTableComputeOFF = 1


class CatTableInvertMode(Enum):
    CatInvertColumn = 0
    CatInvertRow = 1
    CatInvertAll = 2


class CatTablePosition(Enum):
    CatTableMiddleCenter = 0
    CatTableBottomCenter = 1
    CatTableMiddleLeft = 2
    CatTableTopLeft = 3
    CatTableBottomRight = 4
    CatTableMiddleRight = 5
    CatTableTopCenter = 6
    CatTableTopRight = 7
    CatTableBottomLeft = 8


class CatTextAnchorPosition(Enum):
    catCapRight = 0
    catHalfRight = 1
    catBottomCenter = 2
    catMiddleCenter = 3
    catUnsusedValue1 = 4
    catTopLeft = 5
    catBottomRight = 6
    catBaseRight = 7
    catCapCenter = 8
    catUnsusedValue2 = 9
    catBaseLeft = 10
    catTopCenter = 11
    catBaseCenter = 12
    catTopRight = 13
    catHalfLeft = 14
    catMiddleLeft = 15
    catCapLeft = 16
    catBottomLeft = 17
    catMiddleRight = 18
    catHalfCenter = 19


class CatTextFlipMode(Enum):
    catTextAutoFlip = 0
    catTextHorizontalAndVerticalFlip = 1
    catTextHorizontalFlip = 2
    catTextVerticalFlip = 3
    catTextNoFlip = 4


class CatTextFrameType(Enum):
    catEllipse = 0
    catRightFlag = 1
    catBothFlag = 2
    catLeftFlag = 3
    catCustom = 4
    catNone = 5
    catRectangle = 6
    catTriangle = 7
    catScoredCircle = 8
    catSquare = 9
    catDiamond = 10
    catOblong = 11
    catCircle = 12


class CatTextProperty(Enum):
    catSuperscript = 0
    catFontName = 1
    catBold = 2
    catOverline = 3
    catItalic = 4
    catBorder = 5
    catFontSize = 6
    catSubscript = 7
    catCharRatio = 8
    catPlain = 9
    catAlignment = 10
    catCharSpacing = 11
    catStrikethrough = 12
    catKerning = 13
    catParagraph = 14
    catColor = 15
    catUnderline = 16


class CatWeldAdditionalSymbol(Enum):
    catSmoothWelding = 0
    catNoneAddWelding = 1
    catFlushWelding = 2
    catConvexWelding = 3
    catFlatWelding = 4
    catConcaveWelding = 5


class CatWelding(Enum):
    catFirstWeldingBis = 0
    catSecondWeldingTer = 1
    catFirstWeldingTer = 2
    catSecondWelding = 3
    catNoneWelding = 4
    catFirstWelding = 5
    catSecondWeldingBis = 6


class CatWeldingField(Enum):
    catWeldingFieldFive = 0
    catWeldingFieldEleven = 1
    catWeldingFieldEight = 2
    catWeldingFieldOne = 3
    catWeldingFieldFifteen = 4
    catWeldingFieldFourteen = 5
    catWeldingNone = 6
    catWeldingFieldTwelve = 7
    catWeldingFieldTen = 8
    catWeldingFieldThree = 9
    catWeldingFieldThirteen = 10
    catWeldingFieldSeven = 11
    catWeldingFieldNine = 12
    catWeldingFieldSix = 13
    catWeldingFieldFour = 14
    catWeldingFieldTwo = 15


class CatWeldingSide(Enum):
    catWeldingUp = 0
    catWeldingDown = 1


class CatWeldingSymbol(Enum):
    catHVFlareWelding = 0
    catEFlangeWelding = 1
    catUGrooveWelding = 2
    catHVGrooveWelding = 3
    catSeamWelding = 4
    catEFlangeISOWelding = 5
    catSpotWelding = 6
    catTransparencyWelding = 7
    catOverlayWelding = 8
    catEdgeCommonWelding = 9
    catConsumableWelding = 10
    catHYGrooveWelding = 11
    catYGrooveWelding = 12
    catVFlareWelding = 13
    catSpotJISWelding = 14
    catNoneMainWelding = 15
    catEndToEndWelding = 16
    catHUGrooveWelding = 17
    catMWelding = 18
    catVGrooveWelding = 19
    catMeltThruWelding = 20
    catInclinedJointWelding = 21
    catScarfWelding = 22
    catHVOGrooveWelding = 23
    catEdgeWelding = 24
    catCFlangeWelding = 25
    catSurfaceJointWelding = 26
    catMRWelding = 27
    catVOGrooveWelding = 28
    catPlugWelding = 29
    catRechargWelding = 30
    catStudWelding = 31
    catSquareWelding = 32
    catBackWelding = 33
    catFilletWelding = 34


