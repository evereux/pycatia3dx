from pycatia3dx.knowledge_interfaces.parms_set import ParmsSet
from pycatia3dx.knowledge_interfaces.rels_set import RelsSet
from pycatia3dx.mmr_automation_interfaces.body import Body
from pycatia3dx.mmr_automation_interfaces.hybrid_body import HybridBody

body_types = {
    'Body': Body,
    'HybridBody': HybridBody,
    'ParmsSet': ParmsSet,
    'RelsSet': RelsSet,
}
