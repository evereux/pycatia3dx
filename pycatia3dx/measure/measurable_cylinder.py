"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.measure.measurable_surface import MeasurableSurface


class MeasurableCylinder(MeasurableSurface):
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
                |                             MeasurableCylinder
                | 
                | Interface representing the measurement on a cylinder.
                | Get the area, the center of gravity and the perimeter by inheritance. Get the
                | radius, a point and the two limit points on the axis of the
                | cylinder.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def get_axis(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetAxis(double oXVector,double oYVector,double oZVector)
                |     Retrieves the axis vector of the cylinder.
                | 
                |     Example:
                | 
                |            This example retrieves the axis vector of theMeasurableCylinder
                |            measure.
                |            
                | 
                |              Set theMeasureService = CATIA.ActiveEditor.GetService("MeasurableService")
                |              Dim theMeasurableCylinder As MeasurableCylinder
                |              Set theMeasurableCylinder = theMeasureService.GetMeasurable(theSelection, CAAMeasurableCylinder)
                |              Dim theXVector As Double
                |              Dim theYVector As Double
                |              Dim theZVector As Double
                |              theMeasurableCylinder.GetAxis theXVector, theYVector,
                |              theZVector

        :return: tuple
        """
        return self.com_object.GetAxis()

    def get_point(self, o_x_point: float, o_y_point: float, o_z_point: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetPoint(double oXPoint,double oYPoint,double oZPoint)
                |     Retrieves the position of a point on the axis of the
                |     cylinder.
                | 
                |     Example:
                | 
                |            This example retrieves the position of a point on the axis of
                |            theMeasurableCylinder measure.
                |            
                | 
                |              Set theMeasureService = CATIA.ActiveEditor.GetService("MeasurableService")
                |              Dim theMeasurableCylinder As MeasurableCylinder
                |              Set theMeasurableCylinder = theMeasureService.GetMeasurable(theSelection, CAAMeasurableCylinder)
                |              Dim theXPoint As Double
                |              Dim theYPoint As Double
                |              Dim theZPoint As Double
                |              theMeasurableCylinder.GetPoint theXPoint, theYPoint,
                |              theZPoint

        :param float o_x_point:
        :param float o_y_point:
        :param float o_z_point:
        :return: None
        """
        return self.com_object.GetPoint(o_x_point, o_y_point, o_z_point)

    def get_points(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetPoints(double oXStartPoint,double oYStartPoint,double
                | oZStartPoint,double oXEndPoint,double oYEndPoint,double
                | oZEndPoint)
                |     Retrieves the position of the two limit points on the axis of the cylinder.
                |     The distance between these points fit with the height of the
                |     cylinder.
                | 
                |     Example:
                | 
                |            This example retrieves the position the two limit points on the axis
                |            of theMeasurableCylinder measure.
                |            
                | 
                |              Set theMeasureService = CATIA.ActiveEditor.GetService("MeasurableService")
                |              Dim theMeasurableCylinder As MeasurableCylinder
                |              Set theMeasurableCylinder = theMeasureService.GetMeasurable(theSelection, CAAMeasurableCylinder)
                |              Dim theXStartPoint As Double
                |              Dim theYStartPoint As Double
                |              Dim theZStartPoint As Double
                |              Dim theXEndPoint As Double
                |              Dim theYEndPoint As Double
                |              Dim theZEndPoint As Double
                |              theMeasurableCylinder.GetPoints theXStartPoint, theYStartPoint,
                |              theZStartPoint, theXEndPoint, theYEndPoint,
                |              theZEndPoint

        :return: tuple
        """
        # todo: check this method, does it require system service?
        return self.com_object.GetPoints()

    def get_radius(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetRadius() As double
                |     Retrieves the radius of the cylinder.
                | 
                |     Example:
                | 
                |            This example retrieves the Radius of theMeasurableCylinder
                |            measure.
                |            
                | 
                |              Set theMeasureService = CATIA.ActiveEditor.GetService("MeasurableService")
                |              Dim theMeasurableCylinder As MeasurableCylinder
                |              Set theMeasurableCylinder = theMeasureService.GetMeasurable(theSelection, CAAMeasurableCylinder)
                |              Dim theRadius As Double
                |              theRadius = theMeasurableCylinder.GetRadius

        :return: float
        """
        return self.com_object.GetRadius()

    def __repr__(self):
        return f'MeasurableCylinder(name="{self.name}")'
