# Requires "requests" to be installed (see python-requests.org)
import requests
import cv2
from PIL import Image

def bg():
    response = requests.post(
        'https://ja.clippingmagic.com/api/v1/images',
        files={'image': open("face/face.png", 'rb')},
        data={
            'format': 'result',
            'test': 'true', # TODO: Remove for production
            # TODO: Add more upload options here
            'background.color': '#FFFFFF'
        },
        headers={
            'Authorization':
            'Basic MTE1MTI6aDJ1Zzd2MWpzdTUwZXRvOGJoajF1dGliZWN2NDZmdjloMHN1M3Y3YnFlam1rZ2YzaTUxOA=='
        },
    )
    if response.status_code == requests.codes.ok:
        # Store these if you want to be able to use the Smart Editor
        image_id = response.headers['x-amz-meta-id']
        image_secret = response.headers['x-amz-meta-secret']

        with open("face/face.png", 'wb') as out:
            out.write(response.content)
    else:
        print("Error:", response.status_code, response.text)