from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Establishment
from elasticsearch_dsl import Search
from django.urls import reverse
from django.http import HttpResponseBadRequest


@login_required
def dashboard(request):
    if not request.user.is_authenticated:
        return redirect("index")
    user = request.user
    message = request.GET.get("message", "")
    # establishment = Establishment.objects.filter(establishment_adm=user.id)
    return render(
        request,
        "dashboard/dashboard.html",
        {
            "user": user,
            "message": message,
            # "establishment": establishment,
        },
    )


def search_view(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Método não permitido")

    term_search = request.POST.get("establishment")

    if term_search:
        s_exact = Search(index="establishment_index").query(
            "match", establishment_name=term_search
        )
        results_exact = s_exact.execute()

        if results_exact.hits.total.value > 0:
            results = [
                Establishment.objects.get(establishment_id=hit.establishment_id)
                for hit in results_exact
            ]
            return render(
                request,
                "establishment/results.html",
                {"results": results, "term": term_search},
            )
        #         if results_exact.hits.total.value > 0: # RETORNA PRODUTOS JUNTO
        #             establishments = [Establishment.objects.get(establishment_id=hit.establishment_id) for hit in results_exact]
        #             results = [(establishment, establishment.product_set.all()) for establishment in establishments]
        #             return render(request, "establishment/results.html", {"results": results})

        s_prefix = Search(index="establishment_index").query(
            "match_phrase_prefix", establishment_name=term_search
        )
        results_prefix = s_prefix.execute()

        if results_prefix.hits.total.value > 0:
            results = [
                Establishment.objects.get(establishment_id=hit.establishment_id)
                for hit in results_prefix
            ]
            return render(
                request,
                "establishment/results.html",
                {"results": results, "term": term_search},
            )
    #         if results_prefix.hits.total.value > 0:  # RETORNA PRODUTOS JUNTO
    #             establishments = [Establishment.objects.get(establishment_id=hit.establishment_id) for hit in results_prefix]
    #             results = [(establishment, establishment.product_set.all()) for establishment in establishments]
    #             return render(request, "establishment/results.html", {"results": results})

    message = "Estabelecimento não encontrado ou não existe nenhum estabelecimento com este nome!"
    url = reverse("establishment:dashboard") + f"?message={message}"
    return redirect(url)