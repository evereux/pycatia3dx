"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.interfaces.service import Service
from pycatia3dx.mmr_automation_interfaces.part import Part
from pycatia3dx.mode.reference import Reference
from pycatia3dx.srs.rfg_grid_face import RfgGridFace
from pycatia3dx.types.general import CATVariant


class RfgService(Service):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     InfInterfaces.Service
                |                         RfgService
                | 
                | Service related to reference planes and Ref surface
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def create_project_data(self, i_active_rep_part: Part) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub CreateProjectData(Part iActiveRepPart)
                |     creates ProjectData
                | 
                |     Parameters:
                | 
                |         iActiveRepPart
                |             part where ProjectData will be created.

        :param Part i_active_rep_part:
        :return: None
        """
        return self.com_object.CreateProjectData(i_active_rep_part.com_object)

    def create_ref_surface_feature(self, i_part: Reference, i_project_data: Reference) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub CreateRefSurfaceFeature(Reference iPart,Reference
                | iProjectData)
                |     creates a Reference Surface (like Hull)
                | 
                |     Parameters:
                | 
                |         iPart
                |             part where reference surface feature will be created.
                |             
                |         iProjectData
                |             openbody in the part where reference surface feature will be
                |             created.

        :param Reference i_part:
        :param Reference i_project_data:
        :return: None
        """
        return self.com_object.CreateRefSurfaceFeature(i_part.com_object, i_project_data.com_object)

    def get_reference_plane(self, i_part: Part, i_plane_system_index: CATVariant, i_plane_index: CATVariant) -> RfgGridFace:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetReferencePlane(Part iPart,CATVariant iPlaneSystemIndex,CATVariant
                | iPlaneIndex) As RfgGridFace
                |     Returns a reference plane in the specific PlaneSystems.
                | 
                |     Parameters:
                | 
                |         iPart
                |             Parent part of the plane. 
                |         iPlaneSystemIndex
                |             Represents the plane system.
                |             1 : DECK
                |             2 : CROSS
                |             3 : LONG 
                |         iPlaneIndex
                |             part where ProjectData will be created. 
                | 
                |     Example:
                | 
                | 
                |              This example retrieves in RefPlane the reference planes contained
                |              into the 1st PlaneSystem,
                |              and which has CROSS.12 as a name.
                |              
                | 
                |              Dim ObjRfgService As RfgService
                |              Set ObjRfgService = CATIA.ActiveEditor.GetService("RfgService")
                |              Dim RefPlane As RfgGridFace
                |              Set RefPlane = ObjRfgService.GetReferencePlane ObjPart, 2, "CROSS.12"

        :param Part i_part:
        :param CATVariant i_plane_system_index:
        :param CATVariant i_plane_index:
        :return: RfgGridFace
        """
        return RfgGridFace(self.com_object.GetReferencePlane(i_part.com_object, i_plane_system_index, i_plane_index))

    def synchronize_planes(self, i_part: Part) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SynchronizePlanes(Part iPart)
                |     Synchronize the local reference planes to the external plane
                |     definition.
                | 
                |     Parameters:
                | 
                |         iPart
                |             This part's reference planes will be synchronized.

        :param Part i_part:
        :return: None
        """
        return self.com_object.SynchronizePlanes(i_part.com_object)

    def synchronize_ref_surface(self, i_part: Part) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SynchronizeRefSurface(Part iPart)
                |     Synchronize the import of the reference surface with the external reference
                |     surface definition.
                | 
                |     Parameters:
                | 
                |         iPart
                |             This part's reference Surface will be synchronized.

        :param Part i_part:
        :return: None
        """
        return self.com_object.SynchronizeRefSurface(i_part.com_object)

    def __repr__(self):
        return f'RfgService(name="{ self.name }")'
