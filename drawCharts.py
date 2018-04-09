import charts

data = [1,2,5,9,6,3,4,8]
options = dict(height=400, title=dict(text='My first chart!'))
charts.plot(data, options=options, name='List data', save='temp.svg', show='inline')