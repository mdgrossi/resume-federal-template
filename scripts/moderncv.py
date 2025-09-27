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

def mdskills(items, ncol=2, icons=True):
    """Generate markdown syntax for a list with `ncol` columns from contents of 
    dict `items` as described below. Note that this returns a string of
    code needed to create a table, not a table itself. This is used within a
    Quarto markdown files to display a table when that file is rendered.
    
    ARGUMENTS
    ---------
    items: list of dictionaries each containing the following items:
        {
        'skill': str, the name of the skill to be displayed,
        'years': str, the number of years of experience to be displayed,
        'scale': int, a value from 1-10 indicating the degree of experience or
        expertise for the given skill.
        }
        Normally, this dictionary would be from the YAML front matter of a
        Quarto markdown file.
    ncols: int, the number of columns the skills table should be arranged in
    icons: Bool, if True, each skill will be prefaced by an appropriate icon,
        if one is available for that skill (icons display in html rendering
        only). Defaults to True.
    """
    
    # Column configuration
    nskills = len(items)
    perrow = nskills//ncol
    
    # Include skill icons, if desired
    if icons:
        icon_dict = dict({
            'Data Analysis': '{{< iconify icon-park analysis >}}',
            'Data Science': '{{< iconify devicon plotly >}}',
            'Data Governance': '{{< iconify fluent data-usage-sparkle-20-filled >}}',
            'Python': '{{< iconify devicon python >}}',
            'R': '{{< iconify devicon rstudio >}}',
            'Cloud (AWS, GCP)': '{{< iconify ri cloud-fill >}}',
            'Machine Learning': '{{< iconify carbon machine-learning-model >}}',
            'Git': '{{< iconify mdi github >}}',
            'Docker': '{{< iconify skill-icons docker >}}',
            '\\LaTeX': '{{< iconify skill-icons latex-dark >}}',
            'Jupyter': '{{< iconify logos jupyter >}}',
            'Quarto': '{{< iconify simple-icons quarto >}}'
        })

        col1 = ''.join(f'- {icon_dict[s["skill"]]} **{s["skill"]}** [({s["years"]})]{{style="color: grey"}}\n' for i,s in enumerate(items) if i < perrow)
        col2 = ''.join(f'- {icon_dict[s["skill"]]} **{s["skill"]}** [({s["years"]})]{{style="color: grey"}}\n' for i,s in enumerate(items) if i >= perrow)
    
    else:
        
        col1 = ''.join(f'- **{s["skill"]}** [({s["years"]})]{{style="color: grey"}}\n' for i,s in enumerate(items) if i < perrow)
        col2 = ''.join(f'- **{s["skill"]}** [({s["years"]})]{{style="color: grey"}}\n' for i,s in enumerate(items) if i >= perrow)

    # De-LaTeXify
    col1 = col1.replace('\\', '')
    col2 = col2.replace('\\', '')

    # Generate table
    display(Markdown(':::: {.columns layout-ncols="2"}'))
    display(Markdown(':::{.column}'))    
    display(Markdown(col1))
    display(Markdown(':::'))
    display(Markdown(':::{.column}'))
    display(Markdown(col2))
    display(Markdown(':::'))
    display(Markdown('::::'))

def mdeducation(items, abbrev=True):
    """Generate markdown syntax for a list of degrees from contents of
    dict `items` as described below. Note that this returns a string of
    code needed to create a table, not a table itself. This is used within a
    Quarto markdown files to display a table when that file is rendered.
    
    ARGUMENTS
    ---------
    items: list of dictionaries each containing the following items:
        {
        'degree': str, the type of degree (e.g., 'B.A.', 'Master of Science'),
        'major': str, the name of the degree,
        'institution': str, the name of the institution from which the degree
        was earned,
        'location': str, location of the institution,
        'date': str, the date of degree conferral,
        'minor': str (optional), the name(s) of any minor earned,
        'extra': str (optional), any other relevant information (e.g., award)
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
            display(Markdown(f'**{abbr[item["degree"]]}, {item["major"]}**  '))
        else:
            display(Markdown(f'**{item["degree"]}, {item["major"]}**  '))
        if 'extra' in item.keys():
            display(Markdown(f'*{item["institution"]}, {item["location"]}* ({item["extra"]})  '))
        else:
            display(Markdown(f'*{item["institution"]}, {item["location"]}*  '))
        if 'minor' in item.keys():
          display(Markdown(f'Minor in {item["minor"]}  '))
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
        if item['employer'] == '' and item['location'] == '':
            if 'extra' in item.keys():
                display(Markdown(f'| *{item["role"]}, {item["extra"]}* | *{item["date"]}* |\n'.replace('****', '')))
            else:
                display(Markdown(f'| *{item["role"]}* | *{item["date"]}* |\n'.replace('****', '')))    
        else:
            if 'extra' in item.keys():
                display(Markdown(f'| **{item["employer"]}** <br> *{item["role"]}, {item["extra"]}* | **{item["location"]}** <br> *{item["date"]}* |\n'.replace('****', '')))
            else:
                display(Markdown(f'| **{item["employer"]}** <br> *{item["role"]}* | **{item["location"]}** <br> *{item["date"]}* |\n'.replace('****', '')))
        display(Markdown(item["details"]))

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
        'degree': str, the type of degree (e.g., 'B.A.', 'Master of Science'),
        'major': str, the name of the degree,
        'institution': str, the name of the institution from which the degree
        was earned,
        'location': str, location of the institution,
        'date': str, the date of degree conferral,
        'minor': str (optional), the name(s) of any minor earned,
        'extra': str (optional), any other relevant information (e.g., award)
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

def cvaddedu(items):
    """Generate markdown syntax for a CV list of additional education from 
    contents of dict `items` as described below. Note that this returns a 
    string of code needed to create a table, not a table itself. This is used
    within a Quarto markdown files to display a table when that file is
    rendered.
    
    ARGUMENTS
    ---------
    items: list of dictionaries, each containing the following items:
        {
        'major': str, the name of the degree,
        'institution': str, the name of the institution from which the degree
        was earned,
        'location': str, location of the institution,
        'date': str, the date of degree conferral,
        'extra': str (optional), any other relevant information (e.g., award)
        }
        Normally, this dictionary would be from the YAML front matter of a
        Quarto markdown file.
    """
    
    table_start = '<table class = "mytable">\n<tbody>\n'
    entries = ""
    for item in items:
        entries += f"<tr><td class='year'><b>{item['date']}</b></td><td>{item['major']} (<i>{item['extra']}</i>), {item['institution']}, {item['location']}</td></tr>"
    table_end = '</tbody>\n</table>\n'
    
    # Assemble table
    html_table = table_start + entries + table_end
    display(Markdown(html_table))


def cvteaching(items):
    """Generate markdown syntax for a CV list of teaching experience from 
    contents of dict `items` as described below. Note that this returns a 
    string of code needed to create a table, not a table itself. This is used
    within a Quarto markdown files to display a table when that file is
    rendered.
    
    ARGUMENTS
    ---------
    items: list of dictionaries, each containing the following items:
        {
        'role': str, duty title,
        'course': str, name of course or class,
        'date': str, date(s) of course,
        'institution': str, name of academic institution,
        'extra': str (optional), any other relevant information
        }
        Normally, this dictionary would be from the YAML front matter of a
        Quarto markdown file.
    """
    
    table_start = '<table class = "mytable">\n<tbody>\n'
    entries = ""
    for item in items:
        if 'extra' not in item.keys():
            entries += f"<tr><td class='year'><b>{item['date']}</b></td><td>{item['role']}, {item['course']}, {item['institution']}</td></tr>"
        else:
            entries += f"<tr><td class='year'><b>{item['date']}</b></td><td>{item['role']}, {item['course']} ({item['extra']}), {item['institution']}</td></tr>"
    table_end = '</tbody>\n</table>\n'
    
    # Assemble table
    html_table = table_start + entries + table_end
    display(Markdown(html_table))

def cvservice(items):
    """Generate markdown syntax for a CV list of service activities from 
    contents of dict `items` as described below. Note that this returns a 
    string of code needed to create a table, not a table itself. This is used
    within a Quarto markdown files to display a table when that file is
    rendered.
    
    ARGUMENTS
    ---------
    items: list of dictionaries, each containing the following items:
        {
        'activity': str, description of service activity,
        'date': str, date(s) of course,
        'institution': str, name of academic institution,
        'extra': str (optional), any other relevant information
        }
        Normally, this dictionary would be from the YAML front matter of a
        Quarto markdown file.
    """
    
    table_start = '<table class = "mytable">\n<tbody>\n'
    entries = ""
    for item in items:
        if 'extra' not in item.keys():
            entries += f"<tr><td class='year'><b>{item['date']}</b></td><td>{item['activity']}, {item['institution']}</td></tr>"
        else:
            entries += f"<tr><td class='year'><b>{item['date']}</b></td><td>{item['activity']} (<i>{item['extra']}</i>), {item['institution']}</td></tr>"
    table_end = '</tbody>\n</table>\n'
    
    # Assemble table
    html_table = table_start + entries + table_end
    display(Markdown(html_table))
