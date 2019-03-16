import plotly.plotly as py


data = dict(                # data dictionary has: type,node dictionary, line dictionary
    type='sankey',          # initialize Sankey
    node = dict(            # node variables:consists of pad,thickness
      pad = 100,            # gap between the flows (bigger values, bigger gap)
      thickness = 20,          # thickess sets the node thickness
      line = dict(              # sets the node position (technically useless)
        color = "green",        #line colour
        width = 0.5             #width of line (set to minimum such as 0.5)
      ),
      label = ["A1", "A2", "B1", "B2", "C1", "C2"],                 #nodes
      color = ["blue", "blue", "blue", "blue", "blue", "blue"]      #node colour
    ),
    link = dict(        # links
      source = [0,1,0,2,3,3],       #calls array elements from label array
      target = [2,3,3,4,4,5],       #calls array elements from label array
      value = [8,4,2,8,4,2]         #energy value for each source ad target
  ))

layout =  dict(                         #layout dictionary
    title = "Basic Sankey Diagram",
    font = dict(
      size = 10
    )
)

fig = dict(data=[data], layout=layout)             
py.plot(fig, validate=False)
