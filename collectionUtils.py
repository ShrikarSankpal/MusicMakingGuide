import pandas

df_scales = pandas.read_csv('datasets/df_scalesData.csv')
#print(df_scales)

def getScale(lst_notes):
    lst_toReurn=[]
    #print("In getScale()")
    #print("lst_notes: ",lst_notes, len(lst_notes))
    #print("lst_notes, split: ",lst_notes.split(),type(lst_notes.split()))
    for index, row in df_scales.iterrows():

        #print(row['Notes'].strip('[').strip(']').split(' ,'))
        #print("row['Notes]: ",row['Notes'],type(row['Notes']), row['Note'],row['Scale'])
        #print("splitted row['Notes]: ",row['Notes'].split(", "))
        A = set([i[1:-1] for i in row['Notes'].split(", ")])
        B = set(lst_notes.split())
        
        #symm_diff = set.symmetric_difference(A,B)
        interxn = set.intersection(A,B)
        #print("set1: ", A, type(A),len(A))
        #print("set2: ", B, type(B),len(B))
        #print("intersection: ",interxn)
        
        if len(interxn)==len(B):
            #print("Exact match found")
            lst_toReurn.append(row['Note']+" "+row['Scale'])
    
    if len(lst_toReurn)==0:
        return "Not Found"
    else:
        return lst_toReurn
    
    
print(getScale("C D E F G A B C"))