from enum import Enum


class CatArrangeStyle(Enum):
    catArrangeTiledHorizontalInCurrentTab = 0
    catArrangeTiledVerticalInCurrentTab = 1
    catArrangeTiledVertical = 2
    catArrangeTiledGridInAllTab = 3
    catArrangeTiledGridInNewTab = 4
    catArrangeTiledHorizontalInAllTab = 5
    catArrangeTiledVerticalInNewTab = 6
    catArrangeTiledVerticalInAllTab = 7
    catArrangeCascade = 8
    catArrangeTiledHorizontal = 9
    catArrangeTiledGridInCurrentTab = 10
    catArrangeTiledHorizontalInNewTab = 11


class CatBannerPosition(Enum):
    catBannerPositionBottom = 0
    catBannerPositionLeft = 1
    catBannerPositionNone = 2
    catBannerPositionTop = 3
    catBannerPositionRight = 4


class CatCameraType(Enum):
    catCamera3D = 0
    catCamera2D = 1


class CatCaptureFormat(Enum):
    catCaptureFormatBMP = 0
    catCaptureFormatTIFF = 1
    catCaptureFormatEMF = 2
    catCaptureFormatJPEG = 3
    catCaptureFormatTIFFGreyScale = 4
    catCaptureFormatCGM = 5


class CatClippingMode(Enum):
    catClippingModeClear = 0
    catClippingModeFar = 1
    catClippingModeNear = 2
    catClippingModeNearAndFar = 3


class CatImageRotation(Enum):
    catImageNoRotation = 0
    catImageRotation180 = 1
    catImageBestRotation = 2
    catImageRotation90 = 3
    catImageRotation270 = 4


class CATInteractionType(Enum):
    CATEscape = 0
    CATOtherEditor = 1
    CATSelection = 2
    CATInputRedo = 3
    CATMouseMove = 4
    CATInputUndo = 5
    CATExclusiveCommand = 6
    CATIndication = 7


class CatLightingMode(Enum):
    catNeonLightSource = 0
    catInfiniteLightSource = 1


class CATMultiSelectionMode(Enum):
    CATMultiSelTriggWhenSelPerf = 0
    CATMultiSelTriggWhenUserValidatesSelection = 1
    CATMonoSel = 2


class CatNavigationStyle(Enum):
    catNavigationExamine = 0
    catNavigationFly = 1
    catNavigationWalk = 2


class CatPaperOrientation(Enum):
    catPaperPortrait = 0
    catPaperLandscape = 1
    catPaperBestFit = 2


class CatPaperSize(Enum):
    catPaperC = 0
    catPaperB = 1
    catPaperA4 = 2
    catPaperLetter = 3
    catPaperE = 4
    catPaperUser = 5
    catPaperF = 6
    catPaperA0 = 7
    catPaperD = 8
    catPaperA = 9
    catPaperA3 = 10
    catPaperA1 = 11
    catPaperA2 = 12
    catPaperLegal = 13


class CATPPRTreeItemType(Enum):
    CATResourcesList = 0
    CATProcessList = 1
    CATProductList = 2


class CatPrintColor(Enum):
    catColorTrueColor = 0
    catColorGreyScale = 1
    catColorMonochrome = 2


class CatPrinterDirState(Enum):
    CatPrinterDirProtect = 0
    CatPrinterDirFree = 1


class CatPrintLineCap(Enum):
    catPrintFlat = 0
    catPrintRound = 1
    catPrintSquare = 2


class CatPrintLineSpecification(Enum):
    catPrintScaled = 0
    catPrintAbsolute = 1
    catPrintNoThickness = 2


class CatPrintQuality(Enum):
    catPrintQualityHigh = 0
    catPrintQualityCustom = 1
    catPrintQualityDraft = 2
    catPrintQualityLow = 3
    catPrintQualityMedium = 4


class CatPrintRenderingMode(Enum):
    catPrintRenderingModeShadingWithTriangles = 0
    catPrintRenderingModeWireframe = 1
    catPrintRenderingModeDefault = 2
    catPrintRenderingModeHiddenLineRemoval = 3
    catPrintRenderingModeOnScreen = 4
    catPrintRenderingModeDynamicHiddenLineRemoval = 5


class CatProjectionMode(Enum):
    catProjectionCylindric = 0
    catProjectionUndefined = 1
    catProjectionConic = 2


class CatRenderingMode(Enum):
    catRenderMaterialWithoutSmoothEdges = 0
    catRenderQuickHiddenLinesRemovalWithHalfSmoothEdgeWithoutVertices = 1
    catRenderShadingWithEdgesWithoutOutlinesWithoutVerticesWithTransparency = 2
    catRenderCustomRenderingMode = 3
    catRenderShadingWithTransparency = 4
    catRenderShadingWithEdgesWithOutlines = 5
    catRenderShadingWithEdgesWithoutOutlinesWithTransparency = 6
    catRenderWireFrameWithHalfSmoothEdgesWithoutVertices = 7
    catRenderWireFrame = 8
    catRenderShadingWithEdgesWithHalfSmoothEdge = 9
    catRenderRayTracingWithMaterial = 10
    catRenderWireFrameWithHalfSmoothEdgeWithOutlinesWithoutVertices = 11
    catRenderMaterialWithHalfSmoothEdgeWithoutVertices = 12
    catRenderShadingWithEdgesWithOutlinesWithTriangles = 13
    catRenderQuickHiddenLinesRemovalWithoutVertices = 14
    catRenderQuickHiddenLinesRemovalWithHiddenEdgesWithOutlinesWithoutVertices = 15
    catRenderWireFrameWithoutSmoothEdgesWithoutVertices = 16
    catRenderMaterialWithHalfSmoothEdgeWithoutVerticesWithOutlines = 17
    catRenderQuickHiddenLinesRemovalWithHiddenEdgesWithHalfSmoothEdgeWithoutVertices = 18
    catRenderQuickHiddenLinesRemoval = 19
    catRenderHiddenLinesRemoval = 20
    catRenderShadingWithEdgesWithoutOutlinesWithoutVerticesWithTrangles = 21
    catRenderShadingWithTriangles = 22
    catRenderWireFrameWithOutlinesWithoutSmoothEdgesWithoutVertices = 23
    catRenderShadingWithEdgesAndHiddenEdges = 24
    catRenderShadingWithEdgesWithOutlinesWithTransparency = 25
    catRenderShadingWithEdgesWithHalfSmoothEdgeWithoutVertices = 26
    catRenderQuickHiddenLinesRemovalWithHiddenEdgesWithoutSmoothEdgesWithoutVertices = 27
    catRenderShadingWithEdgesWithoutOutlinesWithTriangles = 28
    catRenderQuickHiddenLinesRemovalWithHiddenEdgesWithOutlines = 29
    catRenderQuickHiddenLinesRemovalWithoutSmoothEdgesWithoutVertices = 30
    catRenderShadingWithEdgesWithHalfSmoothEdgeWithTriangles = 31
    catRenderShading = 32
    catRenderMaterial = 33
    catRenderMaterialWithHalfSmoothEdge = 34
    catRenderRayTracingWithMaterialAndEdges = 35
    catRenderShadingWithEdgesWithoutSmoothEdges = 36
    catRenderShadingWithEdgesWithHalfSmoothEdgeWithTransparency = 37
    catRenderMaterialWithEdges = 38
    catRenderShadingWithEdges = 39


class CatScriptCommand(Enum):
    CatScriptCommandDefault = 0
    CatScriptCommandStop = 1
    CatScriptCommandStart = 2


class CATSelectionFilter(Enum):
    CylindricalBiDim = 0
    RectilinearMonoDim = 1
    RectilinearMonoDimInfinite = 2
    PlanarBiDim = 3
    BiDim = 4
    ZeroDim = 5
    MonoDim = 6
    BiDimInfinite = 7
    MonoDimInfinite = 8
    TriDim = 9
    PlanarBiDimInfinite = 10


class CatSpecsAndGeomWindowLayout(Enum):
    catWindowSpecsOnly = 0
    catWindowSpecsAndGeom = 1
    catWindowGeomOnly = 2


class CatSpecsLayout(Enum):
    catSpecsViewerHorizontalUp = 0
    catSpecsViewerVerticalCentered = 1
    catSpecsViewerVerticalRelational = 2
    catSpecsViewerHorizontalIndented = 3
    catSpecsViewerHorizontalRelational = 4
    catSpecsViewerHorizontalCentered = 5


class CatVisLayerType(Enum):
    catVisLayerNone = 0
    catVisLayerBasic = 1


class CatVisPropertyPick(Enum):
    catVisPropertyNoPickAttr = 0
    catVisPropertyPickAttr = 1


class CatVisPropertyShow(Enum):
    catVisPropertyNoShowAttr = 0
    catVisPropertyShowAttr = 1


class CatVisPropertyStatus(Enum):
    catVisPropertyDefined = 0
    catVisPropertyUnDefined = 1


class CatVisPropertyType(Enum):
    catVisPropertySymbol = 0
    catVisPropertyColor = 1
    catVisPropertyLineType = 2
    catVisPropertyAll = 3
    catVisPropertyOpacity = 4
    catVisPropertyWidth = 5


class CatWindowState(Enum):
    catWindowStateNormal = 0
    catWindowStateMaximized = 1
    catWindowStateMinimized = 2


