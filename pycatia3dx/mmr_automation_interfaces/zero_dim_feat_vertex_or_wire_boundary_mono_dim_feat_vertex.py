"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-27 12:30:08.885021

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.mmr_automation_interfaces.vertex import Vertex


class ZeroDimFeatVertexOrWireBoundaryMonoDimFeatVertex(Vertex):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     InfModelInterfaces.Reference
                |                         CATMmrAutomationInterfaces.Boundary
                |                             CATMmrAutomationInterfaces.Vertex
                |                                ZeroDimFeatVertexOrWireBoundaryMonoDimFeatVertex
                | 
                | 0-D boundary beeing either an isolated point or the extremity of a feature
                | whose topological result is one dimensional.
                | Role: This Boundary object may be, for example, the extremity of a line
                | segment.
                | You will create a ZeroDimFeatVertexOrWireBoundaryMonoDimFeatVertex object using
                | the Shapes.GetBoundary , HybridShapes.GetBoundary , Sketches.GetBoundary or
                | Selection.SelectElement2 method. Then, you pass it to the
                | operator.
                | The lifetime of a ZeroDimFeatVertexOrWireBoundaryMonoDimFeatVertex object is
                | limited, see Boundary.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def __repr__(self):
        return f'ZeroDimFeatVertexOrWireBoundaryMonoDimFeatVertex(name="{ self.name }")'
