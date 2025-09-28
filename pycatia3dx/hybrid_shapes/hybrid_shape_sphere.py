"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-27 14:29:47.477239

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.knowledge_interfaces.angle import Angle
from pycatia3dx.knowledge_interfaces.length import Length
from pycatia3dx.mmr_automation_interfaces.hybrid_shape import HybridShape
from pycatia3dx.mode.reference import Reference


class HybridShapeSphere(HybridShape):

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
                |                         HybridShapeSphere
                | 
                | Represents the hybrid shape sphere feature object.
                | Role: To access the data of the hybrid shape sphere explicit feature
                | object.
                | The Sphere feature : a Sphere is made up of 4 angles parameters.
                | 
                | See also:
                |     HybridShapeFactory
    
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
                |     Returns or sets axis on the object.
                | 
                |     Parameters:
                | 
                |         oDir
                |             return value for CATScript applications, with (IDLRETVAL) function
                |             type 
                | 
                |     See also:
                |         Reference
                |     See also:
                |         HybridShapeFactory

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
    def begin_meridian_angle(self) -> Angle:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property BeginMeridianAngle() As Angle (Read Only)
                |     Returns BeginMeridianAngle on the object.
                | 
                |     Parameters:
                | 
                |         oAngle
                |             return value for CATScript applications, with (IDLRETVAL) function
                |             type 
                | 
                |     See also:
                |         Angle
                |     See also:
                |         HybridShapeFactory

        :return: Angle
        """

        return Angle(self.com_object.BeginMeridianAngle)

    @property
    def begin_parallel_angle(self) -> Angle:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property BeginParallelAngle() As Angle (Read Only)
                |     Returns BeginParallelAngle on the object.
                | 
                |     Parameters:
                | 
                |         oAngle
                |             return value for CATScript applications, with (IDLRETVAL) function
                |             type 
                | 
                |     See also:
                |         Angle
                |     See also:
                |         HybridShapeFactory

        :return: Angle
        """

        return Angle(self.com_object.BeginParallelAngle)

    @property
    def center(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property Center() As Reference
                |     Returns or sets the sphere center.
                |     Sub-element(s) supported (see Boundary object): Vertex.
                | 
                |     Example:
                |         This example retrieves in HybShpSphereCenter the center of the
                |         HybShpSphere hybrid shape sphere.
                | 
                |          Dim HybShpSphereCenter As Reference
                |          HybShpSphereCenter = HybShpSphere.Center

        :return: Reference
        """

        return Reference(self.com_object.Center)

    @center.setter
    def center(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.Center = value

    @property
    def end_meridian_angle(self) -> Angle:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property EndMeridianAngle() As Angle (Read Only)
                |     Returns EndMeridianAngle on the object.
                | 
                |     Parameters:
                | 
                |         oAngle
                |             return value for CATScript applications, with (IDLRETVAL) function
                |             type 
                | 
                |     See also:
                |         Angle
                |     See also:
                |         HybridShapeFactory

        :return: Angle
        """

        return Angle(self.com_object.EndMeridianAngle)

    @property
    def end_parallel_angle(self) -> Angle:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property EndParallelAngle() As Angle (Read Only)
                |     Returns EndParallelAngle on the object.
                | 
                |     Parameters:
                | 
                |         oAngle
                |             return value for CATScript applications, with (IDLRETVAL) function
                |             type 
                | 
                |     See also:
                |         Angle
                |     See also:
                |         HybridShapeFactory

        :return: Angle
        """

        return Angle(self.com_object.EndParallelAngle)

    @property
    def limitation(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property Limitation(long iLimitationType)
                |     Returns whether the sphere is created as a whole sphere or
                |     not.
                |     Legal values: 0 for a sphere with angles and 1 for a whole
                |     sphere.
                | 
                |     Example:

        :return: bool
        """

        return self.com_object.Limitation

    @limitation.setter
    def limitation(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.Limitation = value

    @property
    def radius(self) -> Length:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property Radius() As Length (Read Only)
                |     Role: Get sphere radius.
                | 
                |     Parameters:
                | 
                |         oRadius
                |             Sphere radius return value for CATScript applications, with
                |             (IDLRETVAL) function type 
                | 
                |     See also:
                |         Length
                |     See also:
                |         HybridShapeFactory

        :return: Length
        """

        return Length(self.com_object.Radius)

    def set_begin_meridian_angle(self, i_angle: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub SetBeginMeridianAngle(double iAngle)
                |     Sets BeginMeridianAngle on the object.
                | 
                |     Parameters:
                | 
                |         iAngle
                | 
                |     See also:
                |         Angle
                |     See also:
                |         HybridShapeFactory

        :param float i_angle:
        :return: None
        """
        return self.com_object.SetBeginMeridianAngle(i_angle)

    def set_begin_parallel_angle(self, i_angle: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub SetBeginParallelAngle(double iAngle)
                |     Sets BeginParallelAngle on the object.
                | 
                |     Parameters:
                | 
                |         iAngle
                | 
                |     See also:
                |         Angle
                |     See also:
                |         HybridShapeFactory

        :param float i_angle:
        :return: None
        """
        return self.com_object.SetBeginParallelAngle(i_angle)

    def set_end_meridian_angle(self, i_angle: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub SetEndMeridianAngle(double iAngle)
                |     Sets EndMeridianAngle on the object.
                | 
                |     Parameters:
                | 
                |         iAngle
                | 
                |     See also:
                |         Angle
                |     See also:
                |         HybridShapeFactory

        :param float i_angle:
        :return: None
        """
        return self.com_object.SetEndMeridianAngle(i_angle)

    def set_end_parallel_angle(self, i_angle: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub SetEndParallelAngle(double iAngle)
                |     Sets EndParallelAngle on the object.
                | 
                |     Parameters:
                | 
                |         iAngle
                | 
                |     See also:
                |         Angle
                |     See also:
                |         HybridShapeFactory

        :param float i_angle:
        :return: None
        """
        return self.com_object.SetEndParallelAngle(i_angle)

    def set_radius(self, i_radius: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub SetRadius(double iRadius)
                |     Sets Radius on the object.
                | 
                |     Parameters:
                | 
                |         iAngle
                | 
                |     See also:
                |         Angle
                |     See also:
                |         HybridShapeFactory

        :param float i_radius:
        :return: None
        """
        return self.com_object.SetRadius(i_radius)

    def __repr__(self):
        return f'HybridShapeSphere(name="{ self.name }")'
