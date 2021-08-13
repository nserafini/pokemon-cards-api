from functools import wraps

from flask import current_app, request

from flask_restful import Api

from api.exceptions import ApiKeyError, NotFoundError


class BaseAPI(Api):
    def handle_error(self, error):
        """Handle api errors."""

        try:
            raise error
        except NotFoundError as error:
            response = {"error": str(error)}
            status_code = 404
        except Exception as error:
            response = {"error": str(error)}
            status_code = 500
        return response, status_code


def validate_access(method):
    """Validate Api Key."""
    @wraps(method)
    def _impl(*method_args, **method_kwargs):

        headers = request.headers
        api_key_header = headers.get('Api-Key', None)
        if api_key_header is None:
            raise ApiKeyError("No Api Key was provided.")

        if api_key_header != current_app.config.get('API_KEY'):
            raise ApiKeyError("Invalid Api Key.")

        return method(*method_args, **method_kwargs)
    return _impl
