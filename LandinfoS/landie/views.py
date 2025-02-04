from django.shortcuts import render, get_object_or_404
from .models import LandRecord
import joblib
from django.http import JsonResponse
import openai

def home(request):
    records = LandRecord.objects.all()
    return render(request, 'landie/home.html', {'records': records})

def land_detail(reuest, pk):
    record = get_object_or_404(LandRecord, pk=pk)
    return render(request, 'landie/land_detail.html', {'record': record})

def register(request):
    return render(request, 'landie/register.html')

# Load the trained model
model = joblib.load('ml/land_price_model.pkl')

def predict_price(request):
    if request.method == "POST":
        area = float(request.POST['area_sqft'])
        land_type = 1 if request.POST['land_type'] == 'Residential' else 0

        prediction = model.predict([[area, land_type]])

        return render(request, 'predict_price.html', {'predicted_price': prediction[0]})

    return render(request, 'predict_price.html')

def chatbot_response(request):
    if request.method == "POST":
            user_message = request.POST.get('message')
            openai.api_key = "Valid API key to be set"
            response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "user", "content": user_message}]
            )

            return JsonResponse({"response": response.choices[0].message['content']})
        return JsonResponse({"error": "Invalid request"})
