# -*- coding: utf-8 -*-
"""
Description:
    SETSIMENV Set simulation envirement.

EXAMPLE:
    setsimenv
    
INPUT:
    
    
OUTPUT:
    
 
 Copyright, 2018 (C), H.B. Zhang, <hongbo.zhang83@gmail.com>

Modifications:
Version    Date        Author        Log.
V1.0       20180714    H.B. Zhang    Create this script
Ref:

"""

import os
import sys

def get_current_path(self):
    paths = sys.path
    current_file = os.path.basename(__file__)
    for path in paths:
        try:
            if current_file in os.listdir(path):
                self.current_path = path
                break
        except (FileExistsError,FileNotFoundError) as e:
            print(e)
