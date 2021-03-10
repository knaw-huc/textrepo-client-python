
# flake8: noqa

# Import all APIs into this package.
# If you have many APIs here with many many models used in each API this may
# raise a `RecursionError`.
# In order to avoid this, import only the API that you directly need like:
#
#   from .api.about_api import AboutApi
#
# or import this package, but before doing it, use:
#
#   import sys
#   sys.setrecursionlimit(n)

# Import APIs into API package:
from textrepo_client.api.about_api import AboutApi
from textrepo_client.api.contents_api import ContentsApi
from textrepo_client.api.dashboard_api import DashboardApi
from textrepo_client.api.documents_api import DocumentsApi
from textrepo_client.api.files_api import FilesApi
from textrepo_client.api.find_api import FindApi
from textrepo_client.api.import_api import ImportApi
from textrepo_client.api.index_api import IndexApi
from textrepo_client.api.metadata_api import MetadataApi
from textrepo_client.api.task_api import TaskApi
from textrepo_client.api.types_api import TypesApi
from textrepo_client.api.versions_api import VersionsApi
