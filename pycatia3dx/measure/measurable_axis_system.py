"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.measure.measurable_in_context import MeasurableInContext


class MeasurableAxisSystem(MeasurableInContext):

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
                |                         MeasurableAxisSystem
                | 
                | Interface representing the measurement on an axis system.
                | Get the position of the axis system.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def get_axis(self, io_axis_position: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Sub GetAxis(CATSafeArrayVariant ioAxisPosition)
                |     Retrieves the information of the axis system.
                | 
                |     Parameters:
                | 
                |         ioAxisPosition
                |             The information of the axis system with respect to the product
                |             coordinate system:
                | 
                |                 ioAxisPosition(0) is the X coordinate of the origin of the axis
                |                 system
                |                 ioAxisPosition(1) is the Y coordinate of the origin of the axis
                |                 system
                |                 ioAxisPosition(2) is the Z coordinate of the origin of the axis
                |                 system
                |                 ioAxisPosition(3) is the X coordinate of the first direction of
                |                 the axis system
                |                 ioAxisPosition(4) is the Y coordinate of the first direction of
                |                 the axis system
                |                 ioAxisPosition(5) is the Z coordinate of the first direction of
                |                 the axis system
                |                 ioAxisPosition(6) is the X coordinate of the second direction
                |                 of the axis system
                |                 ioAxisPosition(7) is the Y coordinate of the second direction
                |                 of the axis system
                |                 ioAxisPosition(8) is the Z coordinate of the second direction
                |                 of the axis system
                |                 ioAxisPosition(9) is the X coordinate of the third direction of
                |                 the axis system
                |                 ioAxisPosition(10) is the Y coordinate of the third direction
                |                 of the axis system
                |                 ioAxisPosition(11) is the Z coordinate of the third direction
                |                 of the axis system 
                | 
                |     Example:
                | 
                |            This example retrieves information of the axis system of
                |            theMeasurableAxisSystem measure.
                |            
                | 
                |              Set theMeasureService = CATIA.ActiveEditor.GetService("MeasurableService")
                |              Dim theMeasurableAxisSystem As
                |              MeasurableAxisSystem
                |              Set theMeasurableAxisSystem = theMeasureService.GetMeasurable(theSelection, CAAMeasurableAxisSystem)
                |              Dim theAxisPosition(11)
                |              theMeasurableAxisSystem.GetAxisSystem
                |              theAxisPosition

        :param tuple io_axis_position:
        :return: None
        """
        return self.com_object.GetAxis(io_axis_position)

    def __repr__(self):
        return f'MeasurableAxisSystem(name="{ self.name }")'
