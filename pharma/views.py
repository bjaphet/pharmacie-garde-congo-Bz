from django.shortcuts import render
from .models import Pharmacie, Ville, Periode, GardePharmacie
from .forms import FilterForm

# def afficher_pharmacies(request):
#     pharmacies = []
#     form = FilterForm()

#     if request.method == 'POST':
#         form = FilterForm(request.POST)
#         if form.is_valid():
#             ville = form.cleaned_data['ville']
#             periode = form.cleaned_data['periode']

#             # Récupérer les pharmacies qui se trouvent dans la ville sélectionnée
#             pharmacies = Pharmacie.objects.filter(ville=ville)

#             # Filtrer les pharmacies qui sont de garde pendant la période sélectionnée
#             pharmacies_de_garde = GardePharmacie.objects.filter(periode=periode, pharmacie__in=pharmacies)
#             pharmacies = [garde.pharmacie for garde in pharmacies_de_garde]

#     return render(request, 'afficher_pharmacies.html', {'form': form, 'pharmacies': pharmacies})


def form_pharmacies(request):
    form = FilterForm()
    return render(request, 'formulaire.html', {'form': form})



from django.shortcuts import render
from .models import Pharmacie, Ville, Periode, GardePharmacie
from .forms import FilterForm

def resultat_pharmacies(request):
    pharmacies = []
    ville_id = request.GET.get('ville')
    periode_id = request.GET.get('periode')

    if ville_id and periode_id:
        ville = Ville.objects.get(id=ville_id)
        periode = Periode.objects.get(id=periode_id)

        # Récupérer les pharmacies dans la ville sélectionnée
        pharmacies = Pharmacie.objects.filter(ville=ville)

        # Filtrer les pharmacies qui sont de garde pendant la période sélectionnée
        pharmacies_de_garde = GardePharmacie.objects.filter(periode=periode, pharmacie__in=pharmacies)
        pharmacies = [garde.pharmacie for garde in pharmacies_de_garde]

    return render(request, 'resultat.html', {'pharmacies': pharmacies})
