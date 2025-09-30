"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class ManufacturingMountPoint(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     ManufacturingMountPoint
                | 
                | Interface to manage mount point of tool, tool assembly, holder, insert
                | .
                | ..
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def get_axis_base_point(self, osp_axis_system: AnyObject, o_father_product: AnyObject, i_inside: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetAxisBasePoint(AnyObject ospAxisSystem,AnyObject oFatherProduct,boolean
                | iInside)
                |     Returns the axis which defines the base point of the Tool.
                | 
                |     Parameters:
                | 
                |         ospAxisSystem
                |             : the axis system AxisSystem 
                |         oFatherProduct
                |             : first father product (in general: 3DPart) 
                |         iInside
                |             : to cover the structure (default false)

        :param AnyObject osp_axis_system:
        :param AnyObject o_father_product:
        :param bool i_inside:
        :return: None
        """
        return self.com_object.GetAxisBasePoint(osp_axis_system.com_object, o_father_product.com_object, i_inside)

    def get_axis_machine_mount_point(self, osp_axis_system: AnyObject, o_father_product: AnyObject, i_inside: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetAxisMachineMountPoint(AnyObject ospAxisSystem,AnyObject
                | oFatherProduct,boolean iInside)
                |     Returns the axis which defines the mount point of the Tool
                | 
                |     Parameters:
                | 
                |         ospAxisSystem
                |             : the axis system AxisSystem 
                |         oFatherProduct
                |             : first father product (in general: 3DPart) 
                |         iInside
                |             : to cover the structure (default false)

        :param AnyObject osp_axis_system:
        :param AnyObject o_father_product:
        :param bool i_inside:
        :return: None
        """
        return self.com_object.GetAxisMachineMountPoint(osp_axis_system.com_object, o_father_product.com_object, i_inside)

    def get_base_point(self, i_inside: bool) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetBasePoint(boolean iInside) As CATSafeArrayVariant
                |     Returns the matrix transformation which allows to define the positionning
                |     of the tool assembly
                | 
                |     Parameters:
                | 
                |         oMountTransfo
                |             : the matrix transformation 
                |         iInside
                |             : to cover the structure (Default: False)

        :param bool i_inside:
        :return: tuple
        """
        return self.com_object.GetBasePoint(i_inside)

    def get_machine_mount_point(self, i_inside: bool) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetMachineMountPoint(boolean iInside) As
                | CATSafeArrayVariant
                |     Returns the matrix transformation which allows to define the positionning
                |     of the tool assembly
                | 
                |     Parameters:
                | 
                |         oMountTransfo
                |             : the matrix transformation 
                |         iInside
                |             : to cover the structure (Default: False)

        :param bool i_inside:
        :return: tuple
        """
        return self.com_object.GetMachineMountPoint(i_inside)

    def remove_base_point(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub RemoveBasePoint()
                |     Remove the axis Base Point defined for Tool.
                | 
                |     Parameters:
                | 
                |         iAxis
                |             : the axis

        :return: None
        """
        return self.com_object.RemoveBasePoint()

    def remove_machine_mount_point(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub RemoveMachineMountPoint()
                |     Remove the axis Mount Point defined for Tool.
                | 
                |     Parameters:
                | 
                |         iAxis
                |             : the axis

        :return: None
        """
        return self.com_object.RemoveMachineMountPoint()

    def set_base_point(self, i_axis: AnyObject, i_father_product: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetBasePoint(AnyObject iAxis,AnyObject iFatherProduct)
                |     Set the axis which defines the base point of the Tool.
                | 
                |     Parameters:
                | 
                |         iAxis
                |             : the axis system CATIMf3DAxisSystem 
                |         iFatherProduct
                |             : first father product (in general: 3DPart)

        :param AnyObject i_axis:
        :param AnyObject i_father_product:
        :return: None
        """
        return self.com_object.SetBasePoint(i_axis.com_object, i_father_product.com_object)

    def set_machine_mount_point(self, i_axis: AnyObject, i_father_product: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetMachineMountPoint(AnyObject iAxis,AnyObject
                | iFatherProduct)
                |     Set the matrix transformation which allows to define the positionning of
                |     the tool assembly
                | 
                |     Parameters:
                | 
                |         iAxis
                |             : the 3D axis system CATIMf3DAxisSystem 
                |         iFatherProduct
                |             : first father product (in general: 3DPart)

        :param AnyObject i_axis:
        :param AnyObject i_father_product:
        :return: None
        """
        return self.com_object.SetMachineMountPoint(i_axis.com_object, i_father_product.com_object)

    def __repr__(self):
        return f'ManufacturingMountPoint(name="{ self.name }")'
