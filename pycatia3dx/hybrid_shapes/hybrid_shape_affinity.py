"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-27 14:29:47.477239

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.knowledge_interfaces.real_param import RealParam
from pycatia3dx.mmr_automation_interfaces.hybrid_shape import HybridShape
from pycatia3dx.mode.reference import Reference


class HybridShapeAffinity(HybridShape):

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
                |                         HybridShapeAffinity
                | 
                | Represents the hybrid shape affinity feature object.
                | Role: To access the data of the hybrid shape affinity feature object. This data
                | includes:
                | 
                |     The element to transform using the affinity
                |     The affinity reference coordinate system origin
                |     The affinity reference coordinate system reference plane
                |     The affinity reference coordinate system first direction
                |     The affinity ratio along the x, y and z directions of the reference
                |     coordinate system
                |     The element to transform using the affinity
                | 
                | The reference coordinate system is always a direct one.
                | 
                | LICENSING INFORMATION: Creation of volume result requires GSO
                | License
                | if GSO License is not granted , setting of Volume context has not
                | effect
                | 
                | Use the CATIAHybridShapeFactory to create a HybridShapeAffinity
                | object.
                | 
                | See also:
                |     HybridShapeFactory
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def axis_first_direction(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property AxisFirstDirection() As Reference
                |     Returns or sets the first direction of the reference coordinate
                |     system.
                |     Sub-element(s) supported (see Boundary object): RectilinearTriDimFeatEdge,
                |     RectilinearBiDimFeatEdge or RectilinearMonoDimFeatEdge.
                | 
                |     Example:
                |         This example retrieves in FirstDir the first direction of the reference
                |         coordinate system used by the Affinity hybrid shape
                |         feature.
                | 
                |          Dim FirstDir As Reference 
                |          Set FirstDir = Affinity.AxisFirstDirection

        :return: Reference
        """

        return Reference(self.com_object.AxisFirstDirection)

    @axis_first_direction.setter
    def axis_first_direction(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.AxisFirstDirection = value

    @property
    def axis_origin(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property AxisOrigin() As Reference
                |     Returns or sets the origin of the reference coordinate
                |     system.
                |     Sub-element(s) supported (see Boundary object): Vertex.
                | 
                |     Example:
                |         This example retrieves in Origin the origin of the reference coordinate
                |         system used by the Affinity hybrid shape feature.
                | 
                |          Dim Origin As Reference 
                |          Set Origin = Affinity.AxisOrigin

        :return: Reference
        """

        return Reference(self.com_object.AxisOrigin)

    @axis_origin.setter
    def axis_origin(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.AxisOrigin = value

    @property
    def axis_plane(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property AxisPlane() As Reference
                |     Returns or sets the reference plane of the reference coordinate
                |     system.
                |     Sub-element(s) supported (see Boundary object):
                |     PlanarFace.
                | 
                |     Example:
                |         This example retrieves in RefPlane the reference plane of the reference
                |         coordinate system used by the Affinity hybrid shape
                |         feature.
                | 
                |          Dim RefPlane As Reference 
                |          Set RefPlane = Affinity.AxisPlane

        :return: Reference
        """

        return Reference(self.com_object.AxisPlane)

    @axis_plane.setter
    def axis_plane(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.AxisPlane = value

    @property
    def creation_mode(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property CreationMode() As boolean
                |     Returns or sets the creation mode(creation or
                |     modification).
                |     Legal values: True if the result is a creation feature and False if the
                |     result is a modification feature.
                | 
                |     Example:
                | 
                |          This example sets that the mode of
                |          the hybShpAffinity hybrid shape affinity to creation
                |          
                | 
                |          hybShpAffinity.CreationMode = True

        :return: bool
        """

        return self.com_object.CreationMode

    @creation_mode.setter
    def creation_mode(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.CreationMode = value

    @property
    def elem_to_transform(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property ElemToTransform() As Reference
                |     Returns or sets the element to transform using the
                |     affinity.
                | 
                |     Example:
                |         This example retrieves in ElementToTransform the element to transform
                |         for the Affinity hybrid shape feature.
                | 
                |          Dim ElementToTransform As Reference 
                |          Set ElementToTransform = Affinity.ElemToTransform

        :return: Reference
        """

        return Reference(self.com_object.ElemToTransform)

    @elem_to_transform.setter
    def elem_to_transform(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.ElemToTransform = value

    @property
    def volume_result(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property VolumeResult() As boolean
                |     Returns or sets the volume result.
                |     Legal values: True if the result of affinity is required as volume (option
                |     is effective only in case of volumes,requires GSO License) and False if it is
                |     needed as surface .
                | 
                |     Example:
                | 
                |          This example sets that the result of
                |          the hybShpAffinity hybrid shape affinity is volume.
                |          
                | 
                |          hybShpAffinity.VolumeResult = True

        :return: bool
        """

        return self.com_object.VolumeResult

    @volume_result.setter
    def volume_result(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.VolumeResult = value

    @property
    def x_ratios(self) -> RealParam:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property XRatios() As RealParam (Read Only)
                |     Returns the affinity ratio along the X Direction of the reference
                |     coordinate system.
                | 
                |     Example:
                |         This example retrieves in X the ratio of the affinity along the X
                |         Direction of the reference coordinate system used by the Affinity hybrid shape
                |         feature.
                | 
                |          Dim X As RealParam 
                |          Set X = Affinity.XRatios

        :return: RealParam
        """

        return RealParam(self.com_object.XRatios)

    @property
    def y_ratios(self) -> RealParam:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property YRatios() As RealParam (Read Only)
                |     Returns the affinity ratio along the Y Direction of the reference
                |     coordinate system.
                | 
                |     Example:
                |         This example retrieves in Y the ratio of the affinity along the Y
                |         Direction of the reference coordinate system used by the Affinity hybrid shape
                |         feature.
                | 
                |          Dim Y As RealParam 
                |          Set Y = Affinity.YRatios

        :return: RealParam
        """

        return RealParam(self.com_object.YRatios)

    @property
    def z_ratios(self) -> RealParam:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property ZRatios() As RealParam (Read Only)
                |     Returns the affinity ratio along the Z Direction of the reference
                |     coordinate system.
                | 
                |     Example:
                |         This example retrieves in Z the ratio of the affinity along the Z
                |         Direction of the reference coordinate system used by the Affinity hybrid shape
                |         feature.
                | 
                |          Dim Z As RealParam 
                |          Set Z = Affinity.ZRatios

        :return: RealParam
        """

        return RealParam(self.com_object.ZRatios)

    def __repr__(self):
        return f'HybridShapeAffinity(name="{ self.name }")'
