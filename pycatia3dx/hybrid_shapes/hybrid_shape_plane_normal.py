"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-27 14:29:47.477239

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.hybrid_shapes.plane import Plane
from pycatia3dx.mode.reference import Reference


class HybridShapePlaneNormal(Plane):

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
                |                         CATGSMIDLItf.Plane
                |                             HybridShapePlaneNormal
                | 
                | Normal plane.
                | Role: Allows to access data of the plane feature normal to a curve at a given
                | point.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def curve(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property Curve() As Reference
                |     Role: Get the curve to which the plane is to be normal.
                | 
                |     Parameters:
                | 
                |         oCurve
                |             reference curve. 
                | 
                |     See also:
                |         Reference
                |     Returns:
                |         HRESULT S_OK if Ok E_FAIL else return error code for C++
                |         Implementations 
                |     See also:
                |         HybridShapeFactory

        :return: Reference
        """

        return Reference(self.com_object.Curve)

    @curve.setter
    def curve(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.Curve = value

    @property
    def point(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property Point() As Reference
                |     Role: Get the point where the plane is to be normal.
                | 
                |     Parameters:
                | 
                |         oPoint
                |             point 
                | 
                |     See also:
                |         Reference
                |     Returns:
                |         HRESULT S_OK if Ok E_FAIL else return error code for C++
                |         Implementations 
                |     See also:
                |         HybridShapeFactory

        :return: Reference
        """

        return Reference(self.com_object.Point)

    @point.setter
    def point(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.Point = value

    def __repr__(self):
        return f'HybridShapePlaneNormal(name="{ self.name }")'
