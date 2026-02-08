"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.measure.measurable_in_context import MeasurableInContext


class MeasurableCurve(MeasurableInContext):
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
                |                         MeasurableCurve
                | 
                | Interface representing the measurement on a curve.
                | Get the length and the characteristic points on the curve(start, middle and end
                | points).
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def get_length(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetLength() As double
                |     Retrieves the Length of the curve.
                | 
                |     Example:
                | 
                |            This example retrieves the Length of theMeasurableCurve
                |            measure.
                |            
                | 
                |              Set theMeasureService = CATIA.ActiveEditor.GetService("MeasurableService")
                |              Dim theMeasurableCurve As MeasurableCurve
                |              Set theMeasurableCurve = theMeasureService.GetMeasurable(theSelection, CAAMeasurableCurve)
                |              Dim theLength As Double
                |              theLength = theMeasurableCurve.GetLength

        :return: float
        """
        return self.com_object.GetLength()

    def get_points(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetPoints(CATSafeArrayVariant ioStartPoint,CATSafeArrayVariant
                | ioMidPoint,CATSafeArrayVariant ioEndPoint)
                |     Retrieves the characteristic points of the curve : the start point, the middle point and the end point.
                | 
                |     Parameters:
                | 
                |         ioStartPoint
                |             The information of the start point of the curve with respect to the
                |             product coordinate system:
                | 
                |                 ioStartPoint(0) is the X coordinate of the startpoint of the
                |                 curve
                |                 ioStartPoint(1) is the Y coordinate of the startpoint of the
                |                 curve
                |                 ioStartPoint(2) is the Z coordinate of the startpoint of the
                |                 curve 
                | 
                |         ioMidPoint
                |             The information of the middle point of the curve with respect to
                |             the product coordinate system:
                | 
                |                 oCoordinates(0) is the X coordinate of the midpoint of the
                |                 curve
                |                 oCoordinates(1) is the Y coordinate of the midpoint of the
                |                 curve
                |                 oCoordinates(2) is the Z coordinate of the midpoint of the
                |                 curve 
                | 
                |         ioEndPoint
                |             The information of the end point of the curve with respect to the
                |             product coordinate system:
                | 
                |                 oCoordinates(0) is the X coordinate of the endpoint of the
                |                 curve
                |                 oCoordinates(1) is the Y coordinate of the endpoint of the
                |                 curve
                |                 oCoordinates(2) is the Z coordinate of the endpoint of the
                |                 curve 
                | 
                |     Example:
                | 
                |            This example retrieves the characteristic points of the curve of
                |            theMeasurableCurve measure.
                |            
                | 
                |              Set theMeasureService = CATIA.ActiveEditor.GetService("MeasurableService")
                |              Dim theMeasurableCurve As MeasurableCurve
                |              Set theMeasurableCurve = theMeasureService.GetMeasurable(theSelection, CAAMeasurableCurve)
                |              Dim theStartPoint(2)
                |              Dim theMidPoint(2)
                |              Dim theEndPoint(2)
                |              theMeasurableCurve.GetPoints theStartPoint, theMidPoint,
                |              theEndPoint

        :return: tuple
        """
        # todo: check this method, does it require system service?
        return self.com_object.GetPoints()

    def __repr__(self):
        return f'MeasurableCurve(name="{self.name}")'
