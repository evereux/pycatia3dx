from enum import Enum


class CATStrCollarThrowOrientation(Enum):
    catStrCollarThrowOrientationNormal = 0
    catStrCollarThrowOrientationInvert = 1
    catStrCollarThrowOrientationCentered = 2


class CATStrOpeningCreationMode(Enum):
    catStrOpeningPartDesign = 0
    catStrOpeningSlot = 1
    catStrOpeningStandard = 2
    catStrOpeningOutputProfile = 3
    catStrOpening3DObject = 4
    catStrOpeningUndefined = 5


class CATStrOpeningMode(Enum):
    catStrOpeningModeOutputProfile = 0
    catStrOpeningModeUndefined = 1
    catStrOpeningModeStandard = 2
    catStrOpeningMode3DObject = 3


class CATStrOpeningSTDMode(Enum):
    catStrOpeningSTDUndefinedMode = 0
    catStrOpeningSTDCatalogMode = 1
    catStrOpeningSTDOblongMode = 2
    catStrOpeningSTDRoundMode = 3
    catStrOpeningSTDRectMode = 4


class CATStrPanelMode(Enum):
    catStrPanelModeUndefined = 0
    catStrPanelModeSurf = 1


class CATStrPlateFaceName(Enum):
    catStrPlateFaceBottom = 0
    catStrPlateFaceTop = 1
    catStrPlateFaceNameUndefined = 2


class CATStrProfileMode(Enum):
    catStrProfileModeUndefined = 0
    catStrProfileModeSurf2Crvs = 1
    catStrProfileModeCrv = 2
    catStrProfileModeSurfSurf = 3
    catStrProfileModeOnLimits = 4
    catStrProfileModePtLength = 5
    catStrProfileModePtLimit = 6
    catStrProfileModePts = 7
    catStrProfileModeOnOpening = 8


class CATStrUseBracketPositionMode(Enum):
    catStr3DAxisPositionMode = 0
    catStrPlateStiffenerPositionMode = 1
    catStrMultiLimitsPositionMode = 2
    catStrStiffenerStiffenerPositionMode = 3


