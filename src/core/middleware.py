from django.shortcuts import redirect
from django.urls import resolve


class AuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        allowed_urls = [
            "/",
            "/login/",
            "/cadastro/",
            "/convidado/",
        ]

        blocked_urls = ['/admin/']
        blocked_routes = ["administration_view"]

        if not request.user.is_authenticated and request.path not in allowed_urls:
            return redirect("src.core:index")

        if request.user.is_authenticated and request.path in blocked_urls:
            if not request.user.is_staff:
                return redirect('establishment:dashboard')
        if request.user.is_authenticated:
            current_route_name = resolve(request.path_info).url_name
            print(current_route_name)
            if current_route_name in blocked_routes and not request.user.is_staff:
                return redirect("establishment:dashboard")

        response = self.get_response(request)
        return response
