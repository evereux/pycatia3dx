from enum import Enum


class SimAcousticCouplingFormulationType(Enum):
    SimAcousticCouplingSurfaceToSurface = 0
    SimAcousticCouplingNodeToSurface = 1


class SimAcousticCouplingMainSurfaceType(Enum):
    SimAcousticCouplingNodeBasedMainSurface = 0
    SimAcousticCouplingElementBasedMainSurface = 1


class SimAcousticCouplingMasterSurfaceType(Enum):
    SimAcousticCouplingNodeBased = 0
    SimAcousticCouplingElementBased = 1


class SimAmplitudeDefinitionType(Enum):
    SimAmplitudeUserDefinition = 0
    SimAmplitudeTabularDefinition = 1
    SimAmplitudeSmoothStepDefinition = 2
    SimAmplitudePeriodicDefinition = 3


class SimAmplitudeTimeSpanType(Enum):
    SimAmplitudeStepTime = 0
    SimAmplitudeTotalTime = 1


class SimAMSEigensolverAcousticCouplingType(Enum):
    SimAMSEigensolverOn = 0
    SimAMSEigensolverOff = 1
    SimAMSEigensolverProjection = 2


class SimApplicationType(Enum):
    SimApplicationType_Solver_Default = 0
    SimApplicationType_Transient_Fidelity = 1
    SimApplicationType_Quasi_Static = 2
    SimApplicationType_Moderate_Dissipation = 3


class SimBeamLoadComponentSystem(Enum):
    SimBeamLoadLocalComponentSystem = 0
    SimBeamLoadGlobalComponentSystem = 1


class SimBearingLoadInteractionType(Enum):
    SimBearingLoadOutward = 0
    SimBearingLoadInward = 1


class SimBearingLoadOrientationType(Enum):
    SimBearingLoadParallel = 0
    SimBearingLoadRadial = 1


class SimBearingLoadProfileType(Enum):
    SimBearingLoadSinusoidal = 0
    SimBearingLoadParabolic = 1


class SimBuckleStepSolverType(Enum):
    SimBuckleStepSUBSPACE = 0
    SimBuckleStepLANCZOS = 1


class SimConnectorDampingDampingOrder(Enum):
    SimConnectorDampingLinear = 0
    SimConnectorDampingNonLinear = 1


class SimConnectorDampingTableColumn(Enum):
    SimConnectorDampingTemperature = 0
    SimConnectorDampingVelocity = 1
    SimConnectorDampingCoefficient = 2


class SimConnectorRotationVariationType(Enum):
    SimConnectorRotationUniform = 0
    SimConnectorRotationUserDefined = 1


class SimConnectorRotationVelocityVariationType(Enum):
    SimConnectorRotationVelocityUniform = 0
    SimConnectorRotationVelocityUserDefined = 1


class SimConnectorTranslationVariationType(Enum):
    SimConnectorTranslationUserDefined = 0
    SimConnectorTranslationUniform = 1


class SimConnectorTranslationVelocityVariationType(Enum):
    SimConnectorTranslationVelocityUserDefined = 0
    SimConnectorTranslationVelocityUniform = 1


class SimCoupledCreepIntegration(Enum):
    SimCoupledImplicit = 0
    SimCoupledExplicit = 1


class SimCoupledSolutionTechnique(Enum):
    SimCoupledSeparated = 0
    SimCoupledFullNewton = 1


class SimCoupledThermalResponseType(Enum):
    SimCoupledThermalSteadyState = 0
    SimCoupledThermalTransient = 1


class SimDirectHarmonicResponseStepIntervalType(Enum):
    SimDirectHarmonicResponseStepFrequencySpread = 0
    SimDirectHarmonicResponseStepEigenFrequency = 1
    SimDirectHarmonicResponseStepDirectRange = 2
    SimDirectHarmonicResponseStepFrequencyIncrement = 3


class SimDirectHarmonicResponseStepScaleType(Enum):
    SimDirectHarmonicResponseStepLogarithmic = 0
    SimDirectHarmonicResponseStepLinear = 1


class SimDirectHarmonicResponseStepTableColumn(Enum):
    SimDirectHarmonicResponseStepUpper = 0
    SimDirectHarmonicResponseStepBias = 1
    SimDirectHarmonicResponseStepNumberOfPoints = 2
    SimDirectHarmonicResponseStepScaleFactor = 3
    SimDirectHarmonicResponseStepSpread = 4
    SimDirectHarmonicResponseStepLower = 5
    SimDirectHarmonicResponseStepIncrement = 6


class SimExplicitDynamicStepFixedIncrementationTypeEnm(Enum):
    SimExplicitDynamicStepUSERDEFINED = 0
    SimExplicitDynamicStepELEMENTBYELEMENT = 1


class SimFrequencyBasedDampingDampingType(Enum):
    SimFrequencyBasedDampingStructuralDamping = 0
    SimFrequencyBasedDampingCriticalDampingFraction = 1
    SimFrequencyBasedDampingRayleighDamping = 2


class SimFrequencyBasedDampingModesType(Enum):
    SimFrequencyBasedDampingStructuralAndAcoustic = 0
    SimFrequencyBasedDampingStructural = 1
    SimFrequencyBasedDampingAcoustic = 2


class SimFrequencyBasedDampingTableColumn(Enum):
    SimFrequencyBasedDampingDampingFraction = 0
    SimFrequencyBasedDampingMassDamping = 1
    SimFrequencyBasedDampingDampingFactor = 2
    SimFrequencyBasedDampingFrequency = 3
    SimFrequencyBasedDampingStiffnessDamping = 4


class SimFrequencyStepSolverType(Enum):
    SimFrequencyStepLanczos = 0
    SimFrequencyStepAMS = 1


class SimGeneralGlobalDampingModesType(Enum):
    SimGeneralGlobalDampingStructural = 0
    SimGeneralGlobalDampingStructuralAndAcoustic = 1
    SimGeneralGlobalDampingAcoustic = 2
    SimGeneralGlobalDampingNone = 3


class SimHarmonicResponseStepIntervalType(Enum):
    SimHarmonicResponseStepEigenfrequency = 0
    SimHarmonicResponseStepDirectRange = 1
    SimHarmonicResponseStepFrequencySpread = 2
    SimHarmonicResponseStepFrequencyIncrement = 3


class SimHarmonicResponseStepProjectionType(Enum):
    SimHarmonicResponseStepRangeValues = 0
    SimHarmonicResponseStepAllFrequency = 1
    SimHarmonicResponseStepNone = 2
    SimHarmonicResponseStepCenterFrequencies = 3


class SimHarmonicResponseStepScaleType(Enum):
    SimHarmonicResponseStepLogarithmic = 0
    SimHarmonicResponseStepLinear = 1


class SimHarmonicResponseStepTableColumn(Enum):
    SimHarmonicResponseStepNumberOfPoints = 0
    SimHarmonicResponseStepLower = 1
    SimHarmonicResponseStepIncrement = 2
    SimHarmonicResponseStepScaleFactor = 3
    SimHarmonicResponseStepBias = 4
    SimHarmonicResponseStepSpread = 5
    SimHarmonicResponseStepUpper = 6


class SimInitialStressType(Enum):
    SimInitialStressTensorStress = 0
    SimInitialStressRebarStress = 1


class SimLanczosEigensolverAcousticCouplingType(Enum):
    SimLanczosEigensolverOn = 0
    SimLanczosEigensolverOff = 1
    SimLanczosEigensolverProjection = 2


class SimMassScalingMassScalingBehavior(Enum):
    SimMassScalingBeginningOfStep = 0
    SimMassScalingThroughoutStep = 1
    SimMassScalingResetMassMatrix = 2


class SimMassScalingMassScalingMethod(Enum):
    SimMassScalingUniform = 0
    SimMassScalingSameTimeIncrement = 1
    SimMassScalingBelowMin = 2


class SimMatrixStorageScheme(Enum):
    SimMatrixStorage_Unsymmetric = 0
    SimMatrixStorage_Symmetric = 1
    SimMatrixStorage_Default = 2


class SimModalDampingDampingType(Enum):
    SimModalDampingRayleigh = 0
    SimModalDampingStructural = 1
    SimModalDampingFraction = 2


class SimModalDampingTableColumn(Enum):
    SimModalDampingAlpha = 0
    SimModalDampingFrequency = 1
    SimModalDampingDampingFraction = 2
    SimModalDampingDampingFactor = 3
    SimModalDampingBeta = 4


class SimModeBasedDampingDampingType(Enum):
    SimModeBasedDampingCriticalDampingFraction = 0
    SimModeBasedDampingRayleigh = 1
    SimModeBasedDampingComposite = 2
    SimModeBasedDampingStructural = 3


class SimModeBasedDampingTableColumn(Enum):
    SimModeBasedDampingStiffnessScaling = 0
    SimModeBasedDampingStiffnessDamping = 1
    SimModeBasedDampingMassScaling = 2
    SimModeBasedDampingMassDamping = 3
    SimModeBasedDampingLastMode = 4
    SimModeBasedDampingDampingFactor = 5
    SimModeBasedDampingDampingFraction = 6
    SimModeBasedDampingFirstMode = 7


class SimNormalBehaviorTableColumn(Enum):
    SimNormalBehaviorOverclosure = 0
    SimNormalBehaviorPressure = 1


class SimOutputElementLocation(Enum):
    SimOutputAtIntegrationPoints = 0
    SimOutputAtNodes = 1
    SimOutputAtCentroid = 2
    SimOutputAtNodesAveraged = 3


class SimOutputFrequencyType(Enum):
    SimOutputNumberInterval = 0
    SimOutputTimeInterval = 1
    SimOutputFrequency = 2


class SimOutputOutputGroup(Enum):
    SimOutputHistory = 0
    SimOutputField = 1


class SimOutputSectionPointSelectionType(Enum):
    SimOutputSpecify = 0
    SimOutputByLayer = 1
    SimOutputDefault = 2
    SimOutputAll = 3


class SimPeriodicAmplitudeColumnType(Enum):
    SimPeriodicAmplitudeASeriesColumn = 0
    SimPeriodicAmplitudeBSeriesColumn = 1


class SimRandomGlobalDampingModesType(Enum):
    SimRandomGlobalDampingAcoustic = 0
    SimRandomGlobalDampingStructural = 1
    SimRandomGlobalDampingStructuralAndAcoustic = 2


class SimRandomVibrationStepDampingDefinition(Enum):
    SimRandomVibrationStepGlobal = 0
    SimRandomVibrationStepModeRange = 1
    SimRandomVibrationStepNoDamping = 2
    SimRandomVibrationStepFrequencyCurve = 3


class SimRandomVibrationStepTableColumn(Enum):
    SimRandomVibrationStepFrequencyScale = 0
    SimRandomVibrationStepCalculationPoints = 1
    SimRandomVibrationStepUpperBoundary = 2
    SimRandomVibrationStepLowerBoundary = 3
    SimRandomVibrationStepBias = 4


class SimResponseSpectrumStepAlignAxisType(Enum):
    SimResponseSpectrumStepZAxis = 0
    SimResponseSpectrumStepXAxis = 1
    SimResponseSpectrumStepYAxis = 2


class SimResponseSpectrumStepDampingDefinition(Enum):
    SimResponseSpectrumStepModeRange = 0
    SimResponseSpectrumStepNoDamping = 1
    SimResponseSpectrumStepGlobal = 2
    SimResponseSpectrumStepFrequencyCurve = 3


class SimResponseSpectrumStepDirectionalSummationMethod(Enum):
    SimResponseSpectrumStepSquareRootOfSumOfSquares = 0
    SimResponseSpectrumStepThirtyPercentRule = 1
    SimResponseSpectrumStepFortyPercentRule = 2
    SimResponseSpectrumStepAlgebraic = 3


class SimResponseSpectrumStepDirectionType(Enum):
    SimResponseSpectrumStepThird = 0
    SimResponseSpectrumStepFirst = 1
    SimResponseSpectrumStepSecond = 2


class SimResponseSpectrumStepModalSummationMethod(Enum):
    SimResponseSpectrumStepSquareRootOfSumOfSquaresMethod = 0
    SimResponseSpectrumStepGroupingMethod = 1
    SimResponseSpectrumStepNavalResearchLaboratory = 2
    SimResponseSpectrumStepAbsoluteValues = 3
    SimResponseSpectrumStepDoubleSumCombination = 4
    SimResponseSpectrumStepCompleteQuadraticCombination = 5
    SimResponseSpectrumStepTenPercentMethod = 6


class SimResponseSpectrumStepRigidResponseMethod(Enum):
    SimResponseSpectrumStepLindleyYow = 0
    SimResponseSpectrumStepNone = 1
    SimResponseSpectrumStepGupta = 2


class SimShellEdgeLoadTractionType(Enum):
    SimShellEdgeLoadShear = 0
    SimShellEdgeLoadTransverse = 1
    SimShellEdgeLoadNormal = 2


class SimSlidingVelocityTranslationalDof(Enum):
    SimSlidingVelocityTranslationZ = 0
    SimSlidingVelocityTranslationY = 1
    SimSlidingVelocityTranslationX = 2


class SimSlidingVelocityType(Enum):
    SimSlidingVelocityRotation = 0
    SimSlidingVelocityTranslation = 1


class SimSmoothStepAmplitudeDomainType(Enum):
    SimSmoothStepAmplitudeTimeDomain = 0
    SimSmoothStepAmplitudeFrequencyDomain = 1


class SimSmoothStepAmplitudeTableColumn(Enum):
    SimSmoothStepAmplitudeAmplitude = 0
    SimSmoothStepAmplitudeTime = 1


class SimSolutionControlsAverageFlux(Enum):
    SimSolutionControlsAverage = 0
    SimSolutionControlsInitial = 1
    SimSolutionControlsDefault = 2


class SimSolutionControlsDefinition(Enum):
    SimSolutionControlsSpecify = 0
    SimSolutionControlsReset = 1
    SimSolutionControlsPropagate = 2


class SimSolutionControlsDOFField(Enum):
    SimSolutionControlsFluidElectricPotential = 0
    SimSolutionControlsPressureLagrangeMultiplier = 1
    SimSolutionControlsPorePressure = 2
    SimSolutionControlsElectricPotential = 3
    SimSolutionControlsTemperature = 4
    SimSolutionControlsHydrostaticFluidPressure = 5
    SimSolutionControlsElectricPotentialPiezo = 6
    SimSolutionControlsVolumeLagrangeMultiplier = 7
    SimSolutionControlsIonConcentration = 8
    SimSolutionControlsRotation = 9
    SimSolutionControlsDisplacement = 10


class SimSpectrumDefinitionType(Enum):
    SimSpectrumDisplacement = 0
    SimSpectrumVelocity = 1
    SimSpectrumAcceleration = 2
    SimSpectrumGravity = 3


class SimSpectrumTableColumn(Enum):
    SimSpectrumFrequencyCol = 0
    SimSpectrumDisplacementCol = 1
    SimSpectrumDampingRatioCol = 2
    SimSpectrumAccelerationCol = 3
    SimSpectrumVelocityCol = 4
    SimSpectrumGravityCol = 5


class SimStabilizationStabilizationType(Enum):
    SimStabilizationPropagated = 0
    SimStabilizationNoStabilization = 1
    SimStabilizationEnergyFraction = 2
    SimStabilizationDamping = 3


class SimStaticPerturbationStepSolutionTechnique(Enum):
    SimStaticPerturbationStepFullNewton = 0
    SimStaticPerturbationStepLCP = 1


class SimStaticRiksStepDisplacementType(Enum):
    SimStaticRiksStepDisplacementRotation = 0
    SimStaticRiksStepDisplacementNone = 1
    SimStaticRiksStepDisplacementTranslation = 2


class SimSteadyStateTransportStepInertiaEffect(Enum):
    SimSteadyStateTransportStepHighSpeedInertia = 0
    SimSteadyStateTransportStepLowSpeedInertia = 1
    SimSteadyStateTransportStepNoInertia = 2


class SimSteadyStateTransportStepMullinsEffect(Enum):
    SimSteadyStateTransportStepRampMullins = 0
    SimSteadyStateTransportStepImmediateMullins = 1


class SimSurfaceBasedContactDiscretizationMethod(Enum):
    SimSurfaceBasedContactSurfaceToSurface = 0
    SimSurfaceBasedContactNodeToSurface = 1


class SimTabularAmplitudeDomainType(Enum):
    SimTabularAmplitudeTimeDomain = 0
    SimTabularAmplitudeFrequencyDomain = 1


class SimTabularAmplitudeTableColumn(Enum):
    SimTabularAmplitudeAmplitude = 0
    SimTabularAmplitudeTime = 1


class SimTimeIncrementationScheme(Enum):
    SimTimeIncrementation_Fixed = 0
    SimTimeIncrementation_Automatic = 1
    SimTimeIncrementation_SolverDefault = 2
    SimTimeIncrementation_Direct = 3


class SimVolumetricHeatSourceHeatSourceType(Enum):
    SimVolumetricHeatSourceTotal = 0
    SimVolumetricHeatSourcePerUnitVolume = 1


