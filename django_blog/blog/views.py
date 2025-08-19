from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from .forms import UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Post

# List all posts
class PostListView(ListView):
    model = Post
    template_name = "post_list.html"
    context_object_name = "posts"

# View a single post
class PostDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"

# Create a new post
class PostCreateView(CreateView):
    model = Post
    template_name = "post_form.html"
    fields = ["title", "content"]

# Update a post
class PostUpdateView(UpdateView):
    model = Post
    template_name = "post_form.html"
    fields = ["title", "content"]

# Delete a post
class PostDeleteView(DeleteView):
    model = Post
    template_name = "post_confirm_delete.html"
    success_url = reverse_lazy("post_list")

def register(request):
    form = CustomUserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login')  # After registration, go to login
    else:
        form = CustomUserCreationForm()
    return render(request, 'blog/register.html', {'form': form})

@login_required
def profile(request):
    profile = request.user.userprofile  # automatically created by signals

    if request.method == "POST":
        request.user.username = request.POST.get("username")
        request.user.email = request.POST.get("email")
        request.user.save()

        profile.bio = request.POST.get("bio")
        if request.FILES.get("profile_picture"):
            profile.profile_picture = request.FILES.get("profile_picture")
        profile.save()

        return redirect("profile")

    return render(request, "profile.html", {"profile": profile})
