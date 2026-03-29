"""
    The catia base object is from which most other functionality derives. See examples for more information.

    >>> from pycatia3dx import catia3dx
    >>> application = catia()

"""

from pycatia3dx.annotation.enums import *
from pycatia3dx.composites_use.enums import *
from pycatia3dx.del_curve_trajectory.enums import *
from pycatia3dx.del_resource_builder.enums import *
from pycatia3dx.del_robot_simulation.enums import *
from pycatia3dx.del_rof_surf.enums import *
from pycatia3dx.del_spot_welding.enums import *
from pycatia3dx.del_spot_welding_as_is.enums import *
from pycatia3dx.dnb_fitting.enums import *
from pycatia3dx.dnb_igp_arc_welding_use.enums import *
from pycatia3dx.dnb_igp_olp_use.enums import *
from pycatia3dx.drafting.enums import *
from pycatia3dx.drafting_2d.enums import *
from pycatia3dx.eng_connection.enums import *
from pycatia3dx.fmt_mode.enums import *
from pycatia3dx.hybrid_shapes.enums import *
from pycatia3dx.interfaces.enums import *
from pycatia3dx.kin_mechanism.enums import *
from pycatia3dx.kin_simulation.enums import *
from pycatia3dx.know_how.enums import *
from pycatia3dx.knowledge_interfaces.enums import *
from pycatia3dx.material.enums import *
from pycatia3dx.measure.enums import *
from pycatia3dx.measure.enums import *
from pycatia3dx.mmr_automation_interfaces.enums import *
from pycatia3dx.opns_section.enums import *
from pycatia3dx.os.enums import *
from pycatia3dx.part.enums import *
from pycatia3dx.pcb_board.enums import *
from pycatia3dx.plm_access.enums import *
from pycatia3dx.plm_interference.enums import *
from pycatia3dx.sim_rep.enums import *
from pycatia3dx.sketcher.enums import *
from pycatia3dx.sma_few_optimization.enums import *
from pycatia3dx.sma_mat_material.enums import *
from pycatia3dx.sma_mpa_base.enums import *
from pycatia3dx.sma_mpa_foundation.enums import *
from pycatia3dx.sma_mpa_results.enums import *
from pycatia3dx.sma_mpa_structural_mode.enums import *
from pycatia3dx.sma_spa_structural.enums import *
from pycatia3dx.structure.enums import *
from pycatia3dx.system.enums import *
from pycatia3dx.tps.enums import *
from pycatia3dx.version import version

from pycatia3dx.base_interfaces.base_application import catia_application as catia3dx

__author__ = 'Paul Bourne'
__author_email = 'evereux@gmail.com'
__description__ = 'A python module to interface with the CATIA 3DX COM object.'
__name__ = "pycatia3dx"
__version__ = version
__url__ = "https://github.com/evereux/pycatia"

name = __name__
