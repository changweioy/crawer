# -*- coding: utf-8 -*-

# Scrapy settings for note_book project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'note_book'

SPIDER_MODULES = ['note_book.spiders']
NEWSPIDER_MODULE = 'note_book.spiders'
ITEM_PIPELINES=['note_book.pipelines_note_book.NoteBookPipeline']
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'note_book (+http://www.yourdomain.com)'
