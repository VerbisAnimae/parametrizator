#!/usr/bin/env python
# coding: utf-8

import streamlit as st
from urllib import parse
from urllib.request import urlopen
from urllib.parse import (
        urlencode, unquote, urlparse, parse_qsl, urljoin, urlsplit, SplitResult
    )
import pyperclip

#import html 
#Cabecera con estilo

html_temp = """
<style>.icon-button {display:none}.streamlit-button {
    display: inline-flex;
    position: absolute;
    right:0;
    align-items: center;
    justify-content: center;
    font-weight: 400;
    padding: .375rem .75rem;
    border-radius: .25rem;
    margin: 0;
    line-height: 1.6;
    color: #262730;
}
div:nth-child(15) {padding-bottom:30px}
</style>
<div style="background-color:{};padding:{}">
<center><img src="https://pbs.twimg.com/profile_banners/361128374/1567413737/1500x500" alt="Logo de Cheil" width="600" style="width: 100%;
  max-width: 400px;
  height: auto;"></center>
<h1 style="color:#044a9d;text-align:center;">PARAMETRIZADOR PARA CHEIL </h1>
<h3 style="color:orange;text-align:center;margin-top:5px;">Developed by Raúl Fernández</h3>
<p style="margin-top:20px; margin-bottom:40px">Cuando introduzcas una nueva URL, recuerda volver a dar al enter.</p>
</div>
"""
st.markdown(html_temp,unsafe_allow_html=True)


url = st.text_input("Introduce la URL y dale al enter")
#url= input('Please enter your URL:\n')

if url.endswith('/')== False:
    u_final=url+'/'
else:
    u_final=url

query = urlparse(url).query
        
st.text('¿Para qué tercero es?')
gmb = st.checkbox('GMB')
if gmb:
    st.text('¿Alguna tienda en particular?')
    Madrid = st.checkbox('Madrid')
    if Madrid:
        source = 'google-madrid'
    Valencia = st.checkbox('Valencia')
    if Valencia:
        source = 'google-valencia'        
    google = st.checkbox('Genérico')
    if google:
        source = 'google'  
    medium='organic'
    st.text('Elige el tipo de campaña:')
    Logica = st.checkbox('Lógica de la herramienta')
    if Logica:    
        campaign='gmb'
        if url.find('/offer/') != -1:
            typeofcampaign=campaign+'-offer'
        else:
            typeofcampaign=campaign+'-product'
            
    Offer = st.checkbox('Offer')
    if Offer:    
        typeofcampaign='gmb-offer'
    
    Product = st.checkbox('Product')
    if Product:    
        typeofcampaign='gmb-product'
    
    Evento = st.checkbox('Event')
    if Evento:    
        typeofcampaign='gmb-event'
        
    url_concatenated=parse.urlencode({'utm_source':source,'utm_medium':medium, 'utm_campaign':typeofcampaign })
    
    if not query:
        url_final= '?'+url_concatenated
    else:
        url_final= '&'+url_concatenated
    
    if not query:
        v = u_final + url_final    
    else:
        v = u_final.rstrip('/') + url_final
        
    st.write('Aquí tienes tu URL: %s' % v)
    copy=st.button('Copiar')
    if copy:
        pyperclip.copy(v)  # now the clipboard content will be string "abc"
        text = pyperclip.paste()  # text will have the content of clipboard
        st.write('¡URL copiada!')
other = st.checkbox('Otro')
if other:
    parameter=st.text_input('Introduce el primer párametro')
    parameter_value= st.text_input('Introduce su valor')
    second_parameter=st.text_input('Introduce el segundo párametro')
    parameter_second_value= st.text_input('Introduce el segundo valor')
    third_parameter=st.text_input('Introduce el tercer párametro')
    parameter_third_value= st.text_input('Introduce el tercer valor')
    query = urlparse(url).query

    url_concatenated=parse.urlencode({parameter:parameter_value,second_parameter:parameter_second_value, third_parameter:parameter_third_value })
#params = query.split('=')
#print(params)
    if not query:
        url_final= '?'+url_concatenated
    else:
        url_final= '&'+url_concatenated
    if not query:
        v = u_final + url_final    
    else:
        v = u_final.rstrip('/') + url_final
    
    st.write('Aquí tienes tu URL: %s' % v)
    copy2=st.button('Copiar')
    if copy2:
        pyperclip.copy(v)  # now the clipboard content will be string "abc"
        text = pyperclip.paste()  # text will have the content of clipboard
        st.write('¡URL copiada!')




