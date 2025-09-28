"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.measure.measurable_surface import MeasurableSurface


class MeasurableSphere(MeasurableSurface):

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
                |                             MeasurableSphere
                | 
                | Interface representing the measurement on a sphere.
                | Get the area, the center of gravity and the perimeter by inheritance. Get the
                | radius and the center point.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def get_center(self, o_x_center: float, o_y_center: float, o_z_center: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Sub GetCenter(double oXCenter,double oYCenter,double oZCenter)
                |     Retrieves the position of the center of the sphere.
                | 
                |     Example:
                | 
                |            This example retrieves the position of the center of
                |            theMeasurableSphere measure.
                |            
                | 
                |              Set theMeasureService = CATIA.ActiveEditor.GetService("MeasurableService")
                |              Dim theMeasurableSphere As MeasurableSphere
                |              Set theMeasurableSphere = theMeasureService.GetMeasurable(theSelection, CAAMeasurableSphere)
                |              Dim theXCenter As Double
                |              Dim theYCenter As Double
                |              Dim theZCenter As Double
                |              theMeasurableSphere.GetCenter theXCenter, theYCenter,
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

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Func GetRadius() As double
                |     Retrieves the radius of the sphere.
                | 
                |     Example:
                | 
                |            This example retrieves the Radius of theMeasurableSphere
                |            measure.
                |            
                | 
                |              Set theMeasureService = CATIA.ActiveEditor.GetService("MeasurableService")
                |              Dim theMeasurableSphere As MeasurableSphere
                |              Set theMeasurableSphere = theMeasureService.GetMeasurable(theSelection, CAAMeasurableSphere)
                |              Dim theRadius As Double
                |              theRadius = theMeasurableSphere.GetRadius

        :return: float
        """
        return self.com_object.GetRadius()

    def __repr__(self):
        return f'MeasurableSphere(name="{ self.name }")'
