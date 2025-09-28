"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-27 12:30:08.885021

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.knowledge_interfaces.relation import Relation


class Rule(Relation):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     KnowledgeIDLItf.KnowledgeObject
                |                        
                |                        KnowledgeIDLItf.KnowledgeActivateObject
                |                             KnowledgeIDLItf.Relation
                |                                 Rule
                | 
                | Represents the Knowledge rule relation.
                | The following example shows how to create a rule that selects a depth with
                | respect to a mass value. The depth and mass parameters should exist before the
                | creation of the rule object.
                | 
                |  Dim part1 As Part
                |  Set part1 = ...
                |  Dim mass As RealParam
                |  Set mass = part1.Parameters.CreateReal("mass", 5.)
                |  Dim depth As RealParam
                |  Set depth = part1.Parameters.CreateReal("depth", 0.)
                |  Dim selectdepth As Relation
                |  Set selectdepth = part1.Relations.CreateProgram
                |                     ("select_depth",
                |                      "Select depth with respect to mass", 
                |                      "if (mass>2kg) { depth=2mm } else { depth=1mm
                |                      }")
                |  
                | 
                | See also:
                |     Relations.CreateProgram
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def __repr__(self):
        return f'Rule(name="{ self.name }")'
