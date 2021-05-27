from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^display_Amino$', display_Amino, name='display_amino'),
    url(r'^display_Bcaa$', display_Bcaa, name='display_bcaa'),
    url(r'^display_Beta$', display_Beta, name='display_beta'),
    url(r'^display_Caffeine$', display_Caffeine, name='display_caffeine'),
    url(r'^display_LC$', display_LC, name='display_lc'),
    url(r'^display_NewOne$', display_NewOne, name='display_newone'),
    url(r'^display_Post$', display_Post, name='display_post'),
    url(r'^display_Pre$', display_Pre, name='display_pre'),
    url(r'^display_Protein$', display_Protein, name='display_protein'),
    url(r'^display_Recovery$', display_Recovery, name='display_recovery'),
    url(r'^display_test$', display_Test, name='display_test'),


]