# resume-quarto-moderncv

## Professional r&#232;sum&#232; and academic curriculum vit&aelig; easily generated in `pdf`, `html`, and `docx` formats

### Overview
This template can be used to easily create a professional private sector r&#232;sum&#232; and/or an academic curriculum vit&aelig; (CV) in `pdf`, `html`, and `docx` formats using [Quarto](https://quarto.org/) and [Python](https://www.python.org/):

* [Quarto](https://quarto.org/docs/get-started/) (>= 1.6.42)
* [Python](https://www.python.org/downloads/) (>= 3.9.6)

The `pdf` version is a custom and limited Quarto implementation of the LaTeX [moderncv](https://ctan.org/pkg/moderncv) template. The implementation is inspired by and derived from the [modern2-cv](https://github.com/schochastics/modern2-cv) Quarto template by [schochastics](https://github.com/schochastics).

The `html` rendering supports integration with a portfolio website. It is based upon [this quarto-resume](https://github.com/busemorose/resume_quarto) by [busemorose](https://github.com/busemorose), but uses Python instead of R to format the content, mostly due to seemingly endless challenges installing R's flextable package.

Credit and kudos to both authors, as well as all upstream template authors, none of whom I know personally. Thank you for your contributions to [open science](https://en.wikipedia.org/wiki/Open_science). This template serves to pay it forward.

The `docx` version is intended to provide a quick and easy way to populate a Microsoft Word document with the same content for occasions when this file format is needed. While the `pdf` and `html` versions are properly and similarly formatted, the `docx` version requires considerable manual intervention after the file is created.

R&egrave;sum&egrave; and CV content are entered in `_contents.yml`. Layout and formatting customizations can be made in `resume.qmd` and `cv.qmd`. Instructions are provided below.

### Previews

|       | R&egrave;sum&egrave;           | Curriculum vit&aelig; (CV)    |
|:-----:| :----------------------------: | :---------------------------: |
| **PDF**  | ![PDF r&#232;sum&#232;](images/resume-pdf-preview.jpg) | ![PDF CV](images/cv-pdf-preview.jpg) |
| **HTML** | ![HTML r&#232;sum&#232;](images/resume-html-preview.jpg) | ![HTML CV](images/cv-html-preview.jpg) |

### Creating a R&egrave;sum&egrave; and CV

R&egrave;sum&egrave; and CV content are provided in YAML format in `_content.yml`. Most (but not all) of the variables are used in both the r&egrave;sum&egrave; and CV, thereby streamlining the process of making two separate but related documents. All are described below. All entries are strings unless otherwise noted.

All content variables (*e.g.*, education) contain `include-in-resume` and/or `include-in-cv` Boolean variables that, when `true`, will include that section in the r&egrave;sum&egrave; and/or CV, respectively. If `false` or omitted altogether, the section will not show up in either document. This makes it easy to keep the contents of both documents separate, if desired. Some fields, like funding procurement, can currently only be included in the CV, since this type of information is rarely (if ever) included in traditional r&egrave;sum&egrave;s. They also include header variables --- `resume-header` and/or `cv-header` --- to change the default section headers in all versions of the r&egrave;sum&egrave; and CV documents simultaneously.

#### Header Information

Header information appears in the banner at the top of the `html` rendering. These include the standard Quarto `title` and `subtitle` top-level YAML arguments:

| Keyword       | Description                                   |
| :------------ | :-------------------------------------------- |
| `title`       | Your full name  for website header            |
| `subtitle`    | Occupation or job title                       |

For example:

```{.yaml filename="_contents.yml"}
---
title: "John Doe"
subtitle: "Underwater Basket Weaver"
---
```

The name displayed at the top of the `pdf` and `docx` files are passed to `author` via second-level `firstname`, `lastname`, and optional `suffix` arguments:

| Keyword       | Description                                   |
| :------------ | :-------------------------------------------- |
| `firstname`   | Your first name for `pdf` and `docx` files    |
| `lastname`    | Your last name for `pdf` and `docx` files     |
| `suffix`      | Optional suffix to follow the name            |

For example:

```yaml
author:
  firstname: "John"
  lastname: "Doe"
  suffix: "Jr."
```

Note that your name needs to be provided twice in `_contents.yml`: to `title` (for `html` and `docx` rendering) and to `author` (for `pdf`), in order for all documents to display properly.

#### Contact Information

Contact information for the top of the r&egrave;sum&egrave; and CV are passed to the top level `content` key, as in `author` above:

| Keyword       | Description                                   |
| :------------ | :-------------------------------------------- |
| `phone`       | Phone number                                  |
| `email`       | Email address. Will generate a "mailto" call if formatted properly as an email address (with an "@" symbol)               |
| `website`     | URL to personal or professional website       |
| `github`      | Your [GitHub](https://github.com) username only. Will generate the custom web URL directing to this user's dashboard. |
| `linkedin`    | Your [LinkedIn](https://www.linkedin.com/) handle only. Will generate the custom web URL directing to this user's public page. |
| `orcid`       | Your [ORCID](https://orcid.org/) number only.  Will generate the custom web URL directing to this user's public page.|
| `researchgate` | Your [ResearchGate](https://www.researchgate.net/) handle only.  Will generate the custom web URL directing to this user's public page. |
| `extrainfo`   | Any other information to include at the top of the r&egrave;sum&egrave; and CV? |

A physical or mailing address can also be passed to the `contact` key. It is separated into `line1` and `line2` keys:

```yaml
contact:
  address:
    line1: "123 Waterman Lane"
    line2: "Anylocation, US"
```

Putting it all together so far:

```yaml
---
title: "John Doe, Jr."
subtitle: "Underwater Basket Weaver"
author:
  firstname: "John"
  lastname: "Doe"
  suffix: "Jr."
contact:
  address: 
    line1: "123 Waterman Lane"
    line2: "Anylocation, US"
  phone: "555-123-4321"
  email: "emailaddress"
  website: "personalwebsiteurl"
  github: "GithubUsername"
  linkedin: "linkedInUrlHandle"
  orcid: "orcid"
  researchgate: "ResearchGateUrlHandle"
  extrainfo: "Anything else to highlight up front?"
---
```

#### Summary

An optional professional summary for the r&egrave;sum&egrave; can be passed to the top level `summary` key, if desired. This is usually a paragraph-like executive summary of the r&egrave;sum&egrave; itself or used to highlight or emphasize key knowledge, skills, and abilities. Omit if not desired.

The summary does not appear in the CV.

#### Education

**Note: This section, and all of the following sections, are optional. Omitting the section from `_contents.yml` will prevent it from appearing in the rendered documents.**

Education (*i.e.*, degrees earned) is provided to the `education` category as a list of `items` with the following elements:

| Keyword       | Description                                   |
| :------------ | :-------------------------------------------- |
| `degree`      | Type of degree (*e.g.*, B.S., Master's of Science, *etc.*) |
| `major`       | Primary field or area of study of the degree  |
| `institution` | Name of the degree-granting institution       |
| `location`    | Location of the institution                   |
| `date`        | Date of degree conferral                      |
| `minor`       | Minor or secondary area(s) of study (optional) |
| `extra`       | Any additional information (*e.g.*, awards) (optional) |

In addition, the `education` category also takes Boolean control flags specifying which document to include as well as header variables to set section headers:

| Keyword             | Description                                        |
| :------------------ | :------------------------------------------------- |
| `include-in-resume` | (Boolean) If `true`, this section will appear in the r&egrave;sum&egrave;. If `false` or omitted altogether, it will be excluded. |
| `include-in-cv`     | (Boolean) If `true`, this section will appear in the CV. If `false` or omitted altogether, it will be excluded. |
| `resume-header`     | Section header text as it should appear in the r&egrave;sum&egrave; |
| `cv-header`         | Section header text as it should appear in the CV  |

For example:

```yaml
education:
  include-in-resume: true
  include-in-cv: true
  resume-header: "Education"
  cv-header: "Education"
  items:
    - degree: "Bachelor of Arts"
      major: "Underwater Basket Weaving"
      institution: "University of Awesomeness"
      location: "Anylocation, US"
      date: "2000"
      minor: "SCUBA Diving"
      extra: "Graduated top of my class of 1"
    - degree: "Master of Arts"
      major: "Upside Down Underwater Basket Weaving"
      institution: "University of Awesomeness"
      location: "Anylocation, US"
      date: "2002"
```

##### Additional Education

There is also an option to add additional education to a CV displayed in a more succinct format. This could be used to highlight continuing education or incomplete degrees. Use the `additional-education` key with a list of `items` containing of the following elements, as above:

| Keyword       | Description                                   |
| :------------ | :-------------------------------------------- |
| `major`       | Primary field or area of study                |
| `institution` | Name of the academic institution              |
| `location`    | Location of the institution                   |
| `date`        | Date(s) of study                              |
| `extra`       | Any additional information (optional)         |

This section also supports the following:

| Keyword             | Description                                        |
| :------------------ | :------------------------------------------------- |
| `include-in-resume` | (Boolean) If `true`, this section will appear in the r&egrave;sum&egrave;. If `false` or omitted altogether, it will be excluded. |
| `resume-header`     | Section header text as it should appear in the r&egrave;sum&egrave; (unused for now, as this section is not currently supported in r&egrave;sum&egrave;s) |
| `cv-header`         | Section header text as it should appear in the CV |

#### Skills

Technical skills are included in r&egrave;sum&egrave;s only. They are displayed as a simple bulleted list for `html` and `docx` and as a table with status bar-like visualizations of overall competence in `pdf` rendering. They are provided as a list of `items`, as in `education` above, with the following entries:

| Keyword       | Description                                   |
| :------------ | :-------------------------------------------- |
| `skill`       | Name of the skill                             |
| `years`       | Number of years of experience                 |
| `scale`       | (string) Value between 0 and 1 quantifying the amount of experience or level of expertise. Should be relative to `years`. For example, the skill with the maximum number of years of experience should have `scale` = 1. |

The `skills` section also takes four additional arguments:

| Keyword       | Description                                   |
| :------------ | :-------------------------------------------- |
| `include-in-resume` | (Boolean) If `true`, this section will be included in the r&egrave;sum&egrave;. If `false` or omitted, it will be excluded. |
| `resume-header`     | Section header text as it should appear in the r&egrave;sum&egrave; |
| `ncol`        | Integer specifying the number of columns for the skills list |
| `softskills`  | Additional soft (*i.e.*, non-technical) skills passed as a single string of comma-separated skills (optional) |

#### Experience

Professional experience is passed as a list of `items`, as in `education` above, with the following entries:

| Keyword       | Description                                   |
| :------------ | :-------------------------------------------- |
| `role`        | Job or position title                         |
| `employer`    | Name of employer                              |
| `location`    | Location of employer                          |
| `date`        | Date(s) of employment                         |
| `details`     | Description of job duties or accomplishments. This must be a single string, but asterisks (*) will be treated as bullets and will create a list when rendered. See example below. |
| `extra`       | Any additional information to include (optional) |

In addition, the `experience` category also takes Boolean control flags specifying which document to include as well as header variables to set section headers:

| Keyword             | Description                                        |
| :------------------ | :------------------------------------------------- |
| `include-in-resume` | (Boolean) If `true`, this section will appear in the r&egrave;sum&egrave;. If `false` or omitted altogether, it will be excluded. |
| `include-in-cv`     | (Boolean) If `true`, this section will appear in the CV. If `false` or omitted altogether, it will be excluded. |
| `resume-header`     | Section header text as it should appear in the r&egrave;sum&egrave; |
| `cv-header`         | Section header text as it should appear in the CV  |

For example:

```yaml
experience:
  include-in-resume: true
  include-in-cv: true
  resume-header: "Experience"
  cv-header: "Professional Experience"
  items:
    - role: "Senior Basket Weaver III"
      employer: "Underwater Basket Weavers of America"
      location: "Pacific Ocean"
      extra: "2022 Employee of the Year"
      date: "Jan 2010--present"
      details: |
        * Design unique and custom baskets according to customers' needs
        * Assemble ~100 made-to-order baskets underwater each year, with 105% 5-star ratings on our customer feedback portal.
```

#### Research

The optional research category is only used in CVs. Research activities are passed as a list of `items`, as in `education` above, with the following keywords:

| Keyword       | Description                                   |
| :------------ | :-------------------------------------------- |
| `entry`       | Description of research activity              |
| `date`        | Date(s) of research activity                  |

In addition, the `research` category also takes Boolean control flags specifying which document to include as well as header variables to set section headers:

| Keyword             | Description                                        |
| :------------------ | :------------------------------------------------- |
| `include-in-resume` | (Boolean) If `true`, this section will appear in the r&egrave;sum&egrave;. If `false` or omitted altogether, it will be excluded. |
| `include-in-cv`     | (Boolean) If `true`, this section will appear in the CV. If `false` or omitted altogether, it will be excluded. |
| `resume-header`     | Section header text as it should appear in the r&egrave;sum&egrave; |
| `cv-header`         | Section header text as it should appear in the CV  |

For example:

```yaml
research:
  include-in-resume: false
  include-in-cv: true
  resume-header: "Research Experience"
  cv-header: "Research"
  items:
    - entry: "Developing eco-friendly baskets in underwater environments: combatting biodegradation when weaving baskets underwater"
      date: "2029-2023"
```

#### Awards

Awards are passed as a list of `items` with keyword `award`. In addition, the `awards` category also takes Boolean control flags specifying which document to include as well as header variables to set section headers:

| Keyword             | Description                                        |
| :------------------ | :------------------------------------------------- |
| `include-in-resume` | (Boolean) If `true`, this section will appear in the r&egrave;sum&egrave;. If `false` or omitted altogether, it will be excluded. |
| `include-in-cv`     | (Boolean) If `true`, this section will appear in the CV. If `false` or omitted altogether, it will be excluded. |
| `resume-header`     | Section header text as it should appear in the r&egrave;sum&egrave; |
| `cv-header`         | Section header text as it should appear in the CV  |

#### Funding Awards

The `fundingawarded` category is currently used only in CVs to list grants or other competitive funding. Provide as a list of `items` with keywords `entry` and `date`, as in `research` above. As above, `include-in-cv` must be `true` for this section to appear and the section header can be set with `cv-header`.

#### Publications

Four categories of `publications` are supported: `peer-reviewed` for peer-reviewed publications such as journal articles; `proceedings` for conference proceedings; `tech-reports` for non-peer reviewed technical reports; and `talks` for presentations, posters, or contributed abstracts. All categories are passed as lists of `items` with keyword `paper`. Subsection headers can also be set for each sub-category. For example:

```yaml
publications:
  peer-reviewed:
    resume-subheader: "Peer Reviewed"
    cv-subheader: "Peer Reviewed"
    items:
      - paper: "Paper 1"
      - paper: "Paper 2"
      - paper: "Paper 3"
```

In addition, the `publications` category also takes Boolean control flags specifying which document to include in as well as header variables to set the section headers:

| Keyword             | Description                                        |
| :------------------ | :------------------------------------------------- |
| `include-in-resume` | (Boolean) If `true`, this section will appear in the r&egrave;sum&egrave;. If `false` or omitted altogether, it will be excluded. |
| `include-in-cv`     | (Boolean) If `true`, this section will appear in the CV. If `false` or omitted altogether, it will be excluded. |
| `resume-header`     | Section header text as it should appear in the r&egrave;sum&egrave; |
| `cv-header`         | Section header text as it should appear in the CV  |

Note that these flags are passed to the top level `publications`. The first two flags control the inclusion of the entire publications section in the documents. The categories cannot currently be controlled individually without omitting data from `_contents.yml`. It is currently all or or nothing.

#### Memberships

Professional memberships can be listed under the `membership` category as a list of `items` with key `entry`, as in `fundingawarded` above. This category is currently only supported in CVs. Also supports `include-in-cv` and `cv-header` arguments, as above.

#### Teaching

Teaching experience can be provided to the `teaching` category as a list of `items` with the following elements:

| Keyword       | Description                                   |
| :------------ | :-------------------------------------------- |
| `role`        | Role title or description                     |
| `course`      | Name of class or course taught                |
| `institution` | Name of the degree-granting institution       |
| `date`        | Date(s) of teaching work                      |
| `extra`       | Any additional information (*e.g.*, awards) (optional) |

In addition, the `teaching` category also takes Boolean control flags specifying which document to include as well as header variables to set section headers:

| Keyword             | Description                                        |
| :------------------ | :------------------------------------------------- |
| `include-in-cv`     | (Boolean) If `true`, this section will appear in the CV. If `false` or omitted altogether, it will be excluded. |
| `cv-header`         | Section header text as it should appear in the CV  |

For example:

```yaml
teaching:
  include-in-cv: true
  cv-header: Teaching
  items:
    - date: 2019
      role: Student Teacher
      course: "ART 101: Introduction to Basketry"
      institution: University of Awesomeness
      extra: "'Twas a great class'"
```

Note that `teaching` is currently only supported in CVs.

#### Service

The `service` category can be used to capture community service, outreach, or other related activities. Entries are passed as a list of `items` with the following elements:

| Keyword       | Description                                   |
| :------------ | :-------------------------------------------- |
| `activity`    | Description of activity                       |
| `institution` | Name of the degree-granting institution       |
| `date`        | Date(s) of teaching work                      |

This `service` category is currently only supported in CVs. Its header can be set with `cv-header` and its inclusion controlled with `include-in-cv`.

#### Media

Media publicity can be listed under the `media` category as a list of `items` with key `entry`, as in `membership` above. This category is currently only supported in CVs. Also supports `include-in-cv` and `cv-header` arguments, as above.

#### Certifications

Relevant certifications can be listed under the `certifications` category as a list of `items` with key `entry`, as in `membership` above. This category is currently only supported in CVs. Also supports `include-in-cv` and `cv-header` arguments, as above.

#### Miscellaneous

The r&egrave;sum&egrave; and CV file names are passed to `resumefilename` and `cvfilename`, respectively (do not include a file extension.) These are used to create hyperlinks to the `pdf` and `docx` files:

```yaml
resumefilename: "my-resume"
cvfilename: "my-cv"
```

Page numbers can also be toggled on and off in each document by setting `resume-page-numbers` and `cv-page-numbers` to either `true` or `false`.

### Customization

#### Rendering `html` and `docx`

R&egrave;sum&egrave; and CV renderings can be customized further in `resume.qmd` and `cv.qmd` Quarto markdown files, respectively. The most important elements to modify are the `output-file` arguments in the front matter under `resume-pdf` and `docx` in `resume.qmd` to specify the name of the r&egrave;sum&egrave; file produced, and under `cv-pdf` and `docx` in `cv.qmd` to specify the name of the CV file to be produced.

The body of these markdown files controls the `html` and `docx` renderings. One may wish to rearrange or add new sections in either document. In addition, any social or web media omitted from the `contact` section in `_contents.yml` should be removed or commented out in these files to prevent errors during rendering if `html` and/or `docx` renderings are desired. The current version of this template does not handle these entries conditionally.

These renderings are constructed using Python functions found in `scripts/moderncv.py`. All functions process subsets of `_contents.yml` passed to an `items` keyword. (Python loads the contents of YAML files as nested dictionaries and lists.) For example, multiple entries under the `skills` category in `_contents.yml` would create a list of dictionaries, one dictionary per skill, which would look like this:

```{.python filename="Sample Python function"}
with open("_contents.yml", "r") as f:
  contents = yaml.safe_load(f)

print(contents["skills"]["items"])

[{
    "skill": "Basket weaving",
    "years": "20+ yrs.",
    "scale": "1"
},
{
    "skill": "SCUBA",
    "years": "15+ yrs.",
    "scale": "0.7" 
},...]
```

Some functions take additional arguments; these are summarized here but consult the respective docstring for more information.

| Function      | Arguments                 | Usage             |
| :------------ | :------------------------ | :-----------------|
| `mdlist`      | `items`: as described above <br> `bullets`: whether or not to include bullets in the list | Create a simple list of entries. Used for Awards and Publications. |
| `mdskills`    | `items`: as described above <br> `ncols`: number of columns for the skills table <br> `icons`: whether skills should be prefaced by an appropriate icon, if one is available for that skill (displayed in `html` rendering only) | Display skills in a r&egrave;sum&egrave;, either as a table (`pdf`) or a bulleted list (`html` and `docx`) |
| `mdeducation` | `items`: as described above <br> `abbrev`: whether or not to always abbreviate degree type | Create a formatted list of degrees for a r&egrave;sum&egrave; |
| `mdexperience`| `items`: as described above | Create a formatted list of professional experiences for a r&egrave;sum&egrave; |
| `cventry`     | `items`: as described above | Create a list of CV entries prefaced by the date. Used for Research and Funding categories. |
| `cvexperience` | `items`: as described above | Create a list of professional experiences prefaced by the date for a CV |
| `cveducation` | `items`: as described above | Create a list of educational degrees prefaced by the date for a CV |
| `cvaddedu`    | `items`: as described above | Create a list of additional educational undertakings prefaced by the date for a CV |
| `cvteaching`  | `items`: as described above | Create a list of teaching experience prefaced by the date for a CV |
| `cvservice`   | `items`: as described above | Create a list of service, outreach, *etc.* prefaced by the date for a CV |

#### Rendering `pdf`

Customizing the `pdf` renderings is somewhat more involved, as it requires knowledge of LaTeX in addition to the Markdown described above. The `pdf` r&egrave;sum&egrave; and CV renderings are templated in `_extensions/schochastics/resume/resumetemplate.tex` and `_extensions/schochastics/cv/cvtemplate.tex`, respectively. Sections can be added or rearranged in these files, as well as other more advanced customizations, if one knows what one is doing in LaTeX. The advanced user may also find the LaTeX ["moderncv" package documentation](https://ctan.math.washington.edu/tex-archive/macros/latex/contrib/moderncv/manual/moderncv_userguide.pdf) helpful.

### Advanced

As with all Quarto projects, additional modifications can be made in `_quarto.qmd`. This is only needed if one does not like the existing layout or functionality. Generally, this file does not need to be modified.

In addition, a `_website.yml` file is included in case one wishes to convert the `html` rendering into a stand-alone website. Add this file to the `metadata-files` list in the front matter of `resume.qmd` and/or `cv.qmd` to add navigation bars on the top and left side as well as a footer at the bottom of each page.

### Usage

This repository is configured to publish the `html` renderings to GitHub Pages. This is updated automatically when changes are committed or pushed. The r&egrave;sum&egrave; and CV can be accessed from the landing page and linked to directly from other sites, if desired. Corresponding `pdf` and `docx` files can be downloaded from the `html` page.