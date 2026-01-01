from enum import IntEnum


class DELSpotAccuracyProfileAndAccelerationMoves(IntEnum):
    AccuracyProfilePressureStartMove = 0
    AccuracyProfilePressureMove = 1
    AccuracyProfilePressureEndMove = 2
    AccuracyProfileBackupMove = 3


class DELSpotMovingTipClearanceMoves(IntEnum):
    MovingTipApproachMove = 0
    MovingTipPressureStartMove = 1
    MovingTipPressureEndMove = 2


class DELSpotProfileApproachDir(IntEnum):
    X_Axis = 0
    Y_Axis = 1
    Z_Axis = 2
    Neg_X_Axis = 3
    Neg_Y_Axis = 4
    Neg_Z_Axis = 5


class DELSpotProfileMoves(IntEnum):
    ApproachMove = 0
    PressureStartMove = 1
    PressureEndMove = 2
    BackupMove = 3


class DELSpotStationaryTipClearanceMoves(IntEnum):
    StationaryTipApproachAndBackupMove = 0
    StationaryTipPressureStartMove = 1
    StationaryTipPressureEndMove = 2
