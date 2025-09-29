"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.fmt_mode.sim_mesh_part import SimMeshPart
from pycatia3dx.system.cat_base_dispatch import CATBaseDispatch


class SimFemFeatureInitialization(CATBaseDispatch):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 SimFemFeatureInitialization
                | 
                | Interface representing FEM feature initialization services.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def initialize_mesh_part_from_geometry(self, i_mesh_part: SimMeshPart) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub InitializeMeshPartFromGeometry(SimMeshPart iMeshPart)
                |     Initialize Mesh Size and Sag from the mesh part support geometry. A mesh
                |     part support must be already defined.

        :param SimMeshPart i_mesh_part:
        :return: None
        """
        return self.com_object.InitializeMeshPartFromGeometry(i_mesh_part.com_object)

    def __repr__(self):
        return f'SimFemFeatureInitialization(name="{self.name}")'
