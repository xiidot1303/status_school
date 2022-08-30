from django.forms import ModelForm
from app.models import *
from django import forms

offices = (
    ("", ""),
    (
        "Chilonzor tumani, Farhod bozori ro'parasi Oazis savdo markazi 2-qavati",
        "Chilonzor tumani, Farhod bozori ro'parasi Oazis savdo markazi 2-qavati",
        ),
    (
        "Yunusobod 3-mavze, Yangi shahar ko'chasi 4-bino. Mega planet",
        "Yunusobod 3-mavze, Yangi shahar ko'chasi 4-bino. Mega planet",
        ),
    (
        "Sergili 4-mavze, Qipchoq ko'chasi, Havas marketini yonida. Mo'ljal: Quddus sharif masjidi ro'parasi",
        "Sergili 4-mavze, Qipchoq ko'chasi, Havas marketini yonida. Mo'ljal: Quddus sharif masjidi ro'parasi",
        ),
    (
        "Samarqand shahar, Beruniy ko'chasi 67-uy. Mo'ljal: Temir yo'l vokzalidan Pavorotga qarab yurganda Elektr tarmoqlari binosida",
        "Samarqand shahar, Beruniy ko'chasi 67-uy. Mo'ljal: Temir yo'l vokzalidan Pavorotga qarab yurganda Elektr tarmoqlari binosida",
        ),
)

times = (
    ("", ""),
    (
        "9:00 dan 10:30 gacha",
        "9:00 dan 10:30 gacha",
        ),
    (
        "10:30 dan 12:00 gacha",
        "10:30 dan 12:00 gacha",
        ),
    (
        "14:00 dan 15:30 gacha",
        "14:00 dan 15:30 gacha",
        ),
    (
        "15:30 dan 17:00 gacha",
        "15:30 dan 17:00 gacha",
        ),
)

degrees = (
    ("", ""),
    (2, "2-sinf"),
    (3, "3-sinf"),
    (4, "4-sinf"),
    (5, "5-sinf"),
    (6, "6-sinf"),
)

class ApplicationForm(ModelForm):
    class Meta:
        model = Application
        fields = {
            "name",
            "degree",
            "phone",
            "office",
            "time",
            "payment",
            "address"
        }

        labels = {
            "name": "O'quvchi ismi",
            "degree": "O'quvchi sinfi",
            "phone": "Telefon raqamingiz",
            "office": "Qaysi filialimiz sizga qulay?",
            "time": "Qaysi payt siz uchun qulay?",
            "payment": "Sizga qulay bo'lgan oylik to'lov",
            "address": "Yashash manzilingiz"
        }

        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control mb-5"}),
            "degree": forms.Select(choices=degrees, attrs={"class": "custom-select form-control mb-5 choicesjs"}),
            "phone": forms.TextInput(attrs={"class": "form-control mb-5", "placeholder": "+998991234567"}),
            "office": forms.Select(choices=offices, attrs={"class": "custom-select form-control mb-5 choicesjs"}),
            "time": forms.Select(choices=times, attrs={"class": "custom-select form-control mb-5 choicesjs"}),
            "payment": forms.TextInput(attrs={"class": "form-control mb-5"}),
            "address": forms.TextInput(attrs={"class": "form-control mb-5"}),
        }
    
    field_order = [
        "name",
        "degree",
        "phone",
        "office",
        "time",
        "payment",
        "address"
    ]