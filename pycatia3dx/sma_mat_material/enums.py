from enum import IntEnum


class SimAcousticAbsorptionMaterialTableColumn(IntEnum):
    SimAcousticAbsorptionMagnitude = 0
    SimAcousticAbsorptionPhase = 1
    SimAcousticAbsorptionFrequency = 2


class SimBulkModulusBulkModulusType(IntEnum):
    SimBulkModulusBulk_Modulus = 0
    SimBulkModulusComplex_Bulk_Modulus = 1


class SimBulkModulusMaterialTableColumn(IntEnum):
    SimBulkModulusRealPart = 0
    SimBulkModulusTemperature = 1
    SimBulkModulusComplexRealPart = 2
    SimBulkModulusImaginaryPart = 3
    SimBulkModulusFrequency = 4


class SimCastIronPlasticityCompressionHardeningMaterialTableColumn(IntEnum):
    SimCastIronPlasticitySigmaC = 0
    SimCastIronPlasticityEpsilonC = 1
    SimCastIronPlasticityTemperatureC = 2


class SimCastIronPlasticityPlasticityMaterialTableColumn(IntEnum):
    SimCastIronPlasticityPlasticPoissonsRatio = 0
    SimCastIronPlasticityPlasticTemperature = 1


class SimCastIronPlasticityTensionHardeningMaterialTableColumn(IntEnum):
    SimCastIronPlasticitySigmaT = 0
    SimCastIronPlasticityEpsilonT = 1
    SimCastIronPlasticityTemperatureT = 2


class SimConductivityConductivityType(IntEnum):
    SimConductivityIsotropicConductivity = 0
    SimConductivityOrthotropicConductivity = 1
    SimConductivityAnisotropicConductivity = 2


class SimConductivityMaterialTableColumn(IntEnum):
    SimConductivityThermalConductivity = 0
    SimConductivityK1 = 1
    SimConductivityK2 = 2
    SimConductivityK3 = 3
    SimConductivityK11 = 4
    SimConductivityK12 = 5
    SimConductivityK13 = 6
    SimConductivityK22 = 7
    SimConductivityK23 = 8
    SimConductivityK33 = 9
    SimConductivityTemperature = 10


class SimDamageEvolutionCategory(IntEnum):
    SimDamageEvolutionDisplacement = 0
    SimDamageEvolutionEnergy = 1


class SimDamageEvolutionDegradation(IntEnum):
    SimDamageEvolutionMaximum = 0
    SimDamageEvolutionMultiplicative = 1


class SimDamageEvolutionMaterialTableColumn(IntEnum):
    SimDamageEvolutionLongitudinalTensileFractureEnergy = 0
    SimDamageEvolutionLongitudinalCompressiveFractureEnergy = 1
    SimDamageEvolutionTransverseTensileFractureEnergy = 2
    SimDamageEvolutionTransverseCompressiveFractureEnergy = 3
    SimDamageEvolutionDisplacementAtFailure = 4
    SimDamageEvolutionExponentialLawParameter = 5
    SimDamageEvolutionDamageVariable = 6
    SimDamageEvolutionDisplacementTabular = 7
    SimDamageEvolutionFractureEnergy = 8
    SimDamageEvolutionTemperature = 9


class SimDamageEvolutionSoftening(IntEnum):
    SimDamageEvolutionLinear = 0
    SimDamageEvolutionExponential = 1
    SimDamageEvolutionTabular = 2


class SimDamageStabilizationMaterialTableColumn(IntEnum):
    SimDamageStabilizationViscosityCoefficientLongitudinalTensileDirection = 0
    SimDamageStabilizationViscosityCoefficientLongitudinalCompressiveDirection = 1
    SimDamageStabilizationViscosityCoefficientTransverseTensileDirection = 2
    SimDamageStabilizationViscosityCoefficientTransverseCompressiveDirection = 3


class SimDensityMaterialTableColumn(IntEnum):
    SimDensityDensity = 0
    SimDensityTemperature = 1


class SimDepvarMaterialTableColumn(IntEnum):
    SimDepvarOutputVariableKey = 0
    SimDepvarOutputVariableDescription = 1


class SimDuctileDamageMaterialTableColumn(IntEnum):
    SimDuctileDamageFractureStrain = 0
    SimDuctileDamageStressTriaxiality = 1
    SimDuctileDamageStrainRate = 2
    SimDuctileDamageTemperature = 3


class SimElasticElasticType(IntEnum):
    SimElasticIsotropic = 0
    SimElasticOrthotropic = 1
    SimElasticEngineeringConstants = 2
    SimElasticLamina = 3
    SimElasticAnisotropic = 4
    SimElasticTransverselyIsotropic = 5


class SimElasticMaterialTableColumn(IntEnum):
    SimElasticYoungsModulus = 0
    SimElasticPoissonsRatio = 1
    SimElasticD1111 = 2
    SimElasticD1122 = 3
    SimElasticD2222 = 4
    SimElasticD1133 = 5
    SimElasticD2233 = 6
    SimElasticD3333 = 7
    SimElasticD1112 = 8
    SimElasticD2212 = 9
    SimElasticD3312 = 10
    SimElasticD1212 = 11
    SimElasticD1113 = 12
    SimElasticD2213 = 13
    SimElasticD3313 = 14
    SimElasticD1213 = 15
    SimElasticD1313 = 16
    SimElasticD1123 = 17
    SimElasticD2223 = 18
    SimElasticD3323 = 19
    SimElasticD1223 = 20
    SimElasticD1323 = 21
    SimElasticD2323 = 22
    SimElasticE1 = 23
    SimElasticE2 = 24
    SimElasticE3 = 25
    SimElasticNu12 = 26
    SimElasticNu13 = 27
    SimElasticNu23 = 28
    SimElasticG12 = 29
    SimElasticG13 = 30
    SimElasticG23 = 31
    SimElasticParallelYoungModulus = 32
    SimElasticNormalYoungModulus = 33
    SimElasticParallelPoissonsRatio = 34
    SimElasticNormalPoissonsRatio = 35
    SimElasticParallelShearModulus = 36
    SimElasticTemperature = 37


class SimElasticModuliTimeScaleType(IntEnum):
    SimElasticLongTerm = 0
    SimElasticInstantaneous = 1


class SimElongationMaterialTableColumn(IntEnum):
    SimElongationElongationAtFracture = 0
    SimElongationTemperature = 1


class SimEOSEOSType(IntEnum):
    SimEOSIdealGas = 0
    SimEOSJWL = 1
    SimEOSUsUp = 2
    SimEOSTabular = 3


class SimEOSMaterialTableColumn(IntEnum):
    SimEOSf1 = 0
    SimEOSf2 = 1
    SimEOSVolumetricStrain = 2


class SimExpansionExpansionType(IntEnum):
    SimExpansionIsotropic = 0
    SimExpansionAnisotropic = 1
    SimExpansionOrthotropic = 2
    SimExpansionTransverselyIsotropic = 3


class SimExpansionMaterialTableColumn(IntEnum):
    SimExpansionAlpha = 0
    SimExpansionAlpha11 = 1
    SimExpansionAlpha22 = 2
    SimExpansionAlpha33 = 3
    SimExpansionAlpha12 = 4
    SimExpansionAlpha13 = 5
    SimExpansionAlpha23 = 6
    SimExpansionParallelExpansionCoeff = 7
    SimExpansionNormalExpansionCoeff = 8
    SimExpansionTemperature = 9


class SimFailStrainMaterialTableColumn(IntEnum):
    SimFailStrainTensileStrainFiber = 0
    SimFailStrainCompressiveStrainFiber = 1
    SimFailStrainTensileStrainFiberTransverse = 2
    SimFailStrainCompressiveStrainFiberTransverse = 3
    SimFailStrainShearStrain = 4
    SimFailStrainTemperature = 5


class SimFailStressMaterialTableColumn(IntEnum):
    SimFailStressTensileStressFiber = 0
    SimFailStressCompressiveStressFiber = 1
    SimFailStressTensileStressFiberTransverse = 2
    SimFailStressCompressiveStressFiberTransverse = 3
    SimFailStressShearStrength = 4
    SimFailStressCrossProductTermCoefficient = 5
    SimFailStressEquibiaxialStressLimit = 6
    SimFailStressTemperature = 7


class SimFluidCapacityInput(IntEnum):
    SimFluidCapacityPolynomial = 0
    SimFluidCapacityTabular = 1


class SimFluidCapacityMaterialTableColumn(IntEnum):
    SimFluidCapacityMolarHeat = 0
    SimFluidCapacityMolarHeatA = 1
    SimFluidCapacityMolarHeatB = 2
    SimFluidCapacityMolarHeatC = 3
    SimFluidCapacityMolarHeatD = 4
    SimFluidCapacityMolarHeatE = 5
    SimFluidCapacityTemperature = 6


class SimFluidCavityBulkModulusMaterialTableColumn(IntEnum):
    SimFluidCavityBulkModulusBulkModulus = 0
    SimFluidCavityBulkModulusTemperature = 1


class SimFluidCavityDensityMaterialTableColumn(IntEnum):
    SimFluidCavityDensityConstant = 0
    SimFluidCavityDensityTemperature = 1


class SimFluidCavityExpansionMaterialTableColumn(IntEnum):
    SimFluidCavityExpansionCoefficient = 0
    SimFluidCavityExpansionTemperature = 1


class SimFluidMolecularWeightMaterialTableColumn(IntEnum):
    SimFluidMolecularWeightConstant = 0


class SimGasketMembraneElasticMaterialTableColumn(IntEnum):
    SimGasketMembraneElasticYoungsModulus = 0
    SimGasketMembraneElasticPoissonsRatio = 1
    SimGasketMembraneElasticTemperature = 2


class SimGasketThicknessBehaviorBehaviorType(IntEnum):
    SimGasketThicknessBehaviorElasticPlastic = 0
    SimGasketThicknessBehaviorDamage = 1


class SimGasketThicknessBehaviorLoadingMaterialTableColumn(IntEnum):
    SimGasketThicknessBehaviorLoadPressure = 0
    SimGasketThicknessBehaviorLoadClosure = 1
    SimGasketThicknessBehaviorLoadTemperature = 2


class SimGasketThicknessBehaviorUnloadingMaterialTableColumn(IntEnum):
    SimGasketThicknessBehaviorUnloadPressure = 0
    SimGasketThicknessBehaviorUnloadClosure = 1
    SimGasketThicknessBehaviorUnloadPlasticClosure = 2
    SimGasketThicknessBehaviorUnloadTemperature = 3


class SimGasketTransverseShearElasticMaterialTableColumn(IntEnum):
    SimGasketTransverseShearElasticShearStiffness = 0
    SimGasketTransverseShearElasticTemperature = 1


class SimGasketTransverseShearElasticUnitType(IntEnum):
    SimGasketTransverseShearElasticStress = 0
    SimGasketTransverseShearElasticForce = 1


class SimHashinDamageEvolutionCondition(IntEnum):
    SimHashinDamageEvolutionEnergy = 0


class SimHashinDamageEvolutionMaterialTableColumn(IntEnum):
    SimHashinDamageEvolutionLongitudinalTensileFractureEnergy = 0
    SimHashinDamageEvolutionLongitudinalCompressiveFractureEnergy = 1
    SimHashinDamageEvolutionTransverseTensileFractureEnergy = 2
    SimHashinDamageEvolutionTransverseCompressiveFractureEnergy = 3
    SimHashinDamageEvolutionTemperature = 4


class SimHashinDamageEvolutionSofteningResponse(IntEnum):
    SimHashinDamageEvolutionLinear = 0


class SimHashinDamageMaterialTableColumn(IntEnum):
    SimHashinDamageLongitudinalTensileStrength = 0
    SimHashinDamageLongitudinalCompressiveStrength = 1
    SimHashinDamageTransverseTensileStrength = 2
    SimHashinDamageTransverseCompressiveStrength = 3
    SimHashinDamageLongitudinalShearStrength = 4
    SimHashinDamageTransverseShearStrength = 5
    SimHashinDamageTemperature = 6


class SimHeatGenerationUserDefinedMaterialTableColumn(IntEnum):
    SimHeatGenerationUserDefinedProperties = 0


class SimHyperelasticityMaterialTableColumn(IntEnum):
    SimHyperelasticityMu = 0
    SimHyperelasticityLambdaM = 1
    SimHyperelasticityD = 2
    SimHyperelasticityBeta = 3
    SimHyperelasticityLamdaM = 4
    SimHyperelasticityAlpha = 5
    SimHyperelasticityMu1 = 6
    SimHyperelasticityMu2 = 7
    SimHyperelasticityMu3 = 8
    SimHyperelasticityMu4 = 9
    SimHyperelasticityMu5 = 10
    SimHyperelasticityMu6 = 11
    SimHyperelasticityAlpha1 = 12
    SimHyperelasticityAlpha2 = 13
    SimHyperelasticityAlpha3 = 14
    SimHyperelasticityAlpha4 = 15
    SimHyperelasticityAlpha5 = 16
    SimHyperelasticityAlpha6 = 17
    SimHyperelasticityD1 = 18
    SimHyperelasticityD2 = 19
    SimHyperelasticityD3 = 20
    SimHyperelasticityD4 = 21
    SimHyperelasticityD5 = 22
    SimHyperelasticityD6 = 23
    SimHyperelasticityC10 = 24
    SimHyperelasticityC01 = 25
    SimHyperelasticityC20 = 26
    SimHyperelasticityC11 = 27
    SimHyperelasticityC02 = 28
    SimHyperelasticityC30 = 29
    SimHyperelasticityC21 = 30
    SimHyperelasticityC12 = 31
    SimHyperelasticityC03 = 32
    SimHyperelasticityC40 = 33
    SimHyperelasticityC31 = 34
    SimHyperelasticityC22 = 35
    SimHyperelasticityC13 = 36
    SimHyperelasticityC04 = 37
    SimHyperelasticityC50 = 38
    SimHyperelasticityC41 = 39
    SimHyperelasticityC32 = 40
    SimHyperelasticityC23 = 41
    SimHyperelasticityC14 = 42
    SimHyperelasticityC05 = 43
    SimHyperelasticityC60 = 44
    SimHyperelasticityC51 = 45
    SimHyperelasticityC42 = 46
    SimHyperelasticityC33 = 47
    SimHyperelasticityC24 = 48
    SimHyperelasticityC15 = 49
    SimHyperelasticityC06 = 50
    SimHyperelasticityTemperature = 51


class SimHyperelasticityModuliTimeScale(IntEnum):
    SimHyperelasticityLongTerm = 0
    SimHyperelasticityInstantaneous = 1


class SimHyperelasticityStrainEnergyPotentialOrder(IntEnum):
    SimHyperelasticityN1 = 0
    SimHyperelasticityN2 = 1
    SimHyperelasticityN3 = 2
    SimHyperelasticityN4 = 3
    SimHyperelasticityN5 = 4
    SimHyperelasticityN6 = 5


class SimHyperelasticityStrainEnergyPotential(IntEnum):
    SimHyperelasticityArruda_Boyce = 0
    SimHyperelasticityNeo_Hooke = 1
    SimHyperelasticityOgden = 2
    SimHyperelasticityPolynomial = 3
    SimHyperelasticityReduced_Polynomial = 4
    SimHyperelasticityMooney_Rivlin = 5
    SimHyperelasticityVan_Der_Waals = 6
    SimHyperelasticityYeoh = 7


class SimHyperfoamMaterialTableColumn(IntEnum):
    SimHyperfoammu1 = 0
    SimHyperfoammu2 = 1
    SimHyperfoammu3 = 2
    SimHyperfoammu4 = 3
    SimHyperfoammu5 = 4
    SimHyperfoammu6 = 5
    SimHyperfoamalpha1 = 6
    SimHyperfoamalpha2 = 7
    SimHyperfoamalpha3 = 8
    SimHyperfoamalpha4 = 9
    SimHyperfoamalpha5 = 10
    SimHyperfoamalpha6 = 11
    SimHyperfoamnu1 = 12
    SimHyperfoamnu2 = 13
    SimHyperfoamnu3 = 14
    SimHyperfoamnu4 = 15
    SimHyperfoamnu5 = 16
    SimHyperfoamnu6 = 17
    SimHyperfoamTemperature = 18


class SimHyperfoamModuliTimeScale(IntEnum):
    SimHyperfoamLONG_TERM = 0
    SimHyperfoamINSTANTANEOUS = 1


class SimHyperfoamStrainEnergyPotentialOrder(IntEnum):
    SimHyperfoamN1 = 0
    SimHyperfoamN2 = 1
    SimHyperfoamN3 = 2
    SimHyperfoamN4 = 3
    SimHyperfoamN5 = 4
    SimHyperfoamN6 = 5


class SimLatentHeatMaterialTableColumn(IntEnum):
    SimLatentHeatLatentHeat = 0
    SimLatentHeatSolidusTemperature = 1
    SimLatentHeatLiquidusTemperature = 2


class SimMaterialTableOptionalColumn(IntEnum):
    SimMaterialTableStrainRate = 0
    SimMaterialTableFrequency = 1
    SimMaterialTableTemperature = 2


class SimPlasticIsotropicMaterialTableColumn(IntEnum):
    SimPlasticIsotropicYieldStress = 0
    SimPlasticIsotropicPlasticStrain = 1
    SimPlasticIsotropicStrainRate = 2
    SimPlasticIsotropicYieldStressCombined = 3
    SimPlasticIsotropicPlasticStrainCombined = 4
    SimPlasticQ_Infinity = 5
    SimPlasticHardeningParam_b = 6
    SimPlasticA = 7
    SimPlasticB = 8
    SimPlasticn = 9
    SimPlasticm = 10
    SimPlasticMeltingTemp = 11
    SimPlasticTransitionTemp = 12
    SimPlasticIsotropicTemperature = 13


class SimPlasticKinematicMaterialTableColumn(IntEnum):
    SimPlasticKinematicYieldStress = 0
    SimPlasticC1 = 1
    SimPlasticC2 = 2
    SimPlasticC3 = 3
    SimPlasticC4 = 4
    SimPlasticC5 = 5
    SimPlasticC6 = 6
    SimPlasticC7 = 7
    SimPlasticC8 = 8
    SimPlasticC9 = 9
    SimPlasticC10 = 10
    SimPlasticGamma1 = 11
    SimPlasticGamma2 = 12
    SimPlasticGamma3 = 13
    SimPlasticGamma4 = 14
    SimPlasticGamma5 = 15
    SimPlasticGamma6 = 16
    SimPlasticGamma7 = 17
    SimPlasticGamma8 = 18
    SimPlasticGamma9 = 19
    SimPlasticGamma10 = 20
    SimPlasticKinematicTemperature = 21


class SimPlasticPlasticHardening(IntEnum):
    SimPlasticIsotropic_Tabular = 0
    SimPlasticIsotropic_JohnsonCook = 1
    SimPlasticKinematic = 2
    SimPlasticCombined_Tabular = 3
    SimPlasticCombined_Exponential = 4


class SimPlasticPlasticYieldCriteria(IntEnum):
    SimPlasticMises = 0
    SimPlasticHill = 1


class SimPlasticPotentialMaterialTableColumn(IntEnum):
    SimPlasticR11 = 0
    SimPlasticR22 = 1
    SimPlasticR33 = 2
    SimPlasticR12 = 3
    SimPlasticR13 = 4
    SimPlasticR23 = 5
    SimPlasticPotentialTemperature = 6


class SimPorousElasticityMaterialTableColumn(IntEnum):
    SimPorousElasticityLogBulkModulus = 0
    SimPorousElasticityShearModulus = 1
    SimPorousElasticityPoissonRatio = 2
    SimPorousElasticityTensileLimit = 3
    SimPorousElasticityTemperature = 4


class SimPorousElasticityShearType(IntEnum):
    SimPorousElasticityG = 0
    SimPorousElasticityPoisson = 1


class SimProofStressMaterialTableColumn(IntEnum):
    SimProofStressProofStressAt2PC = 0
    SimProofStressTemperature = 1


class SimRateDependentHardeningType(IntEnum):
    SimPowerlaw = 0
    SimYieldRatio = 1
    SimJohnsonCook = 2


class SimRateDependentMaterialTableColumn(IntEnum):
    SimRateDependentMultiplier = 0
    SimRateDependentExponent = 1
    SimRateDependentYieldStressRatio = 2
    SimRateDependentEquivalentPlasticStrainRate = 3
    SimRateDependentTemperature = 4


class SimSpecificHeatMaterialTableColumn(IntEnum):
    SimSpecificHeatSpecificHeat = 0
    SimSpecificHeatTemperature = 1


class SimSpecificHeatSpecificHeatType(IntEnum):
    SimSpecificHeatConstantVolume = 0
    SimSpecificHeatConstantPressure = 1


class SimTensileFailureCriteria(IntEnum):
    SimNone = 0
    SimBrittle = 1
    SimDuctile = 2


class SimTensileFailureMaterialTableColumn(IntEnum):
    SimTensileFailureHydroStaticCutOffStress = 0
    SimTensileFailureTemperature = 1


class SimUltimateStrengthMaterialCompressiveTableColumn(IntEnum):
    SimUltimateStrengthUltimateCompressiveStrength = 0
    SimUltimateStrengthCompressiveTemperature = 1


class SimUltimateStrengthMaterialTensileTableColumn(IntEnum):
    SimUltimateStrengthUltimateTensileStrength = 0
    SimUltimateStrengthTensileTemperature = 1


class SimUserDefinedFieldDirectSpecificationTableColumn(IntEnum):
    SimUserDefinedFieldVariableNum = 0
    SimUserDefinedFieldVariableName = 1


class SimUserDefinedFieldRedefinitionResource(IntEnum):
    SimUserDefinedFieldUserSubroutineRedefinition = 0
    SimUserDefinedFieldDirectSpecificationRedefinition = 1


class SimUserDefinedHybridFormulation(IntEnum):
    SimUserDefinedIncremental = 0
    SimUserDefinedTotal = 1
    SimUserDefinedIncompressible = 2


class SimUserDefinedMaterialTableColumn(IntEnum):
    SimUserDefinedMechanicalConstants = 0
    SimUserDefinedThermalConstants = 1


class SimUserDefinedPhysics(IntEnum):
    SimUserDefinedMechanical = 0
    SimUserDefinedThermal = 1
    SimUserDefinedThermoMechanical = 2


class SimViscoelasticityFrequencyType(IntEnum):
    SimViscoelasticityFORMULA = 0
    SimViscoelasticityPRONY = 1
    SimViscoelasticityTABULAR = 2


class SimViscoelasticityMaterialTableColumn(IntEnum):
    SimViscoelasticityRealG1 = 0
    SimViscoelasticityImagG1 = 1
    SimViscoelasticityA = 2
    SimViscoelasticityRealK1 = 3
    SimViscoelasticityImagK1 = 4
    SimViscoelasticityB = 5
    SimViscoelasticityPronyG = 6
    SimViscoelasticityPronyK = 7
    SimViscoelasticityPronyTAU = 8
    SimViscoelasticityIsotropicPreloadNoneGReal = 9
    SimViscoelasticityIsotropicPreloadNoneGImag = 10
    SimViscoelasticityIsotropicPreloadNoneKReal = 11
    SimViscoelasticityIsotropicPreloadNoneKImag = 12
    SimViscoelasticityIsotropicPreloadNoneFreq = 13
    SimViscoelasticityIsotropicPreloadUniaxialLossModulus = 14
    SimViscoelasticityIsotropicPreloadUniaxialStorageModulus = 15
    SimViscoelasticityIsotropicPreloadUniaxialFreq = 16
    SimViscoelasticityIsotropicPreloadUniaxialStrain = 17
    SimViscoelasticityIsotropicPreloadVolumetricLossModulus = 18
    SimViscoelasticityIsotropicPreloadVolumetricStorageModulus = 19
    SimViscoelasticityIsotropicPreloadVolumetricFreq = 20
    SimViscoelasticityIsotropicPreloadVolumetricVolumeRatio = 21
    SimViscoelasticityTractionPreloadNoneNormLossModulus = 22
    SimViscoelasticityTractionPreloadNoneNormStorageModulus = 23
    SimViscoelasticityTractionPreloadNoneFreq = 24
    SimViscoelasticityTractionPreloadUniaxialLossModulus = 25
    SimViscoelasticityTractionPreloadUniaxialStorageModulus = 26
    SimViscoelasticityTractionPreloadUniaxialFreq = 27
    SimViscoelasticityTractionPreloadUniaxialClosure = 28
    SimViscoelasticityTimeGReal = 29
    SimViscoelasticityTimeGImag = 30
    SimViscoelasticityTimeKReal = 31
    SimViscoelasticityTimeKImag = 32
    SimViscoelasticityTimeFreq = 33


class SimViscoelasticityPreloadType(IntEnum):
    SimViscoelasticityNONE = 0
    SimViscoelasticityUNIAXIAL = 1
    SimViscoelasticityVOLUMETRIC = 2


class SimViscoelasticityTabularSubType(IntEnum):
    SimViscoelasticityISOTROPIC = 0
    SimViscoelasticityTRACTION = 1


class SimViscoelasticityTimeType(IntEnum):
    SimViscoelasticityTIMEPRONY = 0
    SimViscoelasticityFREQUENCYDATA = 1


class SimViscoelasticityViscoelasticityDomain(IntEnum):
    SimViscoelasticityFREQUENCY = 0
    SimViscoelasticityTIME = 1


class SimVolumetricDragMaterialTableColumn(IntEnum):
    SimVolumetricDragVolumetricDrag = 0
    SimVolumetricDragFrequency = 1
    SimVolumetricDragTemperature = 2
