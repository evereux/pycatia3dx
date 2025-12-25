from enum import Enum


class SimAnimationTypes(Enum):
    SimScaleFactor = 0
    SimTimeHistory = 1
    SimStreamline = 2
    SimFrameBased = 3
    SimHarmonic = 4
    SimEventSeries = 5
    SimTimeHistoryAndLoopover = 6
    SimUndefAnimation = 7
    SimScanSingleFrame = 8
    SimLoopOverModes = 9


class SimAnimPlaybackTypes(Enum):
    SimPlaybackFramesPerSec = 0
    SimPlaybackTotalTime = 1


class SimAveraging(Enum):
    SimSectionBoundaries = 0
    SimNoBoundaries = 1


class SimAxisType(Enum):
    SimNoAxis = 0
    SimAxialTransverse = 1
    SimGlobal = 2
    SimNormalTangential = 3
    SimModelAxis = 4
    SimResultsCsys = 5
    SimResultsSim = 6


class SimCalculationBetweenSupports(Enum):
    SimDiffSupport2AndSupport1 = 0
    SimDiffSupport1AndSupport2 = 1
    SimSumSupport1AndSupport2 = 2


class SimColumnSeparator(Enum):
    SimComma = 0
    SimSemicolon = 1


class SimComplexValues(Enum):
    SimEnvelopeMin = 0
    SimPhaseAngle = 1
    SimEnvelopeMaxAbsolute = 2
    SimValueAtAngle = 3
    SimEnvelopeMax = 4


class SimConfiguration(Enum):
    SimVPSingle = 0
    SimVPTriBottom = 1
    SimVPTwoRow = 2
    SimVPFourSquare = 3
    SimVPTwoColumn = 4
    SimVPTriLeft = 5


class SimFieldPlotTypes(Enum):
    SimColorCode = 0
    SimIsoContour = 1
    SimContour = 2
    SimSymbol = 3


class SimFileType(Enum):
    SimXls = 0
    SimCsv = 1
    SimXlsx = 2


class SimLocation(Enum):
    SimCentroids = 0
    SimElementNodes = 1
    SimNodes = 2
    SimFaceElements = 3
    SimIntegrationPoints = 4


class SimNodeSymbolType(Enum):
    SimNodeSymbolSphere = 0
    SimNodeSymbolFullSquare = 1
    SimNodeSymbolDot = 2
    SimNodeSymbolCross = 3
    SimNodeSymbolSmallDot = 4
    SimNodeSymbolFullCircle2 = 5
    SimNodeSymbolStar = 6
    SimNodeSymbolConcentric = 7
    SimNodeSymbolPlus = 8
    SimNodeSymbolFullSquare2 = 9
    SimNodeSymbolCoincident = 10
    SimNodeSymbolFullCircle = 11


class SimProcessingTypes(Enum):
    SimScalars = 0
    SimQuantity = 1
    SimTensors = 2
    SimVectors = 3


class SimQuantityComponentEnum(Enum):
    SimVector_Component_1 = 0
    SimTensor_Component_32 = 1
    SimTensor_Component_23_Engineering = 2
    Sim4th_Order_Tensor_Component_2222 = 3
    SimVector_Component_3 = 4
    SimQuaternion_Component_1 = 5
    SimTensor_Component_31 = 6
    SimTensor_Second_Principal = 7
    SimQuaternion_Component_0 = 8
    SimVector_Component_2 = 9
    Sim4th_Order_Tensor_Component_2212 = 10
    SimTensor_Minimum_InPlane_Principal = 11
    Sim4th_Order_Tensor_Component_1122 = 12
    SimRotational_Vector_Component_1 = 13
    SimRotational_Vector_Component_2 = 14
    Sim4th_Order_Tensor_Component_1111 = 15
    SimTensor_Component_11 = 16
    Sim4th_Order_Tensor_Component_1222 = 17
    SimRotational_Vector_Component_3 = 18
    SimTensor_Maximum_Principal = 19
    Sim4th_Order_Tensor_Component_2211 = 20
    SimTensor_Component_22 = 21
    SimTensor_Component_21 = 22
    SimTensor_Mid_Principal = 23
    SimAll_Vector_Components = 24
    SimTensor_Maximum_InPlane_Principal = 25
    SimTensor_Component_12 = 26
    SimTensor_Component_13 = 27
    SimTensor_Component_33 = 28
    SimQuaternion_Component_2 = 29
    Sim4th_Order_Tensor_Component_1211 = 30
    SimTensor_Minimum_Principal = 31
    SimQuaternion_Component_3 = 32
    Sim4th_Order_Tensor_Component_1212 = 33
    SimTensor_Third_Principal = 34
    SimTensor_First_Principal = 35
    SimTensor_OutOfPlane_Principal = 36
    Sim4th_Order_Tensor_Component_1112 = 37
    SimTensor_Component_12_Engineering = 38
    SimTensor_Component_13_Engineering = 39
    SimScalar = 40
    SimTensor_Component_23 = 41


class SimQuantityInvariantEnum(Enum):
    SimOrtho2 = 0
    SimAbsolute_In_Plane_Principal_Magnitude = 1
    SimTresca_Equivalent = 2
    SimOrtho3 = 3
    SimPressure = 4
    SimOutOfPlane_Principal = 5
    SimMinimum_In_Plane_Principal = 6
    SimMagnitude = 7
    SimThirdVariant = 8
    SimAbsolute_Principal_Magnitude = 9
    SimAbsolute_Maximum_Principal = 10
    SimMinimum_Principal = 11
    SimMises_Equivalent = 12
    SimOrtho1 = 13
    SimMaximum_In_Plane_Principal = 14
    SimMaximum_Principal = 15
    SimMid_Principal = 16
    SimFirstVariant = 17
    SimAbsolute_Maximum_In_Plane_Principal = 18


class SimRenderStyle(Enum):
    SimRenderWireframe = 0
    SimRenderContour = 1
    SimRenderShaded = 2


class SimResultsSource(Enum):
    SimFieldSourcePreLoad = 0
    SimFieldSourceResults = 1
    SimFieldSourceDiagnostic = 2
    SimFieldSourceHistory = 3
    SimFieldSourceCompute = 4


class SimSamplingFilterTypes(Enum):
    SimTotalFrames = 0
    SimFrameInterval = 1
    SimTimeInterval = 2


class SimSamplingRateTypes(Enum):
    SimRegularFrameInterval = 0
    SimAllSelectedFrames = 1
    SimRegularTimeInterval = 2


class SimSectionPointLocations(Enum):
    SimAbsMaxOverSectionPoints = 0
    SimFirstSectionPoint = 1
    SimTop = 2
    SimAllSectionPoints = 3
    SimMinOverSectionPoints = 4
    SimMiddle = 5
    SimTopAndBottom = 6
    SimMaxOverSectionPoints = 7
    SimMinMaxOverSectionPoints = 8
    SimLocationUndefined = 9
    SimBottom = 10
    SimLocationNone = 11
    SimSectionRatio = 12


class SimSectionPointLocation(Enum):
    SimSectionBottom = 0
    SimSectionTop = 1
    SimSectionTopBottom = 2


class SimSelectionType(Enum):
    SimRestraints = 0
    SimConnectorSections = 1
    SimLoads = 2
    SimCutSurfaces = 3
    SimDisplayGroups = 4
    SimElementSets = 5
    SimNodeSets = 6
    SimNoSelection = 7
    SimSurfaces = 8
    SimMeshGroups = 9


class SimShellStyle(Enum):
    SimShellNone = 0
    SimElevation = 1
    SimOffset = 2
    SimThick = 3


class SimStrainGaugePositionType(Enum):
    SimPositionElementFace = 0
    SimPositionPoint = 1
    SimPositionNode = 2


class SimStrainGaugeVariableType(Enum):
    SimStrainFromStrain = 0
    SimStress = 1
    SimStrainFromDisplacement = 2


class SimSymbolicFrameRangesEnum(Enum):
    SimAllFramesInStep = 0
    SimAllFrames = 1
    SimUndefined = 2
    SimLastFrameOfEachStep = 3
    SimFrequencyFrames = 4
    SimTimeBasedFrames = 5


class SimTargetSpeedTypes(Enum):
    SimTargetSpeedMax = 0
    SimTargetSpeedFramesPerSec = 1
    SimTargetSpeedDuration = 2


class SimThicknessDataSourceType(Enum):
    SimThickSourceField = 0
    SimThickSourceSection = 1


class SimThresholdType(Enum):
    SimThresholdLowerLimit = 0
    SimThresholdNone = 1
    SimThresholdPercentUpperLimit = 2
    SimThresholdUpperLimit = 3
    SimThresholdPercentLowerLimit = 4


class SimTransformTypes(Enum):
    SimNodal = 0
    SimNone = 1
    SimUserDefined = 2
    SimUserModelAxis = 3


class SimValuePerSupportOption(Enum):
    SimValuePerSupportSum = 0
    SimValuePerSupportAbsoluteMax = 1
    SimValuePerSupportMax = 2
    SimValuePerSupportMin = 3
    SimValuePerSupportLast = 4
    SimValuePerSupportAverage = 5
    SimValuePerSupportNone = 6


class SimVisibleEdges(Enum):
    SimOutline = 0
    SimVisibleEdgesNone = 1
    SimMesh = 2


