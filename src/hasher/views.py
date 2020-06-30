import os
from django.shortcuts import render, HttpResponse, redirect
from django.http import HttpResponseRedirect, Http404

from .forms import UploadFileForm
from .utils import hash_file, handle_uploaded_file


def index(request):
    return render(request, 'index.html')


def upload_file(request):

    if request.POST:
        form = UploadFileForm(request.POST, request.FILES)
        print(request.FILES)
        md5_hash = handle_uploaded_file(request.FILES['upload_file'])

    else:
        form = UploadFileForm()
    return render(request, 'index.html', {'md5_hash': md5_hash})


def download_file(request):

    if request.POST:

        md5_hash = request.POST['md5_hash']

        if len(md5_hash) == 32:
            for root, dirs, files in os.walk("./store/{}/".format(md5_hash[:2])):
                for file in files:
                    if file.startswith(md5_hash):

                        file_path = os.path.join(root, file)

                        with open(file_path, 'rb') as f:
                            response = HttpResponse(f.read(),
                                                    content_type="application/")
                            response['Content-Disposition'] = 'inline; filename=' + \
                                                              os.path.basename(file_path)
                        return response

        not_found = True
        return render(request, 'index.html', {'not_found': not_found})


def delete_file(request):

    if request.POST:

        md5_hash = request.POST['md5_hash']

        if len(md5_hash) == 32:
            catalog = "./store/{}/".format(md5_hash[:2])

            for root, dirs, files in os.walk(catalog):
                for file in files:
                    if file.startswith(md5_hash):

                        file_path = os.path.join(root, file)

                        os.remove(file_path)
                        os.rmdir(catalog)

                        del_success = True
                        return render(request,
                                      'index.html',
                                      {'del_success': del_success}
                                     )

        not_found = True
        return render(request, 'index.html', {'not_found': not_found})
