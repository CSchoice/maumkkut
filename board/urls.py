from . import views
from django.urls import path

urlpatterns = [
    # 게시판 URL 패턴
    path('board/<str:board_type>/', views.post_list, name='post-list'),
    path('board/<str:board_type>/<int:pk>/', views.post_detail, name='post-detail'),

    # 댓글 URL 패턴
    path('board/<int:post_id>/comments/', views.comment_list, name='comment-list'),
    path('board/<int:post_id>/comments/<int:comment_id>/', views.comment_operations, name='comment-operations'),
    path('board/<int:post_id>/comments/<int:comment_id>/detail/', views.comment_detail, name='comment-detail'),

    # 통합 신고 기능 URL 패턴
    path('report/<str:item_type>/<int:item_id>/', views.report_item, name='report-item'),

    # 신고된 게시글 및 댓글 조회 및 삭제 URL 패턴
    path('reported/posts/', views.reported_posts_list, name='reported-posts-list'),
    path('reported/posts/<int:post_id>/', views.reported_post_detail, name='reported-post-detail'),
    path('reported/comments/', views.reported_comments_list, name='reported-comments-list'),
    path('reported/comments/<int:comment_id>/', views.reported_comment_detail, name='reported-comment-detail'),

    # 공통 조회 기능 URL 패턴
    path('posts/search/', views.search_posts, name='search-posts'),
]
