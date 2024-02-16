from abc import ABC,abstractmethod

class DataFetcher(ABC):
    @abstractmethod
    def fetch_data(self,api):
        pass

class server_DataFetcher(DataFetcher):
    def fetch_data(self, api):
        print("fetching data ........")
        return (f"network is {api}")


class cache_DataFetcher(DataFetcher):
    def __init__(self,DataFetcher):
        self.data_fetcher=DataFetcher
        self.cache={}
    def fetch_data(self, api):
        print("Fetching data .....")

        if api in self.cache:
            print("fetching data .....")
            return self.cache[api]
        else:
            data=self.data_fetcher.fetch_data(api)
            self.cache[api]=data
            return data
        
server=server_DataFetcher()
cache=cache_DataFetcher(server)

print(cache.fetch_data("https://guuithub.com/MiniEnemy/Python-4thsem"))
