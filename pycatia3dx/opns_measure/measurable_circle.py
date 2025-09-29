"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.opns_measure.measurable_curve import MeasurableCurve


class MeasurableCircle(MeasurableCurve):
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
                |                         CATOpnsMeasureIDLItf.MeasurableCurve
                |                             MeasurableCircle
                | 
                | Interface representing the measurement on a circle.
                | Get the length and the characteristic points on the curve (start, middle and
                | end points) by inheritance. Get the center, the radius, the angle and the axis
                | vector of the circle.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def get_angle(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetAngle() As double
                |     Retrieves the angle of the circle.
                | 
                |     Example:
                | 
                |            This example retrieves the Angle of theMeasurableCircle
                |            measure.
                |            
                | 
                |              Set theMeasureService = CATIA.ActiveEditor.GetService("MeasurableService")
                |              Dim theMeasurableCircle As MeasurableCircle
                |              Set theMeasurableCircle = theMeasureService.GetMeasurable(theSelection, CAAMeasurableCircle)
                |              Dim theAngle As Double
                |              theAngle = theMeasurableCircle.GetAngle

        :return: float
        """
        return self.com_object.GetAngle()

    def get_axis(self, o_x_vector: float, o_y_vector: float, o_z_vector: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetAxis(double oXVector,double oYVector,double oZVector)
                |     Retrieves the axis vector of the circle.
                | 
                |     Example:
                | 
                |            This example retrieves the axis vector of theMeasurableCircle
                |            measure.
                |            
                | 
                |              Set theMeasureService = CATIA.ActiveEditor.GetService("MeasurableService")
                |              Dim theMeasurableCircle As MeasurableCircle
                |              Set theMeasurableCircle = theMeasureService.GetMeasurable(theSelection, CAAMeasurableCircle)
                |              Dim theXVector As Double
                |              Dim theYVector As Double
                |              Dim theZVector As Double
                |              theMeasurableCircle.GetAxis theXVector, theYVector,
                |              theZVector

        :param float o_x_vector:
        :param float o_y_vector:
        :param float o_z_vector:
        :return: None
        """
        return self.com_object.GetAxis(o_x_vector, o_y_vector, o_z_vector)

    def get_center(self, o_x_center: float, o_y_center: float, o_z_center: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetCenter(double oXCenter,double oYCenter,double oZCenter)
                |     Retrieves the position of the center of the circle.
                | 
                |     Example:
                | 
                |            This example retrieves the position of the center of
                |            theMeasurableCircle measure.
                |            
                | 
                |              Set theMeasureService = CATIA.ActiveEditor.GetService("MeasurableService")
                |              Dim theMeasurableCircle As MeasurableCircle
                |              Set theMeasurableCircle = theMeasureService.GetMeasurable(theSelection, CAAMeasurableCircle)
                |              Dim theXCenter As Double
                |              Dim theYCenter As Double
                |              Dim theZCenter As Double
                |              theMeasurableCircle.GetCenter theXCenter, theYCenter,
                |              theZCenter

        :param float o_x_center:
        :param float o_y_center:
        :param float o_z_center:
        :return: None
        """
        return self.com_object.GetCenter(o_x_center, o_y_center, o_z_center)

    def get_radius(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetRadius() As double
                |     Retrieves the radius of the circle.
                | 
                |     Example:
                | 
                |            This example retrieves the Radius of theMeasurableCircle
                |            measure.
                |            
                | 
                |              Set theMeasureService = CATIA.ActiveEditor.GetService("MeasurableService")
                |              Dim theMeasurableCircle As MeasurableCircle
                |              Set theMeasurableCircle = theMeasureService.GetMeasurable(theSelection, CAAMeasurableCircle)
                |              Dim theRadius As Double
                |              theRadius = theMeasurableCircle.GetRadius

        :return: float
        """
        return self.com_object.GetRadius()

    def __repr__(self):
        return f'MeasurableCircle(name="{self.name}")'
