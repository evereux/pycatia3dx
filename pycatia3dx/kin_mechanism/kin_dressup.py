"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.product_structure_client.vpm_occurrence import VPMOccurrence
from pycatia3dx.system.any_object import AnyObject


class KinDressup(AnyObject):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     KinDressup
                | 
                | The interface to manage the dressup products of the mechanism.
                | Example:
                |     Get the KinDressup object from a KinMechanism object:
                | 
                |       ...
                |       Dim MyMechRep  As  KinMechanism
                |       Set MyMechRep = MyRepRef.GetItem("MECHRep")
                |       ...
                |       Dim Dressup As  KinDressup
                |       Set Dressup = MyMechRep.GetItem("KinDressup")
                |       ...
                |      
                | 
                |     Property Index
                |     MechanismProducts 	Returns the list of the mechanism
                |     products.
                |     Method Index
                |     AttachDressupProduct 	Attaches a product to a given mechanism product thru
                |     a dressup link.
                |     DetachDressupProduct 	Detaches a dressup product previously attached to a
                |     mechanism product.
                |     GetDressupProducts 	Returns the dressup product list attached to a given
                |     mechanism product.
                | 
                |     Properties
                | 
                |     Property MechanismProducts() As CATSafeArrayVariant (Read
                |     Only)
                |         Returns the list of the mechanism products. This list does not contains
                |         the dressup products but only the mechanism products.
                | 
                |         Returns:
                |             The products of the mechanism. Each single product is a
                |             VPMOccurrence 
                |         Example:
                |             Identify the list of the mechanism products:
                | 
                |               ...
                |               Dim MyMechRep  As  KinMechanism
                |               Set MyMechRep = MyRepRef.GetItem("MECHRep")
                |               ...
                |               Dim Dressup As  KinDressup
                |               Set Dressup = MyMechRep.GetItem("KinDressup")
                |               ...
                |               Dim MechProducts
                |               MechProducts = Dressup.MechanismProducts
                | 
                |               Dim j As Integer
                |               ' loop to identify each mechanism products
                |               For j = 0 To UBound(MechProducts)
                |                 Dim Product As VPMOccurrence
                |                 Set Product = MechProducts(j)
                |                 MsgBox " mechanism product : " & Product.Name
                |               Next
                |              
                | 
                | 
                |     Methods
                | 
                |     Sub AttachDressupProduct(VPMOccurrence iMechanismProduct,VPMOccurrence
                |     iAttachedProduct)
                |         Attaches a product to a given mechanism product thru a dressup
                |         link.
                | 
                |         Parameters:
                | 
                |             iMechanismProduct
                |                 A product of the mechanism 
                |             iAttachedProduct
                |                 A product to be attached 
                |             Example:
                |                 The mechanism contains a product named "Product 1.1". "Product
                |                 2.2" is attached to "Product 1.1":
                | 
                |                   ...
                |                   ...
                |                   Dim MyMechRep  As  KinMechanism
                |                   Set MyMechRep = MyRepRef.GetItem("MECHRep")
                |                   ...
                |                   Dim Dressup As  KinDressup
                |                   Set Dressup = MyMechRep.GetItem("KinDressup")
                |                   ...
                |                   Dim OccurrencesList As VPMOccurrences
                |                   Set OccurrencesList = myRootOccurrence.Occurrences
                | 
                |                   Dim MechanismPart As VPMOccurrence
                |                   Set MechanismPart = OccurrencesList.GetItem("Product 1.1")
                | 
                |                   Dim Product22 As VPMOccurrence
                |                   Set Product22 = OccurrencesList.GetItem("Product 2.2")  *
                | 
                |                   ' Attach Product 2.2 to Product 1.1
                |                   Call Dressup.AttachDressupProduct(MechanismPart,
                |                   Product22)
                |                  
                | 
                |     Sub DetachDressupProduct(VPMOccurrence iAttachedProduct)
                |         Detaches a dressup product previously attached to a mechanism
                |         product.
                | 
                |         Parameters:
                | 
                |             iAttachedProduct
                |                 A product to be detached from the mechanism 
                |             Example:
                |                 "Product 2.2" is detached from the
                |                 mechanism.":
                | 
                |                   ...
                |                   Dim MyMechRep  As  KinMechanism
                |                   Set MyMechRep = MyRepRef.GetItem("MECHRep")
                |                   ...
                |                   Dim Dressup As  KinDressup
                |                   Set Dressup = MyMechRep.GetItem("KinDressup")
                |                   ...
                |                   Dim OccurrencesList As VPMOccurrences
                |                   Set OccurrencesList = myRootOccurrence.Occurrences
                | 
                |                   Dim Product22 As VPMOccurrence
                |                   Set Product22 = OccurrencesList.GetItem("Product 2.2")
                | 
                |                   ' Detach Product 2.2 from the mechanism
                |                   Call Dressup.DetachDressupProduct(Product22)
                |                  
                | 
                |     Func GetDressupProducts(VPMOccurrence iMechanismProduct) As
                |     CATSafeArrayVariant
                |         Returns the dressup product list attached to a given mechanism
                |         product.
                | 
                |         Parameters:
                | 
                |             iMechanismProduct
                |                 A product of the mechanism 
                | 
                |         Returns:
                |             The dressup product list as a CATSafeArrayVariant. Each single
                |             product is a VPMOccurrence 
                |         Example:
                |             The mechanism contains a product named "Product 1.1". The following
                |             example returns all the dressup products attached to "Product
                |             1.1":
                | 
                |               ...
                |               Dim MyMechRep  As  KinMechanism
                |               Set MyMechRep = MyRepRef.GetItem("MECHRep")
                |               ...
                |               Dim Dressup As  KinDressup
                |               Set Dressup = MyMechRep.GetItem("KinDressup")
                |               ...
                |               Dim MechanismPart As VPMOccurrence
                |               Set MechanismPart = OccurrencesList.GetItem("Product 1.1")
                |               ...
                |               Dim OccurrencesList As VPMOccurrences
                |               Set OccurrencesList = myRootOccurrence.Occurrences
                | 
                |               Dim MechanismPart As VPMOccurrence
                |               Set MechanismPart = OccurrencesList.GetItem("Product 1.1")
                | 
                |               Dim ListAttached
                |               ListAttached = Dressup.GetDressupProducts(MechanismPart)
                | 
                |               Dim j As Integer
                |               ' loop to identify each attached product
                |               For j = 0 To UBound(ListAttached)
                |                 Dim Product As VPMOccurrence
                |                 Set Product = ListAttached(j)
                |                 MsgBox " Attached product : " & Product.Name
                |               Next
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def mechanism_products(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2026-01-04 12:20:59.068917)
                | Property MechanismProducts() As CATSafeArrayVariant (Read
                | Only)
                |     Returns the list of the mechanism products. This list does not contains the
                |     dressup products but only the mechanism products.
                |
                |     Returns:
                |         The products of the mechanism. Each single product is a
                |         VPMOccurrence
                |     Example:
                |         Identify the list of the mechanism products:
                |
                |           ...
                |           Dim MyMechRep  As  KinMechanism
                |           Set MyMechRep = MyRepRef.GetItem("MECHRep")
                |           ...
                |           Dim Dressup As  KinDressup
                |           Set Dressup = MyMechRep.GetItem("KinDressup")
                |           ...
                |           Dim MechProducts
                |           MechProducts = Dressup.MechanismProducts
                |
                |           Dim j As Integer
                |           ' loop to identify each mechanism products
                |           For j = 0 To UBound(MechProducts)
                |             Dim Product As VPMOccurrence
                |             Set Product = MechProducts(j)
                |             MsgBox " mechanism product : " & Product.Name
                |           Next

        :return: tuple
        """

        return self.com_object.MechanismProducts

    def attach_dressup_product(self, i_mechanism_product: VPMOccurrence, i_attached_product: VPMOccurrence) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2026-01-04 12:20:59.068917)
                | Sub AttachDressupProduct(VPMOccurrence iMechanismProduct,VPMOccurrence
                | iAttachedProduct)
                |     Attaches a product to a given mechanism product thru a dressup
                |     link.
                |
                |     Parameters:
                |
                |         iMechanismProduct
                |             A product of the mechanism
                |         iAttachedProduct
                |             A product to be attached
                |         Example:
                |             The mechanism contains a product named "Product 1.1". "Product 2.2"
                |             is attached to "Product 1.1":
                |
                |               ...
                |               ...
                |               Dim MyMechRep  As  KinMechanism
                |               Set MyMechRep = MyRepRef.GetItem("MECHRep")
                |               ...
                |               Dim Dressup As  KinDressup
                |               Set Dressup = MyMechRep.GetItem("KinDressup")
                |               ...
                |               Dim OccurrencesList As VPMOccurrences
                |               Set OccurrencesList = myRootOccurrence.Occurrences
                |
                |               Dim MechanismPart As VPMOccurrence
                |               Set MechanismPart = OccurrencesList.GetItem("Product 1.1")
                |
                |               Dim Product22 As VPMOccurrence
                |               Set Product22 = OccurrencesList.GetItem("Product 2.2")  *
                |
                |               ' Attach Product 2.2 to Product 1.1
                |               Call Dressup.AttachDressupProduct(MechanismPart,
                |               Product22)

        :param VPMOccurrence i_mechanism_product:
        :param VPMOccurrence i_attached_product:
        :return: None
        """
        return self.com_object.AttachDressupProduct(i_mechanism_product.com_object, i_attached_product.com_object)

    def detach_dressup_product(self, i_attached_product: VPMOccurrence) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2026-01-04 12:20:59.068917)
                | Sub DetachDressupProduct(VPMOccurrence iAttachedProduct)
                |     Detaches a dressup product previously attached to a mechanism
                |     product.
                |
                |     Parameters:
                |
                |         iAttachedProduct
                |             A product to be detached from the mechanism
                |         Example:
                |             "Product 2.2" is detached from the mechanism.":
                |
                |               ...
                |               Dim MyMechRep  As  KinMechanism
                |               Set MyMechRep = MyRepRef.GetItem("MECHRep")
                |               ...
                |               Dim Dressup As  KinDressup
                |               Set Dressup = MyMechRep.GetItem("KinDressup")
                |               ...
                |               Dim OccurrencesList As VPMOccurrences
                |               Set OccurrencesList = myRootOccurrence.Occurrences
                |
                |               Dim Product22 As VPMOccurrence
                |               Set Product22 = OccurrencesList.GetItem("Product 2.2")
                |
                |               ' Detach Product 2.2 from the mechanism
                |               Call Dressup.DetachDressupProduct(Product22)

        :param VPMOccurrence i_attached_product:
        :return: None
        """
        return self.com_object.DetachDressupProduct(i_attached_product.com_object)

    def get_dressup_products(self, i_mechanism_product: VPMOccurrence) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2026-01-04 12:20:59.068917)
                | Func GetDressupProducts(VPMOccurrence iMechanismProduct) As
                | CATSafeArrayVariant
                |     Returns the dressup product list attached to a given mechanism
                |     product.
                |
                |     Parameters:
                |
                |         iMechanismProduct
                |             A product of the mechanism
                |
                |     Returns:
                |         The dressup product list as a CATSafeArrayVariant. Each single product
                |         is a VPMOccurrence
                |     Example:
                |         The mechanism contains a product named "Product 1.1". The following
                |         example returns all the dressup products attached to "Product
                |         1.1":
                |
                |           ...
                |           Dim MyMechRep  As  KinMechanism
                |           Set MyMechRep = MyRepRef.GetItem("MECHRep")
                |           ...
                |           Dim Dressup As  KinDressup
                |           Set Dressup = MyMechRep.GetItem("KinDressup")
                |           ...
                |           Dim MechanismPart As VPMOccurrence
                |           Set MechanismPart = OccurrencesList.GetItem("Product 1.1")
                |           ...
                |           Dim OccurrencesList As VPMOccurrences
                |           Set OccurrencesList = myRootOccurrence.Occurrences
                |
                |           Dim MechanismPart As VPMOccurrence
                |           Set MechanismPart = OccurrencesList.GetItem("Product 1.1")
                |
                |           Dim ListAttached
                |           ListAttached = Dressup.GetDressupProducts(MechanismPart)
                |
                |           Dim j As Integer
                |           ' loop to identify each attached product
                |           For j = 0 To UBound(ListAttached)
                |             Dim Product As VPMOccurrence
                |             Set Product = ListAttached(j)
                |             MsgBox " Attached product : " & Product.Name
                |           Next

        :param VPMOccurrence i_mechanism_product:
        :return: tuple
        """
        return self.com_object.GetDressupProducts(i_mechanism_product.com_object)

    def __repr__(self):
        return f'KinDressup(name="{self.name}")'
