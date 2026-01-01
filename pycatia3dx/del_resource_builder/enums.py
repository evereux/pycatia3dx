from enum import IntEnum


class AccuracyType(IntEnum):
    ACCURACY_TYPE_DISTANCE = 0
    ACCURACY_TYPE_SPEED = 1


class DELRscControllerDataContext(IntEnum):
    DELRscControllerDataContext_None = 0
    DELRscControllerDataContext_Reference = 1
    DELRscControllerDataContext_Instance = 2


class DELRscControllerGenericProfilesType(IntEnum):
    DELRscControllerGenericProfilesType_Tool = 0
    DELRscControllerGenericProfilesType_Motion = 1
    DELRscControllerGenericProfilesType_Accuracy = 2
    DELRscControllerGenericProfilesType_ObjectFrame = 3


class DELRscJointType(IntEnum):
    DELRscJointType_Linear = 0
    DELRscJointType_Angular = 1


class DELRscMotionControllerType(IntEnum):
    DELRscMotionControllerType_Default = 0
    DELRscMotionControllerType_Rail = 1
    DELRscMotionControllerType_EndOfArm = 2
    DELRscMotionControllerType_WorkpiecePositioner = 3
    DELRscMotionControllerType_Arm = 4
    DELRscMotionControllerType_FixedTool = 5


class DELRscSimulationStatus(IntEnum):
    DELRscSimulationStatus_ArmSolutionGood = 0
    DELRscSimulationStatus_DOFSoftErrorExceeded = 1
    DELRscSimulationStatus_ArmTargetUnreachable = 2
    DELRscSimulationStatus_DOFHardErrorExceeded = 3
    DELRscSimulationStatus_ArmSolutionSingular = 4
    DELRscSimulationStatus_ArmPostureInvalid = 5
    DELRscSimulationStatus_ArmNoSolution = 6
    DELRscSimulationStatus_ArmSolverError = 7


class DELRscSimulationVisualizationUpdate(IntEnum):
    DELRscSimulationVisualizationUpdate_OFF = 0
    DELRscSimulationVisualizationUpdate_ON = 1


class MotionBasis(IntEnum):
    MOTION_ABSOLUTE = 0
    MOTION_PERCENT = 1
    MOTION_TIME = 2
    MOTION_SPEEDACCEL = 3
