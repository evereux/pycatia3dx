"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.sma_mpa_results.sim_sensor_output_parameters import SimSensorOutputParameters
from pycatia3dx.system.any_object import AnyObject


class SimHistorySensor(AnyObject):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimHistorySensor
                | 
                | Represents the history sensor.
                | Role:Creating the history sensor feature using the
                | SimHistorySensorFactory::CreateSensor. Then set the different API's provided in
                | this interface and update the history sensor using and the
                | SimHistorySensor.Update() method.
                | Example:
                | 
                |  Given a SimResultsAnalysisCase object, you can create a Sensor object as
                |  following.
                |  
                | 
                |  Dim oHistorySensor As SimHistorySensor
                |  Set oHistorySensor = oResultsAnalysisCase.CreateHistorySensor
                |  oHistorySensor.Variable = "ALLAE"
                |  oHistorySensor.InvariantQuantity = SimScalar
                |  oHistorySensor.SetAllTimeBasedSteps
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
    def component_quantity(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ComponentQuantity(SimQuantityComponentEnum ieComponent) (Write
                | Only)
                |     Sets the component type for the quantity. Refer the
                |     SMAIAMpaQuantityEnums.idl file all the available enum types.

        :return: int
        """

        return self.com_object.ComponentQuantity

    @component_quantity.setter
    def component_quantity(self, value: int):
        """
        :param int value:
        """

        self.com_object.ComponentQuantity = value

    @property
    def invariant_quantity(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property InvariantQuantity(SimQuantityInvariantEnum ieInvariant) (Write
                | Only)
                |     Sets the invariant type for the quantity. Refer the
                |     SMAIAMpaQuantityEnums.idl file all the available enum types.

        :return: int
        """

        return self.com_object.InvariantQuantity

    @invariant_quantity.setter
    def invariant_quantity(self, value: int):
        """
        :param int value:
        """

        self.com_object.InvariantQuantity = value

    @property
    def last_value(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property LastValue(boolean ibFlag) (Write Only)
                |     Creates the parameter for the last value. The parameter will be created
                |     only if a single sub-region is specified through SetSupport() API. If there are
                |     no regions and sub-regions, the last value will be created for whole model.

        :return: bool
        """

        return self.com_object.LastValue

    @last_value.setter
    def last_value(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.LastValue = value

    @property
    def sensor_output_parameter(self) -> SimSensorOutputParameters:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property SensorOutputParameter() As SimSensorOutputParameters
                |     Gets/Sets the sensor output parameters object.
                |     Refer @see #SMAIAMpaSensorOutputParameters about how to set the different
                |     parameter creation criteria.

        :return: SimSensorOutputParameters
        """

        return SimSensorOutputParameters(self.com_object.SensorOutputParameter)

    @sensor_output_parameter.setter
    def sensor_output_parameter(self, value: SimSensorOutputParameters):
        """
        :param SimSensorOutputParameters value:
        """

        self.com_object.SensorOutputParameter = value

    @property
    def variable(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Variable(CATBSTR icsVariableType) (Write Only)
                |     Specifies the variable on which the history sensor is to be created. For
                |     example the variable can be S, RT, UT etc.

        :return: str
        """

        return self.com_object.Variable

    @variable.setter
    def variable(self, value: str):
        """
        :param False value:
        """

        self.com_object.Variable = value

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

        :param ie_complex_value:
        :param float i_value_at_angle:
        :return: None
        """
        return self.com_object.SetComplex(ie_complex_value, i_value_at_angle)

    def set_parameters(self, ib_max_flag: bool, ib_min_flag: bool, ib_absolute_max_flag: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetParameters(boolean ibMaxFlag,boolean ibMinFlag,boolean
                | ibAbsoluteMaxFlag)
                |     Sets the parameters for which the values are to be
                |     calculated.
                | 
                |     Parameters:
                | 
                |         ibMaxFlag
                |             Set true to create the maximum extrema parameter. 
                |         ibMinFlag
                |             Set true to create the minimum extrema parameter. 
                |         ibAbsoluteMaxFlag
                |             Set true to create the absolute maximum extrema parameter.

        :param bool ib_max_flag:
        :param bool ib_min_flag:
        :param bool ib_absolute_max_flag:
        :return: None
        """
        return self.com_object.SetParameters(ib_max_flag, ib_min_flag, ib_absolute_max_flag)

    def set_step_and_frame(self, ics_persistent_step_id: str, in_frame_index: int, in_load_case_index: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetStepAndFrame(CATBSTR icsPersistentStepID,long inFrameIndex,long
                | inLoadCaseIndex)
                |     Sets the step, frame and load case information needed to create the history
                |     Sensor.
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

            3DEXPERIENCE Automation Help (2026-02-08 14:05:01.675948))
                | Sub SetSupport(CATSafeArrayVariant ilsRegions,CATSafeArrayVariant
                | ilnbSubRegionIndices,CATSafeArrayVariant ilsSubRegions)
                |     Sets the support for creating the history Sensor such as regions and
                |     sub-regions. a) No need to call this method if the history sensor is to be
                |     created on the whole model since there are no supports to be selected. b) In
                |     case of supports available all the three parameters must be
                |     set.
                |
                |     Parameters:
                |
                |         ilsRegions
                |             It is the array of strings which specifies the name of the
                |             region(s).
                |         ilnbSubRegionIndices
                |             It is the array of integers. Specifies the number of sub-regions
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
        # todo: check this method, does it require system service?
        # Autogenerated comment:
        # some methods require a system service call as the methods expects a vb array object
        # passed to it and there is no way to do this directly with python. In those cases the following code
        # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # vba_function_name = 'set_support'
        # vba_code = """
        # Public Function set_support(sim_history_sensor)
        #     Dim ilsRegions (2)
        #     sim_history_sensor.SetSupport ilsRegions
        #     set_support = ilsRegions
        # End Function
        # """

        # system_service = SystemService(self.application.SystemService)
        # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_support2(self, ils_regions: tuple, ilnb_sub_region_indices: tuple, ils_sub_regions: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2026-02-08 14:05:01.675948))
                | Sub SetSupport2(CATSafeArrayVariant ilsRegions,CATSafeArrayVariant
                | ilnbSubRegionIndices,CATSafeArrayVariant ilsSubRegions)
                |     Sets the second support for creating the history Sensor. Calling
                |     SetSupport() is mandatory if the second support is to be set. The
                |     put_SensorOutputParameter() will have to be used to set the parameters if the
                |     second support is specified. a) No need to call this method if the history
                |     sensor is to be created on the whole model on only Support 1 is enough. b) In
                |     case of supports available all the three parameters must be
                |     set.
                |
                |     Parameters:
                |
                |         ilsRegions
                |             It is the array of strings which specifies the name of the
                |             region(s).
                |         ilnbSubRegionIndices
                |             It is the array of integers. Specifies the number of sub-regions
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
        return self.com_object.SetSupport2(ils_regions, ilnb_sub_region_indices, ils_sub_regions)
        # todo: check this method, does it require system service?
        # Autogenerated comment:
        # some methods require a system service call as the methods expects a vb array object
        # passed to it and there is no way to do this directly with python. In those cases the following code
        # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # vba_function_name = 'set_support2'
        # vba_code = """
        # Public Function set_support2(sim_history_sensor)
        #     Dim ilsRegions (2)
        #     sim_history_sensor.SetSupport2 ilsRegions
        #     set_support2 = ilsRegions
        # End Function
        # """

        # system_service = SystemService(self.application.SystemService)
        # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def update(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub Update()
                |     Creates the history sensor. This method needs to be called at the end after
                |     setting all the above attributes. 

        :return: None
        """
        return self.com_object.Update()

    def __repr__(self):
        return f'SimHistorySensor(name="{self.name}")'
