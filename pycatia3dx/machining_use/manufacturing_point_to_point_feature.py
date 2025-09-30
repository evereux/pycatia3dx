"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class ManufacturingPointToPointFeature(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     ManufacturingPointToPointFeature
                | 
                | Interface representing Point to Point Feature.
                | Role: This interface offers services to manage Point to Point
                | Feature.
                | ManufacturingActivity activity = .... ManufacturingPointToPointFeature
                | ptToPtFeature = activity.GetFeature() as ManufacturingPointToPointFeature;
                | ptToPtFeature.AddPositionPoint(0, 0, 0, 0, 0);
                | ptToPtFeature.AddPositionPoint(10, 10, 10, 1, 0);
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def add_position(self, i_position_to_add: AnyObject, i_position: int, i_product: AnyObject, i_current_site_rank: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub AddPosition(AnyObject iPositionToAdd,long iPosition,AnyObject iProduct,long
                | iCurrentSiteRank)
                |     Insertion/Ajout de Motion point géométrique (Goto)
                | 
                |     Parameters:
                | 
                |         iPositionToAdd
                |             Geometry to add 
                |         iPosition
                |             Position (default: 0) 
                |         iProduct
                |             Product (default: null) 
                |         iCurrentSiteRank
                |             Current site rank (default: 0)

        :param AnyObject i_position_to_add:
        :param int i_position:
        :param AnyObject i_product:
        :param int i_current_site_rank:
        :return: None
        """
        return self.com_object.AddPosition(i_position_to_add.com_object, i_position, i_product.com_object, i_current_site_rank)

    def add_position_point(self, x: float, y: float, z: float, i_position: int, i_current_site_rank: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub AddPositionPoint(double x,double y,double z,long iPosition,long
                | iCurrentSiteRank)
                |     Insertion/Ajout de Motion point (Goto)
                | 
                |     Parameters:
                | 
                |         iPositionToAdd
                |             Point to add 
                |         iPosition
                |             Position (default: 0) 
                |         iCurrentSiteRank
                |             Current site rank (default: 0)

        :param float x:
        :param float y:
        :param float z:
        :param int i_position:
        :param int i_current_site_rank:
        :return: None
        """
        return self.com_object.AddPositionPoint(x, y, z, i_position, i_current_site_rank)

    def get_computed_position(self, index: int) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetComputedPosition(long Index) As CATSafeArrayVariant
                |     Retrieves the computed Point position of the @Index'th Sequential motion
                |     under the MO.
                | 
                |     Parameters:
                | 
                |         Index
                |             Index of Sequential motion under the MO. 
                |         oCoordinates
                |             Computed Point Coordinates. 
                | 
                |     Returns:
                |         Return code.
                |         Legal values:
                | 
                |             S_OK: the List is defined
                |             E_FAIL: otherwise

        :param int index:
        :return: tuple
        """
        return self.com_object.GetComputedPosition(index)

    def __repr__(self):
        return f'ManufacturingPointToPointFeature(name="{ self.name }")'
