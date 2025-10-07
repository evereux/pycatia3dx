"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.mode.reference import Reference
from pycatia3dx.system.collection import Collection
from pycatia3dx.tps.user_surface import UserSurface
from pycatia3dx.types.general import CATVariant


class UserSurfaces(Collection):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     UserSurfaces

    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def generate(self, i_support: Reference) -> UserSurface:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Generate(Reference iSupport) As UserSurface
                |     Use this method in a Part. Creates a new user surface and adds it to the
                |     Surfaces collection.
                | 
                |     Parameters:
                | 
                |         iSupport
                |             The first reference that will support the user surface The
                |             following Boundary object is supported:
                |             Face , PlanarFace , CylindricalFace
                |             Edge , TriDimFeatEdge , RectilinearTriDimFeatEdge , BiDimFeatEdge ,
                |             RectilinearBiDimFeatEdge , MonoDimFeatEdge ,
                |             RectilinearMonoDimFeatEdge
                |             Vertex , TriDimFeatVertexOrBiDimFeatVertex ,
                |             NotWireBoundaryMonoDimFeatVertex,
                |             ZeroDimFeatVertexOrWireBoundaryMonoDimFeatVertex
                | 
                |     Returns:
                |         The created user surface 
                |     Example:
                |         The following example creates a user surface names NewUserSurf from the
                |         reference Ref in the Surfaces collection of the rootPart part in the active 3D
                |         Shape representation.
                | 
                |          Dim rootPart as CATIAPart
                |          Set rootPart = CATIA.ActiveEditor.ActiveObject
                |          Set NewUserSurf = rootPart.UserSurfaces.Add(Ref)

        :param Reference i_support:
        :return: UserSurface
        """
        return UserSurface(self.com_object.Generate(i_support.com_object))

    def item(self, i_index: CATVariant) -> UserSurface:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Item(CATVariant iIndex) As UserSurface
                |     Find a user surface inside the collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The position of the users surface in the collection
                |             
                | 
                |     Returns:
                |         The user surface that is in the iIndex position in the collection

        :param CATVariant i_index:
        :return: UserSurface
        """
        return UserSurface(self.com_object.Item(i_index))

    def make_user_surface_node(self, i_first_user_surf: UserSurface, i_second_user_surf: UserSurface) -> UserSurface:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func MakeUserSurfaceNode(UserSurface iFirstUserSurf,UserSurface
                | iSecondUserSurf) As UserSurface
                |     Usefull to create a User Surface Node from two others User Surface. Creates
                |     a new user surface and adds it to the Surfaces collection.
                | 
                |     Parameters:
                | 
                |         iFirstUserSurf
                |             The first User Surface to use. 
                |         iSecondUserSurf
                |             The second User Surface to use. 
                | 
                |     Returns:
                |         The created user surface

        :param UserSurface i_first_user_surf:
        :param UserSurface i_second_user_surf:
        :return: UserSurface
        """
        return UserSurface(self.com_object.MakeUserSurfaceNode(i_first_user_surf.com_object, i_second_user_surf.com_object))

    def make_user_surface_node2(self, i_list_of_user_surfaces: tuple) -> UserSurface:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func MakeUserSurfaceNode2(CATSafeArrayVariant iListOfUserSurfaces) As
                | UserSurface
                |     Usefull to create a User Surface Node from a list of User Surfaces. Creates
                |     a new user surface and adds it to the Surfaces collection.
                | 
                |     Parameters:
                | 
                |         iListOfUserSurfaces
                |             The list User Surfaces to use. 
                | 
                |     Returns:
                |         The created user surface 

        :param tuple i_list_of_user_surfaces:
        :return: UserSurface
        """
        return UserSurface(self.com_object.MakeUserSurfaceNode2(i_list_of_user_surfaces))

    def __repr__(self):
        return f'UserSurfaces(name="{ self.name }")'
