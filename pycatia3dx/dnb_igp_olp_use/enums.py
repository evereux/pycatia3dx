from enum import Enum


class DELOlpAccelerationMode(Enum):
    delOlpVariableTime = 0
    delOlpConstantTime = 1


class DELOlpAstNodeType(Enum):
    delAstASSIGN = 0
    delAstCASEDEFAULT = 1
    delAstELSEIF = 2
    delAstENDTEST = 3
    delAstENDIF = 4
    delAstCONTROLLER = 5
    delAstUNARYEXP = 6
    delAstMODULE = 7
    delAstPOSITIONS = 8
    delAstSTATEMENTS = 9
    delAstBINARYEXP = 10
    delAstFORMAT = 11
    delAstINSTRUCTIONS = 12
    delAstCONDEXP = 13
    delAstFOR = 14
    delAstPARAMETERS = 15
    delAstFUNCTION = 16
    delAstTASK = 17
    delAstUNTIL = 18
    delAstARGUMENTS = 19
    delAstTOKEN = 20
    delAstROOT = 21
    delAstELSE = 22
    delAstEXPRESSION = 23
    delAstEOL = 24
    delAstENDFOR = 25
    delAstGROUPEXP = 26
    delAstIF = 27
    delAstOPERATOR = 28
    delAstGOTO = 29
    delAstHEADER = 30
    delAstSTATEMENT = 31
    delAstCONST_BOOLEAN = 32
    delAstRUN = 33
    delAstVARIABLE = 34
    delAstWAIT = 35
    delAstENDWHILE = 36
    delAstRETURN = 37
    delAstCASE = 38
    delAstMOTION = 39
    delAstCONST_INTEGER = 40
    delAstFILE = 41
    delAstLABEL = 42
    delAstPULSE = 43
    delAstCOMMENT = 44
    delAstKEYWORD = 45
    delAstDECLARATIONS = 46
    delAstWHILE = 47
    delAstIDENTIFIER = 48
    delAstCONST_DOUBLE = 49
    delAstSTRING = 50
    delAstTEST = 51
    delAstDO = 52


class DELOlpAxisDirection(Enum):
    delOlpYNegative = 0
    delOlpZPositive = 1
    delOlpYPositive = 2
    delOlpXPositive = 3
    delOlpZNegative = 4
    delOlpXNegative = 5


class DELOlpChoreographyEventType(Enum):
    delOlpMotionTraceChoreography = 0
    delOlpVisibilityChoreography = 1
    delOlpColorChoreography = 2
    delOlpOtherChoreography = 3
    delOlpTextChoreography = 4
    delOlpViewpointChoreography = 5


class DELOlpConveyorTrackingMode(Enum):
    delOlpRailTracking = 0
    delOlpCircularTracking = 1
    delOlpLineTracking = 2


class DELOlpDataType(Enum):
    delOlpInteger = 0
    delOlpUnknownType = 1
    delOlpPositionVariable = 2
    delOlpString = 3
    delOlpBoolean = 4
    delOlpDouble = 5


class DELOlpDeviceType(Enum):
    delOlpRobotDevice = 0
    delOlpConveyorDevice = 1
    delOlpAllDevices = 2
    delOlpWorkpiecePositionerDevice = 3
    delOlpToolDevice = 4
    delOlpRailDevice = 5


class DELOlpEditableType(Enum):
    delOlpStringEditor = 0
    delOlpIntEditor = 1
    delOlpEditableComboEditor = 2
    delOlpDoubleEditor = 3
    delOlpComboEditor = 4
    delOlpNoEditor = 5


class DELOlpGunState(Enum):
    delOlpOn = 0
    delOlpOff = 1


class DELOlpInitialPositionMode(Enum):
    DELOlpCurrentPosition = 0
    DELOlpDesignPosition = 1


class DELOlpInstructionType(Enum):
    delOlpSpotOperation = 0
    delOlpAbort = 1
    delOlpRobotMotion = 2
    delOlpJumpTask = 3
    delOlpClinchOperation = 4
    delOlpPRun = 5
    delOlpRunByString = 6
    delOlpBoltOperation = 7
    delOlpRun = 8
    delOlpWaypointMotion = 9
    delOlpDrillOperation = 10
    delOlpPointAdhesiveOperation = 11
    delOlpSealantSurfaceOperation = 12
    delOlpTimer = 13
    delOlpWait = 14
    delOlpWaypointOperation = 15
    delOlpSealantOperation = 16
    delOlpLoop = 17
    delOlpTrigger = 18
    delOlpAssign = 19
    delOlpPaintOperation = 20
    delOlpGoto = 21
    delOlpPulse = 22
    delOlpCustom = 23
    delOlpSeamSearchOperation = 24
    delOlpGrab = 25
    delOlpTestCase = 26
    delOlpTemplate = 27
    delOlpAssignByString = 28
    delOlpGeneralSurfaceOperation = 29
    delOlpIf = 30
    delOlpArcOperation = 31
    delOlpPointOperation = 32
    delOlpRivetOperation = 33
    delOlpBreak = 34
    delOlpFor = 35
    delOlpPathAdhesiveOperation = 36
    delOlpRelease = 37
    delOlpReturn = 38


class DELOlpIODirection(Enum):
    delOlpInput = 0
    delOlpInOut = 1
    delOlpOutput = 2


class DELOlpJointType(Enum):
    delOlpLinearJoint = 0
    delOlpRotationalJoint = 1


class DELOlpMessageType(Enum):
    delOlpNotice = 0
    delOlpError = 1
    delOlpWarning = 2


class DELOlpMotionProfileUnits(Enum):
    delOlpMotionProfilePercent = 0
    delOlpMotionProfileAbsolute = 1


class DELOlpMotionType(Enum):
    delOlpCircularViaMotion = 0
    delOlpJointMotion = 1
    delOlpLinearMotion = 2
    delOlpCircularMotion = 3


class DELOlpOffsetType(Enum):
    delOlpCartesianStationOffset = 0
    delOlpCartesianToolOffset = 1
    delOlpNoOffset = 2
    delOlpCartesianObjectFrameOffset = 3
    delOlpJointOffset = 4


class DELOlpOrientationMode(Enum):
    delOlpOrientWrist = 0
    delOlpOrient2Axis = 1
    delOlpOrient1Axis = 2
    delOlpOrient3Axis = 3


class DELOlpPositionRef(Enum):
    delOlpUserDefined = 0
    delOlpMount = 1
    delOlpRobotOrigin = 2
    delOlpWorld = 3
    delOlpStation = 4
    delOlpRailOrigin = 5
    delOlpRobotBase = 6
    delOlpUnknown = 7


class DELOlpProcessType(Enum):
    delOlpUndefinedProcess = 0
    delOlpWeld = 1
    delOlpOscillationPoint = 2
    delOlpEndProcess = 3
    delOlpDepart = 4
    delOlpStartWeld = 5
    delOlpMidProcess = 6
    delOlpTouchPoint = 7
    delOlpApproach = 8
    delOlpEndWeld = 9
    delOlpViaPoint = 10
    delOlpStartProcess = 11


class DELOlpPulseType(Enum):
    delOlpPulseOff = 0
    delOlpPulseExpression = 1
    delOlpPulseInvert = 2
    delOlpPulseOn = 3
    delOlpPulseLiteralInteger = 4


class DELOlpRelativeMoveType(Enum):
    delOlpJointRelative = 0
    delOlpCartesianToolRelative = 1
    delOlpNoRelative = 2


class DELOlpSynchronizationMode(Enum):
    delOlpIndependent = 0
    delOlpCoordinated = 1
    delOlpSyncCoord = 2
    delOlpSynchronized = 3


class DELOlpTagGroupType(Enum):
    delOlpRivetTrajectory = 0
    delOlpGeneralSurfaceTrajecotry = 1
    delOlpArcTrajectory = 2
    delOlpSeamSearchTrajectory = 3
    delOlpTagGroup = 4
    delOlpSealantSurfaceTrajectory = 5
    delOlpGeneralPathTrajectory = 6
    delOlpPaintSurfaceTrajectory = 7
    delOlpManufacturingPattern = 8
    delOlpSpotTrajectory = 9
    delOlpShotPeenSurfaceTrajectory = 10


class DELOlpTargetType(Enum):
    delOlpTagTarget = 0
    delOlpJointTarget = 1
    delOlpCartesianTarget = 2
    delOlpHomeTarget = 3


class DELOlpTeachCommand(Enum):
    delOlpCmdRobotMotionTag = 0
    delOlpCmdArcOperation = 1
    delOlpCmdNone = 2
    delOlpCmdRobotMotionCartesian = 3
    delOlpCmdDelete = 4
    delOlpCmdModify = 5
    delOlpCmdRobotMotionJoint = 6
    delOlpCmdSpotOperation = 7


class DELOlpTimeLinearAngularBasis(Enum):
    delOlpLinearBasis = 0
    delOlpTimeBasis = 1
    delOlpAngularBasis = 2


class DELOlpTimerAction(Enum):
    delOlpTimerStart = 0
    delOlpTimerStop = 1
    delOlpTimerReset = 2


class DELOlpTraceLevel(Enum):
    delOlpAllTraces = 0
    delOlpNoTraces = 1
    delOlpUserTraces = 2


class DELOlpTriggerConditionType(Enum):
    delOlpImmediateTrigger = 0
    delOlpPlaneTrigger = 1
    delOlpTimeTrigger = 2
    delOlpDistanceTrigger = 3


class DELOlpTurnMode(Enum):
    delOlpAbsShortestAngle = 0
    delOlpTurnNumber = 1
    delOlpSolutionAngle = 2
    delOlpShortestAngle = 3
    delOlpTurnSign = 4


class DELOlpTurnSignType(Enum):
    delOlpTurnSignPositive = 0
    delOlpTurnSignNegative = 1


class DELOlpVariableType(Enum):
    delOlpExternalIO = 0
    delOlpAllVariables = 1
    delOlpProcedureIO = 2
    delOlpLocalVariable = 3
    delOlpConstant = 4
    delOlpAlias = 5


