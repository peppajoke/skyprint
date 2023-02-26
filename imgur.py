import requests
import credentials

def upload_image(image_path):
    """
    Uploads the image at the specified path to Imgur and returns the image URL.

    Args:
        image_path (str): The path to the image file to upload.
        client_id (str): The client ID for your Imgur application.

    Returns:
        str: The URL of the uploaded image.
    """
    # Open the image file and read the binary data
    with open(image_path, 'rb') as f:
        image_data = f.read()

    # Define the Imgur API endpoint URL for image upload
    endpoint = 'https://api.imgur.com/3/image'

    # Define the headers for the POST request, including the client ID
    headers = {'Authorization': f'Client-ID {credentials.imgur_client_id}'}

    # Define the data to send in the POST request
    data = {'image': image_data}

    # Send the POST request to upload the image to Imgur
    response = requests.post(endpoint, headers=headers, data=data)

    # Extract the image URL from the response JSON
    image_url = response.json()['data']['link']

    # Return the image URL
    return image_url
