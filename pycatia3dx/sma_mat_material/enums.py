SimAcousticAbsorptionMaterialTableColumn = [
    'SimAcousticAbsorptionMagnitude',
    'SimAcousticAbsorptionPhase',
    'SimAcousticAbsorptionFrequency',
]
SimBulkModulusBulkModulusType = [
    'SimBulkModulusBulk_Modulus',
    'SimBulkModulusComplex_Bulk_Modulus',
]
SimBulkModulusMaterialTableColumn = [
    'SimBulkModulusRealPart',
    'SimBulkModulusTemperature',
    'SimBulkModulusComplexRealPart',
    'SimBulkModulusImaginaryPart',
    'SimBulkModulusFrequency',
]
SimCastIronPlasticityCompressionHardeningMaterialTableColumn = [
    'SimCastIronPlasticitySigmaC',
    'SimCastIronPlasticityEpsilonC',
    'SimCastIronPlasticityTemperatureC',
]
SimCastIronPlasticityPlasticityMaterialTableColumn = [
    'SimCastIronPlasticityPlasticPoissonsRatio',
    'SimCastIronPlasticityPlasticTemperature',
]
SimCastIronPlasticityTensionHardeningMaterialTableColumn = [
    'SimCastIronPlasticitySigmaT',
    'SimCastIronPlasticityEpsilonT',
    'SimCastIronPlasticityTemperatureT',
]
SimConductivityConductivityType = [
    'SimConductivityIsotropicConductivity',
    'SimConductivityOrthotropicConductivity',
    'SimConductivityAnisotropicConductivity',
]
SimConductivityMaterialTableColumn = [
    'SimConductivityThermalConductivity',
    'SimConductivityK1',
    'SimConductivityK2',
    'SimConductivityK3',
    'SimConductivityK11',
    'SimConductivityK12',
    'SimConductivityK13',
    'SimConductivityK22',
    'SimConductivityK23',
    'SimConductivityK33',
    'SimConductivityTemperature',
]
SimDamageEvolutionCategory = [
    'SimDamageEvolutionDisplacement',
    'SimDamageEvolutionEnergy',
]
SimDamageEvolutionDegradation = [
    'SimDamageEvolutionMaximum',
    'SimDamageEvolutionMultiplicative',
]
SimDamageEvolutionMaterialTableColumn = [
    'SimDamageEvolutionLongitudinalTensileFractureEnergy',
    'SimDamageEvolutionLongitudinalCompressiveFractureEnergy',
    'SimDamageEvolutionTransverseTensileFractureEnergy',
    'SimDamageEvolutionTransverseCompressiveFractureEnergy',
    'SimDamageEvolutionDisplacementAtFailure',
    'SimDamageEvolutionExponentialLawParameter',
    'SimDamageEvolutionDamageVariable',
    'SimDamageEvolutionDisplacementTabular',
    'SimDamageEvolutionFractureEnergy',
    'SimDamageEvolutionTemperature',
]
SimDamageEvolutionSoftening = [
    'SimDamageEvolutionLinear',
    'SimDamageEvolutionExponential',
    'SimDamageEvolutionTabular',
]
SimDamageStabilizationMaterialTableColumn = [
    'SimDamageStabilizationViscosityCoefficientLongitudinalTensileDirection',
    'SimDamageStabilizationViscosityCoefficientLongitudinalCompressiveDirection',
    'SimDamageStabilizationViscosityCoefficientTransverseTensileDirection',
    'SimDamageStabilizationViscosityCoefficientTransverseCompressiveDirection',
]
SimDensityMaterialTableColumn = [
    'SimDensityDensity',
    'SimDensityTemperature',
]
SimDepvarMaterialTableColumn = [
    'SimDepvarOutputVariableKey',
    'SimDepvarOutputVariableDescription',
]
SimDuctileDamageMaterialTableColumn = [
    'SimDuctileDamageFractureStrain',
    'SimDuctileDamageStressTriaxiality',
    'SimDuctileDamageStrainRate',
    'SimDuctileDamageTemperature',
]
SimElasticElasticType = [
    'SimElasticIsotropic',
    'SimElasticOrthotropic',
    'SimElasticEngineeringConstants',
    'SimElasticLamina',
    'SimElasticAnisotropic',
    'SimElasticTransverselyIsotropic',
]
SimElasticMaterialTableColumn = [
    'SimElasticYoungsModulus',
    'SimElasticPoissonsRatio',
    'SimElasticD1111',
    'SimElasticD1122',
    'SimElasticD2222',
    'SimElasticD1133',
    'SimElasticD2233',
    'SimElasticD3333',
    'SimElasticD1112',
    'SimElasticD2212',
    'SimElasticD3312',
    'SimElasticD1212',
    'SimElasticD1113',
    'SimElasticD2213',
    'SimElasticD3313',
    'SimElasticD1213',
    'SimElasticD1313',
    'SimElasticD1123',
    'SimElasticD2223',
    'SimElasticD3323',
    'SimElasticD1223',
    'SimElasticD1323',
    'SimElasticD2323',
    'SimElasticE1',
    'SimElasticE2',
    'SimElasticE3',
    'SimElasticNu12',
    'SimElasticNu13',
    'SimElasticNu23',
    'SimElasticG12',
    'SimElasticG13',
    'SimElasticG23',
    'SimElasticParallelYoungModulus',
    'SimElasticNormalYoungModulus',
    'SimElasticParallelPoissonsRatio',
    'SimElasticNormalPoissonsRatio',
    'SimElasticParallelShearModulus',
    'SimElasticTemperature',
]
SimElasticModuliTimeScaleType = [
    'SimElasticLongTerm',
    'SimElasticInstantaneous',
]
SimElongationMaterialTableColumn = [
    'SimElongationElongationAtFracture',
    'SimElongationTemperature',
]
SimEOSEOSType = [
    'SimEOSIdealGas',
    'SimEOSJWL',
    'SimEOSUsUp',
    'SimEOSTabular',
]
SimEOSMaterialTableColumn = [
    'SimEOSf1',
    'SimEOSf2',
    'SimEOSVolumetricStrain',
]
SimExpansionExpansionType = [
    'SimExpansionIsotropic',
    'SimExpansionAnisotropic',
    'SimExpansionOrthotropic',
    'SimExpansionTransverselyIsotropic',
]
SimExpansionMaterialTableColumn = [
    'SimExpansionAlpha',
    'SimExpansionAlpha11',
    'SimExpansionAlpha22',
    'SimExpansionAlpha33',
    'SimExpansionAlpha12',
    'SimExpansionAlpha13',
    'SimExpansionAlpha23',
    'SimExpansionParallelExpansionCoeff',
    'SimExpansionNormalExpansionCoeff',
    'SimExpansionTemperature',
]
SimFailStrainMaterialTableColumn = [
    'SimFailStrainTensileStrainFiber',
    'SimFailStrainCompressiveStrainFiber',
    'SimFailStrainTensileStrainFiberTransverse',
    'SimFailStrainCompressiveStrainFiberTransverse',
    'SimFailStrainShearStrain',
    'SimFailStrainTemperature',
]
SimFailStressMaterialTableColumn = [
    'SimFailStressTensileStressFiber',
    'SimFailStressCompressiveStressFiber',
    'SimFailStressTensileStressFiberTransverse',
    'SimFailStressCompressiveStressFiberTransverse',
    'SimFailStressShearStrength',
    'SimFailStressCrossProductTermCoefficient',
    'SimFailStressEquibiaxialStressLimit',
    'SimFailStressTemperature',
]
SimFluidCapacityInput = [
    'SimFluidCapacityPolynomial',
    'SimFluidCapacityTabular',
]
SimFluidCapacityMaterialTableColumn = [
    'SimFluidCapacityMolarHeat',
    'SimFluidCapacityMolarHeatA',
    'SimFluidCapacityMolarHeatB',
    'SimFluidCapacityMolarHeatC',
    'SimFluidCapacityMolarHeatD',
    'SimFluidCapacityMolarHeatE',
    'SimFluidCapacityTemperature',
]
SimFluidCavityBulkModulusMaterialTableColumn = [
    'SimFluidCavityBulkModulusBulkModulus',
    'SimFluidCavityBulkModulusTemperature',
]
SimFluidCavityDensityMaterialTableColumn = [
    'SimFluidCavityDensityConstant',
    'SimFluidCavityDensityTemperature',
]
SimFluidCavityExpansionMaterialTableColumn = [
    'SimFluidCavityExpansionCoefficient',
    'SimFluidCavityExpansionTemperature',
]
SimFluidMolecularWeightMaterialTableColumn = [
    'SimFluidMolecularWeightConstant',
]
SimGasketMembraneElasticMaterialTableColumn = [
    'SimGasketMembraneElasticYoungsModulus',
    'SimGasketMembraneElasticPoissonsRatio',
    'SimGasketMembraneElasticTemperature',
]
SimGasketThicknessBehaviorBehaviorType = [
    'SimGasketThicknessBehaviorElasticPlastic',
    'SimGasketThicknessBehaviorDamage',
]
SimGasketThicknessBehaviorLoadingMaterialTableColumn = [
    'SimGasketThicknessBehaviorLoadPressure',
    'SimGasketThicknessBehaviorLoadClosure',
    'SimGasketThicknessBehaviorLoadTemperature',
]
SimGasketThicknessBehaviorUnloadingMaterialTableColumn = [
    'SimGasketThicknessBehaviorUnloadPressure',
    'SimGasketThicknessBehaviorUnloadClosure',
    'SimGasketThicknessBehaviorUnloadPlasticClosure',
    'SimGasketThicknessBehaviorUnloadTemperature',
]
SimGasketTransverseShearElasticMaterialTableColumn = [
    'SimGasketTransverseShearElasticShearStiffness',
    'SimGasketTransverseShearElasticTemperature',
]
SimGasketTransverseShearElasticUnitType = [
    'SimGasketTransverseShearElasticStress',
    'SimGasketTransverseShearElasticForce',
]
SimHashinDamageEvolutionCondition = [
    'SimHashinDamageEvolutionEnergy',
]
SimHashinDamageEvolutionMaterialTableColumn = [
    'SimHashinDamageEvolutionLongitudinalTensileFractureEnergy',
    'SimHashinDamageEvolutionLongitudinalCompressiveFractureEnergy',
    'SimHashinDamageEvolutionTransverseTensileFractureEnergy',
    'SimHashinDamageEvolutionTransverseCompressiveFractureEnergy',
    'SimHashinDamageEvolutionTemperature',
]
SimHashinDamageEvolutionSofteningResponse = [
    'SimHashinDamageEvolutionLinear',
]
SimHashinDamageMaterialTableColumn = [
    'SimHashinDamageLongitudinalTensileStrength',
    'SimHashinDamageLongitudinalCompressiveStrength',
    'SimHashinDamageTransverseTensileStrength',
    'SimHashinDamageTransverseCompressiveStrength',
    'SimHashinDamageLongitudinalShearStrength',
    'SimHashinDamageTransverseShearStrength',
    'SimHashinDamageTemperature',
]
SimHeatGenerationUserDefinedMaterialTableColumn = [
    'SimHeatGenerationUserDefinedProperties',
]
SimHyperelasticityMaterialTableColumn = [
    'SimHyperelasticityMu',
    'SimHyperelasticityLambdaM',
    'SimHyperelasticityD',
    'SimHyperelasticityBeta',
    'SimHyperelasticityLamdaM',
    'SimHyperelasticityAlpha',
    'SimHyperelasticityMu1',
    'SimHyperelasticityMu2',
    'SimHyperelasticityMu3',
    'SimHyperelasticityMu4',
    'SimHyperelasticityMu5',
    'SimHyperelasticityMu6',
    'SimHyperelasticityAlpha1',
    'SimHyperelasticityAlpha2',
    'SimHyperelasticityAlpha3',
    'SimHyperelasticityAlpha4',
    'SimHyperelasticityAlpha5',
    'SimHyperelasticityAlpha6',
    'SimHyperelasticityD1',
    'SimHyperelasticityD2',
    'SimHyperelasticityD3',
    'SimHyperelasticityD4',
    'SimHyperelasticityD5',
    'SimHyperelasticityD6',
    'SimHyperelasticityC10',
    'SimHyperelasticityC01',
    'SimHyperelasticityC20',
    'SimHyperelasticityC11',
    'SimHyperelasticityC02',
    'SimHyperelasticityC30',
    'SimHyperelasticityC21',
    'SimHyperelasticityC12',
    'SimHyperelasticityC03',
    'SimHyperelasticityC40',
    'SimHyperelasticityC31',
    'SimHyperelasticityC22',
    'SimHyperelasticityC13',
    'SimHyperelasticityC04',
    'SimHyperelasticityC50',
    'SimHyperelasticityC41',
    'SimHyperelasticityC32',
    'SimHyperelasticityC23',
    'SimHyperelasticityC14',
    'SimHyperelasticityC05',
    'SimHyperelasticityC60',
    'SimHyperelasticityC51',
    'SimHyperelasticityC42',
    'SimHyperelasticityC33',
    'SimHyperelasticityC24',
    'SimHyperelasticityC15',
    'SimHyperelasticityC06',
    'SimHyperelasticityTemperature',
]
SimHyperelasticityModuliTimeScale = [
    'SimHyperelasticityLongTerm',
    'SimHyperelasticityInstantaneous',
]
SimHyperelasticityStrainEnergyPotentialOrder = [
    'SimHyperelasticityN1',
    'SimHyperelasticityN2',
    'SimHyperelasticityN3',
    'SimHyperelasticityN4',
    'SimHyperelasticityN5',
    'SimHyperelasticityN6',
]
SimHyperelasticityStrainEnergyPotential = [
    'SimHyperelasticityArruda_Boyce',
    'SimHyperelasticityNeo_Hooke',
    'SimHyperelasticityOgden',
    'SimHyperelasticityPolynomial',
    'SimHyperelasticityReduced_Polynomial',
    'SimHyperelasticityMooney_Rivlin',
    'SimHyperelasticityVan_Der_Waals',
    'SimHyperelasticityYeoh',
]
SimHyperfoamMaterialTableColumn = [
    'SimHyperfoammu1',
    'SimHyperfoammu2',
    'SimHyperfoammu3',
    'SimHyperfoammu4',
    'SimHyperfoammu5',
    'SimHyperfoammu6',
    'SimHyperfoamalpha1',
    'SimHyperfoamalpha2',
    'SimHyperfoamalpha3',
    'SimHyperfoamalpha4',
    'SimHyperfoamalpha5',
    'SimHyperfoamalpha6',
    'SimHyperfoamnu1',
    'SimHyperfoamnu2',
    'SimHyperfoamnu3',
    'SimHyperfoamnu4',
    'SimHyperfoamnu5',
    'SimHyperfoamnu6',
    'SimHyperfoamTemperature',
]
SimHyperfoamModuliTimeScale = [
    'SimHyperfoamLONG_TERM',
    'SimHyperfoamINSTANTANEOUS',
]
SimHyperfoamStrainEnergyPotentialOrder = [
    'SimHyperfoamN1',
    'SimHyperfoamN2',
    'SimHyperfoamN3',
    'SimHyperfoamN4',
    'SimHyperfoamN5',
    'SimHyperfoamN6',
]
SimLatentHeatMaterialTableColumn = [
    'SimLatentHeatLatentHeat',
    'SimLatentHeatSolidusTemperature',
    'SimLatentHeatLiquidusTemperature',
]
SimMaterialTableOptionalColumn = [
    'SimMaterialTableStrainRate',
    'SimMaterialTableFrequency',
    'SimMaterialTableTemperature',
]
SimPlasticIsotropicMaterialTableColumn = [
    'SimPlasticIsotropicYieldStress',
    'SimPlasticIsotropicPlasticStrain',
    'SimPlasticIsotropicStrainRate',
    'SimPlasticIsotropicYieldStressCombined',
    'SimPlasticIsotropicPlasticStrainCombined',
    'SimPlasticQ_Infinity',
    'SimPlasticHardeningParam_b',
    'SimPlasticA',
    'SimPlasticB',
    'SimPlasticn',
    'SimPlasticm',
    'SimPlasticMeltingTemp',
    'SimPlasticTransitionTemp',
    'SimPlasticIsotropicTemperature',
]
SimPlasticKinematicMaterialTableColumn = [
    'SimPlasticKinematicYieldStress',
    'SimPlasticC1',
    'SimPlasticC2',
    'SimPlasticC3',
    'SimPlasticC4',
    'SimPlasticC5',
    'SimPlasticC6',
    'SimPlasticC7',
    'SimPlasticC8',
    'SimPlasticC9',
    'SimPlasticC10',
    'SimPlasticGamma1',
    'SimPlasticGamma2',
    'SimPlasticGamma3',
    'SimPlasticGamma4',
    'SimPlasticGamma5',
    'SimPlasticGamma6',
    'SimPlasticGamma7',
    'SimPlasticGamma8',
    'SimPlasticGamma9',
    'SimPlasticGamma10',
    'SimPlasticKinematicTemperature',
]
SimPlasticPlasticHardening = [
    'SimPlasticIsotropic_Tabular',
    'SimPlasticIsotropic_JohnsonCook',
    'SimPlasticKinematic',
    'SimPlasticCombined_Tabular',
    'SimPlasticCombined_Exponential',
]
SimPlasticPlasticYieldCriteria = [
    'SimPlasticMises',
    'SimPlasticHill',
]
SimPlasticPotentialMaterialTableColumn = [
    'SimPlasticR11',
    'SimPlasticR22',
    'SimPlasticR33',
    'SimPlasticR12',
    'SimPlasticR13',
    'SimPlasticR23',
    'SimPlasticPotentialTemperature',
]
SimPorousElasticityMaterialTableColumn = [
    'SimPorousElasticityLogBulkModulus',
    'SimPorousElasticityShearModulus',
    'SimPorousElasticityPoissonRatio',
    'SimPorousElasticityTensileLimit',
    'SimPorousElasticityTemperature',
]
SimPorousElasticityShearType = [
    'SimPorousElasticityG',
    'SimPorousElasticityPoisson',
]
SimProofStressMaterialTableColumn = [
    'SimProofStressProofStressAt2PC',
    'SimProofStressTemperature',
]
SimRateDependentHardeningType = [
    'SimPowerlaw',
    'SimYieldRatio',
    'SimJohnsonCook',
]
SimRateDependentMaterialTableColumn = [
    'SimRateDependentMultiplier',
    'SimRateDependentExponent',
    'SimRateDependentYieldStressRatio',
    'SimRateDependentEquivalentPlasticStrainRate',
    'SimRateDependentTemperature',
]
SimSpecificHeatMaterialTableColumn = [
    'SimSpecificHeatSpecificHeat',
    'SimSpecificHeatTemperature',
]
SimSpecificHeatSpecificHeatType = [
    'SimSpecificHeatConstantVolume',
    'SimSpecificHeatConstantPressure',
]
SimTensileFailureCriteria = [
    'SimNone',
    'SimBrittle',
    'SimDuctile',
]
SimTensileFailureMaterialTableColumn = [
    'SimTensileFailureHydroStaticCutOffStress',
    'SimTensileFailureTemperature',
]
SimUltimateStrengthMaterialCompressiveTableColumn = [
    'SimUltimateStrengthUltimateCompressiveStrength',
    'SimUltimateStrengthCompressiveTemperature',
]
SimUltimateStrengthMaterialTensileTableColumn = [
    'SimUltimateStrengthUltimateTensileStrength',
    'SimUltimateStrengthTensileTemperature',
]
SimUserDefinedFieldDirectSpecificationTableColumn = [
    'SimUserDefinedFieldVariableNum',
    'SimUserDefinedFieldVariableName',
]
SimUserDefinedFieldRedefinitionResource = [
    'SimUserDefinedFieldUserSubroutineRedefinition',
    'SimUserDefinedFieldDirectSpecificationRedefinition',
]
SimUserDefinedHybridFormulation = [
    'SimUserDefinedIncremental',
    'SimUserDefinedTotal',
    'SimUserDefinedIncompressible',
]
SimUserDefinedMaterialTableColumn = [
    'SimUserDefinedMechanicalConstants',
    'SimUserDefinedThermalConstants',
]
SimUserDefinedPhysics = [
    'SimUserDefinedMechanical',
    'SimUserDefinedThermal',
    'SimUserDefinedThermoMechanical',
]
SimViscoelasticityFrequencyType = [
    'SimViscoelasticityFORMULA',
    'SimViscoelasticityPRONY',
    'SimViscoelasticityTABULAR',
]
SimViscoelasticityMaterialTableColumn = [
    'SimViscoelasticityRealG1',
    'SimViscoelasticityImagG1',
    'SimViscoelasticityA',
    'SimViscoelasticityRealK1',
    'SimViscoelasticityImagK1',
    'SimViscoelasticityB',
    'SimViscoelasticityPronyG',
    'SimViscoelasticityPronyK',
    'SimViscoelasticityPronyTAU',
    'SimViscoelasticityIsotropicPreloadNoneGReal',
    'SimViscoelasticityIsotropicPreloadNoneGImag',
    'SimViscoelasticityIsotropicPreloadNoneKReal',
    'SimViscoelasticityIsotropicPreloadNoneKImag',
    'SimViscoelasticityIsotropicPreloadNoneFreq',
    'SimViscoelasticityIsotropicPreloadUniaxialLossModulus',
    'SimViscoelasticityIsotropicPreloadUniaxialStorageModulus',
    'SimViscoelasticityIsotropicPreloadUniaxialFreq',
    'SimViscoelasticityIsotropicPreloadUniaxialStrain',
    'SimViscoelasticityIsotropicPreloadVolumetricLossModulus',
    'SimViscoelasticityIsotropicPreloadVolumetricStorageModulus',
    'SimViscoelasticityIsotropicPreloadVolumetricFreq',
    'SimViscoelasticityIsotropicPreloadVolumetricVolumeRatio',
    'SimViscoelasticityTractionPreloadNoneNormLossModulus',
    'SimViscoelasticityTractionPreloadNoneNormStorageModulus',
    'SimViscoelasticityTractionPreloadNoneFreq',
    'SimViscoelasticityTractionPreloadUniaxialLossModulus',
    'SimViscoelasticityTractionPreloadUniaxialStorageModulus',
    'SimViscoelasticityTractionPreloadUniaxialFreq',
    'SimViscoelasticityTractionPreloadUniaxialClosure',
    'SimViscoelasticityTimeGReal',
    'SimViscoelasticityTimeGImag',
    'SimViscoelasticityTimeKReal',
    'SimViscoelasticityTimeKImag',
    'SimViscoelasticityTimeFreq',
]
SimViscoelasticityPreloadType = [
    'SimViscoelasticityNONE',
    'SimViscoelasticityUNIAXIAL',
    'SimViscoelasticityVOLUMETRIC',
]
SimViscoelasticityTabularSubType = [
    'SimViscoelasticityISOTROPIC',
    'SimViscoelasticityTRACTION',
]
SimViscoelasticityTimeType = [
    'SimViscoelasticityTIMEPRONY',
    'SimViscoelasticityFREQUENCYDATA',
]
SimViscoelasticityViscoelasticityDomain = [
    'SimViscoelasticityFREQUENCY',
    'SimViscoelasticityTIME',
]
SimVolumetricDragMaterialTableColumn = [
    'SimVolumetricDragVolumetricDrag',
    'SimVolumetricDragFrequency',
    'SimVolumetricDragTemperature',
]
