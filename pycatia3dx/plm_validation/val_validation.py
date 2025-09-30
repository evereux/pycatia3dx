"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.plm_modeller_base.plm_entity import PLMEntity
from pycatia3dx.plm_validation.val_checks import VALChecks
from pycatia3dx.plm_validation.val_concerns import VALConcerns
from pycatia3dx.plm_validation.val_contexts import VALContexts
from pycatia3dx.plm_validation.val_reviews import VALReviews


class VALValidation(PLMEntity):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     PLMModelerBaseIDLItf.PLMEntity
                |                         VALValidation
                | 
                | Allows management of Validation entity
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def checks(self) -> VALChecks:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Checks() As VALChecks (Read Only)
                |     Returns the Checks collection.

        :return: VALChecks
        """

        return VALChecks(self.com_object.Checks)

    @property
    def concerns(self) -> VALConcerns:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Concerns() As VALConcerns (Read Only)
                |     Returns the Concerns collection.

        :return: VALConcerns
        """

        return VALConcerns(self.com_object.Concerns)

    @property
    def contexts(self) -> VALContexts:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Contexts() As VALContexts (Read Only)
                |     Returns the Contexts collection.

        :return: VALContexts
        """

        return VALContexts(self.com_object.Contexts)

    @property
    def reviews(self) -> VALReviews:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Reviews() As VALReviews (Read Only)
                |     Returns the Reviews collection.

        :return: VALReviews
        """

        return VALReviews(self.com_object.Reviews)

    @property
    def type(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Type() As CATBSTR (Read Only)
                |     Returns the type of the Validation ("Product", "Simulation" or "Image").

        :return: str
        """

        return self.com_object.Type

    def __repr__(self):
        return f'ValValidation(name="{ self.name }")'
