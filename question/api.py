from tastypie.resources import ModelResource
from question.models import *


class QuestionResource(ModelResource):
	class Meta:
		queryset = module.Question.objects.all()
		resource.name = 'question'