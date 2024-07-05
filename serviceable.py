class Serviceable:
    def needs_service(self) -> bool:
        raise NotImplementedError("Subclasses must implement this method")
