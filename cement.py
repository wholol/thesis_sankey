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
      label = ["propane","natural gas","diesel","gasoline","electricity","fuel","coal","crude oil","biomass"
               ,"limestone extraction/processing","alumina refining","bauxite mining","cement manufacturing","silica sand production",
               "cement production","mixing","admixture","aggregate","concrete production"], #nodes  FIGURE ALL THE NODES FIRST BEFORE PROCEEDING
      color = ["blue","blue","blue","blue","blue","blue","blue","blue","blue","blue","blue","blue","blue","blue","blue"
                "blue","blue","blue","blue"]          #node colour
    ),
    link = dict(                    #links
      source = [0,1,2,3,1,2,3,5,6,2,4,6,4,5,6,2,1,4,6,8,9,10,11,12,13],    #calls array elements from label array
      target = [9,9,9,9,10,10,10,10,10,11,11,11,12,12,12,13,13,13,13,13,14,14,14,14,14],      #calls array elements from label array , matches 0 and 2, 1 and 3 etc.
      value = [2834.25,221.48,2033.14,215.88,649.04,25.96,463.06,2040,649.04,78.53,11.098,17.85,8659.7,8659.7,40508.9,18.098,0.017
               ,28.93,0.08437,0.0867,6249.3,3210.17,107.48,57888.3,47.2]         #energy value for each source ad target
  ))

layout =  dict(                         #layout dictionary
    title = "Rail infrastructure energy",
    font = dict(
      size = 30
    )
)

fig = dict(data=[data], layout=layout)
py.plot(fig, validate=False)

# 11/4/19 #
#further break down concrete into components
#determine the CO2 output of respective concrete components possibly
