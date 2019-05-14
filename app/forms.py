from django import forms
from django.core.files.storage import default_storage
from .models import UploadFile


class SingleUploadForm(forms.Form):
    file = forms.ImageField(label='画像ファイル')

    def save(self):
        upload_file = self.cleaned_data['file']
        file_name = default_storage.save(upload_file.name, upload_file)
        return default_storage.url(file_name)


class SingleUploadModelForm(forms.ModelForm):

    class Meta:
        model = UploadFile
        fields = '__all__'


class BaseUploadFormSet(forms.BaseFormSet):

    def save(self):
        # ['/media/1.png', '/media/2.png']のようなファイルのURLが入ったリストになる
        url_list = []

        # SingleUploadFormのsaveを順に呼び出し、ファイルURLを集める
        for form in self.forms:
            try:
                url = form.save()
            except KeyError:
                # ファイルがアップロードされていないフォームは、KeyErrorになるので、ここで無視する
                pass
            else:
                url_list.append(url)
        return url_list


UploadFormSet = forms.formset_factory(SingleUploadForm, formset=BaseUploadFormSet, extra=5)

UploadModelFormSet = forms.modelformset_factory(
    UploadFile, form=SingleUploadModelForm,
    extra=3
)


class MultipleUploadForm(forms.Form):
    file = forms.ImageField(
        label='画像ファイル',
        widget=forms.ClearableFileInput(attrs={'multiple': True})
    )

    def save(self):
        url_list = []
        for upload_file in self.files.getlist('file'):
            file_name = default_storage.save(upload_file.name, upload_file)
            file_path = default_storage.url(file_name)
            url_list.append(file_path)
        return url_list
