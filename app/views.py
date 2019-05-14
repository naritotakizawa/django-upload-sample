from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from .forms import SingleUploadForm, SingleUploadModelForm, UploadFormSet, UploadModelFormSet, MultipleUploadForm
from .models import UploadFile


class SingleUploadView(generic.FormView):
    form_class = SingleUploadForm
    template_name = 'app/upload.html'

    def form_valid(self, form):
        download_url = form.save()
        context = {
            'download_url': download_url,
            'form': form,
        }
        return self.render_to_response(context)


class SingleUploadWithModelView(generic.CreateView):
    """ファイルモデルのアップロードビュー"""
    model = UploadFile
    form_class = SingleUploadModelForm
    template_name = 'app/upload.html'
    success_url = reverse_lazy('app:file_list')


class FileListView(generic.ListView):
    """アップロードされたファイルの一覧ページ"""
    model = UploadFile


class MultiUploadView(generic.FormView):
    form_class = UploadFormSet
    template_name = 'app/upload.html'

    def form_valid(self, form):
        download_url_list = form.save()
        context = {
            'download_url_list': download_url_list,
            'form': form,
        }
        return self.render_to_response(context)


def multi_upload_with_model(request):
    formset = UploadModelFormSet(request.POST or None, files=request.FILES or None, queryset=UploadFile.objects.none())
    if request.method == 'POST' and formset.is_valid():
        formset.save()
        return redirect('app:file_list')

    context = {
        'form': formset
    }

    return render(request, 'app/upload.html', context)


class InputMultiUploadView(generic.FormView):
    form_class = MultipleUploadForm
    template_name = 'app/upload.html'

    def form_valid(self, form):
        download_url_list = form.save()
        context = {
            'download_url_list': download_url_list,
            'form': form,
        }
        return self.render_to_response(context)
