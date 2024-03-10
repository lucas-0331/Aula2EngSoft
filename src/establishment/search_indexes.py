from elasticsearch_dsl import Document, Text, Long
from elasticsearch_dsl.connections import connections
from .models import Establishment

connection_alias = "default"
connections.create_connection(alias=connection_alias, hosts=["http://localhost:9200"])

class EstablishmentIndex(Document):
    establishment_id = Long()
    establishment_name = Text()

    class Index:
        index_name = "establishment_index"
        name = index_name


def index_data_view():
    try:
        for establishment_obj in Establishment.objects.all():
            establishment_instance = EstablishmentIndex(
                meta={"id": establishment_obj.establishment_id},
                establishment_id=establishment_obj.establishment_id,
                establishment_name=establishment_obj.establishment_name,
            )

            establishment_instance.save(using=connection_alias)
    except:
        pass