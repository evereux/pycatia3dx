from enum import Enum


class CatArrangeStyle(Enum):
    catArrangeCascade = 0
    catArrangeTiledHorizontal = 1
    catArrangeTiledVertical = 2
    catArrangeTiledHorizontalInAllTab = 3
    catArrangeTiledVerticalInAllTab = 4
    catArrangeTiledGridInAllTab = 5
    catArrangeTiledHorizontalInCurrentTab = 6
    catArrangeTiledVerticalInCurrentTab = 7
    catArrangeTiledGridInCurrentTab = 8
    catArrangeTiledHorizontalInNewTab = 9
    catArrangeTiledVerticalInNewTab = 10
    catArrangeTiledGridInNewTab = 11


class CatBannerPosition(Enum):
    catBannerPositionNone = 0
    catBannerPositionBottom = 1
    catBannerPositionTop = 2
    catBannerPositionLeft = 3
    catBannerPositionRight = 4


class CatCameraType(Enum):
    catCamera2D = 0
    catCamera3D = 1


class CatCaptureFormat(Enum):
    catCaptureFormatCGM = 0
    catCaptureFormatEMF = 1
    catCaptureFormatTIFF = 2
    catCaptureFormatTIFFGreyScale = 3
    catCaptureFormatBMP = 4
    catCaptureFormatJPEG = 5


class CatClippingMode(Enum):
    catClippingModeClear = 0
    catClippingModeNear = 1
    catClippingModeFar = 2
    catClippingModeNearAndFar = 3


class CatImageRotation(Enum):
    catImageNoRotation = 0
    catImageRotation90 = 1
    catImageRotation180 = 2
    catImageRotation270 = 3
    catImageBestRotation = 4


class CATInteractionType(Enum):
    CATSelection = 0
    CATIndication = 1
    CATMouseMove = 2
    CATInputUndo = 3
    CATInputRedo = 4
    CATEscape = 5
    CATOtherEditor = 6
    CATExclusiveCommand = 7


class CatLightingMode(Enum):
    catInfiniteLightSource = 0
    catNeonLightSource = 1


class CATMultiSelectionMode(Enum):
    CATMonoSel = 0
    CATMultiSelTriggWhenSelPerf = 1
    CATMultiSelTriggWhenUserValidatesSelection = 2


class CatNavigationStyle(Enum):
    catNavigationExamine = 0
    catNavigationWalk = 1
    catNavigationFly = 2


class CatPaperOrientation(Enum):
    catPaperPortrait = 0
    catPaperLandscape = 1
    catPaperBestFit = 2


class CatPaperSize(Enum):
    catPaperLetter = 0
    catPaperLegal = 1
    catPaperA0 = 2
    catPaperA1 = 3
    catPaperA2 = 4
    catPaperA3 = 5
    catPaperA4 = 6
    catPaperA = 7
    catPaperB = 8
    catPaperC = 9
    catPaperD = 10
    catPaperE = 11
    catPaperF = 12
    catPaperUser = 13


class CATPPRTreeItemType(Enum):
    CATProcessList = 0
    CATProductList = 1
    CATResourcesList = 2


class CatPrintColor(Enum):
    catColorTrueColor = 0
    catColorGreyScale = 1
    catColorMonochrome = 2


class CatPrinterDirState(Enum):
    CatPrinterDirFree = 0
    CatPrinterDirProtect = 1


class CatPrintLineCap(Enum):
    catPrintFlat = 0
    catPrintSquare = 1
    catPrintRound = 2


class CatPrintLineSpecification(Enum):
    catPrintAbsolute = 0
    catPrintScaled = 1
    catPrintNoThickness = 2


class CatPrintQuality(Enum):
    catPrintQualityDraft = 0
    catPrintQualityLow = 1
    catPrintQualityMedium = 2
    catPrintQualityHigh = 3
    catPrintQualityCustom = 4


class CatPrintRenderingMode(Enum):
    catPrintRenderingModeDefault = 0
    catPrintRenderingModeWireframe = 1
    catPrintRenderingModeHiddenLineRemoval = 2
    catPrintRenderingModeShadingWithTriangles = 3
    catPrintRenderingModeDynamicHiddenLineRemoval = 4
    catPrintRenderingModeOnScreen = 5


class CatProjectionMode(Enum):
    catProjectionConic = 0
    catProjectionCylindric = 1
    catProjectionUndefined = 2


class CatRenderingMode(Enum):
    catRenderShading = 0
    catRenderShadingWithEdges = 1
    catRenderWireFrame = 2
    catRenderHiddenLinesRemoval = 3
    catRenderQuickHiddenLinesRemoval = 4
    catRenderMaterial = 5
    catRenderMaterialWithEdges = 6
    catRenderShadingWithEdgesAndHiddenEdges = 7
    catRenderShadingWithEdgesWithoutSmoothEdges = 8
    catRenderWireFrameWithoutSmoothEdgesWithoutVertices = 9
    catRenderWireFrameWithHalfSmoothEdgesWithoutVertices = 10
    catRenderShadingWithEdgesWithOutlines = 11
    catRenderQuickHiddenLinesRemovalWithoutVertices = 12
    catRenderQuickHiddenLinesRemovalWithHiddenEdgesWithOutlines = 13
    catRenderQuickHiddenLinesRemovalWithHiddenEdgesWithOutlinesWithoutVertices = 14
    catRenderWireFrameWithHalfSmoothEdgeWithOutlinesWithoutVertices = 15
    catRenderWireFrameWithOutlinesWithoutSmoothEdgesWithoutVertices = 16
    catRenderQuickHiddenLinesRemovalWithHiddenEdgesWithoutSmoothEdgesWithoutVertices = 17
    catRenderQuickHiddenLinesRemovalWithHiddenEdgesWithHalfSmoothEdgeWithoutVertices = 18
    catRenderQuickHiddenLinesRemovalWithoutSmoothEdgesWithoutVertices = 19
    catRenderQuickHiddenLinesRemovalWithHalfSmoothEdgeWithoutVertices = 20
    catRenderShadingWithEdgesWithHalfSmoothEdgeWithoutVertices = 21
    catRenderShadingWithEdgesWithHalfSmoothEdge = 22
    catRenderRayTracingWithMaterial = 23
    catRenderRayTracingWithMaterialAndEdges = 24
    catRenderShadingWithEdgesWithOutlinesWithTransparency = 25
    catRenderShadingWithEdgesWithOutlinesWithTriangles = 26
    catRenderShadingWithEdgesWithoutOutlinesWithTransparency = 27
    catRenderShadingWithEdgesWithoutOutlinesWithTriangles = 28
    catRenderShadingWithEdgesWithHalfSmoothEdgeWithTransparency = 29
    catRenderShadingWithEdgesWithHalfSmoothEdgeWithTriangles = 30
    catRenderShadingWithTransparency = 31
    catRenderShadingWithTriangles = 32
    catRenderShadingWithEdgesWithoutOutlinesWithoutVerticesWithTransparency = 33
    catRenderShadingWithEdgesWithoutOutlinesWithoutVerticesWithTrangles = 34
    catRenderMaterialWithoutSmoothEdges = 35
    catRenderMaterialWithHalfSmoothEdge = 36
    catRenderMaterialWithHalfSmoothEdgeWithoutVertices = 37
    catRenderMaterialWithHalfSmoothEdgeWithoutVerticesWithOutlines = 38
    catRenderCustomRenderingMode = 39


class CatScriptCommand(Enum):
    CatScriptCommandDefault = 0
    CatScriptCommandStop = 1
    CatScriptCommandStart = 2


class CATSelectionFilter(Enum):
    ZeroDim = 0
    MonoDim = 1
    MonoDimInfinite = 2
    RectilinearMonoDim = 3
    RectilinearMonoDimInfinite = 4
    BiDim = 5
    BiDimInfinite = 6
    PlanarBiDim = 7
    PlanarBiDimInfinite = 8
    CylindricalBiDim = 9
    TriDim = 10


class CatSpecsAndGeomWindowLayout(Enum):
    catWindowSpecsOnly = 0
    catWindowGeomOnly = 1
    catWindowSpecsAndGeom = 2


class CatSpecsLayout(Enum):
    catSpecsViewerHorizontalIndented = 0
    catSpecsViewerHorizontalUp = 1
    catSpecsViewerHorizontalCentered = 2
    catSpecsViewerVerticalCentered = 3
    catSpecsViewerHorizontalRelational = 4
    catSpecsViewerVerticalRelational = 5


class CatVisLayerType(Enum):
    catVisLayerBasic = 0
    catVisLayerNone = 1


class CatVisPropertyPick(Enum):
    catVisPropertyPickAttr = 0
    catVisPropertyNoPickAttr = 1


class CatVisPropertyShow(Enum):
    catVisPropertyShowAttr = 0
    catVisPropertyNoShowAttr = 1


class CatVisPropertyStatus(Enum):
    catVisPropertyDefined = 0
    catVisPropertyUnDefined = 1


class CatVisPropertyType(Enum):
    catVisPropertyLineType = 0
    catVisPropertyWidth = 1
    catVisPropertyColor = 2
    catVisPropertyOpacity = 3
    catVisPropertySymbol = 4
    catVisPropertyAll = 5


class CatWindowState(Enum):
    catWindowStateMaximized = 0
    catWindowStateMinimized = 1
    catWindowStateNormal = 2
