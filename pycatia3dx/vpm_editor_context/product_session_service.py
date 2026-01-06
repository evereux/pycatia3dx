"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2026-01-04 12:20:59.068917

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.interfaces.service import Service
from pycatia3dx.product_structure_client.shape_3ds import Shape3Ds
from pycatia3dx.product_structure_client.vpm_root_occurrence import VPMRootOccurrence


class ProductSessionService(Service):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2026-01-04 12:20:59.068917)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     InfInterfaces.Service
                |                         ProductSessionService
                | 
                | Interface representing the session service related to Product
                | data.
                | This interface is to be used as service to :
                | 
                |     get the session CATIAShape3Ds collection object.
                |     compare Root Occurrences.
                | 
                | Example of how to retrieve such an object using
                | Application.GetSessionService:
                | 
                |  Dim aProductModelerSrv as ProductSessionService
                |  Set aProductModelerSrv = CATIA.GetSessionService("ProductSessionService")
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def shape3_ds(self) -> Shape3Ds:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2026-01-04 12:20:59.068917)
                | Property Shape3Ds() As Shape3Ds (Read Only)
                |     Returns the CATIAShape3Ds collection of CATIAShape3D objects available in
                |     session.

        :return: Shape3Ds
        """

        return Shape3Ds(self.com_object.Shape3Ds)

    def compare_root_occurrences(self, i_first_root_occurrence: VPMRootOccurrence,
                                 i_second_root_occurrence: VPMRootOccurrence) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2026-01-04 12:20:59.068917))
                | Func CompareRootOccurrences(VPMRootOccurrence
                | iFirstRootOccurrence,VPMRootOccurrence iSecondRootOccurrence) As
                | CatCompareOccurrenceResult
                |     Compare two Root Occurrences.
                | 
                |     Parameters:
                | 
                |         iFirstRootOccurrence
                |             one of the two Root Occurrences to be compared. 
                |         iSecondRootOccurrence
                |             the other Root Occurrences to be compared. 
                | 
                |     Returns:
                |         The CatCompareOccurrenceResult as result of the comparison operation.

        :param VPMRootOccurrence i_first_root_occurrence:
        :param VPMRootOccurrence i_second_root_occurrence:
        :return: int
        """
        return self.com_object.CompareRootOccurrences(
            i_first_root_occurrence.com_object,
            i_second_root_occurrence.com_object
        )

    def __repr__(self):
        return f'ProductSessionService(name="{self.name}")'
