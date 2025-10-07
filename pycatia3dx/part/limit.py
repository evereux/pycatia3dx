"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.knowledge_interfaces.length import Length
from pycatia3dx.mode.reference import Reference
from pycatia3dx.system.any_object import AnyObject


class Limit(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     Limit
                | 
                | Represents the limit of a prism or a hole shape.
                | 
                | See also:
                |     Prism, Hole
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def dimension(self) -> Length:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Dimension() As Length (Read Only)
                |     Returns or sets the limit dimension. This property is valid for the offset
                |     limit mode only, that is when CatLimitMode is set to catOffsetLimit .

        :return: Length
        """

        return Length(self.com_object.Dimension)

    @property
    def limit_mode(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property LimitMode() As CatLimitMode
                |     Returns or sets the limit mode.

        :return: CatLimitMode
        """

        return self.com_object.LimitMode

    @limit_mode.setter
    def limit_mode(self, value: int):
        """
        :param int value:
        """

        self.com_object.LimitMode = value

    @property
    def limiting_element(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property LimitingElement() As Reference
                |     Returns or sets the limiting element. This property is valid when the
                |     limiting object is a surface or a plane, that is when CatLimitMode is set to
                |     catUpToSurfaceLimit and catUpToPlaneLimit.
                |     To set the property, you can use the following Boundary object: Face.

        :return: Reference
        """

        return Reference(self.com_object.LimitingElement)

    @limiting_element.setter
    def limiting_element(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.LimitingElement = value

    def __repr__(self):
        return f'Limit(name="{ self.name }")'
