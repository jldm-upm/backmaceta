# -*- mode: python; coding: utf-8 -*-
#
###########################################################################
# Filename:    tarea.py
# -------------------------------------------------------------------------
# Proyecto:     C.E.S.P.E.D.
# Autor:      José L. Domenech
# Descripcion:
#
#   Ejecuta una función (sin parámetros) de forma periódica (cada N
#   segundos o fracción de segundo)
#
# Requiere:    threading, time
# -------------------------------------------------------------------------
# Historia:
#   + 05/11/2019 - Primera version
###########################################################################

import threading
import time

import cesped.utilidades as utils


class Tarea(threading.Thread):
    def __init__(self, ctrl, func, ms):
        ''' Constructor '''
        threading.Thread.__init__(self)
        self.ejecutando = True
        self.ctrl       = ctrl
        self.funcion    = func
        self.periodo    = ms

    def run(self):
        ''' `Thread.run' (forma parte de la API de `threading.Thread')'''
        time.sleep(self.periodo / utils.FLOAT_MS_IN_SEG)
        while getattr(self, "ejecutando", True):
            t1 = utils.timestamp()
            self.funcion()
            # NOTA: Bien, pero puede aparecer una desviación en la
            # activación de una tarea
            ms_espera = max(0, self.periodo - (utils.timestamp() - t1))
            time.sleep(ms_espera / utils.FLOAT_MS_IN_SEG)
            self.ejecutando = True

    def stop(self):
        '''Para la tarea.'''
        self.ejecutando = False

    ejecutando = True
    ctrl       = None
    funcion    = lambda x: x
    periodo    = 1000
