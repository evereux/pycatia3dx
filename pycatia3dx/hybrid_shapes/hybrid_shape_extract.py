"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-27 14:29:47.477239

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.mmr_automation_interfaces.hybrid_shape import HybridShape
from pycatia3dx.mode.reference import Reference


class HybridShapeExtract(HybridShape):

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
                |                         HybridShapeExtract
                | 
                | Represents the hybrid shape extract feature object.
                | Role: To access the data of the hybrid shape extract feature
                | object.
                | 
                | Use the CATIAHybridShapeFactory to create a HybridShapeExtract
                | object.
                | 
                | See also:
                |     HybridShapeFactory.AddNewExtract
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def angular_threshold(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property AngularThreshold() As double
                |     Returns or sets the AngularThreshold.
                | 
                |     Example: This example retrieves the AngularThreshold of the hybShpExtract
                |     in AngularThH.
                | 
                |      Dim AngularThH as double
                |      AngularThH = hybShpExtract.AngularThreshold

        :return: float
        """

        return self.com_object.AngularThreshold

    @angular_threshold.setter
    def angular_threshold(self, value: float):
        """
        :param float value:
        """

        self.com_object.AngularThreshold = value

    @property
    def angular_threshold_activity(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property AngularThresholdActivity() As boolean
                |     Returns or sets the AngularThresholdActivity.
                | 
                |     Example: This example retrieves the AngularThresholdActivity of the
                |     hybShpExtract in AngularActivity .
                | 
                |      Dim AngularActivity as boolean 
                |      AngularActivity = hybShpExtract.AngularThresholdActivity

        :return: bool
        """

        return self.com_object.AngularThresholdActivity

    @angular_threshold_activity.setter
    def angular_threshold_activity(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.AngularThresholdActivity = value

    @property
    def complementary_extract(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property ComplementaryExtract() As boolean
                |     Returns or sets the ComplementaryExtract checked/unchecked for the extract.

        :return: bool
        """

        return self.com_object.ComplementaryExtract

    @complementary_extract.setter
    def complementary_extract(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.ComplementaryExtract = value

    @property
    def curvature_threshold(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property CurvatureThreshold() As double
                |     Returns or sets the CurvatureThreshold.
                | 
                |     Example: This example retrieves the CurvatureThreshold of the hybShpExtract
                |     in CurvatureThH.
                | 
                |      Dim CurvatureThH as double
                |      CurvatureThH = hybShpExtract.CurvatureThreshold

        :return: float
        """

        return self.com_object.CurvatureThreshold

    @curvature_threshold.setter
    def curvature_threshold(self, value: float):
        """
        :param float value:
        """

        self.com_object.CurvatureThreshold = value

    @property
    def curvature_threshold_activity(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property CurvatureThresholdActivity() As boolean
                |     Returns or sets the CurvatureThresholdActivity.
                | 
                |     Example: This example retrieves the CurvatureThresholdActivity of the
                |     hybShpExtract in CurvatureActivity .
                | 
                |      Dim CurvatureActivity as boolean 
                |      CurvatureActivity = hybShpExtract.CurvatureThresholdActivity

        :return: bool
        """

        return self.com_object.CurvatureThresholdActivity

    @curvature_threshold_activity.setter
    def curvature_threshold_activity(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.CurvatureThresholdActivity = value

    @property
    def distance_threshold(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property DistanceThreshold() As double
                |     Returns or sets the DistanceThreshold.
                | 
                |     Example: This example retrieves the DistanceThreshold of the hybShpExtract
                |     in DistanceThH.
                | 
                |      Dim DistanceThH as double
                |      DistanceThH = hybShpExtract.DistanceThreshold

        :return: float
        """

        return self.com_object.DistanceThreshold

    @distance_threshold.setter
    def distance_threshold(self, value: float):
        """
        :param float value:
        """

        self.com_object.DistanceThreshold = value

    @property
    def distance_threshold_activity(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property DistanceThresholdActivity() As boolean
                |     Returns or sets the DistanceThresholdActivity.
                | 
                |     Example: This example retrieves the DistanceThresholdActivity of the
                |     hybShpExtract in DistanceActivity .
                | 
                |      Dim DistanceActivity as boolean 
                |      DistanceActivity = hybShpExtract.DistanceThresholdActivity

        :return: bool
        """

        return self.com_object.DistanceThresholdActivity

    @distance_threshold_activity.setter
    def distance_threshold_activity(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.DistanceThresholdActivity = value

    @property
    def elem(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property Elem() As Reference
                |     Returns or sets the sub element used as init for the
                |     propagation.
                | 
                |     See also:
                |         HybridShapeFactory

        :return: Reference
        """

        return Reference(self.com_object.Elem)

    @elem.setter
    def elem(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.Elem = value

    @property
    def is_federated(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property IsFederated() As boolean
                |     Returns or sets the IsFederated flag checked/unchecked for the extract.

        :return: bool
        """

        return self.com_object.IsFederated

    @is_federated.setter
    def is_federated(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.IsFederated = value

    @property
    def propagation_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property PropagationType() As long
                |     Returns or sets the type of propagation for the extract.
                |     The propagation types for the extract can have the following
                |     values:
                | 
                |         1 for extraction propagation in point continuity
                |         2 for extraction propagation in tangent continuity
                |         3 for extraction without propagation

        :return: int
        """

        return self.com_object.PropagationType

    @propagation_type.setter
    def propagation_type(self, value: int):
        """
        :param int value:
        """

        self.com_object.PropagationType = value

    @property
    def support(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property Support() As Reference
                |     Returns or sets the support for the extract.

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
        return f'HybridShapeExtract(name="{ self.name }")'
