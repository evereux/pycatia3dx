from enum import IntEnum


class DELDRApproachDirection(IntEnum):
    DRProfile_ApproachXPlus = 0
    DRProfile_ApproachXMinus = 1
    DRProfile_ApproachYPlus = 2
    DRProfile_ApproachYMinus = 3
    DRProfile_ApproachZPlus = 4
    DRProfile_ApproachZMinus = 5


class DELDRProfileCycle(IntEnum):
    DRProfile_Drill = 0
    DRProfile_CounterSink = 1
    DRProfile_RivetBolt = 2
    DRProfile_Sealant = 3
    DRProfile_User1 = 4
    DRProfile_User2 = 5
    DRProfile_User3 = 6
    DRProfile_User4 = 7
    DRProfile_User5 = 8
    DRProfile_User6 = 9
    DRProfile_User7 = 10


class DELDRProfileMoves(IntEnum):
    DRProfile_Approach = 0
    DRProfile_Action = 1
    DRProfile_Retract = 2


class DELDRProfilePrecycle(IntEnum):
    DRProfile_None = 0
    DRProfile_Hole = 1
    DRProfile_Rivet = 2
    DRProfile_Bolt = 3


class DELDRProfileType(IntEnum):
    DRProfile_DrillOnly = 0
    DRProfile_RivetOnly = 1
    DRProfile_DrillRivet = 2


class DELSpotRivetApproachDirection(IntEnum):
    RivetProfile_ApproachXPlus = 0
    RivetProfile_ApproachXMinus = 1
    RivetProfile_ApproachYPlus = 2
    RivetProfile_ApproachYMinus = 3
    RivetProfile_ApproachZPlus = 4
    RivetProfile_ApproachZMinus = 5


class DELSpotRivetProfileMoves(IntEnum):
    RivetProfile_Approach = 0
    RivetProfile_Start = 1
    RivetProfile_Action = 2
    RivetProfile_Complete = 3
    RivetProfile_Retract = 4
