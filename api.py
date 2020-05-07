from threading import Thread

from flask import Flask, jsonify
from flask_restful import Resource, Api


class HealthApi(Thread):
    class HealthCheck(Resource):

        def __init__(self, **kwargs):
            self.environment = kwargs

        def get(self):
            return jsonify({"pc_heat_level": self.environment["pc_heat_level"],
                            "current_temp": self.environment["current_temp"],
                            "error": self.environment["error"]})

    class Shutdown(Resource):
        def get(self):
            pass

    def __init__(self, data):
        self.app = Flask(__name__)
        self.api = Api(self.app)

        self.api.add_resource(HealthApi.HealthCheck, "/health", resource_class_kwargs=data)
        self.api.add_resource(HealthApi.Shutdown, "/quit")
        super().__init__()
    def run(self):
        self.app.run(port=80)