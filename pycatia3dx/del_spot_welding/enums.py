from enum import Enum


class DELDRApproachDirection(Enum):
    DRProfile_ApproachXPlus = 0
    DRProfile_ApproachXMinus = 1
    DRProfile_ApproachZPlus = 2
    DRProfile_ApproachZMinus = 3
    DRProfile_ApproachYPlus = 4
    DRProfile_ApproachYMinus = 5


class DELDRProfileCycle(Enum):
    DRProfile_User1 = 0
    DRProfile_User7 = 1
    DRProfile_Sealant = 2
    DRProfile_User3 = 3
    DRProfile_RivetBolt = 4
    DRProfile_User4 = 5
    DRProfile_User6 = 6
    DRProfile_User5 = 7
    DRProfile_Drill = 8
    DRProfile_User2 = 9
    DRProfile_CounterSink = 10


class DELDRProfileMoves(Enum):
    DRProfile_Retract = 0
    DRProfile_Action = 1
    DRProfile_Approach = 2


class DELDRProfilePrecycle(Enum):
    DRProfile_Bolt = 0
    DRProfile_Hole = 1
    DRProfile_Rivet = 2
    DRProfile_None = 3


class DELDRProfileType(Enum):
    DRProfile_RivetOnly = 0
    DRProfile_DrillOnly = 1
    DRProfile_DrillRivet = 2


class DELSpotRivetApproachDirection(Enum):
    RivetProfile_ApproachYPlus = 0
    RivetProfile_ApproachXMinus = 1
    RivetProfile_ApproachZMinus = 2
    RivetProfile_ApproachZPlus = 3
    RivetProfile_ApproachXPlus = 4
    RivetProfile_ApproachYMinus = 5


class DELSpotRivetProfileMoves(Enum):
    RivetProfile_Start = 0
    RivetProfile_Retract = 1
    RivetProfile_Complete = 2
    RivetProfile_Approach = 3
    RivetProfile_Action = 4


