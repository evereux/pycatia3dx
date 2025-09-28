"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-27 14:29:47.477239

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.hybrid_shapes.hybrid_shape_direction import HybridShapeDirection
from pycatia3dx.knowledge_interfaces.angle import Angle
from pycatia3dx.knowledge_interfaces.length import Length
from pycatia3dx.mmr_automation_interfaces.hybrid_shape import HybridShape
from pycatia3dx.mode.reference import Reference


class HybridShapeExtremumPolar(HybridShape):

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
                |                         HybridShapeExtremumPolar
                | 
                | Represents the hybrid shape extremum polar feature.
                | Role: To access the data of the extremum polar feature . This data
                | includes:
                | 
                |     The contour
                |     The support (if exist )
                |     The direction of evaluation
                |     The extermum type
                | 
                | Use the HybridShapeFactory.AddNewExtremumPolarto create a
                | HybridShapeExtremumPolar object.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def angle(self) -> Angle:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property Angle() As Angle (Read Only)
                |     returns the resulting angle of extremum.

        :return: Angle
        """

        return Angle(self.com_object.Angle)

    @property
    def contour(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property Contour() As Reference
                |     returns or sets the input contour.

        :return: Reference
        """

        return Reference(self.com_object.Contour)

    @contour.setter
    def contour(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.Contour = value

    @property
    def dir(self) -> HybridShapeDirection:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property Dir() As HybridShapeDirection
                |     returns or sets the direction of computation.

        :return: HybridShapeDirection
        """

        return HybridShapeDirection(self.com_object.Dir)

    @dir.setter
    def dir(self, value: HybridShapeDirection):
        """
        :param HybridShapeDirection value:
        """

        self.com_object.Dir = value

    @property
    def extremum_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property ExtremumType() As short
                |     returns or sets the type of extremum.

        :return: int
        """

        return self.com_object.ExtremumType

    @extremum_type.setter
    def extremum_type(self, value: int):
        """
        :param int value:
        """

        self.com_object.ExtremumType = value

    @property
    def origin(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property Origin() As Reference
                |     returns or sets the origin of the polar axis.

        :return: Reference
        """

        return Reference(self.com_object.Origin)

    @origin.setter
    def origin(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.Origin = value

    @property
    def radius(self) -> Length:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property Radius() As Length (Read Only)
                |     returns the resulting radius of extremum.

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
                |     returns or sets the support (if exist).

        :return: Reference
        """

        return Reference(self.com_object.Support)

    @support.setter
    def support(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.Support = value

    def __repr__(self):
        return f'HybridShapeExtremumPolar(name="{ self.name }")'
