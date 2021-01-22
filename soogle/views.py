from django.shortcuts import render, redirect, get_object_or_404, resolve_url
from django.utils import timezone
from .forms import PostForm, CommentForm
from .models import Post
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.db.models import Q, Count
from django.contrib import messages

import logging
# Create your views here.

logger = logging.getLogger('soogle')

def index(request):
    return render(request, 'index.html')

def profile(request):
    pass

@login_required(login_url = 'account:login')
def post_write(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.create_date = timezone.now()
            post.save()
            return redirect('soogle:post_list')
    else:
        form = PostForm()
    context = {'form': form}
    return render(request, 'post/post_write.html', context)


@login_required(login_url = 'account:login')
def post_modify(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.user != post.author:
        messages.error(request, '수정권한이 없습니다.')
        return redirect('soogle:post_detail', post_id=post.id)

    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.modify_date = timezone.now()
            post.save()
            return redirect('soogle:post_detail', post_id=post.id)

    else:
        form = PostForm(instance=post)
    context = {'form': form}
    return render(request, 'post/post_write.html', context)


@login_required(login_url='account:login')
def post_delete(request, post_id):

    post = get_object_or_404(Post, pk=post_id)
    if request.user != post.author:
        messages.error(request, '삭제권한이 없습니다.')
        return redirect('soogle:post_detail', post_id=post.id)
    post.delete()
    return redirect('soogle:post_list')



def post_list(request):
    logger.info("INFO 레벨로 출력")

    # 입력 파라미터
    page = request.GET.get('page', '1')  # 페이지
    kw = request.GET.get('kw', '')  # 검색어

    so = request.GET.get('so', 'recent')  # 정렬기준

    # 정렬
    if so == 'recommend':
        post_list = Post.objects.annotate(num_voter=Count('voter')).order_by('-num_voter', '-create_date')
    elif so == 'popular':
        post_list = Post.objects.annotate(num_comment=Count('comment')).order_by('-num_comment', '-create_date')
    else:  # recent
        post_list = Post.objects.order_by('-create_date')

    # 조회
    if kw:
        post_list = post_list.filter(
            Q(title__icontains=kw) |  # 제목검색
            Q(contents__icontains=kw) |  # 내용검색
            Q(author__username__icontains=kw) |  # 질문 글쓴이검색
            Q(comment__author__username__icontains=kw)  # 답변 글쓴이검색
        ).distinct()

    # 페이징처리

    paginator = Paginator(post_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)

    context = {'post_list': page_obj, 'page': page, 'kw': kw, 'so': so}  # page와 kw가 추가되었다.

    return render(request, "post/post_list.html", context)

def post_detail(request, post_id):

    post = get_object_or_404(Post, pk=post_id)



    context = {"post": post}
    return render(request, "post/post_detail.html", context)


@login_required(login_url='account:login')
def comment_write(request, post_id):

    post = get_object_or_404(Post, pk=post_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user  # 추가한 속성 author 적용
            comment.create_date = timezone.now()
            comment.post = post
            comment.save()
            return redirect('{}#comment_{}'.format(
                resolve_url('soogle:post_detail', post_id=post.id), comment.id))
    else:
        form = CommentForm()
    context = {'post': post, 'form': form}
    return render(request, 'post/post_detail.html', context)

@login_required(login_url='account:login')
def post_vote(request, post_id):

    post = get_object_or_404(Post, pk=post_id)
    if request.user == post.author:
        messages.error(request, '본인이 작성한 글은 추천할 수 없습니다.')
    else:
        post.voter.add(request.user)
        messages.success(request, '추천이 완료되었습니다.')
    return redirect('soogle:post_detail', post_id=post.id)

def soogle_membership(request):
    return render(request, 'post/soogle_membership.html')

