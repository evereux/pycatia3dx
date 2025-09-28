"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-27 12:30:08.885021

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.knowledge_interfaces.relation import Relation


class Formula(Relation):

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
                |                                 Formula
                | 
                | Represents the formula Knowledge relation.
                | The following example shows how to create a formula that computes the mass of a
                | cuboid, given its geometric dimensions and the density of the material it is
                | made of:
                | 
                |  Dim aParmFact as ParametersFactory
                |  Set aParmFact = ...
                |  Dim aRelFact as RelationsFactory
                |  Set aRelFact = aParmFact.Root.GetKnowledgeRootSet(True, 1).Factory
                |  Dim width As RealParam
                |  Set width = aParmFact.CreateReal("width", 1.)  
                |  Dim height As RealParam
                |  Set height = aParmFact.CreateReal("height", 2.)  
                |  Dim depth As RealParam
                |  Set depth = aParmFact.CreateReal("depth", 3.)  
                |  Dim density As RealParam
                |  Set density = aParmFact.CreateReal("density", 1.5)  
                |  Dim mass As RealParam
                |  Set mass = aParmFact.CreateReal("mass", 0.)  
                |  Dim computemass As RealParam
                |  Set computemass = aRelFact.CreateFormula
                |                     ("computemass",
                |                      "Computes the cuboid mass",  mass,
                |                      "(width*height*depth)*density")
                |  
                | 
                | See also:
                |     ParametersFactory, RelationsFactory, KnowledgeObjects
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def __repr__(self):
        return f'Formula(name="{ self.name }")'
