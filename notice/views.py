from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404, resolve_url
from .forms import NoticeForm
from django.utils import timezone
from .models import Notice
from django.db.models import Q, Count
from django.contrib import messages


# Create your views here.

def notice_list(request):

    # 입력 파라미터
    page = request.GET.get('page', '1')  # 페이지

    notice_list = Notice.objects.order_by('-create_date')

    # 페이징처리

    paginator = Paginator(notice_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)

    context = {'notice_list': page_obj, 'page': page}

    return render(request, "notice/notice_list.html", context)

@login_required(login_url = 'account:login')
def notice_write(request):

    if request.method == "POST":
        form = NoticeForm(request.POST)
        if form.is_valid():
            notice = form.save(commit=False)
            notice.author = request.user
            notice.create_date = timezone.now()
            notice.save()
            return redirect('notice:notice_list')
    else:
        form = NoticeForm()
    context = {'form': form}
    return render(request, 'notice/notice_write.html', context)

def notice_detail(request, notice_id):

    notice = get_object_or_404(Notice, pk=notice_id)

    return render(request, 'notice/notice_detail.html', {'notice': notice})

@login_required(login_url = 'account:login')
def notice_modify(request, notice_id):
    notice = get_object_or_404(Notice, pk=notice_id)
    if request.user != notice.author:
        messages.error(request, '수정권한이 없습니다.')
        return redirect('notice:notice_detail', notice_id=notice.id)

    if request.method == "POST":
        form = NoticeForm(request.POST, instance=notice)
        if form.is_valid():
            notice = form.save(commit=False)
            notice.author = request.user
            notice.modify_date = timezone.now()
            notice.save()
            return redirect('notice:notice_detail', notice_id=notice.id)

    else:
        form = NoticeForm(instance=notice)
    context = {'form': form}
    return render(request, 'notice/notice_write.html', context)

@login_required(login_url='account:login')
def notice_delete(request, notice_id):

    notice = get_object_or_404(Notice, pk=notice_id)
    if request.user != notice.author:
        messages.error(request, '삭제권한이 없습니다.')
        return redirect('notice:notice_detail', notice_id=notice.id)
    notice.delete()
    return redirect('notice:notice_list')

@login_required(login_url='account:login')
def notice_vote(request, notice_id):

    notice = get_object_or_404(Notice, pk=notice_id)
    if request.user == notice.author:
        messages.error(request, '본인이 작성한 글은 추천할 수 없습니다.')
    else:
        notice.voter.add(request.user)
        messages.success(request, '추천이 완료되었습니다.')
    return redirect('notice:notice_detail', notice_id=notice.id)

