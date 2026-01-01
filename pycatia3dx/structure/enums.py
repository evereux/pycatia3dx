from enum import IntEnum


class CATStrCollarThrowOrientation(IntEnum):
    catStrCollarThrowOrientationInvert = 0
    catStrCollarThrowOrientationNormal = 1
    catStrCollarThrowOrientationCentered = 2


class CATStrOpeningCreationMode(IntEnum):
    catStrOpeningUndefined = 0
    catStrOpeningOutputProfile = 1
    catStrOpening3DObject = 2
    catStrOpeningStandard = 3
    catStrOpeningPartDesign = 4
    catStrOpeningSlot = 5


class CATStrOpeningMode(IntEnum):
    catStrOpeningModeUndefined = 0
    catStrOpeningMode3DObject = 1
    catStrOpeningModeOutputProfile = 2
    catStrOpeningModeStandard = 3


class CATStrOpeningSTDMode(IntEnum):
    catStrOpeningSTDUndefinedMode = 0
    catStrOpeningSTDRoundMode = 1
    catStrOpeningSTDRectMode = 2
    catStrOpeningSTDOblongMode = 3
    catStrOpeningSTDCatalogMode = 4


class CATStrPanelMode(IntEnum):
    catStrPanelModeUndefined = 0
    catStrPanelModeSurf = 1


class CATStrPlateFaceName(IntEnum):
    catStrPlateFaceNameUndefined = 0
    catStrPlateFaceBottom = 1
    catStrPlateFaceTop = 2


class CATStrProfileMode(IntEnum):
    catStrProfileModeUndefined = 0
    catStrProfileModePtLength = 1
    catStrProfileModePtLimit = 2
    catStrProfileModePts = 3
    catStrProfileModeCrv = 4
    catStrProfileModeSurf2Crvs = 5
    catStrProfileModeSurfSurf = 6
    catStrProfileModeOnOpening = 7
    catStrProfileModeOnLimits = 8


class CATStrUseBracketPositionMode(IntEnum):
    catStr3DAxisPositionMode = 0
    catStrPlateStiffenerPositionMode = 1
    catStrStiffenerStiffenerPositionMode = 2
    catStrMultiLimitsPositionMode = 3
