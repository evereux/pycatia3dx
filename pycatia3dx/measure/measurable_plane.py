"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.measure.measurable_surface import MeasurableSurface


class MeasurablePlane(MeasurableSurface):

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
                |                             MeasurablePlane
                | 
                | Interface representing the measurement on a plane.
                | Get the area, the center of gravity and the perimeter by inheritance. Get the
                | plane informations.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def get_plane(self, io_plane: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Sub GetPlane(CATSafeArrayVariant ioPlane)
                |     Retrieves informations of the plane.
                | 
                |     Parameters:
                | 
                |         ioPlane
                |             The informations of the plane with respect to the product
                |             coordinate system:
                | 
                |                 ioPlane(0) is the X coordinate of the origin
                |                 ioPlane(1) is the Y coordinate of the origin
                |                 ioPlane(2) is the Z coordinate of the origin
                |                 ioPlane(3) is the X coordinate of the first direction of the
                |                 plane
                |                 ioPlane(4) is the Y coordinate of the first direction of the
                |                 plane
                |                 ioPlane(5) is the Z coordinate of the first direction of the
                |                 plane
                |                 ioPlane(6) is the X coordinate of the second direction of the
                |                 plane
                |                 ioPlane(7) is the Y coordinate of the second direction of the
                |                 plane
                |                 ioPlane(8) is the Z coordinate of the second direction of the
                |                 plane 
                | 
                |     Example:
                | 
                |            This example retrieves informations of the plane of
                |            theMeasurablePlane measure.
                |            
                | 
                |              Set theMeasureService = CATIA.ActiveEditor.GetService("MeasurableService")
                |              Dim theMeasurablePlane As MeasurablePlane
                |              Set theMeasurablePlane = theMeasureService.GetMeasurable(theSelection, CAAMeasurablePlane)
                |              Dim thePlane(8)
                |              theMeasurablePlane.GetPlane thePlane

        :param tuple io_plane:
        :return: None
        """
        return self.com_object.GetPlane(io_plane)

    def __repr__(self):
        return f'MeasurablePlane(name="{ self.name }")'
