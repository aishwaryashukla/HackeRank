import pandas as pd
import pprint as pp
import pprint
import casparser
import json

data_dictionary ={'folio':[],
                  'amc':[],
                  'amfi':[],
                  'scheme':[],
                  'type':[],
                  'isin':[],
                  'transaction_date': [],
                  'description': [],
                  'amount': [],
                  'units':[],
                  'nav': [],
                  'balance': [],
                  'transation_type': []

}
df = pd.DataFrame(data_dictionary)
data = casparser.read_cas_pdf("/Users/aishwaryashukla/Downloads/8291588090320240820318201335355925.pdf", "Fastrack@12")
print((data))
for i in data.folios:
    for sc in i.schemes:
        for x in sc.transactions:
            # print(f' {i.folio}, {i.amc}, {sc.amfi}, {sc.scheme} , {sc.type}'
            #       f', {sc.isin}, {x} ')
            new_row = {
                'folio': i.folio,
                'amc': i.amc,
                'amfi': sc.amfi,
                'scheme': sc.scheme,
                'type': sc.type,
                'isin': sc.isin,
                'transaction_date': x.date,
                'description': x.description,
                'amount': x.amount,
                'units': x.units,
                'nav': x.nav,
                'balance': x.balance,
                'transation_type': x.type
            }
            df = df._append(new_row,ignore_index=True)

df.fillna(0)
df.to_csv("mf.csv")
