"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.knowledge_interfaces.parameter import Parameter
from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.types.general import CATVariant


class StrReferenceSketchPublicParameters(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     StrReferenceSketchPublicParameters
                | 
                | Object for Public parameters collection of Reference Sketch used in Sketch
                | Based Panel or Sketch Based Plate creation.
                | Obtained from function call GetReferenceSketchPublicParameters on
                | SfdSketchBasedPanel.
                | 
                | Example:
                | 
                | 
                |          This example retrieves StrReferenceSketchPublicParameters from the
                |          object.
                |          
                | 
                |           Dim ObjStrReferenceSketchPublicParms As
                |           StrReferenceSketchPublicParameters
                |           Set ObjStrReferenceSketchPublicParms = ObjSfdSketchBasedPanel.GetReferenceSketchPublicParameters
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def count(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Count() As long
                |     Returns the number of public parameters exposed by the reference
                |     sketch.
                | 
                |     Example:
                | 
                |          
                | 
                |              This example obtains the number of public parameters available for
                |              editing
                |              
                | 
                |              Dim ObjStrReferenceSketchPublicParms As
                |              StrReferenceSketchPublicParameters
                |              Set ObjStrReferenceSketchPublicParms = oObjSfdSketchBasedPlate.StrReferenceSketchPublicParameters
                |              Dim NCount As Integer
                |              Set NCount = ObjStrReferenceSketchPublicParms.Count

        :return: int
        """
        return self.com_object.Count()

    def item(self, i_index: CATVariant) -> Parameter:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Item(CATVariant iIndex) As Parameter
                |     Returns the public parameter of reference sketch at location
                |     iIndex.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index location of the public parameter 
                | 
                |     Example:
                | 
                | 
                |             This example retrieves the public parameter at location 1 and
                |             modifies it to
                |              20mm
                | 
                |              Dim ObjPublicParm As Parameter
                |              Set ObjPublicParm = ObjStrReferenceSketchPublicParms.Item(1)
                |              ObjPublicParm.ValuateFromString("200mm")

        :param CATVariant i_index:
        :return: Parameter
        """
        return Parameter(self.com_object.Item(i_index))

    def __repr__(self):
        return f'StrReferenceSketchPublicParameters(name="{ self.name }")'
