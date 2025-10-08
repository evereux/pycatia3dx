"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.mmr_automation_interfaces.factory import Factory
from pycatia3dx.structure.sdd_product_bracket import SddProductBracket
from pycatia3dx.structure.sdd_product_member import SddProductMember
from pycatia3dx.structure.sdd_product_plate import SddProductPlate


class SddFactory(Factory):
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
                |                         SddFactory
                | 
                | Object to create Structure Detail Modeler Objects.
                | Role: To create the structure object such as Plate, Contour Based Plate and
                | Member.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def add_product_bracket(self, i_position_mode: int) -> SddProductBracket:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func AddProductBracket(CATStrUseBracketPositionMode iPositionMode) As
                | SddProductBracket
                |     Returns a created Bracket. For setting further attributes please refer to
                |     StrCategoryMngt, StrMaterialMngt, StrPanelSurf, StrPlateExtrusionMngt,
                |     StrPanelLimitMngt, StrSketchBasedDMSMngt.
                |     Role: Creates a Bracket.
                | 
                |     Parameters:
                | 
                |         iPositionMode
                |             The PositionMode define the delimitation is made by which type of
                |             mode. ( CATStrUseBracketPositionMode)
                |             - 3: catStr3DAxisPositionMode
                |             - 4: catStrPlateStiffenerPositionMode
                |             - 5: catStrStiffenerStiffenerPositionMode
                |             - 6: catStrMultiLimitsPositionMode 
                | 
                |     Example:
                | 
                | 
                |              This example creates a Bracket.
                |              
                | 
                |              Dim ObjSddFactory As SddFactory
                |              SFDProdSel.Add ObjVPMRootOccurrence
                |              Set ObjSddFactory = SFDProdSel.FindObject("CATIASddFactory")
                |              Dim ObjProductBracket As SddProductBracket
                |              Set ObjProductBracket = ObjSddFactory.AddProductBracket(5)

        :param int i_position_mode:
        :return: SddProductBracket
        """
        return SddProductBracket(self.com_object.AddProductBracket(i_position_mode))

    def add_product_member(self) -> SddProductMember:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func AddProductMember() As SddProductMember
                |     Returns a created Member. See StrCategoryMngt, StrMaterialMngt,
                |     StrSectionMngt, StrOpenings, StrProfileLimitMngt objects.
                |     Role: Creates a Member.
                | 
                |     Example:
                | 
                | 
                |              This example creates a member.
                |              
                | 
                |               'Get SddFactory
                |               Dim product1Service As PLMProductService
                |               Set product1Service = CATIA.ActiveEditor.GetService("PLMProductService")
                |               Dim ObjVPMRootOccurrence As VPMRootOccurrence
                |               Set ObjVPMRootOccurrence = product1Service.RootOccurrence
                |               Set ObjSelection = CATIA.ActiveEditor.Selection
                |               ObjSelection.Add ObjVPMRootOccurrence
                |               Dim ObjSddFactory As SddFactory
                |               Set ObjSddFactory = ObjSelection.FindObject("CATIASddFactory")
                |               Dim ObjMember As SddProductMember
                |               Set ObjMember = ObjSddFactory.AddProductMember

        :return: SddProductMember
        """
        return SddProductMember(self.com_object.AddProductMember())

    def add_product_plate(self, i_concave_mode: bool) -> SddProductPlate:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func AddProductPlate(boolean iConcaveMode) As SddProductPlate
                |     Returns an empty panel created.
                |     Role:Creates an empty panel, ie a VPMReference typed with
                |     V_Discipline="Structure_Plate" and
                |     PLMExtension="StrPlate".
                | 
                |     Parameters:
                | 
                |         iConcaveMode
                |             Defines Advanced plate or basic plate. For creation of advanced
                |             plate this should be TRUE.

        :param bool i_concave_mode:
        :return: SddProductPlate
        """
        return SddProductPlate(self.com_object.AddProductPlate(i_concave_mode))

    def init_resources(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub InitResources()
                |     Loads SDD resources
                | 
                |     Example:
                |              This example initializes resources for SDD
                |              system.
                |
                |               ObjSddFactory.InitResources

        :return: None
        """
        return self.com_object.InitResources()

    def __repr__(self):
        return f'SddFactory(name="{self.name}")'
