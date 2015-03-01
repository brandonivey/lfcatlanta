from django import template

from videos.models import Video


MAX_RESULTS_PAGE = 3
register = template.Library()

@register.assignment_tag
def latest_videos(num_videos):
    limit = num_videos if num_videos else MAX_RESULTS_PAGE
    video_list = Video.objects.published().order_by('-pub_date')[0:limit]
    return video_list
