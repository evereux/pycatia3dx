"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.structure.str_category_mngt import StrCategoryMngt
from pycatia3dx.structure.str_material_mngt import StrMaterialMngt
from pycatia3dx.structure.str_panel_limit_mngt import StrPanelLimitMngt
from pycatia3dx.structure.str_panel_surf import StrPanelSurf
from pycatia3dx.structure.str_plate_extrusion_mngt import StrPlateExtrusionMngt
from pycatia3dx.structure.str_reference_sketch_public_parameters import StrReferenceSketchPublicParameters
from pycatia3dx.structure.str_sketch_based_dms_mngt import StrSketchBasedDMSMngt


class SfdSketchBasedPlate(AnyObject):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SfdSketchBasedPlate
                | 
                | Object to manage the Structure Functional Modeler SketchBasedPlate
                | object.
                | Role: Allows accessing and setting of SketchBasedPlate's data.
                | 
                | See also:
                |     SfdFactory
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def str_category_mngt(self) -> StrCategoryMngt:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property StrCategoryMngt() As StrCategoryMngt (Read Only)
                |     Returns the StrCategoryMngt object.
                | 
                |     Example:
                | 
                |          
                |              
                |              This example retrieves in ObjStrCategoryMngt the StrCategoryMngt
                |              object
                |              of the SfdPanel
                |              
                | 
                |              Dim ObjStrCategoryMngt As StrCategoryMngt
                |              Set ObjStrCategoryMngt = ObjSfdSketchBasedPlate.StrCategoryMngt

        :return: StrCategoryMngt
        """

        return StrCategoryMngt(self.com_object.StrCategoryMngt)

    @property
    def str_material_mngt(self) -> StrMaterialMngt:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property StrMaterialMngt() As StrMaterialMngt (Read Only)
                |     Returns the StrMaterialMngt object.
                | 
                |     Example:
                | 
                |          
                |              
                |              This example retrieves in ObjMaterialMngt the StrMaterialMngt
                |              object
                |              of the SfdPanel
                |              
                | 
                |              Dim ObjMaterialMngt As StrMaterialMngt
                |              Set ObjMaterialMngt = ObjSfdSketchBasedPlate.StrMaterialMngt

        :return: StrMaterialMngt
        """

        return StrMaterialMngt(self.com_object.StrMaterialMngt)

    @property
    def str_panel_limit_mngt(self) -> StrPanelLimitMngt:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property StrPanelLimitMngt() As StrPanelLimitMngt (Read Only)
                |     Returns the StrPanelLimitMngt object.
                | 
                |     Example:
                | 
                |          
                |              
                |              This example retrieves in ObjStrPanelLimitMngt the
                |              StrPanelLimitMngt object
                |              of the SfdPanel
                |              
                | 
                |              Dim ObjStrPanelLimitMngt As StrPanelLimitMngt
                |              Set ObjStrPanelLimitMngt = ObjSfdSketchBasedPlate.StrPanelLimitMngt

        :return: StrPanelLimitMngt
        """

        return StrPanelLimitMngt(self.com_object.StrPanelLimitMngt)

    @property
    def str_panel_surf(self) -> StrPanelSurf:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property StrPanelSurf() As StrPanelSurf (Read Only)
                |     Returns the StrPanelSurf object.
                | 
                |     Example:
                | 
                |          
                | 
                |              This example retrieves in ObjSfdPanelSurf the StrPanelSurf
                |              object
                |              of the SfdPanel
                |              
                | 
                |              Dim ObjSfdSketchBasedPlate As SfdSketchBasedPlate
                |              Set ObjSfdSketchBasedPlate = ObjSfdFactory.AddSfdSketchBasedPlate(DestPart, False)
                |              Dim ObjSfdPanelSurf As StrPanelSurf 
                |              Set ObjSfdPanelSurf = ObjSfdSketchBasedPlate.StrPanelSurf

        :return: StrPanelSurf
        """

        return StrPanelSurf(self.com_object.StrPanelSurf)

    @property
    def str_plate_extrusion_mngt(self) -> StrPlateExtrusionMngt:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property StrPlateExtrusionMngt() As StrPlateExtrusionMngt (Read
                | Only)
                |     Returns the StrPlateExtrusionMngt object.
                | 
                |     Example:
                | 
                |          
                |              
                |              This example retrieves in ObjStrPlateExtrusionMngt the
                |              StrPlateExtrusionMngt object
                |              of the SfdPanel
                |              
                | 
                |              Dim ObjStrPlateExtrusionMngt As
                |              StrPlateExtrusionMngt
                |              Set ObjStrPlateExtrusionMngt = ObjSfdSketchBasedPlate.StrPlateExtrusionMngt

        :return: StrPlateExtrusionMngt
        """

        return StrPlateExtrusionMngt(self.com_object.StrPlateExtrusionMngt)

    @property
    def str_reference_sketch_public_parameters(self) -> StrReferenceSketchPublicParameters:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property StrReferenceSketchPublicParameters() As
                | StrReferenceSketchPublicParameters (Read Only)
                |     Returns the CATIAStrReferenceSketchPublicParameters to the Reference Sketch
                |     Public Parameters used in creation of SketchBasedPlate
                |     object.
                | 
                |     Parameters:
                | 
                |         oListPublicParms
                |             The list of the Reference Sketch Public Parameters available for
                |             modification. 
                | 
                |     Example:
                | 
                |          
                |              
                |              This example retrieves in ObjStrReferenceSketchPublicParms, the
                |              list of available
                |                public parameters for the selected reference
                |                sketch.
                | 
                |              Dim ObjStrReferenceSketchPublicParms As
                |              StrReferenceSketchPublicParameters
                |              Set ObjStrReferenceSketchPublicParms = oObjSfdSketchBasedPlate.StrReferenceSketchPublicParameters
                | 
                | 
                |              It then modifies the first public parameter so obtained in the
                |              list to 2000mm.
                | 
                |              Dim ObjPublicParm As Parameter
                |              Set ObjPublicParm = ObjStrReferenceSketchPublicParms.Item(1)
                |              ObjPublicParm.ValuateFromString ("2000mm")

        :return: StrReferenceSketchPublicParameters
        """

        return StrReferenceSketchPublicParameters(self.com_object.StrReferenceSketchPublicParameters)

    @property
    def str_sketch_based_dms_mngt(self) -> StrSketchBasedDMSMngt:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property StrSketchBasedDMSMngt() As StrSketchBasedDMSMngt (Read
                | Only)
                |     Returns the StrSketchBasedDMSMngt object.
                | 
                |     Example:
                | 
                |          
                |              
                |              This example retrieves in ObjStrSketchBasedDMSMngt the
                |              StrSketchBasedDMSMngt object
                |              of the SfdPanel
                |              
                | 
                |              Dim ObjStrSketchBasedDMSMngt As
                |              StrSketchBasedDMSMngt
                |              Set ObjStrSketchBasedDMSMngt = ObjSfdSketchBasedPlate.SfdStrSketchBasedDMSMngt

        :return: StrSketchBasedDMSMngt
        """

        return StrSketchBasedDMSMngt(self.com_object.StrSketchBasedDMSMngt)

    def __repr__(self):
        return f'SfdSketchBasedPlate(name="{self.name}")'
