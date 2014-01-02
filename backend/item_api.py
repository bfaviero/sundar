from templating import Template, error_page
from utils import request_arg, optional_request_arg as ora, optional_string_request_arg as osra
from django.http import HttpResponse
from django.core.context_processors import csrf
from django.shortcuts import redirect
from s3_api import upload_image
from models import Supplier, Item
def get_item(request):
    item_id = request_arg(request, "item_id")
    return Item.objects.get(id=item_id)

def set_item(request):
    """ If item exists, update item. Else, create new item """
    item = None
    item_id = ora(request, "item_id")
    #TODO: supplier = ora(request, "supplier_id")
    supplier_id = ora(request, "supplier_id")
    if not supplier_id:
        supplier_id = "TEST"
    if item_id:
        try: 
            item = Item.objects.get(id=item_id)
        except:
            item = Item()
    else:
        item = Item()
    item.product_name = osra(request, "product_name")
    #TODO: item.supplier = Supplier().objects.get(supplier_id)
    if ora(request, "in_stock"): item.in_stock = True
    else: item.in_stock = False
    item.wholesale_price = osra(request, "wholesale_price")
    item.wholesale_price_units = osra(request, "price_units")
    item.fabric_width = osra(request, "fabric_width")
    item.fabric_width_units = osra(request, "width_units")
    item.textile_type = osra(request, "textile_type")
    item.weave_type = osra(request, "weave_type")
    #TODO set image url image1_url
    if request.FILES.get('image'):
        item = _add_image(request.FILES['image'], supplier_id, item)
    item.save()
    return redirect("/mobile/product_list")

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
    #TODO: uncomment after account functionality built; current return is for demo
    #sup = Supplier.objects.get(id=request_arg(request, "supplier_id"))
    #return Item.objects.all(supplier=sup)
    return Item.objects.all() 
 