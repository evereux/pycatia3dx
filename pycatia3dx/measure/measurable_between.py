"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.measure.measurable_in_context import MeasurableInContext
from pycatia3dx.mmr_automation_interfaces.axis_system import AxisSystem
from pycatia3dx.system.any_object import AnyObject


class MeasurableBetween(MeasurableInContext):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     CATOpnsMeasureIDLItf.MeasurableInContext
                |                         MeasurableBetween
                | 
                | Interface representing the measurement between two elements.
                | Get the minimun distance between the two elements and the points of each
                | element which realised this distance.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def angle_to(self, i_other_object: AnyObject, i_other_math_axis: tuple, o_angle: float, o_x_first_point: float, o_y_first_point: float, o_z_first_point: float, o_x_other_point: float, o_y_other_point: float, o_z_other_point: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Sub AngleTo(AnyObject iOtherObject,CATSafeArrayVariant iOtherMathAxis,double
                | oAngle,double oXFirstPoint,double oYFirstPoint,double oZFirstPoint,double
                | oXOtherPoint,double oYOtherPoint,double oZOtherPoint)
                |     Retrieves the angle between the theMeasurableBetween and a
                |     CATIABase.
                | 
                |     Parameters:
                | 
                |         iOtherObject
                | 
                |                 iOtherObject is the second element of the measure.
                |                 
                | 
                |         iOtherMathAxis
                | 
                |                 iOtherMathAxis is the axis system of the second
                |                 element.
                |                 If the dimension of the CATSafeArrayVariant is different of 12,
                |                 a default axis (1,0,0, 0,1,0, 0,0,1, 0,0,0) is taking account.
                |                 
                | 
                |     Example:
                | 
                |            This example retrieves the angle between two
                |            selections.
                |            
                | 
                |              Set theMeasureService = CATIA.ActiveEditor.GetService("MeasurableService")
                |              Dim theMeasurableBetween As MeasurableBetween
                |              Set theMeasurableBetween = theMeasureService.GetMeasurable(theFirstSelection, CAAMeasurableBetween)
                |              Dim theOtherMathAxis(0)
                |              Dim theAngle As Double
                |              Dim theXFirstPoint As Double
                |              Dim theYFirstPoint As Double
                |              Dim theZFirstPoint As Double
                |              Dim theXOtherPoint As Double
                |              Dim theYOtherPoint As Double
                |              Dim theZOtherPoint As Double
                |              theMeasurableBetween.AngleTo theSecondSelection, theOtherMathAxis,
                |              theAngle, theXFirstPoint, theYFirstPoint, theZFirstPoint, theXOtherPoint,
                |              theYOtherPoint, theZOtherPoint

        :param AnyObject i_other_object:
        :param tuple i_other_math_axis:
        :param float o_angle:
        :param float o_x_first_point:
        :param float o_y_first_point:
        :param float o_z_first_point:
        :param float o_x_other_point:
        :param float o_y_other_point:
        :param float o_z_other_point:
        :return: None
        """
        return self.com_object.AngleTo(i_other_object.com_object, i_other_math_axis, o_angle, o_x_first_point, o_y_first_point, o_z_first_point, o_x_other_point, o_y_other_point, o_z_other_point)

    def distance_min_to(self, i_other_object: AnyObject, i_other_math_axis: tuple, o_distance: float, o_x_first_point: float, o_y_first_point: float, o_z_first_point: float, o_x_other_point: float, o_y_other_point: float, o_z_other_point: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Sub DistanceMinTo(AnyObject iOtherObject,CATSafeArrayVariant
                | iOtherMathAxis,double oDistance,double oXFirstPoint,double oYFirstPoint,double
                | oZFirstPoint,double oXOtherPoint,double oYOtherPoint,double
                | oZOtherPoint)
                |     Retrieves the minimum distance between the theMeasurableBetween and a
                |     CATIABase. Bodies (openbody, hybridbody..) cannot be measured
                |     between.
                | 
                |     Parameters:
                | 
                |         iOtherObject
                | 
                |                 iOtherObject is the second element of the measure.
                |                 
                | 
                |         iOtherMathAxis
                | 
                |                 iOtherMathAxis is the axis system of the second
                |                 element.
                |                 If the dimension of the CATSafeArrayVariant is different of 12,
                |                 a default axis (1,0,0, 0,1,0, 0,0,1, 0,0,0) is taking account.
                |                 
                | 
                |     Example:
                | 
                |            This example retrieves the distance between two
                |            selections.
                |            
                | 
                |              Set theMeasureService = CATIA.ActiveEditor.GetService("MeasurableService")
                |              Dim theMeasurableBetween As MeasurableBetween
                |              Set theMeasurableBetween = theMeasureService.GetMeasurable(theFirstSelection, CAAMeasurableBetween)
                |              Dim theOtherMathAxis(0)
                |              Dim theDistance As Double
                |              Dim theXFirstPoint As Double
                |              Dim theYFirstPoint As Double
                |              Dim theZFirstPoint As Double
                |              Dim theXOtherPoint As Double
                |              Dim theYOtherPoint As Double
                |              Dim theZOtherPoint As Double
                |              theMeasurableBetween.DistanceMinTo theSecondSelection,
                |              theOtherMathAxis, theDistance, theXFirstPoint, theYFirstPoint, theZFirstPoint,
                |              theXOtherPoint, theYOtherPoint, theZOtherPoint

        :param AnyObject i_other_object:
        :param tuple i_other_math_axis:
        :param float o_distance:
        :param float o_x_first_point:
        :param float o_y_first_point:
        :param float o_z_first_point:
        :param float o_x_other_point:
        :param float o_y_other_point:
        :param float o_z_other_point:
        :return: None
        """
        return self.com_object.DistanceMinTo(i_other_object.com_object, i_other_math_axis, o_distance, o_x_first_point, o_y_first_point, o_z_first_point, o_x_other_point, o_y_other_point, o_z_other_point)

    def distance_min_to_as(self, i_other_object: AnyObject, i_other_math_axis: AxisSystem, o_distance: float, o_x_first_point: float, o_y_first_point: float, o_z_first_point: float, o_x_other_point: float, o_y_other_point: float, o_z_other_point: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Sub DistanceMinToAS(AnyObject iOtherObject,AxisSystem iOtherMathAxis,double
                | oDistance,double oXFirstPoint,double oYFirstPoint,double oZFirstPoint,double
                | oXOtherPoint,double oYOtherPoint,double oZOtherPoint)
                |     Retrieves the minimum distance between the theMeasurableBetween and a
                |     CATIABase. Bodies (openbody, hybridbody..) cannot be measured
                |     between.
                | 
                |     Parameters:
                | 
                |         iOtherObject
                | 
                |                 iOtherObject is the second element of the measure.
                |                 
                | 
                |         iOtherMathAxis
                | 
                |                 iOtherMathAxis is the axis system of the second element.
                |                 
                | 
                |     Example:
                | 
                |            This example retrieves the distance between two
                |            selections.
                |            
                | 
                |              Set theMeasureService = CATIA.ActiveEditor.GetService("MeasurableService")
                |              Dim theMeasurableBetween As MeasurableBetween
                |              Set theMeasurableBetween = theMeasureService.GetMeasurable(theFirstSelection, CAAMeasurableBetween)
                |              Dim AxisSystem As AxisSystem
                |              Dim theDistance As Double
                |              Dim theXFirstPoint As Double
                |              Dim theYFirstPoint As Double
                |              Dim theZFirstPoint As Double
                |              Dim theXOtherPoint As Double
                |              Dim theYOtherPoint As Double
                |              Dim theZOtherPoint As Double
                |              theMeasurableBetween.DistanceMinToAS theSecondSelection,
                |              theOtherMathAxis, theDistance, theXFirstPoint, theYFirstPoint, theZFirstPoint,
                |              theXOtherPoint, theYOtherPoint, theZOtherPoint

        :param AnyObject i_other_object:
        :param AxisSystem i_other_math_axis:
        :param float o_distance:
        :param float o_x_first_point:
        :param float o_y_first_point:
        :param float o_z_first_point:
        :param float o_x_other_point:
        :param float o_y_other_point:
        :param float o_z_other_point:
        :return: None
        """
        return self.com_object.DistanceMinToAS(i_other_object.com_object, i_other_math_axis.com_object, o_distance, o_x_first_point, o_y_first_point, o_z_first_point, o_x_other_point, o_y_other_point, o_z_other_point)

    def distance_min_to_point(self, i_x_point: float, i_y_point: float, i_z_point: float, o_distance: float, o_x_other_point: float, o_y_other_point: float, o_z_other_point: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Sub DistanceMinToPoint(double iXPoint,double iYPoint,double iZPoint,double
                | oDistance,double oXOtherPoint,double oYOtherPoint,double
                | oZOtherPoint)
                |     Retrieves the minimum distance between the theMeasurableBetween and a
                |     point.
                | 
                |     Example:
                | 
                |            
                | 
                |              Set theMeasureService = CATIA.ActiveEditor.GetService("MeasurableService")
                |              Dim theMeasurableBetween As MeasurableBetween
                |              Set theMeasurableBetween = theMeasureService.GetMeasurable(theFirstSelection, CAAMeasurableBetween)
                |              Dim theXPoint As Double
                |              theXPoint = 10
                |              Dim theYPoint As Double
                |              theYPoint = 50
                |              Dim theZPoint As Double
                |              theZPoint = 20
                |              Dim theDistance As Double
                |              Dim theXOtherPoint As Double
                |              Dim theYOtherPoint As Double
                |              Dim theZOtherPoint As Double
                |              theMeasurableBetween.DistanceMinToPoint theXPoint, theYPoint,
                |              theZPoint, theDistance, theXOtherPoint,
                |              theYOtherPoint,theZOtherPoint

        :param float i_x_point:
        :param float i_y_point:
        :param float i_z_point:
        :param float o_distance:
        :param float o_x_other_point:
        :param float o_y_other_point:
        :param float o_z_other_point:
        :return: None
        """
        return self.com_object.DistanceMinToPoint(i_x_point, i_y_point, i_z_point, o_distance, o_x_other_point, o_y_other_point, o_z_other_point)

    def set_computation_mode(self, i_computation_mode: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Sub SetComputationMode(CATMeasurableModeOfCalc
                | iComputationMode)
                |     Set the mode of computation of the object. The computation mode of the
                |     object can be: Exact else Approximate, Exact only or Approximate only.

        :param int i_computation_mode:
        :return: None
        """
        return self.com_object.SetComputationMode(i_computation_mode)

    def __repr__(self):
        return f'MeasurableBetween(name="{ self.name }")'
