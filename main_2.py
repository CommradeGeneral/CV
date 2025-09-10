import info,skills
import os

latex_file = open("Muhammad_Hashim.tex","w")

#---- premables

premables = '''%begining of latex
\\documentclass[9pt]{extarticle}
\\input{packages.tex}
\\input{configs.tex}
\\begin{document}
\\pagenumbering{gobble}
\\noindent
\\begin{tikzpicture}
	\\path (0,0) coordinate (left) -- (\\linewidth,0) coordinate (right);
	\\node [anchor = north west, inner sep = 0pt,scale = 1.6] (name) at (left) {%
		\\bfseries\\Large
		'''

premables = premables + info.personal_info["Name"] + '};'

premables = premables + '''
        \\node [anchor = north west, inner sep = 0pt, scale = 1.3] (title) at ([yshift = -1ex]name.south west){%
            \\bfseries
            ''' + info.personal_info["Title"] + '};'
premables = premables + '''
        \\node [anchor = north west, inner sep = 1ex] (info0) at ([yshift = -1ex] title.south west) {
            \\varBox{\\linewidth}{\\begin{itemize}[nosep,align=left,labelwidth=\\widthof{W:},leftmargin = !,font=\\bfseries]'''


premables = premables + '''
                \\begin{multicols}{2}
                '''
try:
    premables = premables + '''
            \\item[\\faMapMarker*] '''
    v = 0
    for u in info.personal_info["Address"]:
        premables= premables + u
        v = v + 1
        if v < len(info.personal_info["Address"]):
            premables = premables + ' \\par '
except KeyError:
    pass

premables = premables + ''' \\item[\\faMobile*] '''
y = 0

for x in info.personal_info["Tel"]:
    premables = premables + x + ' '
    y = y+1
    if y < len(info.personal_info["Tel"]):
        premables = premables + ' - '

y = 0
z = 0

try:
    for x in info.personal_info["Whatsapp"]:
        y = y + 1
        if y==1:
            premables = premables + '''            
                \\item[\\faWhatsapp] '''

        premables = premables + x + ' '
        z = z + 1
        if z < len(info.personal_info["Whatsapp"]):
             premables = premables + ' - '
except KeyError:
    pass

y = 0
z = 0

try:
    for x in info.personal_info["Telegram"]:
        y = y + 1
        if y==1:
            premables = premables + '''            
                \\item[\\faTelegram] '''

        premables = premables + x + ' '
        z = z + 1
        if z < len(info.personal_info["Telegram"]):
             premables = premables + ' - '
except KeyError:
    pass


premables = premables + '''            
                \\columnbreak '''


y = 0
z = 0

try:
    premables = premables + '''
                \\item[\\faAt] '''
    for x in info.personal_info["Email"]:
        premables = premables + x + ' '
        z = z + 1
        if z < len(info.personal_info["Email"]):
             premables = premables + '\\par '
except KeyError:
    pass

y = 0
z = 0
try:
    for x in info.personal_info["LinkedIn"]:
        if z == 0:
            premables = premables + '''
                \\item[\\faLinkedin] '''
            
        premables = premables + x + ' '
        z = z + 1
        if z < len(info.personal_info["LinkedIn"]):
             premables = premables + '\\par '
except KeyError:
    pass

y = 0
z = 0
try:
    for x in info.personal_info["Github"]:
        if z == 0:
            premables = premables + '''
                \\item[\\faGithub] '''
            
        premables = premables + x + ' '
        z = z + 1
        if z < len(info.personal_info["Github"]):
             premables = premables + '\\par '
except KeyError:
    pass

premables = premables + '''
            \\end{multicols}'''


premables = premables + '''
            \\end{itemize}}};'''



premables = premables + '''
        \\begin{scope}[on background layer]
            \\fill [light!40] (info0.north west) rectangle (right |- current bounding box.south);
        \\end{scope}'''


premables = premables + '''
\\end{tikzpicture}
'''
premables = premables + '''
\\columnratio{0.6}
\\begin{paracol}{2}
\\section{Summary}
'''
premables = premables + info.my_objective



premables = premables + '''
\\section{Work experience}

'''

for x in info.work_experience:
    try:
        temp = x["Positions"]
        for y in x["Positions"]:
            premables = premables + '\\begin{expbox}[title = {\\bfseries ' + y["Position"] + '}]\n'
            premables = premables + '\t {\\bfseries ' + x["Name"] + '} \n'
            premables = premables + '\t \\begin{itemize}[nosep,align = left, leftmargin = !, labelwidth = \\widthof{L:}] \n'
            premables = premables + '\t\t \\item[\\faCalendar*] ' + y["Duration"][0] + ' - ' + y["Duration"][1] + '\n'
            premables = premables + '\t\t \\item[{\\faMapMarker*}] ' + x["Headquarter"] + '\n'
            try:
                premables = premables + '\t\t \\item[{\\seg\\char"EA8D}] ' + y["Location"] + '\n'
            except KeyError:
                pass

            
            try:
                temp = y["Position_Det"]
                premables = premables + '\t \\end{itemize}\n'
                premables = premables + '{\t\\color{light}\\dotfill}\\smallskip \n'
                premables = premables + '\t \\begin{itemize}[nosep,align = left, leftmargin = !, labelwidth = \\widthof{L:}]\\raggedright\n'
                premables = premables + y["Position_Det"]
                premables = premables + '\t \\end{itemize}\n'
            except:
                pass
            
            premables = premables + '\\end{expbox}\n'
            #\begin{itemize}[nosep,align = left, leftmargin = !, labelwidth = \widthof{L:}]
    except KeyError:
        pass

    
        y = x
        premables = premables + '\\begin{expbox}[title = {\\bfseries ' + y["Position"] + '}]\n'
        premables = premables + '\t {\\bfseries ' + x["Name"] + '} \n'
        premables = premables + '\t \\begin{itemize}[nosep,align = left, leftmargin = !, labelwidth = \\widthof{L:}] \n'
        premables = premables + '\t\t \\item[\\faCalendar*] ' + y["Duration"][0] + ' - ' + y["Duration"][1] + '\n'
        premables = premables + '\t\t \\item[{\\faMapMarker*}] ' + x["Headquarter"] + '\n'
        try:
            premables = premables + '\t\t \\item[{\\seg\\char"EA8D}] ' + y["Location"] + '\n'
        except KeyError:
            pass

        try:
            temp = y["Position_Det"]
            premables = premables + '\t \\end{itemize}\n'
            premables = premables + '{\t\\color{light}\\dotfill}\\smallskip \n'
            premables = premables + '\t \\begin{itemize}[nosep,align = left, leftmargin = !, labelwidth = \\widthof{L:}]\\raggedright\n'
            premables = premables + y["Position_Det"]
            premables = premables + '\t \\end{itemize}\n'
        except:
            pass

        premables = premables + '\\end{expbox}\n'
# --- edu

premables = premables + '''
\\section{Education}

'''

for x in info.education:
    premables = premables + '\\begin{expbox}'
    premables = premables + '[' + 'title = {\\bfseries ' + x["Degree"] +  '}]\n'
    premables = premables + '\t\\begin{itemize}[nosep,align = left, leftmargin = !, labelwidth = \\widthof{L:}]\\raggedright\n'
    try:
        premables = premables + '\t\t\\item[\\faUniversity] ' + x["Faculty"] +' - ' + x["Name"] + '.\n'
    except KeyError:
        pass


    #\\item[\\faCalendar*] ' + y["Duration"][0] + ' - ' + y["Duration"][1] + '\n'
    try:
        premables = premables + '\t\t\\item[\\faCalendar*] ' + x["Duration"][0] + ' - ' + x["Duration"][1] + '\n'
    except KeyError:
        pass

    premables = premables + '\t\\end{itemize}\n'
    premables = premables + '\\end{expbox}\n\n'

# --- skills
premables = premables + '''
\\switchcolumn  
\\section{Languages}

'''

j = 1
for x in skills.Languages["skills"]:
    premables = premables +'\\languageitem[' + "{}".format(x["Level"][0]) + ']{' + x["Name"] + '}{'+ x["Level"][1] +'}'
    if j < len(skills.Languages["skills"]):
        premables = premables + '\\par\\medskip'

    premables = premables + '\n'
    j = j + 1;

premables = premables + '''
\\section{Skills}

'''


premables = premables + '''
\\begin{description}[nosep, align = left, style=nextline]\\raggedright
'''

for x in skills.my_skills:
    premables = premables + "\t\\item[" + x["Name"] + "]\n"
    u = 0
    try:
        y = x["Description"]
        premables = premables + "\t{\\color{light}" + y + "}\n"
        u = 1
    except KeyError:
        pass

    try:
        y = x["skills"]
        if (u==1):
            premables = premables + "\t\\par\n"

        v = 1
        for z in x["skills"]:
            premables = premables + "\t\\inlineitemi[" + "{}".format(z["Level"][0]) + "]{" + z["Name"] +""
            try:
                premables = premables + " (" + z["Level"][1] + ")"
            except IndexError:
                    pass
            
            
            
            premables = premables + "}"


            premables = premables + "\n"

    except KeyError:
        pass
    
    #premables = premables + "\t\\begin{}"
    
premables = premables + '''
\\end{description}
'''
# --- end skills


#-- courses

premables = premables + '''
\\section{Courses \\& Achievements}

'''

for x in info.courses:
    premables = premables + '\\begin{expbox}[title = {\\bfseries\\raggedright ' + x["Name"] + '}]\n'
    premables = premables + '\t {\\bfseries\\raggedright ' + x["Training Center"] + '} \n'
    premables = premables + '\t\\begin{itemize}[nosep,align = left, leftmargin = !, labelwidth = \\widthof{L:}]\\raggedright\n'

    try:
        premables = premables + '\t\t\\item[\\faCalendar*] ' + x["Duration"][0] + ' - ' + x["Duration"][1] + '\n'
    except KeyError:
        pass

    try:
        premables = premables + '\t\t\\item[\\faMapMarker*] ' + x["Location"] + '. \n'
    except KeyError:
        pass

    try:
        temp_val = x["Tracks"]
        n = 0
        premables = premables + '\t\t\\item[{\\bfseries Tracks:}] \\phantom{.}\n'
        premables = premables + '\t\t\\begin{itemize}[nosep,leftmargin = *, align = left] \\raggedright\n'
        for y in x["Tracks"]:
            premables = premables + '\t\t\t\\item ' + y + '\n'

        premables = premables + '\t\t\\end{itemize}\n'
    except KeyError:
        pass
    premables = premables + '\t\\end{itemize}\n'
    premables = premables + '\t\\end{expbox}\n'


premables = premables + '''
\\section{Personal Info}

'''
premables = premables + '\\begin{itemize}[nosep,align = left, leftmargin = !, labelwidth = \\widthof{L:}]\\raggedright\n'
try:
    premables = premables + '''
            \\item[\\faMapMarker*] '''
    v = 0
    for u in info.personal_info["Address"]:
        premables= premables + u
        v = v + 1
        if v < len(info.personal_info["Address"]):
            premables = premables + ' \\par '
            
except KeyError:
    pass

try:
    premables = premables + '''
            \\item[\\faBirthdayCake] ''' + info.personal_info["DoE"] 
except KeyError:
    pass

premables = premables + '\\end{itemize}\n'

premables = premables + '''
\\end{paracol}
\\end{document}
'''




latex_file.write(premables)
latex_file.close()

os.system("lualatex -interaction=nonstopmode -shell-escape Muhammad_Hashim.tex rm Muhammad_Hashim.aux Muhammad_Hashim.log Muhammad_Hashim-inc.eps Muhammad_Hashim.tex Muhammad_Hashimconverted-to.pdf ")
os.startfile("Muhammad_Hashim.pdf")
print(premables)
