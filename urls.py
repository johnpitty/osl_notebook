from django.conf.urls.defaults import *
from notebook.notes.models import Note, Tag

from django.contrib import databrowse

from django.views.generic import list_detail

from env_settings import MEDIA_ROOT, DB_ROOT

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

import settings
import os
import imp
#import postman

#databrowse.site.register(Note)
#databrowse.site.register(Tag)

#import django_cron
#django_cron.autodiscover()

urlpatterns = patterns('',
    # Example:
    #(r'^notebook/', include('notebook.foo.urls')),
     
    (r'^messages/', include('postman.urls')),

    (r'^notification/', include('notification.urls')),

    (r'^getNotices/', 'notebook.notes.views.get_notices'),
   

    (r'^$','notebook.notes.views.root'),
    (r'^myadmin/doc/', include('django.contrib.admindocs.urls')),
    (r'^myadmin/', include('notebook.notes.admin.urls')),

    #TODO: maybe all urls for adding and updating shouldn't have a username in the url, and 
    #should get it from the request 
    (r'^user/bookmarkbook/bookmarks/addBookmark/', 'notebook.bookmarks.views.add_bookmark'), #for the add bookmark browser button 
    (r'^user/scrapbook/scraps/addScrap/', 'notebook.scraps.views.add_scrap'),  #for the add scrap browser button    

    #(r'^users/(?P<username>[^/]+)/$', 'notebook.social.views.wall'),
    (r'^social/(?P<username>[^/]+)/$', 'notebook.social.views.profile'),
    (r'^social/(?P<username>[^/]+)/addFriend/$', 'notebook.social.views.add_friend'),

#below seem not used
    #(r'^users/(?P<username>[^/]+)/wall/snippets/$', 'notebook.social.views.wall_snippets'),
    #(r'^users/(?P<username>[^/]+)/wall/bookmarks/$', 'notebook.social.views.wall_bookmarks'),
    #(r'^users/(?P<username>[^/]+)/wall/scraps/$', 'notebook.social.views.wall_scraps'),
    (r'^groups/(?P<groupname>[^/]+)/$', 'notebook.social.views.group_index'),

    (r'^groups/(?P<groupname>[^/]+)/joinGroup/$', 'notebook.social.views.join_group'),
    (r'^groups/(?P<groupname>[^/]+)/admin/$', 'notebook.social.views.group_admin'),
    (r'^groups/(?P<groupname>[^/]+)/admin/deleteMember/$', 'notebook.social.views.group_delete_member'),
    (r'^groups/(?P<groupname>[^/]+)/admin/addTags2Group/$', 'notebook.social.views.group_add_tags'),
    (r'^groups/(?P<groupname>[^/]+)/admin/removeTagFromGroup/$', 'notebook.social.views.group_remove_tag'),
    (r'^groups/(?P<groupname>[^/]+)/admin/updateGroup/$', 'notebook.social.views.update_group'),


    #(r'^groups/(?P<groupname>[^/]+)/snippets/$', 'notebook.social.views.group_snippets'),
    (r'^groups/(?P<groupname>[^/]+)/(?P<bookname>[^/]+)/notes/$', 'notebook.social.views.group'),
    #(r'^groups/(?P<groupname>[^/]+)/(?P<bookname>[^/]+)/notes/note/(?P<note_id>[^/]+)/$', 'notebook.social.views.note'),
    (r'^groups/(?P<groupname>[^/]+)/(?P<bookname>[^/]+)/tags/(?P<tag_name>[^/]+)/$','notebook.social.views.group_tag'),



    #TODO: distinguish btw social notes and notes when merging snippets/bookmarks/scraps back here
    #TODO: better regex
    (r'^groups/[^/]+/[^/]+/addComment/$', 'notebook.social.views.add_comment'),
    (r'^social/.+/addComment/$', 'notebook.social.views.add_comment'),
    (r'^social/.+/addCourse/$', 'notebook.social.views.add_course'),
    (r'^social/.+/deleteOuterlink/$', 'notebook.social.views.delete_outer_link'),
    (r'^social/.+/deleteCourse/$', 'notebook.social.views.delete_course'),

     (r'/friends/.+/notes/addComment/$', 'notebook.social.views.add_comment'),
    (r'^social/(?P<username>[^/]+)/commentsfor/$', 'notebook.social.views.comments_4_user'),
    (r'^social/(?P<username>[^/]+)/commentsby/$', 'notebook.social.views.comments_by_user'),
    #for now, no deleting of social comments TODO:
    (r'^groups/[^/]+/[^/]+/deleteComment/$','notebook.social.views.delete_comment'),
    (r'^social/.+/deleteComment/$','notebook.social.views.delete_comment'),
    #for now, still keep share in notes.views instead of moving to social.views (If moving, might need to move sites binding together) TODO: 
    (r'^social/(?P<bookname>[^/]+)/share/$','notebook.notes.views.share'),

    (r'/voteUseful/$','notebook.social.views.vote_useful'), 
    (r'/voteUnuseful/$','notebook.social.views.vote_unuseful'), 
    (r'/take/$','notebook.social.views.take'), 

    (r'^(?P<username>[^/]+)/groups/$', 'notebook.social.views.groups'),
    (r'^(?P<username>[^/]+)/groups/addGroup$', 'notebook.social.views.groups'),
    (r'^(?P<username>[^/]+)/friends/$', 'notebook.social.views.friends'),
    (r'^suggest/$', 'notebook.social.views.suggest'),
    (r'^(?P<username>[^/]+)/friends/(?P<bookname>[^/]+)/notes/$', 'notebook.social.views.friends_notes2'), 
    (r'^(?P<username>[^/]+)/groups/(?P<bookname>[^/]+)/notes/$', 'notebook.social.views.groups_notes'),
    (r'^(?P<username>[^/]+)/groups/(?P<bookname>[^/]+)/$', 'notebook.social.views.groups_notes'),

    (r'^social/(?P<username>[^/]+)/(?P<bookname>[^/]+)/$', 'notebook.social.views.notes'),
    (r'^social/(?P<username>[^/]+)/(?P<bookname>[^/]+)/notes/$', 'notebook.social.views.notes'),
    (r'^social/(?P<username>[^/]+)/(?P<bookname>[^/]+)/notes/note/(?P<note_id>[^/]+)/$','notebook.social.views.note'),
    (r'^social/(?P<username>[^/]+)/(?P<bookname>[^/]+)/tags/(?P<tag_name>[^/]+)/$', 'notebook.social.views.notes_tag'),
    #might delete this one or the above one
    (r'^social/(?P<username>[^/]+)/(?P<bookname>[^/]+)/notes/tags/(?P<tag_name>[^/]+)/$', 'notebook.social.views.notes_tag'),
    (r'^social/(?P<username>[^/]+)/(?P<bookname>[^/]+)/folders/(?P<foldername>[^/]+)/$', 'notebook.social.views.folders'),


 

   #TODO:put tagframe at front, since it doesn't distinguis btw personal and public book. For example /tagframe/username/...
    (r'^(?P<username>[^/]+)/tagframe/$', 'notebook.tags.views.index'),
   # (r'^(?P<username>[^/]+)/tagframe/addTagFrame/$', 'notebook.tags.views.add_tag_frame'),
    (r'^(?P<username>[^/]+)/tagframe/addTags2Frame/$', 'notebook.tags.views.add_tags_2_frame'),
    (r'^(?P<username>[^/]+)/tagframe/removeFrame/$', 'notebook.tags.views.remove_frame'),
    (r'^(?P<username>[^/]+)/tagframe/deleteFrame/$', 'notebook.tags.views.delete_frame'),
    
    (r'^(?P<username>[^/]+)/tagframe/(?P<tag_path>[^/]+)/(?P<bookname>[^/]+)/notes/$', 'notebook.tags.views.notes_by_tag'),
    (r'^(?P<username>[^/]+)/tagframe/getRelatedTags/$','notebook.tags.views.get_related_tags'),  
    (r'^(?P<username>[^/]+)/tagframe/export/$','notebook.tags.views.export'),  


    #below dupldate a lot with patterns in 'notebook.notes.urls', refactor TODO:
    (r'^(?P<username>[^/]+)/tagframe/(.*)/(?P<bookname>[^/]+)/notes/updateNoteInline/$','notebook.notes.views.update_note_inline'),
    (r'^(?P<username>[^/]+)/tagframe/(.*)/(?P<bookname>[^/]+)/notes/updateNoteTagsInline/$','notebook.notes.views.update_note_tags_inline'),
    (r'^(?P<username>[^/]+)/tagframe/(.*)/(?P<bookname>[^/]+)/notes/addComment/$','notebook.notes.views.add_comment'),
    (r'^(?P<username>[^/]+)/tagframe/(.*)/(?P<bookname>[^/]+)/notes/deleteComment/$','notebook.notes.views.delete_comment'),
    (r'^(?P<username>[^/]+)/tagframe/(.*)/(?P<bookname>[^/]+)/notes/makePrivate/$','notebook.notes.views.make_private'),
    (r'^(?P<username>[^/]+)/tagframe/(.*)/(?P<bookname>[^/]+)/notes/makePublic/$','notebook.notes.views.make_public'),
    
    (r'^(?P<username>[^/]+)/tagframe/(.*)/(?P<bookname>[^/]+)/notes/voteUpNote/$','notebook.notes.views.vote_up_note'), 
    (r'^(?P<username>[^/]+)/tagframe/(.*)/(?P<bookname>[^/]+)/notes/voteDownNote/$','notebook.notes.views.vote_down_note'),
    (r'^(?P<username>[^/]+)/tagframe/(.*)/(?P<bookname>[^/]+)/notes/deleteNote/$','notebook.notes.views.delete_note'),
    (r'^(?P<username>[^/]+)/tagframe/(.*)/(?P<bookname>[^/]+)/notes/addNote/$','notebook.notes.views.add_note'),  
    (r'^(?P<username>[^/]+)/tagframe/(.*)/(?P<bookname>[^/]+)/notes/addTags2Notes2/$','notebook.notes.views.add_tags_to_notes2'),
    (r'^(?P<username>[^/]+)/tagframe/(.*)/(?P<bookname>[^/]+)/notes/removeTagsFromNotes2/$','notebook.notes.views.remove_tags_from_notes2'),

  

   #TODO: seems to be matching too many things 
    (r'^(?P<username>[^/]+)/(?P<bookname>[^/]+)/',include('notebook.notes.urls')),


   # (r'^(?P<username>[^/]+)/notebook/',include('notebook.notes.urls')),
   # (r'^(?P<username>[^/]+)/snippetbook/',include('notebook.snippets.urls')),
   # (r'^(?P<username>[^/]+)/bookmarkbook/',include('notebook.bookmarks.urls')),
   # (r'^(?P<username>[^/]+)/scrapbook/',include('notebook.scraps.urls')),

    (r'settings/setAdvanced$', 'notebook.notes.views.settings_set_advanced'),
    (r'settings/updateProfile/$', 'notebook.notes.views.settings_update_profile'),
    (r'settings/$', 'notebook.notes.views.settings'),
    (r'settings/tags/$', 'notebook.notes.views.settings_tags'),
    (r'settings/tags/updateTagName/$', 'notebook.notes.views.update_tag_name'),
    (r'settings/tags/tag/(?P<tag_name>[^/]+)/$', 'notebook.notes.views.settings_tag'),
    (r'settings/tags/tag/(?P<tag_name>[^/]+)/updateTag/$', 'notebook.notes.views.settings_tag_update'),
    (r'settings/tags/addTag/$', 'notebook.notes.views.settings_tag_add'),
    (r'settings/tags/deleteTag/$', 'notebook.notes.views.delete_tag'),
    
    (r'settings/tags/addTags2WSs/$', 'notebook.notes.views.settings_add_tags_2_wss2'),
    
    (r'settings/tags/removeTagsFromWSs/$', 'notebook.notes.views.settings_remove_tags_from_wss2'),

    #(r'settings/workingsets/addTags2WSs/$', 'notebook.notes.views.settings_add_tags_2_wss'),
    (r'settings/workingsets/addTags2WSs2/$', 'notebook.notes.views.settings_add_tags_2_wss2'),
    #(r'settings/workingsets/removeTagsFromWSs/$', 'notebook.notes.views.settings_remove_tags_from_wss'),
    (r'settings/workingsets/removeTagsFromWSs2/$', 'notebook.notes.views.settings_remove_tags_from_wss2'),

    (r'settings/workingsets/$', 'notebook.notes.views.settings_workingsets'),
    (r'settings/workingsets/addWS/$', 'notebook.notes.views.settings_workingset_add'),
    (r'settings/workingsets/updateWSInline/$', 'notebook.notes.views.settings_workingset_update_inline'),

    (r'settings/workingsets/workingset/(?P<ws_name>[^/]+)/$', 'notebook.notes.views.settings_workingset'),
    (r'settings/workingsets/workingset/(?P<ws_name>[^/]+)/updateWS/$', 'notebook.notes.views.settings_workingset_update'),
    (r'^deleteWS/$', 'notebook.notes.views.settings_workingset_delete'),   

    (r'settings/bind/$', 'notebook.notes.views.bind'),
    (r'settings/bind/requestAuth$', 'notebook.notes.views.bind_request_auth'),
    (r'settings/bindCheck$', 'notebook.notes.views.bind_check'),
    (r'settings/bind/removeAuth$', 'notebook.notes.views.bind_remove_auth'),

    (r'login/$', 'django.contrib.auth.views.login'),
    (r'^loginUser/$', 'notebook.notes.views.login_user'), 
    (r'^logout/$', 'notebook.notes.views.logout_view'),
    (r'^passwordChange/$', 'django.contrib.auth.views.password_change'),
    (r'^passwordChanged/$', 'django.contrib.auth.views.password_change_done'),

    (r'registre/$', 'notebook.notes.views.register_user'),

    (r'^setLang/$', 'notebook.notes.views.set_language'),

    (r'/toggleShowNotesMode/$','notebook.notes.views.toggle_show_notes_mode'),
    (r'/toggleShowCachesMode/$','notebook.notes.views.toggle_show_caches_mode'),
    (r'/toggleAddNoteMode/$','notebook.notes.views.toggle_add_note_mode'),

 
    (r'/importBookmark/$','notebook.bookmarks.views.import_bookmark'),

    (r'^forNewUsers/$','notebook.notes.views.for_new_users'),
    (r'^about$','notebook.notes.views.about'),

    (r'^test','notebook.notes.views.test'),


    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    
    (r'^admin/', include(admin.site.urls)),
    

    (r'^databrowse/(.*)', databrowse.site.root),

    (r'^site_media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': MEDIA_ROOT}),

    (r'^file/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': DB_ROOT}),

)
