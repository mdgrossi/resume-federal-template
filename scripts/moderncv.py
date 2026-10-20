from IPython.display import Markdown

def list_html(items):
    """Generate html syntax for a list of values. Note that this returns a
    string of html code needed to create a table, not a table itself. This is
    used within a Quarto markdown files to display a table when that file is
    rendered.
    
    ARGUMENTS
    ---------
    items: list of dictionaries containing the table entries as values. 
        Normally, this dictionary would be from the YAML front matter of a
        Quarto markdown file.
    """
    
    list_start = "<html><ul>"
    list_end = "</ul></html>"
    key, _ = list(items[0].items())[0]
    items = "".join(f"<li>{i[key]}</li>" for i in items)
    html_list = list_start + items + list_end
    display(Markdown(html_list))

def mdlist(items, bullets=True):
    """Generate markdown syntax for a list of values. Note that this returns a
    string of markdown code needed to create a table, not a table itself. This
    is used within a Quarto markdown files to display a table when that file is
    rendered.
    
    ARGUMENTS
    ---------
    items: list of dictionaries containing the table entries as values. 
        Normally, this dictionary would be from the YAML front matter of a
        Quarto markdown file.
    bullets: Bool, whether or not to include bullets in the list. Defaults to
        True.
    """
    
    key, _ = list(items[0].items())[0]
    if bullets:
        items = "".join(f"- {i[key]}\n" for i in items)
    else:
        items = "".join(f"{i[key]}\n\n" for i in items)
    display(Markdown(items))

def mdeducation(items, abbrev=True):
    """Generate markdown syntax for a list of degrees from contents of
    dict `items` as described below. Note that this returns a string of
    code needed to create a table, not a table itself. This is used within a
    Quarto markdown files to display a table when that file is rendered.
    
    ARGUMENTS
    ---------
    items: list of dictionaries each containing the following items:
        {
        'degree': str, the type of degree (e.g., 'Master of Science'),
        'major': str, the name of the degree,
        'institution': str, the name of the institution from which the degree
        was earned,
        'location': str, location of the institution,
        'date': str, the date of degree conferral,
        'gpa': str, earned GPA (e.g., '3.00/4.00'),
        'credits': str, number credit hours earned,
        'minor': str (optional), the name(s) of any minor earned,
        'extra': str (optional), any other relevant information (e.g., award, relevant coursework)
        }
        Normally, this dictionary would be from the YAML front matter of a
        Quarto markdown file.
    abbrev: Boolean, whether or not to always abbreviate degree type. Defaults
        to True.
    """    
    abbr = dict({
        'Bachelor of Science': 'B.S.',
        'Bachelor of Arts': 'B.A.',
        'Master of Science': 'M.S.',
        'Master of Arts': 'M.A.',
        'Doctor of Philosophy': 'Ph.D.'
    })

    for item in items:
        if abbrev:
            display(Markdown(f'**{abbr[item["degree"]]}, {item["major"]}** ({item["credits"]} credit hours) [**{item["date"]}**]{{style="float:right"}}  '))
        else:
            display(Markdown(f'**{item["degree"]}, {item["major"]}** ({item["credits"]} credit hours) [**{item["date"]}**]{{style="float:right"}}  '))
        display(Markdown(f'[GPA {item["gpa"]}]{{style="float:right"}} *{item["institution"]}, {item["location"]}*  '))
        if 'minor' in item.keys():
            display(Markdown(f'Minor in {item["minor"]}  '))
        if 'extra' in item.keys():
            display(Markdown(f'{item["extra"]}'))
        display(Markdown(' '))

def mdexperience(items):
    """Generate markdown syntax for a list of jobs from contents of dict
    `items` as described below. Note that this returns a string of code needed
    to create a table, not a table itself. This is used within a Quarto
    markdown files to display a table when that file is rendered.
    
    ARGUMENTS
    ---------
    items: list of dictionaries each containing the following items:
        {
        'role': str, job title,
        'employer': str, name of employer,
        'date': str, date or date of employment,
        'location': str, location of employment
        'details': str, description of responsibilities. Multiple 
        responsibilities can be entered on separate lines prefaced by an 
        asterisk ('*'), which will render as list.
        'extra': str (optional), any other relevant information
        }
        Normally, this dictionary would be from the YAML front matter of a
        Quarto markdown file.
    """    

    # Remove pdf page breaks
    ind = [i for i,d in enumerate(items) if 'role' not in d.keys()]
    for i in ind:
        items[i-1]['details'] = items[i-1]['details'] + items[i]['details']
    items = [d for i,d in enumerate(items) if i not in ind]

    newitems = items.copy()
    for item in newitems:
        # Add missing elements as placeholders
        for k in ['role', 'employer', 'location', 'date', 'details']:
            if k not in item.keys():
                item[k] = ''

        display(Markdown('|  |  |'))
        display(Markdown('| :--- | ---: |'))
        if 'federal-series' in item:
            if 'extra' in item:
                display(Markdown(f'| **{item["role"]}** ({item["federal-series"]}) <br> *{item["employer"]}, {item["location"]}* <br> {item["extra"]} | **{item["date"]}** <br> *{item["hours-per-week"]} hours per week* |\n'.replace('****', '')))
            else:
                display(Markdown(f'| **{item["role"]}** ({item["federal-series"]}) <br> *{item["employer"]}, {item["location"]}* | **{item["date"]}** <br> *{item["hours-per-week"]} hours per week* |\n'.replace('****', '')))
        else:
            if 'extra' in item:
                display(Markdown(f'| **{item["role"]}** <br> *{item["employer"]}, {item["location"]}* <br> {item["extra"]} | **{item["date"]}** <br> *{item["hours-per-week"]} hours per week* |\n'.replace('****', '')))
            else:
                display(Markdown(f'| **{item["role"]}** <br> *{item["employer"]}, {item["location"]}* | **{item["date"]}** <br> *{item["hours-per-week"]} hours per week* |\n'.replace('****', '')))
        display(Markdown(item["details"]))

def mdlanguages(items):
    """Generate markdown syntax for a list of 
    dict `items` as described below. Note that this returns a string of
    code needed to create a table, not a table itself. This is used within a
    Quarto markdown files to display a table when that file is rendered.
    
    ARGUMENTS
    ---------
    items: list of dictionaries each containing the following items:
        {
        'language': str, the name of the skill to be displayed,
        'spoken-proficiency': str, level of spoken proficiency (usually "none", "novice", "intermediate", or "advanced"),
        'written-proficiency': str, level of writing proficiency (usually "none", "novice", "intermediate", or "advanced"),
        'read-proficiency: str, level of reading proficiency (usually "none", "novice", "intermediate", or "advanced")
        }
        Normally, this dictionary would be from the YAML front matter of a
        Quarto markdown file.
    """
    
    entry = ''.join(f'- **{s["language"]}:** [Speaking: {s["speaking-proficiency"]} | Writing: {s["writing-proficiency"]} | Reading: {s["reading-proficiency"]}]{{style="color: grey"}}\n' for i,s in enumerate(items))

    # De-LaTeXify
    entry = entry.replace('\\', '')

    # Generate table
    display(Markdown(entry))

def mdfreeform(text):
    display(Markdown(text['text']))

def cventry(items):
    """Generates markdown syntax for an html table creating a CV entry with
    date on left and entry description on right. Note that this returns a
    string of code needed to create a table, not a table itself. This is 
    used within a Quarto markdown files to display a table when that file is
    rendered.
    
    ARGUMENTS
    ---------
    items: list of dictionaries containing each of the following:
        {
        'entry': str, description of activity, experience, accomplishment, etc.
        'year': str, year(s) for entry
        }
        Normally, this dictionary would be from the YAML front matter of a
        Quarto markdown file.
    """
    entrykey = [i for i in items[0].keys() if i!='date'][0]
    table_start = '<table class = "mytable">\n<tbody>\n'
    entries = "".join(f"<tr><td class='year'><b>{item['date']}</b></td><td>{item[entrykey]}</td></tr>" for item in items)
    table_end = '</tbody>\n</table>\n'
    
    # Assemble table
    html_table = table_start + entries + table_end
    display(Markdown(html_table))
    
def cvexperience(items):
    """Generate markdown syntax for a CV list of jobs from contents of dict
    `items` as described below. Note that this returns a string of code needed
    to create a table, not a table itself. This is used within a Quarto
    markdown files to display a table when that file is rendered.
    
    ARGUMENTS
    ---------
    items: list of dictionaries, each containing the following items:
        {
        'role': str, job title,
        'employer': str, name of employer,
        'date': str, date or date range of employment,
        'location': str, location of employment
        'extra': str (optional), any other relevant information
        }
        Normally, this dictionary would be from the YAML front matter of a
        Quarto markdown file.
    """
    
    # Remove pdf page breaks
    ind = [i for i,d in enumerate(items) if 'role' not in d.keys()]
    for i in ind:
        items[i-1]['details'] = items[i-1]['details'] + items[i]['details']
    items = [d for i,d in enumerate(items) if i not in ind]

    table_start = '<table class = "mytable">\n<tbody>\n'
    entries = ""
    for item in items:
        if 'location' not in item.keys() and 'extra' not in item.keys():
            entries += f"<tr><td class='year'><b>{item['date']}</b></td><td><b>{item['role']}</b><br>{item['employer']}</td></tr>"
        elif 'location' not in item.keys():
            entries += f"<tr><td class='year'><b>{item['date']}</b></td><td><b>{item['role']}</b> | {item['extra']}<br>{item['employer']}</td></tr>"
        elif 'extra' not in item.keys():
            entries += f"<tr><td class='year'><b>{item['date']}</b></td><td><b>{item['role']}</b><br>{item['employer']}, {item['location']}</td></tr>"
        else:
            entries += f"<tr><td class='year'><b>{item['date']}</b></td><td><b>{item['role']}</b> | {item['extra']}<br>{item['employer']}, {item['location']}</td></tr>"
    table_end = '</tbody>\n</table>\n'
    
    # Assemble table
    html_table = table_start + entries + table_end
    display(Markdown(html_table))

def cveducation(items, abbrev=True):
    """Generate html syntax for a CV list of degrees from contents of dict
    `items` as described below. Note that this returns a string of code needed
    to create a table, not a table itself. This is used within a Quarto
    markdown files to display a table when that file is rendered.
    
    ARGUMENTS
    ---------
    items: list of dictionaries, each containing the following items:
        {
        'degree': str, the type of degree (e.g., 'Master of Science'),
        'major': str, the name of the degree,
        'institution': str, the name of the institution from which the degree
        was earned,
        'location': str, location of the institution,
        'date': str, the date of degree conferral,
        'gpa': str, earned GPA (e.g., '3.00/4.00'),
        'credits': str, number credit hours earned,
        'minor': str (optional), the name(s) of any minor earned,
        'extra': str (optional), any other relevant information (e.g., award, relevant coursework)
        }
        Normally, this dictionary would be from the YAML front matter of a
        Quarto markdown file.
    abbrev: Boolean, whether or not to always abbreviate degree type. Defaults
        to True.
    """    
    abbr = dict({
        'Bachelor of Science': 'B.S.',
        'Bachelor of Arts': 'B.A.',
        'Master of Science': 'M.S.',
        'Master of Arts': 'M.A.',
        'Doctor of Philosophy': 'Ph.D.'
    })
    if abbrev:
        for item in items:
            item['degree'] = abbr[item['degree']]

    table_start = '<table class = "mytable">\n<tbody>\n'
    entries = ""
    for item in items:
        if 'minor' in item.keys():
            if 'extra' in item.keys():
                entries += f"<tr><td class='year'><b>{item['date']}</b></td><td><b>{item['degree']}</b>, {item['major']}, {item['institution']}, {item['location']}<br>Minor: {item['minor']} | *{item['extra']}*</td></tr>"            
            else:
                entries += f"<tr><td class='year'><b>{item['date']}</b></td><td><b>{item['degree']}</b>, {item['major']}, {item['institution']}, {item['location']}<br>Minor: {item['minor']}</td></tr>"
        elif 'extra' in item.keys():
            if 'minor' in item.keys():
                entries += f"<tr><td class='year'><b>{item['date']}</b></td><td><b>{item['degree']}</b>, {item['major']}, {item['institution']}, {item['location']}<br>Minor: {item['minor']} | *{item['extra']}*</td></tr>"
            else:
                entries += f"<tr><td class='year'><b>{item['date']}</b></td><td><b>{item['degree']}</b>, {item['major']}, {item['institution']}, {item['location']}<br>*{item['extra']}*</td></tr>"                
        else:
            entries += f"<tr><td class='year'><b>{item['date']}</b></td><td><b>{item['degree']}</b>, {item['major']}, {item['institution']}, {item['location']}</td></tr>"
    table_end = '</tbody>\n</table>\n'
    
    # Assemble table
    html_table = table_start + entries + table_end
    display(Markdown(html_table))
