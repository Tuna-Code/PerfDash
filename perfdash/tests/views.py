from django.shortcuts import render

# Create your views here.
from .models import Test, Host, Location

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_hosts = Host.objects.all().count()
    num_tests = Test.objects.all().count()

    num_throughput_tests = Test.objects.filter(type__exact='t').count()

    # The 'all()' is implied by default.
    num_locations = Location.objects.count()

    context = {
        'num_hosts': num_hosts,
        'num_tests': num_tests,
        'num_throughput_tests': num_throughput_tests,
        'num_locations': num_locations,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)
