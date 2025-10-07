"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.del_resource_builder.rsc_transform import RscTransform
from pycatia3dx.del_robot_simulation.tag_group import TagGroup
from pycatia3dx.interfaces.service import Service
from pycatia3dx.product_structure_client.vpm_occurrence import VPMOccurrence


class CalibLeastSquaresService(Service):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     InfInterfaces.Service
                |                         CalibLeastSquaresService
                | 
                | Service to calibrate a workpiece or resource.
                | 
                | Example: (VB.NET)
                | 
                |  Dim robot As VPMOccurrence = ...
                |  Dim cell As VPMOccurrence = ...
                |  Dim nominal As TagGroup = ... 
                |  Dim measured As TagGroup = ... 
                | 
                |  Dim LSQService As CalibLeastSquaresService = CATIA.Application.GetSessionService("CalibLeastSquaresService")
                |  Try
                |    calibration.PartToCalibrate = robot
                |    calibration.SetNominalPoints(nominal, cell, True)
                |    calibration.SetMeasuredPoints(measured, cell, False)
                |    calibration.DoCalibration(True, True)
                |    If calibration.RMSError < 0.01 Then
                |      calibration.ApplyCalibration()
                |    End If
                |  Catch ex As Exception
                |    Dim errormsg As String = calibration.LastErrorMessage
                |    If errormsg.Length > 0 Then
                |      MsgBox(errormsg)
                |    Else
                |      MsgBox("calibration failed with no error")
                |    End If
                |  End Try
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def calibration_distance(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property CalibrationDistance() As double (Read Only)
                |     Output: Get the calibration distance.
                |     This is the translation distance the part will be or has been moved. This
                |     cannot be called before DoCalibration. Value is in meters.

        :return: float
        """

        return self.com_object.CalibrationDistance

    @property
    def calibration_offset(self) -> RscTransform:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property CalibrationOffset() As RscTransform (Read Only)
                |     Output: Get the calibration transform.
                |     This is the transform that will be or has been applied to the part
                |     position. You can calculate the resulting part position before calling
                |     ApplyCalibration as follows:
                | 
                | 
                |      Dim PartPosition As RscTransform = LSQService.PartPosition
                |      Dim CalibrationTransform As RscTransform = LSQService.CalibrationOffset
                |      Dim CalibratedPosition as RscTransform = PartPosition.Multiply(CalibrationTransform)
                | 
                |      
                | 
                |     This cannot be called before DoCalibration.

        :return: RscTransform
        """

        return RscTransform(self.com_object.CalibrationOffset)

    @property
    def calibration_rotation(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property CalibrationRotation() As double (Read Only)
                |     Output: Get the calibration rotation.
                |     This is the amount the part will be rotated. This rotation value is about
                |     an axis and incorporates the yaw pitch and roll values into a single number.
                |     This is useful if you want to ensure only a small rotation will be applied by
                |     ApplyCalibration. This cannot be called before DoCalibration. Value is in
                |     radians.

        :return: float
        """

        return self.com_object.CalibrationRotation

    @property
    def free_pitch(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property FreePitch() As boolean
                |     Input: Get/Set if Pitch parameter is free.
                |     Specifies the directions in which the resource may be translated during
                |     adjustment. Unless the resource is known to be aligned with an axis or on a
                |     plane, the [X, Y, Z] parameters should all be set Free during calibration. If
                |     true, then the Pitch coordinate of the part is free to be adjusted during the
                |     calibration Default value is True if not set. This cannot be set after
                |     DoCalibration.

        :return: bool
        """

        return self.com_object.FreePitch

    @free_pitch.setter
    def free_pitch(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.FreePitch = value

    @property
    def free_roll(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property FreeRoll() As boolean
                |     Input: Get/Set if Roll parameter is free.
                |     Specifies the directions in which the resource may be translated during
                |     adjustment. Unless the resource is known to be aligned with an axis or on a
                |     plane, the [X, Y, Z] parameters should all be set Free during calibration. If
                |     true, then the Roll coordinate of the part is free to be adjusted during the
                |     calibration Default value is True if not set. This cannot be set after
                |     DoCalibration.

        :return: bool
        """

        return self.com_object.FreeRoll

    @free_roll.setter
    def free_roll(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.FreeRoll = value

    @property
    def free_x(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property FreeX() As boolean
                |     Input: Get/Set if X parameter is free.
                |     Specifies the directions in which the resource may be translated during
                |     adjustment. Unless the resource is known to be aligned with an axis or on a
                |     plane, the [X, Y, Z] parameters should all be set Free during calibration. If
                |     true, then the X coordinate of the part is free to be adjusted during the
                |     calibration This cannot be set after DoCalibration.

        :return: bool
        """

        return self.com_object.FreeX

    @free_x.setter
    def free_x(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.FreeX = value

    @property
    def free_y(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property FreeY() As boolean
                |     Input: Get/Set if Y parameter is free.
                |     Specifies the directions in which the resource may be translated during
                |     adjustment. Unless the resource is known to be aligned with an axis or on a
                |     plane, the [X, Y, Z] parameters should all be set Free during calibration. If
                |     true, then the Y coordinate of the part is free to be adjusted during the
                |     calibration Default value is True if not set. This cannot be set after
                |     DoCalibration.

        :return: bool
        """

        return self.com_object.FreeY

    @free_y.setter
    def free_y(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.FreeY = value

    @property
    def free_yaw(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property FreeYaw() As boolean
                |     Input: Get/Set if Yaw parameter is free.
                |     Specifies the directions in which the resource may be translated during
                |     adjustment. Unless the resource is known to be aligned with an axis or on a
                |     plane, the [X, Y, Z] parameters should all be set Free during calibration. If
                |     true, then the Yaw coordinate of the part is free to be adjusted during the
                |     calibration Default value is True if not set. This cannot be set after
                |     DoCalibration.

        :return: bool
        """

        return self.com_object.FreeYaw

    @free_yaw.setter
    def free_yaw(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.FreeYaw = value

    @property
    def free_z(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property FreeZ() As boolean
                |     Input: Get/Set if Z parameter is free.
                |     Specifies the directions in which the resource may be translated during
                |     adjustment. Unless the resource is known to be aligned with an axis or on a
                |     plane, the [X, Y, Z] parameters should all be set Free during calibration. If
                |     true, then the Z coordinate of the part is free to be adjusted during the
                |     calibration Default value is True if not set. This cannot be set after
                |     DoCalibration.

        :return: bool
        """

        return self.com_object.FreeZ

    @free_z.setter
    def free_z(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.FreeZ = value

    @property
    def last_error_message(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property LastErrorMessage() As CATBSTR (Read Only)
                |     Output: Get the error message from the last function call, property set or
                |     get.
                |     The message is translated into the user's current language settings.

        :return: str
        """

        return self.com_object.LastErrorMessage

    @property
    def max_rotation_uncertainty(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property MaxRotationUncertainty() As double (Read Only)
                |     Output: Get maximum rotational uncertainty.
                |     This value represents the maximum of the uncertainties for the fit on the
                |     parameters to be identified. Large uncertainty values are an indication that
                |     the experimental observation strategy is flawed, even if the RMS fitting error
                |     is small. This cannot be called before DoCalibration. This fails if Yaw, Pitch
                |     and Roll parameters are all fixed. Value is in radians.

        :return: float
        """

        return self.com_object.MaxRotationUncertainty

    @property
    def max_translation_uncertainty(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property MaxTranslationUncertainty() As double (Read Only)
                |     Output: Get maximum translation uncertainty.
                |     This value represents the maximum of the uncertainties for the fit on the
                |     parameters to be identified. Large uncertainty values are an indication that
                |     the experimental observation strategy is flawed, even if the RMS fitting error
                |     is small. This cannot be called before DoCalibration. This fails if X, Y, and Z
                |     parameters are all fixed. Value is in meters.

        :return: float
        """

        return self.com_object.MaxTranslationUncertainty

    @property
    def measurement_noise(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property MeasurementNoise() As double
                |     Input: Get/Set the estimated measurement noise.
                |     An estimate of the uncertainty of the positional measurements during the
                |     calibration experiment. The measurement noise need only be an order of
                |     magnitude estimate, for example 0.0001m or 0.001m. Min value for Noise
                |     Measurement is 0.0001m which is also the default value if not
                |     set.
                |     Units are in meters. This cannot be set after DoCalibration.

        :return: float
        """

        return self.com_object.MeasurementNoise

    @measurement_noise.setter
    def measurement_noise(self, value: float):
        """
        :param float value:
        """

        self.com_object.MeasurementNoise = value

    @property
    def num_iterations(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property NumIterations() As long (Read Only)
                |     Output: Get the number of iterations it took for the LSQ algorithm to
                |     converge.
                |     This cannot be called before DoCalibration.

        :return: int
        """

        return self.com_object.NumIterations

    @property
    def part_position(self) -> RscTransform:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property PartPosition() As RscTransform (Read Only)
                |     Output: Get the current part position.
                |     If called before ApplyCalibration this will be the original (uncalibrated)
                |     position. If called after ApplyCalibration this will be the newly calibrated
                |     position. This cannot be called before setting the PartToCalibrate.

        :return: RscTransform
        """

        return RscTransform(self.com_object.PartPosition)

    @property
    def part_to_calibrate(self) -> VPMOccurrence:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property PartToCalibrate() As VPMOccurrence
                |     Input: Get/Set the workpiece or resource to calibrate.
                |     This is the occurrence of the product, robot or other resource to move
                |     during the calibration. This must be set before calling DoCalibration.

        :return: VPMOccurrence
        """

        return VPMOccurrence(self.com_object.PartToCalibrate)

    @part_to_calibrate.setter
    def part_to_calibrate(self, value: VPMOccurrence):
        """
        :param VPMOccurrence value:
        """

        self.com_object.PartToCalibrate = value

    @property
    def rms_error(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property RMSError() As double (Read Only)
                |     Output: Get root mean square fitting error.
                |     The root mean square fitting error on the points after adjusting the part
                |     to the best fit possible. This cannot be called before DoCalibration. Value is
                |     in meters.

        :return: float
        """

        return self.com_object.RMSError

    def apply_calibration(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub ApplyCalibration()
                |     Action: Apply the calibration position to the part.
                |     This must be called after DoCalibration and can only be called 1 time.

        :return: None
        """
        return self.com_object.ApplyCalibration()

    def do_calibration(self, i_with3_pt: bool, i_order_tags: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub DoCalibration(boolean iWith3Pt,boolean iOrderTags)
                |     Action: Do the calibration.
                |     You must set the required inputs PartToCalibrate, SetNominalPoints,
                |     SetMeasueredPoints before calling DoCalibration. After DoCalibration you can
                |     get output values. You can repeat the calibration by changing input parameters
                |     and calling DoCalibration again. If an error occurs this function will throw an
                |     exception and you can call LastErrorMessage to get information about the
                |     problem.
                | 
                |     Parameters:
                | 
                |         iWith3Pt
                |             Do a 3Pt calibration before the LSQ calibration. The calibration is
                |             done with 3 points chosen from the input tag groups. The purpose is to get the
                |             part closer to the target so the least squares algorithm has a better chance of
                |             conversion. If the parts are far apart or have a large rotation, it is
                |             recommended to set this to True. 
                |         iOrderTags
                |             Automatically calculate the order of the measured and nominal tags.
                |             If this is False, the tags are matched up in the order they are in the tag
                |             group. If True, a best fit will be computed to order the tags.

        :param bool i_with3_pt:
        :param bool i_order_tags:
        :return: None
        """
        return self.com_object.DoCalibration(i_with3_pt, i_order_tags)

    def get_measured_points(self, o_points: TagGroup, o_tag_group_owner: VPMOccurrence) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetMeasuredPoints(TagGroup oPoints,VPMOccurrence
                | oTagGroupOwner)
                |     Input: Get measured calibration points.
                | 
                |     Parameters:
                | 
                |         oPoints
                |             The tag group with the measured points. 
                |         oTagGroupOwner
                |             The owner occurrence of the tag group.

        :param TagGroup o_points:
        :param VPMOccurrence o_tag_group_owner:
        :return: None
        """
        return self.com_object.GetMeasuredPoints(o_points.com_object, o_tag_group_owner.com_object)

    def get_nominal_points(self, o_points: TagGroup, o_tag_group_owner: VPMOccurrence) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetNominalPoints(TagGroup oPoints,VPMOccurrence
                | oTagGroupOwner)
                |     Input: Get nominal calibration points.
                | 
                |     Parameters:
                | 
                |         oPoints
                |             The tag group with the nominal points. 
                |         oTagGroupOwner
                |             The owner occurrence of the tag group.

        :param TagGroup o_points:
        :param VPMOccurrence o_tag_group_owner:
        :return: None
        """
        return self.com_object.GetNominalPoints(o_points.com_object, o_tag_group_owner.com_object)

    def set_measured_points(self, i_points: TagGroup, i_tag_group_owner: VPMOccurrence, i_force_detach: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetMeasuredPoints(TagGroup iPoints,VPMOccurrence iTagGroupOwner,boolean
                | iForceDettach)
                |     Input: Set measured calibration points.
                |     This is the location the nominal points need to be moved to. This must be
                |     set before calling DoCalibration and after setting PartToCalibrate. The
                |     measured points cannot be attached to the part being calibrated. If the tag
                |     group is not valid, this function will throw an exception and you can call
                |     LastErrorMessage to get information about the problem.
                | 
                |     Parameters:
                | 
                |         iPoints
                |             The tag group with the measured points. 
                |         iTagGroupOwner
                |             The owner occurrence of the tag group. 
                |         iForceDettach
                |             If set to true, the tag group will be detached from the part being
                |             calibrated if it is attached to it.

        :param TagGroup i_points:
        :param VPMOccurrence i_tag_group_owner:
        :param bool i_force_detach:
        :return: None
        """
        return self.com_object.SetMeasuredPoints(i_points.com_object, i_tag_group_owner.com_object, i_force_detach)

    def set_nominal_points(self, i_points: TagGroup, i_tag_group_owner: VPMOccurrence, i_force_attachment: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetNominalPoints(TagGroup iPoints,VPMOccurrence iTagGroupOwner,boolean
                | iForceAttachement)
                |     Input: Set nominal calibration points.
                |     This is the current simulation location of the points to be calibrated.
                |     This must be set before calling DoCalibration and after setting
                |     PartToCalibrate. The nominal points must be attached to the part being
                |     calibrated. When the part is moved, by the calibration these points will then
                |     be moved to the same location. If the tag group is not valid, this function
                |     will throw an exception and you can call LastErrorMessage to get information
                |     about the problem.
                | 
                |     Parameters:
                | 
                |         iPoints
                |             The tag group with the nominal points. 
                |         iTagGroupOwner
                |             The owner occurrence of the tag group. 
                |         iForceAttachement
                |             If set to true, the tag group will be attached to the part to
                |             calibrate, regardless if it is already attached. 

        :param TagGroup i_points:
        :param VPMOccurrence i_tag_group_owner:
        :param bool i_force_attachment:
        :return: None
        """
        return self.com_object.SetNominalPoints(i_points.com_object, i_tag_group_owner.com_object, i_force_attachment)

    def __repr__(self):
        return f'CalibLeastSquaresService(name="{ self.name }")'
