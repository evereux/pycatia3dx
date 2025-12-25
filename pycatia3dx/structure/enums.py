from enum import Enum


class CATStrCollarThrowOrientation(Enum):
    catStrCollarThrowOrientationInvert = 0
    catStrCollarThrowOrientationNormal = 1
    catStrCollarThrowOrientationCentered = 2


class CATStrOpeningCreationMode(Enum):
    catStrOpeningUndefined = 0
    catStrOpeningOutputProfile = 1
    catStrOpening3DObject = 2
    catStrOpeningStandard = 3
    catStrOpeningPartDesign = 4
    catStrOpeningSlot = 5


class CATStrOpeningMode(Enum):
    catStrOpeningModeUndefined = 0
    catStrOpeningMode3DObject = 1
    catStrOpeningModeOutputProfile = 2
    catStrOpeningModeStandard = 3


class CATStrOpeningSTDMode(Enum):
    catStrOpeningSTDUndefinedMode = 0
    catStrOpeningSTDRoundMode = 1
    catStrOpeningSTDRectMode = 2
    catStrOpeningSTDOblongMode = 3
    catStrOpeningSTDCatalogMode = 4


class CATStrPanelMode(Enum):
    catStrPanelModeUndefined = 0
    catStrPanelModeSurf = 1


class CATStrPlateFaceName(Enum):
    catStrPlateFaceNameUndefined = 0
    catStrPlateFaceBottom = 1
    catStrPlateFaceTop = 2


class CATStrProfileMode(Enum):
    catStrProfileModeUndefined = 0
    catStrProfileModePtLength = 1
    catStrProfileModePtLimit = 2
    catStrProfileModePts = 3
    catStrProfileModeCrv = 4
    catStrProfileModeSurf2Crvs = 5
    catStrProfileModeSurfSurf = 6
    catStrProfileModeOnOpening = 7
    catStrProfileModeOnLimits = 8


class CATStrUseBracketPositionMode(Enum):
    catStr3DAxisPositionMode = 0
    catStrPlateStiffenerPositionMode = 1
    catStrStiffenerStiffenerPositionMode = 2
    catStrMultiLimitsPositionMode = 3
