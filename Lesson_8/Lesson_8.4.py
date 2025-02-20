from tools import fetch_youbike_data
import pandas as pd
youbike_data:list[dict] = fetch_youbike_data()
def map_func(value:dict)->str:
   return value['sarea'] 

duplicate_map = map(map_func,youbike_data)
unique_map = set(duplicate_map)
area_list = list(unique_map)
area_list
from tools import fetch_youbike_data
import pandas as pd
youbike_data:list[dict] = fetch_youbike_data()

area_list = list(set(map(lambda value:value['sarea'],youbike_data)))
area_list