SimAcousticCouplingFormulationType = {
    'SimAcousticCouplingNodeToSurface',
    'SimAcousticCouplingSurfaceToSurface',
}
SimAcousticCouplingMainSurfaceType = {
    'SimAcousticCouplingElementBasedMainSurface',
    'SimAcousticCouplingNodeBasedMainSurface',
}
SimAcousticCouplingMasterSurfaceType = {
    'SimAcousticCouplingElementBased',
    'SimAcousticCouplingNodeBased',
}
SimAmplitudeDefinitionType = {
    'SimAmplitudeTabularDefinition',
    'SimAmplitudeSmoothStepDefinition',
    'SimAmplitudePeriodicDefinition',
    'SimAmplitudeUserDefinition',
}
SimAmplitudeTimeSpanType = {
    'SimAmplitudeStepTime',
    'SimAmplitudeTotalTime',
}
SimAMSEigensolverAcousticCouplingType = {
    'SimAMSEigensolverOn',
    'SimAMSEigensolverProjection',
    'SimAMSEigensolverOff',
}
SimApplicationType = {
    'SimApplicationType_Solver_Default',
    'SimApplicationType_Transient_Fidelity',
    'SimApplicationType_Moderate_Dissipation',
    'SimApplicationType_Quasi_Static',
}
SimBeamLoadComponentSystem = {
    'SimBeamLoadGlobalComponentSystem',
    'SimBeamLoadLocalComponentSystem',
}
SimBearingLoadInteractionType = {
    'SimBearingLoadOutward',
    'SimBearingLoadInward',
}
SimBearingLoadOrientationType = {
    'SimBearingLoadRadial',
    'SimBearingLoadParallel',
}
SimBearingLoadProfileType = {
    'SimBearingLoadSinusoidal',
    'SimBearingLoadParabolic',
}
SimBuckleStepSolverType = {
    'SimBuckleStepLANCZOS',
    'SimBuckleStepSUBSPACE',
}
SimConnectorDampingDampingOrder = {
    'SimConnectorDampingLinear',
    'SimConnectorDampingNonLinear',
}
SimConnectorDampingTableColumn = {
    'SimConnectorDampingCoefficient',
    'SimConnectorDampingTemperature',
    'SimConnectorDampingVelocity',
}
SimConnectorRotationVariationType = {
    'SimConnectorRotationUniform',
    'SimConnectorRotationUserDefined',
}
SimConnectorRotationVelocityVariationType = {
    'SimConnectorRotationVelocityUniform',
    'SimConnectorRotationVelocityUserDefined',
}
SimConnectorTranslationVariationType = {
    'SimConnectorTranslationUniform',
    'SimConnectorTranslationUserDefined',
}
SimConnectorTranslationVelocityVariationType = {
    'SimConnectorTranslationVelocityUniform',
    'SimConnectorTranslationVelocityUserDefined',
}
SimCoupledCreepIntegration = {
    'SimCoupledImplicit',
    'SimCoupledExplicit',
}
SimCoupledSolutionTechnique = {
    'SimCoupledFullNewton',
    'SimCoupledSeparated',
}
SimCoupledThermalResponseType = {
    'SimCoupledThermalSteadyState',
    'SimCoupledThermalTransient',
}
SimDirectHarmonicResponseStepIntervalType = {
    'SimDirectHarmonicResponseStepFrequencyIncrement',
    'SimDirectHarmonicResponseStepEigenFrequency',
    'SimDirectHarmonicResponseStepDirectRange',
    'SimDirectHarmonicResponseStepFrequencySpread',
}
SimDirectHarmonicResponseStepScaleType = {
    'SimDirectHarmonicResponseStepLogarithmic',
    'SimDirectHarmonicResponseStepLinear',
}
SimDirectHarmonicResponseStepTableColumn = {
    'SimDirectHarmonicResponseStepLower',
    'SimDirectHarmonicResponseStepUpper',
    'SimDirectHarmonicResponseStepIncrement',
    'SimDirectHarmonicResponseStepNumberOfPoints',
    'SimDirectHarmonicResponseStepBias',
    'SimDirectHarmonicResponseStepScaleFactor',
    'SimDirectHarmonicResponseStepSpread',
}
SimExplicitDynamicStepFixedIncrementationTypeEnm = {
    'SimExplicitDynamicStepELEMENTBYELEMENT',
    'SimExplicitDynamicStepUSERDEFINED',
}
SimFrequencyBasedDampingDampingType = {
    'SimFrequencyBasedDampingCriticalDampingFraction',
    'SimFrequencyBasedDampingStructuralDamping',
    'SimFrequencyBasedDampingRayleighDamping',
}
SimFrequencyBasedDampingModesType = {
    'SimFrequencyBasedDampingStructuralAndAcoustic',
    'SimFrequencyBasedDampingStructural',
    'SimFrequencyBasedDampingAcoustic',
}
SimFrequencyBasedDampingTableColumn = {
    'SimFrequencyBasedDampingFrequency',
    'SimFrequencyBasedDampingDampingFraction',
    'SimFrequencyBasedDampingDampingFactor',
    'SimFrequencyBasedDampingMassDamping',
    'SimFrequencyBasedDampingStiffnessDamping',
}
SimFrequencyStepSolverType = {
    'SimFrequencyStepLanczos',
    'SimFrequencyStepAMS',
}
SimGeneralGlobalDampingModesType = {
    'SimGeneralGlobalDampingNone',
    'SimGeneralGlobalDampingStructuralAndAcoustic',
    'SimGeneralGlobalDampingStructural',
    'SimGeneralGlobalDampingAcoustic',
}
SimHarmonicResponseStepIntervalType = {
    'SimHarmonicResponseStepFrequencyIncrement',
    'SimHarmonicResponseStepEigenfrequency',
    'SimHarmonicResponseStepDirectRange',
    'SimHarmonicResponseStepFrequencySpread',
}
SimHarmonicResponseStepProjectionType = {
    'SimHarmonicResponseStepNone',
    'SimHarmonicResponseStepAllFrequency',
    'SimHarmonicResponseStepCenterFrequencies',
    'SimHarmonicResponseStepRangeValues',
}
SimHarmonicResponseStepScaleType = {
    'SimHarmonicResponseStepLogarithmic',
    'SimHarmonicResponseStepLinear',
}
SimHarmonicResponseStepTableColumn = {
    'SimHarmonicResponseStepLower',
    'SimHarmonicResponseStepUpper',
    'SimHarmonicResponseStepIncrement',
    'SimHarmonicResponseStepNumberOfPoints',
    'SimHarmonicResponseStepBias',
    'SimHarmonicResponseStepScaleFactor',
    'SimHarmonicResponseStepSpread',
}
SimInitialStressType = {
    'SimInitialStressTensorStress',
    'SimInitialStressRebarStress',
}
SimLanczosEigensolverAcousticCouplingType = {
    'SimLanczosEigensolverOn',
    'SimLanczosEigensolverProjection',
    'SimLanczosEigensolverOff',
}
SimMassScalingMassScalingBehavior = {
    'SimMassScalingBeginningOfStep',
    'SimMassScalingThroughoutStep',
    'SimMassScalingResetMassMatrix',
}
SimMassScalingMassScalingMethod = {
    'SimMassScalingUniform',
    'SimMassScalingBelowMin',
    'SimMassScalingSameTimeIncrement',
}
SimMatrixStorageScheme = {
    'SimMatrixStorage_Default',
    'SimMatrixStorage_Symmetric',
    'SimMatrixStorage_Unsymmetric',
}
SimModalDampingDampingType = {
    'SimModalDampingFraction',
    'SimModalDampingRayleigh',
    'SimModalDampingStructural',
}
SimModalDampingTableColumn = {
    'SimModalDampingFrequency',
    'SimModalDampingDampingFraction',
    'SimModalDampingAlpha',
    'SimModalDampingBeta',
    'SimModalDampingDampingFactor',
}
SimModeBasedDampingDampingType = {
    'SimModeBasedDampingCriticalDampingFraction',
    'SimModeBasedDampingStructural',
    'SimModeBasedDampingComposite',
    'SimModeBasedDampingRayleigh',
}
SimModeBasedDampingTableColumn = {
    'SimModeBasedDampingFirstMode',
    'SimModeBasedDampingLastMode',
    'SimModeBasedDampingDampingFraction',
    'SimModeBasedDampingDampingFactor',
    'SimModeBasedDampingMassScaling',
    'SimModeBasedDampingStiffnessScaling',
    'SimModeBasedDampingMassDamping',
    'SimModeBasedDampingStiffnessDamping',
}
SimNormalBehaviorTableColumn = {
    'SimNormalBehaviorPressure',
    'SimNormalBehaviorOverclosure',
}
SimOutputElementLocation = {
    'SimOutputAtIntegrationPoints',
    'SimOutputAtNodes',
    'SimOutputAtCentroid',
    'SimOutputAtNodesAveraged',
}
SimOutputFrequencyType = {
    'SimOutputFrequency',
    'SimOutputNumberInterval',
    'SimOutputTimeInterval',
}
SimOutputOutputGroup = {
    'SimOutputField',
    'SimOutputHistory',
}
SimOutputSectionPointSelectionType = {
    'SimOutputDefault',
    'SimOutputSpecify',
    'SimOutputAll',
    'SimOutputByLayer',
}
SimPeriodicAmplitudeColumnType = {
    'SimPeriodicAmplitudeASeriesColumn',
    'SimPeriodicAmplitudeBSeriesColumn',
}
SimRandomGlobalDampingModesType = {
    'SimRandomGlobalDampingStructuralAndAcoustic',
    'SimRandomGlobalDampingStructural',
    'SimRandomGlobalDampingAcoustic',
}
SimRandomVibrationStepDampingDefinition = {
    'SimRandomVibrationStepModeRange',
    'SimRandomVibrationStepFrequencyCurve',
    'SimRandomVibrationStepGlobal',
    'SimRandomVibrationStepNoDamping',
}
SimRandomVibrationStepTableColumn = {
    'SimRandomVibrationStepLowerBoundary',
    'SimRandomVibrationStepUpperBoundary',
    'SimRandomVibrationStepCalculationPoints',
    'SimRandomVibrationStepBias',
    'SimRandomVibrationStepFrequencyScale',
}
SimResponseSpectrumStepAlignAxisType = {
    'SimResponseSpectrumStepXAxis',
    'SimResponseSpectrumStepYAxis',
    'SimResponseSpectrumStepZAxis',
}
SimResponseSpectrumStepDampingDefinition = {
    'SimResponseSpectrumStepModeRange',
    'SimResponseSpectrumStepFrequencyCurve',
    'SimResponseSpectrumStepGlobal',
    'SimResponseSpectrumStepNoDamping',
}
SimResponseSpectrumStepDirectionalSummationMethod = {
    'SimResponseSpectrumStepAlgebraic',
    'SimResponseSpectrumStepSquareRootOfSumOfSquares',
    'SimResponseSpectrumStepFortyPercentRule',
    'SimResponseSpectrumStepThirtyPercentRule',
}
SimResponseSpectrumStepDirectionType = {
    'SimResponseSpectrumStepFirst',
    'SimResponseSpectrumStepSecond',
    'SimResponseSpectrumStepThird',
}
SimResponseSpectrumStepModalSummationMethod = {
    'SimResponseSpectrumStepAbsoluteValues',
    'SimResponseSpectrumStepSquareRootOfSumOfSquaresMethod',
    'SimResponseSpectrumStepNavalResearchLaboratory',
    'SimResponseSpectrumStepTenPercentMethod',
    'SimResponseSpectrumStepCompleteQuadraticCombination',
    'SimResponseSpectrumStepGroupingMethod',
    'SimResponseSpectrumStepDoubleSumCombination',
}
SimResponseSpectrumStepRigidResponseMethod = {
    'SimResponseSpectrumStepNone',
    'SimResponseSpectrumStepGupta',
    'SimResponseSpectrumStepLindleyYow',
}
SimShellEdgeLoadTractionType = {
    'SimShellEdgeLoadNormal',
    'SimShellEdgeLoadTransverse',
    'SimShellEdgeLoadShear',
}
SimSlidingVelocityTranslationalDof = {
    'SimSlidingVelocityTranslationX',
    'SimSlidingVelocityTranslationY',
    'SimSlidingVelocityTranslationZ',
}
SimSlidingVelocityType = {
    'SimSlidingVelocityTranslation',
    'SimSlidingVelocityRotation',
}
SimSmoothStepAmplitudeDomainType = {
    'SimSmoothStepAmplitudeTimeDomain',
    'SimSmoothStepAmplitudeFrequencyDomain',
}
SimSmoothStepAmplitudeTableColumn = {
    'SimSmoothStepAmplitudeAmplitude',
    'SimSmoothStepAmplitudeTime',
}
SimSolutionControlsAverageFlux = {
    'SimSolutionControlsDefault',
    'SimSolutionControlsInitial',
    'SimSolutionControlsAverage',
}
SimSolutionControlsDefinition = {
    'SimSolutionControlsPropagate',
    'SimSolutionControlsReset',
    'SimSolutionControlsSpecify',
}
SimSolutionControlsDOFField = {
    'SimSolutionControlsDisplacement',
    'SimSolutionControlsRotation',
    'SimSolutionControlsTemperature',
    'SimSolutionControlsPorePressure',
    'SimSolutionControlsElectricPotential',
    'SimSolutionControlsElectricPotentialPiezo',
    'SimSolutionControlsFluidElectricPotential',
    'SimSolutionControlsHydrostaticFluidPressure',
    'SimSolutionControlsPressureLagrangeMultiplier',
    'SimSolutionControlsVolumeLagrangeMultiplier',
    'SimSolutionControlsIonConcentration',
}
SimSpectrumDefinitionType = {
    'SimSpectrumAcceleration',
    'SimSpectrumDisplacement',
    'SimSpectrumGravity',
    'SimSpectrumVelocity',
}
SimSpectrumTableColumn = {
    'SimSpectrumAccelerationCol',
    'SimSpectrumDampingRatioCol',
    'SimSpectrumFrequencyCol',
    'SimSpectrumDisplacementCol',
    'SimSpectrumGravityCol',
    'SimSpectrumVelocityCol',
}
SimStabilizationStabilizationType = {
    'SimStabilizationNoStabilization',
    'SimStabilizationDamping',
    'SimStabilizationEnergyFraction',
    'SimStabilizationPropagated',
}
SimStaticPerturbationStepSolutionTechnique = {
    'SimStaticPerturbationStepFullNewton',
    'SimStaticPerturbationStepLCP',
}
SimStaticRiksStepDisplacementType = {
    'SimStaticRiksStepDisplacementNone',
    'SimStaticRiksStepDisplacementTranslation',
    'SimStaticRiksStepDisplacementRotation',
}
SimSteadyStateTransportStepInertiaEffect = {
    'SimSteadyStateTransportStepNoInertia',
    'SimSteadyStateTransportStepHighSpeedInertia',
    'SimSteadyStateTransportStepLowSpeedInertia',
}
SimSteadyStateTransportStepMullinsEffect = {
    'SimSteadyStateTransportStepRampMullins',
    'SimSteadyStateTransportStepImmediateMullins',
}
SimSurfaceBasedContactDiscretizationMethod = {
    'SimSurfaceBasedContactNodeToSurface',
    'SimSurfaceBasedContactSurfaceToSurface',
}
SimTabularAmplitudeDomainType = {
    'SimTabularAmplitudeTimeDomain',
    'SimTabularAmplitudeFrequencyDomain',
}
SimTabularAmplitudeTableColumn = {
    'SimTabularAmplitudeAmplitude',
    'SimTabularAmplitudeTime',
}
SimTimeIncrementationScheme = {
    'SimTimeIncrementation_Automatic',
    'SimTimeIncrementation_Fixed',
    'SimTimeIncrementation_Direct',
    'SimTimeIncrementation_SolverDefault',
}
SimVolumetricHeatSourceHeatSourceType = {
    'SimVolumetricHeatSourcePerUnitVolume',
    'SimVolumetricHeatSourceTotal',
}
