# Generated by Django 5.2.1 on 2025-06-18 12:46

from django.apps import apps as registry
from django.db import migrations
from django.db.models.signals import post_migrate

from ...core.search_tasks import set_order_search_document_values


def update_order_search_vector(apps, _schema_editor):
    def on_migrations_complete(sender=None, **kwargs):
        set_order_search_document_values.delay()

    sender = registry.get_app_config("order")
    post_migrate.connect(on_migrations_complete, weak=False, sender=sender)


class Migration(migrations.Migration):
    dependencies = [
        ("order", "0212_orderline_product_type_id_btree_idx"),
    ]

    operations = [
        migrations.RunPython(
            update_order_search_vector,
            reverse_code=migrations.RunPython.noop,
        )
    ]
