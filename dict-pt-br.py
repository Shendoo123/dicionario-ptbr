#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from xml.etree import ElementTree as ET
import os
import glob

dados = []
gramatica = []
i = 0
# My path
path = os.getcwd() + '/dicionarioXML'
#allFiles = glob.glob(path+'/*.xml')
allFiles = glob.glob(path+'/M.xml')

# Saving the dictionary
for fil in allFiles:
    print('Processing the file: ', fil[-5:])
    root = ET.parse(fil).getroot()
    for word in root.findall('entry'):
        gotWord  = False
        gotOrth  = False
        gotGram  = False

        try:
            iD = word.get('id')
            gotWord = True
        except AttributeError:
            pass
        try:    
            orth = word.find('form/orth').text
            gotOrth = True
        except AttributeError:
            pass
        try:
            temp = []
            j = 0
            temp.append([])
            for senti in word:
                for grama in senti.findall('gramGrp'):
                    temp[j].append(grama.text)
                
                for sen in senti.findall('def'):
                    defi = sen.text
                    defi = defi.replace('\n' ,'')
                    defi = defi.replace('_' ,'')
                    temp[j].append(defi)

                if temp[j] != []:
                    j += 1
                    temp.append([])

            if len(temp) != 0:
                if temp[-1] == []:
                    del temp[-1]
                gramatica.append([])
                gramatica[i] = temp
            gotGram = True
        except AttributeError:
            pass
        if gotGram and gotOrth and gotWord:
            dados.append([])
            #print(gramatica[i])
            dados[i] = [iD, orth.lower(), gramatica[i]]
            i += 1

#print(dados)
print(type(dados))

# métodos de pesquisa
#print('manga:1' in dic_pt_br) #retorna true ou falso
#print(contatos['manga:2']) #outro método de busca
#print('zanga:2' in dic_pt_br.keys())

#consulta de palavras

'''
dados = []
i = 0
path = os.getcwd() + '/dicionarioXML'
#allFiles = glob.glob(path+'/*.xml')
allFiles = glob.glob(path+'/M.xml')

for fil in allFiles:
    print('Processing the file: ', fil[-5:])
    root = ET.parse(fil).getroot()
    
    for word in root.findall('entry'):
        gotWord  = False
        gotOrth  = False
        gotGram  = False
        gotDefi  = False

        try:
            iD = word.get('id')
            gotWord = True
        except AttributeError:
            pass
        try:    
            orth = word.find('form/orth').text
            gotOrth = True
        except AttributeError:
            pass
        try:
            gram = word.find('sense/gramGrp').text
            gotGram = True
        except AttributeError:
            pass
        try:
            defi = word.find('sense/def').text
            gotDefi = True
        except AttributeError:
            pass
        if gotDefi and gotGram and gotOrth and gotWord:
            dados.append([])
            defi = defi.replace('\n' ,'')
            defi = defi.replace('_' ,'')
            dados[i] = [iD, orth.lower(), gram, defi]
            i+=1
'''
