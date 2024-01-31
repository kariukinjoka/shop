import pandas as pd
from .models import ItemMaster

def load_data():
    df = pd.read_excel('products/Item_master.xlsx')

    for index, row in df.iterrows():
        print(f"--------------{index}----------------")
        try:
            item_master = ItemMaster.objects.create(
                ITEM_CODE=row['ITEM_CODE'],
                ITEM_NAME=row['ITEM_NAME'],
                ITEM_IG_CODE=row['ITEM_IG_CODE'],
                ITEM_UOM_CODE=row['ITEM_UOM_CODE'],
                ITEM_STK_NONSTK=row['ITEM_STK_NONSTK'],
                CLASSIFICATION=row['CLASSIFICATION'],
                PRODUCT_TYPE=row['PRODUCT_TYPE'],
                BRAND=row['BRAND'],
                BRAND_CODE2=row['BRAND_CODE2'],
                CATEGORY=row['CATEGORY'],
                SPECIFICATION=row['SPECIFICATION'],
                SECTION_WIDTH=row['SECTION_WIDTH'],
                PROFILE=row['PROFILE'],
                RIM_SIZE=row['RIM_SIZE'],
                PATTERN=row['PATTERN'],
                PLAY_RATING=row['PLAY_RATING'],
                OTHER=row['OTHER'],
                VAT=row['VAT'],
            )
            
            item_master.save()
        except:
            pass


    print("Data loaded into Django model.")
