from enum import Enum


class SimAcousticCouplingFormulationType(Enum):
    SimAcousticCouplingNodeToSurface = 0
    SimAcousticCouplingSurfaceToSurface = 1


class SimAcousticCouplingMainSurfaceType(Enum):
    SimAcousticCouplingElementBasedMainSurface = 0
    SimAcousticCouplingNodeBasedMainSurface = 1


class SimAcousticCouplingMasterSurfaceType(Enum):
    SimAcousticCouplingElementBased = 0
    SimAcousticCouplingNodeBased = 1


class SimAmplitudeDefinitionType(Enum):
    SimAmplitudeTabularDefinition = 0
    SimAmplitudeSmoothStepDefinition = 1
    SimAmplitudePeriodicDefinition = 2
    SimAmplitudeUserDefinition = 3


class SimAmplitudeTimeSpanType(Enum):
    SimAmplitudeStepTime = 0
    SimAmplitudeTotalTime = 1


class SimAMSEigensolverAcousticCouplingType(Enum):
    SimAMSEigensolverOn = 0
    SimAMSEigensolverProjection = 1
    SimAMSEigensolverOff = 2


class SimApplicationType(Enum):
    SimApplicationType_Solver_Default = 0
    SimApplicationType_Transient_Fidelity = 1
    SimApplicationType_Moderate_Dissipation = 2
    SimApplicationType_Quasi_Static = 3


class SimBeamLoadComponentSystem(Enum):
    SimBeamLoadGlobalComponentSystem = 0
    SimBeamLoadLocalComponentSystem = 1


class SimBearingLoadInteractionType(Enum):
    SimBearingLoadOutward = 0
    SimBearingLoadInward = 1


class SimBearingLoadOrientationType(Enum):
    SimBearingLoadRadial = 0
    SimBearingLoadParallel = 1


class SimBearingLoadProfileType(Enum):
    SimBearingLoadSinusoidal = 0
    SimBearingLoadParabolic = 1


class SimBuckleStepSolverType(Enum):
    SimBuckleStepLANCZOS = 0
    SimBuckleStepSUBSPACE = 1


class SimConnectorDampingDampingOrder(Enum):
    SimConnectorDampingLinear = 0
    SimConnectorDampingNonLinear = 1


class SimConnectorDampingTableColumn(Enum):
    SimConnectorDampingCoefficient = 0
    SimConnectorDampingTemperature = 1
    SimConnectorDampingVelocity = 2


class SimConnectorRotationVariationType(Enum):
    SimConnectorRotationUniform = 0
    SimConnectorRotationUserDefined = 1


class SimConnectorRotationVelocityVariationType(Enum):
    SimConnectorRotationVelocityUniform = 0
    SimConnectorRotationVelocityUserDefined = 1


class SimConnectorTranslationVariationType(Enum):
    SimConnectorTranslationUniform = 0
    SimConnectorTranslationUserDefined = 1


class SimConnectorTranslationVelocityVariationType(Enum):
    SimConnectorTranslationVelocityUniform = 0
    SimConnectorTranslationVelocityUserDefined = 1


class SimCoupledCreepIntegration(Enum):
    SimCoupledImplicit = 0
    SimCoupledExplicit = 1


class SimCoupledSolutionTechnique(Enum):
    SimCoupledFullNewton = 0
    SimCoupledSeparated = 1


class SimCoupledThermalResponseType(Enum):
    SimCoupledThermalSteadyState = 0
    SimCoupledThermalTransient = 1


class SimDirectHarmonicResponseStepIntervalType(Enum):
    SimDirectHarmonicResponseStepFrequencyIncrement = 0
    SimDirectHarmonicResponseStepEigenFrequency = 1
    SimDirectHarmonicResponseStepDirectRange = 2
    SimDirectHarmonicResponseStepFrequencySpread = 3


class SimDirectHarmonicResponseStepScaleType(Enum):
    SimDirectHarmonicResponseStepLogarithmic = 0
    SimDirectHarmonicResponseStepLinear = 1


class SimDirectHarmonicResponseStepTableColumn(Enum):
    SimDirectHarmonicResponseStepLower = 0
    SimDirectHarmonicResponseStepUpper = 1
    SimDirectHarmonicResponseStepIncrement = 2
    SimDirectHarmonicResponseStepNumberOfPoints = 3
    SimDirectHarmonicResponseStepBias = 4
    SimDirectHarmonicResponseStepScaleFactor = 5
    SimDirectHarmonicResponseStepSpread = 6


class SimExplicitDynamicStepFixedIncrementationTypeEnm(Enum):
    SimExplicitDynamicStepELEMENTBYELEMENT = 0
    SimExplicitDynamicStepUSERDEFINED = 1


class SimFrequencyBasedDampingDampingType(Enum):
    SimFrequencyBasedDampingCriticalDampingFraction = 0
    SimFrequencyBasedDampingStructuralDamping = 1
    SimFrequencyBasedDampingRayleighDamping = 2


class SimFrequencyBasedDampingModesType(Enum):
    SimFrequencyBasedDampingStructuralAndAcoustic = 0
    SimFrequencyBasedDampingStructural = 1
    SimFrequencyBasedDampingAcoustic = 2


class SimFrequencyBasedDampingTableColumn(Enum):
    SimFrequencyBasedDampingFrequency = 0
    SimFrequencyBasedDampingDampingFraction = 1
    SimFrequencyBasedDampingDampingFactor = 2
    SimFrequencyBasedDampingMassDamping = 3
    SimFrequencyBasedDampingStiffnessDamping = 4


class SimFrequencyStepSolverType(Enum):
    SimFrequencyStepLanczos = 0
    SimFrequencyStepAMS = 1


class SimGeneralGlobalDampingModesType(Enum):
    SimGeneralGlobalDampingNone = 0
    SimGeneralGlobalDampingStructuralAndAcoustic = 1
    SimGeneralGlobalDampingStructural = 2
    SimGeneralGlobalDampingAcoustic = 3


class SimHarmonicResponseStepIntervalType(Enum):
    SimHarmonicResponseStepFrequencyIncrement = 0
    SimHarmonicResponseStepEigenfrequency = 1
    SimHarmonicResponseStepDirectRange = 2
    SimHarmonicResponseStepFrequencySpread = 3


class SimHarmonicResponseStepProjectionType(Enum):
    SimHarmonicResponseStepNone = 0
    SimHarmonicResponseStepAllFrequency = 1
    SimHarmonicResponseStepCenterFrequencies = 2
    SimHarmonicResponseStepRangeValues = 3


class SimHarmonicResponseStepScaleType(Enum):
    SimHarmonicResponseStepLogarithmic = 0
    SimHarmonicResponseStepLinear = 1


class SimHarmonicResponseStepTableColumn(Enum):
    SimHarmonicResponseStepLower = 0
    SimHarmonicResponseStepUpper = 1
    SimHarmonicResponseStepIncrement = 2
    SimHarmonicResponseStepNumberOfPoints = 3
    SimHarmonicResponseStepBias = 4
    SimHarmonicResponseStepScaleFactor = 5
    SimHarmonicResponseStepSpread = 6


class SimInitialStressType(Enum):
    SimInitialStressTensorStress = 0
    SimInitialStressRebarStress = 1


class SimLanczosEigensolverAcousticCouplingType(Enum):
    SimLanczosEigensolverOn = 0
    SimLanczosEigensolverProjection = 1
    SimLanczosEigensolverOff = 2


class SimMassScalingMassScalingBehavior(Enum):
    SimMassScalingBeginningOfStep = 0
    SimMassScalingThroughoutStep = 1
    SimMassScalingResetMassMatrix = 2


class SimMassScalingMassScalingMethod(Enum):
    SimMassScalingUniform = 0
    SimMassScalingBelowMin = 1
    SimMassScalingSameTimeIncrement = 2


class SimMatrixStorageScheme(Enum):
    SimMatrixStorage_Default = 0
    SimMatrixStorage_Symmetric = 1
    SimMatrixStorage_Unsymmetric = 2


class SimModalDampingDampingType(Enum):
    SimModalDampingFraction = 0
    SimModalDampingRayleigh = 1
    SimModalDampingStructural = 2


class SimModalDampingTableColumn(Enum):
    SimModalDampingFrequency = 0
    SimModalDampingDampingFraction = 1
    SimModalDampingAlpha = 2
    SimModalDampingBeta = 3
    SimModalDampingDampingFactor = 4


class SimModeBasedDampingDampingType(Enum):
    SimModeBasedDampingCriticalDampingFraction = 0
    SimModeBasedDampingStructural = 1
    SimModeBasedDampingComposite = 2
    SimModeBasedDampingRayleigh = 3


class SimModeBasedDampingTableColumn(Enum):
    SimModeBasedDampingFirstMode = 0
    SimModeBasedDampingLastMode = 1
    SimModeBasedDampingDampingFraction = 2
    SimModeBasedDampingDampingFactor = 3
    SimModeBasedDampingMassScaling = 4
    SimModeBasedDampingStiffnessScaling = 5
    SimModeBasedDampingMassDamping = 6
    SimModeBasedDampingStiffnessDamping = 7


class SimNormalBehaviorTableColumn(Enum):
    SimNormalBehaviorPressure = 0
    SimNormalBehaviorOverclosure = 1


class SimOutputElementLocation(Enum):
    SimOutputAtIntegrationPoints = 0
    SimOutputAtNodes = 1
    SimOutputAtCentroid = 2
    SimOutputAtNodesAveraged = 3


class SimOutputFrequencyType(Enum):
    SimOutputFrequency = 0
    SimOutputNumberInterval = 1
    SimOutputTimeInterval = 2


class SimOutputOutputGroup(Enum):
    SimOutputField = 0
    SimOutputHistory = 1


class SimOutputSectionPointSelectionType(Enum):
    SimOutputDefault = 0
    SimOutputSpecify = 1
    SimOutputAll = 2
    SimOutputByLayer = 3


class SimPeriodicAmplitudeColumnType(Enum):
    SimPeriodicAmplitudeASeriesColumn = 0
    SimPeriodicAmplitudeBSeriesColumn = 1


class SimRandomGlobalDampingModesType(Enum):
    SimRandomGlobalDampingStructuralAndAcoustic = 0
    SimRandomGlobalDampingStructural = 1
    SimRandomGlobalDampingAcoustic = 2


class SimRandomVibrationStepDampingDefinition(Enum):
    SimRandomVibrationStepModeRange = 0
    SimRandomVibrationStepFrequencyCurve = 1
    SimRandomVibrationStepGlobal = 2
    SimRandomVibrationStepNoDamping = 3


class SimRandomVibrationStepTableColumn(Enum):
    SimRandomVibrationStepLowerBoundary = 0
    SimRandomVibrationStepUpperBoundary = 1
    SimRandomVibrationStepCalculationPoints = 2
    SimRandomVibrationStepBias = 3
    SimRandomVibrationStepFrequencyScale = 4


class SimResponseSpectrumStepAlignAxisType(Enum):
    SimResponseSpectrumStepXAxis = 0
    SimResponseSpectrumStepYAxis = 1
    SimResponseSpectrumStepZAxis = 2


class SimResponseSpectrumStepDampingDefinition(Enum):
    SimResponseSpectrumStepModeRange = 0
    SimResponseSpectrumStepFrequencyCurve = 1
    SimResponseSpectrumStepGlobal = 2
    SimResponseSpectrumStepNoDamping = 3


class SimResponseSpectrumStepDirectionalSummationMethod(Enum):
    SimResponseSpectrumStepAlgebraic = 0
    SimResponseSpectrumStepSquareRootOfSumOfSquares = 1
    SimResponseSpectrumStepFortyPercentRule = 2
    SimResponseSpectrumStepThirtyPercentRule = 3


class SimResponseSpectrumStepDirectionType(Enum):
    SimResponseSpectrumStepFirst = 0
    SimResponseSpectrumStepSecond = 1
    SimResponseSpectrumStepThird = 2


class SimResponseSpectrumStepModalSummationMethod(Enum):
    SimResponseSpectrumStepAbsoluteValues = 0
    SimResponseSpectrumStepSquareRootOfSumOfSquaresMethod = 1
    SimResponseSpectrumStepNavalResearchLaboratory = 2
    SimResponseSpectrumStepTenPercentMethod = 3
    SimResponseSpectrumStepCompleteQuadraticCombination = 4
    SimResponseSpectrumStepGroupingMethod = 5
    SimResponseSpectrumStepDoubleSumCombination = 6


class SimResponseSpectrumStepRigidResponseMethod(Enum):
    SimResponseSpectrumStepNone = 0
    SimResponseSpectrumStepGupta = 1
    SimResponseSpectrumStepLindleyYow = 2


class SimShellEdgeLoadTractionType(Enum):
    SimShellEdgeLoadNormal = 0
    SimShellEdgeLoadTransverse = 1
    SimShellEdgeLoadShear = 2


class SimSlidingVelocityTranslationalDof(Enum):
    SimSlidingVelocityTranslationX = 0
    SimSlidingVelocityTranslationY = 1
    SimSlidingVelocityTranslationZ = 2


class SimSlidingVelocityType(Enum):
    SimSlidingVelocityTranslation = 0
    SimSlidingVelocityRotation = 1


class SimSmoothStepAmplitudeDomainType(Enum):
    SimSmoothStepAmplitudeTimeDomain = 0
    SimSmoothStepAmplitudeFrequencyDomain = 1


class SimSmoothStepAmplitudeTableColumn(Enum):
    SimSmoothStepAmplitudeAmplitude = 0
    SimSmoothStepAmplitudeTime = 1


class SimSolutionControlsAverageFlux(Enum):
    SimSolutionControlsDefault = 0
    SimSolutionControlsInitial = 1
    SimSolutionControlsAverage = 2


class SimSolutionControlsDefinition(Enum):
    SimSolutionControlsPropagate = 0
    SimSolutionControlsReset = 1
    SimSolutionControlsSpecify = 2


class SimSolutionControlsDOFField(Enum):
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


class SimSpectrumDefinitionType(Enum):
    SimSpectrumAcceleration = 0
    SimSpectrumDisplacement = 1
    SimSpectrumGravity = 2
    SimSpectrumVelocity = 3


class SimSpectrumTableColumn(Enum):
    SimSpectrumAccelerationCol = 0
    SimSpectrumDampingRatioCol = 1
    SimSpectrumFrequencyCol = 2
    SimSpectrumDisplacementCol = 3
    SimSpectrumGravityCol = 4
    SimSpectrumVelocityCol = 5


class SimStabilizationStabilizationType(Enum):
    SimStabilizationNoStabilization = 0
    SimStabilizationDamping = 1
    SimStabilizationEnergyFraction = 2
    SimStabilizationPropagated = 3


class SimStaticPerturbationStepSolutionTechnique(Enum):
    SimStaticPerturbationStepFullNewton = 0
    SimStaticPerturbationStepLCP = 1


class SimStaticRiksStepDisplacementType(Enum):
    SimStaticRiksStepDisplacementNone = 0
    SimStaticRiksStepDisplacementTranslation = 1
    SimStaticRiksStepDisplacementRotation = 2


class SimSteadyStateTransportStepInertiaEffect(Enum):
    SimSteadyStateTransportStepNoInertia = 0
    SimSteadyStateTransportStepHighSpeedInertia = 1
    SimSteadyStateTransportStepLowSpeedInertia = 2


class SimSteadyStateTransportStepMullinsEffect(Enum):
    SimSteadyStateTransportStepRampMullins = 0
    SimSteadyStateTransportStepImmediateMullins = 1


class SimSurfaceBasedContactDiscretizationMethod(Enum):
    SimSurfaceBasedContactNodeToSurface = 0
    SimSurfaceBasedContactSurfaceToSurface = 1


class SimTabularAmplitudeDomainType(Enum):
    SimTabularAmplitudeTimeDomain = 0
    SimTabularAmplitudeFrequencyDomain = 1


class SimTabularAmplitudeTableColumn(Enum):
    SimTabularAmplitudeAmplitude = 0
    SimTabularAmplitudeTime = 1


class SimTimeIncrementationScheme(Enum):
    SimTimeIncrementation_Automatic = 0
    SimTimeIncrementation_Fixed = 1
    SimTimeIncrementation_Direct = 2
    SimTimeIncrementation_SolverDefault = 3


class SimVolumetricHeatSourceHeatSourceType(Enum):
    SimVolumetricHeatSourcePerUnitVolume = 0
    SimVolumetricHeatSourceTotal = 1
