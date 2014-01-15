from templating import Template, error_page
from decimal import Decimal
from utils import request_arg, optional_request_arg as ora, optional_string_request_arg as osra
from django.http import HttpResponse
from django.core.context_processors import csrf
from django.shortcuts import redirect
from s3_api import upload_image
from models import Supplier, Item
from django.contrib.auth.signals import user_logged_in, user_logged_out

def get_item(request, item_id):
    return Item.objects.get(id=item_id)

def set_item(request, item_id):
    if item_id:
        try:
            item = Item.objects.get(id=item_id)
        except:
            item = Item()
    else:
        item = Item()
    item.product_name = osra(request, "product_name")
    item.product_code = osra(request, "product_code")
    #TO TURN ACCOUNTS ON, exchange request.user.email_addr for ACCOUNTS_OFF_EMAIL in lines below
    #ACCOUNTS_OFF_EMAIL = 'jagkgill@gmail.com'
    item.supplier = Supplier.objects.get(email_addr=request.user.email_addr)
    #boolean value
    item.in_stock = ora(request, "in_stock") if ora(request, "in_stock") else False
    item.made_to_order = ora(request, "made_to_order") if ora(request, "made_to_order") else False
    item.reorder_av = ora(request, "reorder_av") if ora(request, "reorder_av") else False
    lead_time_unit = osra(request, "lead_time_unit")
    item.lead_time = lead_time(Decimal(osra(request, "lead_time")), lead_time_unit)
    item.wholesale_price = Decimal(osra(request, "wholesale_price"))
    item.wholesale_price_units = osra(request, "price_units")
    item.volume_discount = osra(request, "volume_discount")
    item.fabric_width = Decimal(osra(request, "fabric_width"))
    item.fabric_width_units = osra(request, "width_units")
    item.material_type = osra(request, "material_type")
    item.fiber_type = osra(request, "fiber_type")
    item.textile_type = osra(request, "textile_type")
    item.weave_type = osra(request, "weave_type")
    item.weight = osra(request, "weight")
    item.weight_units = osra(request, "weight_units")
    item.color = osra(request, "color")
    item.country_origin = osra(request, "country_origin")
    #TODO set image url image1_url
    #TO TURN ACCOUNTS ON

    if request.FILES.get('image1'):
        item = _add_image(request.FILES['image1'], request.user.email_addr, item)
    if request.FILES.get('image2'):
        item = _add_image(request.FILES['image2'], request.user.email_addr, item)
    if request.FILES.get('image3'):
        item = _add_image(request.FILES['image3'], request.user.email_addr, item)
    if request.FILES.get('image4'):
        item = _add_image(request.FILES['image4'], request.user.email_addr, item)
    item.save()
    return redirect("/mobile/product_list")
def lead_time(time, units):
    '''lead time is stored in days, so convert appropriately'''
    if units=="weeks":
        return time*3
    elif units=="months":
        return time*30
    else:
        return time

def _add_image(image, supplier_id, item):
    url = upload_image(image, supplier_id, item.product_name)
    if not item.image1_url: item.image1_url = url
    elif not item.image2_url: item.image2_url = url
    elif not item.image3_url: item.image3_url = url
    elif not item.image4_url: item.image4_url = url
    elif not item.image5_url: item.image5_url = url
    return item

def delete_item(request):
    return HttpResponse("SUCCESS DELETE ITEM")

def get_items(request):
    return Item.objects.filter(supplier=request.user)

def get_all_items(request):
    return Item.objects.all()
