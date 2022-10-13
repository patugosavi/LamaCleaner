from django.shortcuts import render


from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view

import datetime

from pathlib import Path

import cv2
import pytest
import torch

from lama_cleaner.model_manager import ModelManager
from lama_cleaner.schema import Config, HDStrategy, LDMSampler, SDSampler

# Create your views here.


current_dir = Path(__file__).parent.absolute().resolve()
save_dir = current_dir / 'inpaintingresult'
save_dir.mkdir(exist_ok=True, parents=True)


@api_view(['POST',])
def lamaCleaner(request):
    if request.method == "POST":
        input_image = request.POST['input_image']
        mask_image = request.POST['mask_image']
        userid=request.POST['userid']

        imagename=f"inpaint_{userid}.png"
        model = ModelManager(name="lama", device="cpu")
        img = cv2.imread(str(input_image))
        img = cv2.cvtColor(img, cv2.COLOR_BGRA2RGB)
        mask = cv2.imread(str(mask_image), cv2.IMREAD_GRAYSCALE)

        res = model(img, mask, get_config(HDStrategy.RESIZE))  #you can use three types of strategy (CROP,RESIZE,ORIGINAL)
        cv2.imwrite(
            str(save_dir / imagename),
            res,
            [int(cv2.IMWRITE_JPEG_QUALITY), 100, int(cv2.IMWRITE_PNG_COMPRESSION), 0],
        )

        response = {
                    'status':200,
                    'message': "success",
                    'User':imagename
                    }

        return JsonResponse(response,safe=False)

def get_config(strategy, **kwargs):
    data = dict(
        ldm_steps=1,
        ldm_sampler=LDMSampler.plms,
        hd_strategy=strategy,
        hd_strategy_crop_margin=32,
        hd_strategy_crop_trigger_size=200,
        hd_strategy_resize_limit=200,
    )
    data.update(**kwargs)
    return Config(**data)

