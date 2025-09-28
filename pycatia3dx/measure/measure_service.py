"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.interfaces.service import Service
from pycatia3dx.measure.measure_between import MeasureBetween
from pycatia3dx.measure.measure_item import MeasureItem


class MeasureService(Service):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     InfInterfaces.Service
                |                         MeasureService
                | 
                | Interface representing the service to retrieve a measure between or
                | item.
                | CATIApplication.ActiveEditor.GetService("MeasureService")
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def get_measure_between(self, i_first_selections: tuple, i_second_selections: tuple) -> MeasureBetween:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Func GetMeasureBetween(CATSafeArrayVariant iFirstSelections,CATSafeArrayVariant
                | iSecondSelections) As MeasureBetween
                |     Retrieves the Measure Between
                | 
                |     Parameters:
                | 
                |         iFirstSelections
                |             The first set of the selected objects 
                |         iSecondSelections
                |             The second set of the selected objects 
                | 
                |     Returns:
                |         The Measure Between
                | 
                |         Example:
                |             This example get the MeasureBetween.
                | 
                |                Set theMeasureService = CATIA.ActiveEditor.GetService("MeasureService")
                |                Dim theMeasureBetween As MeasureBetween
                |                Set theMeasureBetween = theMeasureService.GetMeasureBetween(FirstSelections, SecondSelections)

        :param tuple i_first_selections:
        :param tuple i_second_selections:
        :return: MeasureBetween
        """
        return MeasureBetween(self.com_object.GetMeasureBetween(i_first_selections, i_second_selections))

    def get_measure_item(self, i_selections: tuple) -> MeasureItem:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Func GetMeasureItem(CATSafeArrayVariant iSelections) As
                | MeasureItem
                |     Retrieves the Measure Item
                | 
                |     Parameters:
                | 
                |         iSelections
                |             The set of the selected objects 
                | 
                |     Returns:
                |         The Measure Item
                | 
                |         Example:
                |             This example get the MeasureItem.
                | 
                |                Set theMeasureService = CATIA.ActiveEditor.GetService("MeasureService")
                |                Dim theMeasureItem As MeasureItem
                |                Set theMeasureItem = theMeasureService.GetMeasureItem(theSelection)

        :param tuple i_selections:
        :return: MeasureItem
        """
        return MeasureItem(self.com_object.GetMeasureItem(i_selections))

    def __repr__(self):
        return f'MeasureService(name="{ self.name }")'
