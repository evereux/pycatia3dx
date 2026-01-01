from enum import IntEnum


class CatArrangeStyle(IntEnum):
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


class CatBannerPosition(IntEnum):
    catBannerPositionNone = 0
    catBannerPositionBottom = 1
    catBannerPositionTop = 2
    catBannerPositionLeft = 3
    catBannerPositionRight = 4


class CatCameraType(IntEnum):
    catCamera2D = 0
    catCamera3D = 1


class CatCaptureFormat(IntEnum):
    catCaptureFormatCGM = 0
    catCaptureFormatEMF = 1
    catCaptureFormatTIFF = 2
    catCaptureFormatTIFFGreyScale = 3
    catCaptureFormatBMP = 4
    catCaptureFormatJPEG = 5


class CatClippingMode(IntEnum):
    catClippingModeClear = 0
    catClippingModeNear = 1
    catClippingModeFar = 2
    catClippingModeNearAndFar = 3


class CatImageRotation(IntEnum):
    catImageNoRotation = 0
    catImageRotation90 = 1
    catImageRotation180 = 2
    catImageRotation270 = 3
    catImageBestRotation = 4


class CATInteractionType(IntEnum):
    CATSelection = 0
    CATIndication = 1
    CATMouseMove = 2
    CATInputUndo = 3
    CATInputRedo = 4
    CATEscape = 5
    CATOtherEditor = 6
    CATExclusiveCommand = 7


class CatLightingMode(IntEnum):
    catInfiniteLightSource = 0
    catNeonLightSource = 1


class CATMultiSelectionMode(IntEnum):
    CATMonoSel = 0
    CATMultiSelTriggWhenSelPerf = 1
    CATMultiSelTriggWhenUserValidatesSelection = 2


class CatNavigationStyle(IntEnum):
    catNavigationExamine = 0
    catNavigationWalk = 1
    catNavigationFly = 2


class CatPaperOrientation(IntEnum):
    catPaperPortrait = 0
    catPaperLandscape = 1
    catPaperBestFit = 2


class CatPaperSize(IntEnum):
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


class CATPPRTreeItemType(IntEnum):
    CATProcessList = 0
    CATProductList = 1
    CATResourcesList = 2


class CatPrintColor(IntEnum):
    catColorTrueColor = 0
    catColorGreyScale = 1
    catColorMonochrome = 2


class CatPrinterDirState(IntEnum):
    CatPrinterDirFree = 0
    CatPrinterDirProtect = 1


class CatPrintLineCap(IntEnum):
    catPrintFlat = 0
    catPrintSquare = 1
    catPrintRound = 2


class CatPrintLineSpecification(IntEnum):
    catPrintAbsolute = 0
    catPrintScaled = 1
    catPrintNoThickness = 2


class CatPrintQuality(IntEnum):
    catPrintQualityDraft = 0
    catPrintQualityLow = 1
    catPrintQualityMedium = 2
    catPrintQualityHigh = 3
    catPrintQualityCustom = 4


class CatPrintRenderingMode(IntEnum):
    catPrintRenderingModeDefault = 0
    catPrintRenderingModeWireframe = 1
    catPrintRenderingModeHiddenLineRemoval = 2
    catPrintRenderingModeShadingWithTriangles = 3
    catPrintRenderingModeDynamicHiddenLineRemoval = 4
    catPrintRenderingModeOnScreen = 5


class CatProjectionMode(IntEnum):
    catProjectionConic = 0
    catProjectionCylindric = 1
    catProjectionUndefined = 2


class CatRenderingMode(IntEnum):
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


class CatScriptCommand(IntEnum):
    CatScriptCommandDefault = 0
    CatScriptCommandStop = 1
    CatScriptCommandStart = 2


class CATSelectionFilter(IntEnum):
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


class CatSpecsAndGeomWindowLayout(IntEnum):
    catWindowSpecsOnly = 0
    catWindowGeomOnly = 1
    catWindowSpecsAndGeom = 2


class CatSpecsLayout(IntEnum):
    catSpecsViewerHorizontalIndented = 0
    catSpecsViewerHorizontalUp = 1
    catSpecsViewerHorizontalCentered = 2
    catSpecsViewerVerticalCentered = 3
    catSpecsViewerHorizontalRelational = 4
    catSpecsViewerVerticalRelational = 5


class CatVisLayerType(IntEnum):
    catVisLayerBasic = 0
    catVisLayerNone = 1


class CatVisPropertyPick(IntEnum):
    catVisPropertyPickAttr = 0
    catVisPropertyNoPickAttr = 1


class CatVisPropertyShow(IntEnum):
    catVisPropertyShowAttr = 0
    catVisPropertyNoShowAttr = 1


class CatVisPropertyStatus(IntEnum):
    catVisPropertyDefined = 0
    catVisPropertyUnDefined = 1


class CatVisPropertyType(IntEnum):
    catVisPropertyLineType = 0
    catVisPropertyWidth = 1
    catVisPropertyColor = 2
    catVisPropertyOpacity = 3
    catVisPropertySymbol = 4
    catVisPropertyAll = 5


class CatWindowState(IntEnum):
    catWindowStateMaximized = 0
    catWindowStateMinimized = 1
    catWindowStateNormal = 2
