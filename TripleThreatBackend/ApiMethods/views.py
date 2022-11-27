from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from ApiMethods.models import *

from ApiMethods.serializers import *

@csrf_exempt
def AbcClientApi(request,id = 0):
    if request.method== 'GET':
        abcclient = AbcClient.objects.all()
        AbcClient_Serializer = AbcClientSerializer(abcclient, many = True)
        return JsonResponse(AbcClient_Serializer.data, safe = False)
    elif request.method== 'POST':
        AbcClient_data = JSONParser().parse(request)
        AbcClient_Serializer = AbcClientSerializer(data = AbcClient_data)
        if AbcClient_Serializer.is_valid():
            AbcClient_Serializer.save()
            return JsonResponse("Added Successfully", safe= False)
        return JsonResponse("Failed to add", safe= False)
    elif request.method== 'PUT':
        AbcClient_data = JSONParser().parse(request)
        abcclient = AbcClient.objects.get(abc_client_id = AbcClient_data['abc_client_id'])
        AbcClient_Serializer = AbcClientSerializer(abcclient, data= AbcClient_data)
        if AbcClient_Serializer.is_valid():
            AbcClient_Serializer.save()
            return JsonResponse("Updated Successfully", safe= False)
        return JsonResponse("Failed to Update", safe= False)
    elif request.method == 'DELETE':
        abcclient = AbcClient.objects.get(abc_client_id = id)
        AbcClient.delete(abcclient)
        return JsonResponse("Deleted Successfully", safe= False)    





@csrf_exempt
def AbcResourceApi(request,id = 0):
    if request.method== 'GET':
        abcresource = AbcResource.objects.all()
        AbcResource_Serializer = AbcResourceSerializer(abcresource, many = True)
        return JsonResponse(AbcResource_Serializer.data, safe = False)
    elif request.method== 'POST':
        AbcResource_data = JSONParser().parse(request)
        AbcResource_Serializer = AbcResourceSerializer(data = AbcResource_data)
        if AbcResource_Serializer.is_valid():
            AbcResource_Serializer.save()
            return JsonResponse("Added Successfully", safe= False)
        return JsonResponse("Failed to add", safe= False)
    elif request.method== 'PUT':
        AbcResource_data = JSONParser().parse(request)
        abcresource = AbcResource.objects.get(abc_resource_id = AbcResource_data['abc_resource_id'])
        AbcResource_Serializer = AbcResourceSerializer(abcresource, data= AbcResource_data)
        if AbcResource_Serializer.is_valid():
            AbcResource_Serializer.save()
            return JsonResponse("Updated Successfully", safe= False)
        return JsonResponse("Failed to Update", safe= False)
    elif request.method == 'DELETE':
        abcresource = AbcResource.objects.get(abc_resource_id = id)
        AbcResource.delete(abcresource)
        return JsonResponse("Deleted Successfully", safe= False)    




@csrf_exempt
def AccessLogApi(request,id = 0):
    if request.method== 'GET':
        accesslog = AccessLog.objects.all()
        AccessLog_Serializer = AccessLogSerializer(accesslog, many = True)
        return JsonResponse(AccessLog_Serializer.data, safe = False)
    elif request.method== 'POST':
        AccessLog_data = JSONParser().parse(request)
        AccessLog_Serializer = AccessLogSerializer(data = AccessLog_data)
        if AccessLog_Serializer.is_valid():
            AccessLog_Serializer.save()
            return JsonResponse("Added Successfully", safe= False)
        return JsonResponse("Failed to add", safe= False)
    elif request.method== 'PUT':
        AccessLog_data = JSONParser().parse(request)
        accesslog = AccessLog.objects.get(access_log_id = AccessLog_data['access_log_id'])
        AccessLog_Serializer = AccessLogSerializer(accesslog, data= AccessLog_data)
        if AccessLog_Serializer.is_valid():
            AccessLog_Serializer.save()
            return JsonResponse("Updated Successfully", safe= False)
        return JsonResponse("Failed to Update", safe= False)
    elif request.method == 'DELETE':
        accesslog = AccessLog.objects.get(access_log_id = id)
        AccessLog.delete(accesslog)
        return JsonResponse("Deleted Successfully", safe= False)    



@csrf_exempt
def AddressApi(request,id = 0):
    if request.method== 'GET':
        address = Address.objects.all() if id == 0 else Address.objects.get(address_id = id)
        Address_Serializer = AddressSerializer(address, many = True if id == 0 else False)
        return JsonResponse(Address_Serializer.data, safe = False)
    elif request.method== 'POST':
        Address_data = JSONParser().parse(request)
        Address_Serializer = AddressSerializer(data = Address_data)
        if Address_Serializer.is_valid():
            Address_Serializer.save()
            return JsonResponse("Added Successfully", safe= False)
        return JsonResponse("Failed to add", safe= False)
    elif request.method== 'PUT':
        Address_data = JSONParser().parse(request)
        address = Address.objects.get(address_id = Address_data['address_id'])
        Address_Serializer = AddressSerializer(address, data= Address_data)
        if Address_Serializer.is_valid():
            Address_Serializer.save()
            return JsonResponse("Updated Successfully", safe= False)
        return JsonResponse("Failed to Update", safe= False)
    elif request.method == 'DELETE':
        address = Address.objects.get(address_id = id)
        Address.delete(address)
        return JsonResponse("Deleted Successfully", safe= False)    



@csrf_exempt
def ClientContactsApi(request,id = 0):
    if request.method== 'GET':
        clientcontacts = ClientContacts.objects.all()
        ClientContacts_Serializer = ClientContactsSerializer(clientcontacts, many = True)
        return JsonResponse(ClientContacts_Serializer.data, safe = False)
    elif request.method== 'POST':
        ClientContacts_data = JSONParser().parse(request)
        ClientContacts_Serializer = ClientContactsSerializer(data = ClientContacts_data)
        if ClientContacts_Serializer.is_valid():
            ClientContacts_Serializer.save()
            return JsonResponse("Added Successfully", safe= False)
        return JsonResponse("Failed to add", safe= False)
    elif request.method== 'PUT':
        ClientContacts_data = JSONParser().parse(request)
        clientcontacts = ClientContacts.objects.get(client_contact_id = ClientContacts_data['client_contact_id'])
        ClientContacts_Serializer = ClientContactsSerializer(clientcontacts, data= ClientContacts_data)
        if ClientContacts_Serializer.is_valid():
            ClientContacts_Serializer.save()
            return JsonResponse("Updated Successfully", safe= False)
        return JsonResponse("Failed to Update", safe= False)
    elif request.method == 'DELETE':
        clientcontacts = ClientContacts.objects.get(client_contact_id = id)
        ClientContacts.delete(clientcontacts)
        return JsonResponse("Deleted Successfully", safe= False)    




@csrf_exempt
def ContactApi(request,id = 0):
    if request.method== 'GET':
        contact = Contact.objects.all()
        Contact_Serializer = ContactSerializer(contact, many = True)
        return JsonResponse(Contact_Serializer.data, safe = False)
    elif request.method== 'POST':
        Contact_data = JSONParser().parse(request)
        Contact_Serializer = ContactSerializer(data = Contact_data)
        if Contact_Serializer.is_valid():
            Contact_Serializer.save()
            return JsonResponse("Added Successfully", safe= False)
        return JsonResponse("Failed to add", safe= False)
    elif request.method== 'PUT':
        Contact_data = JSONParser().parse(request)
        contact = Contact.objects.get(contact_id = Contact_data['contact_id'])
        Contact_Serializer = ContactSerializer(contact, data= Contact_data)
        if Contact_Serializer.is_valid():
            Contact_Serializer.save()
            return JsonResponse("Updated Successfully", safe= False)
        return JsonResponse("Failed to Update", safe= False)
    elif request.method == 'DELETE':
        contact = Contact.objects.get(contact_id = id)
        Contact.delete(contact)
        return JsonResponse("Deleted Successfully", safe= False)    





@csrf_exempt
def InventoryApi(request,id = 0):
    if request.method== 'GET':
        objects = Inventory.objects.select_related('abc_client', "storage_type")
        inventory = objects.all() if id == 0 else objects.get(inventory_id = id)
        Inventory_Serializer = InventorySerializer(inventory, many = True if id == 0 else False)
        # inventory = Inventory.objects.all()
        # Inventory_Serializer = InventorySerializer(inventory, many = True)
        return JsonResponse(Inventory_Serializer.data, safe = False)
    elif request.method== 'POST':
        Inventory_data = JSONParser().parse(request)
        Inventory_Serializer = InventorySerializer(data = Inventory_data)
        if Inventory_Serializer.is_valid():
            Inventory_Serializer.save()
            return JsonResponse("Added Successfully", safe= False)
        return JsonResponse("Failed to add", safe= False)
    elif request.method== 'PUT':
        Inventory_data = JSONParser().parse(request)
        inventory = Inventory.objects.get(inventory_id = Inventory_data['inventory_id'])
        Inventory_Serializer = InventorySerializer(inventory, data= Inventory_data)
        if Inventory_Serializer.is_valid():
            Inventory_Serializer.save()
            return JsonResponse("Updated Successfully", safe= False)
        return JsonResponse("Failed to Update", safe= False)
    elif request.method == 'DELETE':
        inventory = Inventory.objects.get(inventory_id = id)
        Inventory.delete(inventory)
        return JsonResponse("Deleted Successfully", safe= False)    




@csrf_exempt
def ResourceTypeApi(request,id = 0):
    if request.method== 'GET':
        resourcetype = ResourceType.objects.all() if id == 0 else resourcetype.objects.get(resource_id = id)
        ResourceType_Serializer = ResourceTypeSerializer(resourcetype, many = True if id == 0 else False)

        # resourcetype = ResourceType.objects.all()
        # ResourceType_Serializer = ResourceType(resourcetype, many = True)
        return JsonResponse(ResourceType_Serializer.data, safe = False)
    elif request.method== 'POST':
        ResourceType_data = JSONParser().parse(request)
        ResourceType_Serializer = ResourceType(data = ResourceType_data)
        if ResourceType_Serializer.is_valid():
            ResourceType_Serializer.save()
            return JsonResponse("Added Successfully", safe= False)
        return JsonResponse("Failed to add", safe= False)
    elif request.method== 'PUT':
        ResourceType_data = JSONParser().parse(request)
        resourcetype = ResourceType.objects.get(resource_type_id = ResourceType_data['resource_type_id'])
        ResourceType_Serializer = ResourceType(resourcetype, data= ResourceType_data)
        if ResourceType_Serializer.is_valid():
            ResourceType_Serializer.save()
            return JsonResponse("Updated Successfully", safe= False)
        return JsonResponse("Failed to Update", safe= False)
    elif request.method == 'DELETE':
        resourcetype = ResourceType.objects.get(resource_type_id = id)
        ResourceType.delete(resourcetype)
        return JsonResponse("Deleted Successfully", safe= False)    




@csrf_exempt
def StorageTypeApi(request,id = 0):
    if request.method== 'GET':
        storagetype = StorageType.objects.all() if id == 0 else storagetype.objects.get(storage_id = id)
        StorageType_Serializer = StorageTypeSerializer(storagetype, many = True if id == 0 else False)
        # storagetype = StorageType.objects.all()
        # StorageType_Serializer = StorageTypeSerializer(storagetype, many = True)
        return JsonResponse(StorageType_Serializer.data, safe = False)
    elif request.method== 'POST':
        StorageType_data = JSONParser().parse(request)
        StorageType_Serializer = StorageTypeSerializer(data = StorageType_data)
        if StorageType_Serializer.is_valid():
            StorageType_Serializer.save()
            return JsonResponse("Added Successfully", safe= False)
        return JsonResponse("Failed to add", safe= False)
    elif request.method== 'PUT':
        StorageType_data = JSONParser().parse(request)
        storagetype = StorageType.objects.get(storage_type_id = StorageType_data['storage_type_id'])
        StorageType_Serializer = StorageTypeSerializer(storagetype, data= StorageType_data)
        if StorageType_Serializer.is_valid():
            StorageType_Serializer.save()
            return JsonResponse("Updated Successfully", safe= False)
        return JsonResponse("Failed to Update", safe= False)
    elif request.method == 'DELETE':
        storagetype = StorageType.objects.get(storage_type_id = id)
        StorageType.delete(storagetype)
        return JsonResponse("Deleted Successfully", safe= False)    




