from abc import ABC, abstractmethod

# class vehicle(ABC):
    
    
#     @abstractmethod
#     def start(self):
#         pass
#     def stop(self):
#         pass

# class car(vehicle):
#     def __init__(self,name):
#         self.name=name

#     def start(self):
#         print(f"{self.name} is starting..")

#     def stop(self):
#         print(f"{self.name} is going to stop")

# car = car(name="bmw")


# car.start()
# car.stop()


class DataFetcher(ABC):
    @abstractmethod
    def fetch_data(self,api):
        pass

class server_DataFetcher(DataFetcher):
    def fetch_data(self, api):
        print("fetching data from cache")
        return f"networ data for {api}"
class cache_DataFetcher(DataFetcher):
    def __init__(self,Data_Fetcher):
        self.data_fetcher=Data_Fetcher
        self.cache={}
    def fetch_data(self, api):
        print("fetching data from server")

        if api in self.cache:
            print("fetching data from cache")
            return self.cache[api]

        else:
            data=self.data_fetcher.fetch_data(api)
            self.cache[api]=data
            return data
server  = server_DataFetcher()        
cache   =cache_DataFetcher(server)

print(cache.fetch_data("www.facebook.com/posts"))


