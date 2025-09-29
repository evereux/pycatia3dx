"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.types.general import CATVariant


class CompositesServices(AnyObject):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     CompositesServices
                | 
                | Represents CATIACompositesServices that allow to query composites
                | entity.
                | Role: On any object recovers is it his a composites object or not and provides
                | its type if yes.
                | 
                | Example:
                |     This VBScript example illustrates how to GetCompositesType if any , on
                |     objects in CATIA Part. 
                | 
                |      '-------------------------------------------------------------------
                |      ' CATIA Composites
                |      ' VBScript example to identify composites object type
                |      '------------------------------------------------------------------
                |      Sub CATMain()
                |         Const UNKNOWN       = 0 
                |         Const STACKING      = 1 
                |         Const PLYGROUP      = 2 
                |         Const SEQUENCE      = 3
                |         Const CUTPIECEGROUP = 4
                |         Const PLY           = 5
                |         Const CORE          = 6
                |         Const CUTPIECE      = 7
                |         ' Part 
                |         Set myPart = CATIA.ActiveDocument.Part
                |      
                |         ' Get Service Object by querying on part - extension of CATIA Base
                |         
                |         Set myCompServObj = myPart.GetItem("CATCompositesServices")
                |         
                |         ' Hybrid Bodies
                |         Set myHBodies = myPart.HybridBodies
                |         
                |         ' Get Part Hybrid Bodies Count
                |         HBCount = myHBodies.Count
                |        
                |         StckCnt = 0
                |         For N = 1 To PartHBCount
                |            ' Iterate through all Hybrid Bodies in Part one by one and retrieve
                |            its type
                |              Set myObject = myHBodies.Item(N)
                |              myCompServObj.GetCompositesType myObject, myType
                |              If myType = STACKING Then
                |         		     ' ==> Stacking Composites feature type is recovered  among
                |         hybridshapes under part 
                |         		    ObjCompositesStacking =  myObject
                |         		    ' ....
                |         		Exit For 
                |         	End if 
                |         Next 
                |         Mggbox "Stacking="& ObjCompositesStacking.Name 
                |      End Sub
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def get_composites_type(self, i_object: CATVariant, o_composites_type: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Sub GetCompositesType(CATVariant iObject,CATCompositesTypeEnum
                | oCompositesType)
                |     Retrieves "Composites Type" of an 3D object.
                | 
                |     Parameters:
                | 
                |         iObject
                |             Object whose type is to be retrieved. 
                |         oCompositesType
                |             Composites Type of input object. 
                | 
                |     See also:
                |         CATCompositesTypeEnum

        :param CATVariant i_object:
        :param int o_composites_type:
        :return: None
        """
        return self.com_object.GetCompositesType(i_object, o_composites_type)

    def __repr__(self):
        return f'CompositesServices(name="{self.name}")'
