"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.dnb_igp_olp_use.olp_procedures import OLPProcedures
from pycatia3dx.dnb_igp_olp_use.olp_variables import OLPVariables


class OLPBehavior(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     OlpBehavior
                | 
                | Interface for accessing a resource's behavior.
                | 
                | This interface can only be used by a translator within the Robotics Off-line
                | Programming (OLP) Download or Upload command.
                | This object can be retrieved from a
                | OlpTranslatorHelper.Behavior.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def global_variables(self) -> OLPVariables:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property GlobalVariables() As OlpVariables (Read Only)
                |     The global variables, IO, and constants in this behavior.

        :return: OLPVariables
        """

        return OLPVariables(self.com_object.GlobalVariables)

    @property
    def procedures(self) -> OLPProcedures:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Procedures() As OlpProcedures (Read Only)
                |     All procedures (robot tasks) for this behavior.
                |     To get a list of the procedures being downloaded use
                |     OlpTranslatorHelper.Tasks 

        :return: OLPProcedures
        """

        return OLPProcedures(self.com_object.Procedures)

    def __repr__(self):
        return f'OLPBehavior(name="{ self.name }")'
