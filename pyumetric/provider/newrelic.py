"""
NewRelic as Metric Provider
"""

import requests
from .exceptions import NewRelicApiException
from .exceptions import NewRelicInvalidApiKeyException
from .exceptions import NewRelicInvalidParameterException


class NewRelic():

    api_key = None
    __api_url = "https://api.newrelic.com"
    __api_version = "v2"
    __apps_list_endpoint = "{url}/{version}/applications.json"
    __app_info_endpoint = "{url}/{version}/applications/{app_id}.json"
    __metrics_list_endpoint = "{url}/{version}/applications/{app_id}/metrics.json"
    __metric_info_endpoint = "{url}/{version}/applications/{app_id}/metrics/data.json"

    def __init__(self, api_key):
        self.api_key = api_key

    def get_apps(self):
        try:
            request = requests.get(
                self.__apps_list_endpoint.format(url=self.__api_url, version=self.__api_version),
                headers=self.get_headers(),
                data=''
            )
            if request.status_code == 200:
                return request
            else:
                raise NewRelicApiException("Error, Invalid status code %d" % (request.status_code))
        except Exception as e:
            raise NewRelicApiException(e)

    def get_app(self, app_id):

        if app_id is None or app_id == "":
            raise NewRelicInvalidParameterException("NewRelic application id is required!")

        try:
            request = requests.get(
                self.__app_info_endpoint.format(url=self.__api_url, version=self.__api_version, app_id=app_id),
                headers=self.get_headers(),
                data=''
            )
            if request.status_code == 200:
                return request
            else:
                raise NewRelicApiException("Error, Invalid status code %d" % (request.status_code))
        except Exception as e:
            raise NewRelicApiException(e)

    def get_metrics(self, app_id, metric_name=None):

        if app_id is None or app_id == "":
            raise NewRelicInvalidParameterException("NewRelic application id is required!")

        data = ''
        if metric_name is not None and metric_name.strip() != "":
            data = "name=%s" % (metric_name)

        try:
            request = requests.get(
                self.__metrics_list_endpoint.format(url=self.__api_url, version=self.__api_version, app_id=app_id),
                headers=self.get_headers(),
                data=data
            )
            if request.status_code == 200:
                return request
            else:
                raise NewRelicApiException("Error, Invalid status code %d" % (request.status_code))
        except Exception as e:
            raise NewRelicApiException(e)

    def get_metric(self, app_id, metric_name):

        if app_id is None or app_id == "":
            raise NewRelicInvalidParameterException("NewRelic application id is required!")

        if metric_name is None or metric_name == "":
            raise NewRelicInvalidParameterException("NewRelic metric name is required!")

        raise NotImplementedError("NewRelic get_metric method not implemented yet!")

    def get_headers(self):
        if self.api_key.strip() == "":
            raise NewRelicInvalidApiKeyException("NewRelic API Key is required!")
        return {
            'X-Api-Key': self.api_key
        }