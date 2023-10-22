from flask import Flask
from flask_graphql import GraphQLView
import threading
from schema import schema
import data

app = Flask(__name__)
app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))

if __name__ == '__main__':
    price_simulation_thread = threading.Thread(target=data.simulate_price_changes)
    price_simulation_thread.start()
    app.run(debug=True)
