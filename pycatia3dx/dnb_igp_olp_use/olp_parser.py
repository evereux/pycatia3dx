"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.dnb_igp_olp_use.olp_ast_branch import OLPAstBranch
from pycatia3dx.dnb_igp_olp_use.olp_error_reporter import OLPErrorReporter


class OLPParser(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     OlpParser
                | 
                | Parser for compiling a Native Robot Language program using Flex and
                | Bison.
                | 
                | This interface can only be used by a translator within the Robotics Off-line
                | Programming (OLP) Download or Upload command.
                | Output of the parsed NRL program is the Abstract Syntax Tree (AST). This object
                | can be retrieved using OlpTranslatorHelper.CreateParser
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def ast_root(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property AstRoot(OLPAstBranch iAST) (Write Only)
                |     Used to set the root of the Abstract Syntax Tree (AST). All AST branches
                |     and leaves created during parse will be descendents of this
                |     root.
                | 
                |     Parameters:
                | 
                |         iAST
                |             The AST root node.

        :return: None
        """

        return None

    @ast_root.setter
    def ast_root(self, value: OLPAstBranch):
        """
        :param OLPAstBranch value:
        """

        self.com_object.AstRoot = value.com_object

    @property
    def error_reporter(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ErrorReporter(OlpErrorReporter iReporter) (Write
                | Only)
                |     The object used to log any parse errors.
                |     All warnings and errors will be displayed using this
                |     reporter.
                | 
                |     Parameters:
                | 
                |         iReporter
                |             The error reporter to use.

        :return: None
        """

        return None

    @error_reporter.setter
    def error_reporter(self, value: OLPErrorReporter):
        """
        :param OLPErrorReporter value:
        """

        self.com_object.ErrorReporter = value.com_object

    def parse(self, i_file: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub Parse(CATBSTR iFile)
                |     Used to parse the absolute file name sent. The parser generates the
                |     Abstract Syntax Tree (AST) starting from the root set in AstRoot. Errors and
                |     warnings are displayed using the ErrorReporter.
                | 
                |     Parameters:
                | 
                |         iFile
                |             The file to parse.

        :param str i_file:
        :return: None
        """
        return self.com_object.Parse(i_file)

    def parse_string(self, i_text: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub ParseString(CATBSTR iText)
                |     Used to parse a string rather than a file.
                | 
                |     Parameters:
                | 
                |         iText
                |             The text to parse. 

        :param str i_text:
        :return: None
        """
        return self.com_object.ParseString(i_text)

    def __repr__(self):
        return f'OLPParser(name="{ self.name }")'
