from enum import Enum


class SimAnimationTypes(Enum):
    SimUndefAnimation = 0
    SimScaleFactor = 1
    SimTimeHistory = 2
    SimLoopOverModes = 3
    SimScanSingleFrame = 4
    SimTimeHistoryAndLoopover = 5
    SimFrameBased = 6
    SimStreamline = 7
    SimEventSeries = 8
    SimHarmonic = 9


class SimAnimPlaybackTypes(Enum):
    SimPlaybackFramesPerSec = 0
    SimPlaybackTotalTime = 1


class SimAveraging(Enum):
    SimSectionBoundaries = 0
    SimNoBoundaries = 1


class SimAxisType(Enum):
    SimNoAxis = 0
    SimGlobal = 1
    SimResultsCsys = 2
    SimResultsSim = 3
    SimModelAxis = 4
    SimNormalTangential = 5
    SimAxialTransverse = 6


class SimCalculationBetweenSupports(Enum):
    SimDiffSupport1AndSupport2 = 0
    SimDiffSupport2AndSupport1 = 1
    SimSumSupport1AndSupport2 = 2


class SimColumnSeparator(Enum):
    SimComma = 0
    SimSemicolon = 1


class SimComplexValues(Enum):
    SimValueAtAngle = 0
    SimEnvelopeMaxAbsolute = 1
    SimEnvelopeMax = 2
    SimEnvelopeMin = 3
    SimPhaseAngle = 4


class SimConfiguration(Enum):
    SimVPFourSquare = 0
    SimVPTriLeft = 1
    SimVPTriBottom = 2
    SimVPTwoRow = 3
    SimVPTwoColumn = 4
    SimVPSingle = 5


class SimFieldPlotTypes(Enum):
    SimContour = 0
    SimSymbol = 1
    SimIsoContour = 2
    SimColorCode = 3


class SimFileType(Enum):
    SimCsv = 0
    SimXlsx = 1
    SimXls = 2


class SimLocation(Enum):
    SimNodes = 0
    SimCentroids = 1
    SimFaceElements = 2
    SimIntegrationPoints = 3
    SimElementNodes = 4


class SimNodeSymbolType(Enum):
    SimNodeSymbolSphere = 0
    SimNodeSymbolCross = 1
    SimNodeSymbolPlus = 2
    SimNodeSymbolConcentric = 3
    SimNodeSymbolCoincident = 4
    SimNodeSymbolFullCircle = 5
    SimNodeSymbolFullSquare = 6
    SimNodeSymbolStar = 7
    SimNodeSymbolDot = 8
    SimNodeSymbolSmallDot = 9
    SimNodeSymbolFullCircle2 = 10
    SimNodeSymbolFullSquare2 = 11


class SimProcessingTypes(Enum):
    SimScalars = 0
    SimQuantity = 1
    SimTensors = 2
    SimVectors = 3


class SimQuantityComponentEnum(Enum):
    SimVector_Component_1 = 0
    SimTensor_Component_11 = 1
    Sim4th_Order_Tensor_Component_1111 = 2
    Sim4th_Order_Tensor_Component_1112 = 3
    Sim4th_Order_Tensor_Component_1122 = 4
    SimTensor_Component_12 = 5
    Sim4th_Order_Tensor_Component_1211 = 6
    Sim4th_Order_Tensor_Component_1212 = 7
    Sim4th_Order_Tensor_Component_1222 = 8
    SimTensor_Component_12_Engineering = 9
    SimTensor_Component_13 = 10
    SimTensor_Component_13_Engineering = 11
    SimVector_Component_2 = 12
    SimTensor_Component_21 = 13
    SimTensor_Component_22 = 14
    Sim4th_Order_Tensor_Component_2211 = 15
    Sim4th_Order_Tensor_Component_2212 = 16
    Sim4th_Order_Tensor_Component_2222 = 17
    SimTensor_Component_23 = 18
    SimTensor_Component_23_Engineering = 19
    SimVector_Component_3 = 20
    SimTensor_Component_31 = 21
    SimTensor_Component_32 = 22
    SimTensor_Component_33 = 23
    SimTensor_First_Principal = 24
    SimTensor_Second_Principal = 25
    SimTensor_Third_Principal = 26
    SimQuaternion_Component_0 = 27
    SimQuaternion_Component_1 = 28
    SimQuaternion_Component_2 = 29
    SimQuaternion_Component_3 = 30
    SimRotational_Vector_Component_1 = 31
    SimRotational_Vector_Component_2 = 32
    SimRotational_Vector_Component_3 = 33
    SimScalar = 34
    SimTensor_Minimum_Principal = 35
    SimTensor_Mid_Principal = 36
    SimTensor_Maximum_Principal = 37
    SimAll_Vector_Components = 38
    SimTensor_Maximum_InPlane_Principal = 39
    SimTensor_Minimum_InPlane_Principal = 40
    SimTensor_OutOfPlane_Principal = 41


class SimQuantityInvariantEnum(Enum):
    SimFirstVariant = 0
    SimThirdVariant = 1
    SimMagnitude = 2
    SimMaximum_In_Plane_Principal = 3
    SimMaximum_Principal = 4
    SimMid_Principal = 5
    SimMinimum_In_Plane_Principal = 6
    SimMinimum_Principal = 7
    SimMises_Equivalent = 8
    SimOutOfPlane_Principal = 9
    SimPressure = 10
    SimTresca_Equivalent = 11
    SimAbsolute_Maximum_Principal = 12
    SimAbsolute_Maximum_In_Plane_Principal = 13
    SimAbsolute_Principal_Magnitude = 14
    SimAbsolute_In_Plane_Principal_Magnitude = 15
    SimOrtho1 = 16
    SimOrtho2 = 17
    SimOrtho3 = 18


class SimRenderStyle(Enum):
    SimRenderContour = 0
    SimRenderShaded = 1
    SimRenderWireframe = 2


class SimResultsSource(Enum):
    SimFieldSourceResults = 0
    SimFieldSourceDiagnostic = 1
    SimFieldSourcePreLoad = 2
    SimFieldSourceHistory = 3
    SimFieldSourceCompute = 4


class SimSamplingFilterTypes(Enum):
    SimTimeInterval = 0
    SimFrameInterval = 1
    SimTotalFrames = 2


class SimSamplingRateTypes(Enum):
    SimAllSelectedFrames = 0
    SimRegularTimeInterval = 1
    SimRegularFrameInterval = 2


class SimSectionPointLocations(Enum):
    SimLocationUndefined = 0
    SimLocationNone = 1
    SimFirstSectionPoint = 2
    SimAllSectionPoints = 3
    SimTop = 4
    SimTopAndBottom = 5
    SimBottom = 6
    SimMiddle = 7
    SimMinMaxOverSectionPoints = 8
    SimMaxOverSectionPoints = 9
    SimAbsMaxOverSectionPoints = 10
    SimMinOverSectionPoints = 11
    SimSectionRatio = 12


class SimSectionPointLocation(Enum):
    SimSectionTop = 0
    SimSectionTopBottom = 1
    SimSectionBottom = 2


class SimSelectionType(Enum):
    SimNoSelection = 0
    SimDisplayGroups = 1
    SimCutSurfaces = 2
    SimNodeSets = 3
    SimElementSets = 4
    SimSurfaces = 5
    SimMeshGroups = 6
    SimRestraints = 7
    SimLoads = 8
    SimConnectorSections = 9


class SimShellStyle(Enum):
    SimShellNone = 0
    SimThick = 1
    SimOffset = 2
    SimElevation = 3


class SimStrainGaugePositionType(Enum):
    SimPositionPoint = 0
    SimPositionNode = 1
    SimPositionElementFace = 2


class SimStrainGaugeVariableType(Enum):
    SimStress = 0
    SimStrainFromStrain = 1
    SimStrainFromDisplacement = 2


class SimSymbolicFrameRangesEnum(Enum):
    SimUndefined = 0
    SimAllFrames = 1
    SimLastFrameOfEachStep = 2
    SimAllFramesInStep = 3
    SimTimeBasedFrames = 4
    SimFrequencyFrames = 5


class SimTargetSpeedTypes(Enum):
    SimTargetSpeedMax = 0
    SimTargetSpeedFramesPerSec = 1
    SimTargetSpeedDuration = 2


class SimThicknessDataSourceType(Enum):
    SimThickSourceSection = 0
    SimThickSourceField = 1


class SimThresholdType(Enum):
    SimThresholdNone = 0
    SimThresholdLowerLimit = 1
    SimThresholdUpperLimit = 2
    SimThresholdPercentLowerLimit = 3
    SimThresholdPercentUpperLimit = 4


class SimTransformTypes(Enum):
    SimNone = 0
    SimNodal = 1
    SimUserDefined = 2
    SimUserModelAxis = 3


class SimValuePerSupportOption(Enum):
    SimValuePerSupportNone = 0
    SimValuePerSupportMax = 1
    SimValuePerSupportMin = 2
    SimValuePerSupportAbsoluteMax = 3
    SimValuePerSupportAverage = 4
    SimValuePerSupportSum = 5
    SimValuePerSupportLast = 6


class SimVisibleEdges(Enum):
    SimOutline = 0
    SimMesh = 1
    SimVisibleEdgesNone = 2
