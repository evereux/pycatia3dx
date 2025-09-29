"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.fmt_mode.sim_mesh_specification import SimMeshSpecification
from pycatia3dx.fmt_mode.sim_mesh_topology import SimMeshTopology
from pycatia3dx.fmt_mode.sim_topology_specification import SimTopologySpecification
from pycatia3dx.system.cat_base_dispatch import CATBaseDispatch


class SimMeshServices(CATBaseDispatch):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 SimMeshServices
                | 
                | Interface containing services related to mesh model.
                | 
                | OpenMesher() and CloseMesher() must be called with
                | SimMeshServicesVariable.OpenMesher() / SimMeshServicesVariable.CloseMesher() as
                | in samples below to avoid any issue, e.g. during an Update
                | 
                | Example:
                | 
                |      This example shows how to retrieve the mesh topology and add it as support
                |      of the created local mesh specification:
                |      
                | 
                |      Dim MeshServices1 As SimMeshServices
                |      Set MeshServices1 = MP1.GetItem("SimMeshServices") 'With MP1 as a SimMeshPart
                |      MeshServices1.OpenMesher() 'It opens the mesher of MP1
                |      Dim MeshTopo1 As SimMeshTopology
                |      Set MeshTopo1 = MeshServices1.GetNearestTopology(0#, 0#, 0#, 2, 0#)
                |      Dim MeshSpec1 As SimMeshSpecification
                |      Set MeshSpec1 = MP1.GetMeshSpecifications.Add("CATFmtStudioMappedSpec")
                |      Call MeshServices1.AddTopologyAsSupport(MeshSpec1,
                |      MeshTopo1)
                |      MeshServices1.CloseMesher() 'It closes the mesher of MP1, MeshTopo1 is now
                |      unavailable
                |
                | Example:
                | 
                |      This example shows how to retrieve the mesh topology from an existing
                |      local topology specification:
                |
                |      Dim MeshServices1 As SimMeshServices
                |      Set MeshServices1 = MP1.GetItem("SimMeshServices") 'With MP1 as a SimMeshPart
                |      MeshServices1.OpenMesher() 'It opens the mesher of MP1
                |      Dim LocalMshSpec1 As SimTopologySpecification
                |      Set LocalMshSpec1 = MP1.GetTopologySpecifications.Item(1)
                |      Dim MeshTopo1()
                |      MeshTopo1 = MeshServices1.GetTopology(LocalMshSpec1)
                |      MeshServices1.CloseMesher() 'It closes the mesher of MP1, MeshTopo1 is now
                |      unavailable
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def add_topology_as_support(self, i_local_mesh_spec: SimMeshSpecification, i_topo: SimMeshTopology) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub AddTopologyAsSupport(SimMeshSpecification iLocalMeshSpec,SimMeshTopology
                | iTopo)
                |     Add the mesh topology as support of the local mesh
                |     specification.
                | 
                |     Parameters:
                | 
                |         iLocalMeshSpec
                |             The local mesh specification. 
                |         iTopo
                |             The mesh topology.

        :param SimMeshSpecification i_local_mesh_spec:
        :param SimMeshTopology i_topo:
        :return: None
        """
        return self.com_object.AddTopologyAsSupport(i_local_mesh_spec.com_object, i_topo.com_object)

    def close_mesher(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub CloseMesher()
                |     Closes the mesher. Use this method after use of this service to properly
                |     close the mesher. If not the model could be erroneous, e.g. with an Update
                |     call.

        :return: None
        """
        return self.com_object.CloseMesher()

    def get_nearest_topology(self, i_x: float, i_y: float, i_z: float, i_dimension: int,
                             i_tolerance: float) -> SimMeshTopology:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetNearestTopology(double iX,double iY,double iZ,long iDimension,double
                | iTolerance) As SimMeshTopology
                |     Returns the mesh topology (domain / edge / vertex) the closest to a given
                |     point.
                | 
                |     Parameters:
                | 
                |         iX,
                |             iY, iZ Coordinates of the point in the local coordinate system of
                |             the FEMRep. 
                |         iDimension
                |             Dimension of the topology to get (from 0 to 2). 
                |         iTolerance
                |             Maximum distance allowed for the search in millimeters. If the
                |             value is set to 0, no limit will be applied. 
                | 
                |     Returns:
                |         The closest mesh topology (domain / edge / vertex) with respect to the
                |         input point. Can be empty if no mesh exist. Return at least one mesh topology
                |         if two or more are equidistant from the input point.
                |         The topology will be generated if it has not already been computed.

        :param float i_x:
        :param float i_y:
        :param float i_z:
        :param int i_dimension:
        :param float i_tolerance:
        :return: SimMeshTopology
        """
        return SimMeshTopology(self.com_object.GetNearestTopology(i_x, i_y, i_z, i_dimension, i_tolerance))

    def get_topology(self, i_local_spec: SimTopologySpecification) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetTopology(SimTopologySpecification iLocalSpec) As
                | CATSafeArrayVariant
                |     Returns the mesh topology (domain / edge / vertex) created behind a local
                |     topology specification.
                | 
                |     Parameters:
                | 
                |         iLocalSpec
                |             Local topology specification (Imposed curve / point...)
                |             
                | 
                |     Returns:
                |         The mesh topologies.

        :param SimTopologySpecification i_local_spec:
        :return: tuple
        """
        return self.com_object.GetTopology(i_local_spec.com_object)

    def open_mesher(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub OpenMesher()
                |     Opens the mesher. Use this method before any other call to this service. It
                |     is mandatory to use the CloseMesher after use.

        :return: None
        """
        return self.com_object.OpenMesher()

    def __repr__(self):
        return f'SimMeshServices()'
