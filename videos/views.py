from datetime import datetime

from django.shortcuts import get_object_or_404

from mezzanine.conf import settings
from mezzanine.utils.views import render, paginate

from models import Video


MAX_RESULTS_PAGE = 3


def video_list(request, template="videos/video_list.html"):
    """
    Render list of videos
    """
    templates = []
    video_list = list(Video.objects.published().order_by('-pub_date'))

    video_list = paginate(video_list, request.GET.get("page", 1),
                          MAX_RESULTS_PAGE,
                          settings.MAX_PAGING_LINKS)
    print video_list
    context = {'video_list': video_list}
    templates.append(template)
    return render(request, templates, context)


def video_detail(request, slug, template="videos/video.html"):
    """
    Render individual video post
    """
    templates = []
    video_list = Video.objects.published()
    video_object = get_object_or_404(video_list, slug=slug)
    context = {'video_object': video_object}
    templates.append(template)
    return render(request, templates, context)
