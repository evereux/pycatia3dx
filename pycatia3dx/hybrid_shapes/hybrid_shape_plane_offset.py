"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-27 14:29:47.477239

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.hybrid_shapes.plane import Plane
from pycatia3dx.knowledge_interfaces.length import Length
from pycatia3dx.mode.reference import Reference


class HybridShapePlaneOffset(Plane):

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
                |                             HybridShapePlaneOffset
                | 
                | Offset plane.
                | Role: Allows to access data of the plane feature created with an offset to
                | another plane.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def offset(self) -> Length:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property Offset() As Length (Read Only)
                |     Returns the offset value.

        :return: Length
        """

        return Length(self.com_object.Offset)

    @property
    def orientation(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property Orientation() As long
                |     Returns or sets the plane orientation.
                |     Role: The orientation allows you to invert the plane from the reference
                |     plane.
                |     Legal values: the orientation is 1 if the plane orientation is not
                |     inverted, and -1 otherwise.

        :return: int
        """

        return self.com_object.Orientation

    @orientation.setter
    def orientation(self, value: int):
        """
        :param int value:
        """

        self.com_object.Orientation = value

    @property
    def plane(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property Plane() As Reference
                |     Returns or sets the reference plane.
                |     Sub-element(s) supported (see Boundary object): PlanarFace.

        :return: Reference
        """

        return Reference(self.com_object.Plane)

    @plane.setter
    def plane(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.Plane = value

    def __repr__(self):
        return f'HybridShapePlaneOffset(name="{ self.name }")'
