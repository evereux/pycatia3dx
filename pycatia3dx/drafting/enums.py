from enum import Enum


class Cat3DColorInheritanceMode(Enum):
    cat3DColorInheritanceModeOff = 0
    cat3DColorInheritanceModeOn = 1


class CatAreaFillType(Enum):
    catAreaFillOnMathematicPoints = 0
    catAreaFillOnCurves = 1


class CatDftGenRepresentationPolicy(Enum):
    catDftCustomParam = 0
    catDftAllDesignRepsPolicy = 1
    catDftAllSessionRepsPolicy = 2
    catDftFirstDesignRepsPolicy = 3


class CatDrawingViewType(Enum):
    catViewRear = 0
    catViewPure_Sketch = 1
    catViewDetail = 2
    catViewLeft = 3
    catViewSectionCut = 4
    catViewMain = 5
    catViewBackground = 6
    catViewUnfolded = 7
    catViewAuxiliary = 8
    catViewAxonometric = 9
    catViewUntyped = 10
    catViewFront = 11
    catViewSection = 12
    catViewBottom = 13
    catViewIsom = 14
    catViewRight = 15
    catViewTop = 16


class CatFilletRepresentation(Enum):
    catFilletRepSymbolic = 0
    catFilletRepNone = 1
    catFilletRepProjectedOriginalEdge = 2
    catFilletRepOriginalEdge = 3
    catFilletRepBoundary = 4


class CatGenRepresentationMode(Enum):
    catModeApproximate = 0
    catModeRaster = 1
    catModeCGR = 2
    catModeExact = 3


class CatGenViewRasterMode(Enum):
    catImageShadingEdgesNoLight = 0
    catImageShadingEdges = 1
    catImageShadingNoLight = 2
    catImageHRD = 3
    catImageShading = 4


class CatHiddenLineMode(Enum):
    catHlrModeOn = 0
    catHlrModeOff = 1


class CatImageViewMode(Enum):
    catImageModeShadingNoLightSource = 0
    catImageModeOff = 1
    catImageModeHRD = 2
    catImageModeShadingWithEdges = 3
    catImageModeShadingWithEdgesAndNoLightSource = 4
    catImageModeShading = 5


class CatPictureFormat(Enum):
    catPicturePNG = 0
    catPictureJPEG = 1
    catPictureNONE = 2
    catPictureCCITTG3 = 3


class CatPictureType(Enum):
    catPictureVector = 0
    catPictureRaster = 1


class CatPointsProjectionMode(Enum):
    catPointsProjectionModeOn = 0
    catPointsProjectionModeOff = 1


class CatProjViewType(Enum):
    catRightView = 0
    catTopView = 1
    catBottomView = 2
    catRearView = 3
    catLeftView = 4


class CatRepresentationMode(Enum):
    catExactMode = 0
    catPolyhedricMode = 1
    catVisualMode = 2


class CatSheetGenViewsPosMode(Enum):
    catFixedCG = 0
    catFixedAxis = 1


class CatSheetProjectionMethod(Enum):
    catThirdAngle = 0
    catFirstAngle = 1


class CatThreadLinkedTo(Enum):
    cat2DPoint = 0
    cat3DThread = 1
    catNoLink = 2
    cat3DGeom = 3
    cat2DCircle = 4
    catNotDefined = 5
    cat3DHole = 6


class CatThreadType(Enum):
    catTaped = 0
    catThreaded = 1


class CatWireframeMode(Enum):
    catGenWFAlwaysVisible = 0
    catGenWFCanBeHidden = 1
    catGenWFOff = 2


class RasterLevelOfDetail(Enum):
    HighQuality = 0
    LowQuality = 1
    NormalQuality = 2
    Customize = 3


