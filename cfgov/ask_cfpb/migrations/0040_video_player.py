# Generated by Django 2.2.12 on 2020-06-05 15:30

from django.db import migrations
import v1.atomic_elements.organisms
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks

import logging
import re

from v1.util.migrations import migrate_page_types_and_fields


logger = logging.getLogger(__name__)


# This is a reasonable but not official regex for YouTube video IDs.
# https://webapps.stackexchange.com/a/54448
YOUTUBE_EMBED = re.compile(r'^https:\/\/www\.youtube\.com\/embed\/([\w-]+)')


def mapper(page_or_revision, value):
    video_url = value.get('video_url')

    if video_url:
        match = YOUTUBE_EMBED.match(video_url)

        if match:
            value['video_id'] = match.group(1)
            logger.debug('%s: %s -> %s' % (
                page_or_revision,
                video_url,
                value['video_id'],
            ))

    return value


def migrate_forwards(apps, schema_editor):
    migrate_page_types_and_fields(
        apps,
        [
            ('ask_cfpb', 'AnswerPage', 'answer_content', 'video_player'),
            ('ask_cfpb', 'AnswerPage', 'answer_content', (
                'faq_schema',
                'questions',
                'answer_content',
                'video_player',
            )),
            ('ask_cfpb', 'AnswerPage', 'answer_content', (
                'how_to_schema',
                'steps',
                'step_content',
                'video_player',
            )),
        ],
        mapper
    )


def migrate_backwards(apps, schema_editor):
    raise NotImplementedError


class Migration(migrations.Migration):

    dependencies = [
        ('ask_cfpb', '0039_add_title_to_howto_block'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answerpage',
            name='answer_content',
            field=wagtail.core.fields.StreamField([('text', wagtail.core.blocks.StructBlock([('content', wagtail.core.blocks.RichTextBlock(features=['bold', 'italic', 'h2', 'h3', 'link', 'ol', 'ul', 'document-link', 'image', 'embed'], label='Text'))])), ('table_block', v1.atomic_elements.organisms.AtomicTableBlock(table_options={'renderer': 'html'})), ('tip', wagtail.core.blocks.StructBlock([('content', wagtail.core.blocks.RichTextBlock(features=['link', 'document-link'], label='Tip'))])), ('video_player', wagtail.core.blocks.StructBlock([('video_id', wagtail.core.blocks.RegexBlock(error_messages={'invalid': 'The YouTube video ID is in the wrong format.'}, help_text='Enter the YouTube video ID, which is located at the end of the video URL, after "v=". For example, the video ID for https://www.youtube.com/watch?v=1V0Ax9OIc84 is 1V0Ax9OIc84.', label='YouTube video ID', regex='^[\\w-]{11}$', required=False)), ('thumbnail_image', wagtail.images.blocks.ImageChooserBlock(help_text='Optional thumbnail image to show before or after the video plays.', required=False))])), ('how_to_schema', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(max_length=500)), ('description', wagtail.core.blocks.RichTextBlock(blank=True, features=['ol', 'ul', 'bold', 'italic', 'link', 'document-link'], required=False)), ('steps', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(max_length=500)), ('step_content', wagtail.core.blocks.StreamBlock([('text', wagtail.core.blocks.StructBlock([('content', wagtail.core.blocks.RichTextBlock(features=['bold', 'italic', 'h3', 'link', 'ol', 'ul', 'document-link', 'image', 'embed'], label='Text'))])), ('table_block', v1.atomic_elements.organisms.AtomicTableBlock(table_options={'renderer': 'html'})), ('tip', wagtail.core.blocks.StructBlock([('content', wagtail.core.blocks.RichTextBlock(features=['link', 'document-link'], label='Tip'))])), ('video_player', wagtail.core.blocks.StructBlock([('video_id', wagtail.core.blocks.RegexBlock(error_messages={'invalid': 'The YouTube video ID is in the wrong format.'}, help_text='Enter the YouTube video ID, which is located at the end of the video URL, after "v=". For example, the video ID for https://www.youtube.com/watch?v=1V0Ax9OIc84 is 1V0Ax9OIc84.', label='YouTube video ID', regex='^[\\w-]{11}$', required=False)), ('thumbnail_image', wagtail.images.blocks.ImageChooserBlock(help_text='Optional thumbnail image to show before or after the video plays.', required=False))]))]))])))])), ('faq_schema', wagtail.core.blocks.StructBlock([('description', wagtail.core.blocks.RichTextBlock(blank=True, features=['ol', 'ul', 'bold', 'italic', 'link', 'document-link'], required=False)), ('questions', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('question', wagtail.core.blocks.CharBlock(max_length=500)), ('answer_content', wagtail.core.blocks.StreamBlock([('text', wagtail.core.blocks.StructBlock([('content', wagtail.core.blocks.RichTextBlock(features=['bold', 'italic', 'h3', 'link', 'ol', 'ul', 'document-link', 'image', 'embed'], label='Text'))])), ('table_block', v1.atomic_elements.organisms.AtomicTableBlock(table_options={'renderer': 'html'})), ('tip', wagtail.core.blocks.StructBlock([('content', wagtail.core.blocks.RichTextBlock(features=['link', 'document-link'], label='Tip'))])), ('video_player', wagtail.core.blocks.StructBlock([('video_id', wagtail.core.blocks.RegexBlock(error_messages={'invalid': 'The YouTube video ID is in the wrong format.'}, help_text='Enter the YouTube video ID, which is located at the end of the video URL, after "v=". For example, the video ID for https://www.youtube.com/watch?v=1V0Ax9OIc84 is 1V0Ax9OIc84.', label='YouTube video ID', regex='^[\\w-]{11}$', required=False)), ('thumbnail_image', wagtail.images.blocks.ImageChooserBlock(help_text='Optional thumbnail image to show before or after the video plays.', required=False))]))]))])))]))], blank=True, verbose_name='Answer'),
        ),
        migrations.RunPython(migrate_forwards, migrate_backwards),
    ]
