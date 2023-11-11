from django.http import HttpResponse
from django.shortcuts import render
from measurements.services import FakeMeasurementService

# Create your views here.
def list(request) -> HttpResponse:
    results = FakeMeasurementService.list()
    return render(
        request=request,
        template_name="measurements/measurements.html",
        context={"list_of_measurements": results}
    )

def measurements_details(request, id: int):
    pass