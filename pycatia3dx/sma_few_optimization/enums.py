from enum import Enum


class SimBasePlaneType(Enum):
    SimPrintingBed = 0
    SimSupportStructures = 1


class SimCalculatedResponseVariableType(Enum):
    SimAddAbsoluteValues = 0
    SimSubtractValues = 1
    SimSubtractAbsoluteValues = 2
    SimCombineValues = 3


class SimCastingControlType(Enum):
    SimSplitDraw = 0
    SimSingleDraw = 1
    SimAutoDraw = 2


class SimCenterOfGravityConstraintType(Enum):
    SimMaintain = 0
    SimDefine = 1


class SimDensityUpdateStrategyType(Enum):
    SimAggressiveDensityUpdateStrategy = 0
    SimConservativeDensityUpdateStrategy = 1
    SimAutomaticDensityUpdateStrategy = 2
    SimNormalDensityUpdateStrategy = 3


class SimDesignResponseDirection(Enum):
    SimDirectionAny = 0
    SimDirectionY = 1
    SimDirectionX = 2
    SimDirectionZ = 3


class SimDisplacementConstraintType(Enum):
    SimSpecificDirection = 0
    SimAllDirection = 1


class SimFastenerForceType(Enum):
    SimAxial = 0
    SimShear = 1


class SimFrequencyResponseVariableType(Enum):
    SimSingleMode = 0
    SimMultipleModeAggregation = 1


class SimMassConstraintType(Enum):
    SimRatioConstraint = 0
    SimAbsoluteConstraint = 1


class SimMaterialInterpolationType(Enum):
    SimMimpMaterialInterpolation = 0
    SimAutomaticMaterialInterpolation = 1
    SimSimpMaterialInterpolation = 2
    SimRampMaterialInterpolation = 3


class SimMomentOfInertiaComponent(Enum):
    SimComponentZZ = 0
    SimComponentXX = 1
    SimComponentXY = 2
    SimComponentYZ = 3
    SimComponentYY = 4
    SimComponentXZ = 5


class SimNodalUpdateType(Enum):
    SimAggressive = 0
    SimAutomatic = 1
    SimNormal = 2
    SimConservative = 3


class SimOptimizationTargetMassType(Enum):
    SimAbsolute = 0
    SimRatio = 1


class SimOptimizationTaskType(Enum):
    SimMinimizeResponseVariableValues = 0
    SimMinimizeMass = 1
    SimMaximizeLowestFrequency = 2
    SimMaximizeStiffness = 3
    SimMinimizeMaximumStress = 4
    SimMaximizeResponseVariableValues = 5
    SimMinimizeTheMaximumResponseVariableValues = 6


class SimPenetrationCheckType(Enum):
    SimBothDirection = 0
    SimOppositeDirection = 1
    SimNormalDirection = 2


class SimReactionForceConstraintType(Enum):
    SimComponent = 0
    SimTotal = 1


class SimReferenceModeType(Enum):
    SimPrevious = 0
    SimInitial = 1


class SimRemoveSoftElementsType(Enum):
    SimStandardRemoveSoftElements = 0
    SimAggressiveRemoveSoftElements = 1
    SimInactiveRemoveSoftElements = 2


class SimStrainType(Enum):
    SimPEMAGStrain = 0


class SimVectorUpdateType(Enum):
    SimFirst = 0
    SimAll = 1
    SimDefault = 2


