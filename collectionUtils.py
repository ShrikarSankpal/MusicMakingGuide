import pandas

df_scales = pandas.read_csv('datasets/df_scalesData.csv')
df_chords = pandas.read_csv('datasets/df_chordsData.csv')

def getScale(lst_notes):
    result={'Exact Matches':[],'Scales Containing Given Notes':[]}
    for index, row in df_scales.iterrows():
        A = set([i[1:-1] for i in row['Notes'].split(", ")])
        B = set(lst_notes.split())

        interxn = set.intersection(A,B)
        #print("set1: ", A, type(A),len(A))
        #print("set2: ", B, type(B),len(B))
        #print("intersection: ",interxn)
        
        if len(interxn)==len(B):
            result['Scales Containing Given Notes'].append(row['Note']+" "+row['Scale'])
            if len(interxn)==len(A):
                result['Exact Matches'].append(row['Note']+" "+row['Scale'])
    
    if len(result['Scales Containing Given Notes'])==0:
        return "Not Found"
    else:
        return result

def getChord(lst_notes):
    result={'Exact Matches':[],'Chords Containing Given Notes':[]}
    
    for index, row in df_chords.iterrows():
        A = set(row['ChordNotes'].split(","))
        B = set(lst_notes.split())
        interxn = set.intersection(A,B)
        #print("set1: ", A, type(A),len(A))
        #print("set2: ", B, type(B),len(B))
        #print("intersection: ",interxn)
        
        if len(interxn)==len(B):
            result['Chords Containing Given Notes'].append(row['indexNoteChord'])
            if len(interxn)==len(A):
                result['Exact Matches'].append(row['indexNoteChord'])
            
    
    if len(result['Chords Containing Given Notes'])==0:
        return "Not Found"
    else:
        return result
    
    
#print(getScale("C D E F G A"))
#print(getChord("C E A"))