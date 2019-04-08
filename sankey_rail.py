import plotly.plotly as py
years = 30

data = dict(                # data dictionary has: type,node dictionary, line dictionary
    type='sankey',          # initialize Sankey diagram
    node = dict(            # node variables:consists of pad,thickness
      pad = 100,            # gap between the flows (bigger values, bigger gap)
      thickness = 100,          # thickess sets the node thickness
      line = dict(              # sets the node position (technically useless)
        color = "green",        #line colour
        width = 0.5             #width of line (set to minimum such as 0.5)
      ),
        domain = dict(
      x =  [0,1],
      y =  [0,1]
    ),
        orientation = "h",
        valueformat = ".0f",
        valuesuffix = "GJ",
      label = ["coal", "natural gas", "coke", "diesel", "oil", "peat","biomass","crude oil","bone meal","fuel"
               ,"steel manufacture","ballast manufacture","concrete manufacture","rail + concrete construction",
               "ballast construction","maintain ballast","steel rail maintain", "steel recycling","concrete recycling"], #nodes  FIGURE ALL THE NODES FIRST BEFORE PROCEEDING
      color = ["blue", "blue", "blue", "blue", "blue", "blue","blue","blue","blue","blue","blue","blue","blue"
               ,"blue","blue","blue","blue","blue","blue"]      #steel is element 10,manufacuturing is element 13          #node colour
    ),
    link = dict(                    # links
      source =  [0,9,0,1,0,6,1,4,5,7,2,8,0,3,3,3,3,3,9],    #calls array elements from label array
      target = [11,11,10,10,17,12,12,12,12,12,12,12,12,12,16,14,15,13,18],      #calls array elements from label array , matches 0 and 2, 1 and 3 etc.
      value = [862.15/years,28863.45/years,6162240/years,192570/years,410873.64/years,68.838/years,779047.768/years
          ,60.08/years,6.88/years,229000/years,164138.4/years,3128.4/years,1153749.2/years
               ,23959.2/years,3988.14/years,4556/years,218000/years,6854.4/years,6904.94/years]         #energy value for each source ad target
  ))

layout =  dict(                         #layout dictionary
    title = "Rail infrastructure energy",
    font = dict(
      size = 10
    )
)

fig = dict(data=[data], layout=layout)
py.plot(fig, validate=False)
