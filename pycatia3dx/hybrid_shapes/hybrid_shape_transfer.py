"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-27 14:29:47.477239

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.mmr_automation_interfaces.hybrid_shape import HybridShape
from pycatia3dx.mode.reference import Reference


class HybridShapeTransfer(HybridShape):

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
                |                         HybridShapeTransfer
                | 
                | Represents the hybrid shape Transfer feature object.
                | Role: To access the data of the hybrid shape Transfer feature object. This data
                | includes:
                | 
                |     The element to transfer
                |     The surface to unfold
                |     The unfolded surface
                | 
                | Use the CATIAHybridShapeFactory to create a HybridShapeTransfer
                | object.
                | 
                | See also:
                |     HybridShapeFactory
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def element_to_transfer(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property ElementToTransfer() As Reference
                |     Returns or sets the element to transfer.

        :return: Reference
        """

        return Reference(self.com_object.ElementToTransfer)

    @element_to_transfer.setter
    def element_to_transfer(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.ElementToTransfer = value

    @property
    def surface_to_unfold(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property SurfaceToUnfold() As Reference
                |     Returns or sets the surface to unfold.

        :return: Reference
        """

        return Reference(self.com_object.SurfaceToUnfold)

    @surface_to_unfold.setter
    def surface_to_unfold(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.SurfaceToUnfold = value

    @property
    def type_of_transfer(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property TypeOfTransfer() As long
                |     Returns or sets the type of transfer.
                | 
                |         0= The type of surface is not defined
                |         1= The type of transfer is folded to unfolded
                |         2= The type of surface is unfolded to folded

        :return: int
        """

        return self.com_object.TypeOfTransfer

    @type_of_transfer.setter
    def type_of_transfer(self, value: int):
        """
        :param int value:
        """

        self.com_object.TypeOfTransfer = value

    @property
    def unfold_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property UnfoldType() As long
                |     Returns or sets the type of unfold to take into account during
                |     transfer.
                | 
                |         0= The type is undefined
                |         1= The surface to unfold is ruled,
                |         2= the surface to unfold is all

        :return: int
        """

        return self.com_object.UnfoldType

    @unfold_type.setter
    def unfold_type(self, value: int):
        """
        :param int value:
        """

        self.com_object.UnfoldType = value

    @property
    def unfolded_surface(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property UnfoldedSurface() As Reference
                |     Returns or sets the unfolded surface.

        :return: Reference
        """

        return Reference(self.com_object.UnfoldedSurface)

    @unfolded_surface.setter
    def unfolded_surface(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.UnfoldedSurface = value

    def __repr__(self):
        return f'HybridShapeTransfer(name="{ self.name }")'
