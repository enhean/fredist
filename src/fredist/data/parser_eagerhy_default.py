#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author: Enrique Henestroza Anguiano
#

"""
Template: A user-modifiable file to quickly generate feature vectors for
parsing and correction.
"""

import sys
from dtbutils import *

class Template(object):

    def __init__(self):

        return


    #
    # Obtain feature vector given features corresponding to items s_X and n_X.
    #
    def feature_vector(self,s_0,s_1,s_2,n_0,n_1,n_2,n_3,d_0,c_0,c_d,fpos):

        if fpos in ['P', 'P+D', 'P+PRO']: #, 'CC', 'CS']:
            return n_0[FPS]+\
                   n_0[LEM]+\
                   n_0[LFPS]+\
                   n_0[LLAB]+\
                   n_1[FPS]+\
                   n_1[LEM]+\
                   n_2[FPS]+\
                   n_3[FPS]+\
                   s_0[FPS]+\
                   s_0[LEM]+\
                   s_0[LAB]+\
                   s_0[HFPS]+\
                   s_0[HLEM]+\
                   s_0[LFPS]+\
                   s_0[LLAB]+\
                   s_0[RFPS]+\
                   s_0[RLAB]+\
                   c_0[FPS]+\
                   c_0[LEM]+\
                   c_0[LAB]+\
                   c_0[HFPS]+\
                   c_0[HLEM]+\
                   c_0[LFPS]+\
                   c_0[LLAB]+\
                   c_0[RFPS]+\
                   c_0[RLAB]+\
                   c_d[LDIS]+\
                   c_d[GDIS]+\
                   c_d[NDEP]+\
                   c_d[PUNC]
        else:
            return n_0[FPS]+\
                   n_0[LEM]+\
                   n_0[LFPS]+\
                   n_0[LLAB]+\
                   n_1[FPS]+\
                   n_1[LEM]+\
                   n_2[FPS]+\
                   n_3[FPS]+\
                   s_0[FPS]+\
                   s_0[LEM]+\
                   s_0[LAB]+\
                   s_0[HFPS]+\
                   s_0[HLEM]+\
                   s_0[LFPS]+\
                   s_0[LLAB]+\
                   s_0[RFPS]+\
                   s_0[RLAB]+\
                   s_1[FPS]+\
                   s_2[FPS]
        
