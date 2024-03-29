# config/management/commands/create_index.py

from django.core.management.base import BaseCommand
from elasticsearch_dsl import connections
from src.establishment.search_indexes import EstablishmentIndex
import warnings
from elasticsearch.exceptions import ElasticsearchWarning

warnings.simplefilter("ignore", ElasticsearchWarning)
connections.create_connection(alias='default', hosts=['http://localhost:9200'])

EstablishmentIndex._index.delete(ignore=404)
EstablishmentIndex.init()

class Command(BaseCommand):
    help = "Creates the Elasticsearch index"

    def handle(self, *args, **options):
        # No need to create the connection again here, as it's already created above.
        EstablishmentIndex.init()
