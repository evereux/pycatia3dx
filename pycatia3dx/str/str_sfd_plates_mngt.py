"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.str.str_references import StrReferences
from pycatia3dx.str.str_sfd_plates import StrSfdPlates


class StrSfdPlatesMngt(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     StrSfdPlatesMngt
                | 
                | Object to manage the Plates and the seams(cutting element) on SFD
                | Panel.
                | Role: To define seams for SFD Panel.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def cutting_elements(self) -> StrReferences:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property CuttingElements() As StrReferences
                |     Returns or sets the cutting element(seams) on the Panel.
                | 
                |     Example:
                | 
                | 
                |              This example sets CuttingElements for the SfdPanel to create split
                |              plates.
                |              
                | 
                |               Dim ObjSfdPlatesMngt As SfdPlatesMngt
                |               Set ObjSfdPlatesMngt = iObjSfdPanel.SfdPlatesMngt
                |               Dim ListOfCuttingRefs As StrReferences
                |               'Retrieve object of CuttingElement List
                |               Set ListOfCuttingRefs = ObjSfdPlatesMngt.CuttingElements
                |               'Add the references of cutting elements in the
                |               list
                |               ListOfCuttingRefs.Add ReferenceOfCuttingElem
                |               'set the cutting element list
                |               ObjSfdPlatesMngt.CuttingElements = ListOfCuttingRefs

        :return: StrReferences
        """

        return StrReferences(self.com_object.CuttingElements)

    @cutting_elements.setter
    def cutting_elements(self, value: StrReferences):
        """
        :param StrReferences value:
        """

        self.com_object.CuttingElements = value

    def get_plates(self) -> StrSfdPlates:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetPlates() As StrSfdPlates
                |     Returns the Plates of this Panel..
                | 
                |     Example:
                | 
                | 
                |              This example retrieves list of plates under this super
                |              plate.
                |              
                | 
                |               Dim ObjSfdPlateList As SfdPlates
                |               Set ObjSfdPlateList = ObjSfdPlatesMngt.GetPlates

        :return: StrSfdPlates
        """
        return StrSfdPlates(self.com_object.GetPlates())

    def run(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub Run()
                |     Generates the plates under a Panel.
                |     Role: This function applies to a Panel only. The Run() method is used to
                |     generate the plates under a panel. The Run method will add or remove plates
                |     depending on the cutting elements set in the Panel. 

        :return: None
        """
        return self.com_object.Run()

    def __repr__(self):
        return f'StrSfdPlatesMngt(name="{ self.name }")'
