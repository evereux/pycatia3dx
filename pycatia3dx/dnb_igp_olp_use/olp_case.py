"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.dnb_igp_olp_use.olp_ast_branch import OLPAstBranch
from pycatia3dx.dnb_igp_olp_use.olp_instructions import OLPInstructions


class OLPCase(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     OlpCase
                | 
                | A case block for a test case instruction.
                | 
                | This interface can only be used by a translator within the Robotics Off-line
                | Programming (OLP) Download or Upload command.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def instructions(self) -> OLPInstructions:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Instructions() As OlpInstructions (Read Only)
                |     The list of instructions executed if the case is matched.

        :return: OLPInstructions
        """

        return OLPInstructions(self.com_object.Instructions)

    @property
    def values(self) -> OLPAstBranch:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Values() As OlpAstBranch
                |     The expression that determines when this case is executed.
                |     Multiple values can be specified if they are seperated by comma operators
                |     (,). When set, the OlpAstBranch.Value of the AST tree is used for the
                |     expression. When retrieved, the DELMIA expression is parsed and is returned in
                |     the format expected by OlpExpressionFixerDownload. You can find more
                |     information on the OLP Expression AST format in the documentation under
                |     Automation | Robotics | Robotics Offline Programming | Offline Programming
                |     Expression Translation. 

        :return: OLPAstBranch
        """

        return OLPAstBranch(self.com_object.Values)

    @values.setter
    def values(self, value: OLPAstBranch):
        """
        :param OlpAstBranch value:
        """

        self.com_object.Values = value

    def __repr__(self):
        return f'OLPCase(name="{ self.name }")'
