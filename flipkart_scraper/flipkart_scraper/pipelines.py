import pymongo


class FlipkartScraperPipeline:
    def __init__(self):
        self.conn = pymongo.MongoClient("mongodb+srv://akash:8jNYW8eVQCHORH6M@cluster0.k8zrx.mongodb.net/product?retryWrites=true&w=majority")

        # creating database
        db = self.conn['flipkartDB']
        # creating collection
        self.collection = db['products']

    def process_item(self, item, spider):

        """
            method stores the data in db
            params:
                self (class instance)
                item (list): data scraped
            return:
                item (list)
        """

        for i in range(0, len(item['product_price'])):
            try:
                name = item['product_name'][i] if item['product_name'][i] != None else ''
                features = item['product_features'][i] if item['product_features'] != None else ''
                price = item['product_price'][i] if item['product_price'] != None else ''
                self.collection.insert({
                'product_name': name,
                # 'product_image': item['product_image'][i],
                'product_features': features,
                'product_price': price,
                # 'product_rating': item['product_rating'][i],
                'product_type': item['product_type']
                })
            except IndexError:
                pass
        return item
