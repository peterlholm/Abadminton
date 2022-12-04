import numpy as np
from fremmode.models import Fremmode

def get_deltager_matrix(medlems_list, date_list):
    "Create the matrix with fremmoder"
    # pylint: disable=invalid-name

    array = np.zeros((len(medlems_list),len(date_list)),dtype=int)
    frem = Fremmode.objects.filter(Date__gte=date_list[0]).filter(Date__lte=date_list[-1]).order_by('Date')
    for f in frem.values():
        if f['Date'] in date_list:
            index = date_list.index(f['Date'])
            if f['Medlem'] in medlems_list:
                array[medlems_list.index(f['Medlem'])][index] = f['State']
            elif f['Medlem'] <= 0:
                for m in range(len(medlems_list)):
                    array[m][index] = f['State']
    return array
