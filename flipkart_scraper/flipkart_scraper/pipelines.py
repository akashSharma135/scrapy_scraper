import pymongo


class FlipkartScraperPipeline:
    def __init__(self):
        self.conn = pymongo.MongoClient("mongodb+srv://akash:8jNYW8eVQCHORH6M@cluster0.k8zrx.mongodb.net/product?retryWrites=true&w=majority")

        # creating database
        db = self.conn['mydb']
        # creating collection
        self.collection = db['electronics']

    def process_item(self, item, spider):
        for i in range(0, len(item['product_name'])):
            
            self.collection.insert({
            'product_name': item['product_name'][i],
            'product_image': item['product_image'][i],
            'product_features': item['product_features'][i],
            'product_price': item['product_price'][i],
            'product_rating': item['product_rating'][i],
            'product_type': item['product_type']
            })
            
        return item
