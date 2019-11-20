# -*- mode: python; coding: utf-8 -*-
#
################################################################################
# Filename:    endpoint.py
#-------------------------------------------------------------------------------
# Project:     C.E.S.P.E.D.
# Author:      José L. Domenech
# Description:
#
#   Define un EndPoint, como una url y los parámetros necesarios, con
#   el que se puede realizar una petición POST para enviar datos que
#   serán codificados como JSON
#
# Requiere: json, requests
#-------------------------------------------------------------------------------
# Historia:
#   + 05/11/2019 - First version
################################################################################

import json
import requests


class EndPoint:

    def __init__(self, url, timeout_s=3.0, **kwargs):
        '''url:     string
           timeout_s: tiempo de espera antes de cerrar la conexión (3 s)
           kwargs:  se usará como dict con keys como strings que se
                    sustituiran por su valor en la url

             e.j.) EndPoint('https://api.com?param=_KEY_',_KEY_='clave')
              sería equivalente a EndPoint('https://api.com?param=clave')
        '''
        self.url       = url
        self.timeout_s = timeout_s
        self.subst     = kwargs

    def enviar_post_json(self, dato):
        '''envia un `dato' que será previamente convertido a formato JSON'''

        mi_url = self.url
        for k in self.subst:
            mi_url = mi_url.replace(k, self.subst[k])

        resultado = requests.post(mi_url, timeout=self.timeout_s, json=dato)

        print("enviar_post_json: Resultado=" + str(resultado))
        print(resultado.content)
        
        return resultado
