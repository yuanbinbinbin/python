#coding:utf-8

import json


class MixChart:
	'''柱形图与折线图混合'''
	def __init__(self, title, subtitle, div_id):

		self._credits = {'credits': {'enabled': False}}
		self._chart = {'chart': {'zoomType': 'xy', 'renderTo': div_id}}
		self._title = {'title': {'text': title}}
		self._subtitle = {'subtitle': {'text': subtitle}}
		self._xAxis = {'xAxis': [{ 
		        'categories': [],
		        'crosshair': True
		    }]}
		self._yAxis = {'yAxis': [{ 
		        'title': {
		            'text': '',
		            'style': {
						'color': 'Highcharts.getOptions().colors[0]'
					}
		        },
		        'labels': {
		            'format': '{value}',
		            'style': {
						'color': 'Highcharts.getOptions().colors[0]'
					}
		        },
		        'plotLines': [{'color': '#FF0000'}]
		    }, { 
		        'title': {
		            'text': '',
		            'style': {
						'color': 'Highcharts.getOptions().colors[1]'
					}
		        },
		        'labels': {
		            'format': '{value}',
		            'style': {
						'color': 'Highcharts.getOptions().colors[1]'
					}
		        },
		        'min': 0,
		        'opposite': True,
		        'plotLines': [{'color': '#FF0000'}]
		    }]}
		self._plotOptions = {'plotOptions': {'series': {
		            							'dataLabels': {'enabled': True}},
		            						 'column': {'dataLabels': {'inside': True}},
		            						 'spline': {'dataLabels': {'enabled': True}}
		            						 }}
		self._series = {'series': []}


	def setyAxistitle(self, d):	
		self._yAxis['yAxis'][d.keys()[0]]['title']['text'] = d.values()[0]


	def setxAxiscategories(self, d):
		self._xAxis['xAxis'][0]['categories'] = d

	def setyAxislabelformat(self, d):
		self._yAxis['yAxis'][d.keys()[0]]['labels']['format'] = d.values()[0]

	def setseries(self, d):
		self._series['series'].append(d)

	def setseriesdataLabels(self, d):
		self._plotOptions['plotOptions']['series']['dataLabels']['enabled'] = d

	def setcolumndataLabelsinside(self, d):
		self._plotOptions['plotOptions']['column']['dataLabels']['inside'] = d

	def setsplinedataLabelsinside(self, d):
		self._plotOptions['plotOptions']['spline']['dataLabels']['enabled'] = d

	def setyAxisplotlines(self, d):
		for k, v in d.items():
			for item in v:
				self._yAxis['yAxis'][k]['plotLines'][0][item] = v[item]

	def dumps(self):

		self.data = {}
		self.data.update(self._credits)
		self.data.update(self._chart)
		self.data.update(self._title)
		self.data.update(self._subtitle)
		self.data.update(self._xAxis)
		self.data.update(self._yAxis)
		self.data.update(self._plotOptions)
		self.data.update(self._series)
		
		return json.dumps(self.data)


class DoubleColumnChart:
	'''双柱形图'''
	def __init__(self, title, subtitle, div_id):

		self._credits = {'credits': {'enabled': False}}
		self._chart = {'chart': {'type': 'column', 'renderTo': div_id}}
		self._title = {'title': {'text': title}}
		self._subtitle = {'subtitle': {'text': subtitle}}
		self._xAxis = {'xAxis': [{ 
		        'categories': [],
		        'crosshair': True
		    }]}
		self._yAxis = {'yAxis': { 
				'min': None,
		        'title': {
		            'text': ''
		        }
		    }}
		self._plotOptions = {'plotOptions': {'column': {'pointPadding': 0.2,
	                									'borderWidth': 0,
	                									'dataLabels': {'enabled': True}}
		            						 }}
		self._series = {'series': []}

	def setyAxistitle(self, d):
		self._yAxis['yAxis']['title']['text'] = d

	def setxAxiscategories(self, d):
		self._xAxis['xAxis'][0]['categories'] = d

	def setseries(self, d):
		self._series['series'].append(d)

	def setyAxsmin(self, d):
		self._yAxis['yAxis']['min'] = d

	def dumps(self):

		self.data = {}
		self.data.update(self._credits)
		self.data.update(self._chart)
		self.data.update(self._title)
		self.data.update(self._subtitle)
		self.data.update(self._xAxis)
		self.data.update(self._yAxis)
		self.data.update(self._plotOptions)
		self.data.update(self._series)
		
		return json.dumps(self.data)


class SplineChart:
	'''折线图'''
	def __init__(self, title, subtitle, div_id):

		self._credits = {'credits': {'enabled': False}}
		self._chart = {'chart': {'type': 'spline', 'renderTo': div_id}}
		self._title = {'title': {'text': title}}
		self._subtitle = {'subtitle': {'text': subtitle}}
		self._xAxis = {'xAxis': [{ 
		        'categories': []
		    }]}
		self._yAxis = {'yAxis': {
				'plotLines': [{
                'value': 0,
                'width': 1,
                'color': '#808080'
            }],
		        'title': {
		            'text': ''
		        },
		        'step': 2,
		        'min': None
		    }}
		self._plotOptions = {'plotOptions': {'series': {
		            							'dataLabels': {'enabled': True}}
		            						 }}
		self._series = {'series': []}
		self._legend = {'lenged':{
            'borderWidth':0,
            'style': {
                'fontSize': 20
            }
        }}

	def setyAxistitle(self, d):
		self._yAxis['yAxis']['title']['text'] = d

	def setxAxiscategories(self, d):
		self._xAxis['xAxis'][0]['categories'] = d

	def setseries(self, d):
		self._series['series'].append(d)

	def setyAxsmin(self, d):
		self._yAxis['yAxis']['min'] = d

	def setseriesdataLabels(self, d):
		self._plotOptions['plotOptions']['series']['dataLabels']['enabled'] = d

	def dumps(self):

		self.data = {}
		self.data.update(self._credits)
		self.data.update(self._chart)
		self.data.update(self._title)
		self.data.update(self._subtitle)
		self.data.update(self._xAxis)
		self.data.update(self._yAxis)
		self.data.update(self._plotOptions)
		self.data.update(self._series)
		self.data.update(self._legend)
		
		return json.dumps(self.data)


class AccidentChart:
	'''用于BG间故障数统计'''
	def __init__(self, title, subtitle, div_id):

		self._credits = {'credits': {'enabled': False}}
		self._chart = {'chart': {'type': 'column', 'renderTo': div_id}}
		self._color = {'colors': ['#E71825','#F7C709', '#C71585','#BEBEBE']}
		self._title = {'title': {'text': title}}
		self._subtitle = {'subtitle': {'text': subtitle}}
		self._xAxis = {'xAxis': [{ 
		        'categories': []
		    }]}
		self._yAxis = {'yAxis': {
            	'stackLabels': { 'enabled': True},
		        'title': {
		            'text': ''
		        },
		        'min': 0
		    }}
		self._plotOptions = {'plotOptions': {'column': {
		            							'stacking': 'normal'}
		            						 }}
		self._series = {'series': []}

	def setyAxistitle(self, d):
		self._yAxis['yAxis']['title']['text'] = d

	def setxAxiscategories(self, d):
		self._xAxis['xAxis'][0]['categories'] = d

	def setseries(self, d):
		self._series['series'].append(d)

	def dumps(self):

		self.data = {}
		self.data.update(self._credits)
		self.data.update(self._chart)
		self.data.update(self._color)
		self.data.update(self._title)
		self.data.update(self._subtitle)
		self.data.update(self._xAxis)
		self.data.update(self._yAxis)
		self.data.update(self._plotOptions)
		self.data.update(self._series)
		
		return json.dumps(self.data)