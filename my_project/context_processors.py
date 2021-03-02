from django.contrib.auth.forms import AuthenticationForm
from home.forms import UserRegistrationForm ,ContactForm
from products.models import Shopcart

def extras(request):
    signupform = UserRegistrationForm()
    loginform = AuthenticationForm()
    if (request.user.is_authenticated):
        contactfrom = ContactForm()
        instances = Shopcart.objects.filter(customer = request.user)
        prods = []
        for instance in instances:
            prods.append(instance.product.id)
        return {'signupform':signupform,'loginform':loginform,"contactfrom":contactfrom,"cart_items":prods}
    return {'signupform':signupform,'loginform':loginform}
