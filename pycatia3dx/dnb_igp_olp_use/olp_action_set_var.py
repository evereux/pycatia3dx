"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.dnb_igp_olp_use.olp_ast_branch import OLPAstBranch
from pycatia3dx.dnb_igp_olp_use.olp_trigger_action import OLPTriggerAction
from pycatia3dx.dnb_igp_olp_use.olp_variable import OLPVariable


class OLPActionSetVar(OLPTriggerAction):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     DNBIgpOlpUseItf.OlpTriggerAction
                |                         OlpActionSetVar
                | 
                | A trigger action that sets a variable to s specified value.
                | 
                | This interface can only be used by a translator within the Robotics Off-line
                | Programming (OLP) Download or Upload command.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def destination(self) -> OLPVariable:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Destination() As OlpVariable
                |     The variable which is being assigned.
                |     You can retrieve an existing variable using OlpInstruction.FindVariable or
                |     create a new one using OlpVariables.

        :return: OLPVariable
        """

        return OLPVariable(self.com_object.Destination)

    @destination.setter
    def destination(self, value: OLPVariable):
        """
        :param OLPVariable value:
        """

        self.com_object.Destination = value

    @property
    def destination_express(self) -> OLPAstBranch:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property DestinationExpress() As OlpAstBranch
                |     The variable which is being assigned as an expression.

        :return: OLPAstBranch
        """

        return OLPAstBranch(self.com_object.DestinationExpress)

    @destination_express.setter
    def destination_express(self, value: OLPAstBranch):
        """
        :param OLPAstBranch value:
        """

        self.com_object.DestinationExpress = value

    @property
    def source(self) -> OLPAstBranch:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Source() As OlpAstBranch
                |     The expression that evaluates to the value being assigned.
                |     When set, the OlpAstBranch.Value of the AST tree is used for the
                |     expression. When retrieved, the DELMIA expression is parsed and is returned in
                |     the format expected by OlpExpressionFixerDownload. You can find more
                |     information on the OLP Expression AST format in the documentation under
                |     Automation | Robotics | Robotics Offline Programming | Offline Programming
                |     Expression Translation. 

        :return: OLPAstBranch
        """

        return OLPAstBranch(self.com_object.Source)

    @source.setter
    def source(self, value: OLPAstBranch):
        """
        :param OLPAstBranch value:
        """

        self.com_object.Source = value

    def __repr__(self):
        return f'OLPActionSetVar(name="{ self.name }")'
