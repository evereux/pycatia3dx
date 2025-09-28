"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-27 14:29:47.477239

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.hybrid_shapes.hybrid_shape_circle import HybridShapeCircle
from pycatia3dx.knowledge_interfaces.length import Length
from pycatia3dx.mode.reference import Reference


class HybridShapeCircleCenterAxis(HybridShapeCircle):

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
                |                         CATGSMIDLItf.HybridShapeCircle
                |                             HybridShapeCircleCenterAxis
                | 
                | Represents the hybrid shape circle object defined using a point and
                | axis/line.
                | Role: To access the data of the hybrid shape circle center axis
                | object.
                | 
                | This data includes:
                | 
                |     Point
                |     Axis/Line
                |     Value of radius/diameter
                |     Diameter Mode
                |     Projection Mode
                | 
                | Use the CATIAHybridShapeFactory to create a HybridShapeCircleCenterAxis
                | object.
                | 
                | See also:
                |     HybridShapeFactory.AddNewCircleCenterAxis
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def axis(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property Axis() As Reference
                |     Returns or sets the Axis of the circle.
                | 
                |     Example:
                |         This example retrieves in CircleAxis the Axis of plane in which circle
                |         is lying from HybShpCircle hybrid shape circle center axis
                |         feature
                | 
                |          Dim CircleAxis As Reference 
                |          Set CircleAxis = HybShpCircle.Axis

        :return: Reference
        """

        return Reference(self.com_object.Axis)

    @axis.setter
    def axis(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.Axis = value

    @property
    def diameter(self) -> Length:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property Diameter() As Length (Read Only)
                |     Returns the circle diameter. It is expressed as a Length literal. Succeeds
                |     only if DiameterMode is set to True. 
                | 
                | Example:
                |     This example retrieves in HybShpCircleDiameter the diameter of the
                |     HybShpCircle hybrid shape circle center axis feature
                | 
                |      Dim HybShpCircleDiameter As Length
                |      HybShpCircleDiameter = HybShpCircle.Diameter

        :return: Length
        """

        return Length(self.com_object.Diameter)

    @property
    def diameter_mode(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property DiameterMode() As boolean
                |     Returns or sets the DiameterMode.
                |     Legal values: True implies diameter False implies radius (default). When
                |     DiameterMode is changed, Radius/Diameter value, which is stored will not be
                |     modified.
                | 
                |     Example:
                | 
                |           This example sets that the DiameterMode of
                |           the HybShpCircle hybrid shape circle center axis
                |           feature
                |           
                | 
                |           HybShpCircle.DiameterMode = True

        :return: bool
        """

        return self.com_object.DiameterMode

    @diameter_mode.setter
    def diameter_mode(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.DiameterMode = value

    @property
    def point(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property Point() As Reference
                |     Returns or sets the Point of the circle.
                | 
                |     Example:
                |         This example retrieves in CirclePoint the point used for center
                |         computation from HybShpCircle hybrid shape circle center axis
                |         feature
                | 
                |          Dim CirclePoint As Reference 
                |          Set CirclePoint = HybShpCircle.Point

        :return: Reference
        """

        return Reference(self.com_object.Point)

    @point.setter
    def point(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.Point = value

    @property
    def projection_mode(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property ProjectionMode() As boolean
                |     Returns or sets the ProjectionMode.
                |     Legal values: True (default) implies point will be projected on to
                |     axis/line False implies that point will be center of the
                |     circle.
                | 
                |     Example:
                | 
                |           This example sets that the ProjectionMode of
                |           the HybShpCircle hybrid shape circle center axis
                |           feature
                |           
                | 
                |           HybShpCircle.ProjectionMode = True

        :return: bool
        """

        return self.com_object.ProjectionMode

    @projection_mode.setter
    def projection_mode(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.ProjectionMode = value

    @property
    def radius(self) -> Length:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property Radius() As Length (Read Only)
                |     Returns the circle radius. It is expressed as a Length literal. Succeeds
                |     only if DiameterMode is set to False. 
                | Example:
                |     This example retrieves in HybShpCircleRadius the radius of the HybShpCircle
                |     hybrid shape circle center axis feature
                | 
                |      Dim HybShpCircleRadius As Length
                |      HybShpCircleRadius = HybShpCircle.Radius

        :return: Length
        """

        return Length(self.com_object.Radius)

    def __repr__(self):
        return f'HybridShapeCircleCenterAxis(name="{ self.name }")'
