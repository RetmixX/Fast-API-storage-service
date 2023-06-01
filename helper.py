import json
import string
connection_url = f"postgresql://{{USER}}:{{PASSWORD}}@{{HOST}}:5432/{{DB}}"
api_key = "{{API_KEY}}"
url = "https://stablediffusionapi.com/api/v3/text2img"
header = {'Content-Type': 'application/json'}


def get_body(text: string):
    return json.dumps({
        "key": api_key,
        "prompt": text,
        "negative_prompt": None,
        "width": "512",
        "height": "512",
        "samples": "1",
        "num_inference_steps": "20",
        "seed": None,
        "guidance_scale": 7.5,
        "safety_checker": "yes",
        "multi_lingual": "no",
        "panorama": "no",
        "self_attention": "no",
        "upscale": "no",
        "embeddings_model": "embeddings_model_id",
        "webhook": None,
        "track_id": None
    })
