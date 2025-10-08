"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.mmr_automation_interfaces.factory import Factory
from pycatia3dx.mode.reference import Reference
from pycatia3dx.structure.sfd_member import SfdMember
from pycatia3dx.structure.sfd_panel import SfdPanel
from pycatia3dx.structure.sfd_sketch_based_panel import SfdSketchBasedPanel
from pycatia3dx.structure.sfd_sketch_based_plate import SfdSketchBasedPlate


class SfdFactory(Factory):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     CATMmrAutomationInterfaces.Factory
                |                         SfdFactory
                | 
                | Object to create Structure Functional Modeler Objects.
                | Role: To create the structure object such as Panel and Member.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def add_member(self, i_destination: Reference) -> SfdMember:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func AddMember(Reference iDestination) As SfdMember
                |     Returns a Member created. For setting further attributes please refer to
                |     StrCategoryMngt, StrMaterialMngt, StrSectionMngt, StrOpenings,
                |     StrProfileLimitMngt.
                |     Role: Creates a Member.
                | 
                |     Parameters:
                | 
                |         iDestination
                |             The feature under which the Profile will be aggregated.
                |             
                | 
                |     Example:
                | 
                | 
                |              This example creates a panel.
                |              
                | 
                |               Dim PartReference As Reference
                |               Set PartReference = ObjPart.CreateReferenceFromObject(ObjPart)
                |               'Get SfdFactory
                |               Dim ObjSfdFactory As SfdFactory
                |               Set ObjSfdFactory = ObjPart.GetCustomerFactory("SfdFactory")
                |               Dim ObjSfdMember As SfdMember
                |               Set ObjSfdMember = ObjSfdFactory.AddMember(PartReference)

        :param Reference i_destination:
        :return: SfdMember
        """
        return SfdMember(self.com_object.AddMember(i_destination.com_object))

    def add_panel(self, i_destination: Reference, i_concave_mode: bool) -> SfdPanel:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func AddPanel(Reference iDestination,boolean iConcaveMode) As
                | SfdPanel
                |     Returns a Panel.created in regular limitmode For setting further attributes
                |     please refer to StrCategoryMngt, StrMaterialMngt, StrSfdPlatesMngt,
                |     StrPanelSurf, StrPanelLimitMngt
                |     Role: Creates a Panel in the regular limit mode (split
                |     mode).
                | 
                |     Parameters:
                | 
                |         iDestination
                |             Panel's destination. 
                |         iConcaveMode
                |             Defines Advanced plate or basic plate. For creation of advanced
                |             plate this should be TRUE. 
                | 
                |     Example:
                | 
                | 
                |              This example creates a panel.
                |              
                | 
                |               Dim PartReference As Reference
                |               Set PartReference = ObjPart.CreateReferenceFromObject(ObjPart)
                |               'Get SfdFactory
                |               Dim ObjSfdFactory As SfdFactory
                |               Set ObjSfdFactory = ObjPart.GetCustomerFactory("SfdFactory")
                |               Dim ObjSfdPanel As SfdPanel
                |               Set ObjSfdPanel = ObjSfdFactory.AddPanel(PartReference, False)

        :param Reference i_destination:
        :param bool i_concave_mode:
        :return: SfdPanel
        """
        return SfdPanel(self.com_object.AddPanel(i_destination.com_object, i_concave_mode))

    def add_sketch_based_panel(self, i_destination: Reference, i_position_mode: int) -> SfdSketchBasedPanel:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func AddSketchBasedPanel(Reference iDestination,short iPositionMode) As
                | SfdSketchBasedPanel
                |     Returns a SketchBasedPanel created. For setting further attributes please
                |     refer to StrCategoryMngt, StrMaterialMngt, StrPanelSurf, StrPlateExtrusionMngt,
                |     StrPanelLimitMngt, StrSfdPlatesMngt StrSketchBasedDMSMngt,
                |     StrOpeningsMgr.
                |     Role: Creates a SketchBasedPanel.
                | 
                |     Parameters:
                | 
                |         iDestination
                |             The feature under which the Sketch Based Panel will be aggregated.
                |             
                |         iPositionMode
                |             The PositionMode define the delimitation is made by which type of
                |             mode
                |             - 3: 3DAxis mode
                |             - 4: Plate/Stiffener mode
                |             - 5: Stiffener / Stiffener mode
                |             - 6: MultiLimits mode 
                | 
                |     Example:
                | 
                | 
                |              This example creates a SketchBasedPanel.
                |              
                | 
                |               Dim PartReference As Reference
                |               Set PartReference = ObjPart.CreateReferenceFromObject(ObjPart)
                |               'Get SfdFactory
                |               Dim ObjSfdFactory As SfdFactory
                |               Set ObjSfdFactory = ObjPart.GetCustomerFactory("SfdFactory")
                |               Dim ObjSfdSketchBasedPanel As
                |               SfdSketchBasedPanel
                |               Set ObjSfdSketchBasedPanel = ObjSfdFactory.AddSketchBasedPanel(PartReference)

        :param Reference i_destination:
        :param int i_position_mode:
        :return: SfdSketchBasedPanel
        """
        return SfdSketchBasedPanel(self.com_object.AddSketchBasedPanel(i_destination.com_object, i_position_mode))

    def add_sketch_based_plate(self, i_destination: Reference, i_position_mode: int) -> SfdSketchBasedPlate:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func AddSketchBasedPlate(Reference iDestination,short iPositionMode) As
                | SfdSketchBasedPlate
                |     Returns a SketchBasedPlate created. For setting further attributes please
                |     refer to StrCategoryMngt, StrMaterialMngt, StrPanelSurf, StrPlateExtrusionMngt,
                |     StrPanelLimitMngt, StrSketchBasedDMSMngt.
                |     Role: Creates a SketchBasedPlate.
                | 
                |     Parameters:
                | 
                |         iDestination
                |             The feature under which the Sketch Based Plate will be aggregated.
                |             
                |         iPositionMode
                |             The PositionMode define the delimitation is made by which type of
                |             mode
                |             - 3: 3DAxis mode
                |             - 4: Plate/Stiffener mode
                |             - 5: Stiffener / Stiffener mode
                |             - 6: MultiLimits mode 
                | 
                |     Example:
                | 
                | 
                |              This example creates a SketchBasedPlate.
                |              
                | 
                |               Dim PartReference As Reference
                |               Set PartReference = ObjPart.CreateReferenceFromObject(ObjPart)
                |               'Get SfdFactory
                |               Dim ObjSfdFactory As SfdFactory
                |               Set ObjSfdFactory = ObjPart.GetCustomerFactory("SfdFactory")
                |               Dim ObjSketchBasedPlate As SketchBasedPlate
                |               Set ObjSketchBasedPlate = ObjSfdFactory.AddSketchBasedPlate(PartReference)

        :param Reference i_destination:
        :param int i_position_mode:
        :return: SfdSketchBasedPlate
        """
        return SfdSketchBasedPlate(self.com_object.AddSketchBasedPlate(i_destination.com_object, i_position_mode))

    def init_resources(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub InitResources()
                |     Loads SFD resources
                | 
                |     Example:
                | 
                | 
                |              This example initializes resources for SFD
                |              system.
                |              
                | 
                |               ObjSfdServices.InitResources

        :return: None
        """
        return self.com_object.InitResources()

    def __repr__(self):
        return f'SfdFactory(name="{self.name}")'
