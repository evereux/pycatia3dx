"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.interfaces.service import Service
from pycatia3dx.opns_measure.measurable_in_context import MeasurableInContext
from pycatia3dx.system.any_object import AnyObject


class MeasurableService(Service):
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
                |                         MeasurableService
                | 
                | Interface representing the service to retrieve a measurable.
                | CATIApplication.ActiveEditor.GetService("MeasurableService")
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def get_measurable(self, i_measured_item: AnyObject, i_type: int) -> MeasurableInContext:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetMeasurable(AnyObject iMeasuredItem,CATMeasurableType iType) As
                | MeasurableInContext
                |     Retrieves the measurable object
                | 
                |     Example:
                | 
                |            This example get the Measurable from given
                |            MeasurableType.
                |            
                | 
                |              Set theMeasureService = CATIA.ActiveEditor.GetService("MeasurableService")
                |              Dim theMeasurableSurface As MeasurableSurface
                |              Set theMeasurableSurface = theMeasureService.GetMeasurable(theSelection, CAAMeasurableSurface)

        :param AnyObject i_measured_item:
        :param int i_type:
        :return: MeasurableInContext
        """
        return MeasurableInContext(self.com_object.GetMeasurable(i_measured_item.com_object, i_type))

    def __repr__(self):
        return f'MeasurableService(name="{self.name}")'
