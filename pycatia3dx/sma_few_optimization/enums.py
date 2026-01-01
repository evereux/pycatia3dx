from enum import IntEnum


class SimBasePlaneType(IntEnum):
    SimPrintingBed = 0
    SimSupportStructures = 1


class SimCalculatedResponseVariableType(IntEnum):
    SimCombineValues = 0
    SimAddAbsoluteValues = 1
    SimSubtractValues = 2
    SimSubtractAbsoluteValues = 3


class SimCastingControlType(IntEnum):
    SimSingleDraw = 0
    SimSplitDraw = 1
    SimAutoDraw = 2


class SimCenterOfGravityConstraintType(IntEnum):
    SimMaintain = 0
    SimDefine = 1


class SimDensityUpdateStrategyType(IntEnum):
    SimAutomaticDensityUpdateStrategy = 0
    SimNormalDensityUpdateStrategy = 1
    SimConservativeDensityUpdateStrategy = 2
    SimAggressiveDensityUpdateStrategy = 3


class SimDesignResponseDirection(IntEnum):
    SimDirectionAny = 0
    SimDirectionX = 1
    SimDirectionY = 2
    SimDirectionZ = 3


class SimDisplacementConstraintType(IntEnum):
    SimAllDirection = 0
    SimSpecificDirection = 1


class SimFastenerForceType(IntEnum):
    SimAxial = 0
    SimShear = 1


class SimFrequencyResponseVariableType(IntEnum):
    SimSingleMode = 0
    SimMultipleModeAggregation = 1


class SimMassConstraintType(IntEnum):
    SimAbsoluteConstraint = 0
    SimRatioConstraint = 1


class SimMaterialInterpolationType(IntEnum):
    SimAutomaticMaterialInterpolation = 0
    SimSimpMaterialInterpolation = 1
    SimRampMaterialInterpolation = 2
    SimMimpMaterialInterpolation = 3


class SimMomentOfInertiaComponent(IntEnum):
    SimComponentXX = 0
    SimComponentYY = 1
    SimComponentZZ = 2
    SimComponentXY = 3
    SimComponentXZ = 4
    SimComponentYZ = 5


class SimNodalUpdateType(IntEnum):
    SimAutomatic = 0
    SimNormal = 1
    SimConservative = 2
    SimAggressive = 3


class SimOptimizationTargetMassType(IntEnum):
    SimAbsolute = 0
    SimRatio = 1


class SimOptimizationTaskType(IntEnum):
    SimMaximizeStiffness = 0
    SimMinimizeMass = 1
    SimMaximizeLowestFrequency = 2
    SimMinimizeMaximumStress = 3
    SimMaximizeResponseVariableValues = 4
    SimMinimizeResponseVariableValues = 5
    SimMinimizeTheMaximumResponseVariableValues = 6


class SimPenetrationCheckType(IntEnum):
    SimBothDirection = 0
    SimNormalDirection = 1
    SimOppositeDirection = 2


class SimReactionForceConstraintType(IntEnum):
    SimTotal = 0
    SimComponent = 1


class SimReferenceModeType(IntEnum):
    SimPrevious = 0
    SimInitial = 1


class SimRemoveSoftElementsType(IntEnum):
    SimInactiveRemoveSoftElements = 0
    SimStandardRemoveSoftElements = 1
    SimAggressiveRemoveSoftElements = 2


class SimStrainType(IntEnum):
    SimPEMAGStrain = 0


class SimVectorUpdateType(IntEnum):
    SimDefault = 0
    SimAll = 1
    SimFirst = 2
