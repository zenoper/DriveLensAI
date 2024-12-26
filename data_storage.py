import logging
from datetime import datetime

class DataStorage:
    def __init__(self) -> None:
        "Initialize the class and setup logging"
        self.data = {}
        
        # Configure logging
        logging.basicConfig(
            filename='app.log',
            level=logging.INFO,
            format='[%(asctime)s] %(levelname)s: %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        self.logger = logging.getLogger(__name__)
        self.logger.info("DataStorage instance initialized")

    def add(self, key: str, value: str) -> None:
        """
        Adds or updates a value associated with the given key
        """
        action = "updated" if key in self.data else "added"
        self.data[key] = value
        self.logger.info(f"Key '{key}' {action} with value '{value}'")

    def get(self, key: str) -> str:
        """
        Returns the value for the provided key
        """
        result = self.data.get(key, "Key not found")
        if result == "Key not found":
            self.logger.warning(f"Attempted to access non-existent key: '{key}'")
        else:
            self.logger.info(f"Retrieved value for key: '{key}'")
        return result

    def delete(self, key: str) -> None:
        """
        Deletes the value associated with the given key
        """
        if key in self.data:
            del self.data[key]
            self.logger.info(f"Deleted key: '{key}'")
        else:
            self.logger.warning(f"Attempted to delete non-existent key: '{key}'")

    def list(self) -> dict:
        """
        Returns the entire dictionary of data
        """
        self.logger.info(f"Listed all data. Current size: {len(self.data)} items")
        return self.data

if __name__ == "__main__":
    storage = DataStorage()
    
    storage.add("type", "sportscar")
    storage.add("brand", "BMW")
    
    print(storage.get("type"))
    print(storage.get("brand"))
    print(storage.get("nonexistent"))
    
    print(storage.list())
    
    storage.delete("type")
    storage.delete("nonexistent")
    print(storage.list())