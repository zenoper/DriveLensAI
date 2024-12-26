class DataStorage:
    def __init__(self) -> None:
        "Initialize the class"
        self.data = {}

    
    def add(self, key: str, value: str) -> None:
        """
        Adds or updates a value associated with the given key
        """
        self.data[key] = value

    
    def get(self, key: str) -> str:
        """
        Returns the value for the provided key
        """
        return self.data.get(key, "Key not found")
    
    
    def delete(self, key: str) -> None:
        """
        Deletes the value associated with the given key
        """
        if key in self.data:
            del self.data[key]
    
    def list(self) -> dict:
        """
        Returns the entire dictionary of data
        """
        return self.data



if __name__ == "__main__":
    storage = DataStorage()
    
    storage.add("type", "sportscar")
    storage.add("brand", "BMW")
    
    print(storage.get("type"))
    print(storage.get("brand"))
    
    print(storage.list())
    
    storage.delete("type")
    print(storage.list())
