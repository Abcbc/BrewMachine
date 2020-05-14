from threading import Thread

from flask import Flask, jsonify
from flask_restful import Resource, Api

import config


class HealthApi(Thread):

    class HealthCheck(Resource):

        def __init__(self, **kwargs):
            self.api = kwargs["API"]
            self.environment = {}

        def get(self):
            self.api.update_message()
            return jsonify({"pc_heat_level": self.api.environment.get("pc_heat_level"),
                            "current_temp": self.api.environment.get("current_temp"),
                            "error": self.api.environment.get("error")})

    class Shutdown(Resource):
        def get(self):
            pass

    def __init__(self, message_queue):
        self.message_queue = message_queue
        self.environment = {}
        self.app = Flask(__name__)
        self.api = Api(self.app)

        self.api.add_resource(HealthApi.HealthCheck, "/health", resource_class_kwargs={"API": self})
        self.api.add_resource(HealthApi.Shutdown, "/quit")
        super().__init__()

    def run(self):
        self.app.run(port=config.port, host="0.0.0.0")


    def update_message(self):
        while not self.message_queue.empty():
            self.environment = self.message_queue.get()