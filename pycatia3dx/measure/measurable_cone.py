"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.measure.measurable_surface import MeasurableSurface


class MeasurableCone(MeasurableSurface):

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
                |                         CATOpnsMeasureIDLItf.MeasurableSurface
                |                             MeasurableCone
                | 
                | Interface representing the measurement on a cone.
                | Get the area, the center of gravity and the perimeter by inheritance. Get the
                | angle, the axis vector of the cone and three points on this axis (the two limit
                | ones more an other).
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def get_angle(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Func GetAngle() As double
                |     Retrieves the angle of the cone.
                | 
                |     Example:
                | 
                |            This example retrieves the Angle of theMeasurableCone
                |            measure.
                |            
                | 
                |              Set theMeasureService = CATIA.ActiveEditor.GetService("MeasurableService")
                |              Dim theMeasurableCone As MeasurableCone
                |              Set theMeasurableCone = theMeasureService.GetMeasurable(theSelection, CAAMeasurableCone)
                |              Dim theAngle As Double
                |              theAngle = theMeasurableCone.GetAngle

        :return: float
        """
        return self.com_object.GetAngle()

    def get_axis(self, o_x_vector: float, o_y_vector: float, o_z_vector: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Sub GetAxis(double oXVector,double oYVector,double oZVector)
                |     Retrieves the axis vector of the cone.
                | 
                |     Example:
                | 
                |            This example retrieves the axis vector of theMeasurableCone
                |            measure.
                |            
                | 
                |              Set theMeasureService = CATIA.ActiveEditor.GetService("MeasurableService")
                |              Dim theMeasurableCone As MeasurableCone
                |              Set theMeasurableCone = theMeasureService.GetMeasurable(theSelection, CAAMeasurableCone)
                |              Dim theXVector As Double
                |              Dim theYVector As Double
                |              Dim theZVector As Double
                |              theMeasurableCone.GetAxis theXVector, theYVector,
                |              theZVector

        :param float o_x_vector:
        :param float o_y_vector:
        :param float o_z_vector:
        :return: None
        """
        return self.com_object.GetAxis(o_x_vector, o_y_vector, o_z_vector)

    def get_point(self, o_x_point: float, o_y_point: float, o_z_point: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Sub GetPoint(double oXPoint,double oYPoint,double oZPoint)
                |     Retrieves the position of a point on the axis of the cone.
                | 
                |     Example:
                | 
                |            This example retrieves the position of a point on the axis of
                |            theMeasurableCone measure.
                |            
                | 
                |              Set theMeasureService = CATIA.ActiveEditor.GetService("MeasurableService")
                |              Dim theMeasurableCone As MeasurableCone
                |              Set theMeasurableCone = theMeasureService.GetMeasurable(theSelection, CAAMeasurableCone)
                |              Dim theXPoint As Double
                |              Dim theYPoint As Double
                |              Dim theZPoint As Double
                |              theMeasurableCone.GetPoint theXPoint, theYPoint,
                |              theZPoint

        :param float o_x_point:
        :param float o_y_point:
        :param float o_z_point:
        :return: None
        """
        return self.com_object.GetPoint(o_x_point, o_y_point, o_z_point)

    def get_points(self, o_x_start_point: float, o_y_start_point: float, o_z_start_point: float, o_x_end_point: float, o_y_end_point: float, o_z_end_point: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Sub GetPoints(double oXStartPoint,double oYStartPoint,double
                | oZStartPoint,double oXEndPoint,double oYEndPoint,double
                | oZEndPoint)
                |     Retrieves the position of the two limit points on the axis of the cone. The
                |     distance between these points fit with the height of the
                |     cone.
                | 
                |     Example:
                | 
                |            This example retrieves the position the two limit points on the axis
                |            of theMeasurableCone measure.
                |            
                | 
                |              Set theMeasureService = CATIA.ActiveEditor.GetService("MeasurableService")
                |              Dim theMeasurableCone As MeasurableCone
                |              Set theMeasurableCone = theMeasureService.GetMeasurable(theSelection, CAAMeasurableCone)
                |              Dim theXStartPoint As Double
                |              Dim theYStartPoint As Double
                |              Dim theZStartPoint As Double
                |              Dim theXEndPoint As Double
                |              Dim theYEndPoint As Double
                |              Dim theZEndPoint As Double
                |              theMeasurableCone.GetPoints theXStartPoint, theYStartPoint,
                |              theZStartPoint, theXEndPoint, theYEndPoint,
                |              theZEndPoint

        :param float o_x_start_point:
        :param float o_y_start_point:
        :param float o_z_start_point:
        :param float o_x_end_point:
        :param float o_y_end_point:
        :param float o_z_end_point:
        :return: None
        """
        return self.com_object.GetPoints(o_x_start_point, o_y_start_point, o_z_start_point, o_x_end_point, o_y_end_point, o_z_end_point)

    def __repr__(self):
        return f'MeasurableCone(name="{ self.name }")'
