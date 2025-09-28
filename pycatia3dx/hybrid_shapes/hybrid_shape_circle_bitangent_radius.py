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


class HybridShapeCircleBitangentRadius(HybridShapeCircle):

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
                |                             HybridShapeCircleBitangentRadius
                | 
                | Represents the hybrid shape circle object defined using a radius and tangent to
                | two curves.
                | Role: To access the data of the hybrid shape circle object.
                | 
                | This data includes:
                | 
                |     The circle radius
                |     The two curves to which the circle is tangent
                |     The surface that supports the circle
                |     The orientation of each curve
                | 
                | Use the CATIAHybridShapeFactory to create a HybridShapeCircleBitangentRadius
                | object.
                | 
                | See also:
                |     HybridShapeFactory
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def begin_of_circle(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property BeginOfCircle() As long
                |     Return or Set the number of the beginning curve of the circle. This
                |     parameter is used to stabilize the resulting circle
                | 
                |     Example:
                | 
                |          This example set the beginning wire index of
                |          the hybShpcircle hybrid shape circle 
                |          
                | 
                |          hybShpcircle.BeginOfCircle = 1

        :return: int
        """

        return self.com_object.BeginOfCircle

    @begin_of_circle.setter
    def begin_of_circle(self, value: int):
        """
        :param int value:
        """

        self.com_object.BeginOfCircle = value

    @property
    def curve1(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property Curve1() As Reference
                |     Returns or sets the first curve to which the circle is or will be
                |     tangent.
                |     Sub-element(s) supported (see Boundary object): TriDimFeatEdge or
                |     BiDimFeatEdge.
                | 
                |     Example:
                |         This example retrieves in HybShpCircleFirstCurve the first curve to
                |         which the HybShpCircle hybrid shape circle is tangent.
                | 
                |          Dim HybShpCircleFirstCurve As Reference 
                |          HybShpCircleFirstCurve = HybShpCircle.Curve1

        :return: Reference
        """

        return Reference(self.com_object.Curve1)

    @curve1.setter
    def curve1(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.Curve1 = value

    @property
    def curve2(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property Curve2() As Reference
                |     Returns or sets the second curve to which the circle is or will be
                |     tangent.
                |     Sub-element(s) supported (see Boundary object): TriDimFeatEdge or
                |     BiDimFeatEdge.
                | 
                |     Example:
                |         This example sets the second curve to which the HybShpCircle hybrid
                |         shape circle will be tangent to Crv5.
                | 
                |          HybShpCircle.Curve2 Crv5

        :return: Reference
        """

        return Reference(self.com_object.Curve2)

    @curve2.setter
    def curve2(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.Curve2 = value

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
                |     HybShpCircle hybrid shape circle feature
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
                |           the HybShpCircle hybrid shape circle feature
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
    def discrimination_index(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property DiscriminationIndex() As long
                |     Return or set the discrimination index of the current circle. Several
                |     resulting solutions produced by the operator can be same oriented regarding to
                |     the input wire bodies. In such a case, they are sorted in order to distinguish
                |     them. The Sequence FirstOrientation - SecondOrientation - DiscriminationIndex
                |     allows you to identify a unique one-domain solution.
                | 
                |     Example:
                | 
                |          This example set the discrimination index of
                |          the hybShpcircle hybrid shape circle 
                |          
                | 
                |          hybShpcircle.DiscriminationIndex = 2

        :return: int
        """

        return self.com_object.DiscriminationIndex

    @discrimination_index.setter
    def discrimination_index(self, value: int):
        """
        :param int value:
        """

        self.com_object.DiscriminationIndex = value

    @property
    def orientation1(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property Orientation1() As long
                |     Returns or sets the orientation of the first curve to which the circle is
                |     tangent.
                |     Role: The orientation of the first curve determines the side of this curve
                |     taken into account to find the point where the circle is tangent to the
                |     curve.
                |     Legal values: To be provided by Claire (1/-1??)
                | 
                |     Example:
                |         This example sets the orientation of the first curve to which the
                |         HybShpCircle hybrid shape circle is tangent to
                |         reverse.
                | 
                |          HybShpCircle.Orientation1 -1

        :return: int
        """

        return self.com_object.Orientation1

    @orientation1.setter
    def orientation1(self, value: int):
        """
        :param int value:
        """

        self.com_object.Orientation1 = value

    @property
    def orientation2(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property Orientation2() As long
                |     Returns or sets the orientation of the second curve to which the circle is
                |     tangent.
                |     Role: The orientation of the second curve determines the side of this curve
                |     taken into account to find the point where the circle is tangent to the
                |     curve.
                |     Legal values: To be provided by Claire (1/-1??)
                | 
                |     Example:
                |         This example retrieves in HybShpCircleOrientation the orientation of
                |         the second curve to which the HybShpCircle hybrid shape circle is
                |         tangent.
                | 
                |          HybShpCircleOrientation = HybShpCircle.Orientation2

        :return: int
        """

        return self.com_object.Orientation2

    @orientation2.setter
    def orientation2(self, value: int):
        """
        :param int value:
        """

        self.com_object.Orientation2 = value

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
                |     hybrid shape circle.
                | 
                |      Dim HybShpCircleRadius As Length
                |      HybShpCircleRadius = HybShpCircle.Radius

        :return: Length
        """

        return Length(self.com_object.Radius)

    @property
    def support(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property Support() As Reference
                |     Returns or sets the circle support surface.
                |     Sub-element(s) supported (see Boundary object): Face.
                | 
                |     Example:
                |         This example retrieves in HybShpCircleSupportSurf the support surface
                |         of the HybShpCircle hybrid shape circle.
                | 
                |          Dim HybShpCircleSupportSurf As Reference 
                |          HybShpCircleSupportSurf = HybShpCircle.Support

        :return: Reference
        """

        return Reference(self.com_object.Support)

    @support.setter
    def support(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.Support = value

    @property
    def tangent_orientation1(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property TangentOrientation1() As long
                |     Returns or sets the tangent orientation of the circle first reference
                |     element. compared to the circle itself
                | 
                |     Example:
                | 
                |          This example retrieves the tangent orientation of first reference
                |          element of
                |          the hybShpcircle hybrid shape circle in firstOrient.
                |          
                | 
                |          Dim firstOrient As long
                |          firstOrient = hybShpcircle.FirstTangentOrientation

        :return: int
        """

        return self.com_object.TangentOrientation1

    @tangent_orientation1.setter
    def tangent_orientation1(self, value: int):
        """
        :param int value:
        """

        self.com_object.TangentOrientation1 = value

    @property
    def tangent_orientation2(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property TangentOrientation2() As long
                |     Returns or sets the tangent orientation of the circle second reference
                |     element. compared to the corner itself
                | 
                |     Example:
                | 
                |          This example retrieves the tangent orientation of second reference
                |          element of
                |          the hybShpcircle hybrid shape circle in secondOrient.
                |          
                | 
                |          Dim secondOrient As long
                |          secondOrient = hybShpcircle.SecondTangentOrientation

        :return: int
        """

        return self.com_object.TangentOrientation2

    @tangent_orientation2.setter
    def tangent_orientation2(self, value: int):
        """
        :param int value:
        """

        self.com_object.TangentOrientation2 = value

    @property
    def trim_mode(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property TrimMode() As long
                |     Returns or sets whether the circle reference curves are or should be
                |     trimmed.
                |     Legal values: 0 if the circle reference curves are not or should not be
                |     trimmed, 1 if the circle reference curves are or should be trimmed, 2 if only
                |     the first circle reference curve is or should be trimmed, 3 if only the second
                |     circle reference curve is or should be trimmed,
                | 
                |     Example:
                | 
                |          This example sets that the corner reference curves of
                |          the hybShpCircle hybrid shape circle should be
                |          trimmed.
                |          
                | 
                |          hybShpCircle.TrimMode = 1

        :return: int
        """

        return self.com_object.TrimMode

    @trim_mode.setter
    def trim_mode(self, value: int):
        """
        :param int value:
        """

        self.com_object.TrimMode = value

    def __repr__(self):
        return f'HybridShapeCircleBitangentRadius(name="{ self.name }")'
