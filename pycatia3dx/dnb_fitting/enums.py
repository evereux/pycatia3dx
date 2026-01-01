from enum import IntEnum


class DNBInterpolater(IntEnum):
    FitLINEAR = 0
    FitSPLINE = 1
    FitCOMPOSITE = 2


class DNBTrackMode(IntEnum):
    FitTIME = 0
    FitSPEED = 1
