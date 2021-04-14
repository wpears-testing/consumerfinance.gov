# Generated by Django 2.2.16 on 2021-04-07 15:47

from django.db import migrations

# This is a temporary fix for an inconsistency between the expected state of
# the wagtailembeds_embed table constrains and its actual state. This
# manifests as a failure of the wagtailembeds_0008_allow_long_urls migration
# to apply.
#
# Once this migration has successfully run, the function below will be
# removed and this migration will become a noop.
def forwards(apps, schema_editor):
    # Check that the index we're interested in exists
    with schema_editor.connection.cursor() as cursor:
        cursor.execute(
           "SELECT COUNT(*) FROM pg_indexes "
            "WHERE tablename = 'wagtailembeds_embed' and "
            "indexname = 'idx_17439_wagtailembeds_embed_url_37a13a49926a4846_uniq';"
        )
        count = cursor.fetchone()[0]

    if count == 0:
        return

    schema_editor.execute("""
BEGIN;
DROP INDEX IF EXISTS "idx_17439_wagtailembeds_embed_url_37a13a49926a4846_uniq";
ALTER TABLE "wagtailembeds_embed" ADD CONSTRAINT "wagtailembeds_embed_url_max_width_8a2922d8_uniq" UNIQUE ("url", "max_width");
COMMIT;""")


class Migration(migrations.Migration):

    dependencies = [
        ('v1', '0254_delete_homepagecarouselitem'),
    ]

    run_before = [
        ('wagtailembeds', '0008_allow_long_urls'),
    ]

    operations = [
        migrations.RunPython(forwards, atomic=True),
    ]