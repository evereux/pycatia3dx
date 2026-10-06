"""

    Example - Search Service - 001

    Description:
        A wild card search for all products with a name starting with "Test".
        The first item found is then opened.

    Requirements:
        - A Product already saved with a name starting with "Test".

"""

##########################################################
# insert syspath to project folder so examples can be run.
# for development purposes.
import os
import sys

sys.path.insert(0, os.path.abspath("..\\pycatia3dx"))
##########################################################

from pycatia3dx import catia3dx
from pycatia3dx.plm_access.search_service import SearchService
from pycatia3dx.plm_session_builder.plm_open_service import PLMOpenService

application = catia3dx()

search_service: SearchService = application.get_session_service("Search")

db_search = search_service.database_search
db_search.base_type = "VPMReference"
db_search.add_easy_criteria("V_Name", "Test *")

search_service.search()

# open the first result
open_service: PLMOpenService = application.get_session_service("PLMOpenService")
editor = open_service.plm_open(db_search.results[0])
