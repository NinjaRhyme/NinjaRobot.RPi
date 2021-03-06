# coding=utf-8

import time
try: # Debug
    import RPi.GPIO as GPIO
except:
    pass

from NinjaObject import *

# ----------------------------------------------------------------------------------------------------
class NinjaHeart(NinjaObject):
    def __init__(self, robot):
        super(NinjaHeart, self).__init__()
        self.robot = robot

        self.components = []
        self.services = []
        self.init()

    # ----------------------------------------------------------------------------------------------------
    def run(self):
		# start services
        for server in self.services:
            server.start()
        super(NinjaHeart, self).run()

    def process(self):
		# process components
        for component in self.components:
            component.process()
        time.sleep(0.05)
        pass

    def exit(self):
        try:
            for component in self.components:
                self.robot.controller.remove_observer(component)
                component.exit()
            self.components = []
            GPIO.cleanup()
        except:
            pass

    # ----------------------------------------------------------------------------------------------------
    def init(self):
        # GPIO
        try:
            GPIO.setwarnings(True)
            GPIO.setmode(GPIO.BCM)
        except:
            pass

        # components
        if "components" in self.robot.memory.config:
            components = self.robot.memory.config["components"]
            for name in components:
                module = __import__("NinjaComponent." + name, globals(), locals(), [name])
                ComponentClass = getattr(module, name)
                self.components.append(ComponentClass(name))
            for component in self.components:
                self.robot.controller.add_observer(component)
                component.on_configure(components[component.name])
                if "source_for_controller" in components[component.name] and components[component.name]["source_for_controller"]:
                    self.robot.controller.add_source(component)
            pass

        # services
        if "services" in self.robot.memory.config:
            services = self.robot.memory.config["services"]
            for name in services:
                module = __import__("NinjaService." + name + ".Server", globals(), locals(), ["Server"])
                ServerClass = getattr(module, "Server")
                self.services.append(ServerClass(name))
            for server in self.services:
                self.robot.controller.add_observer(server)
                server.on_configure(services[server.name])
                if "source_for_controller" in services[server.name] and services[server.name]["source_for_controller"]:
                    self.robot.controller.add_source(server)
            pass
