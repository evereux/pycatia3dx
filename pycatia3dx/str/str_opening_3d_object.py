"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.mode.reference import Reference
from pycatia3dx.system.any_object import AnyObject


class StrOpening3DObject(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     StrOpening3DObject
                | 
                | Object to manage the Structure Opening created using 3DObject.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def intersecting_element(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property IntersectingElement() As Reference
                |     Returns or Sets the element which defines the contour.
                | 
                |     Example:
                | 
                | 
                |              This example retrieves in IntersectingElement of the opening
                |              created in 3DObject mode.
                |              
                | 
                |              Dim ObjStrOpening3DObject As StrOpening3DObject
                |              Set ObjStrOpening3DObject = ObjStrOpening.StrOpening3DObject
                |              Set CylinderRef = ObjStrOpening3DObject.IntersectingElement

        :return: Reference
        """

        return Reference(self.com_object.IntersectingElement)

    @intersecting_element.setter
    def intersecting_element(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.IntersectingElement = value

    def __repr__(self):
        return f'StrOpening3DObject(name="{ self.name }")'
