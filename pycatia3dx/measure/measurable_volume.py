"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.measure.measurable_in_context import MeasurableInContext


class MeasurableVolume(MeasurableInContext):
    """
        .. note::

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                SystemTS.IUnknown
                    System.IDispatch
                        System.CATBaseUnknown
                            System.CATBaseDispatch
                                System.AnyObject
                                    CATOpnsMeasureIDLItf.MeasurableInContext
                                        MeasurableVolume
                
                Interface representing the measurement on a volume.
                Get the volume, the area and the center of gravity.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def get_area(self) -> float:
        """
        .. note::

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                Func GetArea() As double
                    Retrieves the wet area of the volume.
                
                    Example:
                
                           This example retrieves the wet area of theMeasurableVolume
                           measure.
                           The area unit given by oArea is m²
                           
                
                             Set theMeasureService = CATIA.ActiveEditor.GetService("MeasurableService")
                             Dim theMeasurableVolume As MeasurableVolume
                             Set theMeasurableVolume = theMeasureService.GetMeasurable(theSelection, CAAMeasurableVolume)
                             Dim theArea As Double
                             theArea = theMeasurableVolume.GetArea

        :return: float
        """
        return self.com_object.GetArea()

    def get_c_of_g(self) -> tuple:
        """
        .. note::

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                Sub GetCOfG(double oXCOfG,double oYCOfG,double oZCOfG)
                    Retrieves the position of the center of gravity of a
                    volume.
                
                    Example:
                
                           This example retrieves the position of the center of gravity of
                           theMeasurableVolume measure.
                           
                
                             Set theMeasureService = CATIA.ActiveEditor.GetService("MeasurableService")
                             Dim theMeasurableVolume As MeasurableVolume
                             Set theMeasurableVolume = theMeasureService.GetMeasurable(theSelection, CAAMeasurableVolume)
                             Dim theXCOfG As Double
                             Dim theYCOfG As Double
                             Dim theZCOfG As Double
                             theMeasurableVolume.GetCOG theXCOfG, theYCOfG,
                             theZCOfG

        :return: tuple
        """
        return self.com_object.GetCOfG()

    def get_volume(self) -> float:
        """
        .. note::

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                Func GetVolume() As double
                    Retrieves the volume.
                
                    Example:
                
                           This example retrieves the volume of theMeasurableVolume
                           measure.
                           The area unit given by oArea is m^3
                           
                
                             Set theMeasureService = CATIA.ActiveEditor.GetService("MeasurableService")
                             Dim theMeasurableVolume As MeasurableVolume
                             Set theMeasurableVolume = theMeasureService.GetMeasurable(theSelection, CAAMeasurableVolume)
                             Dim theVolume As Double
                             theVolume = theMeasurableVolume.GetVolume

        :return: float
        """
        return self.com_object.GetVolume()

    def get_volume_area_c_of_g(self) -> tuple:
        """
        .. note::

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                Sub GetVolume_Area_COfG(double oVolume,double oArea,double oXCOfG,double
                oYCOfG,double oZCOfG)
                    Retrieves the volume, the wet area and the center of gravity of the volume.
                    All Units are MKS units (mm, m2 and m3)
                
                    Example:
                
                           This example retrieves the wet area of theMeasurableVolume
                           measure.
                           The area unit given by oVolume is m^3
                           The area unit given by oArea is m²
                           
                
                             Set theMeasureService = CATIA.ActiveEditor.GetService("MeasurableService")
                             Dim theMeasurableVolume As MeasurableVolume
                             Set theMeasurableVolume = theMeasureService.GetMeasurable(theSelection, CAAMeasurableVolume)
                             Dim theVolume As Double
                             Dim theArea As Double
                             Dim theXCOfG As Double
                             Dim theYCOfG As Double
                             Dim theZCOfG As Double
                             theMeasurableVolume.GetVolume_Area_COfG theVolume, theArea,
                             theXCOfG, theYCOfG, theZCOfG

        :return: tuple
        """
        return self.com_object.GetVolume_Area_COfG()

    def __repr__(self):
        return f'MeasurableVolume(name="{self.name}")'
