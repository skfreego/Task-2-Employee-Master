from django.views.generic.base import TemplateView
import xlwt
from django.shortcuts import render
from django.views.generic import View, TemplateView
from django.contrib.auth import authenticate, login
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.contrib.auth import logout
from .forms import AddUserForm, AddEmpForm, UserUpdateForm, EmpUpdateForm
from django.contrib.auth.models import User
from .models import EmpDetails

class LoginView(View):
	template_name = 'index.html'
	def get(self,request):
		form = AddUserForm
		return render(request,self.template_name,{'form':form})

	def post(self,request):
		username = request.POST['username']
		password = request.POST['password1']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect ('home')
		else: return redirect('login')

class HomeView(View):
	template_name = 'home_1.html'
	def get(self,request):
		if not request.user.is_authenticated:
			return redirect('login')
		return render (request,self.template_name)


def logout_view(request):
	request.session.flush()
	logout(request)
	# Redirect to a success page.
	return redirect("login")


class EmpAdd(View):
	template_name = 'services.html'
	form_class = AddUserForm
	cnt_class = AddEmpForm

	def get(self, request):
		if request.user.is_superuser:
			form1 = self.form_class()
			form2 = AddEmpForm()
			return render(request,self.template_name,{'form1':form1, 'form2':form2})
		else:
			return HttpResponse('invalid user')

	def post(self,request):
		form1 = self.form_class(request.POST)
		form2 = AddEmpForm(request.POST, request.FILES)
		if form1.is_valid() and form2.is_valid():
			usr_d = User.objects.create_user(
				username = request.POST.get('username'),
				first_name = request.POST.get('first_name'),
				last_name = request.POST.get('last_name'),
				email = request.POST.get('email'),
				password = request.POST.get('password1'))
			usr_d.is_staff=True
			usr_d.save()
			emp_details = EmpDetails.objects.create(
				user_key = usr_d,
				user_name = usr_d.first_name + " " +usr_d.last_name,
				user_email = request.POST.get('email'),
				user_password = request.POST.get('password1'),
				user_phone = request.POST.get('user_phone'),
				user_address = request.POST.get('user_address'),
				user_image = request.FILES.get('user_image'),
				)
			emp_details.save()

			return redirect('emplist')

		else:
			print('not validated')
			print(form1.errors)
			print(form2.errors)
			form1 = self.form_class()
			form2 = AddEmpForm()
			return render(request,self.template_name,{'form1':form1,'form2':form2})

class EmpList(View):
	template_name='portfolio.html'
	def get(self,request):
		if request.user.is_staff:
			obj = EmpDetails.objects.all()
			context = {
			# 'user_list':obj1,
			'doc_list':obj
			}
			return render(request,self.template_name,context)
		else:
			return HttpResponse('invalid user')


class EmpUpdateView(View):
	template_name = 'empupdate.html'
	def get(self,request,pk):
		if request.user.is_superuser:
			user_objd = User.objects.get(id=pk)
				
			print(user_objd)
			form1 = UserUpdateForm(initial = 
				{'username':user_objd.username,
				'first_name':user_objd.first_name,
				'last_name':user_objd.last_name,
				'email':user_objd.email}
				)
			doc = EmpDetails.objects.get(user_key=user_objd)
		
			print(doc)
			form2 = EmpUpdateForm(initial={
					 'user_name':doc.user_name, 
					 'user_phone':doc.user_phone,
					 'user_address':doc.user_address,
					 'user_image':doc.user_image})
			return render (request,self.template_name,{"form1":form1, "form2":form2})
		else:
			return HttpResponse('invalid user')
	def post(self,request,pk):
		form1 = UserUpdateForm(request.POST)
		form2 = EmpUpdateForm(request.POST)
		if form1.is_valid() and form2.is_valid():
			

			usr_d = User.objects.create(
				username = request.POST.get('username'),
				first_name = request.POST.get('first_name'),
				last_name = request.POST.get('last_name'),
				email = request.POST.get('email'))
				# password = request.POST.get('password1'))
			usr_d.is_staff = True
			usr_d.save()
			usr_doc = EmpDetails.objects.create(
				user_key = usr_d,
				user_name = request.POST.get('first_name') +  ' '+ request.POST.get('last_name'),
				user_email = request.POST.get('email'),
				user_phone = request.POST.get('user_phone'),
				user_address = request.POST.get('user_address'),
				user_image = request.POST.get('user_image'),
				)
			usr_doc.save()
			# messages.success(request, _('Your profile was successfully updated!'))
			return redirect('emplist')

		else:
			form1 = UserUpdateForm()
			form2 = EmpUpdateForm()
			return render(request,self.template_name,{'form1':form1, 'form2' :form2})


class ContactView(TemplateView):
	template_name='contact.html'