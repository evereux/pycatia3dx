"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.sma_mpa_foundation.sim_feature_history import SimFeatureHistory
from pycatia3dx.system.any_object import AnyObject


class SimOutput(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimOutput
                | 
                | Represents the Output object.
                | The examples below use the SimFieldOutput object. The same pattern applies to
                | SimHistoryOutput.
                | 
                | Example:
                |     Given a SimFeatures object, you can create a SimOutput as
                |     following:
                | 
                |      Dim MyFeatures As SimFeatures
                |      ...
                |      Dim MyOutput As SimOutput
                |      Set MyOutput = MyFeatures.Add("SimFieldOutput")
                |      
                | 
                |     Given a SimFeatures object, you can retrieve a SimOutput named "Output.1"
                |     as following:
                | 
                |      Dim MyFeatures As SimFeatures
                |      ...
                |      Dim MyOutput As SimOutput
                |      Set MyOutput = MyFeatures.Item("Output.1")
                |      
                | 
                | Example in Python:
                |     Given a SimFeatures object myFeatures, you can create a SimOutput as
                |     following:
                | 
                |      ...
                |      myOutput = myFeatures.Add("SimFieldOutput")
                |      
                | 
                |     Given a SimFeatures object myFeatures, you can retrieve a SimOutput named
                |     "Output.1" as following:
                | 
                |      ...
                |      myOutput = myFeatures.Item("Output.1")
                |      
                | 
                | See also:
                |     SimFeatures
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def activated(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Activated() As boolean
                |     Returns or sets the activation status.

        :return: bool
        """

        return self.com_object.Activated

    @activated.setter
    def activated(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.Activated = value

    @property
    def exact_time_flag(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ExactTimeFlag() As boolean
                |     Returns or sets the flag that determines if the results are saved at the
                |     exact time.
                |     TRUE: the results are saved at the exact time.
                |     FALSE: the results are saved at the increment ending immediately after the
                |     time.

        :return: bool
        """

        return self.com_object.ExactTimeFlag

    @exact_time_flag.setter
    def exact_time_flag(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.ExactTimeFlag = value

    @property
    def feature_history(self) -> SimFeatureHistory:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property FeatureHistory() As SimFeatureHistory (Read Only)
                |     Returns the feature history.

        :return: SimFeatureHistory
        """

        return SimFeatureHistory(self.com_object.FeatureHistory)

    @property
    def frequency_increments(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property FrequencyIncrements() As long
                |     Output frequency in increments.

        :return: int
        """

        return self.com_object.FrequencyIncrements

    @frequency_increments.setter
    def frequency_increments(self, value: int):
        """
        :param int value:
        """

        self.com_object.FrequencyIncrements = value

    @property
    def frequency_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property FrequencyType() As SimOutputFrequencyType
                |     Returns or sets the output request frequency.

        :return: SimOutputFrequencyType
        """

        return self.com_object.FrequencyType

    @frequency_type.setter
    def frequency_type(self, value: int):
        """
        :param int value:
        """

        self.com_object.FrequencyType = value

    @property
    def list_of_output_variables(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ListOfOutputVariables() As CATSafeArrayVariant (Read
                | Only)
                |     Returns the list of output variable identifiers.

        :return: tuple
        """

        return self.com_object.ListOfOutputVariables

    @property
    def location(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Location() As SimOutputElementLocation
                |     Returns or sets the Element Location enum.

        :return: SimOutputElementLocation
        """

        return self.com_object.Location

    @location.setter
    def location(self, value: int):
        """
        :param int value:
        """

        self.com_object.Location = value

    @property
    def number_interval(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property NumberInterval() As long
                |     Number of intervals during the step at which output is to be saved.

        :return: int
        """

        return self.com_object.NumberInterval

    @number_interval.setter
    def number_interval(self, value: int):
        """
        :param int value:
        """

        self.com_object.NumberInterval = value

    @property
    def output_group(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property OutputGroup() As SimOutputOutputGroup (Read Only)
                |     Returns the output group of the selected output, which can be either field
                |     or history.

        :return: SimOutputOutputGroup
        """

        return self.com_object.OutputGroup

    @property
    def section_point_selection_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property SectionPointSelectionType() As
                | SimOutputSectionPointSelectionType
                |     Returns or sets the section point selection type.

        :return: SimOutputSectionPointSelectionType
        """

        return self.com_object.SectionPointSelectionType

    @section_point_selection_type.setter
    def section_point_selection_type(self, value: int):
        """
        :param int value:
        """

        self.com_object.SectionPointSelectionType = value

    @property
    def section_points(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property SectionPoints() As CATSafeArrayVariant
                |     Returns or sets the sections points.

        :return: tuple
        """

        return self.com_object.SectionPoints

    @section_points.setter
    def section_points(self, value: tuple):
        """
        :param tuple value:
        """

        self.com_object.SectionPoints = value

    @property
    def spec_tree_category(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property SpecTreeCategory() As CATBSTR (Read Only)
                |     Returns a string representing the specification tree category of the
                |     feature. See SimFeatures.GetSpecTreeCategory for usage.

        :return: str
        """

        return self.com_object.SpecTreeCategory

    @property
    def time_interval(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property TimeInterval() As double
                |     Time interval at which output is to be saved.

        :return: float
        """

        return self.com_object.TimeInterval

    @time_interval.setter
    def time_interval(self, value: float):
        """
        :param float value:
        """

        self.com_object.TimeInterval = value

    def add_output_variable(self, i_variable_identifier: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub AddOutputVariable(CATBSTR iVariableIdentifier)
                |     Adds an output variable.
                | 
                |     Parameters:
                | 
                |         iVariableIdentifier[in]
                |             The identifier of the output variable to add. Check the UI and/or
                |             main documentation for the list of authorized values. Examples of valid strings
                |             are: "S" for stress components, "S11" for Stress component 11, "SP" for
                |             Principal Stresses, "U" for Translations and Rotations, etc.

        :param str i_variable_identifier:
        :return: None
        """
        return self.com_object.AddOutputVariable(i_variable_identifier)

    def get_section_point_by_layer(self, o_top: bool, o_middle: bool, o_bottom: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetSectionPointByLayer(boolean oTop,boolean oMiddle,boolean
                | oBottom)
                |     Retrieves the section points by layer.
                |     Only applicable when the section point selection type is
                |     ByLayer.
                | 
                |     Parameters:
                | 
                |         oTop[out]
                |         oMiddle[out]
                |         oBottom[out]

        :param bool o_top:
        :param bool o_middle:
        :param bool o_bottom:
        :return: None
        """
        return self.com_object.GetSectionPointByLayer(o_top, o_middle, o_bottom)

    def remove_output_variable(self, i_variable_identifier: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub RemoveOutputVariable(CATBSTR iVariableIdentifier)
                |     Removes an output variable.
                | 
                |     Parameters:
                | 
                |         iVariableIdentifier[in]
                |             The identifier of the output variable to remove. Check the UI
                |             and/or main documentation for the list of authorized values. Examples of valid
                |             strings are: "S" for stress components, "S11" for Stress component 11, "SP" for
                |             Principal Stresses, "U" for Translations and Rotations, etc.

        :param str i_variable_identifier:
        :return: None
        """
        return self.com_object.RemoveOutputVariable(i_variable_identifier)

    def set_section_point_by_layer(self, i_top: bool, i_middle: bool, i_bottom: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetSectionPointByLayer(boolean iTop,boolean iMiddle,boolean
                | iBottom)
                |     Sets the section points by layer.
                |     Only applicable is the section point selection type is
                |     ByLayer.
                | 
                |     Parameters:
                | 
                |         iTop[in]
                |         iMiddle[in]
                |         iBottom[in]

        :param bool i_top:
        :param bool i_middle:
        :param bool i_bottom:
        :return: None
        """
        return self.com_object.SetSectionPointByLayer(i_top, i_middle, i_bottom)

    def __repr__(self):
        return f'SimOutput(name="{ self.name }")'
