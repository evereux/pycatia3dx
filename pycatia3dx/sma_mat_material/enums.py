from enum import Enum


class SimAcousticAbsorptionMaterialTableColumn(Enum):
    SimAcousticAbsorptionPhase = 0
    SimAcousticAbsorptionFrequency = 1
    SimAcousticAbsorptionMagnitude = 2


class SimBulkModulusBulkModulusType(Enum):
    SimBulkModulusComplex_Bulk_Modulus = 0
    SimBulkModulusBulk_Modulus = 1


class SimBulkModulusMaterialTableColumn(Enum):
    SimBulkModulusRealPart = 0
    SimBulkModulusTemperature = 1
    SimBulkModulusComplexRealPart = 2
    SimBulkModulusImaginaryPart = 3
    SimBulkModulusFrequency = 4


class SimCastIronPlasticityCompressionHardeningMaterialTableColumn(Enum):
    SimCastIronPlasticityEpsilonC = 0
    SimCastIronPlasticitySigmaC = 1
    SimCastIronPlasticityTemperatureC = 2


class SimCastIronPlasticityPlasticityMaterialTableColumn(Enum):
    SimCastIronPlasticityPlasticTemperature = 0
    SimCastIronPlasticityPlasticPoissonsRatio = 1


class SimCastIronPlasticityTensionHardeningMaterialTableColumn(Enum):
    SimCastIronPlasticityTemperatureT = 0
    SimCastIronPlasticitySigmaT = 1
    SimCastIronPlasticityEpsilonT = 2


class SimConductivityConductivityType(Enum):
    SimConductivityOrthotropicConductivity = 0
    SimConductivityIsotropicConductivity = 1
    SimConductivityAnisotropicConductivity = 2


class SimConductivityMaterialTableColumn(Enum):
    SimConductivityK3 = 0
    SimConductivityTemperature = 1
    SimConductivityK11 = 2
    SimConductivityK12 = 3
    SimConductivityK13 = 4
    SimConductivityK1 = 5
    SimConductivityK33 = 6
    SimConductivityK2 = 7
    SimConductivityK22 = 8
    SimConductivityK23 = 9
    SimConductivityThermalConductivity = 10


class SimDamageEvolutionCategory(Enum):
    SimDamageEvolutionEnergy = 0
    SimDamageEvolutionDisplacement = 1


class SimDamageEvolutionDegradation(Enum):
    SimDamageEvolutionMultiplicative = 0
    SimDamageEvolutionMaximum = 1


class SimDamageEvolutionMaterialTableColumn(Enum):
    SimDamageEvolutionTransverseCompressiveFractureEnergy = 0
    SimDamageEvolutionLongitudinalCompressiveFractureEnergy = 1
    SimDamageEvolutionTemperature = 2
    SimDamageEvolutionExponentialLawParameter = 3
    SimDamageEvolutionDisplacementAtFailure = 4
    SimDamageEvolutionLongitudinalTensileFractureEnergy = 5
    SimDamageEvolutionFractureEnergy = 6
    SimDamageEvolutionDamageVariable = 7
    SimDamageEvolutionDisplacementTabular = 8
    SimDamageEvolutionTransverseTensileFractureEnergy = 9


class SimDamageEvolutionSoftening(Enum):
    SimDamageEvolutionExponential = 0
    SimDamageEvolutionTabular = 1
    SimDamageEvolutionLinear = 2


class SimDamageStabilizationMaterialTableColumn(Enum):
    SimDamageStabilizationViscosityCoefficientTransverseCompressiveDirection = 0
    SimDamageStabilizationViscosityCoefficientLongitudinalTensileDirection = 1
    SimDamageStabilizationViscosityCoefficientLongitudinalCompressiveDirection = 2
    SimDamageStabilizationViscosityCoefficientTransverseTensileDirection = 3


class SimDensityMaterialTableColumn(Enum):
    SimDensityTemperature = 0
    SimDensityDensity = 1


class SimDepvarMaterialTableColumn(Enum):
    SimDepvarOutputVariableKey = 0
    SimDepvarOutputVariableDescription = 1


class SimDuctileDamageMaterialTableColumn(Enum):
    SimDuctileDamageTemperature = 0
    SimDuctileDamageFractureStrain = 1
    SimDuctileDamageStressTriaxiality = 2
    SimDuctileDamageStrainRate = 3


class SimElasticElasticType(Enum):
    SimElasticAnisotropic = 0
    SimElasticEngineeringConstants = 1
    SimElasticTransverselyIsotropic = 2
    SimElasticLamina = 3
    SimElasticIsotropic = 4
    SimElasticOrthotropic = 5


class SimElasticMaterialTableColumn(Enum):
    SimElasticD2213 = 0
    SimElasticE2 = 1
    SimElasticParallelYoungModulus = 2
    SimElasticParallelPoissonsRatio = 3
    SimElasticD3313 = 4
    SimElasticD3333 = 5
    SimElasticD1323 = 6
    SimElasticD2222 = 7
    SimElasticG23 = 8
    SimElasticD1112 = 9
    SimElasticG12 = 10
    SimElasticNu23 = 11
    SimElasticD1113 = 12
    SimElasticD1223 = 13
    SimElasticD3323 = 14
    SimElasticPoissonsRatio = 15
    SimElasticE3 = 16
    SimElasticD1111 = 17
    SimElasticD1313 = 18
    SimElasticD2212 = 19
    SimElasticNu12 = 20
    SimElasticD2323 = 21
    SimElasticD1122 = 22
    SimElasticTemperature = 23
    SimElasticD3312 = 24
    SimElasticNormalYoungModulus = 25
    SimElasticD2223 = 26
    SimElasticD1133 = 27
    SimElasticE1 = 28
    SimElasticG13 = 29
    SimElasticD1123 = 30
    SimElasticYoungsModulus = 31
    SimElasticD2233 = 32
    SimElasticD1213 = 33
    SimElasticNormalPoissonsRatio = 34
    SimElasticParallelShearModulus = 35
    SimElasticNu13 = 36
    SimElasticD1212 = 37


class SimElasticModuliTimeScaleType(Enum):
    SimElasticLongTerm = 0
    SimElasticInstantaneous = 1


class SimElongationMaterialTableColumn(Enum):
    SimElongationTemperature = 0
    SimElongationElongationAtFracture = 1


class SimEOSEOSType(Enum):
    SimEOSTabular = 0
    SimEOSUsUp = 1
    SimEOSJWL = 2
    SimEOSIdealGas = 3


class SimEOSMaterialTableColumn(Enum):
    SimEOSf1 = 0
    SimEOSVolumetricStrain = 1
    SimEOSf2 = 2


class SimExpansionExpansionType(Enum):
    SimExpansionAnisotropic = 0
    SimExpansionTransverselyIsotropic = 1
    SimExpansionIsotropic = 2
    SimExpansionOrthotropic = 3


class SimExpansionMaterialTableColumn(Enum):
    SimExpansionAlpha = 0
    SimExpansionAlpha11 = 1
    SimExpansionAlpha23 = 2
    SimExpansionParallelExpansionCoeff = 3
    SimExpansionNormalExpansionCoeff = 4
    SimExpansionTemperature = 5
    SimExpansionAlpha33 = 6
    SimExpansionAlpha13 = 7
    SimExpansionAlpha22 = 8
    SimExpansionAlpha12 = 9


class SimFailStrainMaterialTableColumn(Enum):
    SimFailStrainCompressiveStrainFiber = 0
    SimFailStrainShearStrain = 1
    SimFailStrainCompressiveStrainFiberTransverse = 2
    SimFailStrainTensileStrainFiberTransverse = 3
    SimFailStrainTemperature = 4
    SimFailStrainTensileStrainFiber = 5


class SimFailStressMaterialTableColumn(Enum):
    SimFailStressEquibiaxialStressLimit = 0
    SimFailStressTemperature = 1
    SimFailStressCrossProductTermCoefficient = 2
    SimFailStressCompressiveStressFiber = 3
    SimFailStressTensileStressFiberTransverse = 4
    SimFailStressCompressiveStressFiberTransverse = 5
    SimFailStressTensileStressFiber = 6
    SimFailStressShearStrength = 7


class SimFluidCapacityInput(Enum):
    SimFluidCapacityPolynomial = 0
    SimFluidCapacityTabular = 1


class SimFluidCapacityMaterialTableColumn(Enum):
    SimFluidCapacityMolarHeatC = 0
    SimFluidCapacityMolarHeatD = 1
    SimFluidCapacityMolarHeat = 2
    SimFluidCapacityMolarHeatB = 3
    SimFluidCapacityMolarHeatE = 4
    SimFluidCapacityTemperature = 5
    SimFluidCapacityMolarHeatA = 6


class SimFluidCavityBulkModulusMaterialTableColumn(Enum):
    SimFluidCavityBulkModulusTemperature = 0
    SimFluidCavityBulkModulusBulkModulus = 1


class SimFluidCavityDensityMaterialTableColumn(Enum):
    SimFluidCavityDensityConstant = 0
    SimFluidCavityDensityTemperature = 1


class SimFluidCavityExpansionMaterialTableColumn(Enum):
    SimFluidCavityExpansionTemperature = 0
    SimFluidCavityExpansionCoefficient = 1


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
    SimGasketThicknessBehaviorLoadTemperature = 0
    SimGasketThicknessBehaviorLoadPressure = 1
    SimGasketThicknessBehaviorLoadClosure = 2


class SimGasketThicknessBehaviorUnloadingMaterialTableColumn(Enum):
    SimGasketThicknessBehaviorUnloadPressure = 0
    SimGasketThicknessBehaviorUnloadClosure = 1
    SimGasketThicknessBehaviorUnloadPlasticClosure = 2
    SimGasketThicknessBehaviorUnloadTemperature = 3


class SimGasketTransverseShearElasticMaterialTableColumn(Enum):
    SimGasketTransverseShearElasticShearStiffness = 0
    SimGasketTransverseShearElasticTemperature = 1


class SimGasketTransverseShearElasticUnitType(Enum):
    SimGasketTransverseShearElasticForce = 0
    SimGasketTransverseShearElasticStress = 1


class SimHashinDamageEvolutionCondition(Enum):
    SimHashinDamageEvolutionEnergy = 0


class SimHashinDamageEvolutionMaterialTableColumn(Enum):
    SimHashinDamageEvolutionTransverseCompressiveFractureEnergy = 0
    SimHashinDamageEvolutionTemperature = 1
    SimHashinDamageEvolutionLongitudinalTensileFractureEnergy = 2
    SimHashinDamageEvolutionTransverseTensileFractureEnergy = 3
    SimHashinDamageEvolutionLongitudinalCompressiveFractureEnergy = 4


class SimHashinDamageEvolutionSofteningResponse(Enum):
    SimHashinDamageEvolutionLinear = 0


class SimHashinDamageMaterialTableColumn(Enum):
    SimHashinDamageLongitudinalShearStrength = 0
    SimHashinDamageTemperature = 1
    SimHashinDamageTransverseCompressiveStrength = 2
    SimHashinDamageTransverseShearStrength = 3
    SimHashinDamageLongitudinalTensileStrength = 4
    SimHashinDamageLongitudinalCompressiveStrength = 5
    SimHashinDamageTransverseTensileStrength = 6


class SimHeatGenerationUserDefinedMaterialTableColumn(Enum):
    SimHeatGenerationUserDefinedProperties = 0


class SimHyperelasticityMaterialTableColumn(Enum):
    SimHyperelasticityLamdaM = 0
    SimHyperelasticityC05 = 1
    SimHyperelasticityC41 = 2
    SimHyperelasticityD5 = 3
    SimHyperelasticityC40 = 4
    SimHyperelasticityMu6 = 5
    SimHyperelasticityAlpha1 = 6
    SimHyperelasticityC50 = 7
    SimHyperelasticityC21 = 8
    SimHyperelasticityC30 = 9
    SimHyperelasticityC10 = 10
    SimHyperelasticityC12 = 11
    SimHyperelasticityC42 = 12
    SimHyperelasticityMu4 = 13
    SimHyperelasticityC51 = 14
    SimHyperelasticityMu3 = 15
    SimHyperelasticityC02 = 16
    SimHyperelasticityAlpha = 17
    SimHyperelasticityD3 = 18
    SimHyperelasticityD6 = 19
    SimHyperelasticityD = 20
    SimHyperelasticityC11 = 21
    SimHyperelasticityD4 = 22
    SimHyperelasticityC04 = 23
    SimHyperelasticityC14 = 24
    SimHyperelasticityMu = 25
    SimHyperelasticityC23 = 26
    SimHyperelasticityC31 = 27
    SimHyperelasticityD2 = 28
    SimHyperelasticityC15 = 29
    SimHyperelasticityC22 = 30
    SimHyperelasticityAlpha5 = 31
    SimHyperelasticityC03 = 32
    SimHyperelasticityMu5 = 33
    SimHyperelasticityC33 = 34
    SimHyperelasticityAlpha6 = 35
    SimHyperelasticityD1 = 36
    SimHyperelasticityC32 = 37
    SimHyperelasticityC24 = 38
    SimHyperelasticityAlpha4 = 39
    SimHyperelasticityC60 = 40
    SimHyperelasticityBeta = 41
    SimHyperelasticityAlpha2 = 42
    SimHyperelasticityMu2 = 43
    SimHyperelasticityC13 = 44
    SimHyperelasticityLambdaM = 45
    SimHyperelasticityAlpha3 = 46
    SimHyperelasticityC06 = 47
    SimHyperelasticityC01 = 48
    SimHyperelasticityTemperature = 49
    SimHyperelasticityMu1 = 50
    SimHyperelasticityC20 = 51


class SimHyperelasticityModuliTimeScale(Enum):
    SimHyperelasticityInstantaneous = 0
    SimHyperelasticityLongTerm = 1


class SimHyperelasticityStrainEnergyPotentialOrder(Enum):
    SimHyperelasticityN2 = 0
    SimHyperelasticityN6 = 1
    SimHyperelasticityN5 = 2
    SimHyperelasticityN1 = 3
    SimHyperelasticityN4 = 4
    SimHyperelasticityN3 = 5


class SimHyperelasticityStrainEnergyPotential(Enum):
    SimHyperelasticityReduced_Polynomial = 0
    SimHyperelasticityArruda_Boyce = 1
    SimHyperelasticityYeoh = 2
    SimHyperelasticityNeo_Hooke = 3
    SimHyperelasticityMooney_Rivlin = 4
    SimHyperelasticityOgden = 5
    SimHyperelasticityPolynomial = 6
    SimHyperelasticityVan_Der_Waals = 7


class SimHyperfoamMaterialTableColumn(Enum):
    SimHyperfoamnu6 = 0
    SimHyperfoamalpha3 = 1
    SimHyperfoamnu4 = 2
    SimHyperfoamalpha4 = 3
    SimHyperfoamalpha5 = 4
    SimHyperfoamnu2 = 5
    SimHyperfoammu1 = 6
    SimHyperfoamalpha2 = 7
    SimHyperfoamnu1 = 8
    SimHyperfoamalpha1 = 9
    SimHyperfoammu4 = 10
    SimHyperfoammu3 = 11
    SimHyperfoammu6 = 12
    SimHyperfoamnu3 = 13
    SimHyperfoamTemperature = 14
    SimHyperfoammu5 = 15
    SimHyperfoamnu5 = 16
    SimHyperfoammu2 = 17
    SimHyperfoamalpha6 = 18


class SimHyperfoamModuliTimeScale(Enum):
    SimHyperfoamINSTANTANEOUS = 0
    SimHyperfoamLONG_TERM = 1


class SimHyperfoamStrainEnergyPotentialOrder(Enum):
    SimHyperfoamN2 = 0
    SimHyperfoamN4 = 1
    SimHyperfoamN3 = 2
    SimHyperfoamN5 = 3
    SimHyperfoamN1 = 4
    SimHyperfoamN6 = 5


class SimLatentHeatMaterialTableColumn(Enum):
    SimLatentHeatLiquidusTemperature = 0
    SimLatentHeatSolidusTemperature = 1
    SimLatentHeatLatentHeat = 2


class SimMaterialTableOptionalColumn(Enum):
    SimMaterialTableFrequency = 0
    SimMaterialTableTemperature = 1
    SimMaterialTableStrainRate = 2


class SimPlasticIsotropicMaterialTableColumn(Enum):
    SimPlasticn = 0
    SimPlasticHardeningParam_b = 1
    SimPlasticIsotropicYieldStressCombined = 2
    SimPlasticIsotropicPlasticStrainCombined = 3
    SimPlasticIsotropicStrainRate = 4
    SimPlasticm = 5
    SimPlasticMeltingTemp = 6
    SimPlasticTransitionTemp = 7
    SimPlasticB = 8
    SimPlasticA = 9
    SimPlasticIsotropicPlasticStrain = 10
    SimPlasticIsotropicYieldStress = 11
    SimPlasticIsotropicTemperature = 12
    SimPlasticQ_Infinity = 13


class SimPlasticKinematicMaterialTableColumn(Enum):
    SimPlasticGamma10 = 0
    SimPlasticGamma7 = 1
    SimPlasticC1 = 2
    SimPlasticGamma6 = 3
    SimPlasticC5 = 4
    SimPlasticC9 = 5
    SimPlasticC7 = 6
    SimPlasticGamma2 = 7
    SimPlasticKinematicTemperature = 8
    SimPlasticC6 = 9
    SimPlasticGamma8 = 10
    SimPlasticGamma3 = 11
    SimPlasticC4 = 12
    SimPlasticC2 = 13
    SimPlasticGamma4 = 14
    SimPlasticC3 = 15
    SimPlasticC10 = 16
    SimPlasticGamma5 = 17
    SimPlasticKinematicYieldStress = 18
    SimPlasticGamma9 = 19
    SimPlasticC8 = 20
    SimPlasticGamma1 = 21


class SimPlasticPlasticHardening(Enum):
    SimPlasticKinematic = 0
    SimPlasticCombined_Exponential = 1
    SimPlasticIsotropic_Tabular = 2
    SimPlasticCombined_Tabular = 3
    SimPlasticIsotropic_JohnsonCook = 4


class SimPlasticPlasticYieldCriteria(Enum):
    SimPlasticHill = 0
    SimPlasticMises = 1


class SimPlasticPotentialMaterialTableColumn(Enum):
    SimPlasticR11 = 0
    SimPlasticPotentialTemperature = 1
    SimPlasticR22 = 2
    SimPlasticR33 = 3
    SimPlasticR23 = 4
    SimPlasticR13 = 5
    SimPlasticR12 = 6


class SimPorousElasticityMaterialTableColumn(Enum):
    SimPorousElasticityLogBulkModulus = 0
    SimPorousElasticityTensileLimit = 1
    SimPorousElasticityPoissonRatio = 2
    SimPorousElasticityTemperature = 3
    SimPorousElasticityShearModulus = 4


class SimPorousElasticityShearType(Enum):
    SimPorousElasticityG = 0
    SimPorousElasticityPoisson = 1


class SimProofStressMaterialTableColumn(Enum):
    SimProofStressProofStressAt2PC = 0
    SimProofStressTemperature = 1


class SimRateDependentHardeningType(Enum):
    SimJohnsonCook = 0
    SimPowerlaw = 1
    SimYieldRatio = 2


class SimRateDependentMaterialTableColumn(Enum):
    SimRateDependentMultiplier = 0
    SimRateDependentYieldStressRatio = 1
    SimRateDependentExponent = 2
    SimRateDependentTemperature = 3
    SimRateDependentEquivalentPlasticStrainRate = 4


class SimSpecificHeatMaterialTableColumn(Enum):
    SimSpecificHeatSpecificHeat = 0
    SimSpecificHeatTemperature = 1


class SimSpecificHeatSpecificHeatType(Enum):
    SimSpecificHeatConstantPressure = 0
    SimSpecificHeatConstantVolume = 1


class SimTensileFailureCriteria(Enum):
    SimDuctile = 0
    SimBrittle = 1
    SimNone = 2


class SimTensileFailureMaterialTableColumn(Enum):
    SimTensileFailureHydroStaticCutOffStress = 0
    SimTensileFailureTemperature = 1


class SimUltimateStrengthMaterialCompressiveTableColumn(Enum):
    SimUltimateStrengthUltimateCompressiveStrength = 0
    SimUltimateStrengthCompressiveTemperature = 1


class SimUltimateStrengthMaterialTensileTableColumn(Enum):
    SimUltimateStrengthTensileTemperature = 0
    SimUltimateStrengthUltimateTensileStrength = 1


class SimUserDefinedFieldDirectSpecificationTableColumn(Enum):
    SimUserDefinedFieldVariableNum = 0
    SimUserDefinedFieldVariableName = 1


class SimUserDefinedFieldRedefinitionResource(Enum):
    SimUserDefinedFieldDirectSpecificationRedefinition = 0
    SimUserDefinedFieldUserSubroutineRedefinition = 1


class SimUserDefinedHybridFormulation(Enum):
    SimUserDefinedTotal = 0
    SimUserDefinedIncompressible = 1
    SimUserDefinedIncremental = 2


class SimUserDefinedMaterialTableColumn(Enum):
    SimUserDefinedThermalConstants = 0
    SimUserDefinedMechanicalConstants = 1


class SimUserDefinedPhysics(Enum):
    SimUserDefinedThermal = 0
    SimUserDefinedMechanical = 1
    SimUserDefinedThermoMechanical = 2


class SimViscoelasticityFrequencyType(Enum):
    SimViscoelasticityTABULAR = 0
    SimViscoelasticityPRONY = 1
    SimViscoelasticityFORMULA = 2


class SimViscoelasticityMaterialTableColumn(Enum):
    SimViscoelasticityIsotropicPreloadVolumetricFreq = 0
    SimViscoelasticityTractionPreloadUniaxialStorageModulus = 1
    SimViscoelasticityA = 2
    SimViscoelasticityTimeFreq = 3
    SimViscoelasticityIsotropicPreloadNoneKImag = 4
    SimViscoelasticityTractionPreloadNoneNormLossModulus = 5
    SimViscoelasticityIsotropicPreloadUniaxialStorageModulus = 6
    SimViscoelasticityPronyK = 7
    SimViscoelasticityRealG1 = 8
    SimViscoelasticityB = 9
    SimViscoelasticityTractionPreloadUniaxialFreq = 10
    SimViscoelasticityPronyTAU = 11
    SimViscoelasticityIsotropicPreloadVolumetricStorageModulus = 12
    SimViscoelasticityTimeKReal = 13
    SimViscoelasticityIsotropicPreloadNoneKReal = 14
    SimViscoelasticityIsotropicPreloadUniaxialFreq = 15
    SimViscoelasticityTractionPreloadNoneNormStorageModulus = 16
    SimViscoelasticityPronyG = 17
    SimViscoelasticityTimeGImag = 18
    SimViscoelasticityTractionPreloadUniaxialClosure = 19
    SimViscoelasticityRealK1 = 20
    SimViscoelasticityIsotropicPreloadUniaxialStrain = 21
    SimViscoelasticityImagK1 = 22
    SimViscoelasticityIsotropicPreloadVolumetricVolumeRatio = 23
    SimViscoelasticityIsotropicPreloadNoneFreq = 24
    SimViscoelasticityIsotropicPreloadVolumetricLossModulus = 25
    SimViscoelasticityIsotropicPreloadNoneGImag = 26
    SimViscoelasticityIsotropicPreloadNoneGReal = 27
    SimViscoelasticityImagG1 = 28
    SimViscoelasticityTractionPreloadUniaxialLossModulus = 29
    SimViscoelasticityTimeKImag = 30
    SimViscoelasticityTractionPreloadNoneFreq = 31
    SimViscoelasticityTimeGReal = 32
    SimViscoelasticityIsotropicPreloadUniaxialLossModulus = 33


class SimViscoelasticityPreloadType(Enum):
    SimViscoelasticityNONE = 0
    SimViscoelasticityVOLUMETRIC = 1
    SimViscoelasticityUNIAXIAL = 2


class SimViscoelasticityTabularSubType(Enum):
    SimViscoelasticityTRACTION = 0
    SimViscoelasticityISOTROPIC = 1


class SimViscoelasticityTimeType(Enum):
    SimViscoelasticityTIMEPRONY = 0
    SimViscoelasticityFREQUENCYDATA = 1


class SimViscoelasticityViscoelasticityDomain(Enum):
    SimViscoelasticityTIME = 0
    SimViscoelasticityFREQUENCY = 1


class SimVolumetricDragMaterialTableColumn(Enum):
    SimVolumetricDragTemperature = 0
    SimVolumetricDragFrequency = 1
    SimVolumetricDragVolumetricDrag = 2


