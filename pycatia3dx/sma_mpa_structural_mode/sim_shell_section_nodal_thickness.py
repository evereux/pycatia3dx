"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.system.cat_base_dispatch import CATBaseDispatch


class SimShellSectionNodalThickness(CATBaseDispatch):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 SimShellSectionNodalThickness
                | 
                | Represents the shell section nodal thickness.
                | Role:This object can be retrieved on an existing shell section. You can use
                | this object to set thickness mapping to nodes.
                | Example:
                | 
                |  Given a shell section object, you can get this object and set thicknes mapping
                |  to Nodes.
                |  
                | 
                |  Dim oShellSectionNodalThickness As
                |  SimShellSectionNodalThickness
                |  Set oShellSectionNodalThickness = oShellSection.GetItem("SimShellSectionNodalThickness")
                |  oShellSectionNodalThickness.MapThicknessToNodesFlag = True
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def map_thickness_to_nodes_flag(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property MapThicknessToNodesFlag() As boolean
                |     Returns or sets the flag that determines if the thickness is to be mapped
                |     to nodes or elements (default).
                |     TRUE: the thickness mapped to nodes.
                | 
                |     FALSE: the thickness mapped to elements.

        :return: bool
        """

        return self.com_object.MapThicknessToNodesFlag

    @map_thickness_to_nodes_flag.setter
    def map_thickness_to_nodes_flag(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.MapThicknessToNodesFlag = value

    @property
    def nodal_thickness_map_flag(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property NodalThicknessMapFlag() As boolean
                |     deprecated R426. Please use MapThicknessToNodesFlag method

        :return: bool
        """

        return self.com_object.NodalThicknessMapFlag

    @nodal_thickness_map_flag.setter
    def nodal_thickness_map_flag(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.NodalThicknessMapFlag = value

    def __repr__(self):
        return f'SimShellSectionNodalThickness()'
