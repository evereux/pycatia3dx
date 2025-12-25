from enum import Enum


class DELSpotAccuracyProfileAndAccelerationMoves(Enum):
    AccuracyProfilePressureStartMove = 0
    AccuracyProfilePressureMove = 1
    AccuracyProfilePressureEndMove = 2
    AccuracyProfileBackupMove = 3


class DELSpotMovingTipClearanceMoves(Enum):
    MovingTipApproachMove = 0
    MovingTipPressureStartMove = 1
    MovingTipPressureEndMove = 2


class DELSpotProfileApproachDir(Enum):
    X_Axis = 0
    Y_Axis = 1
    Z_Axis = 2
    Neg_X_Axis = 3
    Neg_Y_Axis = 4
    Neg_Z_Axis = 5


class DELSpotProfileMoves(Enum):
    ApproachMove = 0
    PressureStartMove = 1
    PressureEndMove = 2
    BackupMove = 3


class DELSpotStationaryTipClearanceMoves(Enum):
    StationaryTipApproachAndBackupMove = 0
    StationaryTipPressureStartMove = 1
    StationaryTipPressureEndMove = 2
