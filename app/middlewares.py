from django.http import HttpResponse

# # function based middleware
# def my_middleware(get_response):
#     print("One time config and initialization --my_middleware")
#     def inner(request):
#         print("Before calling view")
#         resp = get_response(request)
#         print("After calling view")
#         return resp
#     return inner

# # class based middleware
# class MyMiddleware():
#     def __init__(self, get_response):
#         self.get_response = get_response
#         print("One time config and initialization--MyMiddleware")    
        
#     def __call__(self, request): 
#         print("Before calling view")
#         resp = self.get_response(request)
#         print("After calling view")
#         return resp
    
# # chaining or nested middlewares

# class MumbaiMiddleware():
#     def __init__(self, get_response):
#         self.get_response = get_response
#         print("In MumbaiMiddleware init method")
        
#     def __call__(self, request):
#         print("Before calling view--MumbaiMiddleware")
#         resp = self.get_response(request)
#         print("After calling view--MumbaiMiddleware")
#         return resp 
    
# class PuneMiddleware():
#     def __init__(self, get_response):
#         self.get_response = get_response
#         print("In PuneMiddleware init method")
        
#     def __call__(self, request):
#         print("Before calling view--PuneMiddleware")
#         resp = self.get_response(request)
#         print("After calling view--PuneMiddleware")
#         return resp 
    
# class DubaiMiddleware():
#     def __init__(self, get_response):
#         self.get_response = get_response
#         print("In DubaiMiddleware init method")
        
#     def __call__(self, request):
#         print("Before calling view--DubaiMiddleware")
#         resp = self.get_response(request)
#         print("After calling view--DubaiMiddleware")
#         return resp 
    

# class HookMiddleware():
#     def __init__(self, get_response):
#         self.get_response = get_response
#         print("In HookMiddleware init method")
        
#     def __call__(self, request):
#         print("Before calling view--HookMiddleware")
#         resp = self.get_response(request)
#         print("After calling view--HookMiddleware")
#         return resp    
    
#     def process_view(self, request, view_func, view_args, view_kwargs):
#         print(view_func.__name__)
#         print("In process view")
#         return None
    
#     def process_exception(self, request, exception):
#         print("In process_exception")
#         msg = f"{exception.__class__.__name__}------>{exception}"
#         return HttpResponse(msg)
    
#     def process_template_response(self, request, response):
#         print("In process_template_response")
#         print(response.context_data)
#         response.context_data['name'] = "Namrata"
#         response.context_data['age'] = 23
#         return response