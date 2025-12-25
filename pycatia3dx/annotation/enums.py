from enum import Enum


class CatBlankingMode(Enum):
    catBlankingInactive = 0
    catBlankingActive = 1
    catBlankingOnGeom = 2


class CatDftWeldFinishSymbol(Enum):
    catFinishWeldingNone = 0
    catDftLetterCWelding = 1
    catDftLetterFWelding = 2
    catDftLetterGWelding = 3
    catDftLetterHWelding = 4
    catDftLetterMWelding = 5
    catDftLetterRWelding = 6
    catDftLetterUWelding = 7
    catDftLetterPWelding = 8
    catDftLetterXWelding = 9
    catDftEqualWelding = 10
    catDftPerpendicularWelding = 11


class CatDftWeldingTail(Enum):
    catDftWeldingTailNO = 0
    catDftWeldingTailYES = 1


class CatDimAnalyse(Enum):
    catDimOnGenItems = 0
    catUnUpdatableDim = 1
    catFakeDim = 2
    catDrivingDim = 3
    catBrokenDim = 4
    catTrueDim = 5
    catBasic = 6
    cat3DDrivableDim = 7
    cat3DDrivedDim = 8
    catIsolatedDim = 9
    catDimOnHideGeom = 10
    cat3DFeatureDim = 11


class CatDimDualDisplay(Enum):
    catDualNone = 0
    catDualBellow = 1
    catDualFractional = 2
    catDualSideBySide = 3


class CatDimFake(Enum):
    catDimFakeNone = 0
    catDimFakeNumValue = 1
    catDimFakeText = 2


class CatDimFrame(Enum):
    catFraNone = 0
    catFraCircle = 1
    catFraScoredCircle = 2
    catFraDiamondShaped = 3
    catFraSquare = 4
    catFraRectangle = 5
    catFraOblong = 6
    catFraRightFlag = 7
    catFraRightTriangle = 8


class CatDimFramedElement(Enum):
    catFraValue = 0
    catFraValueTol = 1
    catFraValueTolText = 2


class CatDimFramedGroup(Enum):
    catFraMain = 0
    catFraDual = 1
    catFraMainAndDual = 2
    catFraBoth = 3


class CatDimLineGraphRep(Enum):
    catDimLine1Part = 0
    catDimLine2Parts = 1
    catDimLineLeader1Part = 2
    catDimLineLeader2Part = 3


class CatDimLineRep(Enum):
    catDimUndef = 0
    catDimHoriz = 1
    catDimVert = 2
    catDimAuto = 3
    catDimUserDefined = 4
    catDimTrueDim = 5
    catDimParallel = 6
    catDimOffset = 7


class CatDimMode(Enum):
    catDimClassical = 0
    catDimCumulate = 1
    catDimHalfDim = 2
    catDimChained = 3
    catDimStacked = 4
    catDimCumulatesystem = 5
    catDimHalfDimSystem = 6


class CatDimOrientation(Enum):
    catHorizontal = 0
    catVertical = 1
    catParallel = 2
    catPerpandicular = 3
    catAngle = 4


class CatDimReference(Enum):
    catScreen = 0
    catView = 1
    catDimLine = 2


class CatDimScore(Enum):
    catDimScoreNone = 0
    catDimUnderScored = 1
    catDimScored = 2
    catCATDrwDimOverScored = 3


class CatDimSymbols(Enum):
    catDimSymbNone = 0
    catDimSymbOpenArrow = 1
    catDimSymbClosedArrow = 2
    catDimSymbFilledArrow = 3
    catDimSymbSymArrow = 4
    catDimSymbSlash = 5
    catDimSymbCircle = 6
    catDimSymbFilledCircle = 7
    catDimSymbScoredCircle = 8
    catDimSymbCircledCross = 9
    catDimSymbTriangle = 10
    catDimSymbFilledTriangle = 11
    catDimSymbCross = 12
    catDimSymbXCross = 13


class CatDimType(Enum):
    catDimDistance = 0
    catDimDistanceOffset = 1
    catDimLength = 2
    catDimLengthCurvilinear = 3
    catDimAngle = 4
    catDimRadius = 5
    catDimRadiusTangent = 6
    catDimRadiusCylinder = 7
    catDimRadiusEdge = 8
    catDimDiameter = 9
    catDimDiameterTangent = 10
    catDimDiameterCylinder = 11
    catDimDiameterEdge = 12
    catDimDiameterCone = 13
    catDimChamfer = 14
    catDimSlope = 15
    catDimLengthCircular = 16
    catDimRadiusFillet = 17
    catDimDiameterTorus = 18
    catDimRadiusTorus = 19
    catDimDistanceMin = 20


class CatJustification(Enum):
    catLeft = 0
    catCenter = 1
    catRight = 2


class CatSymbolType(Enum):
    catNotUsed = 0
    catCross = 1
    catPlus = 2
    catConcentric = 3
    catCoincident = 4
    catFullCircle = 5
    catFullSquare = 6
    catStar = 7
    catDot = 8
    catSmallDot = 9
    catMisc1 = 10
    catMisc2 = 11
    catFullCircle2 = 12
    catFullSquare2 = 13
    catOpenArrow = 14
    catUnfilledArrow = 15
    catBlankedArrow = 16
    catFilledArrow = 17
    catUnfilledCircle = 18
    catBlankedCircle = 19
    catFilledCircle = 20
    catCrossedCircle = 21
    catBlankedSquare = 22
    catFilledSquare = 23
    catBlankedTriangle = 24
    catFilledTriangle = 25
    catManipulatorSquare = 26
    catMamipulatorDiamond = 27
    catManipulatorCircle = 28
    catManipulatorTriangle = 29
    catDoubleOpenArrow = 30
    catWave = 31


class CatTableBorderType(Enum):
    CatTableNone = 0
    CatTableLeft = 1
    CatTableTop = 2
    CatTableRight = 3
    CatTableBottom = 4
    CatTableBackSlashed = 5
    CatTableSlashed = 6
    CatTableHorStrikedOut = 7
    CatTableVerStrikedOut = 8
    CatTableOutLine = 9
    CatTableInside = 10
    CatTableCross = 11


class CatTableComputeMode(Enum):
    CatTableComputeOFF = 0
    CatTableComputeON = 1


class CatTableInvertMode(Enum):
    CatInvertColumn = 0
    CatInvertRow = 1
    CatInvertAll = 2


class CatTablePosition(Enum):
    CatTableTopLeft = 0
    CatTableMiddleLeft = 1
    CatTableBottomLeft = 2
    CatTableTopCenter = 3
    CatTableMiddleCenter = 4
    CatTableBottomCenter = 5
    CatTableTopRight = 6
    CatTableMiddleRight = 7
    CatTableBottomRight = 8


class CatTextAnchorPosition(Enum):
    catUnsusedValue1 = 0
    catTopLeft = 1
    catMiddleLeft = 2
    catBottomLeft = 3
    catTopCenter = 4
    catMiddleCenter = 5
    catBottomCenter = 6
    catTopRight = 7
    catMiddleRight = 8
    catBottomRight = 9
    catUnsusedValue2 = 10
    catCapLeft = 11
    catHalfLeft = 12
    catBaseLeft = 13
    catCapCenter = 14
    catHalfCenter = 15
    catBaseCenter = 16
    catCapRight = 17
    catHalfRight = 18
    catBaseRight = 19


class CatTextFlipMode(Enum):
    catTextNoFlip = 0
    catTextHorizontalFlip = 1
    catTextVerticalFlip = 2
    catTextHorizontalAndVerticalFlip = 3
    catTextAutoFlip = 4


class CatTextFrameType(Enum):
    catNone = 0
    catRectangle = 1
    catSquare = 2
    catCircle = 3
    catScoredCircle = 4
    catDiamond = 5
    catTriangle = 6
    catRightFlag = 7
    catLeftFlag = 8
    catBothFlag = 9
    catOblong = 10
    catEllipse = 11
    catCustom = 12


class CatTextProperty(Enum):
    catBold = 0
    catItalic = 1
    catUnderline = 2
    catOverline = 3
    catStrikethrough = 4
    catSubscript = 5
    catSuperscript = 6
    catFontSize = 7
    catParagraph = 8
    catPlain = 9
    catColor = 10
    catFontName = 11
    catBorder = 12
    catAlignment = 13
    catCharRatio = 14
    catCharSpacing = 15
    catKerning = 16


class CatWeldAdditionalSymbol(Enum):
    catNoneAddWelding = 0
    catFlatWelding = 1
    catConvexWelding = 2
    catConcaveWelding = 3
    catFlushWelding = 4
    catSmoothWelding = 5


class CatWelding(Enum):
    catNoneWelding = 0
    catFirstWelding = 1
    catSecondWelding = 2
    catFirstWeldingBis = 3
    catSecondWeldingBis = 4
    catFirstWeldingTer = 5
    catSecondWeldingTer = 6


class CatWeldingField(Enum):
    catWeldingNone = 0
    catWeldingFieldOne = 1
    catWeldingFieldTwo = 2
    catWeldingFieldThree = 3
    catWeldingFieldFour = 4
    catWeldingFieldFive = 5
    catWeldingFieldSix = 6
    catWeldingFieldSeven = 7
    catWeldingFieldEight = 8
    catWeldingFieldNine = 9
    catWeldingFieldTen = 10
    catWeldingFieldEleven = 11
    catWeldingFieldTwelve = 12
    catWeldingFieldThirteen = 13
    catWeldingFieldFourteen = 14
    catWeldingFieldFifteen = 15


class CatWeldingSide(Enum):
    catWeldingUp = 0
    catWeldingDown = 1


class CatWeldingSymbol(Enum):
    catNoneMainWelding = 0
    catSquareWelding = 1
    catVGrooveWelding = 2
    catHVGrooveWelding = 3
    catYGrooveWelding = 4
    catHYGrooveWelding = 5
    catUGrooveWelding = 6
    catHUGrooveWelding = 7
    catFilletWelding = 8
    catCFlangeWelding = 9
    catEFlangeWelding = 10
    catVFlareWelding = 11
    catHVFlareWelding = 12
    catSpotWelding = 13
    catBackWelding = 14
    catHVOGrooveWelding = 15
    catVOGrooveWelding = 16
    catPlugWelding = 17
    catMRWelding = 18
    catMWelding = 19
    catRechargWelding = 20
    catSpotJISWelding = 21
    catEFlangeISOWelding = 22
    catSeamWelding = 23
    catScarfWelding = 24
    catStudWelding = 25
    catEdgeWelding = 26
    catMeltThruWelding = 27
    catSurfaceJointWelding = 28
    catInclinedJointWelding = 29
    catEndToEndWelding = 30
    catConsumableWelding = 31
    catTransparencyWelding = 32
    catOverlayWelding = 33
    catEdgeCommonWelding = 34
