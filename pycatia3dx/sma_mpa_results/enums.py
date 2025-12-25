SimAnimationTypes = [
    'SimUndefAnimation',
    'SimScaleFactor',
    'SimTimeHistory',
    'SimLoopOverModes',
    'SimScanSingleFrame',
    'SimTimeHistoryAndLoopover',
    'SimFrameBased',
    'SimStreamline',
    'SimEventSeries',
    'SimHarmonic',
]
SimAnimPlaybackTypes = [
    'SimPlaybackFramesPerSec',
    'SimPlaybackTotalTime',
]
SimAveraging = [
    'SimSectionBoundaries',
    'SimNoBoundaries',
]
SimAxisType = [
    'SimNoAxis',
    'SimGlobal',
    'SimResultsCsys',
    'SimResultsSim',
    'SimModelAxis',
    'SimNormalTangential',
    'SimAxialTransverse',
]
SimCalculationBetweenSupports = [
    'SimDiffSupport1AndSupport2',
    'SimDiffSupport2AndSupport1',
    'SimSumSupport1AndSupport2',
]
SimColumnSeparator = [
    'SimComma',
    'SimSemicolon',
]
SimComplexValues = [
    'SimValueAtAngle',
    'SimEnvelopeMaxAbsolute',
    'SimEnvelopeMax',
    'SimEnvelopeMin',
    'SimPhaseAngle',
]
SimConfiguration = [
    'SimVPFourSquare',
    'SimVPTriLeft',
    'SimVPTriBottom',
    'SimVPTwoRow',
    'SimVPTwoColumn',
    'SimVPSingle',
]
SimFieldPlotTypes = [
    'SimContour',
    'SimSymbol',
    'SimIsoContour',
    'SimColorCode',
]
SimFileType = [
    'SimCsv',
    'SimXlsx',
    'SimXls',
]
SimLocation = [
    'SimNodes',
    'SimCentroids',
    'SimFaceElements',
    'SimIntegrationPoints',
    'SimElementNodes',
]
SimNodeSymbolType = [
    'SimNodeSymbolSphere',
    'SimNodeSymbolCross',
    'SimNodeSymbolPlus',
    'SimNodeSymbolConcentric',
    'SimNodeSymbolCoincident',
    'SimNodeSymbolFullCircle',
    'SimNodeSymbolFullSquare',
    'SimNodeSymbolStar',
    'SimNodeSymbolDot',
    'SimNodeSymbolSmallDot',
    'SimNodeSymbolFullCircle2',
    'SimNodeSymbolFullSquare2',
]
SimProcessingTypes = [
    'SimScalars',
    'SimQuantity',
    'SimTensors',
    'SimVectors',
]
SimQuantityComponentEnum = [
    'SimVector_Component_1',
    'SimTensor_Component_11',
    'Sim4th_Order_Tensor_Component_1111',
    'Sim4th_Order_Tensor_Component_1112',
    'Sim4th_Order_Tensor_Component_1122',
    'SimTensor_Component_12',
    'Sim4th_Order_Tensor_Component_1211',
    'Sim4th_Order_Tensor_Component_1212',
    'Sim4th_Order_Tensor_Component_1222',
    'SimTensor_Component_12_Engineering',
    'SimTensor_Component_13',
    'SimTensor_Component_13_Engineering',
    'SimVector_Component_2',
    'SimTensor_Component_21',
    'SimTensor_Component_22',
    'Sim4th_Order_Tensor_Component_2211',
    'Sim4th_Order_Tensor_Component_2212',
    'Sim4th_Order_Tensor_Component_2222',
    'SimTensor_Component_23',
    'SimTensor_Component_23_Engineering',
    'SimVector_Component_3',
    'SimTensor_Component_31',
    'SimTensor_Component_32',
    'SimTensor_Component_33',
    'SimTensor_First_Principal',
    'SimTensor_Second_Principal',
    'SimTensor_Third_Principal',
    'SimQuaternion_Component_0',
    'SimQuaternion_Component_1',
    'SimQuaternion_Component_2',
    'SimQuaternion_Component_3',
    'SimRotational_Vector_Component_1',
    'SimRotational_Vector_Component_2',
    'SimRotational_Vector_Component_3',
    'SimScalar',
    'SimTensor_Minimum_Principal',
    'SimTensor_Mid_Principal',
    'SimTensor_Maximum_Principal',
    'SimAll_Vector_Components',
    'SimTensor_Maximum_InPlane_Principal',
    'SimTensor_Minimum_InPlane_Principal',
    'SimTensor_OutOfPlane_Principal',
]
SimQuantityInvariantEnum = [
    'SimFirstVariant',
    'SimThirdVariant',
    'SimMagnitude',
    'SimMaximum_In_Plane_Principal',
    'SimMaximum_Principal',
    'SimMid_Principal',
    'SimMinimum_In_Plane_Principal',
    'SimMinimum_Principal',
    'SimMises_Equivalent',
    'SimOutOfPlane_Principal',
    'SimPressure',
    'SimTresca_Equivalent',
    'SimAbsolute_Maximum_Principal',
    'SimAbsolute_Maximum_In_Plane_Principal',
    'SimAbsolute_Principal_Magnitude',
    'SimAbsolute_In_Plane_Principal_Magnitude',
    'SimOrtho1',
    'SimOrtho2',
    'SimOrtho3',
]
SimRenderStyle = [
    'SimRenderContour',
    'SimRenderShaded',
    'SimRenderWireframe',
]
SimResultsSource = [
    'SimFieldSourceResults',
    'SimFieldSourceDiagnostic',
    'SimFieldSourcePreLoad',
    'SimFieldSourceHistory',
    'SimFieldSourceCompute',
]
SimSamplingFilterTypes = [
    'SimTimeInterval',
    'SimFrameInterval',
    'SimTotalFrames',
]
SimSamplingRateTypes = [
    'SimAllSelectedFrames',
    'SimRegularTimeInterval',
    'SimRegularFrameInterval',
]
SimSectionPointLocations = [
    'SimLocationUndefined',
    'SimLocationNone',
    'SimFirstSectionPoint',
    'SimAllSectionPoints',
    'SimTop',
    'SimTopAndBottom',
    'SimBottom',
    'SimMiddle',
    'SimMinMaxOverSectionPoints',
    'SimMaxOverSectionPoints',
    'SimAbsMaxOverSectionPoints',
    'SimMinOverSectionPoints',
    'SimSectionRatio',
]
SimSectionPointLocation = [
    'SimSectionTop',
    'SimSectionTopBottom',
    'SimSectionBottom',
]
SimSelectionType = [
    'SimNoSelection',
    'SimDisplayGroups',
    'SimCutSurfaces',
    'SimNodeSets',
    'SimElementSets',
    'SimSurfaces',
    'SimMeshGroups',
    'SimRestraints',
    'SimLoads',
    'SimConnectorSections',
]
SimShellStyle = [
    'SimShellNone',
    'SimThick',
    'SimOffset',
    'SimElevation',
]
SimStrainGaugePositionType = [
    'SimPositionPoint',
    'SimPositionNode',
    'SimPositionElementFace',
]
SimStrainGaugeVariableType = [
    'SimStress',
    'SimStrainFromStrain',
    'SimStrainFromDisplacement',
]
SimSymbolicFrameRangesEnum = [
    'SimUndefined',
    'SimAllFrames',
    'SimLastFrameOfEachStep',
    'SimAllFramesInStep',
    'SimTimeBasedFrames',
    'SimFrequencyFrames',
]
SimTargetSpeedTypes = [
    'SimTargetSpeedMax',
    'SimTargetSpeedFramesPerSec',
    'SimTargetSpeedDuration',
]
SimThicknessDataSourceType = [
    'SimThickSourceSection',
    'SimThickSourceField',
]
SimThresholdType = [
    'SimThresholdNone',
    'SimThresholdLowerLimit',
    'SimThresholdUpperLimit',
    'SimThresholdPercentLowerLimit',
    'SimThresholdPercentUpperLimit',
]
SimTransformTypes = [
    'SimNone',
    'SimNodal',
    'SimUserDefined',
    'SimUserModelAxis',
]
SimValuePerSupportOption = [
    'SimValuePerSupportNone',
    'SimValuePerSupportMax',
    'SimValuePerSupportMin',
    'SimValuePerSupportAbsoluteMax',
    'SimValuePerSupportAverage',
    'SimValuePerSupportSum',
    'SimValuePerSupportLast',
]
SimVisibleEdges = [
    'SimOutline',
    'SimMesh',
    'SimVisibleEdgesNone',
]
