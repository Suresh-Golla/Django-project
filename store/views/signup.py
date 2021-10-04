from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from store.models.customer import Customer
from django.views import View


class Signup(View):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        postData = request.POST
        first_name = postData["firstname"]
        last_name = postData["lastname"]
        phone = postData["phone"]
        email = postData["email"]
        password = postData["password"]

        # validation
        value = {
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'email': email
        }

        error_message = None

        res = Customer(first_name=first_name,
                       last_name=last_name,
                       phone=phone,
                       email=email,
                       password=password)

        error_message = self.validateCustomer(res)

        # save data
        if (not error_message):
            res.password = make_password(res.password)
            res.register()
            return redirect('home')
        else:
            data = {
                'error': error_message,
                'values': value
            }
            return render(request, 'signup.html', data)

    def validateCustomer(self, res):
        error_message = None
        if (not res.first_name):
            error_message = 'First name required'
        elif len(res.first_name) < 5:
            error_message = 'First name must be greater than 5 characters'

        elif (not res.last_name):
            error_message = 'Last name required'
        elif len(res.last_name) < 5:
            error_message = 'Last name must be greater than 5 characters'

        elif (not res.phone):
            error_message = 'Phone number required'
        elif len(res.phone) < 10:
            error_message = 'phone number must contain 10 digits'

        elif (not res.email):
            error_message = 'Email required'
        elif len(res.email) < 5:
            error_message = 'Email must be greater than 4 characters'

        elif (not res.password):
            error_message = 'Password required'
        elif len(res.password) < 5:
            error_message = 'Password must be greater than 5 characters'

        elif res.isExist():
            error_message = 'Email Address Already Used For Registration'
        return error_message
