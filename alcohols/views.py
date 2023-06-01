from random import randint

from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView

import alcohols.models
from alcohols.forms import AddCommentForm
from alcohols.models import Alcohol, Wine, UserProfile


# Create your views here.

class IndexView(View):

    def get(self, request):
        return render(request, "index.html")


class AlcoholsListView(ListView):
    model = Alcohol
    template_name = "list_view.html"
    context_object_name = "alcohols"
    paginate_by = 10
    queryset = Alcohol.objects.all().order_by('votes').reverse()


class AlcoholDetail(View):
    def get(self, request, pk):
        alcohol = Alcohol.objects.get(pk=pk)
        form = AddCommentForm()
        is_favorited = False
        if request.user.is_authenticated:
            try:
                user_profile = UserProfile.objects.get(user=request.user)
            except UserProfile.DoesNotExist:
                # Tworzenie profilu użytkownika, jeśli nie istnieje
                user_profile = UserProfile.objects.create(user=request.user)
            if user_profile.fav_alcohol.filter(pk=pk).exists():
                is_favorited = True
        return render(request, 'alcohol-detail.html', {'alcohol': alcohol, 'form': form, 'is_favorited': is_favorited})

    def post(self, request, pk):
        alcohol = get_object_or_404(Alcohol, pk=pk)

        if 'voteUp' in request.POST:
            alcohol.votes += 1
            alcohol.save()
        elif 'voteDown' in request.POST:
            if alcohol.votes > 0:
                alcohol.votes -= 1
                alcohol.save()
        elif 'add_to_favorites' in request.POST:
            user_profile = UserProfile.objects.get(user=request.user)
            user_profile.fav_alcohol.add(alcohol)
            user_profile.save()
        elif 'remove_from_favorites' in request.POST:
            user_profile = UserProfile.objects.get(user=request.user)
            user_profile.fav_alcohol.remove(alcohol)
            user_profile.save()

        return redirect('alcohol-detail', pk=pk)


class AddComment(View):

    def get(self, request, pk):
        alcohol = Alcohol.objects.get(pk=pk)
        form = AddCommentForm()
        return render(request, 'alcohol-detail.html', {'alcohol': alcohol, 'form': form})

    def post(self, request, pk):
        if not request.user.is_authenticated:
            return redirect('Index')
        alcohol = Alcohol.objects.get(pk=pk)
        form = AddCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.id = randint(0,1000)
            comment.user_id = request.user.id
            comment.alcohol_id = alcohol.id
            comment.save()
            return redirect('alcohol-detail', pk)
        return render(request, 'alcohol-detail.html', {'alcohol': alcohol, 'form': form})

class AddFav(View):
    def get(self, request, pk):
        alcohol = get_object_or_404(Alcohol, pk=pk)
        is_favorited = alcohol.is_favorited_by(request.user)
        form = AddCommentForm()
        return render(request, 'alcohol-detail.html', {'alcohol': alcohol, 'form': form, 'is_favorited': is_favorited})

    def post(self, request, pk):
        alcohol = get_object_or_404(Alcohol, pk=pk)
        if 'add_to_favorites' in request.POST:
            alcohol.add_to_favorites(request.user)
        elif 'remove_from_favorites' in request.POST:
            alcohol.remove_from_favorites(request.user)

        return redirect('alcohol-detail', pk=pk)

class FavoriteAlcoholsView(View):
    def get(self, request):
        if request.user.is_authenticated:
            user_profile = UserProfile.objects.get(user=request.user)
            favorite_alcohols = user_profile.fav_alcohol.all()
            return render(request, 'favorite-alcohols.html', {'favorite_alcohols': favorite_alcohols})
        else:
            return redirect('login')

class WinesListView(ListView):
    model = Wine
    template_name = "wine_view.html"
    context_object_name = "wines"
    paginate_by = 10

    def get_queryset(self):
        return Wine.objects.filter(alcohol__type_id=1).order_by('-alcohol__votes')