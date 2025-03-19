# from functool import wraps
# from .models import Trainee
# def IsTrainee(*decorator_args , **decorator_kwargs):
#     def decorator(view_function):
#         @wraps(view_function)
#         def _wrapped_view(request, *view_args, **view_kwargs):
#             if(Trainee.objects.get(pk=view_args[0]) is not None)
#                 return True
#             else:
#                 return False
#
#             return view_function(request, *args, **kwargs)
#
#         return _wrapped_view
#
#     return decorator