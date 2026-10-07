"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.interfaces.service import Service
from pycatia3dx.mmr_automation_interfaces.part import Part
from pycatia3dx.system.any_object import AnyObject


class PCBService(Service):
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
                |                         PCBService

    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def create_board(self, i_root: AnyObject) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func CreateBoard(CATBaseDispatch iRoot) As CATBaseDispatch
                |     Creates a Board.
                | 
                |     Parameters:
                | 
                |         iRoot
                |             Root product of the Part to extend 
                |         oBoard
                |             The board created 
                | 
                |     Returns:
                | 
                |             The result of the method:
                |             S_OK if succeeded
                |             E_FAIL if failed

        :param AnyObject i_root:
        :return: AnyObject
        """
        return self.com_object.CreateBoard(i_root.com_object)

    def create_component(self, i_root: AnyObject, i_part: Part, i_elec_package_number: str, i_elec_part_number: str,
                         i_elec_type: str) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func CreateComponent(CATBaseDispatch iRoot,Part iPart,CATBSTR
                | iElecPackageNumber,CATBSTR iElecPartNumber,CATBSTR iElecType) As
                | CATBaseDispatch
                |     Creates a Component.
                | 
                |     Parameters:
                | 
                |         iRoot
                |             Root product of the Part to extend 
                |         iElecPackageNumber
                |             The package number used to valuate the component attribute
                |             
                |         iElecPartNumber
                |             The part number used to valuate the part number of the component
                |             
                |         iElecType
                |             The Type of the component to create : ELECTRICAL or MECHANICAL 
                |         oComponent
                |             The Component created 
                | 
                |     Returns:
                | 
                |             The result of the method:
                |             S_OK if succeeded
                |             E_FAIL if failed

        :param AnyObject i_root:
        :param Part i_part:
        :param str i_elec_package_number:
        :param str i_elec_part_number:
        :param str i_elec_type:
        :return: AnyObject
        """
        return self.com_object.CreateComponent(i_root.com_object, i_part.com_object, i_elec_package_number,
                                               i_elec_part_number, i_elec_type)

    def create_panel(self, i_root: AnyObject) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func CreatePanel(CATBaseDispatch iRoot) As CATBaseDispatch
                |     Creates a panel.
                | 
                |     Parameters:
                | 
                |         iRoot
                |             Root product of the Part to extend 
                |         oPanel
                |             The panel created 
                | 
                |     Returns:
                | 
                |             The result of the method:
                |             S_OK if succeeded
                |             E_FAIL if failed

        :param AnyObject i_root:
        :return: AnyObject
        """
        return self.com_object.CreatePanel(i_root.com_object)

    def get_pcb_object(self, i_part: Part) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetPCBObject(Part iPart) As CATBaseDispatch
                |     Gets the Board or Component from the CATIAPart.
                | 
                |     Parameters:
                | 
                |         iPart
                |             The Mechanical Part 
                |         oPCBObject
                |             The corresponding PCB objet (PCBBoard or PCBComponent). The result
                |             of the method:
                |             S_OK if succeeded
                |             E_FAIL if failed

        :param Part i_part:
        :return: AnyObject
        """
        return self.com_object.GetPCBObject(i_part.com_object)

    def get_parent_product(self, i_part: Part) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetParentProduct(Part iPart) As CATBaseDispatch
                |     Gets the product aggregating the Part.
                | 
                |     Parameters:
                | 
                |         iPart
                |             The Mechanical Part 
                |         oRoot
                |             The product aggregating the Part 
                | 
                |     Returns:
                | 
                |             The result of the method:
                |             S_OK if succeeded
                |             E_FAIL if failed 

        :param Part i_part:
        :return: AnyObject
        """
        return self.com_object.GetParentProduct(i_part.com_object)

    def __repr__(self):
        return f'PcbService(name="{self.name}")'
