from django.urls import path
from . import views


def custom_page_not_found(request):
    return django.views.defaults.page_not_found(request)


urlpatterns = [

   
    
    path('',views.index, name='index'),
    path('index1',views.index1,name='index1'),
    path('signup',views.signup, name='signup'),
    path('signup1',views.signup1, name='signup1'),
    path('signup2',views.signup2, name='signup2'),
    path('editprofdp',views.editprofdp, name='editprofdp'),
    path('accountcreated',views.accountcreated, name='accountcreated'),
    path('notifications',views.notifications, name='notifications'),
    path('home',views.home, name='home'),
    path('search',views.search, name='search'),
    path('post',views.post, name='post'),
    path('tag',views.tag, name='tag'),
    path('comments',views.comments, name='comments'),
    path('view_members',views.view_members, name='view_members'),
    path('settings',views.settings, name='settings'),
    path('settings1',views.settings1, name='settings1'),
    path('create_group',views.create_group, name='create_group'),
    path('groups',views.groups, name='groups'),
    path('groups_more',views.more,name='groups_more'),
    path('cpass',views.cpass, name='cpass'),
    path('t1',views.t1,name='t1'),
    path('t2',views.t2,name='t2'),
    path('t3',views.t3,name='t3'),
    path('t4',views.t4,name='t4'),
    path('t5',views.t5,name='t5'),
    path('t6',views.t6,name='t6'),
    path('t7',views.t7,name='t7'),
    path('t8',views.t8,name='t8'),
    path('t9',views.t9,name='t9'),
    path('t10',views.t10,name='t10'),
    path('t11',views.t11,name='t11'),
    path('t12',views.t12,name='t12'),
    path('t13',views.t13,name='t13'),
    path('t14',views.t14,name='t14'),
    path('t15',views.t15,name='t15'),
    path('t16',views.t16,name='t16'),
    path('t17',views.t17,name='t17'),
    path('t18',views.t18,name='t18'),
    path('t19',views.t19,name='t19'),
    path('t20',views.t20,name='t20'),
    path('t21',views.t21,name='t21'),
    path('t22',views.t22,name='t22'),
    path('t23',views.t23,name='t23'),
    path('t24',views.t24,name='t24'),
    path('t25',views.t25,name='t25'),
    path('t26',views.t26,name='t26'),
    path('t27',views.t27,name='t27'),
    path('t28',views.t28,name='t28'),
    path('t29',views.t29,name='t29'),
    path('t30',views.t30,name='t30'),
    path('t31',views.t31,name='t31'),
    path('t32',views.t32,name='t32'),
    path('t33',views.t33,name='t33'),
    path('t34',views.t34,name='t34'),
    path('t35',views.t35,name='t35'),
    path('t36',views.t36,name='t36'),
    path('t40',views.t40,name='t40'),
    path('t41',views.t41,name='t41'),
    path('t42',views.t42,name='t42'),
    path('t43',views.t43,name='t43'),
    path('t44',views.t44,name='t44'),
    path('t45',views.t45,name='t45'),
    path('t46',views.t46,name='t46'),
    path('t47',views.t47,name='t47'),
    path('t48',views.t48,name='t48'),
    path('t49',views.t49,name='t49'),
    path('t50',views.t50,name='t50'),
    path('tutor',views.tutor,name='tutor'),
    path('info',views.info,name='info'),
    path('about',views.about,name='about'),
    path('edit',views.edit,name='edit'),
    path('up',views.up,name='up'),
    path('target',views.target,name='target'),
    path('target1',views.target1,name='target1'),
    path('search/user/<int:uid>',views.prof,name='search/user'),
    path('search/group/<int:gid>',views.grp,name='search/group'),
    path('notifications/like/<int:did>',views.lc,name='notifications/like'),
    path('notifications/comment/<int:did>',views.lc,name='notification/comment'),
    path('notifications/reply/<int:did>',views.rep,name='notification/reply'),
    path('data',views.data,name='data'),
    path('certificate',views.certificate,name='certificate'),
    path('loadcomment',views.loadcomment,name='loadcomment'),
    path('loadtut',views.loadtut,name='loadtut'),
    

]
