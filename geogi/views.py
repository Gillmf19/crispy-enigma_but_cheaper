from django.shortcuts import render
from geopy.geocoders import Nominatim
from .models import Ubicacion

def home(request):
    mensaje_error = None

    if request.method == "POST":
        direccion = request.POST.get("direccion")

        if direccion:
            try:
                geolocator = Nominatim(user_agent="geogi_app")
                location = geolocator.geocode(direccion, timeout=10)

                if location:
                    Ubicacion.objects.create(
                        direccion=direccion,
                        latitud=location.latitude,
                        longitud=location.longitude
                    )
                else:
                    mensaje_error = "No se pudo encontrar la ubicación."
            except Exception:
                mensaje_error = "Error al conectar con el servicio de geocodificación."

    ubicaciones = Ubicacion.objects.all().order_by("-fecha_consulta")

    return render(request, "geogi/index.html", {
        "ubicaciones": ubicaciones,
        "mensaje_error": mensaje_error
    })