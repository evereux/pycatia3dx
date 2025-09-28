"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-27 14:29:47.477239

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.knowledge_interfaces.length import Length
from pycatia3dx.knowledge_interfaces.real_param import RealParam
from pycatia3dx.mmr_automation_interfaces.hybrid_shape import HybridShape
from pycatia3dx.mode.reference import Reference


class HybridShapeBump(HybridShape):

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
                |                         HybridShapeBump
                | 
                | The Bump feature : an Bump is made up of a body to process and some Bump parameters.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def body_to_bump(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property BodyToBump() As Reference
                |     Returns or sets the element to Bump.

        :return: Reference
        """

        return Reference(self.com_object.BodyToBump)

    @body_to_bump.setter
    def body_to_bump(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.BodyToBump = value

    @property
    def center_tension(self) -> RealParam:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property CenterTension() As RealParam
                |     Returns or sets the tension center parameter.

        :return: RealParam
        """

        return RealParam(self.com_object.CenterTension)

    @center_tension.setter
    def center_tension(self, value: RealParam):
        """
        :param RealParam value:
        """

        self.com_object.CenterTension = value

    @property
    def continuity_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property ContinuityType() As long
                |     Returns or sets the continuity type ..
                |     Legal values: the continuity type is either
                | 
                |      PointContinuity      =0
                |      TangentContinuity    =1 
                |      CurvatureContinuity  =2

        :return: int
        """

        return self.com_object.ContinuityType

    @continuity_type.setter
    def continuity_type(self, value: int):
        """
        :param int value:
        """

        self.com_object.ContinuityType = value

    @property
    def deformation_center(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property DeformationCenter() As Reference
                |     Returns or sets the Deformation Center.

        :return: Reference
        """

        return Reference(self.com_object.DeformationCenter)

    @deformation_center.setter
    def deformation_center(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.DeformationCenter = value

    @property
    def deformation_dir(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property DeformationDir() As Reference
                |     Returns or sets the Deformation Direction.

        :return: Reference
        """

        return Reference(self.com_object.DeformationDir)

    @deformation_dir.setter
    def deformation_dir(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.DeformationDir = value

    @property
    def deformation_dist(self) -> Length:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property DeformationDist() As Length
                |     Returns the translate distance (CATIA Parameter).
                |     Note: Distance value is set or retrieve trough a Literaql
                |     parameter
                |     Parameters are value are given in the Part Unit
                |     Example : if Part Unit for dimensions is mm: for 1 mmm, oDefDist.Value will return 1.000

        :return: Length
        """

        return Length(self.com_object.DeformationDist)

    @deformation_dist.setter
    def deformation_dist(self, value: Length):
        """
        :param Length value:
        """

        self.com_object.DeformationDist = value

    @property
    def deformation_dist_value(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property DeformationDistValue() As double
                |     Returns or sets the Deformation distance (double) .
                |     Note: Distance value is expressed in MKS = Meters
                |     Example to set up 1mm , use .001

        :return: float
        """

        return self.com_object.DeformationDistValue

    @deformation_dist_value.setter
    def deformation_dist_value(self, value: float):
        """
        :param float value:
        """

        self.com_object.DeformationDistValue = value

    @property
    def limit_curve(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property LimitCurve() As Reference
                |     Returns or sets the limit curve.

        :return: Reference
        """

        return Reference(self.com_object.LimitCurve)

    @limit_curve.setter
    def limit_curve(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.LimitCurve = value

    @property
    def projection_dir(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property ProjectionDir() As Reference
                |     Returns or sets the limit curve.

        :return: Reference
        """

        return Reference(self.com_object.ProjectionDir)

    @projection_dir.setter
    def projection_dir(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.ProjectionDir = value

    def __repr__(self):
        return f'HybridShapeBump(name="{ self.name }")'
