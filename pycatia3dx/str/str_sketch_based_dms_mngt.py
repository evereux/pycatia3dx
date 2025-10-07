"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.mode.reference import Reference
from pycatia3dx.system.any_object import AnyObject


class StrSketchBasedDMSMngt(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     StrSketchBasedDMSMngt
                | 
                | Object to manage Delimited Molded Surface for
                | StrSketchBasedPanel.
                | 
                | Role: To manage StrSketchBasedPanel's Delimited Molded
                | Surface.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def str_sketch(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property StrSketch() As Reference (Read Only)
                |     Returns or sets the Reference Sketch.
                | 
                |     Example:
                | 
                |          
                | 
                |              This example sets the ReferenceSketch in RefSketch as
                |              Reference.
                |              of SfdSketchBasedPanel or SfdSketchBasedPlate.
                |              
                | 
                |              'get Reference Sketch
                |              Dim RefSketch As Reference
                |              set RefSketch = ObjSfdSketchBasedPanel.ReferenceSketch("SAMPLE_RCO_2LIMITS_KB")
                |             
                |              'set DMS
                |              Dim PanelDMS As StrSketchBasedDMSMngt
                |              Set PanelDMS = oObjSfdSketchBasedPanel.StrSketchBasedDMSMngt
                |              PanelDMS.StrSketch = RefSketch

        :return: Reference
        """

        return Reference(self.com_object.StrSketch)

    def activate_sketch_contour(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub ActivateSketchContour()
                |     Returns the Sketch Contour activated successfuly or not
                | 
                |     Example:
                | 
                | 
                |              With new algorithm of parametric panel/plate, Sketch need to
                |              activate before call update(or build) of feature
                |              This example show activate sketch contour before update the
                |              Parametric panel/Plate

        :return: None
        """
        return self.com_object.ActivateSketchContour()

    def deactivate_sketch_contour(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub DeactivateSketchContour()
                |     Returns the Sketch Contour deactivated successfuly or not
                | 
                |     Example:
                | 
                | 
                |              With new algorithm of parametric panel/plate, Sketch need to
                |              deactivate when parametric panel/plate input
                |              modified
                |              This example show deactivate sketch contour after modified the
                |              Parametric panel/Plate

        :return: None
        """
        return self.com_object.DeactivateSketchContour()

    def set_str_sketch(self, i_ref_sketch_name: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetStrSketch(CATBSTR iRefSketchName)

        :param str i_ref_sketch_name:
        :return: None
        """
        return self.com_object.SetStrSketch(i_ref_sketch_name)

    def __repr__(self):
        return f'StrSketchBasedDmsMngt(name="{ self.name }")'
