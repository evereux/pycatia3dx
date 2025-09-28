"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-27 14:29:47.477239

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.mmr_automation_interfaces.hybrid_shape import HybridShape
from pycatia3dx.mode.reference import Reference


class HybridShapeWrapSurface(HybridShape):

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
                |                         HybridShapeWrapSurface
                | 
                | Represents the hybrid shape wrap surface object.
                | Role: To access the data of the hybrid shape wrap surface
                | object.
                | 
                | This data includes:
                | 
                |     Two definition surfaces (refrence and target), who define the
                |     deformation
                | 
                | Use the CATIAHybridShapeFactory to create a HybridShapeWrapSurface
                | object.
                | 
                | See also:
                |     HybridShapeFactory
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def deformation_mode(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property DeformationMode() As long
                |     Returns or sets whether the wrap surface is or should be created as
                |     a"Normal" or with a "3D" deformation mode.
                |     Legal values: 2 for the normal solution and 1 for 3D
                |     solution.
                | 
                |     Example:
                | 
                |          This example sets the mode to create the wrap surface
                |          hybWrapSurface with a 3D deformation mode.
                |          
                | 
                |          hybWrapSurface.3D deformation mode = 1

        :return: int
        """

        return self.com_object.DeformationMode

    @deformation_mode.setter
    def deformation_mode(self, value: int):
        """
        :param int value:
        """

        self.com_object.DeformationMode = value

    @property
    def reference_surface(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property ReferenceSurface() As Reference
                |     Returns or sets the reference surface of the WrapSurface.
                | 
                |     Example:
                |         This example retrieves in ReferenceSurface the surface to deform of the
                |         ShpWrapSurface hybrid shape WrapSurface feature.
                | 
                |          ReferenceSurface = ShpWrapSurface.Surface

        :return: Reference
        """

        return Reference(self.com_object.ReferenceSurface)

    @reference_surface.setter
    def reference_surface(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.ReferenceSurface = value

    @property
    def surface(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property Surface() As Reference
                |     Returns or sets the reference surface to deform of the
                |     WrapSurface.
                | 
                |     Example:
                |         This example retrieves in SurfaceToDeform the surface to deform of the
                |         ShpWrapSurface hybrid shape WrapSurface feature.
                | 
                |          SurfaceToDeform = ShpWrapSurface.Surface

        :return: Reference
        """

        return Reference(self.com_object.Surface)

    @surface.setter
    def surface(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.Surface = value

    @property
    def target_surface(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property TargetSurface() As Reference
                |     Returns or sets the target surface of the WrapSurface.
                | 
                |     Example:
                |         This example retrieves in TargetSurface the surface to deform of the
                |         ShpWrapSurface hybrid shape WrapSurface feature.
                | 
                |          TargetSurface = ShpWrapSurface.Surface

        :return: Reference
        """

        return Reference(self.com_object.TargetSurface)

    @target_surface.setter
    def target_surface(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.TargetSurface = value

    def __repr__(self):
        return f'HybridShapeWrapSurface(name="{ self.name }")'
