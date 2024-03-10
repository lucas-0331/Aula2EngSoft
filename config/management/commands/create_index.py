from django.core.management.base import BaseCommand
from elasticsearch_dsl import connections
from src.establishment.search_indexes import EstablishmentIndex
import warnings
from elasticsearch.exceptions import ElasticsearchWarning

warnings.simplefilter("ignore", ElasticsearchWarning)
EstablishmentIndex._index.delete(ignore=404)
EstablishmentIndex.init()


class Command(BaseCommand):
    help = "Creates the Elasticsearch index"

    def handle(self, *args, **options):
        connections.create_connection(hosts=["http://localhost:9200"], timeout=20)
        EstablishmentIndex.init()
