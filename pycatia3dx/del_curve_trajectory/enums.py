from enum import Enum


class CtmBaseAxisOrientation(Enum):
    AXIS_RELATIVE_VERTICAL = 0
    AXIS_RELATIVE = 1
    AXIS_RELATIVE_BISECTOR = 2
    AXIS_ABSOLUTE = 3


class CtmCurveType(Enum):
    CURVETYPE_UNKNOWN = 0
    RES_MFGCELL = 1
    PROCESS_TRAJECTORY = 2
    RES_BEADFASTENER = 3


class CtmRakeLocation(Enum):
    FLARESTART = 0
    FLAREEND = 1


class DNBTrajectoryType(Enum):
    WELD = 0
    SEALANT = 1
    ADHESIVE = 2
    GENERAL = 3
    UNDEFINED = 4
