from enum import Enum


class SimBeamProfileShape(Enum):
    SimBeamProfileRectangular = 0
    SimBeamProfileCircular = 1
    SimBeamProfileNone = 2
    SimBeamProfileHex = 3
    SimBeamProfilePipe = 4
    SimBeamProfileGeneral = 5
    SimBeamProfileBox = 6
    SimBeamProfileTrapezoid = 7
    SimBeamProfileL_Beam = 8
    SimBeamProfileChannel = 9
    SimBeamProfileI_Beam = 10
    SimBeamProfileHat = 11
    SimBeamProfileT_Beam = 12


class SimBeamSectionCrossSectionAxis(Enum):
    SimBeamSectionFirstAxis = 0
    SimBeamSectionSecondAxis = 1


class SimBeamSectionOrientation(Enum):
    SimBeamSectionGeometry = 0
    SimBeamSectionAxisSystem = 1


class SimBeamSectionSlendernessOption(Enum):
    SimBeamSectionSpecify = 0
    SimBeamSectionDefault = 1


class SimBeamSectionTransverseShearStiffness(Enum):
    SimBeamSectionNone = 0
    SimBeamSectionIsotropic = 1
    SimBeamSectionCalculate = 2
    SimBeamSectionOrthotropic = 3


class SimCohesiveMechanicalResponse(Enum):
    TractionSeparation = 0
    Gasket = 1
    Continuum = 2


class SimCompositeLayupType(Enum):
    SimLayupByLamina = 0
    SimLayupByPly = 1
    SimFromDesign = 2


class SimCompositeRosetteTransferCylindricalType(Enum):
    SimCompositeCylindericalNinety = 0
    SimCompositeCylindericalZero = 1


class SimCompositeRosetteTransferType(Enum):
    SimCompositeRosetteTypeGuidedCurve = 0
    SimCompositeRosetteTypeCartesian = 1


class SimCompositeShellSectionOffsetMethod(Enum):
    SimCompositeShellSectionFromSolid = 0
    SimCompositeShellSectionTopSurface = 1
    SimCompositeShellSectionNone = 2
    SimCompositeShellSectionBottomSurface = 3
    SimCompositeShellSectionAutomaticOffset = 4
    SimCompositeShellSectionSpecifiedDistanceOffset = 5
    SimCompositeShellSectionThicknessRatio = 6


class SimConnectorCouplingType(Enum):
    SimConnectorCouplingKinematic = 0
    SimConnectorCouplingDistributing = 1


class SimConnectorElasticityElasticityOrder(Enum):
    SimConnectorElasticityNonLinear = 0
    SimConnectorElasticityLinear = 1


class SimConnectorElasticityTableColumn(Enum):
    SimConnectorElasticityTemperature = 0
    SimConnectorElasticityPosition = 1
    SimConnectorElasticityStiffness = 2


class SimConnectorSectionAssembledConnectorType(Enum):
    SimConnectorSectionWeld = 0
    SimConnectorSectionNoAssembledType = 1
    SimConnectorSectionBeam = 2
    SimConnectorSectionCVJoint = 3
    SimConnectorSectionUJoint = 4
    SimConnectorSectionRetractor = 5
    SimConnectorSectionPlanar = 6
    SimConnectorSectionTranslator = 7
    SimConnectorSectionSlipring = 8
    SimConnectorSectionCylindrical = 9
    SimConnectorSectionBushing = 10
    SimConnectorSectionHinge = 11


class SimConnectorSectionRotationalConnectorType(Enum):
    SimConnectorSectionFlowConverter = 0
    SimConnectorSectionProjectionFlexionTorsion = 1
    SimConnectorSectionNoRotationalType = 2
    SimConnectorSectionRotationAccelerometer = 3
    SimConnectorSectionUniversal = 4
    SimConnectorSectionCardan = 5
    SimConnectorSectionEuler = 6
    SimConnectorSectionFlexionTorsion = 7
    SimConnectorSectionConstantVelocity = 8
    SimConnectorSectionAlign = 9
    SimConnectorSectionRotation = 10
    SimConnectorSectionRevolute = 11


class SimConnectorSectionTranslationalConnectorType(Enum):
    SimConnectorSectionAccelerometer = 0
    SimConnectorSectionLink = 1
    SimConnectorSectionCartesian = 2
    SimConnectorSectionRadialThrust = 3
    SimConnectorSectionSlot = 4
    SimConnectorSectionNoTranslationalType = 5
    SimConnectorSectionJoin = 6
    SimConnectorSectionProjectionCartesian = 7
    SimConnectorSectionSlidePlane = 8
    SimConnectorSectionAxialConnector = 9


class SimContactVirtualPartReferencePointInputMode(Enum):
    SimContactVirtualPartCenterOfMass = 0
    SimContactVirtualPartSpecify = 1
    SimContactVirtualPartAutomatic = 2


class SimConversionType(Enum):
    SimParticlesPerDirection = 0
    SimBackgroundGrid = 1


class SimCouplingCouplingType(Enum):
    SimCouplingKinematic = 0
    SimCouplingDistributing = 1
    SimCouplingMultiphysics = 2


class SimEulerianMaterialLocation(Enum):
    SimMLOutsideSupport = 0
    SimMLInsideSupport = 1


class SimEulerianVolumeFractionType(Enum):
    SimVFTComputed = 0
    SimVFTSpecified = 1


class SimFunctionOrder(Enum):
    SimSecond = 0
    SimThird = 1
    SimFifth = 2


class SimLaminateStackingType(Enum):
    SimCompositeLaminateStackingUnknown = 0
    SimCompositeLaminateStackingStackingSequence = 1
    SimCompositeLaminateStackingThicknessLaw = 2


class SimLaminateSymmetryMode(Enum):
    SimLaminateSymmetryPivot = 0
    SimLaminateSymmetryNone = 1
    SimLaminateSymmetryNonPivot = 2


class SimLineFastenerConstructType(Enum):
    SimLineFastenerWedge = 0
    SimLineFastenerSolidHex = 1
    SimLineFastenerShell = 2


class SimLineFastenerMeshCompatibility(Enum):
    SimLineFastenerCompatible = 0
    SimLineFastenerNonCompatible = 1


class SimLineFastenerPlacementFastenerPlacementMethod(Enum):
    SimLineFastenerPlacementPointCoordinates = 0
    SimLineFastenerPlacementSupportBoundary = 1
    SimLineFastenerPlacementLine = 2
    SimLineFastenerPlacementLineLine = 3


class SimNonStructPlyPositionScheme(Enum):
    SimNonStructPlyPositionBottomOnly = 0
    SimNonStructPlyPositionTopAndBottom = 1
    SimNonStructPlyPositionTopOnly = 2
    SimNonStructPlyPositionUnDefined = 3


class SimNonstructuralMassApplicationMethod(Enum):
    SimNonstructuralMassTotalMass = 0
    SimNonstructuralMassMass = 1


class SimNonstructuralMassTotalMassDistributionMethod(Enum):
    SimNonstructuralMassMassProportional = 0
    SimNonstructuralMassVolumeProportional = 1


class SimOrientationAxisOfRotation(Enum):
    SimOrientationAxis3 = 0
    SimOrientationAxis1 = 1
    SimOrientationAxis2 = 2


class SimPointFastenerConstructType(Enum):
    SimPointFastenerAssembled = 0
    SimPointFastenerRigid = 1
    SimPointFastenerSpring = 2
    SimPointFastenerCoupling = 3
    SimPointFastenerBeam = 4
    SimPointFastenerSolidHex = 5


class SimPointFastenerPlacementDistributionOptionOnLine(Enum):
    SimPointFastenerPlacementNumberOfFasteners = 0
    SimPointFastenerPlacementPointSpacing = 1


class SimPointFastenerPlacementFastenerPlacementMethod(Enum):
    SimPointFastenerPlacementLine = 0
    SimPointFastenerPlacementPointCoordinates = 1
    SimPointFastenerPlacementPoint = 2


class SimRebarAttributeType(Enum):
    SimOffset = 0
    SimArea = 1
    SimRadius = 2
    SimAngle = 3
    SimSpacing = 4
    SimExtensionRatio = 5


class SimRebarGeometryType(Enum):
    SimAngular = 0
    SimConstant = 1
    SimLiftEquation = 2


class SimRigidBodyConstraintReferencePointInputMode(Enum):
    SimRigidBodyConstraintCenterOfMass = 0
    SimRigidBodyConstraintAutomatic = 1
    SimRigidBodyConstraintSpecify = 2


class SimShellSectionIntegrationScheme(Enum):
    SimShellSectionSimpsonIntegration = 0
    SimShellSectionGaussIntegration = 1


class SimShellSectionOffsetMethod(Enum):
    SimShellSectionNone = 0
    SimShellSectionBottomSurface = 1
    SimShellSectionThicknessRatio = 2
    SimShellSectionSpecifiedDistanceOffset = 3
    SimShellSectionTopSurface = 4


class SimShellSectionPoissonMethod(Enum):
    SimShellSectionPoissonElastic = 0
    SimShellSectionPoissonMaterial = 1
    SimShellSectionPoissonDefault = 2
    SimShellSectionPoissonValue = 3


class SimShellSectionThicknessType(Enum):
    SimShellSectionThin = 0
    SimShellSectionUser = 1
    SimShellSectionMid = 2


class SimSpringType(Enum):
    SimGeneralSpring = 0
    SimAxialSpring = 1


class SimThicknessType(Enum):
    SimVariable = 0
    SimUniform = 1


class SimTieDiscretizationMethod(Enum):
    SimTieSurfaceToSurface = 0
    SimTieNodeToSurface = 1
    SimTieSolverDefault = 2


class SimVirtualBoltAdvancedCouplingType(Enum):
    SimVirtualBoltAdvancedCouplingTypeDistributingContinuum = 0
    SimVirtualBoltAdvancedCouplingTypeDistributingStructural = 1
    SimVirtualBoltAdvancedCouplingTypeKinematic = 2


class SimVirtualBoltCoupledSurfaceType(Enum):
    SimVirtualBoltCoupledSurfaceTypeInfluenceRadius = 0
    SimVirtualBoltCoupledSurfaceTypeNodeRings = 1


class SimVirtualBoltIntermediateCouplingType(Enum):
    SimVirtualBoltIntermediateCouplingTypeNoConnection = 0
    SimVirtualBoltIntermediateCouplingTypeStandard = 1
    SimVirtualBoltIntermediateCouplingTypeTightFit = 2


class SimVirtualBoltMechanicalBehavior(Enum):
    SimVirtualBoltBehaviorBeam = 0
    SimVirtualBoltBehaviorDeformable = 1
    SimVirtualBoltBehaviorRigid = 2


class SimVirtualBoltSolidSolidConnectionType(Enum):
    SimVirtualBoltSolidSolidConnectionTypeCoupling = 0
    SimVirtualBoltSolidSolidConnectionTypeBeamAtInterface = 1


class SimVirtualBolt_BoltType(Enum):
    SimVirtualBolt_BoltTypeScrewWithHead = 0
    SimVirtualBolt_BoltTypeCountersink = 1
    SimVirtualBolt_BoltTypeGrounded = 2
    SimVirtualBolt_BoltTypeStandard = 3
    SimVirtualBolt_BoltTypeScrew = 4


