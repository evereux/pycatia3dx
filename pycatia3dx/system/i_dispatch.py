#! usr/bin/python3.9
"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2020 on 2025-09-13 15:35:27.265802

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system_ts.i_unknown import IUnknown


class IDispatch(IUnknown):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)

                | SystemTS.IUnknown
                |     IDispatch
                | 
                | Base interface for all Automation interfaces.
                | Role: All Automation interfaces derive from IDispatch which replaces for UNIX
                | the native Microsoft(R) IDispatch interface. This interface supplies basic
                | methods to be Microsoft(R) Automation compliant.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def __repr__(self):
        return f'IDispatch(name="{self.name}")'
