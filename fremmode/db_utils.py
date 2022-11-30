from fremmode.models import Medlemmer, Fremmode


def get_deltager_matrix(medlems_list, date_list):
    print(medlems_list)
    print(date_list)
    entry=[]
    for i in range(len(date_list)):
        entry.append(0)
    print(entry)
    array=[]
    for i in range(len(medlems_list)):
        array.append(entry)
        
    print(array)
    
    # deltagere = Fremmode.objects.filter(Date__gte=fromdate).filter(Date__lte=todate)
    
    # for d in deltagere:
    #     entry = (0,1,2,3)
    #     matrix[d.Medlem]= entry
        
    # print(matrix)
    # print(deltagere)
    # print(deltagere.values())
    # print(list(deltagere))
   
    return None
