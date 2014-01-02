from templating import Template, error_page
from utils import request_arg, optional_request_arg as ora
from django.http import HttpResponse
from django.core.context_processors import csrf
from django.models import Supplier, Item

def get_item(request):
    item_id = request_arg(request, "item_id")
    return Item.objects.get(id=item_id)

def set_item(request):
    """ If item exists, update item. Else, create new item """
    item = None
    item_id = ora(request, "item_id")
    if item_id:
        try: item = Item.objects.get(id=item_id)
        except:item = Item()
    else:
        item = Item()
    item.product_name = ora(request, "product_name")
    if ora(request, "in_stock"): item.in_stock = True
    else: item.in_stock = False
    item.wholesale_price = "%s %s" % (ora(request, "wholesale_price"), ora(request, "price_units"))
    item.fabric_width = "%s %s" % (ora(request, "fabric_width"), ora(request, "width_units"))
    item.textile_types = ora(request, "textile_types")
    item.weave_types = ora(request, "weave_types")
    item.save()

def delete_item(request):
    return HttpResponse("SUCCESS DELETE ITEM")

def get_items(request):
    #TODO: uncomment after account functionality built; current return is for demo
    #sup = Supplier.objects.get(id=request_arg(request, "supplier_id"))
    #return Item.objects.all(supplier=sup)
    return Item.objects.all() 
 