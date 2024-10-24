import pandas as pd
import numpy as np

def time_norm(data):
    data['Tnorm'] = (data['Time [s]'] - data['Time [s]'].min()) / (data['Time [s]'].max() - data['Time [s]'].min())

def cut_norm(data,time):
    data=data.loc[data['Time [s]']<time]
    return data

def interpolate_and_sample(data,time_to_cut,nvalues_to_interpolate):
    aux=data['Time [s]'].max()
    x_to_interpolate=np.linspace(0,time_to_cut,num=nvalues_to_interpolate)

    x=data['Time [s]'].values
    new_data=pd.DataFrame()
    new_data['Time [s]']=x_to_interpolate
    aux_array = np.empty(nvalues_to_interpolate,dtype=float)
    for i in range(nvalues_to_interpolate):
        aux_array[i]=i+1
    new_data['Cycle Nr.']=aux_array

    for column in data.columns.values[2:]:
        new_array = np.empty(x_to_interpolate.shape[0],dtype=float)
        y=data[column].values

        new_array=np.interp(x_to_interpolate,x,y) 
    
        new_data[column]= new_array    #Introducing the new interpolated column

    new_data=new_data.loc[(new_data['Cycle Nr.']==1) | (new_data['Cycle Nr.']%3==0)]    #Sampling of 1/3

    return new_data
                
def normalizeDf(data):
    aux=data.values
    aux=(aux - np.min(aux)) / (np.max(aux) - np.min(aux))
    aux2=pd.DataFrame(aux)
    return aux2
