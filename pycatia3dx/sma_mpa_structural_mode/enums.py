SimBeamProfileShape = [
    'SimBeamProfileNone',
    'SimBeamProfileBox',
    'SimBeamProfileCircular',
    'SimBeamProfileGeneral',
    'SimBeamProfileHex',
    'SimBeamProfileI_Beam',
    'SimBeamProfileL_Beam',
    'SimBeamProfilePipe',
    'SimBeamProfileRectangular',
    'SimBeamProfileTrapezoid',
    'SimBeamProfileT_Beam',
    'SimBeamProfileChannel',
    'SimBeamProfileHat',
]
SimBeamSectionCrossSectionAxis = [
    'SimBeamSectionFirstAxis',
    'SimBeamSectionSecondAxis',
]
SimBeamSectionOrientation = [
    'SimBeamSectionGeometry',
    'SimBeamSectionAxisSystem',
]
SimBeamSectionSlendernessOption = [
    'SimBeamSectionDefault',
    'SimBeamSectionSpecify',
]
SimBeamSectionTransverseShearStiffness = [
    'SimBeamSectionNone',
    'SimBeamSectionCalculate',
    'SimBeamSectionIsotropic',
    'SimBeamSectionOrthotropic',
]
SimCohesiveMechanicalResponse = [
    'TractionSeparation',
    'Continuum',
    'Gasket',
]
SimCompositeLayupType = [
    'SimLayupByLamina',
    'SimLayupByPly',
    'SimFromDesign',
]
SimCompositeRosetteTransferCylindricalType = [
    'SimCompositeCylindericalZero',
    'SimCompositeCylindericalNinety',
]
SimCompositeRosetteTransferType = [
    'SimCompositeRosetteTypeCartesian',
    'SimCompositeRosetteTypeGuidedCurve',
]
SimCompositeShellSectionOffsetMethod = [
    'SimCompositeShellSectionAutomaticOffset',
    'SimCompositeShellSectionNone',
    'SimCompositeShellSectionSpecifiedDistanceOffset',
    'SimCompositeShellSectionThicknessRatio',
    'SimCompositeShellSectionTopSurface',
    'SimCompositeShellSectionBottomSurface',
    'SimCompositeShellSectionFromSolid',
]
SimConnectorCouplingType = [
    'SimConnectorCouplingKinematic',
    'SimConnectorCouplingDistributing',
]
SimConnectorElasticityElasticityOrder = [
    'SimConnectorElasticityLinear',
    'SimConnectorElasticityNonLinear',
]
SimConnectorElasticityTableColumn = [
    'SimConnectorElasticityStiffness',
    'SimConnectorElasticityTemperature',
    'SimConnectorElasticityPosition',
]
SimConnectorSectionAssembledConnectorType = [
    'SimConnectorSectionNoAssembledType',
    'SimConnectorSectionBeam',
    'SimConnectorSectionBushing',
    'SimConnectorSectionCVJoint',
    'SimConnectorSectionCylindrical',
    'SimConnectorSectionHinge',
    'SimConnectorSectionPlanar',
    'SimConnectorSectionRetractor',
    'SimConnectorSectionTranslator',
    'SimConnectorSectionUJoint',
    'SimConnectorSectionWeld',
    'SimConnectorSectionSlipring',
]
SimConnectorSectionRotationalConnectorType = [
    'SimConnectorSectionNoRotationalType',
    'SimConnectorSectionAlign',
    'SimConnectorSectionCardan',
    'SimConnectorSectionConstantVelocity',
    'SimConnectorSectionFlexionTorsion',
    'SimConnectorSectionEuler',
    'SimConnectorSectionProjectionFlexionTorsion',
    'SimConnectorSectionRevolute',
    'SimConnectorSectionRotation',
    'SimConnectorSectionRotationAccelerometer',
    'SimConnectorSectionUniversal',
    'SimConnectorSectionFlowConverter',
]
SimConnectorSectionTranslationalConnectorType = [
    'SimConnectorSectionNoTranslationalType',
    'SimConnectorSectionAccelerometer',
    'SimConnectorSectionAxialConnector',
    'SimConnectorSectionCartesian',
    'SimConnectorSectionJoin',
    'SimConnectorSectionLink',
    'SimConnectorSectionProjectionCartesian',
    'SimConnectorSectionRadialThrust',
    'SimConnectorSectionSlidePlane',
    'SimConnectorSectionSlot',
]
SimContactVirtualPartReferencePointInputMode = [
    'SimContactVirtualPartSpecify',
    'SimContactVirtualPartCenterOfMass',
    'SimContactVirtualPartAutomatic',
]
SimConversionType = [
    'SimBackgroundGrid',
    'SimParticlesPerDirection',
]
SimCouplingCouplingType = [
    'SimCouplingKinematic',
    'SimCouplingDistributing',
    'SimCouplingMultiphysics',
]
SimEulerianMaterialLocation = [
    'SimMLInsideSupport',
    'SimMLOutsideSupport',
]
SimEulerianVolumeFractionType = [
    'SimVFTSpecified',
    'SimVFTComputed',
]
SimFunctionOrder = [
    'SimSecond',
    'SimThird',
    'SimFifth',
]
SimLaminateStackingType = [
    'SimCompositeLaminateStackingUnknown',
    'SimCompositeLaminateStackingThicknessLaw',
    'SimCompositeLaminateStackingStackingSequence',
]
SimLaminateSymmetryMode = [
    'SimLaminateSymmetryNone',
    'SimLaminateSymmetryPivot',
    'SimLaminateSymmetryNonPivot',
]
SimLineFastenerConstructType = [
    'SimLineFastenerSolidHex',
    'SimLineFastenerShell',
    'SimLineFastenerWedge',
]
SimLineFastenerMeshCompatibility = [
    'SimLineFastenerCompatible',
    'SimLineFastenerNonCompatible',
]
SimLineFastenerPlacementFastenerPlacementMethod = [
    'SimLineFastenerPlacementLine',
    'SimLineFastenerPlacementPointCoordinates',
    'SimLineFastenerPlacementLineLine',
    'SimLineFastenerPlacementSupportBoundary',
]
SimNonStructPlyPositionScheme = [
    'SimNonStructPlyPositionUnDefined',
    'SimNonStructPlyPositionTopOnly',
    'SimNonStructPlyPositionBottomOnly',
    'SimNonStructPlyPositionTopAndBottom',
]
SimNonstructuralMassApplicationMethod = [
    'SimNonstructuralMassMass',
    'SimNonstructuralMassTotalMass',
]
SimNonstructuralMassTotalMassDistributionMethod = [
    'SimNonstructuralMassMassProportional',
    'SimNonstructuralMassVolumeProportional',
]
SimOrientationAxisOfRotation = [
    'SimOrientationAxis1',
    'SimOrientationAxis2',
    'SimOrientationAxis3',
]
SimPointFastenerConstructType = [
    'SimPointFastenerRigid',
    'SimPointFastenerSpring',
    'SimPointFastenerSolidHex',
    'SimPointFastenerBeam',
    'SimPointFastenerCoupling',
    'SimPointFastenerAssembled',
]
SimPointFastenerPlacementDistributionOptionOnLine = [
    'SimPointFastenerPlacementNumberOfFasteners',
    'SimPointFastenerPlacementPointSpacing',
]
SimPointFastenerPlacementFastenerPlacementMethod = [
    'SimPointFastenerPlacementPoint',
    'SimPointFastenerPlacementLine',
    'SimPointFastenerPlacementPointCoordinates',
]
SimRebarAttributeType = [
    'SimArea',
    'SimSpacing',
    'SimAngle',
    'SimOffset',
    'SimExtensionRatio',
    'SimRadius',
]
SimRebarGeometryType = [
    'SimConstant',
    'SimAngular',
    'SimLiftEquation',
]
SimRigidBodyConstraintReferencePointInputMode = [
    'SimRigidBodyConstraintSpecify',
    'SimRigidBodyConstraintCenterOfMass',
    'SimRigidBodyConstraintAutomatic',
]
SimShellSectionIntegrationScheme = [
    'SimShellSectionSimpsonIntegration',
    'SimShellSectionGaussIntegration',
]
SimShellSectionOffsetMethod = [
    'SimShellSectionNone',
    'SimShellSectionSpecifiedDistanceOffset',
    'SimShellSectionThicknessRatio',
    'SimShellSectionTopSurface',
    'SimShellSectionBottomSurface',
]
SimShellSectionPoissonMethod = [
    'SimShellSectionPoissonDefault',
    'SimShellSectionPoissonValue',
    'SimShellSectionPoissonMaterial',
    'SimShellSectionPoissonElastic',
]
SimShellSectionThicknessType = [
    'SimShellSectionUser',
    'SimShellSectionMid',
    'SimShellSectionThin',
]
SimSpringType = [
    'SimAxialSpring',
    'SimGeneralSpring',
]
SimThicknessType = [
    'SimUniform',
    'SimVariable',
]
SimTieDiscretizationMethod = [
    'SimTieSurfaceToSurface',
    'SimTieNodeToSurface',
    'SimTieSolverDefault',
]
SimVirtualBoltAdvancedCouplingType = [
    'SimVirtualBoltAdvancedCouplingTypeKinematic',
    'SimVirtualBoltAdvancedCouplingTypeDistributingContinuum',
    'SimVirtualBoltAdvancedCouplingTypeDistributingStructural',
]
SimVirtualBoltCoupledSurfaceType = [
    'SimVirtualBoltCoupledSurfaceTypeInfluenceRadius',
    'SimVirtualBoltCoupledSurfaceTypeNodeRings',
]
SimVirtualBoltIntermediateCouplingType = [
    'SimVirtualBoltIntermediateCouplingTypeNoConnection',
    'SimVirtualBoltIntermediateCouplingTypeStandard',
    'SimVirtualBoltIntermediateCouplingTypeTightFit',
]
SimVirtualBoltMechanicalBehavior = [
    'SimVirtualBoltBehaviorDeformable',
    'SimVirtualBoltBehaviorRigid',
    'SimVirtualBoltBehaviorBeam',
]
SimVirtualBoltSolidSolidConnectionType = [
    'SimVirtualBoltSolidSolidConnectionTypeBeamAtInterface',
    'SimVirtualBoltSolidSolidConnectionTypeCoupling',
]
SimVirtualBolt_BoltType = [
    'SimVirtualBolt_BoltTypeGrounded',
    'SimVirtualBolt_BoltTypeStandard',
    'SimVirtualBolt_BoltTypeCountersink',
    'SimVirtualBolt_BoltTypeScrew',
    'SimVirtualBolt_BoltTypeScrewWithHead',
]
