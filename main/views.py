

# Create your views here.
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from main.models import Cereal, Manufacturer
from django.template import RequestContext
from django.conf import settings

# Create your views here.

#list views
#detail views
#create view
#edit view
#delete view

def base(request):
    context = {}

    cereal = Cereal.objects.all()

    context['cereal'] = cereal

    return render_to_response('base.html', context, context_instance=RequestContext(request))
  

def cereal_list(request):

    context = {}

    cereal = Cereal.objects.all()

    context['cereal'] = cereal

    #render_to_response(template, context dict, context_instance=RequestContext(request))
    return render_to_response('cereal_list.html', context, context_instance=RequestContext(request))


def cereal_detail(request, pk):
    context = {}

    cereal = Cereal.objects.get(pk=pk)

    context['cereal'] = cereal

    return render_to_response('cereal_detail.html', context, context_instance=RequestContext(request))

def cereal_search(request):

    context = {}

    context['request'] = request

    #context ['get_vars'] = request.GET['a']

    #context ['get vars'] = request.GET.get('a', None)

    cereal = request.GET.get('cereal', None)
    #state = request.POST.get('state', None)
    if cereal != None:
        #list
        cereal = Cereal.objects.filter(name__icontains=cereal)
    else:
        cereal = Cereal.objects.all()


    context['cereal'] = cereal

    return render_to_response('cereal_search.html', context, context_instance=RequestContext(request))

def cereal_create(request):

    context = {}

    context['request'] = request.method

    context['manufacturers'] = Manufacturer.objects.all()

    if request.method == "POST":
        name = request.POST.get('name', None)
        manufacturer = request.POST.get('manufacturer', None)
        cereal_type = request.POST.get('cereal_type', None)
        calories = request.POST.get('calories', None)
        protein = request.POST.get('protein', None)
        fat = request.POST.get('fat', None)
        sodium = request.POST.get('sodium', None)
        fiber = request.POST.get('fiber', None)
        carbs = request.POST.get('carbs', None)
        sugars = request.POST.get('sugars', None)
        shelf = request.POST.get('shelf', None)
        potassium = request.POST.get('potassium', None)
        vits_and_mins = request.POST.get('vits_and_mins', None)
        serving_size_weight = request.POST.get('serving_size_weight', None)
        cups_per_serving = request.POST.get('cups_per_serving', None)
        manufacturer_id = request.POST.get('man', None)

        if manufacturer_id != None:
            manufacturer = Manufacturer.objects.get(pk=manufacturer_id)
        else:
            manufacturer = Manufacturer.objects.get(manufacturer="Maypo")

        the_cereal, created = Cereal.objects.get_or_create(name=name)
        
        the_cereal.manufacturer = manufacturer
        the_cereal.cereal_type = cereal_type
        the_cereal.calories = calories
        the_cereal.protein = protein
        the_cereal.fat = fat
        the_cereal.sodium = sodium
        the_cereal.fiber = fiber
        the_cereal.carbs = carbs
        the_cereal.sugars = sugars
        the_cereal.shelf = shelf
        the_cereal.potassium = potassium
        the_cereal.vits_and_mins = vits_and_mins
        the_cereal.serving_size_weight = serving_size_weight
        the_cereal.cups_per_serving = cups_per_serving
        the_cereal.save()

        context['created'] = "Operation Successful"

    elif request.method == 'GET':
        pass

    return render_to_response('cereal_create.html', context, context_instance=RequestContext(request))

def cereal_update(request):
    context = {}
    context['cereals'] = Cereal.objects.all()

    return render_to_response('cereal_update.html', context, context_instance=RequestContext(request))

def cereal_update_spec(request):
    cereal_id = request.POST.get('cereal_id', None)
    print cereal_id
    context = {}
    context['selected_cereal'] = Cereal.objects.get(pk=cereal_id)

    context['request'] = request.method

    context['cereal'] = Cereal.objects.all()

    context['manufacturers'] = Manufacturer.objects.all()

    if request.method == "POST":
        name = request.POST.get('name', None)
        manufacturer = request.POST.get('manufacturer', None)
        cereal_type = request.POST.get('cereal_type', None)
        calories = request.POST.get('calories', None)
        protein = request.POST.get('protein', None)
        fat = request.POST.get('fat', None)
        sodium = request.POST.get('sodium', None)
        fiber = request.POST.get('fiber', None)
        carbs = request.POST.get('carbs', None)
        sugars = request.POST.get('sugars', None)
        shelf = request.POST.get('shelf', None)
        potassium = request.POST.get('potassium', None)
        vits_and_mins = request.POST.get('vits_and_mins', None)
        serving_size_weight = request.POST.get('serving_size_weight', None)
        cups_per_serving = request.POST.get('cups_per_serving', None)
        manufacturer_id = request.POST.get('man', None)

        if manufacturer_id != None:
            manufacturer = Manufacturer.objects.get(pk=manufacturer_id)
        else:
            pass
        the_cereal = Cereal.objects.get(pk=cereal_id)
        the_cereal.manufacturer = manufacturer
        the_cereal.cereal_type = cereal_type
        the_cereal.calories = calories
        the_cereal.protein = protein
        the_cereal.fat = fat
        the_cereal.sodium = sodium
        the_cereal.fiber = fiber
        the_cereal.carbs = carbs
        the_cereal.sugars = sugars
        the_cereal.shelf = shelf
        the_cereal.potassium = potassium
        the_cereal.vits_and_mins = vits_and_mins
        the_cereal.serving_size_weight = serving_size_weight
        the_cereal.cups_per_serving = cups_per_serving
        the_cereal.save()

        context['created'] = "Operation Successful"

    elif request.method == 'GET':
        pass

    return render_to_response('cereal_update_spec.html', context, context_instance=RequestContext(request))

def cereal_delete(request):
    cereal_id = request.POST.get('cereal_id', None)
    print cereal_id
    context = {}
    context['cereals'] = Cereal.objects.all()
    context['request'] = request.method
    print Cereal.objects.filter(pk=cereal_id)
    Cereal.objects.filter(pk=cereal_id).delete()
    if cereal_id != None:
        return HttpResponseRedirect('/cereal_list/')
    else:
        pass
    
    return render_to_response('cereal_delete.html', context, context_instance=RequestContext(request))


def manufacturer_list(request):

    context = {}

    manufacturer = Manufacturer.objects.all()

    context['manufacturer'] = manufacturer

    #render_to_response(template, context dict, context_instance=RequestContext(request))
    return render_to_response('manufacturer_list.html', context, context_instance=RequestContext(request))


def manufacturer_detail(request, pk):
    context = {}

    manufacturer = Manufacturer.objects.get(pk=pk)

    context['man'] = manufacturer

    return render_to_response('manufacturer_detail.html', context, context_instance=RequestContext(request))

def manufacturer_search(request):

    context = {}

    context['request'] = request

    #context ['get_vars'] = request.GET['a']

    #context ['get vars'] = request.GET.get('a', None)

    manufacturer = request.GET.get('manufacturer', None)
    #state = request.POST.get('state', None)
    if manufacturer != None:
        #list
        manufacturers = Manufacturer.objects.filter(manufacturer__icontains=manufacturer)
    else:
        manufacturers = Manufacturer.objects.all()


    context['manufacturers'] = manufacturers

    return render_to_response('manufacturer_search.html', context, context_instance=RequestContext(request))

def manufacturer_create(request):

    context = {}

    context['request'] = request.method

    if request.method == "POST":

        manufacturer = request.POST.get('manufacturer', None)

        the_man, created = Manufacturer.objects.get_or_create(manufacturer=manufacturer)

        the_man.save()

        context['created'] = "Operation Successful"

    elif request.method == 'GET':
        pass

    return render_to_response('manufacturer_create.html', context, context_instance=RequestContext(request))

def manufacturer_update(request):
    context = {}
    context['manufacturers'] = Manufacturer.objects.all()

    return render_to_response('manufacturer_update.html', context, context_instance=RequestContext(request))

def manufacturer_update_spec(request):
    man_id = request.POST.get('man_id', None)
    print man_id
    context = {}
    context['selected_man'] = Manufacturer.objects.get(pk=man_id)
    context['request'] = request.method
    context['manufacturers'] = Manufacturer.objects.all()

    if request.method == "POST":
        manufacturer = request.POST.get('manufacturer', None)

        the_man = Manufacturer.objects.get(pk=man_id)
        the_man.manufacturer = manufacturer
        the_man.save()

        context['created'] = "Operation Successful"

    elif request.method == 'GET':
        pass

    return render_to_response('manufacturer_update_spec.html', context, context_instance=RequestContext(request))

def manufacturer_delete(request):
    man_id = request.POST.get('man_id', None)
    print man_id
    context = {}
    context['manufacturers'] = Manufacturer.objects.all()
    context['request'] = request.method
    print Manufacturer.objects.filter(pk=man_id)
    Manufacturer.objects.filter(pk=man_id).delete()
    if man_id != None:
        return HttpResponseRedirect('/manufacturer_list/')
    else:
        pass
    
    return render_to_response('manufacturer_delete.html', context, context_instance=RequestContext(request))

