"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.product_structure_client.vpm_reference import VPMReference
from pycatia3dx.system.any_object import AnyObject


class VocSilhouetteService(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     VOCSilhouetteService
                | 
                | Represents the CATIAVOCSilhouetteService.
                | Role: To provide the services to create VOC product:
                | Silhouettes
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def create_a_silhouette(self, i_products_to_treat: tuple, i_product_reference: VPMReference, i_list_of_view_points: tuple, i_silhouette_acc: float, i_accuracy_for_simplification: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub CreateASilhouette(CATSafeArrayVariant iProductsToTreat,VPMReference
                | iProductReference,CATSafeArrayVariant iListOfViewPoints,double
                | iSilhouetteAcc,double iAccuracyForSimplification)
                | 
                |     Deprecated:
                |         R2020x Use CATEVOCServices::ComputeASilhouette
                |         (VOCServices.ComputeASilhouette) Compute a Silhouette.
                |         
                |     Parameters:
                | 
                |         iProductsToTreat
                |             List of Products to take into account 
                |         iProductReference
                |             Reference Product. In this case, volume is computed accordingly.
                |             
                |         iListOfViewPoints
                |             A list of view points 
                |         iSilhouetteAcc
                |             Accuracy for the computation. 
                |         iAccuracyForSimplification
                |             Accuracy for the simplification. 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK:Success
                |         E_FAIL:Failure 

        :param tuple i_products_to_treat:
        :param VPMReference i_product_reference:
        :param tuple i_list_of_view_points:
        :param float i_silhouette_acc:
        :param float i_accuracy_for_simplification:
        :return: None
        """
        return self.com_object.CreateASilhouette(i_products_to_treat, i_product_reference.com_object, i_list_of_view_points, i_silhouette_acc, i_accuracy_for_simplification)

    def __repr__(self):
        return f'VocSilhouetteService(name="{ self.name }")'
