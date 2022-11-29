from rest_framework import serializers

from ApiMethods.models import (AbcClient, AbcResource, AccessLog, Address, ClientContacts, Contact, Inventory, ResourceType, StorageType)


class AbcClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = AbcClient 
        fields = ['abc_client_id',
                  'client_name',
                  'company_address',
                  'phone_number',
                  'created_by',
                  'created_date',
                  'modified_by',
                  'modified_date',
                  'is_deleted']


class AbcResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = AbcResource 
        fields = ['abc_resource_id',
                  'inventory',
                  'resource_type',
                  'resource_name',
                  'max_number_of_resources',
                  'current_number_of_resources',
                  'created_by',
                  'created_date',
                  'modified_by',
                  'modified_date',
                  'is_deleted']


class AccessLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccessLog
        fields = ['access_log_id',
                  'username',
                  'action',
                  'table_name',
                  'field_name',
                  'screen_name',
                  'log_time']


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['address_id',
                  'state',
                  'address_line_1',
                  'address_line_2',
                  'country',
                  'postal_code',
                  'city',
                  'created_by',
                  'created_date',
                  'modified_by',
                  'modified_date',
                  'is_deleted']


class ClientContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientContacts
        fields = ['client_contacts_id',
                  'abc_cleint',
                  'contact',
                  'created_by',
                  'created_date',
                  'modified_by',
                  'modified_date',
                  'is_deleted']


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact 
        fields = ['contact_id',
                  'email_address',
                  'phone_number',
                  'first_name',
                  'last_name',
                  'middle_name',
                  'created_by',
                  'created_date',
                  'modified_by',
                  'modified_date',
                  'is_deleted']


class InventorySerializerWithRelatedFields(serializers.ModelSerializer):
    class Meta:
        model = Inventory 
        fields = ['inventory_id',
                #   'abc_client.client_name',
                  'abc_client',
                  'inventory_name',
                  'storage_type',
                #   'storage_type.type_name',
                  'max_item_capacity',

                  'address',
                  'created_by',
                  'created_date',
                  'modified_by',
                  'modified_date',
                  'is_deleted']
        depth = 1

class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory 
        fields = ['inventory_id',
                  'abc_client',
                  'inventory_name',
                  'storage_type',
                  'max_item_capacity',
                  'address',
                  'created_by',
                  'created_date',
                  'modified_by',
                  'modified_date',
                  'is_deleted']

class ResourceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResourceType 
        fields = ['resource_type_id',
                  'type_name',
                  'created_by',
                  'created_date',
                  'modified_by',
                  'modified_date',
                  'is_deleted']


class StorageTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = StorageType 
        fields = ['storage_type_id',
                  'type_name',
                  'created_by',
                  'created_date',
                  'modified_by',
                  'modified_date',
                  'is_deleted']







