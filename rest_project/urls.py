from django.conf.urls import patterns, include, url
from django.contrib import admin

from question.api import *

question_resource = QuestionResource() 
post_resource = PostResource()
comment_resource = CommentResource()

urlpatterns = patterns('',
  # Examples:
  # url(r'^$', 'rest_project.views.home', name='home'),
  # url(r'^blog/', include('blog.urls')),

  url(r'^admin/', include(admin.site.urls)),
  url(r'^api/v1/', include(question_resource.urls)),
  url(r'^api/v2/', include(post_resource.urls)),
  url(r'^api/v2/', include(comment_resource.urls)),
)
