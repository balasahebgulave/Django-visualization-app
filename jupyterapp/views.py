from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse
from random import sample
import pandas as pd
from jupyterlabproject.settings import BASE_DIR
import os 
from sklearn.preprocessing import LabelEncoder
x_encoder = LabelEncoder()
y_encoder = LabelEncoder()
encoder = LabelEncoder()
file_directory = BASE_DIR+'/jupyterapp/media/'
total_files = os.listdir(file_directory)


def jupyter_data(request):
	return render(request , 'jupyterapp/jupyter.html')

def homepage(request):
	return render(request, 'jupyterapp/home.html')


# def configure(request):
# 	if request.method == 'POST':

# 		filename = request.POST.get('file')
# 		filters = request.POST.get('filter')
# 		limit = request.POST.get('limit')
# 		plot = request.POST.get('plot_type')
# 		columns = []
# 		final_result = {}
# 		if filename is not None:
# 			file = file_directory+filename
# 			filedata = pd.read_csv(file, encoding = 'latin1')
# 			columns = list(filedata.columns)
# 			request.session['filename'] = filename
# 			request.session['columns'] = columns

# 		if plot is not None:
# 			try:
# 				x = 0
# 				y = 0
# 				filedata = pd.read_csv(file_directory + request.session['filename'], encoding='latin1')
# 				selected_columns = []
# 				for i in request.session['columns']:
# 					i = request.POST.get(i)
# 					if i != None:
# 						selected_columns.append(i)
# 				request.session['selected_columns'] = selected_columns
# 				request.session['plot'] = plot
# 				x = x_encoder.fit_transform(filedata[selected_columns[-2]])
# 				y = y_encoder.fit_transform(filedata[selected_columns[-1]])
# 				x_value = x_encoder.inverse_transform(x)
# 				y_value = y_encoder.inverse_transform(y)
# 				request.session['x']={'x_encoded':[str(i) for i in x], 'x_real':[str(i) for i in x_value]}
# 				request.session['y']={'y_encoded':[str(j) for j in y] , 'y_real':[str(j) for j in y_value]}
# 				x = [int(i) for i in request.session['x']['x_encoded']]
# 				y = [int(i) for i in request.session['y']['y_encoded']]
# 				request.session['minimum'] =  min(y)
# 				request.session['maximum'] = max(y)
# 				x_value = [(i,j,k,l) for i,j,k,l in zip(x, request.session['x']['x_real'], y ,request.session['y']['y_real'])]
# 				final_result = {'results': y , 'labels': x , 'plot':request.session['plot'], 'minimum':request.session['minimum'], 'maximum':request.session['maximum'], 'x_value':x_value, 'x_label':request.session['selected_columns'][-2],'y_label':request.session['selected_columns'][-1]}

# 			except Exception as e:
# 				print('---------------------error_message-----------------',e)
				
# 		if filters is not None:
# 			x_encoded = []
# 			y_encoded = []
# 			x_real = []
# 			y_real = []
# 			for i , j , k in zip(range(len(request.session['x']['x_encoded'])), [int(i) for i in request.session['x']['x_encoded']],[int(i) for i in request.session['y']['y_encoded']]):
# 				if k == int(filters):
# 					x_encoded.append(int(request.session['x']['x_encoded'][i]))
# 					y_encoded.append(int(request.session['y']['y_encoded'][i]))
# 					x_real.append(request.session['x']['x_real'][i]) 
# 					y_real.append(request.session['y']['y_real'][i])
# 			x_value = ''
# 			x_value = [(i,j,k,l) for i,j,k,l in zip(x_encoded, x_real, y_encoded ,y_real)]
# 			final_result = {'results': y_encoded , 'labels': x_encoded , 'plot':request.session['plot'], 'minimum':request.session['minimum'], 'maximum':request.session['maximum'], 'x_value':x_value, 'x_label':request.session['selected_columns'][-2],'y_label':request.session['selected_columns'][-1]}

# 		if limit is not None:
# 			x_encoded = []
# 			y_encoded = []
# 			x_real = []
# 			y_real = []
# 			for i , j , k in zip(range(len(request.session['x']['x_encoded'])), [int(i) for i in request.session['x']['x_encoded']],[int(i) for i in request.session['y']['y_encoded']]):
# 				if k <= int(limit):
# 					x_encoded.append(int(request.session['x']['x_encoded'][i]))
# 					y_encoded.append(int(request.session['y']['y_encoded'][i]))
# 					x_real.append(request.session['x']['x_real'][i]) 
# 					y_real.append(request.session['y']['y_real'][i])
# 			x_value = ''
# 			x_value = [(i,j,k,l) for i,j,k,l in zip(x_encoded, x_real, y_encoded , y_real)]
# 			final_result = {'results': y_encoded , 'labels': x_encoded , 'plot':request.session['plot'], 'minimum':request.session['minimum'], 'maximum':request.session['maximum'], 'x_value':x_value, 'x_label':request.session['selected_columns'][-2],'y_label':request.session['selected_columns'][-1]}

# 			if request.session['plot'] == None:
# 				request.session['plot'] = 'scatter'

# 		# print('-------final-------',final_result)
# 		return render(request, 'jupyterapp/configure.html', {'columns' : columns, 'total_files' : total_files, 'final_result' : final_result})
# 	return render(request, 'jupyterapp/configure.html', {'total_files':total_files} )







def configure(request):
	if request.method == 'POST':
		filters = request.POST.get('filter')
		limit = request.POST.get('limit')
		plot = request.POST.get('plot_type')
		final_result = {}
		if plot is not None:
			try:
				filedata = pd.read_csv(file_directory + request.session['filename'], encoding='latin1')
				if 'initial' in request.session.keys():
					filedata = filedata.loc[request.session['initial']:request.session['final']]
				selected_columns = request.session['selected_columns']
				request.session['plot'] = plot
				x = x_encoder.fit_transform(filedata[selected_columns[-2]])
				y = y_encoder.fit_transform(filedata[selected_columns[-1]])
				x_value = x_encoder.inverse_transform(x)
				y_value = y_encoder.inverse_transform(y)
				request.session['x']={'x_encoded':[str(i) for i in x], 'x_real':[str(i) for i in x_value]}
				request.session['y']={'y_encoded':[str(j) for j in y] , 'y_real':[str(j) for j in y_value]}
				x = [int(i) for i in request.session['x']['x_encoded']]
				y = [int(i) for i in request.session['y']['y_encoded']]
				request.session['minimum'] =  min(y)
				request.session['maximum'] = max(y)
				x_value = [(i,j,k,l) for i,j,k,l in zip(x, request.session['x']['x_real'], y ,request.session['y']['y_real'])]
				final_result = {'results': y , 'labels': x , 'plot':request.session['plot'], 'minimum':request.session['minimum'], 'maximum':request.session['maximum'], 'x_value':x_value, 'x_label':request.session['selected_columns'][-2],'y_label':request.session['selected_columns'][-1]}

			except Exception as e:
				print('---------------------error_message-----------------',e)
				
		if filters is not None:
			x_encoded = []
			y_encoded = []
			x_real = []
			y_real = []
			for i , j , k in zip(range(len(request.session['x']['x_encoded'])), [int(i) for i in request.session['x']['x_encoded']],[int(i) for i in request.session['y']['y_encoded']]):
				if k == int(filters):
					x_encoded.append(int(request.session['x']['x_encoded'][i]))
					y_encoded.append(int(request.session['y']['y_encoded'][i]))
					x_real.append(request.session['x']['x_real'][i]) 
					y_real.append(request.session['y']['y_real'][i])
			x_value = ''
			x_value = [(i,j,k,l) for i,j,k,l in zip(x_encoded, x_real, y_encoded ,y_real)]
			final_result = {'results': y_encoded , 'labels': x_encoded , 'plot':request.session['plot'], 'minimum':request.session['minimum'], 'maximum':request.session['maximum'], 'x_value':x_value, 'x_label':request.session['selected_columns'][-2],'y_label':request.session['selected_columns'][-1]}

		if limit is not None:
			x_encoded = []
			y_encoded = []
			x_real = []
			y_real = []
			for i , j , k in zip(range(len(request.session['x']['x_encoded'])), [int(i) for i in request.session['x']['x_encoded']],[int(i) for i in request.session['y']['y_encoded']]):
				if k <= int(limit):
					x_encoded.append(int(request.session['x']['x_encoded'][i]))
					y_encoded.append(int(request.session['y']['y_encoded'][i]))
					x_real.append(request.session['x']['x_real'][i]) 
					y_real.append(request.session['y']['y_real'][i])
			x_value = ''
			x_value = [(i,j,k,l) for i,j,k,l in zip(x_encoded, x_real, y_encoded , y_real)]
			final_result = {'results': y_encoded , 'labels': x_encoded , 'plot':request.session['plot'], 'minimum':request.session['minimum'], 'maximum':request.session['maximum'], 'x_value':x_value, 'x_label':request.session['selected_columns'][-2],'y_label':request.session['selected_columns'][-1]}

			if request.session['plot'] == None:
				request.session['plot'] = 'scatter'

		# print('-------final-------',final_result)
		return render(request, 'jupyterapp/configure.html', {'total_files' : total_files, 'final_result' : final_result})
	return render(request, 'jupyterapp/configure.html')







def load_data(request):
	filedata = pd.read_csv(file_directory + request.session['filename'], encoding='latin1')
	index = [i for i in range(len(filedata))]
	context = {'columns':list(filedata.columns), 'values':[], 'filename':request.session['filename'], 'index':index}
	for i in range(len(filedata)):
		row = []
		for j in list(filedata.columns):
			row.append(filedata[j].loc[i])
		context['values'].append(row)
	if request.method == 'POST':
		context = {'columns':list(filedata.columns), 'values':[], 'filename':request.session['filename'], 'index':index}
		initial = request.POST.get('initial')
		final = request.POST.get('final')
		request.session['initial'] = int(initial)
		request.session['final'] = int(final)
		for i in range(int(initial),int(final)):
			row = []
			for j in list(filedata.columns):
				row.append(filedata[j].loc[i])
			context['values'].append(row)
		return render(request, 'jupyterapp/load_data.html',context)

	return render(request, 'jupyterapp/load_data.html',context)

def preprocess(request):
	print('session----------------',request.session.keys())
	filedata = pd.read_csv(file_directory + request.session['filename'], encoding='latin1')
	index = [i for i in range(len(filedata))]
	if 'initial' in request.session.keys():
		index = [i for i in range(request.session['initial'], request.session['final'])]
	context = {'columns':list(filedata.columns), 'values':[], 'filename':request.session['filename'], 'index':index}
	filedata = filedata.apply(encoder.fit_transform)
	request.session['columns'] = list(filedata.columns)

	for i in index:
		row = []
		for j in list(filedata.columns):
			row.append(filedata[j].loc[i])
		context['values'].append(row)

	return render(request, 'jupyterapp/preprocess.html',context)


def select_data(request):
	request.session.pop('initial', None)
	request.session.pop('final', None)
	if request.method == 'POST':
		filename = request.POST.get('file')
		request.session['filename'] = filename
		return redirect('load_data')
	return render(request, 'jupyterapp/select_data.html', {'total_files':total_files} )

def select_columns(request):
	if request.method == 'POST':
		filedata = pd.read_csv(file_directory + request.session['filename'], encoding='latin1')
		selected_columns = []
		for i in request.session['columns']:
			i = request.POST.get(i)
			if i != None:
				selected_columns.append(i)
		request.session['selected_columns'] = selected_columns
		return redirect('configure')

	return render(request , 'jupyterapp/select_columns.html',{'columns':request.session['columns']} )