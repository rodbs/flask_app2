import os
from flask import Flask, render_template, request
import yelp_script
app = Flask(__name__)


@app.route("/")
def index():	
    address = request.values.get('address')
    top3_recommendations = None
    if address:
        top3_recommendations = yelp_script.yelp_search(address)
        #recommendations = recommendations.businesses[0].name
    return render_template('index.html', address = address, top3_recommendations = top3_recommendations)


#Insert the line below to to run on Cloud9  
#if __name__ == "__main__":
#    host = os.environ.get('IP', '0.0.0.0')
#    port = int(os.environ.get('PORT', 8080))
#    app.run(host=host, port=port)
#    app.debug(True)
  

#Insert the line below to to run on Heroku  
if __name__ == "__main__":
    host = os.environ.get('IP', '0.0.0.0')
    port = int(os.environ.get('PORT', 5000))
    app.run(host=host, port=port)
    app.debug(True)