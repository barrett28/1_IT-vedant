from django.shortcuts import render, redirect, get_object_or_404
from .models import Recipe, Rating, Comment, Bookmark
from django.contrib.auth.decorators import login_required
from .forms import RecipeForm
from django.contrib.auth import login, logout, authenticate
from .forms import SignupForm, LoginForm
from django.contrib import messages

# Create your views here.
def index(request):
    featured_recipes = Recipe.objects.all().order_by('-created_at')[:4] 
    return render(request, 'recipe/index.html', {'featured_recipes': featured_recipes,})
def about(request):
    return render(request, 'recipe/about.html')

@login_required
def add_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.user = request.user
            recipe.save()
            return redirect('index')  # Redirect to home after submission
    else:
        form = RecipeForm()
    
    return render(request, 'recipe/add_recipe.html', {'form': form})


# Signup View
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')  # Redirect to recipes home
    else:
        form = SignupForm()
    return render(request, 'recipe/signup.html', {'form': form})

# Login View
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('index')
    else:
        form = LoginForm()
    return render(request, 'recipe/login.html', {'form': form})

# Logout View
def user_logout(request):
    logout(request)
    return redirect('index')


def explore(request):
    if request.user.is_authenticated:
        all_recipes = Recipe.objects.all().order_by('-created_at')
        return render(request, 'recipe/explore.html', { 'recipes': all_recipes})
    else:
        return redirect('login')

def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    return render(request, 'recipe/details.html', {'recipe': recipe})


@login_required
def rate_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    if request.method == 'POST':
        score = int(request.POST.get('score'))
        Rating.objects.update_or_create(
            user=request.user,
            recipe=recipe,
            defaults={'score': score}
        )
    return redirect('recipe_detail', recipe_id=recipe.id)

@login_required
def add_comment(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    if request.method == 'POST':
        Comment.objects.create(
            user=request.user,
            recipe=recipe,
            text=request.POST.get('text')
        )
    return redirect('recipe_detail', recipe_id=recipe.id)

# def fav(request, id):
#     if request.user.is_authenticated:
#         book = Recipe.objects.get(pk = id)
#         user = request.user 
#         Bookmark(user = user, fav = book).save()
#         return render(request, 'recipe/fav.html')
#     else:
#         return redirect('login')

def fav(request, id):
    if not request.user.is_authenticated:
        return redirect('login')
    
    recipe = get_object_or_404(Recipe, pk=id)
    user = request.user
    
    # Check if bookmark already exists
    bookmark, created = Bookmark.objects.get_or_create(
        user=user,
        recipe=recipe
    )
    
    if created:
        messages.success(request, "Added to favorites!")
    else:
        messages.info(request, "This recipe is already in your favorites")
     
    return redirect('recipe_detail', recipe_id=id)


def favorite_recipes(request):
    if request.user.is_authenticated:
            
        # Get all bookmarks for the current user
        bookmarks = Bookmark.objects.filter(user=request.user).select_related('recipe')
        # Extract the recipes from the bookmarks
        favorite_recipes = [bookmark.recipe for bookmark in bookmarks]
        
        return render(request, 'recipe/fav.html', {'favorite_recipes': favorite_recipes})
    else:
        return redirect('login')