from hubspot.crm.contacts import SimplePublicObjectInput
from hubspot.crm.contacts.exceptions import ApiException
from hubspot import HubSpot

api_key = "290c3d3a-e931-49d6-9fa2-11b1f6d0ad15"

ex_id = '3388551'


def create_contact(first_name, last_name, email):
    try:
        api_client = HubSpot(api_key=api_key)
        simple_public_object_input = SimplePublicObjectInput(
            properties={"email": email, "firstname": first_name, "lastname": last_name}
        )
        api_response = api_client.crm.contacts.basic_api.create(
            simple_public_object_input=simple_public_object_input
        )
        return api_response
    except ApiException as e:
        print("Exception when creating contact: %s\n" % e)


def get_contact(contact_id):
    try:
        api_client = HubSpot(api_key=api_key)
        contact_fetched = api_client.crm.contacts.basic_api.get_by_id(contact_id)
        return contact_fetched
    except ApiException as e:
        print("Exception when requesting contact by id: %s\n" % e)


def get_all_contact():
    try:
        api_client = HubSpot(api_key=api_key)
        all_contacts = api_client.crm.contacts.get_all()
        return all_contacts
    except ApiException as e:
        print("Exception when requesting contact by id: %s\n" % e)
