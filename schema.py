#GraphQL schema using python
import graphene
import data

class Stock(graphene.ObjectType):
    name = graphene.String()
    symbol = graphene.String()
    price = graphene.Float()
    highestPrice = graphene.Float()
    lowestPrice = graphene.Float()

# Define class for query 

class Query(graphene.ObjectType):
    stocks = graphene.List(Stock)
    stock = graphene.Field(Stock, symbol=graphene.String())

    def resolve_stocks(self, info):
        return data.stocks

    def resolve_stock(self, info, symbol):
        stock_data = data.get_stock_data_by_symbol(symbol)

        if not stock_data:
            return None

        historical_prices = stock_data.get('historical_prices', []) # store the data in array to calcluate the highest and lowest

        if not historical_prices:
            return Stock(
                name=stock_data['name'],
                symbol=stock_data['symbol'],
                price=stock_data['price'],
                highestPrice=None,
                lowestPrice=None
            )

        highest_price = max(historical_prices)
        lowest_price = min(historical_prices)

        return Stock(
            name=stock_data['name'],
            symbol=stock_data['symbol'],
            price=stock_data['price'],
            highestPrice=highest_price,
            lowestPrice=lowest_price
        )

schema = graphene.Schema(query=Query)
