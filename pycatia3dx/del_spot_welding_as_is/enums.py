from enum import Enum


class DELSpotAccuracyProfileAndAccelerationMoves(Enum):
    AccuracyProfilePressureEndMove = 0
    AccuracyProfileBackupMove = 1
    AccuracyProfilePressureStartMove = 2
    AccuracyProfilePressureMove = 3


class DELSpotMovingTipClearanceMoves(Enum):
    MovingTipPressureEndMove = 0
    MovingTipPressureStartMove = 1
    MovingTipApproachMove = 2


class DELSpotProfileApproachDir(Enum):
    Y_Axis = 0
    Neg_Z_Axis = 1
    X_Axis = 2
    Neg_Y_Axis = 3
    Z_Axis = 4
    Neg_X_Axis = 5


class DELSpotProfileMoves(Enum):
    PressureEndMove = 0
    ApproachMove = 1
    BackupMove = 2
    PressureStartMove = 3


class DELSpotStationaryTipClearanceMoves(Enum):
    StationaryTipPressureEndMove = 0
    StationaryTipPressureStartMove = 1
    StationaryTipApproachAndBackupMove = 2


