"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-27 14:29:47.477239

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.mmr_automation_interfaces.hybrid_shape import HybridShape


class Point(HybridShape):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     CATMmrAutomationInterfaces.HybridShape
                |                         Point
                | 
                | Represents the hybrid shape Point feature object.
                | Role: Declare hybrid shape Point root feature object. All interfaces for
                | different type of Point derives HybridShapePoint.
                | 
                | Use the CATIAHybridShapeFactory to create a HybridShapePoint
                | objects.
                | 
                | See also:
                |     HybridShapeFactory
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def get_coordinates(self, o_coordinates: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub GetCoordinates(CATSafeArrayVariant oCoordinates)
                |     Gets cartesian coordinates of the point.
                | 
                |     Parameters:
                | 
                |         oCoordinates
                |             coordinates of the point. 
                | 
                |     See also:
                |         HybridShapeFactory

        :param tuple o_coordinates:
        :return: None
        """
        return self.com_object.GetCoordinates(o_coordinates)

    def set_coordinates(self, o_coordinates: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub SetCoordinates(CATSafeArrayVariant oCoordinates)
                |     Sets cartesian coordinates of the point.
                |     Note: SetCoordinates can only be used on CATIAHybridShapePointCoord
                |     feature
                | 
                |     Parameters:
                | 
                |         iCoordinates
                |             coordinates of the point. 
                | 
                |     See also:
                |         HybridShapeFactory

        :param tuple o_coordinates:
        :return: None
        """
        return self.com_object.SetCoordinates(o_coordinates)

    def __repr__(self):
        return f'Point(name="{ self.name }")'
