from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .forms import PostForm, EditForm, CommentForm, AddCategoryForm
from .models import Post, Category, Comment


class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-post_date']

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context


def CategoryListView(request):
    cat_menu_list = Category.objects.all()
    return render(request, 'category_list.html',
                  {'cat_menu_list': cat_menu_list})


def CategoryView(request, cats):
    category_posts = Post.objects.filter(category=cats.replace('-', ' '))
    return render(request, 'categories.html',
                  {'cats': cats.title().replace('-', ' '), 'category_posts': category_posts})


class ArticleView(DetailView):
    model = Post
    template_name = 'article.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(ArticleView, self).get_context_data(*args, **kwargs)

        context["cat_menu"] = cat_menu
        return context


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'


class AddCategoryView(CreateView):
    model = Category
    form_class = AddCategoryForm
    template_name = 'add_category.html'


class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update_post.html'
    success_url = reverse_lazy('home')


class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')


class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'add_comment.html'

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)

    success_url = reverse_lazy('home')


@login_required
@csrf_exempt
def like(request):
    if request.method == "POST":
        post_id = request.POST.get('id')
        is_liked = request.POST.get('is_liked')
        try:
            post = Post.objects.get(id=post_id)
            if is_liked == 'no':
                post.like.add(request.user)
                is_liked = 'yes'
            elif is_liked == 'yes':
                post.like.remove(request.user)
                is_liked = 'no'
            post.save()

            return JsonResponse({'like_count': post.like.count(), 'is_liked': is_liked, "status": 201})
        except:
            return JsonResponse({'error': "Post not found", "status": 404})
    return JsonResponse({}, status=400)
