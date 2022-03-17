import yaml


class Service:
    """
    attrs:
    - host
    - environment
    - service
    - ip
    methods:
    - get_dict() -> dict
    - generate_yaml_file(filename)
    """
    def __init__(
        self,
        host: str,
        environment: str,
        service: str,
        ip: str = None,
        concurrency:int = 1
    ):
        self.host = host
        self.environment = environment
        self.service = service
        self.ip = ip
        self.concurrency = concurrency

    def get_dict(self) -> dict:
        return {
            "host": self.host,
            "environment": self.environment,
            "service": self.service,
            "ip": self.ip,
            "concurrency": self.concurrency
        }

    def generate_yaml_file(self, filename) -> dict:
        with open(filename, "w") as file:
            yaml.dump(self.get_dict(), file)

    def __repr__(self):
        return f"Sevice -> host : {self.host}, service: {self.service}, env: {self.environment}"


if __name__ == "__main__":
    service = Service("toto.com", "prod",  "web")
    print(service)