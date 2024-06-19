# unauthenticated_middleware.py
class UnauthenticatedMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Define paths that do not require authentication
        unauthenticated_paths = ['api/v1/visitor/', '/api/v1/specialization/']

        # Check if the requested path is one of the unauthenticated paths
        if request.path.startswith(tuple(unauthenticated_paths)):
            request._dont_enforce_csrf_checks = True
            return self.get_response(request)

        response = self.get_response(request)
        return response
