"After using data.py to generate dataframes, use this to display them in a web broswer"


from flask import render_template
from flask import Flask
import pandas as pd
app = Flask(__name__)

@app.route("/web")
def show_tables():
    eth = pd.read_excel('ethexcel.xlsx', header=0, delim_whitespace=True)
    gaming = pd.read_excel('gamingexcel.xlsx', header=0, delim_whitespace=True)
    gurus = pd.read_excel('gurusexcel.xlsx', header=0, delim_whitespace=True)
    econ = pd.read_excel('econexcel.xlsx', header=0, delim_whitespace=True)
    ai = pd.read_excel('aiexcel.xlsx', header=0, delim_whitespace=True)
    btc = pd.read_excel('btcxcel.xlsx', header=0, delim_whitespace=True)
    space = pd.read_excel('spaceexcel.xlsx', header=0, delim_whitespace=True)
    systems = pd.read_excel('systemsexcel.xlsx', header=0, delim_whitespace=True)

    eth.set_index(['url'], inplace=True,)
    eth.index.name=None
    gaming.set_index(['url'], inplace=True,)
    gaming.index.name=None
    gurus.set_index(['url'], inplace=True,)
    gurus.index.name=None
    econ.set_index(['url'], inplace=True,)
    econ.index.name=None
    ai.set_index(['url'], inplace=True,)
    ai.index.name=None
    btc.set_index(['url'], inplace=True,)
    btc.index.name=None
    space.set_index(['url'], inplace=True,)
    space.index.name=None
    systems.set_index(['url'], inplace=True,)
    systems.index.name=None
    
    eth_table = eth
    gaming_table = gaming
    gurus_table = gurus
    econ_table = econ
    ai_table = ai
    btc_table = btc
    space_table = space
    systems_table = systems
    
    
    return render_template('view.html',tables=[eth_table.to_html(classes='text'),
                                               gaming_table.to_html(classes='text'),
                                               gurus_table.to_html(classes='text'), 
                                               econ_table.to_html(classes='text'), 
                                               ai_table.to_html(classes='text'),
                                               btc_table.to_html(classes='text'),
                                               space_table.to_html(classes='text'),
                                               systems_table.to_html(classes='text')],
                                               titles = ['na', 'text'])
    
  

if __name__ == "__main__":
    app.run(debug=True)
