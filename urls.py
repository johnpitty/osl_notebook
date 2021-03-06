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
    (r'^social/(?P<username>[^/]+)/removeFriend/$', 'notebook.social.views.remove_friend'),

#below seem not used
    #(r'^users/(?P<username>[^/]+)/wall/snippets/$', 'notebook.social.views.wall_snippets'),
    #(r'^users/(?P<username>[^/]+)/wall/bookmarks/$', 'notebook.social.views.wall_bookmarks'),
    #(r'^users/(?P<username>[^/]+)/wall/scraps/$', 'notebook.social.views.wall_scraps'),
    (r'^groups/(?P<groupid>[^/]+)/$', 'notebook.social.views.group_index'),
    (r'^groups/(?P<groupid>[^/]+)/tagframes/$', 'notebook.social.views.group_tagframes'),
    (r'^groups/(?P<groupid>[^/]+)/salons/$', 'notebook.salons.views.group_salons'),
    (r'^groups/(?P<groupid>[^/]+)/salons/salon/(?P<salon_id>[^/]+)/$', 'notebook.salons.views.group_salon'),
    (r'^groups/(?P<groupid>[^/]+)/salons/salon/(?P<salon_id>[^/]+)/signup/$', 'notebook.salons.views.group_salon_signup'),

    (r'^groups/(?P<groupid>[^/]+)/joinGroup/$', 'notebook.social.views.join_group'),
    (r'^groups/(?P<groupid>[^/]+)/admin/$', 'notebook.social.views.group_admin'),
    (r'^groups/(?P<groupid>[^/]+)/admin/deleteMember/$', 'notebook.social.views.group_delete_member'),
    (r'^groups/(?P<groupid>[^/]+)/admin/addTags2Group/$', 'notebook.social.views.group_add_tags'),
    (r'^groups/(?P<groupid>[^/]+)/admin/removeTagFromGroup/$', 'notebook.social.views.group_remove_tag'),
    (r'^groups/(?P<groupid>[^/]+)/admin/updateGroup/$', 'notebook.social.views.update_group'),
    (r'^groups/(?P<groupid>[^/]+)/admin/addUsers2Group/$', 'notebook.social.views.group_add_users'),
    (r'^groups/(?P<groupid>[^/]+)/admin/inviteUsers2Group/$', 'notebook.social.views.group_invite_users'),

    (r'^groups/$', 'notebook.social.views.groups'),

    (r'^learners/$', 'notebook.social.views.learners'),
 
    (r'^people/$', 'notebook.social.views.people'),

    (r'^salons/$', 'notebook.salons.views.salons'),
    (r'^(?P<username>[^/]+)/salons/$', 'notebook.salons.views.my_salons'),


    #(r'^groups/(?P<groupid>[^/]+)/snippets/$', 'notebook.social.views.group_snippets'),
    (r'^groups/(?P<groupid>[^/]+)/(?P<bookname>[^/]+)/notes/$', 'notebook.social.views.group'),
    #(r'^groups/(?P<groupid>[^/]+)/(?P<bookname>[^/]+)/notes/note/(?P<note_id>[^/]+)/$', 'notebook.social.views.note'),
    (r'^groups/(?P<groupid>[^/]+)/(?P<bookname>[^/]+)/tags/(?P<tag_name>[^/]+)/$','notebook.social.views.group_tag'),



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


    (r'^social/(?P<username>[^/]+)/mentioned/$', 'notebook.social.views.mentioned'),
    (r'^social/(?P<username>[^/]+)/mentioned_in_note/$', 'notebook.social.views.mentioned_in_note'),
    (r'^social/(?P<username>[^/]+)/mentioned_in_comment/$', 'notebook.social.views.mentioned_in_comment'),

    (r'/voteUseful/$','notebook.social.views.vote_useful'), 
    (r'/voteUnuseful/$','notebook.social.views.vote_unuseful'), 
    (r'/take/$','notebook.social.views.take'), 

    (r'^(?P<username>[^/]+)/addNoteOnly/$', 'notebook.notes.views.add_note_only'),

    (r'^(?P<username>[^/]+)/groups/$', 'notebook.social.views.my_groups'),
    (r'^(?P<username>[^/]+)/groups/addGroup$', 'notebook.social.views.my_groups'),
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

    (r'^social/(?P<username>[^/]+)/(?P<bookname>[^/]+)/notes/note/(?P<note_id>[^/]+)/getRelatedFrames/$','notebook.social.views.get_related_frames'),
 

    (r'^all/(?P<bookname>[^/]+)/notes/$', 'notebook.social.views.all_notes'), 

   #TODO:put tagframes at front, since it doesn't distinguis btw personal and public book. For example /tagframes/username/...
    (r'^(?P<username>[^/]+)/tagframes/$', 'notebook.tags.views.index'),
   # (r'^(?P<username>[^/]+)/tagframes/addTagFrame/$', 'notebook.tags.views.add_tag_frame'),
    (r'^(?P<username>[^/]+)/tagframes/addTags2Frame/$', 'notebook.tags.views.add_tags_2_frame'),
    (r'^(?P<username>[^/]+)/tagframes/removeFrame/$', 'notebook.tags.views.remove_frame'),
    (r'^(?P<username>[^/]+)/tagframes/deleteFrame/$', 'notebook.tags.views.delete_frame'),
    
    (r'^(?P<username>[^/]+)/tagframes/(?P<tag_path>[^/]+)/(?P<bookname>[^/]+)/notes/$', 'notebook.tags.views.notes_by_tag'),
    (r'^social/(?P<username>[^/]+)/tagframes/(?P<tag_path>[^/]+)/(?P<bookname>[^/]+)/notes/$', 'notebook.tags.views.social_notes_by_tag'),
    (r'^(?P<username>[^/]+)/tagframes/getRelatedTags/$','notebook.tags.views.get_related_tags'),  
    (r'^(?P<username>[^/]+)/tagframes/export/$','notebook.tags.views.export'),  


    #below dupldate a lot with patterns in 'notebook.notes.urls', refactor TODO:
    (r'^(?P<username>[^/]+)/tagframes/(.*)/(?P<bookname>[^/]+)/notes/updateNoteInline/$','notebook.notes.views.update_note_inline'),
    (r'^(?P<username>[^/]+)/tagframes/(.*)/(?P<bookname>[^/]+)/notes/updateNoteTagsInline/$','notebook.notes.views.update_note_tags_inline'),
    (r'^(?P<username>[^/]+)/tagframes/(.*)/(?P<bookname>[^/]+)/notes/addComment/$','notebook.notes.views.add_comment'),
    (r'^(?P<username>[^/]+)/tagframes/(.*)/(?P<bookname>[^/]+)/notes/deleteComment/$','notebook.notes.views.delete_comment'),
    (r'^(?P<username>[^/]+)/tagframes/(.*)/(?P<bookname>[^/]+)/notes/makePrivate/$','notebook.notes.views.make_private'),
    (r'^(?P<username>[^/]+)/tagframes/(.*)/(?P<bookname>[^/]+)/notes/makePublic/$','notebook.notes.views.make_public'),
    
    (r'^(?P<username>[^/]+)/tagframes/(.*)/(?P<bookname>[^/]+)/notes/voteUpNote/$','notebook.notes.views.vote_up_note'), 
    (r'^(?P<username>[^/]+)/tagframes/(.*)/(?P<bookname>[^/]+)/notes/voteDownNote/$','notebook.notes.views.vote_down_note'),
    (r'^(?P<username>[^/]+)/tagframes/(.*)/(?P<bookname>[^/]+)/notes/deleteNote/$','notebook.notes.views.delete_note'),
    (r'^(?P<username>[^/]+)/tagframes/(.*)/(?P<bookname>[^/]+)/notes/addNote/$','notebook.notes.views.add_note'),  
    (r'^(?P<username>[^/]+)/tagframes/(.*)/(?P<bookname>[^/]+)/notes/addTags2Notes2/$','notebook.notes.views.add_tags_to_notes2'),
    (r'^(?P<username>[^/]+)/tagframes/(.*)/(?P<bookname>[^/]+)/notes/removeTagsFromNotes2/$','notebook.notes.views.remove_tags_from_notes2'),

    (r'^(?P<username>[^/]+)/tagframes/tagframe/(?P<tagframe_name>[^/]+)/$','notebook.tags.views.tagframe'),
    (r'^(?P<username>[^/]+)/tagframes/tagframe/(?P<tagframe_name>[^/]+)/pushTagFrame2Groups/$','notebook.tags.views.push_tag_frame_2_groups'),


    (r'^areas/$', 'notebook.areas.views.index'),

    (r'^(?P<username>[^/]+)/areas/$', 'notebook.areas.views.my_areas'),
    (r'^(?P<username>[^/]+)/areas/area/(?P<area_id>[^/]+)/$', 'notebook.areas.views.area'),
    (r'^(?P<username>[^/]+)/areas/area/(?P<areaname>[^/]+)/(?P<bookname>[^/]+)/notes/$', 'notebook.areas.views.area_notes'),
    (r'^(?P<username>[^/]+)/areas/area/(?P<areaname>[^/]+)/(?P<bookname>[^/]+)/getAreaTags/$', 'notebook.areas.views.get_area_tags'),
    (r'^(?P<username>[^/]+)/areas/area/(?P<areaname>[^/]+)/addGroups2Area/$', 'notebook.areas.views.add_groups_2_area'),
    (r'^(?P<username>[^/]+)/areas/area/(?P<areaname>[^/]+)/removeGroupFromArea/$', 'notebook.areas.views.remove_group_from_area'),

    (r'^(?P<username>[^/]+)/(.*)/addQuestion/$', 'notebook.notes.views.add_question'),
    (r'^(?P<username>[^/]+)/(.*)/addProject/$', 'notebook.notes.views.add_project'),


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

    #(r'login/$', 'django.contrib.auth.views.login'),
    (r'login/$', 'notebook.notes.views.login'),
    (r'^loginUser/$', 'notebook.notes.views.login_user'), 
    (r'^logout/$', 'notebook.notes.views.logout_view'),
    (r'^passwordChange/$', 'django.contrib.auth.views.password_change'),
    (r'^passwordChanged/$', 'django.contrib.auth.views.password_change_done'),





    (r'registre/$', 'notebook.notes.views.register_user'),

    (r'reg/$', 'notebook.notes.views.user_register'),
    (r'invite/$', 'notebook.notes.views.user_register_with_code'),
    (r'activate/$', 'notebook.notes.views.activate'),
    (r'supera/$', 'notebook.notes.views.super_admin'),

    (r'switchui/$', 'notebook.notes.views.switch_ui'),


    (r'^setLang/$', 'notebook.notes.views.set_language'),

    (r'/toggleShowNotesMode/$','notebook.notes.views.toggle_show_notes_mode'),
    (r'/toggleShowCachesMode/$','notebook.notes.views.toggle_show_caches_mode'),
    (r'/toggleAddNoteMode/$','notebook.notes.views.toggle_add_note_mode'),

 
    (r'/importBookmark/$','notebook.bookmarks.views.import_bookmark'),

    (r'^forNewUsers/$','notebook.notes.views.for_new_users'),
    (r'^about$','notebook.notes.views.about'),
    (r'^doc/$','notebook.notes.views.doc'),
    (r'^faq/$','notebook.notes.views.faq'),
    (r'^mobile/$','notebook.notes.views.mobile'),
    (r'^results/$','notebook.notes.views.results'),
    (r'^changeYourBroswer/$','notebook.notes.views.change_your_broswer'),
    (r'^whoami/$','notebook.notes.views.whoami'),


    (r'^test','notebook.notes.views.test'),


    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    
    #defaultsystemadmin
    (r'^dsysadmin/', include(admin.site.urls)),
    

    (r'^databrowse/(.*)', databrowse.site.root),

    (r'^site_media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': MEDIA_ROOT}),

    (r'^file/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': DB_ROOT}),

)

from django.contrib.auth import views as auth_views

urlpatterns+=(
url(r'^passreset/$',auth_views.password_reset,name='forgot_password1'),
url(r'^passresetdone/$',auth_views.password_reset_done,name='forgot_password2'),
url(r'^passresetconfirm/(?P<uidb36>[-\w]+)/(?P<token>[-\w]+)/$',auth_views.password_reset_confirm,name='forgot_password3'),
url(r'^passresetcomplete/$',auth_views.password_reset_complete,name='forgot_password4'),
)
