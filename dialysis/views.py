from django.shortcuts import render
from .models import DialysisRecord


def index(request):

    result = None
    alert = None

    if request.method == "POST":

        date = request.POST.get("date")
        patient_id = request.POST.get("patient_id")
        name = request.POST.get("name")

        weight = float(request.POST.get("weight"))
        dw = float(request.POST.get("dw"))
        time = float(request.POST.get("time"))

        uf = weight - dw
        rate = uf / time

        if rate > 1:
            alert = "危険：除水速度が高すぎます"

        # DB保存
        DialysisRecord.objects.update_or_create(
            patient_id=patient_id,
            date=date,
            defaults={
                "name": name,
                "weight": weight,
                "dw": dw,
                "time": time,
                "uf": uf,
                "rate": rate
            }
        )

        result = {
            "uf": round(uf, 2),
            "rate": round(rate, 2)
        }

    return render(request, "dialysis/index.html", {
        "result": result,
        "alert": alert
    })


def history(request):
    records = DialysisRecord.objects.all().order_by("-date")
    return render(request, "dialysis/history.html", {"records": records})