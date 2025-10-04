"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class SimHistoryPlot(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimHistoryPlot
                | 
                | Represents the history plot.
                | Role:After creating the history plot feature using the
                | SimResultsAnalysisCase::CreateHistoryPlot. Then set the different API's
                | provided in this interface and update the history plot using and the
                | SimHistoryPlot.Update() method.
                | Example:
                | 
                |  Given a SimResultsAnalysisCase object, you can create a Sensor object as
                |  following.
                |  
                | 
                |  Dim oHistoryPlot As SimHistoryPlot
                |  Set oHistoryPlot = oResultsAnalysisCase.CreateHistoryPlot
                |  oHistoryPlot.Variable = "ALLAE"
                |  oHistoryPlot.InvariantQuantity = SimScalar
                |  oHistoryPlot.SetAllTimeBasedSteps
                |  oSensor.Update
                |  
                | 
                | See also:
                |     SimResultsAnalysisCase
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def activation_status(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ActivationStatus() As boolean
                |     Sets and gets the activation status of the history plot. When activated the
                |     history plot is displayed in the 2D viewer. When deactivated the history plot
                |     is not displayed in the 2D viewer.

        :return: bool
        """

        return self.com_object.ActivationStatus

    @activation_status.setter
    def activation_status(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.ActivationStatus = value

    @property
    def component_quantity(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ComponentQuantity(SimQuantityComponentEnum ieComponent) (Write
                | Only)
                |     Sets the component type for the quantity. Refer the
                |     SMAIAMpaQuantityEnums.idl file all the available enum types.

        :return: bool
        """

        return self.com_object.ComponentQuantity

    @component_quantity.setter
    def component_quantity(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.ComponentQuantity = value

    @property
    def invariant_quantity(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property InvariantQuantity(SimQuantityInvariantEnum ieInvariant) (Write
                | Only)
                |     Sets the invariant type for the quantity. Refer the
                |     SMAIAMpaQuantityEnums.idl file all the available enum types.

        :return: bool
        """

        return self.com_object.InvariantQuantity

    @invariant_quantity.setter
    def invariant_quantity(self, value: bool):
        """
        :param False value:
        """

        self.com_object.InvariantQuantity = value

    @property
    def variable(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Variable(CATBSTR icsVariableType) (Write Only)
                |     Specifies the variable on which the sensor is to be created. For example
                |     the variable can be S, RT, UT etc.

        :return: str
        """

        return self.com_object.Variable

    @variable.setter
    def variable(self, value: str):
        """
        :param str value:
        """

        self.com_object.Variable = value

    def get_history_curve_list(self, ols_history_curves: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetHistoryCurveList(CATSafeArrayVariant olsHistoryCurves)
                |     Returns the list of curves present in the history plot.
                | 
                |     Parameters:
                | 
                |         olsHistoryCurves
                |             [out] Returns list of the curves.

        :param tuple ols_history_curves:
        :return: None
        """
        return self.com_object.GetHistoryCurveList(ols_history_curves)

    def get_min_max_values(self, od_min: float, od_max: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetMinMaxValues(double odMin,double odMax)
                |     Returns the minimum and maximum values. It considers all the curves and
                |     gives the absolute min and max value.
                | 
                |     Parameters:
                | 
                |         odMin
                |             Returns the minimum value. 
                |         odMax
                |             Returns the maximum value.

        :param float od_min:
        :param float od_max:
        :return: None
        """
        return self.com_object.GetMinMaxValues(od_min, od_max)

    def set_all_time_based_steps(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetAllTimeBasedSteps()
                |     Sets the all the time based steps available. Suppose there are two static
                |     steps, then this option will create a curve that will have the combined range
                |     of step 1 and step 2.

        :return: None
        """
        return self.com_object.SetAllTimeBasedSteps()

    def set_complex(self, ie_complex_value: int, i_value_at_angle: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetComplex(SimComplexValues ieComplexValue,double
                | iValueAtAngle)
                |     Sets the complex type and angle. The complex options are dependent on the
                |     complex options that are set while creating the step.
                | 
                |     Parameters:
                | 
                |         ieComplexValue
                |             Sets the complex type. The available options can be found in
                |             SMAIAMpaSensorEnums.idl 
                |         iValueAtAngle
                |             Sets the complex angle value. Specify the value of the angle. To be
                |             set only when SimComplexValues::SimValueAtAngle option is used for setting the
                |             complex value.

        :param int ie_complex_value:
        :param float i_value_at_angle:
        :return: None
        """
        return self.com_object.SetComplex(ie_complex_value, i_value_at_angle)

    def set_step_and_frame(self, ics_persistent_step_id: str, in_frame_index: int, in_load_case_index: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetStepAndFrame(CATBSTR icsPersistentStepID,long inFrameIndex,long
                | inLoadCaseIndex)
                |     Sets the step, frame and load case information needed to create the history
                |     plot.
                | 
                |     Parameters:
                | 
                |         icsPersistentStepID
                |             The persistent ID of the step. 
                |         inFrameIndex
                |             The frame index. The index starts from 1. This option is needed
                |             only in case of multiple load cases. 
                |         inLoadCaseIndex
                |             The load case index. The index starts from 1. It is needed if a
                |             load case is present in the step.

        :param str ics_persistent_step_id:
        :param int in_frame_index:
        :param int in_load_case_index:
        :return: None
        """
        return self.com_object.SetStepAndFrame(ics_persistent_step_id, in_frame_index, in_load_case_index)

    def set_support(self, ils_regions: tuple, ilnb_sub_region_indices: tuple, ils_sub_regions: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetSupport(CATSafeArrayVariant ilsRegions,CATSafeArrayVariant
                | ilnbSubRegionIndices,CATSafeArrayVariant ilsSubRegions)
                |     Sets the support for creating the history plot such as regions and
                |     sub-regions. One curve per sub-region will be created in the same plot. a) No
                |     need to call this method if the hisoty plot is to be created on the whole model
                |     since there are no supports to be selected. b) In case of supports available
                |     all the three parameters must be set.
                | 
                |     Parameters:
                | 
                |         ilsRegions
                |             It is the list of strings which specifies the name of the
                |             region(s). 
                |         ilnbSubRegionIndices
                |             It is the list of integers. Specifies the number of sub-regions
                |             selected in a region. For example if "Region 1" and "Region 2" is selected and
                |             one needs to select 2 and 3 sub-regions respectively from the regions, one will
                |             have to specify it as [2,3]. 
                |         ilsSubRegions
                |             Specifies the name of the sub-regions. For example "Node 1".

        :param tuple ils_regions:
        :param tuple ilnb_sub_region_indices:
        :param tuple ils_sub_regions:
        :return: None
        """
        return self.com_object.SetSupport(ils_regions, ilnb_sub_region_indices, ils_sub_regions)

    def update(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub Update()
                | 
                |     Deprecated:
                |         Use the UpdateAndView() method.

        :return: None
        """
        return self.com_object.Update()

    def update_and_view(self, ib_show_viewer: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub UpdateAndView(boolean ibShowViewer)
                |     Creates and displays the history plot in the XY viewer. This method needs
                |     to be called at the end after setting all the above
                |     attributes.
                | 
                |     Parameters:
                | 
                |         ibShowViewer
                |             If set true, the plots will be displayed in the XY viewer. If set
                |             false, only the history plot will be created. The user will have to manually
                |             view the plots. 

        :param bool ib_show_viewer:
        :return: None
        """
        return self.com_object.UpdateAndView(ib_show_viewer)

    def __repr__(self):
        return f'SimHistoryPlot(name="{ self.name }")'
