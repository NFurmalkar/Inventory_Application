from django.http import HttpResponseRedirect

class VerifyMiddleware(object):
    def __init__(self,get_response):
        self.get_response = get_response

    def __call__(self,request,id=None, *args, **kwargs):
        print("The pre-processing request")
        if not request.session.get('email'):
            return HttpResponseRedirect('/')
        if id:
            response = self.get_response(request,id)
            print("the post-processing request")
            return response
        else:
            response = self.get_response(request)
            print("the post-processing request")
            return response
