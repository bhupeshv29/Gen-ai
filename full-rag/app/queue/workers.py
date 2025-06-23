from ..db.collections.files import files_collection
from bson import ObjectId
import os
from pdf2image import convert_from_path
import base64
from openai import OpenAI


client = OpenAI(
    api_key="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"
)


def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")


async def process_file(id: str, file_path: str):
    await files_collection.update_one({"_id": ObjectId(id)}, {
        "$set": {
            "status": "processing"
        }
    })

    await files_collection.update_one({"_id": ObjectId(id)}, {
        "$set": {
            "status": "converting to images"
        }
    })

    # Step1: Convert the PDF - Image
    pages = convert_from_path(file_path)
    images = []

    for i, page in enumerate(pages):
        image_save_path = f"/mnt/uploads/images/{id}/image-{i}.jpg"
        os.makedirs(os.path.dirname(image_save_path), exist_ok=True)
        page.save(image_save_path, 'JPEG')
        images.append(image_save_path)

    await files_collection.update_one({"_id": ObjectId(id)}, {
        "$set": {
            "status": "converting to images successs"
        }
    })

    images_base64 = [encode_image(img) for img in images]

    result = client.responses.create(
        model="gpt-4.1",
        input=[
            {
                "role": "user",
                "content": [
                    {"type": "input_text",
                        "text": "Based on the resume below, Roast this resume"},
                    {
                        # flake8: noqa
                        "type": "input_image",
                        "image_url": f"data:image/jpeg;base64,{images_base64[0]}",
                    },
                ],
            }
        ],
    )

    await files_collection.update_one({"_id": ObjectId(id)}, {
        "$set": {
            "status": "processed",
            "result": result.output_text
        }
    })

    # queue: Email Queue - Your file is ready
