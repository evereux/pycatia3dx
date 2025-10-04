"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.sma_mpa_results.sim_sensor_base import SimSensorBase
from pycatia3dx.sma_mpa_results.sim_sensor_output_parameters import SimSensorOutputParameters


class SimSensor(SimSensorBase):

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
                |                         SimSensor
                | 
                | Represents the sensor.
                | Role:After creating the sensor, one needs set the different API's provided in
                | the Interface.
                | Then set the frame selection to the sensor using the
                | SimSensorBase.FrameSelector()
                | and update the sensor using and the SimSensorBase.Update()
                | method.
                | Example:
                | 
                |  Given a SimResultsAnalysisCase object, you can create a Sensor object as
                |  following.
                |  
                | 
                |  Dim oSensor As SimSensor
                |  Set oSensor = oResultsAnalysisCase.CreateSensor
                |  Dim oFrameSelection As SimFramesSelection
                |  Set oFrameSelection = oResultsAnalysisCase.CreateFrameSelector
                |  oFrameSelection.SymbolicFrameRange = SimAllFrames
                |  oSensor.FrameSelector = oFrameSelection
                |  oSensor.Update
                |  
                | 
                | SimResultsAnalysisCase
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def annotation(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Annotation(boolean ibShow) (Write Only)
                |     Shows the annotation on the sensor. The annotation includes the steps,
                |     frame and parameters information.

        :return: bool
        """

        return self.com_object.Annotation

    @annotation.setter
    def annotation(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.Annotation = value

    @property
    def averaging(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Averaging(SimAveraging ieAveraging) (Write Only)
                |     Sets the option for averaging of values.

        :return: int
        """

        return self.com_object.Averaging

    @averaging.setter
    def averaging(self, value: int):
        """
        :param int value:
        """

        self.com_object.Averaging = value

    @property
    def combine_base_state(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property CombineBaseState(boolean ibCombine) (Write Only)
                |     Includes the base state for perturbation for sensor calculation.

        :return: bool
        """

        return self.com_object.CombineBaseState

    @combine_base_state.setter
    def combine_base_state(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.CombineBaseState = value

    @property
    def complex_value(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ComplexValue(SimComplexValues ieComplexValue) (Write
                | Only)
                |     Sets the complex value.

        :return: int
        """

        return self.com_object.ComplexValue

    @complex_value.setter
    def complex_value(self, value: int):
        """
        :param int value:
        """

        self.com_object.ComplexValue = value

    @property
    def complex_value_at_angle(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ComplexValueAtAngle(double iValueAtAngle) (Write
                | Only)
                |     Sets the complex angle value. Specify the value of the angle. To be set
                |     only when
                |     SimComplexValues::SimValueAtAngle option is used for setting the complex
                |     value.
                | 
                |     See also:
                |         ComplexValue

        :return: int
        """

        return self.com_object.ComplexValueAtAngle

    @complex_value_at_angle.setter
    def complex_value_at_angle(self, value: int):
        """
        :param int value:
        """

        self.com_object.ComplexValueAtAngle = value

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
    def compute_quantity_before_averaging(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ComputeQuantityBeforeAveraging(boolean ibQuantityBeforeAveraging)
                | (Write Only)
                |     Sets the value as True to compute the quantity before averaging.

        :return: bool
        """

        return self.com_object.ComputeQuantityBeforeAveraging

    @compute_quantity_before_averaging.setter
    def compute_quantity_before_averaging(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.ComputeQuantityBeforeAveraging = value

    @property
    def coordinate_system(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property CoordinateSystem(CATBSTR icsCoordinateSystem) (Write
                | Only)
                |     Sets the coordinate system for the transform type. This is the name of the
                |     coordinate system.
                |     To be set if transform type is set as user defined.
                | 
                |     See also:
                |         TransformType

        :return: str
        """

        return self.com_object.CoordinateSystem

    @coordinate_system.setter
    def coordinate_system(self, value: str):
        """
        :param str value:
        """

        self.com_object.CoordinateSystem = value

    @property
    def deformation_effects(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property DeformationEffects(boolean ibDeformationEffects) (Write
                | Only)
                |     Sets the deformation effects.

        :return: bool
        """

        return self.com_object.DeformationEffects

    @deformation_effects.setter
    def deformation_effects(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.DeformationEffects = value

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
    def location(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Location(SimLocation ieLocation) (Write Only)
                |     Sets the location at which the results should be evaluated.

        :return: int
        """

        return self.com_object.Location

    @location.setter
    def location(self, value: int):
        """
        :param int value:
        """

        self.com_object.Location = value

    @property
    def ply_type(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property PlyType(CATBSTR icsPlyType) (Write Only)
                |     Sets the ply type. Complete name of the ply needs to be given.

        :return: str
        """

        return self.com_object.PlyType

    @ply_type.setter
    def ply_type(self, value: str):
        """
        :param str value:
        """

        self.com_object.PlyType = value

    @property
    def principal_direction(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property PrincipalDirection(boolean ibPrincipleDirection) (Write
                | Only)
                |     Sets the Principal directions. Set true to evaluate tensors in the three
                |     principal directions.

        :return: bool
        """

        return self.com_object.PrincipalDirection

    @principal_direction.setter
    def principal_direction(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.PrincipalDirection = value

    @property
    def processing_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ProcessingType(SimProcessingTypes ieProcessingType) (Write
                | Only)
                |     Sets the processing type for the sensor.

        :return: int
        """

        return self.com_object.ProcessingType

    @processing_type.setter
    def processing_type(self, value: int):
        """
        :param int value:
        """

        self.com_object.ProcessingType = value

    @property
    def quantity_type(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property QuantityType(CATBSTR icsQuantity) (Write Only)
                |      @deprecated R425 Use InvariantQuantity or ComponentQuantity Sets the
                |      quantity type.

        :return: str
        """

        return self.com_object.QuantityType

    @quantity_type.setter
    def quantity_type(self, value: str):
        """
        :param str value:
        """

        self.com_object.QuantityType = value

    @property
    def sensor_output_parameter(self) -> SimSensorOutputParameters:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property SensorOutputParameter() As SimSensorOutputParameters
                |     Gets/Sets the sensor output parameters object.
                |     SMAIAMpaSensorOutputParameters about how to set the different parameter
                |     creation criteria.

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
    def transform_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property TransformType(SimTransformTypes ieTransfromType) (Write
                | Only)
                |     Sets the transform type. The transform type can be either none or user
                |     defined.
                |     For user defined, the coordinate system needs to be
                |     specified.
                | 
                |     See also:
                |         CoordinateSystem

        :return: int
        """

        return self.com_object.TransformType

    @transform_type.setter
    def transform_type(self, value: int):
        """
        :param str value:
        """

        self.com_object.TransformType = value

    @property
    def variable_type(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property VariableType(CATBSTR icsVariableType) (Write Only)
                |     Specifies the variable on which the sensor is to be created. For example
                |     the variable can be S, RT, UT etc.

        :return: str
        """

        return self.com_object.VariableType

    @variable_type.setter
    def variable_type(self, value: int):
        """
        :param int value:
        """

        self.com_object.VariableType = value

    def set_parameters(self, ib_max_flag: bool, ib_min_flag: bool, ib_absolute_max_flag: bool, ib_parameter_for_each_step_flag: bool, ib_parameter_for_each_frame_or_load_case_flag: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetParameters(boolean ibMaxFlag,boolean ibMinFlag,boolean
                | ibAbsoluteMaxFlag,boolean ibParameterForEachStepFlag,boolean
                | ibParameterForEachFrameOrLoadCaseFlag)
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
                |             
                |         ibParameterForEachStepFlag
                |             Set true to create the parameters for each step. 
                |         ibParameterForEachFrameOrLoadCaseFlag
                |             Set true to create the parameters for each frame of load case.
                |             
                | 
                |     Returns:
                |         S_OK if successful.

        :param bool ib_max_flag:
        :param bool ib_min_flag:
        :param bool ib_absolute_max_flag:
        :param bool ib_parameter_for_each_step_flag:
        :param bool ib_parameter_for_each_frame_or_load_case_flag:
        :return: None
        """
        return self.com_object.SetParameters(ib_max_flag, ib_min_flag, ib_absolute_max_flag, ib_parameter_for_each_step_flag, ib_parameter_for_each_frame_or_load_case_flag)

    def set_support1(self, i_enum_support_type: int, ilscus_support: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetSupport1(SimSelectionType iEnumSupportType,CATSafeArrayVariant
                | ilscusSupport)
                |     Sets one or more supports for the specified type
                | 
                |     Parameters:
                | 
                |         iEnumSupportType
                |             The support type like Display groups, Node sets, mesh groups etc
                |             
                |         ilscusSupport
                |             Array of support strings or features of specified type
                |             
                | 
                |     Example:
                | 
                |          Dim eSelectionType 'As SimSelectionType
                |          eSelectionType = SimDisplayGroups
                |          oResSensorOptions.SetSupport1 eSelectionType,
                |          MySupports

        :param int i_enum_support_type:
        :param tuple ilscus_support:
        :return: None
        """
        return self.com_object.SetSupport1(i_enum_support_type, ilscus_support)

    def set_support2(self, i_enum_support_type: int, ilscus_support: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetSupport2(SimSelectionType iEnumSupportType,CATSafeArrayVariant
                | ilscusSupport)
                |     Sets one or more string based supports for the specified
                |     type
                | 
                |     Parameters:
                | 
                |         iEnumSupportType
                |             The support type like Display groups, Node sets, mesh groups etc
                |             
                |         ilscusSupport
                |             Array of support strings or features of specified type
                |             
                | 
                |     Example:
                | 
                |           Dim eSelectionType 'As SimSelectionType
                |          eSelectionType = SimDisplayGroups
                |          oResSensorOptions.SetSupport2 eSelectionType,
                |          MySupports

        :param int i_enum_support_type:
        :param tuple ilscus_support:
        :return: None
        """
        return self.com_object.SetSupport2(i_enum_support_type, ilscus_support)

    def __repr__(self):
        return f'SimSensor(name="{ self.name }")'
