from pprint import pprint
import tools

def main():
    data:list[dict] = tools.get_aqi(excel_name='aqi.xlsx')
    for item in data:
        print(item['sitenames'])

if __name__ == '__main__':
    main()

def main)(:)
data:list[dict] = Tools