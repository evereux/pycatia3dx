from enum import Enum


class CtmBaseAxisOrientation(Enum):
    AXIS_RELATIVE_VERTICAL = 0
    AXIS_RELATIVE_BISECTOR = 1
    AXIS_RELATIVE = 2
    AXIS_ABSOLUTE = 3


class CtmCurveType(Enum):
    RES_MFGCELL = 0
    CURVETYPE_UNKNOWN = 1
    PROCESS_TRAJECTORY = 2
    RES_BEADFASTENER = 3


class CtmRakeLocation(Enum):
    FLARESTART = 0
    FLAREEND = 1


class DNBTrajectoryType(Enum):
    GENERAL = 0
    SEALANT = 1
    WELD = 2
    UNDEFINED = 3
    ADHESIVE = 4


