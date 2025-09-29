"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class MeasureBetween(AnyObject):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MeasureBetween
                | 
                | Represents the MeasureBetween.
                | The MeasureBetween is the measurement between two set of the selections of the
                | object.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def compute(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub Compute()
                |     To calculate the measure between.
                | 
                |     Example:
                | 
                |            This example Set the direction of MeasureBetween.
                |            
                | 
                |              Set theMeasureService = CATIA.ActiveEditor.GetService("MeasureService")
                |              Dim theMeasureBetween As MeasureBetween
                |              Set theMeasureBetween = theMeasureService.GetMeasureBetween(theSelection1, theSelection2)
                |              ...
                |              theMeasureBetween.Compute

        :return: None
        """
        return self.com_object.Compute()

    def get_angle(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetAngle() As double
                |     Get the angle result from the measure between.
                | 
                |     Returns:
                |         The angle. It should be get after the "Compute" 
                |     Example:
                | 
                |            This example Set the direction of MeasureBetween.
                |            
                | 
                |              Set theMeasureService = CATIA.ActiveEditor.GetService("MeasureService")
                |              Dim theMeasureBetween As MeasureBetween
                |              Set theMeasureBetween = theMeasureService.GetMeasureBetween(theSelection1, theSelection2)
                |              ...
                |              Dim result As Double
                |              result = theMeasureBetween.GetAngle

        :return: float
        """
        return self.com_object.GetAngle()

    def get_axis_system_from_measure(self, o_axis_positioning: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetAxisSystemFromMeasure(CATSafeArrayVariant
                | oAxisPositioning)
                |     Get the position of the axis system of the object with respect to the
                |     absolute axis system. This position corresponds to the product positioning
                |     matrix. All coordinates are internally computed using the axis system of the
                |     object. To provide these coordinates with respect to absolute axis system, it
                |     is required to know the position of the axis system of the
                |     object.
                | 
                |     Parameters:
                | 
                |         ioAxisPosition
                |             The information of the axis system with respect to the product
                |             coordinate system:
                | 
                |                 iAxisPositioning(0) is the X coordinate of the origin of the
                |                 axis system
                |                 iAxisPositioning(1) is the Y coordinate of the origin of the
                |                 axis system
                |                 iAxisPositioning(2) is the Z coordinate of the origin of the
                |                 axis system
                |                 iAxisPositioning(3) is the X coordinate of the first direction
                |                 of the axis system
                |                 iAxisPositioning(4) is the Y coordinate of the first direction
                |                 of the axis system
                |                 iAxisPositioning(5) is the Z coordinate of the first direction
                |                 of the axis system
                |                 iAxisPositioning(6) is the X coordinate of the second direction
                |                 of the axis system
                |                 iAxisPositioning(7) is the Y coordinate of the second direction
                |                 of the axis system
                |                 iAxisPositioning(8) is the Z coordinate of the second direction
                |                 of the axis system
                |                 iAxisPositioning(9) is the X coordinate of the third direction
                |                 of the axis system
                |                 iAxisPositioning(10) is the Y coordinate of the third direction
                |                 of the axis system
                |                 iAxisPositioning(11) is the Z coordinate of the third direction
                |                 of the axis system 
                | 
                |     Example:
                | 
                |            This example get the axis system of theMeasureBetween
                |            computation.
                |            
                | 
                |              Dim theAxisPositioning(11)
                |              theMeasureBetween.GetAxisSystemFromMeasure
                |              theAxisPositioning

        :param tuple o_axis_positioning:
        :return: None
        """
        return self.com_object.GetAxisSystemFromMeasure(o_axis_positioning)

    def get_band_analysis_parameters(self, o_min_distance: float, o_max_distance: float, o_accuracy: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetBandAnalysisParameters(double oMinDistance,double oMaxDistance,double
                | oAccuracy)
                |     Get the Band Analysis Parameters.
                | 
                |     Parameters:
                | 
                |         oMinDistance
                |             The minimum distance 
                |         oMaxDistance
                |             The maximum 
                |         oAccuracy
                |             The accuracy 
                | 
                |     Example:
                | 
                |            This example Get the Band Analysis Parameters of
                |            MeasureBetween.
                |            
                | 
                |              Set theMeasureService = CATIA.ActiveEditor.GetService("MeasureService")
                |              Dim theMeasureBetween As MeasureBetween
                |              Set theMeasureBetween = theMeasureService.GetMeasureBetween(theSelection1, theSelection2)
                |              Dim theMinDistance As Double
                |              Dim theMaxDistance As Double
                |              Dim theAccuracy As Double
                |              theMeasureBetween.GetBandAnalysisParameters theMinDistance
                |              theMaxDistance theAccuracy

        :param float o_min_distance:
        :param float o_max_distance:
        :param float o_accuracy:
        :return: None
        """
        return self.com_object.GetBandAnalysisParameters(o_min_distance, o_max_distance, o_accuracy)

    def get_components(self, o_components: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetComponents(CATSafeArrayVariant oComponents)
                |     Get the Components result from the measure between.
                | 
                |     Parameters:
                | 
                |         oComponents
                |             The components. The components should be get after the "Compute"
                |             
                | 
                |     Example:
                | 
                |            This example Set the direction of MeasureBetween.
                |            
                | 
                |              Set theMeasureService = CATIA.ActiveEditor.GetService("MeasureService")
                |              Dim theMeasureBetween As MeasureBetween
                |              Set theMeasureBetween = theMeasureService.GetMeasureBetween(theSelection1, theSelection2)
                |              ...
                |              Dim meausreComponents
                |              meausreComponents = theMeasureBetween.GetComponents

        :param tuple o_components:
        :return: None
        """
        return self.com_object.GetComponents(o_components)

    def get_computation_mode(self, o_computation_mode: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetComputationMode(CATMeasurableModeOfCalc
                | oComputationMode)
                |     Get the mode of computation of the object.
                | 
                |     Parameters:
                | 
                |         oComputationMode
                |             The mode of computation The computation mode of the object can be:
                |             Exact, Approximate or ExactElseApprox. 
                | 
                |     Example:
                | 
                |            This example get the computation mode of
                |            MeasureBetween.
                |            
                | 
                |              Set theMeasureService = CATIA.ActiveEditor.GetService("MeasureService")
                |              Dim theMeasureBetween As MeasureBetween
                |              Set theMeasureBetween = theMeasureService.GetMeasureBetween(theSelection1, theSelection2)
                |              Dim theComputationType As CATMeasurableModeOfCalc
                |              theComputationType = theMeasureBetween.GetComputationMode

        :param int o_computation_mode:
        :return: None
        """
        return self.com_object.GetComputationMode(o_computation_mode)

    def get_distance(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetDistance() As double
                |     Get the distance result from the measure.
                | 
                |     Returns:
                |         The distance. It should be get after the "Compute" 
                |     Example:
                | 
                |            This example Set the direction of MeasureBetween.
                |            
                | 
                |              Set theMeasureService = CATIA.ActiveEditor.GetService("MeasureService")
                |              Dim theMeasureBetween As MeasureBetween
                |              Set theMeasureBetween = theMeasureService.GetMeasureBetween(theSelection1, theSelection2)
                |              ...
                |              Dim result As Double
                |              result = theMeasureBetween.GetDistance

        :return: float
        """
        return self.com_object.GetDistance()

    def get_distance_measure_type(self, o_distance_measure_type: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetDistanceMeasureType(CATOpnsMeasureDistanceType
                | oDistanceMeasureType)
                |     Get the distance measure type on the measure between.
                | 
                |     Parameters:
                | 
                |         oDistanceMeasureType
                |             The distance measure type The distance measure type can be:
                |             catOpnsMinimumDistance, catOpnsMaximumDistance, catOpnsMaximumDistance12,
                |             catOpnsMinimumDistanceAlongDir, catOpnsBandAnalysis, catOpnsUnknownDistance
                |             @see CATOpnsMeasureDistanceType 
                | 
                |     Example:
                | 
                |            This example get the DistanceMeasureType from theMeasureBetween
                |            computation.
                |            
                | 
                |              Set theMeasureService = CATIA.ActiveEditor.GetService("MeasureService")
                |              Dim theMeasureBetween As MeasureBetween
                |              Set theMeasureBetween = theMeasureService.GetMeasureBetween(theSelection1, theSelection2)
                |              ...
                |              Dim theDistanceType
                |              theDistanceType = theMeasureBetween.GetDistanceMeasureType

        :param int o_distance_measure_type:
        :return: None
        """
        return self.com_object.GetDistanceMeasureType(o_distance_measure_type)

    def get_extension_mode(self, o_ref_extent_mode: int, o_target_extent_mode: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetExtensionMode(CATOpnsMeasureExtensionMode
                | oRefExtentMode,CATOpnsMeasureExtensionMode oTargetExtentMode)
                |     Get the mode of extension of the object.
                | 
                |     Parameters:
                | 
                |         oRefExtentMode
                |             The extension mode for reference 
                |         oTargetExtentMode
                |             The extension mode for target The extension mode of the object can
                |             be: catOpnsFiniteExtend, catOpnsInfiniteExtend 
                | 
                |     Example:
                | 
                |            This example get the extension mode of
                |            MeasureBetween.
                |            
                | 
                |              Set theMeasureService = CATIA.ActiveEditor.GetService("MeasureService")
                |              Dim theMeasureBetween As MeasureBetween
                |              Set theMeasureBetween = theMeasureService.GetMeasureBetween(theSelection1, theSelection2)
                |              Dim theExtensionMode1
                |              Dim theExtensionMode2
                |              theMeasureBetween.GetExtensionMode theExtensionMode1
                |              theExtensionMode2

        :param CATOpnsMeasureExtensionMode o_ref_extent_mode:
        :param CATOpnsMeasureExtensionMode o_target_extent_mode:
        :return: None
        """
        return self.com_object.GetExtensionMode(o_ref_extent_mode, o_target_extent_mode)

    def get_first_point_coordinates(self, o_coordinates: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetFirstPointCoordinates(CATSafeArrayVariant oCoordinates)
                |     Get the First Point Coordinates from the measure between.
                | 
                |     Parameters:
                | 
                |         oCoordinates
                |             The coordinates. The point coordinates should be get after the
                |             "Compute" 
                | 
                |     Example:
                | 
                |            This example Set the direction of MeasureBetween.
                |            
                | 
                |              Set theMeasureService = CATIA.ActiveEditor.GetService("MeasureService")
                |              Dim theMeasureBetween As MeasureBetween
                |              Set theMeasureBetween = theMeasureService.GetMeasureBetween(theSelection1, theSelection2)
                |              ...
                |              Dim result
                |              result = theMeasureBetween.GetFirstPointCoordinates

        :param tuple o_coordinates:
        :return: None
        """
        return self.com_object.GetFirstPointCoordinates(o_coordinates)

    def get_first_selection(self, o_first_selections: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetFirstSelection(CATSafeArrayVariant oFirstSelections)
                |     Get the first selected objects of the measure Between.
                | 
                |     Parameters:
                | 
                |         oFirstSelections
                |             The first set of the selected objects 
                | 
                |     Example:
                | 
                |            This example get the first selected objects of
                |            theMeasureBetween/tt>.
                |            
                | 
                |              Set theMeasureService = CATIA.ActiveEditor.GetService("MeasurableService")
                |              Dim theMeasureBetween As MeasureBetween
                |              Set theMeasureBetween = theMeasureService.GetMeasureBetween(theSelection1, theSelection2)
                |              Dim theSelection
                |              theSelection = theMeasureBetween.GetFirstSelection

        :param tuple o_first_selections:
        :return: None
        """
        return self.com_object.GetFirstSelection(o_first_selections)

    def get_result_computation_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetResultComputationType() As CATResultCalcType
                |     Get the resulting type of computation of the object. The resulting type of
                |     the object can be: Exact, Approximate or Mixed.
                | 
                |     Returns:
                |         The resulting type In case of measures between, this method must be
                |         called after distance or angle computation 
                |     Example:
                | 
                |            This example get the ResultComputationType for theMeasureBetween
                |            computation.
                |            
                | 
                |              Set theMeasureService = CATIA.ActiveEditor.GetService("MeasureService")
                |              Dim theMeasureBetween As MeasureBetween
                |              Set theMeasureBetween = theMeasureService.GetMeasureBetween(theSelection1, theSelection2)
                |              ...
                |              Dim theComputationType As CATResultCalcType
                |              theComputationType = theMeasureBetween.GetResultComputationType

        :return: int
        """
        return self.com_object.GetResultComputationType()

    def get_second_point_coordinates(self, o_coordinates: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetSecondPointCoordinates(CATSafeArrayVariant
                | oCoordinates)
                |     Get the Second Point Coordinates from the measure between.
                | 
                |     Parameters:
                | 
                |         oCoordinates
                |             The coordinates. The point coordinates should be get after the
                |             "Compute" 
                | 
                |     Example:
                | 
                |            This example Set the direction of MeasureBetween.
                |            
                | 
                |              Set theMeasureService = CATIA.ActiveEditor.GetService("MeasureService")
                |              Dim theMeasureBetween As MeasureBetween
                |              Set theMeasureBetween = theMeasureService.GetMeasureBetween(theSelection1, theSelection2)
                |              ...
                |              Dim result
                |              result = theMeasureBetween.GetSecondPointCoordinates

        :param tuple o_coordinates:
        :return: None
        """
        return self.com_object.GetSecondPointCoordinates(o_coordinates)

    def get_second_selection(self, o_second_selections: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetSecondSelection(CATSafeArrayVariant oSecondSelections)
                |     Get the second selected objects of the measure Between.
                | 
                |     Parameters:
                | 
                |         oSecondSelections
                |             The second set of the selected objects 
                | 
                |     Example:
                | 
                |            This example get the second selected objects of
                |            theMeasureBetween.
                |            
                | 
                |              Set theMeasureService = CATIA.ActiveEditor.GetService("MeasurableService")
                |              Dim theMeasureBetween As MeasureBetween
                |              Set theMeasureBetween = theMeasureService.GetMeasureBetween(theSelection1, theSelection2)
                |              Dim theSelection
                |              theSelection = theMeasureBetween.GetSecondSelection

        :param tuple o_second_selections:
        :return: None
        """
        return self.com_object.GetSecondSelection(o_second_selections)

    def get_selection_calculation_types(self, o_first_calculation_type: int, o_second_calculation_type: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetSelectionCalculationTypes(CATResultCalcType
                | oFirstCalculationType,CATResultCalcType
                | oSecondCalculationType)
                |     Get the Selection Calculation Types. The Selection Calculation Types the
                |     measure can be: Exact, Approximate or Mixed.
                | 
                |     Parameters:
                | 
                |         oFirstCalculationType
                |             The first Selection Calculation Type 
                |         oSecondCalculationType
                |             The second Selection Calculation Type 
                | 
                |     Example:
                | 
                |            This example Get the Selection Calculation Types for
                |            theMeasureBetween computation.
                |            
                | 
                |              Set theMeasureService = CATIA.ActiveEditor.GetService("MeasureService")
                |              Dim theMeasureBetween As MeasureBetween
                |              Set theMeasureBetween = theMeasureService.GetMeasureBetween(theSelection1, theSelection2)
                |              ...
                |              Dim firstSelectionCalculationType
                |              Dim secondSelectionCalculationType
                |              theMeasureBetween.GetSelectionCalculationTypes
                |              firstSelectionCalculationType,
                |              secondSelectionCalculationType

        :param int o_first_calculation_type:
        :param int o_second_calculation_type:
        :return: None
        """
        return self.com_object.GetSelectionCalculationTypes(o_first_calculation_type, o_second_calculation_type)

    def set_along_direction(self, i_x_vector: float, i_y_vector: float, i_z_vector: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetAlongDirection(double iXVector,double iYVector,double
                | iZVector)
                |     Set the direction of measure between along direction.
                | 
                |     Parameters:
                | 
                |         iXVector
                |             The X coordinate of the vector 
                |         iYVector
                |             The Y coordinate of the vector 
                |         iZVector
                |             The Z coordinate of the vector 
                | 
                |     Example:
                | 
                |            This example Set the direction of MeasureBetween.
                |            
                | 
                |              Set theMeasureService = CATIA.ActiveEditor.GetService("MeasureService")
                |              Dim theMeasureBetween As MeasureBetween
                |              Set theMeasureBetween = theMeasureService.GetMeasureBetween(theSelection1, theSelection2)
                |              theMeasureBetween.SetAlongDirection 0.0 0.0 1.0

        :param float i_x_vector:
        :param float i_y_vector:
        :param float i_z_vector:
        :return: None
        """
        return self.com_object.SetAlongDirection(i_x_vector, i_y_vector, i_z_vector)

    def set_axis_system_on_measure(self, i_axis_positioning: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetAxisSystemOnMeasure(CATSafeArrayVariant
                | iAxisPositioning)
                |     Set the position of the axis system of the object with respect to the
                |     absolute axis system. This position corresponds to the product positioning
                |     matrix. All coordinates are internally computed using the axis system of the
                |     object. To provide these coordinates with respect to absolute axis system, it
                |     is required to know the position of the axis system of the
                |     object.
                | 
                |     Parameters:
                | 
                |         ioAxisPosition
                |             The information of the axis system with respect to the product
                |             coordinate system:
                | 
                |                 iAxisPositioning(0) is the X coordinate of the origin of the
                |                 axis system
                |                 iAxisPositioning(1) is the Y coordinate of the origin of the
                |                 axis system
                |                 iAxisPositioning(2) is the Z coordinate of the origin of the
                |                 axis system
                |                 iAxisPositioning(3) is the X coordinate of the first direction
                |                 of the axis system
                |                 iAxisPositioning(4) is the Y coordinate of the first direction
                |                 of the axis system
                |                 iAxisPositioning(5) is the Z coordinate of the first direction
                |                 of the axis system
                |                 iAxisPositioning(6) is the X coordinate of the second direction
                |                 of the axis system
                |                 iAxisPositioning(7) is the Y coordinate of the second direction
                |                 of the axis system
                |                 iAxisPositioning(8) is the Z coordinate of the second direction
                |                 of the axis system
                |                 iAxisPositioning(9) is the X coordinate of the third direction
                |                 of the axis system
                |                 iAxisPositioning(10) is the Y coordinate of the third direction
                |                 of the axis system
                |                 iAxisPositioning(11) is the Z coordinate of the third direction
                |                 of the axis system 
                | 
                |     Example:
                | 
                |            This example set the axis system for theMeasureBetween
                |            computation.
                |            
                | 
                |              Dim theAxisPositioning(11)
                |              theAxisPositioning(0) = 0
                |              theAxisPositioning(1) = 0
                |              theAxisPositioning(2) = 0
                |              theAxisPositioning(3) = 1
                |              theAxisPositioning(4) = 0
                |              theAxisPositioning(5) = 0
                |              theAxisPositioning(6) = 0
                |              theAxisPositioning(7) = 1
                |              theAxisPositioning(8) = 0
                |              theAxisPositioning(9) = 0
                |              theAxisPositioning(10) = 0
                |              theAxisPositioning(11) = 1
                |              theMeasureBetween.SetAxisSystemOnMeasure
                |              theAxisPositioning

        :param tuple i_axis_positioning:
        :return: None
        """
        return self.com_object.SetAxisSystemOnMeasure(i_axis_positioning)

    def set_band_analysis_parameters(self, i_min_distance: float, i_max_distance: float, i_accuracy: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetBandAnalysisParameters(double iMinDistance,double iMaxDistance,double
                | iAccuracy)
                |     Set the Band Analysis Parameters.
                | 
                |     Parameters:
                | 
                |         iMinDistance
                |             The minimum distance 
                |         iMaxDistance
                |             The maximum 
                |         iAccuracy
                |             The accuracy 
                | 
                |     Example:
                | 
                |            This example Set the Band Analysis Parameters of
                |            MeasureBetween.
                |            
                | 
                |              Set theMeasureService = CATIA.ActiveEditor.GetService("MeasureService")
                |              Dim theMeasureBetween As MeasureBetween
                |              Set theMeasureBetween = theMeasureService.GetMeasureBetween(theSelection1, theSelection2)
                |              theMeasureBetween.SetBandAnalysisParameters 1.0 2.0
                |              1.0

        :param float i_min_distance:
        :param float i_max_distance:
        :param float i_accuracy:
        :return: None
        """
        return self.com_object.SetBandAnalysisParameters(i_min_distance, i_max_distance, i_accuracy)

    def set_computation_mode(self, i_computation_mode: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetComputationMode(CATMeasurableModeOfCalc
                | iComputationMode)
                |     Set the mode of computation of the object.
                | 
                |     Parameters:
                | 
                |         iComputationMode
                |             The mode of computation The computation mode of the object can be:
                |             Exact, Approximate or ExactElseApprox. 
                | 
                |     Example:
                | 
                |            This example get the computation mode of
                |            theMeasureBetween.
                |            
                | 
                |              Set theMeasureService = CATIA.ActiveEditor.GetService("MeasureService")
                |              Dim theMeasureBetween As MeasureBetween
                |              Set theMeasureBetween = theMeasureService.GetMeasureBetween(theSelection1, theSelection2)
                |              theMeasureBetween.SetComputationMode
                |              MeasExactElseApproxCalculation

        :param int i_computation_mode:
        :return: None
        """
        return self.com_object.SetComputationMode(i_computation_mode)

    def set_distance_measure_type(self, i_distance_measure_type: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetDistanceMeasureType(CATOpnsMeasureDistanceType
                | iDistanceMeasureType)
                |     Set the distance measure type on the measure between.
                | 
                |     Parameters:
                | 
                |         iDistanceMeasureType
                |             The distance measure type The distance measure type can be:
                |             catOpnsMinimumDistance, catOpnsMaximumDistance, catOpnsMaximumDistance12,
                |             catOpnsMinimumDistanceAlongDir, catOpnsBandAnalysis, catOpnsUnknownDistance
                |             @see CATOpnsMeasureDistanceType 
                | 
                |     Example:
                | 
                |            This example Set the DistanceMeasureType for theMeasureBetween
                |            computation.
                |            
                | 
                |              Set theMeasureService = CATIA.ActiveEditor.GetService("MeasureService")
                |              Dim theMeasureBetween As MeasureBetween
                |              Set theMeasureBetween = theMeasureService.GetMeasureBetween(theSelection1, theSelection2)
                |              ...
                |              theMeasureBetween.SetDistanceMeasureType
                |              catOpnsMinimumDistanceAlongDir

        :param int i_distance_measure_type:
        :return: None
        """
        return self.com_object.SetDistanceMeasureType(i_distance_measure_type)

    def set_extension_mode(self, i_ref_extent_mode: int, i_target_extent_mode: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetExtensionMode(CATOpnsMeasureExtensionMode
                | iRefExtentMode,CATOpnsMeasureExtensionMode iTargetExtentMode)
                |     Set the mode of extension of the object.
                | 
                |     Parameters:
                | 
                |         iRefExtentMode
                |             The extension mode for reference 
                |         iTargetExtentMode
                |             The extension mode for target The extension mode of the object can
                |             be: catOpnsFiniteExtend, catOpnsInfiniteExtend 
                | 
                |     Example:
                | 
                |            This example set the extension mode of
                |            theMeasureBetween.
                |            
                | 
                |              Set theMeasureService = CATIA.ActiveEditor.GetService("MeasureService")
                |              Dim theMeasureBetween As MeasureBetween
                |              Set theMeasureBetween = theMeasureService.GetMeasureBetween(theSelection1, theSelection2)
                |              theMeasureBetween.SetExtensionMode catOpnsFiniteExtend
                |              catOpnsFiniteExtend

        :param CATOpnsMeasureExtensionMode i_ref_extent_mode:
        :param CATOpnsMeasureExtensionMode i_target_extent_mode:
        :return: None
        """
        return self.com_object.SetExtensionMode(i_ref_extent_mode, i_target_extent_mode)

    def set_first_selection(self, i_first_selections: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetFirstSelection(CATSafeArrayVariant iFirstSelections)
                |     Set the selected objects of the measure Between.
                | 
                |     Parameters:
                | 
                |         iFirstSelections
                |             The first set of the selected objects 
                | 
                |     Example:
                | 
                |            This example set the first selected objects of
                |            theMeasureBetween.
                |            
                | 
                |              Set theMeasureService = CATIA.ActiveEditor.GetService("MeasurableService")
                |              Dim theMeasureBetween As MeasureBetween
                |              Set theMeasureBetween = theMeasureService.GetMeasureBetween()
                |              theMeasureBetween.SetFirstSelection theSelections

        :param tuple i_first_selections:
        :return: None
        """
        return self.com_object.SetFirstSelection(i_first_selections)

    def set_result_computation_type(self, i_computation_type: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetResultComputationType(CATResultCalcType
                | iComputationType)
                |     Set the resulting type of computation of the object. The computation mode
                |     of the object can be: Exact, Approximate or Mixed.
                | 
                |     Parameters:
                | 
                |         iComputationType
                |             The type of computation In case of measures between, this method
                |             must be called after distance or angle computation
                |             
                | 
                |     Example:
                | 
                |            This example get the ResultComputationType for theMeasureBetween
                |            computation.
                |            
                | 
                |              Set theMeasureService = CATIA.ActiveEditor.GetService("MeasureService")
                |              Dim theMeasureBetween As MeasureBetween
                |              Set theMeasureBetween = theMeasureService.GetMeasureBetween(theSelection1, theSelection2)
                |              ...
                |              theMeasureBetween.SetResultComputationType
                |              ResMixedCalculation

        :param int i_computation_type:
        :return: None
        """
        return self.com_object.SetResultComputationType(i_computation_type)

    def set_second_selection(self, i_second_selections: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetSecondSelection(CATSafeArrayVariant iSecondSelections)
                |     Set the second selected objects of the measure Between.
                | 
                |     Parameters:
                | 
                |         iSecondSelections
                |             The second set of the selected objects 
                | 
                |     Example:
                | 
                |            This example set the second selected objects of
                |            theMeasureBetween.
                |            
                | 
                |              Set theMeasureService = CATIA.ActiveEditor.GetService("MeasurableService")
                |              Dim theMeasureBetween As MeasureBetween
                |              Set theMeasureBetween = theMeasureService.GetMeasureBetween()
                |              theMeasureBetween.SetSecondSelection
                |              theSelections

        :param tuple i_second_selections:
        :return: None
        """
        return self.com_object.SetSecondSelection(i_second_selections)

    def set_selection_calculation_types(self, i_first_calculation_type: int, i_second_calculation_type: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetSelectionCalculationTypes(CATResultCalcType
                | iFirstCalculationType,CATResultCalcType
                | iSecondCalculationType)
                |     Set the Selection Calculation Types. The Selection Calculation Types the
                |     measure can be: Exact, Approximate or Mixed.
                | 
                |     Parameters:
                | 
                |         iFirstCalculationType
                |             The first Selection Calculation Type 
                |         iSecondCalculationType
                |             The second Selection Calculation Type 
                | 
                |     Example:
                | 
                |            This example Set the Selection Calculation Types for
                |            theMeasureBetween computation.
                |            
                | 
                |              Set theMeasureService = CATIA.ActiveEditor.GetService("MeasureService")
                |              Dim theMeasureBetween As MeasureBetween
                |              Set theMeasureBetween = theMeasureService.GetMeasureBetween(theSelection1, theSelection2)
                |              ...
                |              theMeasureBetween.SetSelectionCalculationTypes
                |              ResMixedCalculation, ResMixedCalculation

        :param int i_first_calculation_type:
        :param int i_second_calculation_type:
        :return: None
        """
        return self.com_object.SetSelectionCalculationTypes(i_first_calculation_type, i_second_calculation_type)

    def __repr__(self):
        return f'MeasureBetween(name="{self.name}")'
