"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.interfaces.service import Service
from pycatia3dx.mode.reference import Reference
from pycatia3dx.system.any_object import AnyObject


class StrService(Service):

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
                |                         StrService
                | 
                | Object services related to import and retrieval of real structure objects from
                | its reference.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def convert_reference_to_object(self, i_reference: Reference) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func ConvertReferenceToObject(Reference iReference) As
                | AnyObject
                |     Returns the actual structure object from its corresponding
                |     reference.
                | 
                |     Parameters:
                | 
                |         iReference
                |             The reference of structure object. 
                |         oBase
                |             The real structure object. 
                | 
                |     Example:
                | 
                | 
                |              This example retrieves the plate object on which flange is
                |              present.
                |              
                | 
                |              Dim RefSfdPlate As Reference
                |              Set RefSfdPlate = ObjStrFlange.OperatedPlate
                |              Dim ObjBase As AnyObject
                |              Set ObjBase = ObjStrService.ConvertReferenceToObject(RefSfdPlate)

        :param Reference i_reference:
        :return: AnyObject
        """
        return AnyObject(self.com_object.ConvertReferenceToObject(i_reference.com_object))

    def import_(self, i_usage: str, i_source_prod_occ: AnyObject, i_source_feature: AnyObject, i_target_prod_occ: AnyObject, i_target_feature: AnyObject, i_link_mode: int) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Import(CATBSTR iUsage,CATBaseDispatch iSourceProdOcc,CATBaseDispatch
                | iSourceFeature,CATBaseDispatch iTargetProdOcc,CATBaseDispatch
                | iTargetFeature,long iLinkMode) As CATBaseDispatch
                |     Returns the result of Import of feature (source) into another document
                |     (target). The possibilities are:
                | 
                |     Parameters:
                | 
                |         iUsage
                |             Usage. 
                |         iSourceProdOcc
                |             The product occurrence of the source feature. Optional.
                |             
                |         iSourceFeat
                |             Source feature to import. 
                |         iTargetProdOcc
                |             The product occurrence of the target parent object. Optional.
                |             
                |         iTargetFeature
                |             The parent object (part, body or set) under which to aggregate the
                |             import feature. 
                |         iLinkMode
                |             0: use settings, 1: no link, 2: with link. 

        :param str i_usage:
        :param AnyObject i_source_prod_occ:
        :param AnyObject i_source_feature:
        :param AnyObject i_target_prod_occ:
        :param AnyObject i_target_feature:
        :param int i_link_mode:
        :return: AnyObject
        """
        return self.com_object.Import(i_usage, i_source_prod_occ.com_object, i_source_feature.com_object, i_target_prod_occ.com_object, i_target_feature.com_object, i_link_mode)

    def __repr__(self):
        return f'StrService(name="{ self.name }")'
