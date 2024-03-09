import datetime

from pelican import signals
from pelican.contents import Article
from pelican.readers import BaseReader

import pandas as pd

import pdb


def addArticle(articleGenerator):
    settings = articleGenerator.settings

    # Author, category, and tags are objects, not strings, so they need to
    # be handled using BaseReader's process_metadata() function.
    baseReader = BaseReader(settings)
   
    # employees
    
    df = pd.read_csv(articleGenerator.context["PATH"] + "/employees.csv")
    for row in df.itertuples():
        content = row.notes        
        newArticle = Article(content, {            
            "template": "employee",
            "title": row.firstname + ' ' + row.lastname,  
            "date": datetime.datetime.now(),
            "category": baseReader.process_metadata("category", "employee"),
            "summary": row.title,
            "id": baseReader.process_metadata("id", row.employeeid), 
            "titleofcourtesy": row.titleofcourtesy,
            "birthdate": row.birthdate,
            "hiredate": row.hiredate,
            "address": row.address,
            "city": row.city,
            "region": row.region,
            "postalcode": row.postalcode,
            "country": row.country,
            "homephone": row.homephone,
            "extension": row.extension,
            "photo": row.photopath,
            "reportsto": row.reportsto

		})
        #articleGenerator.articles.insert(0, newArticle)
        articleGenerator.articles.append( newArticle )
        
    df = pd.read_csv(articleGenerator.context["PATH"] + "/categories.csv")
    for row in df.itertuples():
        content = ""
        newArticle = Article(content, {            
            "template": "prodcat",
            "title": row.categoryname,  
            "date": datetime.datetime.now(),
            "category": baseReader.process_metadata("category", "prodcat"),
            "summary": row.description,
            "id": baseReader.process_metadata("id", row.categoryid), 
            "photo": row.picture    
		})
        articleGenerator.articles.append( newArticle )
        
    products = pd.read_csv(articleGenerator.context["PATH"] + "/products.csv")
    suppliers = pd.read_csv(articleGenerator.context["PATH"] + "/suppliers.csv")
    df = pd.merge(products, suppliers, on = 'supplierid')
    # supplierid,companyname,
    # productid,productname,supplierid,categoryid,quantityperunit,unitprice,
    # unitsinstock,unitsonorder,reorderlevel,discontinued
    for row in df.itertuples():
        content = ""
        newArticle = Article(content, {            
            "template": "product",
            "title": row.productname,  
            "date": datetime.datetime.now(),
            "category": baseReader.process_metadata("category", "product"),
            "summary":  "product ::: $" + str(row.unitprice),  # row.categoryname +
            "id": baseReader.process_metadata("id", row.productid), 
            "supplier": row.companyname,
            "categoryid": row.categoryid,
            "quantityperunit": row.quantityperunit,
            "unitprice": row.unitprice,
            "unitsinstock": row.unitsinstock,
            "unitsonorder": row.unitsonorder,
            "reorderlevel": row.reorderlevel,
            "discontinued": row.discontinued
		})
        articleGenerator.articles.append( newArticle )
            
    """
import pandas as pd
df = pd.read_csv(articleGenerator.context["PATH"] + "/employees.csv")
df.loc[0]    
df.loc[0]["lastname"]    

for i in range(len(df)):
    row = df.loc[i]
    print(row["lastname"]   )
    
df = pd.read_csv("products.csv")
df2 = pd.read_csv("suppliers.csv")
df.columns
df2.columns

pd.merge(df,df2,on='supplierid')
pd.merge(df,df2,on='supplierid')[["productname","companyname"]].loc[1:20]
    
    """
    
def delCategory(articleGenerator):
    for i in range(len(articleGenerator.categories)):
        if articleGenerator.categories[i][0].name == "product":
            del articleGenerator.categories[i]
            break
            
def dummy(articleGenerator):
    pass
    #breakpoint()     
            
def register():
    signals.article_generator_finalized.connect(dummy)
    signals.article_generator_pretaxonomy.connect(addArticle)
    signals.article_generator_finalized.connect(delCategory)
