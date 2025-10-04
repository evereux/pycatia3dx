"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.sma_mpa_results.sim_sensor_base import SimSensorBase


class SimStrainGaugeSensor(SimSensorBase):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SMAMpaResultsIDLItf.SimSensorBase
                |                         SimStrainGaugeSensor
                | 
                | Represents the virtual strain gauge sensor.
                | Role:Creating the strain gauge sensor feature using the
                | SimStrainGaugeSensorFactory::CreateSensor. Then set the different API's
                | provided in this interface and update the strain gauge sensor using and the See
                | SimSensorBase.Update() method.
                | Example:
                | 
                |  Given a SimResultsAnalysisCase object, you can create a Sensor object as
                |  following.
                |  
                | 
                |  Dim oStrainGaugeSensor As SimStrainGaugeSensor
                |  Set oStrainGaugeSensor = SimStrainGaugeSensorFactory.CreateSensor
                |  SimStrainGaugeVariableType eType = SimStress
                |  Set oStrainGaugeSensor.Variable = eType
                |  oStrainGaugeSensor.SetOriginLocations dOriginX, dOriginY,
                |  dOriginZ
                |  oStrainGaugeSensor.SetAxisDirections dXx, dXy, dXz, dZx, dZy,
                |  dZz
                |  oStrainGaugeSensor.Update
                |  
                | 
                | See SimResultsAnalysisCase
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def gauge_tolerance(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property GaugeTolerance() As double
                |     Gets/Sets the tolerance for the gauge size. If not set, automatic tolerance
                |     would be computed for the model.

        :return: float
        """

        return self.com_object.GaugeTolerance

    @gauge_tolerance.setter
    def gauge_tolerance(self, value: float):
        """
        :param float value:
        """

        self.com_object.GaugeTolerance = value

    @property
    def position_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property PositionType() As SimStrainGaugePositionType
                |     Gets/Sets the position of the gauge origin. The available option can be
                |     found in the SimStrainGaugePositionType enum. This should be used before
                |     calling SetOriginLocations(). If not called, the SimPositionPoint will be the
                |     default. If SimPositionNode or SimPositionElementFace is used, the input origin
                |     values may changes if the Node/Element faces does not lie exactly on the
                |     specified values. The origin will be snapped to the nearest Node/Element face.
                |     The modified origin values can be retrieved using the GetOriginLocations() API.

        :return: int
        """

        return self.com_object.PositionType

    @position_type.setter
    def position_type(self, value: int):
        """
        :param int value:
        """

        self.com_object.PositionType = value

    @property
    def show_glyph(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ShowGlyph() As boolean
                |     Gets/Sets whether to show the glyph for the sensor gauge values. If not
                |     set, the glyph will not be shown.

        :return: bool
        """

        return self.com_object.ShowGlyph

    @show_glyph.setter
    def show_glyph(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.ShowGlyph = value

    @property
    def track_current_frame(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property TrackCurrentFrame() As boolean
                |     Gets/Sets whether the sensor computation is to be done based on the current
                |     frame. As the current frame changes, the sensor value will also change. If set
                |     as True, no need to call the SetStepAndFrame() method.

        :return: bool
        """

        return self.com_object.TrackCurrentFrame

    @track_current_frame.setter
    def track_current_frame(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.TrackCurrentFrame = value

    @property
    def variable_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property VariableType() As SimStrainGaugeVariableType
                |     Gets/Sets the variable for which the sensor is to be created. The available
                |     option can be found in the SimStrainGaugeVariableType enum.

        :return: int
        """

        return self.com_object.VariableType

    @variable_type.setter
    def variable_type(self, value: int):
        """
        :param int value:
        """

        self.com_object.VariableType = value

    def export(self, ics_file_name: str, ics_file_location: str, ie_file_type: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub Export(CATBSTR icsFileName,CATBSTR icsFileLocation,SimFileType
                | ieFileType)
                |     Exports the sensor values. If the sensor contains multiple gauge values, a
                |     new row will be added in the csv file with a common sensor
                |     name.
                | 
                |     Parameters:
                | 
                |         icsFileName
                |             The name of the file. If not specified, the name of the sensor will
                |             be taken by default. 
                |         icsFileLocation
                |             The location at which the exported file needs to be created.
                |             
                |         ieFileType
                |             The file types. The available options can be found in
                |             SMAIAMpaFileTypeEnum class. 
                | 
                |     Returns:
                |         S_OK if successful.

        :param str ics_file_name:
        :param str ics_file_location:
        :param SimFileType ie_file_type:
        :return: None
        """
        return self.com_object.Export(ics_file_name, ics_file_location, ie_file_type)

    def get_axis_directions(self, in_index: int, od_measurement_x: float, od_measurement_y: float, od_measurement_z: float, od_set_x: float, od_set_y: float, od_set_z: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetAxisDirections(long inIndex,double odMeasurementX,double
                | odMeasurementY,double odMeasurementZ,double odSetX,double odSetY,double
                | odSetZ)
                |     Gets the measurement(X) and set(Z) directions for the gauge
                |     location.
                | 
                |     Parameters:
                | 
                |         inIndex
                |             The row index for which to get the directions. The total avaialbe
                |             rows can be retrieved from GetNumberOfGaugeValues() method.
                |             
                |         odMeasurementX
                |             The X values for the measurement direction. 
                |         odMeasurementY
                |             The Y values for the measurement direction. 
                |         odMeasurementZ
                |             The Z values for the measurement direction. 
                |         odSetX
                |             The X values for the set direction. 
                |         odSetY
                |             The Y values for the set direction. 
                |         odSetZ
                |             The Z values for the set direction.

        :param int in_index:
        :param float od_measurement_x:
        :param float od_measurement_y:
        :param float od_measurement_z:
        :param float od_set_x:
        :param float od_set_y:
        :param float od_set_z:
        :return: None
        """
        return self.com_object.GetAxisDirections(in_index, od_measurement_x, od_measurement_y, od_measurement_z, od_set_x, od_set_y, od_set_z)

    def get_number_of_gauge_values(self, on_rows: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetNumberOfGaugeValues(long onRows)
                |     The number of gauge values. A single sensor can have multiple gauge values.
                |     It is shown in form of table in the UI. It can be used to run a loop to get all
                |     the gauge origin and directions using GetOriginLocations and GetAxisDirections
                |     methods.
                | 
                |     Parameters:
                | 
                |         nRows
                |             The number of rows.

        :param int on_rows:
        :return: None
        """
        return self.com_object.GetNumberOfGaugeValues(on_rows)

    def get_origin_locations(self, in_index: int, on_id: int, od_origin_x: float, od_origin_y: float, od_origin_z: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetOriginLocations(long inIndex,long onID,double odOriginX,double
                | odOriginY,double odOriginZ)
                |     Gets the origin points for the gauge location.
                | 
                |     Parameters:
                | 
                |         inIndex
                |             The row index. The total available rows can be retrieved from
                |             GetGaugeIds() method. 
                |         onID
                |             The row Id for which to get the directions. 
                |         oldOriginX
                |             The X values for the origins. 
                |         oldOriginY
                |             The Y values for the origins. 
                |         oldOriginZ
                |             The Z values for the origins.

        :param int in_index:
        :param int on_id:
        :param float od_origin_x:
        :param float od_origin_y:
        :param float od_origin_z:
        :return: None
        """
        return self.com_object.GetOriginLocations(in_index, on_id, od_origin_x, od_origin_y, od_origin_z)

    def get_size(self, ob_specify: bool, od_length: float, od_width: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetSize(boolean obSpecify,double odLength,double odWidth)
                |     Gets the size of the gauge. It is the rectangular area showing the
                |     gauge.
                | 
                |     Parameters:
                | 
                |         obSpecify
                |             False if no area is specified else true. 
                |         odLength
                |             The length of the gauge rectangle. 
                |         odWidth
                |             The width of the gauge rectangle.

        :param bool ob_specify:
        :param float od_length:
        :param float od_width:
        :return: None
        """
        return self.com_object.GetSize(ob_specify, od_length, od_width)

    def get_step_and_frame(self, ocs_persistent_step_id: str, on_frame_index: int, on_load_case_index: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetStepAndFrame(CATBSTR ocsPersistentStepID,long onFrameIndex,long
                | onLoadCaseIndex)
                |     Gets the step, frame and load case information needed to create the
                |     sensor.
                | 
                |     Parameters:
                | 
                |         ocsPersistentStepID
                |             The persistent ID of the step. 
                |         onFrameIndex
                |             The frame index. The index starts from 1. 
                |         onLoadCaseIndex
                |             The load case index. The index starts from 1.

        :param str ocs_persistent_step_id:
        :param int on_frame_index:
        :param int on_load_case_index:
        :return: None
        """
        return self.com_object.GetStepAndFrame(ocs_persistent_step_id, on_frame_index, on_load_case_index)

    def set_axis_directions(self, id_measurement_x: float, id_measurement_y: float, id_measurement_z: float, id_set_x: float, id_set_y: float, id_set_z: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetAxisDirections(double idMeasurementX,double idMeasurementY,double
                | idMeasurementZ,double idSetX,double idSetY,double idSetZ)
                |     Sets the measurement(X) and set(Z) directions for the gauge location. These
                |     can be called in a loop for setting multiple gauge values. This should be
                |     called for the same number of times as we would call the SetOriginLocations
                |     method. The order shouls also be same as that of SetOriginLocations. Its size
                |     must be same as that of Origin values.
                | 
                |     Parameters:
                | 
                |         idMeasurementX
                |             The X values for the measurement direction. 
                |         idMeasurementY
                |             The Y values for the measurement direction. 
                |         idMeasurementZ
                |             The Z values for the measurement direction. 
                |         idSetX
                |             The X values for the set direction. 
                |         idSetY
                |             The Y values for the set direction. 
                |         idSetZ
                |             The Z values for the set direction.

        :param float id_measurement_x:
        :param float id_measurement_y:
        :param float id_measurement_z:
        :param float id_set_x:
        :param float id_set_y:
        :param float id_set_z:
        :return: None
        """
        return self.com_object.SetAxisDirections(id_measurement_x, id_measurement_y, id_measurement_z, id_set_x, id_set_y, id_set_z)

    def set_origin_locations(self, i_id: int, id_origin_x: float, id_origin_y: float, id_origin_z: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetOriginLocations(long iId,double idOriginX,double idOriginY,double
                | idOriginZ)
                |     Sets the origin points for the gauge location. Alleast one origin point
                |     must be set to create the sensor. For creating multiple points, this method can
                |     be called in a loop.
                | 
                |     Parameters:
                | 
                |         iId
                |             The Id for the specific gauge. The Ids can be retrieved from the
                |             GetGaugeIds() method. The GetGaugeIds() will return empty list while creation
                |             of new sensor. In that case the index can be passed as 1,2...n. The index
                |             should be unique for each gauge value. 
                |         ildOriginX
                |             The X values for the origins. 
                |         ildOriginY
                |             The Y values for the origins. 
                |         ildOriginZ
                |             The Z values for the origins.

        :param int i_id:
        :param float id_origin_x:
        :param float id_origin_y:
        :param float id_origin_z:
        :return: None
        """
        return self.com_object.SetOriginLocations(i_id, id_origin_x, id_origin_y, id_origin_z)

    def set_size(self, ib_specify: bool, id_length: float, id_width: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetSize(boolean ibSpecify,double idLength,double idWidth)
                |     Sets the size for the gauge.
                | 
                |     Parameters:
                | 
                |         ibSpecify
                |             If set false, automatic area will be considered. If true, the
                |             length and width will have to be specified. 
                |         idLength
                |             The length of the gauge rectangle. 
                |         idWidth
                |             The width of the gauge rectangle.

        :param bool ib_specify:
        :param float id_length:
        :param float id_width:
        :return: None
        """
        return self.com_object.SetSize(ib_specify, id_length, id_width)

    def set_step_and_frame(self, ics_persistent_step_id: str, in_frame_index: int, in_load_case_index: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetStepAndFrame(CATBSTR icsPersistentStepID,long inFrameIndex,long
                | inLoadCaseIndex)
                |     Sets the step, frame and load case information needed to create the sensor.
                |     If not set, the track current frame option will be
                |     activated.
                | 
                |     Parameters:
                | 
                |         icsPersistentStepID
                |             The persistent ID of the step. 
                |         inFrameIndex
                |             The frame index. The index starts from 1. 
                |         inLoadCaseIndex
                |             The load case index. The index starts from 1. 

        :param str ics_persistent_step_id:
        :param int in_frame_index:
        :param int in_load_case_index:
        :return: None
        """
        return self.com_object.SetStepAndFrame(ics_persistent_step_id, in_frame_index, in_load_case_index)

    def __repr__(self):
        return f'SimStrainGaugeSensor(name="{ self.name }")'
