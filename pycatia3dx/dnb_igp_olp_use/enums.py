from enum import IntEnum


class DELOlpAccelerationMode(IntEnum):
    delOlpConstantTime = 0
    delOlpVariableTime = 1


class DELOlpAstNodeType(IntEnum):
    delAstROOT = 0
    delAstFILE = 1
    delAstMODULE = 2
    delAstTASK = 3
    delAstCONTROLLER = 4
    delAstINSTRUCTIONS = 5
    delAstPOSITIONS = 6
    delAstDECLARATIONS = 7
    delAstPARAMETERS = 8
    delAstARGUMENTS = 9
    delAstSTATEMENTS = 10
    delAstHEADER = 11
    delAstSTATEMENT = 12
    delAstMOTION = 13
    delAstVARIABLE = 14
    delAstRUN = 15
    delAstIF = 16
    delAstELSEIF = 17
    delAstELSE = 18
    delAstENDIF = 19
    delAstFOR = 20
    delAstENDFOR = 21
    delAstWHILE = 22
    delAstENDWHILE = 23
    delAstDO = 24
    delAstUNTIL = 25
    delAstTEST = 26
    delAstCASE = 27
    delAstCASEDEFAULT = 28
    delAstENDTEST = 29
    delAstGOTO = 30
    delAstLABEL = 31
    delAstASSIGN = 32
    delAstRETURN = 33
    delAstWAIT = 34
    delAstEXPRESSION = 35
    delAstGROUPEXP = 36
    delAstUNARYEXP = 37
    delAstBINARYEXP = 38
    delAstCONDEXP = 39
    delAstFUNCTION = 40
    delAstTOKEN = 41
    delAstKEYWORD = 42
    delAstIDENTIFIER = 43
    delAstSTRING = 44
    delAstCOMMENT = 45
    delAstCONST_INTEGER = 46
    delAstCONST_DOUBLE = 47
    delAstCONST_BOOLEAN = 48
    delAstOPERATOR = 49
    delAstFORMAT = 50
    delAstEOL = 51
    delAstPULSE = 52


class DELOlpAxisDirection(IntEnum):
    delOlpXPositive = 0
    delOlpYPositive = 1
    delOlpZPositive = 2
    delOlpXNegative = 3
    delOlpYNegative = 4
    delOlpZNegative = 5


class DELOlpChoreographyEventType(IntEnum):
    delOlpOtherChoreography = 0
    delOlpMotionTraceChoreography = 1
    delOlpVisibilityChoreography = 2
    delOlpTextChoreography = 3
    delOlpViewpointChoreography = 4
    delOlpColorChoreography = 5


class DELOlpConveyorTrackingMode(IntEnum):
    delOlpLineTracking = 0
    delOlpRailTracking = 1
    delOlpCircularTracking = 2


class DELOlpDataType(IntEnum):
    delOlpBoolean = 0
    delOlpInteger = 1
    delOlpDouble = 2
    delOlpString = 3
    delOlpUnknownType = 4
    delOlpPositionVariable = 5


class DELOlpDeviceType(IntEnum):
    delOlpRobotDevice = 0
    delOlpRailDevice = 1
    delOlpToolDevice = 2
    delOlpWorkpiecePositionerDevice = 3
    delOlpAllDevices = 4
    delOlpConveyorDevice = 5


class DELOlpEditableType(IntEnum):
    delOlpNoEditor = 0
    delOlpStringEditor = 1
    delOlpIntEditor = 2
    delOlpDoubleEditor = 3
    delOlpComboEditor = 4
    delOlpEditableComboEditor = 5


class DELOlpGunState(IntEnum):
    delOlpOn = 0
    delOlpOff = 1


class DELOlpInitialPositionMode(IntEnum):
    DELOlpDesignPosition = 0
    DELOlpCurrentPosition = 1


class DELOlpInstructionType(IntEnum):
    delOlpCustom = 0
    delOlpRobotMotion = 1
    delOlpSpotOperation = 2
    delOlpArcOperation = 3
    delOlpSeamSearchOperation = 4
    delOlpGrab = 5
    delOlpRelease = 6
    delOlpAssign = 7
    delOlpWait = 8
    delOlpRun = 9
    delOlpIf = 10
    delOlpLoop = 11
    delOlpFor = 12
    delOlpGoto = 13
    delOlpBreak = 14
    delOlpReturn = 15
    delOlpPointOperation = 16
    delOlpRivetOperation = 17
    delOlpBoltOperation = 18
    delOlpClinchOperation = 19
    delOlpPointAdhesiveOperation = 20
    delOlpSealantOperation = 21
    delOlpPathAdhesiveOperation = 22
    delOlpPulse = 23
    delOlpTestCase = 24
    delOlpTimer = 25
    delOlpPaintOperation = 26
    delOlpSealantSurfaceOperation = 27
    delOlpGeneralSurfaceOperation = 28
    delOlpTrigger = 29
    delOlpTemplate = 30
    delOlpDrillOperation = 31
    delOlpPRun = 32
    delOlpWaypointOperation = 33
    delOlpWaypointMotion = 34
    delOlpRunByString = 35
    delOlpAssignByString = 36
    delOlpJumpTask = 37
    delOlpAbort = 38


class DELOlpIODirection(IntEnum):
    delOlpInput = 0
    delOlpOutput = 1
    delOlpInOut = 2


class DELOlpJointType(IntEnum):
    delOlpLinearJoint = 0
    delOlpRotationalJoint = 1


class DELOlpMessageType(IntEnum):
    delOlpError = 0
    delOlpWarning = 1
    delOlpNotice = 2


class DELOlpMotionProfileUnits(IntEnum):
    delOlpMotionProfilePercent = 0
    delOlpMotionProfileAbsolute = 1


class DELOlpMotionType(IntEnum):
    delOlpJointMotion = 0
    delOlpLinearMotion = 1
    delOlpCircularMotion = 2
    delOlpCircularViaMotion = 3


class DELOlpOffsetType(IntEnum):
    delOlpNoOffset = 0
    delOlpJointOffset = 1
    delOlpCartesianObjectFrameOffset = 2
    delOlpCartesianToolOffset = 3
    delOlpCartesianStationOffset = 4


class DELOlpOrientationMode(IntEnum):
    delOlpOrient1Axis = 0
    delOlpOrient2Axis = 1
    delOlpOrient3Axis = 2
    delOlpOrientWrist = 3


class DELOlpPositionRef(IntEnum):
    delOlpWorld = 0
    delOlpStation = 1
    delOlpRailOrigin = 2
    delOlpRobotBase = 3
    delOlpMount = 4
    delOlpUserDefined = 5
    delOlpRobotOrigin = 6
    delOlpUnknown = 7


class DELOlpProcessType(IntEnum):
    delOlpUndefinedProcess = 0
    delOlpApproach = 1
    delOlpDepart = 2
    delOlpViaPoint = 3
    delOlpStartWeld = 4
    delOlpWeld = 5
    delOlpEndWeld = 6
    delOlpOscillationPoint = 7
    delOlpTouchPoint = 8
    delOlpStartProcess = 9
    delOlpMidProcess = 10
    delOlpEndProcess = 11


class DELOlpPulseType(IntEnum):
    delOlpPulseOn = 0
    delOlpPulseOff = 1
    delOlpPulseInvert = 2
    delOlpPulseLiteralInteger = 3
    delOlpPulseExpression = 4


class DELOlpRelativeMoveType(IntEnum):
    delOlpNoRelative = 0
    delOlpJointRelative = 1
    delOlpCartesianToolRelative = 2


class DELOlpSynchronizationMode(IntEnum):
    delOlpIndependent = 0
    delOlpSynchronized = 1
    delOlpCoordinated = 2
    delOlpSyncCoord = 3


class DELOlpTagGroupType(IntEnum):
    delOlpTagGroup = 0
    delOlpSpotTrajectory = 1
    delOlpRivetTrajectory = 2
    delOlpSeamSearchTrajectory = 3
    delOlpArcTrajectory = 4
    delOlpGeneralPathTrajectory = 5
    delOlpPaintSurfaceTrajectory = 6
    delOlpSealantSurfaceTrajectory = 7
    delOlpGeneralSurfaceTrajecotry = 8
    delOlpShotPeenSurfaceTrajectory = 9
    delOlpManufacturingPattern = 10


class DELOlpTargetType(IntEnum):
    delOlpJointTarget = 0
    delOlpHomeTarget = 1
    delOlpCartesianTarget = 2
    delOlpTagTarget = 3


class DELOlpTeachCommand(IntEnum):
    delOlpCmdNone = 0
    delOlpCmdModify = 1
    delOlpCmdDelete = 2
    delOlpCmdRobotMotionTag = 3
    delOlpCmdRobotMotionCartesian = 4
    delOlpCmdRobotMotionJoint = 5
    delOlpCmdSpotOperation = 6
    delOlpCmdArcOperation = 7


class DELOlpTimeLinearAngularBasis(IntEnum):
    delOlpTimeBasis = 0
    delOlpLinearBasis = 1
    delOlpAngularBasis = 2


class DELOlpTimerAction(IntEnum):
    delOlpTimerStart = 0
    delOlpTimerStop = 1
    delOlpTimerReset = 2


class DELOlpTraceLevel(IntEnum):
    delOlpNoTraces = 0
    delOlpUserTraces = 1
    delOlpAllTraces = 2


class DELOlpTriggerConditionType(IntEnum):
    delOlpImmediateTrigger = 0
    delOlpDistanceTrigger = 1
    delOlpTimeTrigger = 2
    delOlpPlaneTrigger = 3


class DELOlpTurnMode(IntEnum):
    delOlpTurnNumber = 0
    delOlpTurnSign = 1
    delOlpSolutionAngle = 2
    delOlpShortestAngle = 3
    delOlpAbsShortestAngle = 4


class DELOlpTurnSignType(IntEnum):
    delOlpTurnSignNegative = 0
    delOlpTurnSignPositive = 1


class DELOlpVariableType(IntEnum):
    delOlpExternalIO = 0
    delOlpProcedureIO = 1
    delOlpLocalVariable = 2
    delOlpConstant = 3
    delOlpAllVariables = 4
    delOlpAlias = 5
