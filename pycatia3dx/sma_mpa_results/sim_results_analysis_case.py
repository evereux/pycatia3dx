"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx import SimFileType, SimColumnSeparator
from pycatia3dx.sma_mpa_results.sim_buckle_mode_sensor import SimBuckleModeSensor
from pycatia3dx.sma_mpa_results.sim_export_field import SimExportField
from pycatia3dx.sma_mpa_results.sim_field_plot import SimFieldPlot
from pycatia3dx.sma_mpa_results.sim_frames_selection import SimFramesSelection
from pycatia3dx.sma_mpa_results.sim_frequency_sensor import SimFrequencySensor
from pycatia3dx.sma_mpa_results.sim_history_plot import SimHistoryPlot
from pycatia3dx.sma_mpa_results.sim_resultant_sensor import SimResultantSensor
from pycatia3dx.sma_mpa_results.sim_results_steps import SimResultsSteps
from pycatia3dx.sma_mpa_results.sim_sensor import SimSensor
from pycatia3dx.system.any_object import AnyObject


class SimResultsAnalysisCase(AnyObject):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimResultsAnalysisCase
                | 
                | Represents the results analysis case and can be used to access the data in the
                | case.
                | Example:
                | 
                |  Given a SimResultsManager object, you can create a SimResultsAnalysisCase
                |  object as following.
                |  The index starts from 1.
                |  
                | 
                |   Dim oResultsAnalysisCases As SimResultsAnalysisCases
                |   Set oResultsAnalysisCases = oResultsManager.ResultsAnalysisCases
                |   Dim oResultsAnalysisCase 'As SimResultsAnalysisCase
                |   Set oResultsAnalysisCase = oResultsAnalysisCases.Item(1)
                |  
                | 
                | See also:
                |     SimResultsManager
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def job_diagnostic_summary(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property JobDiagnosticSummary() As CATBaseDispatch (Read Only)
                |     Returns the SimJobDiagnosticSummary.

        :return: AnyObject
        """

        return AnyObject(self.com_object.JobDiagnosticSummary)

    @property
    def results_steps(self) -> SimResultsSteps:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ResultsSteps() As SimResultsSteps (Read Only)
                |     Returns the available steps.
                | 
                |     See also:
                |         SMAIAMpaResultsSteps

        :return: SimResultsSteps
        """

        return SimResultsSteps(self.com_object.ResultsSteps)

    @property
    def scenario_analysis_case(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ScenarioAnalysisCase() As CATBaseDispatch (Read Only)
                |     Returns the scenario analysis case. The actual returned type could be
                |     either SimThermalAnalysisCase or
                |     SimStructuralAnalysisCase depending on the type of analysis that was
                |     run.
                | 
                |     Parameters:
                | 
                |         ospScenarioAnalysisCase
                |             The analysis case.

        :return: AnyObject
        """

        return AnyObject(self.com_object.ScenarioAnalysisCase)

    def add_field_plot_definitions(self, ilcs_files: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2026-02-08 14:05:01.675948))
                | Sub AddFieldPlotDefinitions(CATSafeArrayVariant ilcsFiles)
                |     Adds the Field Plot definitions .xml files. It is OK to add the same file
                |     multiple times, but you will have to call RemoveFieldPlotDefinitions just as
                |     many times to have those definitions ignored.
                |
                |     Parameters:
                |
                |         ilcsFiles
                |             Name(s) of the Field Plot defintion XML files. The string for a
                |             filename can
                |             begin with an environment variable which will be treated like a
                |             'path'.
                |             Example:
                |             $CATReffilesPath/FEM/SMAHvcModelDescription.xml

        :param tuple ilcs_files:
        :return: None
        """
        return self.com_object.AddFieldPlotDefinitions(ilcs_files)
        # todo: check this method, does it require system service?
        # Autogenerated comment:
        # some methods require a system service call as the methods expects a vb array object
        # passed to it and there is no way to do this directly with python. In those cases the following code
        # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # vba_function_name = 'add_field_plot_definitions'
        # vba_code = """
        # Public Function add_field_plot_definitions(sim_results_analysis_case)
        #     Dim ilcsFiles (2)
        #     sim_results_analysis_case.AddFieldPlotDefinitions ilcsFiles
        #     add_field_plot_definitions = ilcsFiles
        # End Function
        # """

        # system_service = SystemService(self.application.SystemService)
        # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def create_buckle_mode_sensor(self) -> SimBuckleModeSensor:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func CreateBuckleModeSensor() As SimBuckleModeSensor
                |     Creates a BuckleMode Sensor.
                | 
                |     Returns:
                |         Creates and returns the BuckleMode Sensor object

        :return: SimBuckleModeSensor
        """
        return SimBuckleModeSensor(self.com_object.CreateBuckleModeSensor())

    def create_custom_plot_by_id(self, ics_plot_id: str) -> SimFieldPlot:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func CreateCustomPlotByID(CATBSTR icsPlotId) As SimFieldPlot
                |     Creates a Field Plot as defined in a plot definition XML file. Also the
                |     user can set any user definations for the plot. User will have to call the
                |     Get/Set SimFieldPlot::FieldDefination() to set any extra defination value for
                |     the plot. The SimFieldPlot::ActivationStatus() can be called to set the
                |     actiation status. The plot is not refreshed after creation. The
                |     SimFieldPlot::Refresh() method has to be called.
                | 
                |     Parameters:
                | 
                |         icsPlotId
                |             The ID of the Plot as specified in the XML file 
                | 
                |     Returns:
                |         Returns an interface to the created Field Plot

        :param str ics_plot_id:
        :return: SimFieldPlot
        """
        return SimFieldPlot(self.com_object.CreateCustomPlotByID(ics_plot_id))

    def create_export_field_from_plot(self, ip_field_plot: SimFieldPlot) -> SimExportField:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func CreateExportFieldFromPlot(SimFieldPlot ipFieldPlot) As
                | SimExportField
                |     Creates a export field plot.
                | 
                |     Parameters:
                | 
                |         ipFieldPlot
                |             Field plot to export 
                | 
                |     Returns:
                |         The Export Field Plot object

        :param SimFieldPlot ip_field_plot:
        :return: SimExportField
        """
        return SimExportField(self.com_object.CreateExportFieldFromPlot(ip_field_plot.com_object))

    def create_field_plot(self, ie_plot_type: int) -> SimFieldPlot:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func CreateFieldPlot(SimFieldPlotTypes iePlotType) As
                | SimFieldPlot
                |     Creates a user defined Field Plot. User will have to call the Get/Set
                |     SimFieldPlot::FieldDefination() to set all the values for the plot. The plot is
                |     not refreshed after creation. The SimFieldPlot::Refresh() method has to be
                |     called.
                | 
                |     Parameters:
                | 
                |         iePlotType
                |             The type of plot to be created such as countour, symbol,
                |             iso-countour, color code. All the type are specified in
                |             SMAIAMpaFieldPlotTypeEnums.idl file. 
                | 
                |     Returns:
                |         Returns an interface to the created Field Plot

        :param int ie_plot_type:
        :return: SimFieldPlot
        """
        return SimFieldPlot(self.com_object.CreateFieldPlot(ie_plot_type))

    def create_field_plot_by_id(self, ics_data_display_id: str, icb_activate: bool) -> SimFieldPlot:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func CreateFieldPlotByID(CATBSTR icsDataDisplayId,boolean icbActivate) As
                | SimFieldPlot
                |     Creates a Field Plot as defined in a plot definition XML file. The plot is
                |     refreshed immediately after creation.
                | 
                |     Parameters:
                | 
                |         icsDataDisplayId
                |             The ID of the Plot as specified in the XML file 
                |         icbActivate
                |             If passed as TRUE, the Field Plot will be displayed once it is
                |             created. The default is FALSE 
                | 
                |     Returns:
                |         Returns an interface to the created Field Plot

        :param str ics_data_display_id:
        :param bool icb_activate:
        :return: SimFieldPlot
        """
        return SimFieldPlot(self.com_object.CreateFieldPlotByID(ics_data_display_id, icb_activate))

    def create_frame_selector(self) -> SimFramesSelection:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func CreateFrameSelector() As SimFramesSelection
                |     Creates a frame selection.
                | 
                |     Returns:
                |         Creates and returns frame selection object

        :return: SimFramesSelection
        """
        return SimFramesSelection(self.com_object.CreateFrameSelector())

    def create_frequency_sensor(self) -> SimFrequencySensor:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func CreateFrequencySensor() As SimFrequencySensor
                |     Creates a frequency sensor.
                | 
                |     Returns:
                |         Creates and returns the frequency sensor object

        :return: SimFrequencySensor
        """
        return SimFrequencySensor(self.com_object.CreateFrequencySensor())

    def create_history_plot(self) -> SimHistoryPlot:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func CreateHistoryPlot() As SimHistoryPlot
                |     Creates a History Plot.
                | 
                |     Returns:
                |         Creates and returns the History Plot object.

        :return: SimHistoryPlot
        """
        return SimHistoryPlot(self.com_object.CreateHistoryPlot())

    def create_resultant_sensor(self) -> SimResultantSensor:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func CreateResultantSensor() As SimResultantSensor
                |     Creates a resultant sensor.
                | 
                |     Returns:
                |         Creates and returns the resultant sensor object

        :return: SimResultantSensor
        """
        return SimResultantSensor(self.com_object.CreateResultantSensor())

    def create_sensor(self) -> SimSensor:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func CreateSensor() As SimSensor
                |     Creates a basic sensor.
                | 
                |     Returns:
                |         Creates and returns the basic sensor object

        :return: SimSensor
        """
        return SimSensor(self.com_object.CreateSensor())

    def create_sensor_by_id(self, ics_sensor_id: str) -> SimSensor:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func CreateSensorByID(CATBSTR icsSensorID) As SimSensor
                |     Creates a sensor using field plot definition defined in XML description
                |     library files.
                | 
                |     Parameters:
                | 
                |         icsSensorID
                |             The ID of the Field Plot as specified in the XML file as sensor ID.
                |             
                | 
                |     Returns:
                |         The new Sensor object.

        :param str ics_sensor_id:
        :return: SimSensor
        """
        return SimSensor(self.com_object.CreateSensorByID(ics_sensor_id))

    def delete_feature(self, isp_results_object: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub DeleteFeature(CATBaseDispatch ispResultsObject)
                |     Deletes an object created by this factory.
                | 
                |     Parameters:
                | 
                |         ispResultsObject
                |             The results object to delete

        :param AnyObject isp_results_object:
        :return: None
        """
        return self.com_object.DeleteFeature(isp_results_object.com_object)

    def export_sensor_output_to_file(
            self,
            il_sensors: tuple,
            ics_file_name: str,
            ics_file_location: str,
            ie_file_type: SimFileType,
            ib_axis_data: bool,
            ie_column_sep: SimColumnSeparator
    ) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2026-02-08 14:05:01.675948))
                | Sub ExportSensorOutputToFile(CATSafeArrayVariant ilSensors,CATBSTR
                | icsFileName,CATBSTR icsFileLocation,SimFileType ieFileType,boolean
                | ibAxisData,SimColumnSeparator ieColumnSep)
                |     Exports sensor output to a file on disk.
                |
                |     Parameters:
                |
                |         ilSensors:
                |             The sensors whose output is to be exported.
                |         icsFileName:
                |             The name of the file.
                |         icsFileLocation:
                |             The path of the file.
                |         ieFileType:
                |             The file type.
                |         ibAxisData:
                |             Whether to export the axis directions. It is applicable only for
                |             resultant sensor. For other sensors, it will be ignored.
                |
                |         ieColumnSep:
                |             Column separator.
                |
                |     Returns:
                |         S_OK on success, E_UNEXPECTED on failure.

        :param tuple il_sensors:
        :param str ics_file_name:
        :param str ics_file_location:
        :param SimFileType ie_file_type:
        :param bool ib_axis_data:
        :param SimColumnSeparator ie_column_sep:
        :return: None
        """
        return self.com_object.ExportSensorOutputToFile(
            il_sensors,
            ics_file_name,
            ics_file_location,
            ie_file_type.com_object,
            ib_axis_data,
            ie_column_sep.com_object
        )
        # todo: check this method, does it require system service?
        # Autogenerated comment:
        # some methods require a system service call as the methods expects a vb array object
        # passed to it and there is no way to do this directly with python. In those cases the following code
        # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # vba_function_name = 'export_sensor_output_to_file'
        # vba_code = """
        # Public Function export_sensor_output_to_file(sim_results_analysis_case)
        #     Dim ilSensors (2)
        #     sim_results_analysis_case.ExportSensorOutputToFile ilSensors
        #     export_sensor_output_to_file = ilSensors
        # End Function
        # """

        # system_service = SystemService(self.application.SystemService)
        # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def export_sensor_output_to_plm(
            self,
            il_sensors: tuple,
            ics_file_name: str,
            ie_file_type: SimFileType,
            ib_axis_data: bool,
            ie_column_sep: SimColumnSeparator
    ) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2026-02-08 14:05:01.675948))
                | Sub ExportSensorOutputToPLM(CATSafeArrayVariant ilSensors,CATBSTR
                | icsFileName,SimFileType ieFileType,boolean ibAxisData,SimColumnSeparator
                | ieColumnSep)
                |     Exports sensor output as PLM document.
                |
                |     Parameters:
                |
                |         ilSensors:
                |             The sensors whose output is to be exported.
                |         icsFileName:
                |             The name of the file.
                |         ieFileType:
                |             The file type.
                |         ibAxisData:
                |             Whether to export the axis directions. It is applicable only for
                |             resultant sensor. For other sensors, it will be ignored.
                |
                |         ieColumnSep:
                |             Column separator.
                |
                |     Returns:
                |         S_OK on success, E_UNEXPECTED on failure.

        :param tuple il_sensors:
        :param str ics_file_name:
        :param SimFileType ie_file_type:
        :param bool ib_axis_data:
        :param SimColumnSeparator ie_column_sep:
        :return: None
        """
        return self.com_object.ExportSensorOutputToPLM(
            il_sensors,
            ics_file_name,
            ie_file_type.com_object,
            ib_axis_data,
            ie_column_sep.com_object
        )
        # todo: check this method, does it require system service?
        # Autogenerated comment:
        # some methods require a system service call as the methods expects a vb array object
        # passed to it and there is no way to do this directly with python. In those cases the following code
        # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # vba_function_name = 'export_sensor_output_to_plm'
        # vba_code = """
        # Public Function export_sensor_output_to_plm(sim_results_analysis_case)
        #     Dim ilSensors (2)
        #     sim_results_analysis_case.ExportSensorOutputToPLM ilSensors
        #     export_sensor_output_to_plm = ilSensors
        # End Function
        # """

        # system_service = SystemService(self.application.SystemService)
        # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_list_of_field_plot_ids(
            self,
            il_fields: tuple,
            ib_include_defaults: bool,
            ib_include_und_mesh: bool,
            ol_field_plot_ids: tuple
    ) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2026-02-08 14:05:01.675948))
                | Sub GetListOfFieldPlotIDs(CATSafeArrayVariant ilFields,boolean
                | ibIncludeDefaults,boolean ibIncludeUndMesh,CATSafeArrayVariant
                | olFieldPlotIds)
                |     Gets a list of creatable Field Plot IDs from the plot definition
                |     files.
                |     Read the Field Plot definition files specified in calls to AddField
                |     PlotDefinitions and, optionally, the default definitions, and return a list of
                |     Field Plot Ids for the defined Field Plots. The returned list can be filtered
                |     to only include Field Plot Ids for which all required fields appear is a
                |     provided list of fields. It is always filtered to only include Field Plot Ids
                |     for Plots that are completely supported by the available
                |     data.
                |
                |     Parameters:
                |
                |         ilFields
                |             If an empty list, the list of existing fields in the model is
                |             used.
                |             The returned list of Field Plot Ids is filtered to exclude the Ids
                |             of Field Plots
                |             referencing fields that are not in the list or fields that are not
                |             in the model
                |         olPlotIds
                |             The returned list of Field Plot Id strings.
                |         ibIncludeDefaults
                |             If TRUE (default) include the internal Field Plot definitions
                |             in
                |             addition to definitions passed to AddField PlotDefinitions.
                |
                |         ibIncludeUndMesh
                |             If TRUE (default) and ibIncludeDefaults is TRUE, include
                |             the
                |             Field Plot Id for the undeformed mesh.

        :param tuple il_fields:
        :param bool ib_include_defaults:
        :param bool ib_include_und_mesh:
        :param tuple ol_field_plot_ids:
        :return: None
        """
        return self.com_object.GetListOfFieldPlotIDs(
            il_fields,
            ib_include_defaults,
            ib_include_und_mesh,
            ol_field_plot_ids
        )
        # todo: check this method, does it require system service?
        # Autogenerated comment:
        # some methods require a system service call as the methods expects a vb array object
        # passed to it and there is no way to do this directly with python. In those cases the following code
        # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # vba_function_name = 'get_list_of_field_plot_i_ds'
        # vba_code = """
        # Public Function get_list_of_field_plot_i_ds(sim_results_analysis_case)
        #     Dim ilFields (2)
        #     sim_results_analysis_case.GetListOfFieldPlotIDs ilFields
        #     get_list_of_field_plot_i_ds = ilFields
        # End Function
        # """

        # system_service = SystemService(self.application.SystemService)
        # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_set(self, ie_set_type: str) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetSet(CATBSTR ieSetType) As CATBaseDispatch
                |     Gets a list of result features created within this
                |     Manager.
                | 
                |     Parameters:
                | 
                |         ieSetType
                |             The type of Set to access such as field plot, sensors, frequency
                |             sensors and resultant sensors. The keyword for various sets are as follows: 1.
                |             Field plot set: "FieldPlotSet". 2. Sensor set: "SensorSet". 3. Resultant sensor
                |             set: "ResultantSensorSet". 4. Frequency sensor set: "FrequencySensorSet". 5.
                |             BuckleMode sensor set: "BuckleModeSensorSet". 6. Historyplot set:
                |             "HistoryPlotSet". 7. User csys set: "UserCsysSet". 8. Display group set:
                |             "DisplayGroupSet". 
                | 
                |     Returns:
                |         The set of specified results feature.
                | 
                |         Example:
                |             The following example returns in FieldPlotSet the field plot set
                |             created in MyResultsAnalysisCase :
                | 
                |              Dim MyResultsAnalysisCase As
                |              SimResultsAnalysisCase
                |              Set MyResultsAnalysisCase = ...
                |              Dim FieldPlotsResultsSet As SimResultsSet
                |              Set FieldPlotsResultsSet = MyResultsAnalysisCase.GetSet("FieldPlotSet")

        :param str ie_set_type:
        :return: AnyObject
        """
        return self.com_object.GetSet(ie_set_type)

    def remove_field_plot_definitions(self, ilcs_files: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2026-02-08 14:05:01.675948))
                | Sub RemoveFieldPlotDefinitions(CATSafeArrayVariant ilcsFiles)
                |     Retracts filename(s) of XML file(s) that contain Field Plot
                |     definitions.
                |
                |     Parameters:
                |
                |         ilcsFiles
                |             Name(s) of the Field Plot defintion XML files to no longer consider

        :param tuple ilcs_files:
        :return: None
        """
        return self.com_object.RemoveFieldPlotDefinitions(ilcs_files)
        # todo: check this method, does it require system service?
        # Autogenerated comment:
        # some methods require a system service call as the methods expects a vb array object
        # passed to it and there is no way to do this directly with python. In those cases the following code
        # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # vba_function_name = 'remove_field_plot_definitions'
        # vba_code = """
        # Public Function remove_field_plot_definitions(sim_results_analysis_case)
        #     Dim ilcsFiles (2)
        #     sim_results_analysis_case.RemoveFieldPlotDefinitions ilcsFiles
        #     remove_field_plot_definitions = ilcsFiles
        # End Function
        # """

        # system_service = SystemService(self.application.SystemService)
        # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'SimResultsAnalysisCase(name="{self.name}")'
