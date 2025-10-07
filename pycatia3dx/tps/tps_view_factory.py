"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.mode.reference import Reference
from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.tps.tps_view import TPSView
from pycatia3dx.types.general import CATVariant


class TPSViewFactory(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     TPSViewFactory
                | 
                | Interface for the TPS Factory.
                | This factory is implemented on the Set object. All the created views are added
                | to the Set from which this interface is retrieved.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def create_view(self, i_plane: Reference, i_view_type: CATVariant) -> TPSView:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func CreateView(Reference iPlane,CATVariant iViewType) As
                | TPSView
                | 
                |     Parameters:
                | 
                |         iPlane
                |             The surface needed to construct the View. The following Boundary
                |             object is supported: PlanarFace. 
                |         iViewType
                |             1 : Front View. 2 : Section View. 3 : Cut View. 

        :param Reference i_plane:
        :param CATVariant i_view_type:
        :return: TPSView
        """
        return TPSView(self.com_object.CreateView(i_plane.com_object, i_view_type))

    def __repr__(self):
        return f'TpsViewFactory(name="{ self.name }")'
