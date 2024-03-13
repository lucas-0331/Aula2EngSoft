from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Establishment
from elasticsearch_dsl import Search
from django.urls import reverse
from django.http import HttpResponseBadRequest
from ..product.models import Category, Product
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


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
    if request.method == "POST":
        term_search = request.POST.get("establishment")

        if term_search:
            # Use uma única consulta para correspondência exata e de prefixo
            s_combined = Search(index="establishment_index").query(
                "multi_match", query=term_search, fields=["establishment_name", "establishment_name.keyword^5"]
            )
            results_combined = s_combined.execute()

            if results_combined.hits.total.value > 0:
                establishments = [
                    Establishment.objects.get(establishment_id=hit.establishment_id)
                    for hit in results_combined
                ]
                return render(
                    request,
                    "establishment/results.html",
                    {"results": establishments, "term": term_search},
                )

        message = "Estabelecimento não encontrado ou não existe nenhum estabelecimento com este nome!"
        url = reverse("establishment:dashboard") + f"?message={message}"
        return redirect(url)

    return redirect("establishment:dashboard")


def establishment_view(request, name, id):
    establishment = get_object_or_404(Establishment, establishment_id=id)
    products = Product.objects.filter(product_establishment=establishment)
    all_categories = Category.objects.all()
    categories_with_products = [
        category for category in all_categories if any(product.product_category == category for product in products)
    ]

    return render(
        request,
        "establishment/establishment.html",
        {"establishment": establishment, "products": products, "categories": categories_with_products},
    )



def administration_view(request, id, name):
    establishment = Establishment.objects.get(establishment_id=id)
    products = Product.objects.filter(product_establishment=id)
    categories = Category.objects.all()

    return render(
        request,
        "establishment/administration.html",
        {
            "products": products,
            "name": name,
            "establishment": establishment,
            "categories": categories,
        },
    )


def order_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            product_data = data.get('product', [])

            # Recuperar os objetos Product correspondentes aos IDs recebidos
            products_from_backend = []
            for item in product_data:
                product_id = item.get('productId')
                quantity = item.get('quantity')

                product = get_object_or_404(Product, product_id=product_id)

                # Adicione o objeto Product e a quantidade à lista
                products_from_backend.append({'product': product, 'quantity': quantity})

            # Faça o que precisar com a lista de produtos do backend
            print(products_from_backend)

            return JsonResponse({'success': True})
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON in the request'}, status=400)

    return JsonResponse({'error': 'Invalid request method'}, status=405)