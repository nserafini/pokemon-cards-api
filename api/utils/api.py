from flask_restful import Api

from api.exceptions import NotFoundError


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
