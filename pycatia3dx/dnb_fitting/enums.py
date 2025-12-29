from enum import Enum


class DNBInterpolater(Enum):
    FitLINEAR = 0
    FitSPLINE = 1
    FitCOMPOSITE = 2


class DNBTrackMode(Enum):
    FitTIME = 0
    FitSPEED = 1
