from enum import Enum


class SimAcousticAbsorptionMaterialTableColumn(Enum):
    SimAcousticAbsorptionMagnitude = 0
    SimAcousticAbsorptionPhase = 1
    SimAcousticAbsorptionFrequency = 2


class SimBulkModulusBulkModulusType(Enum):
    SimBulkModulusBulk_Modulus = 0
    SimBulkModulusComplex_Bulk_Modulus = 1


class SimBulkModulusMaterialTableColumn(Enum):
    SimBulkModulusRealPart = 0
    SimBulkModulusTemperature = 1
    SimBulkModulusComplexRealPart = 2
    SimBulkModulusImaginaryPart = 3
    SimBulkModulusFrequency = 4


class SimCastIronPlasticityCompressionHardeningMaterialTableColumn(Enum):
    SimCastIronPlasticitySigmaC = 0
    SimCastIronPlasticityEpsilonC = 1
    SimCastIronPlasticityTemperatureC = 2


class SimCastIronPlasticityPlasticityMaterialTableColumn(Enum):
    SimCastIronPlasticityPlasticPoissonsRatio = 0
    SimCastIronPlasticityPlasticTemperature = 1


class SimCastIronPlasticityTensionHardeningMaterialTableColumn(Enum):
    SimCastIronPlasticitySigmaT = 0
    SimCastIronPlasticityEpsilonT = 1
    SimCastIronPlasticityTemperatureT = 2


class SimConductivityConductivityType(Enum):
    SimConductivityIsotropicConductivity = 0
    SimConductivityOrthotropicConductivity = 1
    SimConductivityAnisotropicConductivity = 2


class SimConductivityMaterialTableColumn(Enum):
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


class SimDamageEvolutionCategory(Enum):
    SimDamageEvolutionDisplacement = 0
    SimDamageEvolutionEnergy = 1


class SimDamageEvolutionDegradation(Enum):
    SimDamageEvolutionMaximum = 0
    SimDamageEvolutionMultiplicative = 1


class SimDamageEvolutionMaterialTableColumn(Enum):
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


class SimDamageEvolutionSoftening(Enum):
    SimDamageEvolutionLinear = 0
    SimDamageEvolutionExponential = 1
    SimDamageEvolutionTabular = 2


class SimDamageStabilizationMaterialTableColumn(Enum):
    SimDamageStabilizationViscosityCoefficientLongitudinalTensileDirection = 0
    SimDamageStabilizationViscosityCoefficientLongitudinalCompressiveDirection = 1
    SimDamageStabilizationViscosityCoefficientTransverseTensileDirection = 2
    SimDamageStabilizationViscosityCoefficientTransverseCompressiveDirection = 3


class SimDensityMaterialTableColumn(Enum):
    SimDensityDensity = 0
    SimDensityTemperature = 1


class SimDepvarMaterialTableColumn(Enum):
    SimDepvarOutputVariableKey = 0
    SimDepvarOutputVariableDescription = 1


class SimDuctileDamageMaterialTableColumn(Enum):
    SimDuctileDamageFractureStrain = 0
    SimDuctileDamageStressTriaxiality = 1
    SimDuctileDamageStrainRate = 2
    SimDuctileDamageTemperature = 3


class SimElasticElasticType(Enum):
    SimElasticIsotropic = 0
    SimElasticOrthotropic = 1
    SimElasticEngineeringConstants = 2
    SimElasticLamina = 3
    SimElasticAnisotropic = 4
    SimElasticTransverselyIsotropic = 5


class SimElasticMaterialTableColumn(Enum):
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


class SimElasticModuliTimeScaleType(Enum):
    SimElasticLongTerm = 0
    SimElasticInstantaneous = 1


class SimElongationMaterialTableColumn(Enum):
    SimElongationElongationAtFracture = 0
    SimElongationTemperature = 1


class SimEOSEOSType(Enum):
    SimEOSIdealGas = 0
    SimEOSJWL = 1
    SimEOSUsUp = 2
    SimEOSTabular = 3


class SimEOSMaterialTableColumn(Enum):
    SimEOSf1 = 0
    SimEOSf2 = 1
    SimEOSVolumetricStrain = 2


class SimExpansionExpansionType(Enum):
    SimExpansionIsotropic = 0
    SimExpansionAnisotropic = 1
    SimExpansionOrthotropic = 2
    SimExpansionTransverselyIsotropic = 3


class SimExpansionMaterialTableColumn(Enum):
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


class SimFailStrainMaterialTableColumn(Enum):
    SimFailStrainTensileStrainFiber = 0
    SimFailStrainCompressiveStrainFiber = 1
    SimFailStrainTensileStrainFiberTransverse = 2
    SimFailStrainCompressiveStrainFiberTransverse = 3
    SimFailStrainShearStrain = 4
    SimFailStrainTemperature = 5


class SimFailStressMaterialTableColumn(Enum):
    SimFailStressTensileStressFiber = 0
    SimFailStressCompressiveStressFiber = 1
    SimFailStressTensileStressFiberTransverse = 2
    SimFailStressCompressiveStressFiberTransverse = 3
    SimFailStressShearStrength = 4
    SimFailStressCrossProductTermCoefficient = 5
    SimFailStressEquibiaxialStressLimit = 6
    SimFailStressTemperature = 7


class SimFluidCapacityInput(Enum):
    SimFluidCapacityPolynomial = 0
    SimFluidCapacityTabular = 1


class SimFluidCapacityMaterialTableColumn(Enum):
    SimFluidCapacityMolarHeat = 0
    SimFluidCapacityMolarHeatA = 1
    SimFluidCapacityMolarHeatB = 2
    SimFluidCapacityMolarHeatC = 3
    SimFluidCapacityMolarHeatD = 4
    SimFluidCapacityMolarHeatE = 5
    SimFluidCapacityTemperature = 6


class SimFluidCavityBulkModulusMaterialTableColumn(Enum):
    SimFluidCavityBulkModulusBulkModulus = 0
    SimFluidCavityBulkModulusTemperature = 1


class SimFluidCavityDensityMaterialTableColumn(Enum):
    SimFluidCavityDensityConstant = 0
    SimFluidCavityDensityTemperature = 1


class SimFluidCavityExpansionMaterialTableColumn(Enum):
    SimFluidCavityExpansionCoefficient = 0
    SimFluidCavityExpansionTemperature = 1


class SimFluidMolecularWeightMaterialTableColumn(Enum):
    SimFluidMolecularWeightConstant = 0


class SimGasketMembraneElasticMaterialTableColumn(Enum):
    SimGasketMembraneElasticYoungsModulus = 0
    SimGasketMembraneElasticPoissonsRatio = 1
    SimGasketMembraneElasticTemperature = 2


class SimGasketThicknessBehaviorBehaviorType(Enum):
    SimGasketThicknessBehaviorElasticPlastic = 0
    SimGasketThicknessBehaviorDamage = 1


class SimGasketThicknessBehaviorLoadingMaterialTableColumn(Enum):
    SimGasketThicknessBehaviorLoadPressure = 0
    SimGasketThicknessBehaviorLoadClosure = 1
    SimGasketThicknessBehaviorLoadTemperature = 2


class SimGasketThicknessBehaviorUnloadingMaterialTableColumn(Enum):
    SimGasketThicknessBehaviorUnloadPressure = 0
    SimGasketThicknessBehaviorUnloadClosure = 1
    SimGasketThicknessBehaviorUnloadPlasticClosure = 2
    SimGasketThicknessBehaviorUnloadTemperature = 3


class SimGasketTransverseShearElasticMaterialTableColumn(Enum):
    SimGasketTransverseShearElasticShearStiffness = 0
    SimGasketTransverseShearElasticTemperature = 1


class SimGasketTransverseShearElasticUnitType(Enum):
    SimGasketTransverseShearElasticStress = 0
    SimGasketTransverseShearElasticForce = 1


class SimHashinDamageEvolutionCondition(Enum):
    SimHashinDamageEvolutionEnergy = 0


class SimHashinDamageEvolutionMaterialTableColumn(Enum):
    SimHashinDamageEvolutionLongitudinalTensileFractureEnergy = 0
    SimHashinDamageEvolutionLongitudinalCompressiveFractureEnergy = 1
    SimHashinDamageEvolutionTransverseTensileFractureEnergy = 2
    SimHashinDamageEvolutionTransverseCompressiveFractureEnergy = 3
    SimHashinDamageEvolutionTemperature = 4


class SimHashinDamageEvolutionSofteningResponse(Enum):
    SimHashinDamageEvolutionLinear = 0


class SimHashinDamageMaterialTableColumn(Enum):
    SimHashinDamageLongitudinalTensileStrength = 0
    SimHashinDamageLongitudinalCompressiveStrength = 1
    SimHashinDamageTransverseTensileStrength = 2
    SimHashinDamageTransverseCompressiveStrength = 3
    SimHashinDamageLongitudinalShearStrength = 4
    SimHashinDamageTransverseShearStrength = 5
    SimHashinDamageTemperature = 6


class SimHeatGenerationUserDefinedMaterialTableColumn(Enum):
    SimHeatGenerationUserDefinedProperties = 0


class SimHyperelasticityMaterialTableColumn(Enum):
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


class SimHyperelasticityModuliTimeScale(Enum):
    SimHyperelasticityLongTerm = 0
    SimHyperelasticityInstantaneous = 1


class SimHyperelasticityStrainEnergyPotentialOrder(Enum):
    SimHyperelasticityN1 = 0
    SimHyperelasticityN2 = 1
    SimHyperelasticityN3 = 2
    SimHyperelasticityN4 = 3
    SimHyperelasticityN5 = 4
    SimHyperelasticityN6 = 5


class SimHyperelasticityStrainEnergyPotential(Enum):
    SimHyperelasticityArruda_Boyce = 0
    SimHyperelasticityNeo_Hooke = 1
    SimHyperelasticityOgden = 2
    SimHyperelasticityPolynomial = 3
    SimHyperelasticityReduced_Polynomial = 4
    SimHyperelasticityMooney_Rivlin = 5
    SimHyperelasticityVan_Der_Waals = 6
    SimHyperelasticityYeoh = 7


class SimHyperfoamMaterialTableColumn(Enum):
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


class SimHyperfoamModuliTimeScale(Enum):
    SimHyperfoamLONG_TERM = 0
    SimHyperfoamINSTANTANEOUS = 1


class SimHyperfoamStrainEnergyPotentialOrder(Enum):
    SimHyperfoamN1 = 0
    SimHyperfoamN2 = 1
    SimHyperfoamN3 = 2
    SimHyperfoamN4 = 3
    SimHyperfoamN5 = 4
    SimHyperfoamN6 = 5


class SimLatentHeatMaterialTableColumn(Enum):
    SimLatentHeatLatentHeat = 0
    SimLatentHeatSolidusTemperature = 1
    SimLatentHeatLiquidusTemperature = 2


class SimMaterialTableOptionalColumn(Enum):
    SimMaterialTableStrainRate = 0
    SimMaterialTableFrequency = 1
    SimMaterialTableTemperature = 2


class SimPlasticIsotropicMaterialTableColumn(Enum):
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


class SimPlasticKinematicMaterialTableColumn(Enum):
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


class SimPlasticPlasticHardening(Enum):
    SimPlasticIsotropic_Tabular = 0
    SimPlasticIsotropic_JohnsonCook = 1
    SimPlasticKinematic = 2
    SimPlasticCombined_Tabular = 3
    SimPlasticCombined_Exponential = 4


class SimPlasticPlasticYieldCriteria(Enum):
    SimPlasticMises = 0
    SimPlasticHill = 1


class SimPlasticPotentialMaterialTableColumn(Enum):
    SimPlasticR11 = 0
    SimPlasticR22 = 1
    SimPlasticR33 = 2
    SimPlasticR12 = 3
    SimPlasticR13 = 4
    SimPlasticR23 = 5
    SimPlasticPotentialTemperature = 6


class SimPorousElasticityMaterialTableColumn(Enum):
    SimPorousElasticityLogBulkModulus = 0
    SimPorousElasticityShearModulus = 1
    SimPorousElasticityPoissonRatio = 2
    SimPorousElasticityTensileLimit = 3
    SimPorousElasticityTemperature = 4


class SimPorousElasticityShearType(Enum):
    SimPorousElasticityG = 0
    SimPorousElasticityPoisson = 1


class SimProofStressMaterialTableColumn(Enum):
    SimProofStressProofStressAt2PC = 0
    SimProofStressTemperature = 1


class SimRateDependentHardeningType(Enum):
    SimPowerlaw = 0
    SimYieldRatio = 1
    SimJohnsonCook = 2


class SimRateDependentMaterialTableColumn(Enum):
    SimRateDependentMultiplier = 0
    SimRateDependentExponent = 1
    SimRateDependentYieldStressRatio = 2
    SimRateDependentEquivalentPlasticStrainRate = 3
    SimRateDependentTemperature = 4


class SimSpecificHeatMaterialTableColumn(Enum):
    SimSpecificHeatSpecificHeat = 0
    SimSpecificHeatTemperature = 1


class SimSpecificHeatSpecificHeatType(Enum):
    SimSpecificHeatConstantVolume = 0
    SimSpecificHeatConstantPressure = 1


class SimTensileFailureCriteria(Enum):
    SimNone = 0
    SimBrittle = 1
    SimDuctile = 2


class SimTensileFailureMaterialTableColumn(Enum):
    SimTensileFailureHydroStaticCutOffStress = 0
    SimTensileFailureTemperature = 1


class SimUltimateStrengthMaterialCompressiveTableColumn(Enum):
    SimUltimateStrengthUltimateCompressiveStrength = 0
    SimUltimateStrengthCompressiveTemperature = 1


class SimUltimateStrengthMaterialTensileTableColumn(Enum):
    SimUltimateStrengthUltimateTensileStrength = 0
    SimUltimateStrengthTensileTemperature = 1


class SimUserDefinedFieldDirectSpecificationTableColumn(Enum):
    SimUserDefinedFieldVariableNum = 0
    SimUserDefinedFieldVariableName = 1


class SimUserDefinedFieldRedefinitionResource(Enum):
    SimUserDefinedFieldUserSubroutineRedefinition = 0
    SimUserDefinedFieldDirectSpecificationRedefinition = 1


class SimUserDefinedHybridFormulation(Enum):
    SimUserDefinedIncremental = 0
    SimUserDefinedTotal = 1
    SimUserDefinedIncompressible = 2


class SimUserDefinedMaterialTableColumn(Enum):
    SimUserDefinedMechanicalConstants = 0
    SimUserDefinedThermalConstants = 1


class SimUserDefinedPhysics(Enum):
    SimUserDefinedMechanical = 0
    SimUserDefinedThermal = 1
    SimUserDefinedThermoMechanical = 2


class SimViscoelasticityFrequencyType(Enum):
    SimViscoelasticityFORMULA = 0
    SimViscoelasticityPRONY = 1
    SimViscoelasticityTABULAR = 2


class SimViscoelasticityMaterialTableColumn(Enum):
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


class SimViscoelasticityPreloadType(Enum):
    SimViscoelasticityNONE = 0
    SimViscoelasticityUNIAXIAL = 1
    SimViscoelasticityVOLUMETRIC = 2


class SimViscoelasticityTabularSubType(Enum):
    SimViscoelasticityISOTROPIC = 0
    SimViscoelasticityTRACTION = 1


class SimViscoelasticityTimeType(Enum):
    SimViscoelasticityTIMEPRONY = 0
    SimViscoelasticityFREQUENCYDATA = 1


class SimViscoelasticityViscoelasticityDomain(Enum):
    SimViscoelasticityFREQUENCY = 0
    SimViscoelasticityTIME = 1


class SimVolumetricDragMaterialTableColumn(Enum):
    SimVolumetricDragVolumetricDrag = 0
    SimVolumetricDragFrequency = 1
    SimVolumetricDragTemperature = 2
