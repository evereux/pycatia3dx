"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class ManufacturingFeatureFactory(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     ManufacturingFeatureFactory
                | 
                | Interface dedicated to machining features creation.
                | Role: This interface is used to create new machining features.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def create_machining_feature(self, i_type: str) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func CreateMachiningFeature(CATBSTR iType) As AnyObject
                |     Creates a new machining feature.
                | 
                |     Parameters:
                | 
                |         iType
                |             The type of feature (ex: MfgInstructionSet, MfgOffsetPosition)
                |             
                | 
                |     Returns:
                |         The created machining feature

        :param str i_type:
        :return: AnyObject
        """
        return AnyObject(self.com_object.CreateMachiningFeature(i_type))

    def create_mfg_contour(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func CreateMfgContour() As AnyObject
                |     Creates a new Manufacturing continuous contour.
                | 
                |     Parameters:
                | 
                |         oContour
                |             The newly created Manufacturing Contour

        :return: AnyObject
        """
        return AnyObject(self.com_object.CreateMfgContour())

    def list_machining_feature(self, i_filter_type: str) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func ListMachiningFeature(CATBSTR iFilterType) As
                | CATSafeArrayVariant
                |     Gets existing machining features.
                | 
                |     Parameters:
                | 
                |         iFilterType
                |             To filter returned features with a dedicated type 
                | 
                |     Returns:
                |         The list of machining features

        :param str i_filter_type:
        :return: tuple
        """
        return self.com_object.ListMachiningFeature(i_filter_type)

    def __repr__(self):
        return f'ManufacturingFeatureFactory(name="{ self.name }")'
