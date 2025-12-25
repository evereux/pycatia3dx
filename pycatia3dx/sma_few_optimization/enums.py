from enum import Enum


class SimBasePlaneType(Enum):
    SimPrintingBed = 0
    SimSupportStructures = 1


class SimCalculatedResponseVariableType(Enum):
    SimCombineValues = 0
    SimAddAbsoluteValues = 1
    SimSubtractValues = 2
    SimSubtractAbsoluteValues = 3


class SimCastingControlType(Enum):
    SimSingleDraw = 0
    SimSplitDraw = 1
    SimAutoDraw = 2


class SimCenterOfGravityConstraintType(Enum):
    SimMaintain = 0
    SimDefine = 1


class SimDensityUpdateStrategyType(Enum):
    SimAutomaticDensityUpdateStrategy = 0
    SimNormalDensityUpdateStrategy = 1
    SimConservativeDensityUpdateStrategy = 2
    SimAggressiveDensityUpdateStrategy = 3


class SimDesignResponseDirection(Enum):
    SimDirectionAny = 0
    SimDirectionX = 1
    SimDirectionY = 2
    SimDirectionZ = 3


class SimDisplacementConstraintType(Enum):
    SimAllDirection = 0
    SimSpecificDirection = 1


class SimFastenerForceType(Enum):
    SimAxial = 0
    SimShear = 1


class SimFrequencyResponseVariableType(Enum):
    SimSingleMode = 0
    SimMultipleModeAggregation = 1


class SimMassConstraintType(Enum):
    SimAbsoluteConstraint = 0
    SimRatioConstraint = 1


class SimMaterialInterpolationType(Enum):
    SimAutomaticMaterialInterpolation = 0
    SimSimpMaterialInterpolation = 1
    SimRampMaterialInterpolation = 2
    SimMimpMaterialInterpolation = 3


class SimMomentOfInertiaComponent(Enum):
    SimComponentXX = 0
    SimComponentYY = 1
    SimComponentZZ = 2
    SimComponentXY = 3
    SimComponentXZ = 4
    SimComponentYZ = 5


class SimNodalUpdateType(Enum):
    SimAutomatic = 0
    SimNormal = 1
    SimConservative = 2
    SimAggressive = 3


class SimOptimizationTargetMassType(Enum):
    SimAbsolute = 0
    SimRatio = 1


class SimOptimizationTaskType(Enum):
    SimMaximizeStiffness = 0
    SimMinimizeMass = 1
    SimMaximizeLowestFrequency = 2
    SimMinimizeMaximumStress = 3
    SimMaximizeResponseVariableValues = 4
    SimMinimizeResponseVariableValues = 5
    SimMinimizeTheMaximumResponseVariableValues = 6


class SimPenetrationCheckType(Enum):
    SimBothDirection = 0
    SimNormalDirection = 1
    SimOppositeDirection = 2


class SimReactionForceConstraintType(Enum):
    SimTotal = 0
    SimComponent = 1


class SimReferenceModeType(Enum):
    SimPrevious = 0
    SimInitial = 1


class SimRemoveSoftElementsType(Enum):
    SimInactiveRemoveSoftElements = 0
    SimStandardRemoveSoftElements = 1
    SimAggressiveRemoveSoftElements = 2


class SimStrainType(Enum):
    SimPEMAGStrain = 0


class SimVectorUpdateType(Enum):
    SimDefault = 0
    SimAll = 1
    SimFirst = 2
