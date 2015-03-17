# -*- coding: utf-8 -*-
#!/usr/bin/env python
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Author:
#     Anna Chabuda <anna.chabuda@gmail.com>
#

import glob
import os.path

def get_file_name(search_name, search_dir):
    search_dir  = os.path.expanduser(search_dir)  
    files = glob.glob(('{}/{}').format(search_dir, search_name))
    for file_ in files:
        yield file_

def set_first_timestamp(mgr):
    first_timestamp = float(mgr.get_param('first_sample_timestamp'))
    for tag in mgr.get_tags():
        tag['start_timestamp'] -= first_timestamp
        tag['end_timestamp'] -= first_timestamp 
    return mgr
