from typing import Any
from django.shortcuts import render
from .models import Game,GameMainInfo, GameMedia, Genre, GameSecondaryInfo
from django.core.paginator import Paginator

def home(request):
    return render(request, 'base.html', {})

def game_list(request):
    game_info_list = GameMainInfo.objects.filter().order_by('-hit_count_generic__hits')
    page = Paginator(game_info_list,1)
    page_number = request.GET.get('page')
    page_obj = page.get_page(page_number)
    genres = Genre.objects.all()
    
    for game_info in game_info_list:
        game_info.genres = game_info.genre.all()
        print(game_info.genres)

    context = {
        'game_info_list':page_obj,
        'genres':genres,
    }

    return render(request, 'games/game_list.html', context)

from hitcount.utils import get_hitcount_model
from hitcount.views import HitCountMixin
from django.shortcuts import get_object_or_404

def game_detail(request, gid):
    game_info = get_object_or_404(GameMainInfo, game_id= gid)
    game_secondary_info = GameSecondaryInfo.objects.get(game_id=gid)
    game_media = GameMedia.objects.filter(game_info_id = game_info.pk)
    genres = game_info.genre.all()

    hit_count = get_hitcount_model().objects.get_for_object(game_info)
    hits = hit_count.hits
    hit_count_response = HitCountMixin.hit_count(request, hit_count)

    hitcontext = {'pk':hit_count.pk}
    if hit_count_response.hit_counted:
        hits += 1
        hitcontext['hit_counted'] = hit_count_response.hit_counted
        hitcontext['hit_message'] = hit_count_response.hit_message
        hitcontext['total_hits'] = hits

    context = {
        'game_info':game_info, 
        'game_secondary_info':game_secondary_info,
        'game_media':game_media,
        'genres':genres
    }
    return render(request, 'games/game_detail.html', context)

# from django.views.generic import DetailView
# from hitcount.views import HitCountDetailView

# class GameDetailView(HitCountDetailView):
#     model = GameMainInfo
#     count_hit = True

#     context_object_name = 'game_info'
#     template_name = 'games/game_detail.html'

#     def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
#         context = super().get_context_data(**kwargs)
#         game_id = context['game_info'].game.pk
#         game_secondary_info = GameSecondaryInfo.objects.get(game_id=game_id)
#         game_media = GameMedia.objects.filter(game_info_id = context['game_info'].pk)
#         genres = context['game_info'].genre.all()
#         context.update( {
#             'game_secondary_info':game_secondary_info,
#             'game_media':game_media,
#             'genres':genres
#         })
#         return context