"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.dnb_igp_olp_use.olp_instruction import OLPInstruction


class OLPGoto(OLPInstruction):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     DNBIgpOlpUseItf.OlpInstruction
                |                         OlpGoto
                | 
                | A goto instruction.
                | 
                | This interface can only be used by a translator within the Robotics Off-line
                | Programming (OLP) Download or Upload command.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def target_instruction(self) -> OLPInstruction:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property TargetInstruction() As OlpInstruction
                |     The instruction to jump to.
                | 
                |     The label text associated with a goto is set on the instruction using the
                |     OlpInstruction.Label property. If an instruction is referenced from a Goto but
                |     no label text is set, a value will be automatically assigned to the
                |     label.

        :return: OLPInstruction
        """

        return OLPInstruction(self.com_object.TargetInstruction)

    @target_instruction.setter
    def target_instruction(self, value: OLPInstruction):
        """
        :param OLPInstruction value:
        """

        self.com_object.TargetInstruction = value

    def __repr__(self):
        return f'OLPGoto(name="{ self.name }")'
