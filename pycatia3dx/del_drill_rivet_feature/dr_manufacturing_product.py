"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class DrManufacturingProduct(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     DrManufacturingProduct
                | 
                | Represents an object that is Manufacturing product Role: To create Mfg
                | fasteners and DR patterns
                | 
                | See also:
                |     DrManufacturingProduct
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def create_drilling_riveting_pattern(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Func CreateDrillingRivetingPattern() As AnyObject
                |     Creates a drilling & riveting pattern.
                | 
                |     Parameters:
                | 
                |         oDrMfgPattern
                |             The newly created pattern.

        :return: AnyObject
        """
        return AnyObject(self.com_object.CreateDrillingRivetingPattern())

    def create_manufacturing_fastener(self, i_origin_x: float, i_origin_y: float, i_origin_z: float, i_normal_axis_x: float, i_normal_axis_y: float, i_normal_axis_z: float, i_lateral_axis_x: float, i_lateral_axis_y: float, i_lateral_axis_z: float, i_reference: str, ih_geometry: AnyObject, ih_product: AnyObject) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Func CreateManufacturingFastener(double iOriginX,double iOriginY,double
                | iOriginZ,double iNormalAxisX,double iNormalAxisY,double iNormalAxisZ,double
                | iLateralAxisX,double iLateralAxisY,double iLateralAxisZ,CATBSTR
                | iReference,AnyObject ihGeometry,AnyObject ihProduct) As
                | AnyObject
                |     Creates a manufacturing fastener.
                | 
                |     Parameters:
                | 
                |         ohMfgFastener
                |             The newly created manufacturing fastener. 
                |         iOriginX
                |             X Coordinate of local origin. 
                |         iOriginY
                |             Y Coordinate of local origin. 
                |         iOriginZ
                |             Z Coordinate of local origin. 
                |         iNormalAxisX
                |             X Coordinate of local Z direction. 
                |         iNormalAxisY
                |             Y Coordinate of local Z direction. 
                |         iNormalAxisZ
                |             Z Coordinate of local Z direction. 
                |         iLateralAxisX
                |             X Coordinate of local X direction. 
                |         iLateralAxisY
                |             Y Coordinate of local X direction. 
                |         iLateralAxisZ
                |             Z Coordinate of local X direction. 
                |         iReference
                |             Reference name of fastener. 
                |         ihGeometry
                |             Geometry pointed by the fastener. It can be a design point or a PLM
                |             fastener object. 
                |         ihProduct
                |             Product containing the geometry. May be NULL in case of PLM
                |             fastener object.

        :param float i_origin_x:
        :param float i_origin_y:
        :param float i_origin_z:
        :param float i_normal_axis_x:
        :param float i_normal_axis_y:
        :param float i_normal_axis_z:
        :param float i_lateral_axis_x:
        :param float i_lateral_axis_y:
        :param float i_lateral_axis_z:
        :param str i_reference:
        :param AnyObject ih_geometry:
        :param AnyObject ih_product:
        :return: AnyObject
        """
        return AnyObject(self.com_object.CreateManufacturingFastener(i_origin_x, i_origin_y, i_origin_z, i_normal_axis_x, i_normal_axis_y, i_normal_axis_z, i_lateral_axis_x, i_lateral_axis_y, i_lateral_axis_z, i_reference, ih_geometry.com_object, ih_product.com_object))

    def get_manufacturing_features(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Func GetManufacturingFeatures() As CATSafeArrayVariant
                |     Get the Manufacturing features i.e. DrillingRiveting patterns and
                |     unassigned Manufacturing fasteners.
                | 
                |     Parameters:
                | 
                |         oList
                |             List of DrillingRiveting patterns and unassigned Manufacturing
                |             fasteners 

        :return: tuple
        """
        return self.com_object.GetManufacturingFeatures()

    def __repr__(self):
        return f'DrManufacturingProduct(name="{ self.name }")'
