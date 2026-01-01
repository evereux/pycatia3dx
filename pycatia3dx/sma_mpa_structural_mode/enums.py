from enum import IntEnum


class SimBeamProfileShape(IntEnum):
    SimBeamProfileNone = 0
    SimBeamProfileBox = 1
    SimBeamProfileCircular = 2
    SimBeamProfileGeneral = 3
    SimBeamProfileHex = 4
    SimBeamProfileI_Beam = 5
    SimBeamProfileL_Beam = 6
    SimBeamProfilePipe = 7
    SimBeamProfileRectangular = 8
    SimBeamProfileTrapezoid = 9
    SimBeamProfileT_Beam = 10
    SimBeamProfileChannel = 11
    SimBeamProfileHat = 12


class SimBeamSectionCrossSectionAxis(IntEnum):
    SimBeamSectionFirstAxis = 0
    SimBeamSectionSecondAxis = 1


class SimBeamSectionOrientation(IntEnum):
    SimBeamSectionGeometry = 0
    SimBeamSectionAxisSystem = 1


class SimBeamSectionSlendernessOption(IntEnum):
    SimBeamSectionDefault = 0
    SimBeamSectionSpecify = 1


class SimBeamSectionTransverseShearStiffness(IntEnum):
    SimBeamSectionNone = 0
    SimBeamSectionCalculate = 1
    SimBeamSectionIsotropic = 2
    SimBeamSectionOrthotropic = 3


class SimCohesiveMechanicalResponse(IntEnum):
    TractionSeparation = 0
    Continuum = 1
    Gasket = 2


class SimCompositeLayupType(IntEnum):
    SimLayupByLamina = 0
    SimLayupByPly = 1
    SimFromDesign = 2


class SimCompositeRosetteTransferCylindricalType(IntEnum):
    SimCompositeCylindericalZero = 0
    SimCompositeCylindericalNinety = 1


class SimCompositeRosetteTransferType(IntEnum):
    SimCompositeRosetteTypeCartesian = 0
    SimCompositeRosetteTypeGuidedCurve = 1


class SimCompositeShellSectionOffsetMethod(IntEnum):
    SimCompositeShellSectionAutomaticOffset = 0
    SimCompositeShellSectionNone = 1
    SimCompositeShellSectionSpecifiedDistanceOffset = 2
    SimCompositeShellSectionThicknessRatio = 3
    SimCompositeShellSectionTopSurface = 4
    SimCompositeShellSectionBottomSurface = 5
    SimCompositeShellSectionFromSolid = 6


class SimConnectorCouplingType(IntEnum):
    SimConnectorCouplingKinematic = 0
    SimConnectorCouplingDistributing = 1


class SimConnectorElasticityElasticityOrder(IntEnum):
    SimConnectorElasticityLinear = 0
    SimConnectorElasticityNonLinear = 1


class SimConnectorElasticityTableColumn(IntEnum):
    SimConnectorElasticityStiffness = 0
    SimConnectorElasticityTemperature = 1
    SimConnectorElasticityPosition = 2


class SimConnectorSectionAssembledConnectorType(IntEnum):
    SimConnectorSectionNoAssembledType = 0
    SimConnectorSectionBeam = 1
    SimConnectorSectionBushing = 2
    SimConnectorSectionCVJoint = 3
    SimConnectorSectionCylindrical = 4
    SimConnectorSectionHinge = 5
    SimConnectorSectionPlanar = 6
    SimConnectorSectionRetractor = 7
    SimConnectorSectionTranslator = 8
    SimConnectorSectionUJoint = 9
    SimConnectorSectionWeld = 10
    SimConnectorSectionSlipring = 11


class SimConnectorSectionRotationalConnectorType(IntEnum):
    SimConnectorSectionNoRotationalType = 0
    SimConnectorSectionAlign = 1
    SimConnectorSectionCardan = 2
    SimConnectorSectionConstantVelocity = 3
    SimConnectorSectionFlexionTorsion = 4
    SimConnectorSectionEuler = 5
    SimConnectorSectionProjectionFlexionTorsion = 6
    SimConnectorSectionRevolute = 7
    SimConnectorSectionRotation = 8
    SimConnectorSectionRotationAccelerometer = 9
    SimConnectorSectionUniversal = 10
    SimConnectorSectionFlowConverter = 11


class SimConnectorSectionTranslationalConnectorType(IntEnum):
    SimConnectorSectionNoTranslationalType = 0
    SimConnectorSectionAccelerometer = 1
    SimConnectorSectionAxialConnector = 2
    SimConnectorSectionCartesian = 3
    SimConnectorSectionJoin = 4
    SimConnectorSectionLink = 5
    SimConnectorSectionProjectionCartesian = 6
    SimConnectorSectionRadialThrust = 7
    SimConnectorSectionSlidePlane = 8
    SimConnectorSectionSlot = 9


class SimContactVirtualPartReferencePointInputMode(IntEnum):
    SimContactVirtualPartSpecify = 0
    SimContactVirtualPartCenterOfMass = 1
    SimContactVirtualPartAutomatic = 2


class SimConversionType(IntEnum):
    SimBackgroundGrid = 0
    SimParticlesPerDirection = 1


class SimCouplingCouplingType(IntEnum):
    SimCouplingKinematic = 0
    SimCouplingDistributing = 1
    SimCouplingMultiphysics = 2


class SimEulerianMaterialLocation(IntEnum):
    SimMLInsideSupport = 0
    SimMLOutsideSupport = 1


class SimEulerianVolumeFractionType(IntEnum):
    SimVFTSpecified = 0
    SimVFTComputed = 1


class SimFunctionOrder(IntEnum):
    SimSecond = 0
    SimThird = 1
    SimFifth = 2


class SimLaminateStackingType(IntEnum):
    SimCompositeLaminateStackingUnknown = 0
    SimCompositeLaminateStackingThicknessLaw = 1
    SimCompositeLaminateStackingStackingSequence = 2


class SimLaminateSymmetryMode(IntEnum):
    SimLaminateSymmetryNone = 0
    SimLaminateSymmetryPivot = 1
    SimLaminateSymmetryNonPivot = 2


class SimLineFastenerConstructType(IntEnum):
    SimLineFastenerSolidHex = 0
    SimLineFastenerShell = 1
    SimLineFastenerWedge = 2


class SimLineFastenerMeshCompatibility(IntEnum):
    SimLineFastenerCompatible = 0
    SimLineFastenerNonCompatible = 1


class SimLineFastenerPlacementFastenerPlacementMethod(IntEnum):
    SimLineFastenerPlacementLine = 0
    SimLineFastenerPlacementPointCoordinates = 1
    SimLineFastenerPlacementLineLine = 2
    SimLineFastenerPlacementSupportBoundary = 3


class SimNonStructPlyPositionScheme(IntEnum):
    SimNonStructPlyPositionUnDefined = 0
    SimNonStructPlyPositionTopOnly = 1
    SimNonStructPlyPositionBottomOnly = 2
    SimNonStructPlyPositionTopAndBottom = 3


class SimNonstructuralMassApplicationMethod(IntEnum):
    SimNonstructuralMassMass = 0
    SimNonstructuralMassTotalMass = 1


class SimNonstructuralMassTotalMassDistributionMethod(IntEnum):
    SimNonstructuralMassMassProportional = 0
    SimNonstructuralMassVolumeProportional = 1


class SimOrientationAxisOfRotation(IntEnum):
    SimOrientationAxis1 = 0
    SimOrientationAxis2 = 1
    SimOrientationAxis3 = 2


class SimPointFastenerConstructType(IntEnum):
    SimPointFastenerRigid = 0
    SimPointFastenerSpring = 1
    SimPointFastenerSolidHex = 2
    SimPointFastenerBeam = 3
    SimPointFastenerCoupling = 4
    SimPointFastenerAssembled = 5


class SimPointFastenerPlacementDistributionOptionOnLine(IntEnum):
    SimPointFastenerPlacementNumberOfFasteners = 0
    SimPointFastenerPlacementPointSpacing = 1


class SimPointFastenerPlacementFastenerPlacementMethod(IntEnum):
    SimPointFastenerPlacementPoint = 0
    SimPointFastenerPlacementLine = 1
    SimPointFastenerPlacementPointCoordinates = 2


class SimRebarAttributeType(IntEnum):
    SimArea = 0
    SimSpacing = 1
    SimAngle = 2
    SimOffset = 3
    SimExtensionRatio = 4
    SimRadius = 5


class SimRebarGeometryType(IntEnum):
    SimConstant = 0
    SimAngular = 1
    SimLiftEquation = 2


class SimRigidBodyConstraintReferencePointInputMode(IntEnum):
    SimRigidBodyConstraintSpecify = 0
    SimRigidBodyConstraintCenterOfMass = 1
    SimRigidBodyConstraintAutomatic = 2


class SimShellSectionIntegrationScheme(IntEnum):
    SimShellSectionSimpsonIntegration = 0
    SimShellSectionGaussIntegration = 1


class SimShellSectionOffsetMethod(IntEnum):
    SimShellSectionNone = 0
    SimShellSectionSpecifiedDistanceOffset = 1
    SimShellSectionThicknessRatio = 2
    SimShellSectionTopSurface = 3
    SimShellSectionBottomSurface = 4


class SimShellSectionPoissonMethod(IntEnum):
    SimShellSectionPoissonDefault = 0
    SimShellSectionPoissonValue = 1
    SimShellSectionPoissonMaterial = 2
    SimShellSectionPoissonElastic = 3


class SimShellSectionThicknessType(IntEnum):
    SimShellSectionUser = 0
    SimShellSectionMid = 1
    SimShellSectionThin = 2


class SimSpringType(IntEnum):
    SimAxialSpring = 0
    SimGeneralSpring = 1


class SimThicknessType(IntEnum):
    SimUniform = 0
    SimVariable = 1


class SimTieDiscretizationMethod(IntEnum):
    SimTieSurfaceToSurface = 0
    SimTieNodeToSurface = 1
    SimTieSolverDefault = 2


class SimVirtualBoltAdvancedCouplingType(IntEnum):
    SimVirtualBoltAdvancedCouplingTypeKinematic = 0
    SimVirtualBoltAdvancedCouplingTypeDistributingContinuum = 1
    SimVirtualBoltAdvancedCouplingTypeDistributingStructural = 2


class SimVirtualBoltCoupledSurfaceType(IntEnum):
    SimVirtualBoltCoupledSurfaceTypeInfluenceRadius = 0
    SimVirtualBoltCoupledSurfaceTypeNodeRings = 1


class SimVirtualBoltIntermediateCouplingType(IntEnum):
    SimVirtualBoltIntermediateCouplingTypeNoConnection = 0
    SimVirtualBoltIntermediateCouplingTypeStandard = 1
    SimVirtualBoltIntermediateCouplingTypeTightFit = 2


class SimVirtualBoltMechanicalBehavior(IntEnum):
    SimVirtualBoltBehaviorDeformable = 0
    SimVirtualBoltBehaviorRigid = 1
    SimVirtualBoltBehaviorBeam = 2


class SimVirtualBoltSolidSolidConnectionType(IntEnum):
    SimVirtualBoltSolidSolidConnectionTypeBeamAtInterface = 0
    SimVirtualBoltSolidSolidConnectionTypeCoupling = 1


class SimVirtualBolt_BoltType(IntEnum):
    SimVirtualBolt_BoltTypeGrounded = 0
    SimVirtualBolt_BoltTypeStandard = 1
    SimVirtualBolt_BoltTypeCountersink = 2
    SimVirtualBolt_BoltTypeScrew = 3
    SimVirtualBolt_BoltTypeScrewWithHead = 4
