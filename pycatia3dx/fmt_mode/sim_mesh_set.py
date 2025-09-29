"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.fmt_mode.sim_mesh_parts import SimMeshParts
from pycatia3dx.system.any_object import AnyObject


class SimMeshSet(AnyObject):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimMeshSet
                | 
                | Represents a Mesh Set.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def mesh_parts(self) -> SimMeshParts:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property MeshParts() As SimMeshParts (Read Only)
                |     Returns the Mesh Part collection from the current Mesh Set.

        :return: SimMeshParts
        """

        return SimMeshParts(self.com_object.MeshParts)

    def update(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub Update()
                |     Launches the update of all the Mesh Parts contained by the Mesh Set.

        :return: None
        """
        return self.com_object.Update()

    def __repr__(self):
        return f'SimMeshSet(name="{self.name}")'
