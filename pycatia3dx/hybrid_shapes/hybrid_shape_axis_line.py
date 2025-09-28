"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-27 14:29:47.477239

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.hybrid_shapes.hybrid_shape_direction import HybridShapeDirection
from pycatia3dx.mmr_automation_interfaces.hybrid_shape import HybridShape
from pycatia3dx.mode.reference import Reference


class HybridShapeAxisLine(HybridShape):

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
                |                         HybridShapeAxisLine
                | 
                | Represents the hybrid shape axis line feature object.
                | Role: To access the data of the hybrid shape axis line feature object. This
                | data includes:
                | 
                |     The element used to compute the axis
                |     The direction used in orientation of axis
                |     AxisLineType to change the axis type
                | 
                | Use the CATIAHybridShapeFactory to create a HybridShapeAxisLine
                | object.
                | 
                | See also:
                |     HybridShapeFactory
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def axis_line_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property AxisLineType() As long
                |     Returns or sets the axis line type.
                |     Legal values:
                | 
                |     1
                |         This option creates Axis along major axis if element is ellipse or
                |         oblong, Axis is aligned with direction specified if input is circle and
                |         coincides with revolution axis if element is revolution
                |         surface
                |     2
                |         This option creates Axis along minor axis if element is ellipse or
                |         oblong, Axis is normal to direction specified if input is
                |         circle
                |     3
                |         This option creates Axis normal to the element if it is circle, ellipse
                |         or oblong
                | 
                | Example:
                |     This example retrieves in oType the axis line type for the AxisLine hybrid
                |     shape feature.
                | 
                |      Dim oType
                |      Set oType = AxisLine.AxisLineType

        :return: int
        """

        return self.com_object.AxisLineType

    @axis_line_type.setter
    def axis_line_type(self, value: int):
        """
        :param int value:
        """

        self.com_object.AxisLineType = value

    @property
    def direction(self) -> HybridShapeDirection:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property Direction() As HybridShapeDirection
                |     Gets the reference direction used in computation of axis.
                |     This is useful only if the element selected is circle, arc or sphere. If
                |     the element is circle or arc Axis may be normal to reference direction or
                |     aligned with reference direction
                | 
                |     Example:
                |         This example retrieves in oDir the direction for the AxisLine hybrid
                |         shape feature.
                | 
                |          Dim oDir As CATIAHybridShapeDirection
                |          Set oDir = AxisLine.Direction

        :return: HybridShapeDirection
        """

        return HybridShapeDirection(self.com_object.Direction)

    @direction.setter
    def direction(self, value: HybridShapeDirection):
        """
        :param HybridShapeDirection value:
        """

        self.com_object.Direction = value

    @property
    def element(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property Element() As Reference
                |     Returns or sets the element from which axis is computed.
                | 
                |     Example:
                |         This example retrieves in Element the element from which axis is
                |         computed for the AxisLine hybrid shape feature.
                | 
                |          Dim Element As Reference 
                |          Set Element = AxisLine.Element

        :return: Reference
        """

        return Reference(self.com_object.Element)

    @element.setter
    def element(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.Element = value

    def __repr__(self):
        return f'HybridShapeAxisLine(name="{ self.name }")'
