import sys
import pandas as pd
import numpy as np
import requests as r
from bs4 import BeautifulSoup

#url path for open abated lead properties
JSON_OPEN = 'https://healthmke.quickbase.com/db/bpv8vzw6z?a=JBI_GetReportData&initialLoad=true&shouldUseVirtualization=false&qid=15&newTableGrid=true&CompareWithAppLocalTime=1&noCacheJBI=1'

#url path for closed abated lead properties
JSON_PAST = 'https://healthmke.quickbase.com/db/bptrhj6it?a=JBI_GetReportData&initialLoad=true&shouldUseVirtualization=false&qid=84&newTableGrid=true&CompareWithAppLocalTime=1&noCacheJBI=1'

def parse_open_df(df):
    
    address =  [i.pop('value', None) for i in df['57'].values]
    ext_ord_due_date =  [i.pop('value', None) for i in df['13'].values]
    int_ord_due_date =  [i.pop('value', None) for i in df['8'].values]
    int_status =  [i.pop('value', None) for i in df['43'].values]
    ext_status =  [i.pop('value', None) for i in df['44'].values]

    int_status =  [i.pop('value', None) for i in df['45'].values]
    type_of_order =  [i.pop('value', None) for i in df['6'].values]
    order_issue_date =  [i.pop('value', None) for i in df['9'].values]
    ald =  [i.pop('value', None) for i in df['54'].values]
    
    
    # Orders with Open Status - Public (January 2018-YTD)
    open_lead_parsed = pd.DataFrame({
        'Address':address,
        'Exterior Order Due Date':ext_ord_due_date,
        'Interior Orders Due Date':int_ord_due_date,
        'Interior Order Status': int_status,
        'Exterior Order Status': ext_status,
        'Interior Order Status': int_status,
        'Type of Orders': type_of_order,
        'Order Issued Date': order_issue_date,
        'alderman': ald,
    })

    return open_lead_parsed

def parse_closed_dates(abated_json_df):
    
    abated_address =  [i.pop('value', None) for i in abated_json_df['144'].values]
    clear_date =  [i.pop('value', None) for i in abated_json_df['64'].values]
    abated_ald =  [i.pop('value', None) for i in abated_json_df['80'].values]
    
    # Orders with Open Status - Public (January 2018-YTD)
    abated_parse_df = pd.DataFrame({
        'Address':abated_address,
        'Final Clearance Date':clear_date,
        'Alderman': abated_ald,
    })
    
    return abated_parse_df    


def main():
    
    print("argv :", sys.argv)

    # get and parse open lead properties
    open_lead = r.get(JSON_OPEN)
    open_lead_json = pd.DataFrame(open_lead.json()['records'])
    open_lead_df = parse_open_df(open_lead_json)

    # get and parse historical lead properties
    abated = r.get(JSON_PAST)
    abated_json_df = pd.DataFrame(abated.json()['records'])
    abated_lead_df = parse_closed_dates(abated_json_df)

    #save data
    abated_lead_df.to_csv('abated_lead.csv', index=False)
    open_lead_df.to_csv('open_lead.csv', index=False)

    df = pd.DataFrame(np.random.randint(0, 100,\
         size=(10, 4)), columns=list('ABCD'))

    df.to_csv("df_output.csv")


if __name__ == "__main__":

    main()