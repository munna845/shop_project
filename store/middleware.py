from django.utils.deprecation import MiddlewareMixin
import logging

logger = logging.getLogger(__name__)

class RequestLogMiddleware(MiddlewareMixin):
    def process_request(self, request):
        user = request.user if request.user.is_authenticated else "Anonymous"
        
        print(f" {user} - {request.method} Request to: {request.path}") 
        
        logger.info(f"{user} - {request.method} - {request.path}") 
        
        return None