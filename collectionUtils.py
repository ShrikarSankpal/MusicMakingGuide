import pandas

df_scales = pandas.read_csv('datasets/df_scalesData.csv')
df_chords = pandas.read_csv('datasets/df_chordsData.csv')
df_ScalesFormulae=pandas.read_csv("datasets/allScalesAndFormulae.csv")
df_ChordsFormulae=pandas.read_csv("datasets/allChordsAndFormulae.csv")

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
            temp="'-'".join(row['indexNoteChord'][1:-1].\
                replace(",","").\
                    split(" ")).\
                        replace("'-'","").\
                            replace("''"," ")[1:-1]
            #print(temp)
            result['Chords Containing Given Notes'].append(temp)
            if len(interxn)==len(A):
                result['Exact Matches'].append(temp)
            
    
    if len(result['Chords Containing Given Notes'])==0:
        return "Not Found"
    else:
        return result
    
def getScaleNotes(scale_base_note, scale_type):
    #print("User entered: ",scale_base_note, scale_type)
    result={'Exact Matches':[],'Nearby':[]}
    filter_1 = ((df_scales['Note']==scale_base_note) & (df_scales['Scale']==scale_type)).values
    scaleNotes=list(df_scales.iloc[filter_1]['Notes'].values)
    #print("ScaleNotes: ", scaleNotes)
    result['Exact Matches'].append(scaleNotes)
    print("returning: ",result)

    return result


def getChordNotes(chord_base_note, chord_type):
    #print("User entered: ",chord_base_note, chord_type)
    result={'Exact Matches':[],'Nearby':[]}
    
    for index, row in df_chords.iterrows():
        #print(type(row.str))
        #print(row)
        name=row['indexNoteChord'].strip("()").split(", ")
        #print(name[0][1:-1],name[1][1:-1])
        if (name[0][1:-1]==chord_base_note) & (name[1][1:-1]==chord_type):
            print("Match Found: ",name[0][1:-1],name[1][1:-1], row['ChordNotes'])
            result['Exact Matches'].append(row['ChordNotes'])
            break
    print("returning: ",result)

    return result


def getScaleTypes():
    return list(df_ScalesFormulae['Type'].unique())

def getChordTypes():
    return list(df_ChordsFormulae['chordName'].unique())

def sendDict():
    temp={'scale_types':[],'chord_types':[]}
    temp['scale_types']=getScaleTypes()
    temp['chord_types']=getChordTypes()
    return temp


if __name__=='__main__' :
    #print(getScale("C D E F G A"))
    #print(getChord("C E A"))
    #getChord("C E A")
    #print(getScaleNotes("C","Natural_Minor"))
    #print(getScaleTypes())
    #print(sendDict())
    print(getChordNotes("C","Major"))