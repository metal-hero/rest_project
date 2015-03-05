from tastypie.resources import ModelResource
from question.models import *
from tastypie.authorization import Authorization
from tastypie import fields


class QuestionResource(ModelResource):
	text = fields.CharField(attribute="text", use_in="list")
	is_public = fields.BooleanField(attribute="is_public", use_in="detail")

	class Meta:
		queryset = Question.objects.all()
		resource_name = 'question'
		authorization = Authorization()
		always_return_data = True
