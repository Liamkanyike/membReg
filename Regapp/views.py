from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User, auth
from Regapp.models import Church
from Regapp.forms import ChurchForm
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required

from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, HttpResponseNotFound
from django.urls import reverse
import json
from django.db.models import Q
from django.db.models import Count
from django.template.loader import get_template
from xhtml2pdf import pisa

from django.views.generic import ListView


def searchmain(request):
    queryset=Church.objects.all()
    query = request.GET.get('q')
    if query:
        queryset = queryset.filter(
            Q(phone__iexact=query) |
            Q(surname__icontains=query)
            ).distinct()
        context = {
            'queryset':queryset
                 }
        messages.success(request,"Search Complete!")
    return render(request, 'users/results.html', context)


def search(request):
    queryset=Church.objects.all()
    query = request.GET.get('q')
    if query:
        queryset = queryset.filter(
            Q(phone__iexact=query) |
            Q(surname__icontains=query)
            ).distinct()
        context = {
            'queryset':queryset
                 }
        messages.success(request,"Search Complete!")
    return render(request, 'users/results.html', context)


# def login(request):
#     if request.method=='POST':
#         username = request.POST['username']
#         password = request.POST['password']

#         user = auth.authenticate(username=username,password=password)

#         if user is not None:
#             auth.login(request, user)
#             return redirect("/dashboard")
#         else:
#             messages.error(request, "invalid credentials!")
#             return redirect('login')

#     else:
#         return render(request, "login/index.html")


def church_render_pdf_view(request, *args, **kwargs):
    # print("this view was hit")
    pk = kwargs.get('pk')
    church = get_object_or_404(Church, pk=pk)

    template_path = 'users/pdf-result.html'
    context = {'church': church}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="church-details.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
   
    return response


def pdf_view(request, *args, **kwargs):
    pk = kwargs.get('pk')
    church = get_object_or_404(Church, pk=pk)
    

    template_path = 'users/pdf-view-result.html'
    context = {'church': church}

    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)
    try:
        file_name = str(church.document.path).split('/')[-1]
        with open('{}'.format(church.document.path), 'rb') as pdf:
            response = HttpResponse(pdf.read(), content_type='application/pdf')
            response['Content-Disposition'] = 'inline;filename={}'.format(file_name)
            return response
    except:
        html = ''
        return HttpResponse('<br> Oops!! :( <br>  We had some errors displaying the document. Please ensure that you uploaded a document in pdf. <pre>' + html + '</pre>')



def document_download(request, *args, **kwargs):
    pk = kwargs.get('pk')
    church = get_object_or_404(Church, pk=pk)

    file_name = str(church.document.path).split('/')[-1]
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    
    with open('{}'.format(church.document.path), 'rb') as pdf:
        response = HttpResponse(pdf.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename={}'.format(file_name)
        return response
   

   
#def upload(request):
    #context = {}
    #if request.method == 'POST':
        #uploaded_file = request.FILES['document']
        #fs = FileSystemStorage()
        #name = fs.save(uploaded_file.name, uploaded_file)
        #context['url'] = fs.url(name)
    #return render(render, register.html, context)


@login_required
def reg(request):
	if request.method == 'POST':
		form = ChurchForm(request.POST, request.FILES)
		if form.is_valid():
			try:
				form.save()
				messages.success(request,"Successfully Registered Church Info!")
				return redirect('/view')
			except:
				messages.error(request,"Failed to Register Church Info!")
				return HttpResponseRedirect(reverse("reg"))
	else:
		form = ChurchForm()
	return render(request, 'users/register.html',{'form':form})


@login_required
def update(request, id):
    church = get_object_or_404(Church, id=id)
    if request.method == 'GET':
        form = ChurchForm(instance=church)
        return redirect("/view")
    else:
        form = ChurchForm(request.POST,request.FILES, instance=church)
        form.save()
        messages.success(request,"Updated Church Info! Successfully")
        return redirect("/view")


#def logout(request):
    #return redirect("/")

@login_required
def view(request):
	church = Church.objects.order_by('-id')
	return render(request, "users/view.html", {'church':church})

def delete(request, id):
	church = Church.objects.get(id=id)
	church.delete()
	return redirect("/view")

@login_required
def edit(request, id):
	church = Church.objects.get(id=id)
	return render(request, 'users/edit.html',{'church':church})


@login_required
def details(request, id):
	church = Church.objects.get(id=id)
	return render(request, 'users/details2.html',{'church':church})

class ChurchListView(ListView):
    model = Church
    template_name='users/main.html'


@csrf_exempt
def check_email_exist(request):
    email=request.POST.get("email")
    user_obj=Church.objects.filter(email=email).exists()
    if user_obj:
        return HttpResponse(True)
    else:
        return HttpResponse(False)

@csrf_exempt
def check_phone_exist(request):
    phone=request.POST.get("phone")
    user_obj=Church.objects.filter(phone=phone).exists()
    if user_obj:
        return HttpResponse(True)
    else:
        return HttpResponse(False)
