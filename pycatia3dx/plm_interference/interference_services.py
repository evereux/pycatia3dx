"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.interfaces.service import Service
from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.plm_interference.interference_simulation import InterferenceSimulation


class InterferenceServices(Service):

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
                |                         InterferenceServices
                | 
                | Provides services around InterferenceSimulation
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def create_interference_simulation(self, i_reference: AnyObject, o_interference_simulation: InterferenceSimulation) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub CreateInterferenceSimulation(AnyObject iReference,InterferenceSimulation
                | oInterferenceSimulation)
                | 
                |     Deprecated:
                |         R213. use CreateInterferenceSimulation2
                |         Creates an InterferenceSimulation on a reference entity.
                |         
                |     Parameters:
                | 
                |         iReference
                |             The reference entity (for instance a product).
                |             Legal values:
                | 
                |             Valid reference
                |                 The reference is valid for a interference
                |                 checking.
                |             Invalid reference
                |                 The reference is not valid for a interference
                |                 checking.
                | 
                |         oInterferenceSimulation
                |             The created InterferenceSimulation.
                |             Legal values:
                | 
                |             Valid InterferenceSimulation
                |                 The InterferenceSimulation is successfully
                |                 created.
                |             Invalid InterferenceSimulation
                |                 The InterferenceSimulation is not created.
                | 
                |     Example:
                | 
                |            This example creates the oITF1 InterferenceSimulation from the
                |            oRootProduct product.
                |            
                | 
                |            Dim oRootProduct As Product
                |            Set oRootProduct = ...
                |            Dim oITFServices As InterferenceServices
                |            Set oITFServices = CATIA.ActiveEditor.GetService("InterferenceServices")
                |            Dim oITF1 As InterferenceSimulation
                |            oITFServices.CreateInterferenceSimulation(oRootProduct,
                |            oITF1)

        :param AnyObject i_reference:
        :param InterferenceSimulation o_interference_simulation:
        :return: None
        """
        return self.com_object.CreateInterferenceSimulation(i_reference.com_object, o_interference_simulation.com_object)

    def create_interference_simulation2(self, i_reference: AnyObject, i_group_computation_type2: int, o_interference_simulation: InterferenceSimulation) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub CreateInterferenceSimulation2(AnyObject
                | iReference,CatInterferenceGroupComputationType2
                | iGroupComputationType2,InterferenceSimulation
                | oInterferenceSimulation)
                |     Creates an InterferenceSimulation on a reference entity. With this method,
                |     the right number of groups is created in line with the parameter
                |     iGroupComputationType2.
                | 
                |     Parameters:
                | 
                |         iReference
                |             The reference entity of the root product.
                |             Legal values:
                | 
                |             Valid reference
                |                 The reference is valid for a interference
                |                 checking.
                |             Invalid reference
                |                 The reference is not valid for a interference
                |                 checking.
                | 
                |         iGroupComputationType2
                |             The type of computation for group. This parameter influences the
                |             creation of group(s) and the number of them. (see definition of
                |             CATInterferenceGroupComputationType2)
                |             Legal values:
                | 
                |            catInterferenceGroupComputationTypeAllAgainstAllInGroup
                |                 The computation takes into account all the occurrences against
                |                 each other inside groups One group is created.
                |                 
                |            catInterferenceGroupComputationTypeGroupAgainstGroup
                |                 The computation takes into account all the occurrences in a
                |                 group against the others in other group. Two groups are created.
                |                 
                |            catInterferenceGroupComputationTypeGroupAgainstContext
                |                 The computation takes into account all the occurrences of the
                |                 first group against the rest of the context. One group is created.
                |                 
                |            catInterferenceGroupComputationTypeAllAgainstAllInContext
                |                 The computation takes into account all the occurrences against
                |                 each other inside context. No group is created.
                |                 
                | 
                |         oInterferenceSimulation
                |             The created InterferenceSimulation.
                |             Legal values:
                | 
                |             Valid InterferenceSimulation
                |                 The InterferenceSimulation is successfully
                |                 created.
                |             Invalid InterferenceSimulation
                |                 The InterferenceSimulation is not created.
                | 
                |     Example:
                | 
                |            This example creates the oITF1 InterferenceSimulation from the
                |            RootProduct product.
                |            
                | 
                |            Dim RootProduct As VPMRootOccurrence
                |            Set RootProduct = CATIA.ActiveEditor.ActiveObject
                |            
                |            Dim RootProductRef    As VPMReference
                |            Set RootProductRef = RootProduct.ReferenceRootOccurrenceOf
                | 
                |            Dim GroupCmpType As
                |            CatInterferenceGroupComputationType2
                |            GroupCmpType = catInterferenceGroupComputationTypeAllAgainstAllInContext
                |            
                |            Dim oITF1 As InterferenceSimulation
                |            
                |            Dim ITFServices As InterferenceServices
                |            Set ITFServices = CATIA.ActiveEditor.GetService("InterferenceServices")
                | 
                |            ITFServices.CreateInterferenceSimulation RootProductRef,
                |            GroupCmpType, oITF1

        :param AnyObject i_reference:
        :param int i_group_computation_type2:
        :param InterferenceSimulation o_interference_simulation:
        :return: None
        """
        return self.com_object.CreateInterferenceSimulation2(i_reference.com_object, i_group_computation_type2, o_interference_simulation.com_object)

    def __repr__(self):
        return f'InterferenceServices(name="{ self.name }")'
