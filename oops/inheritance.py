class Vehicle:
    """A base class for vehicles demonstrating encapsulation.

    Args:
        brand (str): The brand of the vehicle (e.g., Toyota, Honda)
        year (int): The manufacturing year of the vehicle

    Raises:
        ValueError: If brand is empty or not a string, or if year is not a positive integer
    """

    def __init__(self, brand: str, year: int):
        if not brand or not isinstance(brand, str):
            raise ValueError("Brand must be a non-empty string")
        if not isinstance(year, int) or year <= 0:
            raise ValueError("Year must be a positive integer")

        self.__brand = brand  # Private attribute
        self.__year = year  # Private attribute
        self.__is_running = False  # Private attribute to track engine state

    def start_engine(self) -> str:
        """Start the vehicle's engine.

        Returns:
            str: Status message
        """
        if self.__is_running:
            return f"{self.__brand} engine is already running"
        self.__is_running = True
        return f"{self.__brand} engine started"

    def stop_engine(self) -> str:
        """Stop the vehicle's engine.

        Returns:
            str: Status message
        """
        if not self.__is_running:
            return f"{self.__brand} engine is already stopped"
        self.__is_running = False
        return f"{self.__brand} engine stopped"

    def get_details(self) -> str:
        """Get the vehicle's details.

        Returns:
            str: Vehicle information
        """
        status = "running" if self.__is_running else "stopped"
        return f"Vehicle Type: {self.__class__.__name__}\nBrand: {self.__brand}\nYear: {self.__year}\nStatus: {status}"

    def get_brand(self) -> str:
        """Get the brand of the vehicle.

        Returns:
            str: Vehicle brand
        """
        return self.__brand

    def get_year(self) -> int:
        """Get the manufacturing year of the vehicle.

        Returns:
            int: Vehicle year
        """
        return self.__year


class Car(Vehicle):
    """A derived class for cars with fuel type functionality.

    Args:
        brand (str): The brand of the car
        year (int): The manufacturing year of the car
        fuel_type (str): The type of fuel (e.g., Petrol, Diesel, Electric)

    Raises:
        ValueError: If fuel_type is empty or not a string
    """

    def __init__(self, brand: str, year: int, fuel_type: str):
        super().__init__(brand, year)  # Call parent class constructor
        if not fuel_type or not isinstance(fuel_type, str):
            raise ValueError("Fuel type must be a non-empty string")
        self.__fuel_type = fuel_type  # Private attribute

    def get_details(self) -> str:
        """Override parent get_details to include fuel type.

        Returns:
            str: Car information including fuel type
        """
        parent_details = super().get_details()  # Call parent class get_details
        return f"{parent_details}\nFuel Type: {self.__fuel_type}"

    def honk(self) -> str:
        """Make the car honk

        Returns:
            str: Honk message
        """
        return f"{self.get_brand()} car goes *BEEP BEEP*"


class Motorcycle(Vehicle):
    """A derived class for motorcycles with sidecar option.

    Args:
        brand (str): The brand of the motorcycle
        year (int): The manufacturing year of the motorcycle
        has_sidecar (bool): Whether the motorcycle has a sidecar

    Raises:
        ValueError: If has_sidecar is not a boolean
    """

    def __init__(self, brand: str, year: int, has_sidecar: bool):
        super().__init__(brand, year)  # Call parent class constructor
        if not isinstance(has_sidecar, bool):
            raise ValueError("has_sidecar must be a boolean")
        self.__has_sidecar = has_sidecar  # Private attribute
        

    def start_engine(self) -> str:
        """Override parent start_engine to include motorcycle-specific sound.

        Returns:
            str: Status message with motorcycle sound
        """
        if self._Vehicle__is_running:
            return f"{self.get_brand()} motorcycle engine is already running"
        self._Vehicle__is_running = True
        return f"{self.get_brand()} motorcycle engine started with *VROOM*"
    

    def get_details(self) -> str:
        """Override parent get_details to include sidecar information.

        Returns:
            str: Motorcycle information including sidecar status
        """
        parent_details = super().get_details()  # Call parent class get_details
        sidecar_status = "Yes" if self.__has_sidecar else "No"
        return f"{parent_details}\nHas Sidecar: {sidecar_status}"


if __name__ == "__main__":
    """Driver function to demonstrate inheritance with vehicles"""
    try:
        # Create a car
        car = Car("Toyota", 2020, "Petrol")
        print("Car Operations:")
        print(car.start_engine())
        print(car.honk())
        print(car.get_details())
        print(car.stop_engine())
        print("\n" + "-" * 40 + "\n")

        # Create a motorcycle
        motorcycle = Motorcycle("Harley-Davidson", 2023, True)
        print("Motorcycle Operations:")
        print(motorcycle.start_engine())
        print(motorcycle.get_details())
        print(motorcycle.stop_engine())

    except ValueError as e:
        print(f"Error: {e}")