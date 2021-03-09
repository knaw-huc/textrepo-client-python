# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from from textrepo_client.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from textrepo_client.model.document import Document
from textrepo_client.model.form_document import FormDocument
from textrepo_client.model.form_text_repo_file import FormTextRepoFile
from textrepo_client.model.form_type import FormType
from textrepo_client.model.form_version import FormVersion
from textrepo_client.model.result_document import ResultDocument
from textrepo_client.model.result_documents_overview import ResultDocumentsOverview
from textrepo_client.model.result_page import ResultPage
from textrepo_client.model.result_page_params import ResultPageParams
from textrepo_client.model.result_page_result_document import ResultPageResultDocument
from textrepo_client.model.result_text_repo_file import ResultTextRepoFile
from textrepo_client.model.result_version import ResultVersion
