from enum import Enum


class AccuracyType(Enum):
    ACCURACY_TYPE_SPEED = 0
    ACCURACY_TYPE_DISTANCE = 1


class DELRscControllerDataContext(Enum):
    DELRscControllerDataContext_None = 0
    DELRscControllerDataContext_Reference = 1
    DELRscControllerDataContext_Instance = 2


class DELRscControllerGenericProfilesType(Enum):
    DELRscControllerGenericProfilesType_ObjectFrame = 0
    DELRscControllerGenericProfilesType_Motion = 1
    DELRscControllerGenericProfilesType_Tool = 2
    DELRscControllerGenericProfilesType_Accuracy = 3


class DELRscJointType(Enum):
    DELRscJointType_Angular = 0
    DELRscJointType_Linear = 1


class DELRscMotionControllerType(Enum):
    DELRscMotionControllerType_WorkpiecePositioner = 0
    DELRscMotionControllerType_Default = 1
    DELRscMotionControllerType_Rail = 2
    DELRscMotionControllerType_EndOfArm = 3
    DELRscMotionControllerType_Arm = 4
    DELRscMotionControllerType_FixedTool = 5


class DELRscSimulationStatus(Enum):
    DELRscSimulationStatus_ArmPostureInvalid = 0
    DELRscSimulationStatus_ArmTargetUnreachable = 1
    DELRscSimulationStatus_ArmSolutionSingular = 2
    DELRscSimulationStatus_DOFHardErrorExceeded = 3
    DELRscSimulationStatus_ArmSolutionGood = 4
    DELRscSimulationStatus_ArmSolverError = 5
    DELRscSimulationStatus_ArmNoSolution = 6
    DELRscSimulationStatus_DOFSoftErrorExceeded = 7


class DELRscSimulationVisualizationUpdate(Enum):
    DELRscSimulationVisualizationUpdate_ON = 0
    DELRscSimulationVisualizationUpdate_OFF = 1


class MotionBasis(Enum):
    MOTION_ABSOLUTE = 0
    MOTION_SPEEDACCEL = 1
    MOTION_TIME = 2
    MOTION_PERCENT = 3


