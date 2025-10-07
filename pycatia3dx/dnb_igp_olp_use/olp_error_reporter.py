"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.dnb_igp_olp_use.olp_ast_node import OLPAstNode


class OLPErrorReporter(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     OlpErrorReporter
                | 
                | Interface for reporting translation warnings and errors.
                | 
                | This interface can only be used by a translator within the Robotics Off-line
                | Programming (OLP) Download or Upload command.
                | This object can be retrieved using
                | OlpTranslatorHelper.ErrorReporter
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def add_conditional_error(self, i_msg: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub AddConditionalError(CATBSTR iMsg)
                |     Add an error message only if no error already exists.
                |     Otherwise this message is added as a trace with level all traces. This is
                |     intended for adding an "unexpected" error message when you don't know if some
                |     other code already logged the error.
                | 
                |     Parameters:
                | 
                |         iMsg
                |             The CATUnicodeString which is the message to add.

        :param str i_msg:
        :return: None
        """
        return self.com_object.AddConditionalError(i_msg)

    def add_message(self, i_type: int, i_msg: str, i_associated_v6_object: AnyObject, i_associated_ast_node: OLPAstNode) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub AddMessage(DELOlpMessageType iType,CATBSTR iMsg,CATBaseDispatch
                | iAssociatedV6Object,OlpAstNode iAssociatedAstNode)
                |     Add a new message that will be displayed to the user.
                | 
                |     Parameters:
                | 
                |         iType
                |             The type of message. 
                |         iMsg
                |             The message to add. 
                |         iAssociatedV6Object
                |             An optional V6 object which is associated with the error. Used to
                |             help the user know where the error occured so they can correct it.
                |             
                |         iAssociatedAstNode
                |             An optional AST node which is associated with the error. Used to
                |             display the file and line number of the error in the input or output NRL
                |             program.

        :param int i_type:
        :param str i_msg:
        :param AnyObject i_associated_v6_object:
        :param OLPAstNode i_associated_ast_node:
        :return: None
        """
        return self.com_object.AddMessage(i_type, i_msg, i_associated_v6_object.com_object, i_associated_ast_node.com_object)

    def add_trace(self, i_level: int, i_msg: str, i_associated_object: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub AddTrace(DELOlpTraceLevel iLevel,CATBSTR iMsg,CATBaseDispatch
                | iAssociatedObject)
                |     Add a new debug trace message. This message will be written to the console
                |     if traces are enabled.
                | 
                |     Parameters:
                | 
                |         iLevel
                |             The importance of this trace. The trace will only get logged if the
                |             current tracing mode is set to accept traces of this importance or higher.
                |             Tracing mode is set by the environment variable DNB_OLP_TRACES which can be set
                |             to All, User, or None. 
                |         iMsg
                |             The message to add. 
                |         iAssociatedObject
                |             An optional object which is associated with the error. The name of
                |             the object will be appended to the trace message in the form: "Message Text -
                |             ObjectName" for example "Translating - MotionProfile.1"

        :param int i_level:
        :param str i_msg:
        :param AnyObject i_associated_object:
        :return: None
        """
        return self.com_object.AddTrace(i_level, i_msg, i_associated_object.com_object)

    def add_unique_message(self, i_type: int, i_msg: str, i_associated_v6_object: AnyObject, i_associated_ast_node: OLPAstNode, i_id: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub AddUniqueMessage(DELOlpMessageType iType,CATBSTR iMsg,CATBaseDispatch
                | iAssociatedV6Object,OlpAstNode iAssociatedAstNode,CATBSTR iID)
                |     Add a unique message that will be displayed to the user.
                |     All messages with the given ID will be displayed as a single message to the
                |     user.
                | 
                |     Parameters:
                | 
                |         iType
                |             The type of message. 
                |         iMsg
                |             The message to add. 
                |         iAssociatedV6Object
                |             An optional V6 object which is associated with the error. Used to
                |             help the user know where the error occured so they can correct it.
                |             
                |         iAssociatedAstNode
                |             An optional AST node which is associated with the error. Used to
                |             display the file and line number of the error in the input or output NRL
                |             program. 
                |         iID
                |             The ID of the message to add. All messages with this ID will be
                |             displayed to the user as a single message. The recommended format for the
                |             message id is [Translator].[Class].[Message].[SubMessage] [Translator] - for
                |             example "DELMIAFanuc" etc. [Class] - the C++ or VB class name that generates
                |             the message [Message] - the message key [SubMessage] - an optional sub message
                |             key

        :param int i_type:
        :param str i_msg:
        :param AnyObject i_associated_v6_object:
        :param OLPAstNode i_associated_ast_node:
        :param str i_id:
        :return: None
        """
        return self.com_object.AddUniqueMessage(i_type, i_msg, i_associated_v6_object.com_object, i_associated_ast_node.com_object, i_id)

    def override_message_severity(self, i_severity: int, i_id: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub OverrideMessageSeverity(DELOlpMessageType iSeverity,CATBSTR
                | iID)
                |     Override the message severity for a particular message ID. This can be any
                |     infrastructure message or a message create by the translator. The message must
                |     be added with an ID to be able to override it. The severity specified here will
                |     be used in place of whatever message type is used. This must be called before
                |     the message is added the 1st time.
                | 
                |     Parameters:
                | 
                |         iSeverity
                |             The type of message. 
                |         iID
                |             The ID of the message to override. See AddUniqueMessage for more
                |             details on the ID. You can set the environment variable
                |             DELMIA_OLP_DISPLAY_ERROR_MESSAGE_ID=1 to display the message IDs in the
                |             message. 

        :param int i_severity:
        :param str i_id:
        :return: None
        """
        return self.com_object.OverrideMessageSeverity(i_severity, i_id)

    def __repr__(self):
        return f'OLPErrorReporter(name="{ self.name }")'
