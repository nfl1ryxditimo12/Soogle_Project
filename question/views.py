from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .forms import AboutForm
from .models import About
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages

import logging
# Create your views here.

logger = logging.getLogger('soogle')


def about(request):

    page = request.GET.get('page', '1')
    question_list = About.objects.order_by('-create_date')

    paginator = Paginator(question_list, 10)

    page_obj = paginator.get_page(page)

    context = {'question_list': page_obj}

    return render(request, 'about/about.html', context)

@login_required(login_url='account:login')
def question_write(request):

    if request.method == "POST":
        form = AboutForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.create_date = timezone.now()
            question.save()
            return redirect('question:about')
    else:
        form = AboutForm()
    context = {'form': form}
    return render(request, 'about/about.html', context)

def question_delete(request, question_id):


    question = get_object_or_404(About, pk=question_id)
    if request.user != question.author:
        messages.error(request, '삭제권한이 없습니다.')
        return redirect('question:about', question_id=question.id)
    question.delete()
    return redirect('question:about')