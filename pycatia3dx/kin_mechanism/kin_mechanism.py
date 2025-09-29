"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.kin_mechanism.kin_commands import KinCommands
from pycatia3dx.kin_mechanism.kin_joints import KinJoints
from pycatia3dx.product_structure_client.vpm_occurrence import VPMOccurrence
from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.types.general import CATVariant


class KinMechanism(AnyObject):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     KinMechanism
                | 
                | The interface to access the root feature of the Mechanism
                | Representation.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def commands(self) -> KinCommands:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Commands() As KinCommands (Read Only)
                |     Returns the collection containing the mechanism commands. All the commands
                |     that are defined in the mechanism might be accessed thru that
                |     collection.
                | 
                |     Example:
                |         The following example returns in MyCommands the commands created in
                |         MyMECHRoot :
                | 
                |          Dim MyRepRef as VPMRepReference
                |          Set MyRepRef = ...
                |          Dim disAttr As  String
                |          disAttr = MyRepRef.GetAttributeValue("V_discipline")
                |          If ( attr = "Mechanism" ) Then
                |            Dim MyMECHRoot As KinMechanism
                |            Set MyMECHRoot = MyRepRef.GetItem("MECHRep")
                |            Dim MyCommands As KinCommands
                |            Set MyCommands = MyMECHRoot.Parameters
                |          End If

        :return: KinCommands
        """

        return KinCommands(self.com_object.Commands)

    @property
    def joints(self) -> KinJoints:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Joints() As KinJoints (Read Only)
                |     Returns the collection containing joints in the mechanism. All the joints
                |     that are referenced in the MECH Representation might be accessed thru that
                |     collection.
                | 
                |     Example:
                |         The following example returns in MyJoints the joints referenced in
                |         MyMECHRoot :
                | 
                |          Dim MyRepRef as VPMRepReference
                |          Set MyRepRef = ...
                |          Dim disAttr As  String
                |          disAttr = MyRepRef.GetAttributeValue("V_discipline")
                |          If ( attr = "Mechanism" ) Then
                |            Dim MyMECHRoot As KinMechanism
                |            Set MyMECHRoot = MyRepRef.GetItem("MECHRep")
                |            Dim MyJoints As KinJoints
                |            Set MyJoints = MyMECHRoot.Joints
                |          End If

        :return: KinJoints
        """

        return KinJoints(self.com_object.Joints)

    @property
    def mechanism_products(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property MechanismProducts() As CATSafeArrayVariant (Read
                | Only)
                |     Returns the list of the mechanism products. This list does not contains the
                |     dressup products but only the mechanism products.
                | 
                |     Returns:
                |         The products of the mechanism. Each single product is a VPMOccurrence
                |         
                |     Example:
                |         Identify the list of the mechanism products:
                | 
                |           ...
                |           Dim MyMechRep  As  KinMechanism
                |           Set MyMechRep = MyRepRef.GetItem("MECHRep")
                |           ...
                |           Dim MechProducts
                |           MechProducts = MyRepRef.MechanismProducts
                | 
                |           Dim j As Integer
                |           ' loop to identify each attached product
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

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
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
                |               Dim MyMechanism  As KinMechanism
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
                |               Call MyMechanism.AttachDressupProduct(MechanismPart,
                |               Product22)

        :param VPMOccurrence i_mechanism_product:
        :param VPMOccurrence i_attached_product:
        :return: None
        """
        return self.com_object.AttachDressupProduct(i_mechanism_product.com_object, i_attached_product.com_object)

    def clean_simulation(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Sub CleanSimulation()
                |     Cleans the simulation solver.
                |     Role: To clean the solver.
                | 
                |     Example:
                |         The following example cleans the simulation solver after a
                |         simulation.
                | 
                |          Dim MyRepRef as VPMRepReference
                |          Set MyRepRef = ...
                |          Dim disAttr As  String
                |          disAttr = MyRepRef.GetAttributeValue("V_discipline")
                |          If ( attr = "Mechanism" ) Then
                |            Dim MyMECHRoot As KinMechanism
                |            Set MyMECHRoot = MyRepRef.GetItem("MECHRep")
                |            MyMECHRoot.RunSimulation("OpenDoor",90)
                |            MyMECHRoot.CleanSimulation()
                |          End If

        :return: None
        """
        return self.com_object.CleanSimulation()

    def detach_dressup_product(self, i_attached_product: VPMOccurrence) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
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
                |               Dim MyMechanism  As KinMechanism
                |               ...
                |               Dim OccurrencesList As VPMOccurrences
                |               Set OccurrencesList = myRootOccurrence.Occurrences
                | 
                |               Dim Product22 As VPMOccurrence
                |               Set Product22 = OccurrencesList.GetItem("Product 2.2")  
                | 
                |               ' Detach Product 2.2 from the mechanism
                |               Call MyMechanism.DetachDressupProduct(Product22)

        :param VPMOccurrence i_attached_product:
        :return: None
        """
        return self.com_object.DetachDressupProduct(i_attached_product.com_object)

    def get_dressup_products(self, i_mechanism_product: VPMOccurrence) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
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
                |           Dim MyMechanism  As KinMechanism
                |           ...
                |           Dim OccurrencesList As VPMOccurrences
                |           Set OccurrencesList = myRootOccurrence.Occurrences
                | 
                |           Dim MechanismPart As VPMOccurrence
                |           Set MechanismPart = OccurrencesList.GetItem("Product 1.1")
                |            
                |           Dim ListAttached
                |           ListAttached = MyMechanism.GetDressupProducts(MechanismPart)
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

    def prepare_simulation(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Sub PrepareSimulation()
                |     Prepares the solver to run.
                |     Role: To prepare the mechanism simulation.
                | 
                |     Example:
                |         The following example prepares a simulation for the mechanism
                |         MyMECHRoot :
                | 
                |          Dim MyRepRef as VPMRepReference
                |          Set MyRepRef = ...
                |          Dim disAttr As  String
                |          disAttr = MyRepRef.GetAttributeValue("V_discipline")
                |          If ( attr = "Mechanism" ) Then
                |            Dim MyMECHRoot As KinMechanism
                |            Set MyMECHRoot = MyRepRef.GetItem("MECHRep")
                |            MyMECHRoot.PrepareSimulation()
                |          End If 
                |          
                | 
                | 
                |     Limitation: It is not possible to simulate a macro mechanism using a
                |     mechanism in a sub product. The PrepareSimulation method in such a case fails.

        :return: None
        """
        return self.com_object.PrepareSimulation()

    def run_command(self, i_command: CATVariant, i_value: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Sub RunCommand(CATVariant iCommand,double iValue)
                |     Makes a step of simulation for a mechanism command.
                |     Role: To run the solver for a command.
                | 
                |     Parameters:
                | 
                |         iCommand
                |             The index or the name of the command to run to retrieve from the
                |             collection of commands 
                |         iValue
                |             The targeted value for the simulation (in mm for length and degrees
                |             for angle command)
                | 
                |             Example:
                |                 The following example makes a simulation step for the mechanism
                |                 command"OpenDoor" with 90 degrees as targeted
                |                 value:
                | 
                |                  Dim MyRepRef as VPMRepReference
                |                  Set MyRepRef = ...
                |                  Dim disAttr As  String
                |                  disAttr = MyRepRef.GetAttributeValue("V_discipline")
                |                  If ( attr = "Mechanism" ) Then
                |                    Dim MyMECHRoot As KinMechanism
                |                    Set MyMECHRoot = MyRepRef.GetItem("MECHRep")
                |                    MyMECHRoot.PrepareSimulation()
                |                    MyMECHRoot.RunSimulation("OpenDoor",90)
                |                  End If

        :param CATVariant i_command:
        :param float i_value:
        :return: None
        """
        return self.com_object.RunCommand(i_command, i_value)

    def run_simulation(self, i_cmd_values: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Sub RunSimulation(CATSafeArrayVariant iCmdValues)
                |     Makes a step of simulation for the all mechanism.
                |     Role: To run the solver with given values.
                | 
                |     Parameters:
                | 
                |         iCmdValues
                |             The set of values that command will be taken. (in mm for length and
                |             degrees for angle command)
                | 
                |             Example:
                |                 The following example makes a simulation step for the mechanism
                |                 MyMECHRoot with MyCmdValues as targeted
                |                 values:
                | 
                |                  Dim MyRepRef as VPMRepReference
                |                  Set MyRepRef = ...
                |                  Dim disAttr As  String
                |                  disAttr = MyRepRef.GetAttributeValue("V_discipline")
                |                  If ( attr = "Mechanism" ) Then
                |                    Dim MyMECHRoot As KinMechanism
                |                    Set MyMECHRoot = MyRepRef.GetItem("MECHRep")
                |                    MyMECHRoot.PrepareSimulation()
                |                    Dim MyCmdValues As CATSafeArrayVariant
                |                    MyMECHRoot.RunSimulation(MyCmdValues)*
                |                  End If

        :param tuple i_cmd_values:
        :return: None
        """
        return self.com_object.RunSimulation(i_cmd_values)

    def __repr__(self):
        return f'KinMechanism(name="{self.name}")'
