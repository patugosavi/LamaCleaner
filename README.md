# LamaCleaner

Image Inpainting 

python version 3.10.7

Original Code :- https://github.com/Sanster/lama-cleaner

1)Open project folder (lamacleaner)

2)create environment

py -m venv virenv

Set-ExecutionPolicy -Scope CurrentUser

1

.\virenv\Scripts\activate

pip install django

3)requirements

pip install -r requirements.txt

4)Run-

python manage.py runserver

5)Output (Open postman)

Method - POST

http://127.0.0.1:8000/inpainting/image/inpainting

Keys and valuse:-  (add image default path)

input_image:C:\Users\ADMIN\Downloads\ImageInpaintingusingOpenCV\inpainting\resources\image6.jpg
mask_image:C:\Users\ADMIN\Downloads\ImageInpaintingusingOpenCV\inpainting\resources\mask6.jpg
userid:7


Note :-Use only lama SOTA AI model. If you want to change SOTA AI models then check test_model.py 

