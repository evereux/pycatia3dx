"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.opns_measure.measurable_in_context import MeasurableInContext


class MeasurableSurface(MeasurableInContext):
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
                |                         MeasurableSurface
                | 
                | Interface representing the measurement on a surface.
                | Get the area, the center of gravity and the perimeter.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def get_area(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetArea() As double
                |     Retrieves the area of the surface.
                | 
                |     Example:
                | 
                |            This example retrieves the area of theMeasurableSurface
                |            measure.
                |            The area unit given by oArea is m²
                |            
                | 
                |              Set theMeasureService = CATIA.ActiveEditor.GetService("MeasurableService")
                |              Dim theMeasurableSurface As MeasurableSurface
                |              Set theMeasurableSurface = theMeasureService.GetMeasurable(theSelection, CAAMeasurableSurface)
                |              Dim theArea As Double
                |              theArea = theMeasurableSurface.GetArea

        :return: float
        """
        return self.com_object.GetArea()

    def get_area_c_of_g(self, o_area: float, o_xc_of_g: float, o_yc_of_g: float, o_zc_of_g: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetArea_COfG(double oArea,double oXCOfG,double oYCOfG,double
                | oZCOfG)
                |     Retrieves the area and the position of the center of gravity of the
                |     surface.
                | 
                |     Example:
                | 
                |            This example retrieves the area and the position of the center of
                |            gravity of theMeasurableSurface measure.
                |            The area unit given by oArea is m²
                |            
                | 
                |              Set theMeasureService = CATIA.ActiveEditor.GetService("MeasurableService")
                |              Dim theMeasurableSurface As MeasurableSurface
                |              Set theMeasurableSurface = theMeasureService.GetMeasurable(theSelection, CAAMeasurableSurface)
                |              Dim theArea As Double
                |              Dim theXCOfG As Double
                |              Dim theYCOfG As Double
                |              Dim theZCOfG As Double
                |              theMeasurableSurface.GetCOG theArea, theXCOfG, theYCOfG,
                |              theZCOfG

        :param float o_area:
        :param float o_xc_of_g:
        :param float o_yc_of_g:
        :param float o_zc_of_g:
        :return: None
        """
        return self.com_object.GetArea_COfG(o_area, o_xc_of_g, o_yc_of_g, o_zc_of_g)

    def get_c_of_g(self, o_xc_of_g: float, o_yc_of_g: float, o_zc_of_g: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetCOfG(double oXCOfG,double oYCOfG,double oZCOfG)
                |     Retrieves the position of the center of gravity of a
                |     surface.
                | 
                |     Example:
                | 
                |            This example retrieves the position of the center of gravity of
                |            theMeasurableSurface measure.
                |            
                | 
                |              Set theMeasureService = CATIA.ActiveEditor.GetService("MeasurableService")
                |              Dim theMeasurableSurface As MeasurableSurface
                |              Set theMeasurableSurface = theMeasureService.GetMeasurable(theSelection, CAAMeasurableSurface)
                |              Dim theXCOfG As Double
                |              Dim theYCOfG As Double
                |              Dim theZCOfG As Double
                |              theMeasurableSurface.GetCOG theXCOfG, theYCOfG,
                |              theZCOfG

        :param float o_xc_of_g:
        :param float o_yc_of_g:
        :param float o_zc_of_g:
        :return: None
        """
        return self.com_object.GetCOfG(o_xc_of_g, o_yc_of_g, o_zc_of_g)

    def get_perimeter(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetPerimeter() As double
                |     Retrieves the perimeter of the surface.
                | 
                |     Example:
                | 
                |            This example retrieves the area of theMeasurableSurface
                |            measure.
                |            The area unit given by oArea is m²
                |            
                | 
                |              Set theMeasureService = CATIA.ActiveEditor.GetService("MeasurableService")
                |              Dim theMeasurableSurface As MeasurableSurface
                |              Set theMeasurableSurface = theMeasureService.GetMeasurable(theSelection, CAAMeasurableSurface)
                |              Dim thePerimeter As Double
                |              thePerimeter = theMeasurableSurface.GetPerimeter

        :return: float
        """
        return self.com_object.GetPerimeter()

    def __repr__(self):
        return f'MeasurableSurface(name="{self.name}")'
