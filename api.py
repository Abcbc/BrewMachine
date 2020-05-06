from flask import Flask, jsonify
from flask_restful import Resource, Api
class HealthApi:
    class HealthCheck(Resource):

        def __init__(self, **kwargs):
            self.environment = kwargs

        def get(self):
            return jsonify({"pc_heat_level": self.environment["pc_heat_level"],
                            "current_temp": self.environment["current_temp"],
                            "error": self.environment["error"]})


    def __init__(self, data):
        self.api.add_resource(HealthApi.HealthCheck, "/health", resource_class_kwargs=data)


    def run(self):
        self.app.run(port=6666)