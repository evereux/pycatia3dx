"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.annotation.drawing_dimension import DrawingDimension
from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.tps.controlled_radius import ControlledRadius
from pycatia3dx.tps.dimension_limit import DimensionLimit
from pycatia3dx.tps.dimension_pattern import DimensionPattern
from pycatia3dx.tps.envelop_condition import EnvelopCondition


class Dimension3D(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     Dimension3D
                | 
                | Interface Managing Semantic Dimension.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def controled_radius(self) -> ControlledRadius:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func ControledRadius() As ControledRadius
                |     Gets the Dimension on the Controled Radius interface.
                | 
                |     Parameters:
                | 
                |         oContRadius
                |             The Controled Radius.

        :return: ControlledRadius
        """
        return ControlledRadius(self.com_object.ControledRadius())

    def dimension_limit(self) -> DimensionLimit:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func DimensionLimit() As DimensionLimit
                |     Gets the Dimension on the DimensionLimit interface.
                | 
                |     Parameters:
                | 
                |         oDimLim
                |             The Dimension Limits.

        :return: DimensionLimit
        """
        return DimensionLimit(self.com_object.DimensionLimit())

    def dimension_pattern(self) -> DimensionPattern:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func DimensionPattern() As DimensionPattern
                |     Gets the Dimension on the DimensionPattern interface.
                | 
                |     Parameters:
                | 
                |         oDimPatt
                |             The Dimension Pattern.

        :return: DimensionPattern
        """
        return DimensionPattern(self.com_object.DimensionPattern())

    def envelop_condition(self) -> EnvelopCondition:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func EnvelopCondition() As EnvelopCondition
                |     Gets the Dimension on the EnvelopCondition interface.
                | 
                |     Parameters:
                | 
                |         oEnvCond
                |             The Envelop Condition.

        :return: EnvelopCondition
        """
        return EnvelopCondition(self.com_object.EnvelopCondition())

    def get2d_annot(self) -> DrawingDimension:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Get2dAnnot() As DrawingDimension
                |     Retrieves Drafting Dimension.
                | 
                |     Parameters:
                | 
                |         oDim
                |             The Drafting Dimension.

        :return: DrawingDimension
        """
        return DrawingDimension(self.com_object.Get2dAnnot())

    def has_a_controlled_radius(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func HasAControledRadius() As boolean
                |     Checks if the Dimension has a Controled Radius.
                | 
                |     Parameters:
                | 
                |         oHasConRad
                | 
                |                 TRUE: The dimension has a Controled Radius
                |                 FALSE: The dimension has not a Controled
                |                 Radius

        :return: bool
        """
        return self.com_object.HasAControledRadius()

    def has_an_envelop_condition(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func HasAnEnvelopCondition() As boolean
                |     Checks if the Annotation has an Envelop Condition.
                | 
                |     Parameters:
                | 
                |         oHasEnvCond
                | 
                |                 TRUE: The dimension has an Envelop Condition
                |                 FALSE: The dimension has not an Envelop
                |                 Condition

        :return: bool
        """
        return self.com_object.HasAnEnvelopCondition()

    def has_dimension_limit(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func HasDimensionLimit() As boolean
                |     Checks if the Dimension has a Dimension Limit.
                | 
                |     Parameters:
                | 
                |         oHasDimLim
                | 
                |                 TRUE: Dimension Limit exists
                |                 FALSE: Dimension Limit does not exist

        :return: bool
        """
        return self.com_object.HasDimensionLimit()

    def is_a_continuous_feature_applied(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func IsAContinuousFeatureApplied() As boolean
                |     Checks if the Semantic Dimension is a applied on a Continuous Feature. CF
                |     suffix size modifier is only valid for ASME Standard.
                | 
                |     Parameters:
                | 
                |         oIsACFDim
                | 
                |                 TRUE: The dimension is a applied onto a Continuous
                |                 Feature
                |                 FALSE: The dimension is not applied onto a Continuous
                |                 Feature

        :return: bool
        """
        return self.com_object.IsAContinuousFeatureApplied()

    def is_a_dimension_pattern(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func IsADimensionPattern() As boolean
                |     Checks if the Semantic Dimension is a Dimension Pattern.
                | 
                |     Parameters:
                | 
                |         oIsADimPatt
                | 
                |                 TRUE: The dimension is a Dimension Pattern
                |                 FALSE: The dimension is not a Dimension
                |                 Pattern

        :return: bool
        """
        return self.com_object.IsADimensionPattern()

    def move_value(self, x: float, y: float, sub_part: int, dim_angle_behavior: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub MoveValue(double X,double Y,long SubPart,long
                | DimAngleBehavior)
                |     Moves the dimension value at a given point.
                | 
                |     Returns:
                |         HRESULT error returned code If the modification of the vertical offset value can not be performed because the parameter is locked in the current standard, the method return HRESULT = S_READ_ONLY. 
                |     Parameters:
                | 
                |         X
                |             Point abscissa on which the dimension value will be positionned.
                |             
                |         Y
                |             Point ordinate on which the dimension value will be positionned.
                |             
                |         SubPart
                |             Defines which part of the dimension should be
                |             moved
                |             -1 = Value (vertical move is take account according ptPos coordinates)
                |             0 = Both dimension line and value
                |             1 = Value
                |             2 = Dimension line
                |             3 = Secondary part
                |             4 = Secondary part and value
                |             5 = Secondary part and dimension line
                |             6 = Secondary part, dimension line and value
                |             7 = Value leader (for dimension line with leader one part or two parts) 
                |         DimAngleBehavior
                |             Defines angle dimension line behavior.
                |             0 = Sector angle is switched when ptPos is in opposite sector (Default)
                |             1 = Sector angle is kept what ever ptPos placement 
                |         Example:
                |             This example move dimension value MyDimension
                |             path.
                | 
                |              MyDimension.MoveValue(X, Y, SubPart,
                |              DimAngleBehavior)

        :param float x:
        :param float y:
        :param int sub_part:
        :param int dim_angle_behavior:
        :return: None
        """
        return self.com_object.MoveValue(x, y, sub_part, dim_angle_behavior)

    def __repr__(self):
        return f'Dimension3D(name="{ self.name }")'
