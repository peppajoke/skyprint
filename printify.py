import requests
import json
import random
import base64
import credentials

t_shirt_blueprint_id = 145
shop_id = 5037938
swift_pod_id = 39
dark_color_tee_variant_ids = [38164, 38166, 38153, 38154, 63290, 42818, 38156, 38157, 38158, 38160, 38161, 38162, 38178, 38180, 38167, 38168, 63295, 42824, 38170, 38171, 38172, 38174, 38175, 38176, 38192, 38194, 38181, 38182, 63300, 42830, 38184, 38185, 38186, 38188, 38189, 38190, 38206, 38208, 38195, 38196, 63305, 42836, 38198, 38199, 38200, 38202, 38203, 38204, 38222, 38209, 38210, 63310, 42842, 38212, 38213, 38214, 38216, 38217, 38218, 42122, 42124, 42109, 42111, 42848, 42113, 42114, 42115, 42117, 42118, 42119]

def add_product(title, image_id):
    """
    Add a product to a Printify store using the Printify API.

    Args:
        product_data (dict): A dictionary containing the product data.

    Returns:
        dict: A dictionary representing the newly created product.
    """
    url = f'https://api.printify.com/v1/shops/{shop_id}/products.json'
    headers = {
        'Authorization': f'Bearer {credentials.printify_access_token}',
        'Content-Type': 'application/json'
    }
    payload = json.dumps(create_t_shirt_product_data(title, image_id))
    
    response = requests.post(url, headers=headers, data=payload)

    if response.status_code == 200:
        response_json = json.loads(response.text)
        return response_json
    else:
        print(response)
        raise ValueError(f"Failed to add product. Response code: {response.status_code}, response message: {response_json['message']}")

def get_all_blueprints():
    """
    Get all available blueprints from the Printify API using the provided API key.

    Returns:
        list: A list of dictionaries containing the blueprints available in the Printify API.
    """
    # Construct the API endpoint URL
    url = 'https://api.printify.com/v1/catalog/blueprints.json'

    # Set the API headers
    headers = {
        'Authorization': f'Bearer {credentials.printify_access_token}',
        'Content-Type': 'application/json'
    }

    # Send the HTTP GET request to the API
    response = requests.get(url, headers=headers)

    output = response.json()

    # Return the list of blueprints as a list of dictionaries
    return output

def get_printify_shops():
    url = 'https://api.printify.com/v1/shops.json'
    headers = {
        'Authorization': f'Bearer {credentials.printify_access_token}',
        'Content-Type': 'application/json'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        shops = response.json()
        return shops
    else:
        print(f'Request failed with status code {response.status_code}')

def create_t_shirt_product_data(title, image_id):
    # Store variant IDs
    variants = [{"id": num, "price": 1999, "is_enabled": True } for num in dark_color_tee_variant_ids]

    # Define product data fields
    product_data = {
    "title": title + " - T-Shirt",
    "description": title + "! Buy this T-Shirt today for only $19.99!",
    "blueprint_id": t_shirt_blueprint_id,
    "print_provider_id": swift_pod_id,
    "variants": variants,
      "print_areas": [
        {
          "variant_ids": dark_color_tee_variant_ids,
          "placeholders": [
            {
              "position": "front",
              "images": [
                  {
                    "id": image_id, 
                    "x": 0.5, 
                    "y": 0.2, 
                    "scale": 4,
                    "angle": 0
                  }
              ]
            }
          ]
        }
      ]
  }
    return product_data

def get_print_providers(blueprint_id):
    """
    Retrieves all print providers for a given blueprint on Printify using the Printify API.

    Args:
        api_key (str): Your Printify API key.
        blueprint_id (int): The ID of the blueprint you want to retrieve the print providers for.

    Returns:
        A list of dictionaries containing information about the print providers.
    """
    url = f'https://api.printify.com/v1/catalog/blueprints/{blueprint_id}/print_providers.json'
    headers = {'Authorization': f'Bearer {credentials.printify_access_token}'}

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        # Handle errors appropriately
        print(f'Error {response.status_code}: {response.content}')
        return None

def get_variants(blueprint_id, print_provider_id):
    """
    Retrieves all variants for a given print provider and blueprint on Printify using the Printify API.

    Args:
        blueprint_id (int): The ID of the blueprint you want to retrieve the variants for.
        print_provider_id (int): The ID of the print provider you want to retrieve the variants for.

    Returns:
        A list of dictionaries containing information about the variants.
    """
    url = f'https://api.printify.com/v1/catalog/blueprints/{blueprint_id}/print_providers/{print_provider_id}/variants.json'
    headers = {'Authorization': f'Bearer {credentials.printify_access_token}'}

    response = requests.get(url, headers=headers)
    output = response.json()
    if response.status_code == 200:
        return output
    else:
        # Handle errors appropriately
        print(f'Error {response.status_code}: {response.content}')
        return None

import requests

def upload_image(image_path):
    """
    Uploads an image to Printify using the Images endpoint.

    Args:
    - image_path: string, the file path of the image to upload

    Returns:
    - string, the ID of the uploaded image on Printify
    """

    # Set the endpoint URL and headers
    endpoint = 'https://api.printify.com/v1/uploads/images.json'
    headers = {
        'Authorization': f'Bearer {credentials.printify_access_token}',
    }

    # Open the image file and read its contents
    with open(image_path, 'rb') as f:
        binary_data = f.read()
        base64_data = base64.b64encode(binary_data)
        img_64 = base64_data.decode('utf-8')

    # Set the request data and files
    data = {
        'file_name': image_path,
        'contents': img_64,
    }

    # Send the POST request to Printify
    response = requests.post(endpoint, headers=headers, json=data)

    # Check the response status code and raise an exception if there was an error
    response.raise_for_status()

    # Parse the response JSON and return the image ID
    response_json = response.json()
    return response_json['id']

def get_blueprints(print_provider_id):
    """
    Get all blueprints for a given print provider on Printify API.

    :param print_provider_id: The ID of the print provider to get blueprints for.
    :param api_key: Your API key for accessing Printify API.
    :return: A list of blueprints for the given print provider.
    """
    url = f"https://api.printify.com/v1/catalog/print_providers/{print_provider_id}.json"
    headers = {"Authorization": f"Bearer {credentials.printify_access_token}"}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        blueprints = json.loads(response.text)
        return blueprints
    else:
        print(f"Error retrieving blueprints. Status code: {response.status_code}")


        import requests
import json

def publish_existing_product(product_id):
    # Build the Printify product data
    printify_product_url = f"https://api.printify.com/v1/shops/{shop_id}/products/{product_id}/publish.json"
    headers = {"Authorization": f"Bearer {credentials.printify_access_token}"}
    data = {
        "title": True,
        "description": True,
        "images": True,
        "variants": True,
        "tags": True,
        "keyFeatures": True,
        "shipping_template": True
    }

    # Publish the product on Printify
    response = requests.post(printify_product_url, headers=headers, json=data)
    if response.status_code == 200:
        print("Product published on Printify!")
    else:
        print(response)
        print("Error publishing product on Printify.")