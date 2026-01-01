from enum import IntEnum


class SimAcousticCouplingFormulationType(IntEnum):
    SimAcousticCouplingNodeToSurface = 0
    SimAcousticCouplingSurfaceToSurface = 1


class SimAcousticCouplingMainSurfaceType(IntEnum):
    SimAcousticCouplingElementBasedMainSurface = 0
    SimAcousticCouplingNodeBasedMainSurface = 1


class SimAcousticCouplingMasterSurfaceType(IntEnum):
    SimAcousticCouplingElementBased = 0
    SimAcousticCouplingNodeBased = 1


class SimAmplitudeDefinitionType(IntEnum):
    SimAmplitudeTabularDefinition = 0
    SimAmplitudeSmoothStepDefinition = 1
    SimAmplitudePeriodicDefinition = 2
    SimAmplitudeUserDefinition = 3


class SimAmplitudeTimeSpanType(IntEnum):
    SimAmplitudeStepTime = 0
    SimAmplitudeTotalTime = 1


class SimAMSEigensolverAcousticCouplingType(IntEnum):
    SimAMSEigensolverOn = 0
    SimAMSEigensolverProjection = 1
    SimAMSEigensolverOff = 2


class SimApplicationType(IntEnum):
    SimApplicationType_Solver_Default = 0
    SimApplicationType_Transient_Fidelity = 1
    SimApplicationType_Moderate_Dissipation = 2
    SimApplicationType_Quasi_Static = 3


class SimBeamLoadComponentSystem(IntEnum):
    SimBeamLoadGlobalComponentSystem = 0
    SimBeamLoadLocalComponentSystem = 1


class SimBearingLoadInteractionType(IntEnum):
    SimBearingLoadOutward = 0
    SimBearingLoadInward = 1


class SimBearingLoadOrientationType(IntEnum):
    SimBearingLoadRadial = 0
    SimBearingLoadParallel = 1


class SimBearingLoadProfileType(IntEnum):
    SimBearingLoadSinusoidal = 0
    SimBearingLoadParabolic = 1


class SimBuckleStepSolverType(IntEnum):
    SimBuckleStepLANCZOS = 0
    SimBuckleStepSUBSPACE = 1


class SimConnectorDampingDampingOrder(IntEnum):
    SimConnectorDampingLinear = 0
    SimConnectorDampingNonLinear = 1


class SimConnectorDampingTableColumn(IntEnum):
    SimConnectorDampingCoefficient = 0
    SimConnectorDampingTemperature = 1
    SimConnectorDampingVelocity = 2


class SimConnectorRotationVariationType(IntEnum):
    SimConnectorRotationUniform = 0
    SimConnectorRotationUserDefined = 1


class SimConnectorRotationVelocityVariationType(IntEnum):
    SimConnectorRotationVelocityUniform = 0
    SimConnectorRotationVelocityUserDefined = 1


class SimConnectorTranslationVariationType(IntEnum):
    SimConnectorTranslationUniform = 0
    SimConnectorTranslationUserDefined = 1


class SimConnectorTranslationVelocityVariationType(IntEnum):
    SimConnectorTranslationVelocityUniform = 0
    SimConnectorTranslationVelocityUserDefined = 1


class SimCoupledCreepIntegration(IntEnum):
    SimCoupledImplicit = 0
    SimCoupledExplicit = 1


class SimCoupledSolutionTechnique(IntEnum):
    SimCoupledFullNewton = 0
    SimCoupledSeparated = 1


class SimCoupledThermalResponseType(IntEnum):
    SimCoupledThermalSteadyState = 0
    SimCoupledThermalTransient = 1


class SimDirectHarmonicResponseStepIntervalType(IntEnum):
    SimDirectHarmonicResponseStepFrequencyIncrement = 0
    SimDirectHarmonicResponseStepEigenFrequency = 1
    SimDirectHarmonicResponseStepDirectRange = 2
    SimDirectHarmonicResponseStepFrequencySpread = 3


class SimDirectHarmonicResponseStepScaleType(IntEnum):
    SimDirectHarmonicResponseStepLogarithmic = 0
    SimDirectHarmonicResponseStepLinear = 1


class SimDirectHarmonicResponseStepTableColumn(IntEnum):
    SimDirectHarmonicResponseStepLower = 0
    SimDirectHarmonicResponseStepUpper = 1
    SimDirectHarmonicResponseStepIncrement = 2
    SimDirectHarmonicResponseStepNumberOfPoints = 3
    SimDirectHarmonicResponseStepBias = 4
    SimDirectHarmonicResponseStepScaleFactor = 5
    SimDirectHarmonicResponseStepSpread = 6


class SimExplicitDynamicStepFixedIncrementationTypeEnm(IntEnum):
    SimExplicitDynamicStepELEMENTBYELEMENT = 0
    SimExplicitDynamicStepUSERDEFINED = 1


class SimFrequencyBasedDampingDampingType(IntEnum):
    SimFrequencyBasedDampingCriticalDampingFraction = 0
    SimFrequencyBasedDampingStructuralDamping = 1
    SimFrequencyBasedDampingRayleighDamping = 2


class SimFrequencyBasedDampingModesType(IntEnum):
    SimFrequencyBasedDampingStructuralAndAcoustic = 0
    SimFrequencyBasedDampingStructural = 1
    SimFrequencyBasedDampingAcoustic = 2


class SimFrequencyBasedDampingTableColumn(IntEnum):
    SimFrequencyBasedDampingFrequency = 0
    SimFrequencyBasedDampingDampingFraction = 1
    SimFrequencyBasedDampingDampingFactor = 2
    SimFrequencyBasedDampingMassDamping = 3
    SimFrequencyBasedDampingStiffnessDamping = 4


class SimFrequencyStepSolverType(IntEnum):
    SimFrequencyStepLanczos = 0
    SimFrequencyStepAMS = 1


class SimGeneralGlobalDampingModesType(IntEnum):
    SimGeneralGlobalDampingNone = 0
    SimGeneralGlobalDampingStructuralAndAcoustic = 1
    SimGeneralGlobalDampingStructural = 2
    SimGeneralGlobalDampingAcoustic = 3


class SimHarmonicResponseStepIntervalType(IntEnum):
    SimHarmonicResponseStepFrequencyIncrement = 0
    SimHarmonicResponseStepEigenfrequency = 1
    SimHarmonicResponseStepDirectRange = 2
    SimHarmonicResponseStepFrequencySpread = 3


class SimHarmonicResponseStepProjectionType(IntEnum):
    SimHarmonicResponseStepNone = 0
    SimHarmonicResponseStepAllFrequency = 1
    SimHarmonicResponseStepCenterFrequencies = 2
    SimHarmonicResponseStepRangeValues = 3


class SimHarmonicResponseStepScaleType(IntEnum):
    SimHarmonicResponseStepLogarithmic = 0
    SimHarmonicResponseStepLinear = 1


class SimHarmonicResponseStepTableColumn(IntEnum):
    SimHarmonicResponseStepLower = 0
    SimHarmonicResponseStepUpper = 1
    SimHarmonicResponseStepIncrement = 2
    SimHarmonicResponseStepNumberOfPoints = 3
    SimHarmonicResponseStepBias = 4
    SimHarmonicResponseStepScaleFactor = 5
    SimHarmonicResponseStepSpread = 6


class SimInitialStressType(IntEnum):
    SimInitialStressTensorStress = 0
    SimInitialStressRebarStress = 1


class SimLanczosEigensolverAcousticCouplingType(IntEnum):
    SimLanczosEigensolverOn = 0
    SimLanczosEigensolverProjection = 1
    SimLanczosEigensolverOff = 2


class SimMassScalingMassScalingBehavior(IntEnum):
    SimMassScalingBeginningOfStep = 0
    SimMassScalingThroughoutStep = 1
    SimMassScalingResetMassMatrix = 2


class SimMassScalingMassScalingMethod(IntEnum):
    SimMassScalingUniform = 0
    SimMassScalingBelowMin = 1
    SimMassScalingSameTimeIncrement = 2


class SimMatrixStorageScheme(IntEnum):
    SimMatrixStorage_Default = 0
    SimMatrixStorage_Symmetric = 1
    SimMatrixStorage_Unsymmetric = 2


class SimModalDampingDampingType(IntEnum):
    SimModalDampingFraction = 0
    SimModalDampingRayleigh = 1
    SimModalDampingStructural = 2


class SimModalDampingTableColumn(IntEnum):
    SimModalDampingFrequency = 0
    SimModalDampingDampingFraction = 1
    SimModalDampingAlpha = 2
    SimModalDampingBeta = 3
    SimModalDampingDampingFactor = 4


class SimModeBasedDampingDampingType(IntEnum):
    SimModeBasedDampingCriticalDampingFraction = 0
    SimModeBasedDampingStructural = 1
    SimModeBasedDampingComposite = 2
    SimModeBasedDampingRayleigh = 3


class SimModeBasedDampingTableColumn(IntEnum):
    SimModeBasedDampingFirstMode = 0
    SimModeBasedDampingLastMode = 1
    SimModeBasedDampingDampingFraction = 2
    SimModeBasedDampingDampingFactor = 3
    SimModeBasedDampingMassScaling = 4
    SimModeBasedDampingStiffnessScaling = 5
    SimModeBasedDampingMassDamping = 6
    SimModeBasedDampingStiffnessDamping = 7


class SimNormalBehaviorTableColumn(IntEnum):
    SimNormalBehaviorPressure = 0
    SimNormalBehaviorOverclosure = 1


class SimOutputElementLocation(IntEnum):
    SimOutputAtIntegrationPoints = 0
    SimOutputAtNodes = 1
    SimOutputAtCentroid = 2
    SimOutputAtNodesAveraged = 3


class SimOutputFrequencyType(IntEnum):
    SimOutputFrequency = 0
    SimOutputNumberInterval = 1
    SimOutputTimeInterval = 2


class SimOutputOutputGroup(IntEnum):
    SimOutputField = 0
    SimOutputHistory = 1


class SimOutputSectionPointSelectionType(IntEnum):
    SimOutputDefault = 0
    SimOutputSpecify = 1
    SimOutputAll = 2
    SimOutputByLayer = 3


class SimPeriodicAmplitudeColumnType(IntEnum):
    SimPeriodicAmplitudeASeriesColumn = 0
    SimPeriodicAmplitudeBSeriesColumn = 1


class SimRandomGlobalDampingModesType(IntEnum):
    SimRandomGlobalDampingStructuralAndAcoustic = 0
    SimRandomGlobalDampingStructural = 1
    SimRandomGlobalDampingAcoustic = 2


class SimRandomVibrationStepDampingDefinition(IntEnum):
    SimRandomVibrationStepModeRange = 0
    SimRandomVibrationStepFrequencyCurve = 1
    SimRandomVibrationStepGlobal = 2
    SimRandomVibrationStepNoDamping = 3


class SimRandomVibrationStepTableColumn(IntEnum):
    SimRandomVibrationStepLowerBoundary = 0
    SimRandomVibrationStepUpperBoundary = 1
    SimRandomVibrationStepCalculationPoints = 2
    SimRandomVibrationStepBias = 3
    SimRandomVibrationStepFrequencyScale = 4


class SimResponseSpectrumStepAlignAxisType(IntEnum):
    SimResponseSpectrumStepXAxis = 0
    SimResponseSpectrumStepYAxis = 1
    SimResponseSpectrumStepZAxis = 2


class SimResponseSpectrumStepDampingDefinition(IntEnum):
    SimResponseSpectrumStepModeRange = 0
    SimResponseSpectrumStepFrequencyCurve = 1
    SimResponseSpectrumStepGlobal = 2
    SimResponseSpectrumStepNoDamping = 3


class SimResponseSpectrumStepDirectionalSummationMethod(IntEnum):
    SimResponseSpectrumStepAlgebraic = 0
    SimResponseSpectrumStepSquareRootOfSumOfSquares = 1
    SimResponseSpectrumStepFortyPercentRule = 2
    SimResponseSpectrumStepThirtyPercentRule = 3


class SimResponseSpectrumStepDirectionType(IntEnum):
    SimResponseSpectrumStepFirst = 0
    SimResponseSpectrumStepSecond = 1
    SimResponseSpectrumStepThird = 2


class SimResponseSpectrumStepModalSummationMethod(IntEnum):
    SimResponseSpectrumStepAbsoluteValues = 0
    SimResponseSpectrumStepSquareRootOfSumOfSquaresMethod = 1
    SimResponseSpectrumStepNavalResearchLaboratory = 2
    SimResponseSpectrumStepTenPercentMethod = 3
    SimResponseSpectrumStepCompleteQuadraticCombination = 4
    SimResponseSpectrumStepGroupingMethod = 5
    SimResponseSpectrumStepDoubleSumCombination = 6


class SimResponseSpectrumStepRigidResponseMethod(IntEnum):
    SimResponseSpectrumStepNone = 0
    SimResponseSpectrumStepGupta = 1
    SimResponseSpectrumStepLindleyYow = 2


class SimShellEdgeLoadTractionType(IntEnum):
    SimShellEdgeLoadNormal = 0
    SimShellEdgeLoadTransverse = 1
    SimShellEdgeLoadShear = 2


class SimSlidingVelocityTranslationalDof(IntEnum):
    SimSlidingVelocityTranslationX = 0
    SimSlidingVelocityTranslationY = 1
    SimSlidingVelocityTranslationZ = 2


class SimSlidingVelocityType(IntEnum):
    SimSlidingVelocityTranslation = 0
    SimSlidingVelocityRotation = 1


class SimSmoothStepAmplitudeDomainType(IntEnum):
    SimSmoothStepAmplitudeTimeDomain = 0
    SimSmoothStepAmplitudeFrequencyDomain = 1


class SimSmoothStepAmplitudeTableColumn(IntEnum):
    SimSmoothStepAmplitudeAmplitude = 0
    SimSmoothStepAmplitudeTime = 1


class SimSolutionControlsAverageFlux(IntEnum):
    SimSolutionControlsDefault = 0
    SimSolutionControlsInitial = 1
    SimSolutionControlsAverage = 2


class SimSolutionControlsDefinition(IntEnum):
    SimSolutionControlsPropagate = 0
    SimSolutionControlsReset = 1
    SimSolutionControlsSpecify = 2


class SimSolutionControlsDOFField(IntEnum):
    SimSolutionControlsDisplacement = 0
    SimSolutionControlsRotation = 1
    SimSolutionControlsTemperature = 2
    SimSolutionControlsPorePressure = 3
    SimSolutionControlsElectricPotential = 4
    SimSolutionControlsElectricPotentialPiezo = 5
    SimSolutionControlsFluidElectricPotential = 6
    SimSolutionControlsHydrostaticFluidPressure = 7
    SimSolutionControlsPressureLagrangeMultiplier = 8
    SimSolutionControlsVolumeLagrangeMultiplier = 9
    SimSolutionControlsIonConcentration = 10


class SimSpectrumDefinitionType(IntEnum):
    SimSpectrumAcceleration = 0
    SimSpectrumDisplacement = 1
    SimSpectrumGravity = 2
    SimSpectrumVelocity = 3


class SimSpectrumTableColumn(IntEnum):
    SimSpectrumAccelerationCol = 0
    SimSpectrumDampingRatioCol = 1
    SimSpectrumFrequencyCol = 2
    SimSpectrumDisplacementCol = 3
    SimSpectrumGravityCol = 4
    SimSpectrumVelocityCol = 5


class SimStabilizationStabilizationType(IntEnum):
    SimStabilizationNoStabilization = 0
    SimStabilizationDamping = 1
    SimStabilizationEnergyFraction = 2
    SimStabilizationPropagated = 3


class SimStaticPerturbationStepSolutionTechnique(IntEnum):
    SimStaticPerturbationStepFullNewton = 0
    SimStaticPerturbationStepLCP = 1


class SimStaticRiksStepDisplacementType(IntEnum):
    SimStaticRiksStepDisplacementNone = 0
    SimStaticRiksStepDisplacementTranslation = 1
    SimStaticRiksStepDisplacementRotation = 2


class SimSteadyStateTransportStepInertiaEffect(IntEnum):
    SimSteadyStateTransportStepNoInertia = 0
    SimSteadyStateTransportStepHighSpeedInertia = 1
    SimSteadyStateTransportStepLowSpeedInertia = 2


class SimSteadyStateTransportStepMullinsEffect(IntEnum):
    SimSteadyStateTransportStepRampMullins = 0
    SimSteadyStateTransportStepImmediateMullins = 1


class SimSurfaceBasedContactDiscretizationMethod(IntEnum):
    SimSurfaceBasedContactNodeToSurface = 0
    SimSurfaceBasedContactSurfaceToSurface = 1


class SimTabularAmplitudeDomainType(IntEnum):
    SimTabularAmplitudeTimeDomain = 0
    SimTabularAmplitudeFrequencyDomain = 1


class SimTabularAmplitudeTableColumn(IntEnum):
    SimTabularAmplitudeAmplitude = 0
    SimTabularAmplitudeTime = 1


class SimTimeIncrementationScheme(IntEnum):
    SimTimeIncrementation_Automatic = 0
    SimTimeIncrementation_Fixed = 1
    SimTimeIncrementation_Direct = 2
    SimTimeIncrementation_SolverDefault = 3


class SimVolumetricHeatSourceHeatSourceType(IntEnum):
    SimVolumetricHeatSourcePerUnitVolume = 0
    SimVolumetricHeatSourceTotal = 1
