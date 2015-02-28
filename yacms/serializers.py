from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division
from __future__ import absolute_import

from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import serializers

from yacms.models import CMSContents
from yacms.models import CMSMarkUps
from yacms.models import CMSTemplates
from yacms.models import CMSPageTypes
from yacms.models import CMSEntries



class CMSPageTypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CMSPageTypes
        fields = ('id','page_type','text','view_class')
        
class CMSContentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CMSContents
        fields = ('id', 'content', 'timestamp', 'markup')
         
class CMSMarkUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = CMSMarkUps
        fields = ('id','markup')
        
class CMSTemplatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CMSTemplates
        fields = ('id','name', 'template')
        
class CMSEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = CMSEntries
        fields = ('id','title','path','slug','content','date_created',
                  'page_type','template','frontpage','published',
                  'meta_description','page_number')