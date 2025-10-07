"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.dnb_igp_olp_use.olp_ast_branch import OLPAstBranch
from pycatia3dx.dnb_igp_olp_use.olp_instruction import OLPInstruction


class OLPAssignByString(OLPInstruction):

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
                |                         OlpAssignByString
                | 
                | An assign instruction whose target is specified as a string.
                | 
                | This interface can only be used by a translator within the Robotics Off-line
                | Programming (OLP) Download or Upload command.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def destination_expression(self) -> OLPAstBranch:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property DestinationExpression() As OlpAstBranch
                |     The expression that evaluates to a string for the name of the variable that
                |     is assigned.

        :return: OLPAstBranch
        """

        return OLPAstBranch(self.com_object.DestinationExpression)

    @destination_expression.setter
    def destination_expression(self, value: OLPAstBranch):
        """
        :param OLPAstBranch value:
        """

        self.com_object.DestinationExpression = value

    @property
    def indexes_expression(self) -> OLPAstBranch:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property IndexesExpression() As OlpAstBranch
                |     Set array indexes if the assign target is element(s) from an
                |     array.
                |     In the case of array, it is necessary to specify where to assign values in this array. The format of the indexes expression is as follows, where * means the element(s) to be assigned {2} In array VAR1[5] = {1,*,1,1,1,1} 1 value will be overridden at position 2 {2,2} In array VAR2[3,3] = {{1,1,1};{1,*,1},{1,1,1}} 1 value will overriden at position 2,2 {2} In arary VAR2[3,3] = {{1,1,1};{*,*,*},{1,1,1}} 3 values will overriden at position 2

        :return: OLPAstBranch
        """

        return OLPAstBranch(self.com_object.IndexesExpression)

    @indexes_expression.setter
    def indexes_expression(self, value: OLPAstBranch):
        """
        :param OLPAstBranch value:
        """

        self.com_object.IndexesExpression = value

    @property
    def source(self) -> OLPAstBranch:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Source() As OlpAstBranch
                |     The values to be set, i.e. the source of assignment.
                |     Examples of valid format of the expression: 0.01 {0.01, 0.02, 0.03}

        :return: OLPAstBranch
        """

        return OLPAstBranch(self.com_object.Source)

    @source.setter
    def source(self, value: OLPAstBranch):
        """
        :param OLPAstBranch value:
        """

        self.com_object.Source = value

    def unset_indexes_expression(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub UnsetIndexesExpression()
                |     Unset the array indexes, to indicate a non-array variable.

        :return: None
        """
        return self.com_object.UnsetIndexesExpression()

    def __repr__(self):
        return f'OLPAssignByString(name="{ self.name }")'
