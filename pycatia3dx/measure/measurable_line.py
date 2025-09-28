"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.measure.measurable_curve import MeasurableCurve


class MeasurableLine(MeasurableCurve):

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
                |                             MeasurableLine
                | 
                | Interface representing the measurement on a line.
                | Get the length and the characteristic points on the curve (start, middle and
                | end points) by inheritance. Get the origin and the direction of the
                | line.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def get_direction(self, o_x_vector: float, o_y_vector: float, o_z_vector: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Sub GetDirection(double oXVector,double oYVector,double
                | oZVector)
                |     Retrieves the direction of the line.
                | 
                |     Example:
                | 
                |            This example retrieves the direction of the line of
                |            theMeasurableLine measure.
                |            
                | 
                |              Set theMeasureService = CATIA.ActiveEditor.GetService("MeasurableService")
                |              Dim theMeasurableLine As MeasurableLine
                |              Set theMeasurableLine = theMeasureService.GetMeasurable(theSelection, CAAMeasurableLine)
                |              Dim theXVector As Double
                |              Dim theYVector As Double
                |              Dim theZVector As Double
                |              theMeasurableLine.GetDirection theXVector, theYVector,
                |              theZVector

        :param float o_x_vector:
        :param float o_y_vector:
        :param float o_z_vector:
        :return: None
        """
        return self.com_object.GetDirection(o_x_vector, o_y_vector, o_z_vector)

    def get_origin(self, o_x_origin: float, o_y_origin: float, o_z_origin: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Sub GetOrigin(double oXOrigin,double oYOrigin,double oZOrigin)
                |     Retrieves the position of the origin of the line.
                | 
                |     Example:
                | 
                |            This example retrieves the position of the origin of
                |            theMeasurableLine measure.
                |            
                | 
                |              Set theMeasureService = CATIA.ActiveEditor.GetService("MeasurableService")
                |              Dim theMeasurableLine As MeasurableLine
                |              Set theMeasurableLine = theMeasureService.GetMeasurable(theSelection, CAAMeasurableLine)
                |              Dim theXOrigin As Double
                |              Dim theYOrigin As Double
                |              Dim theZOrigin As Double
                |              theMeasurableLine.GetOrigin theXOrigin, theYOrigin,
                |              theZOrigin

        :param float o_x_origin:
        :param float o_y_origin:
        :param float o_z_origin:
        :return: None
        """
        return self.com_object.GetOrigin(o_x_origin, o_y_origin, o_z_origin)

    def __repr__(self):
        return f'MeasurableLine(name="{ self.name }")'
