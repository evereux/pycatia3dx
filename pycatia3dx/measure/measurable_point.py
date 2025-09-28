"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.measure.measurable_in_context import MeasurableInContext


class MeasurablePoint(MeasurableInContext):

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
                |                         MeasurablePoint
                | 
                | Interface representing the measurement on a point.
                | Get the point coordinates.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def get_point(self, o_x_point: float, o_y_point: float, o_z_point: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Sub GetPoint(double oXPoint,double oYPoint,double oZPoint)
                |     Retrieves the position of the point.
                | 
                |     Example:
                | 
                |            This example retrieves the position of theMeasurablePoint
                |            measure.
                |            
                | 
                |              Set theMeasureService = CATIA.ActiveEditor.GetService("MeasurableService")
                |              Dim theMeasurablePoint As MeasurablePoint
                |              Set theMeasurablePoint = theMeasureService.GetMeasurable(theSelection, CAAMeasurablePoint)
                |              Dim theXPoint As Double
                |              Dim theYPoint As Double
                |              Dim theZPoint As Double
                |              theMeasurablePoint.GetPoint theXPoint, theYPoint,
                |              theZPoint

        :param float o_x_point:
        :param float o_y_point:
        :param float o_z_point:
        :return: None
        """
        return self.com_object.GetPoint(o_x_point, o_y_point, o_z_point)

    def __repr__(self):
        return f'MeasurablePoint(name="{ self.name }")'
