from django import forms

#move this code
notes = ['c','C','d','D','e','f','F','g','G','a','A','b']
guitar_tuning = {'Standard': {0:'e',1:'b',2:'g',3:'d',4:'a',5:'e'}, 'OpenDsus4':{0:'d',1:'a',2:'g',3:'d',4:'a',5:'d'}}
guitar_octave = {'Standard': {0:(5,4), 1:(4,11),2:(4,7),3:(4,2),4:(3,9),5:(3,4)}} #(open_octave, steps_from_this_octave)

guitar = guitar_tuning['Standard']
open_octave = guitar_octave['Standard']

def get_note(start_note,fret):

  i = notes.index(start_note)
  note = notes[(i+fret)%len(notes)]
  return note

def get_octave(fret, string_num):

  octave = open_octave[string_num][0] + (fret + open_octave[string_num][1])/len(notes)
  return str(octave)   

def get_line_note(digits, digit, string_num, ignore_next):

  if ignore_next:
    ignore_next = False
    return '*', '-', ignore_next
    
  elif digits and unicode(digits).isnumeric():
    ignore_next = True
    return get_note(guitar[string_num],int(digits)), get_octave(int(digits),string_num), ignore_next 
     
  elif unicode(digit).isnumeric():  
    return get_note(guitar[string_num],int(digit)), get_octave(int(digit),string_num), ignore_next
    
  else:
    return digit, '-', ignore_next

###    

class TabConverterForm(forms.Form):
    
    guitar_tab_text = forms.CharField(widget=forms.Textarea(attrs={'rows':12, 'cols':100}))
    
    def convert_to_piano_tab(self):
    
        guitar_tab_file = self.cleaned_data.get('guitar_tab_text','')
        #print guitar_tab_file
        piano_tab_file = []

        string_num = 0
        ignore_next = False
        guitar_tab_lines = guitar_tab_file.splitlines()
        #print guitar_tab_lines
        for line in guitar_tab_lines:
          l = line.strip()
          #print l
          piano_line = ""
  
          for i in range(0,len(l)):
            digits = None
    
            if(i+1 != len(l)):
              digits = str(l[i])+str(l[i+1])
            digit = l[i]
    
            note, octave, ignore_next = get_line_note(digits, digit, string_num, ignore_next)
            piano_line += (note+octave)
      
          piano_tab_file.append(piano_line)
          if(l == ""): #blank line, don't add string
            continue
          string_num += 1
          if string_num == 6:
            string_num = 0  
        
        #print ''.join(piano_tab_file)
        '''for line in piano_tab_file:
          print line'''    
        return piano_tab_file
        #pass

          

         
      
    
    
        
