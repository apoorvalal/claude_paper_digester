pgp_prompt = """

We are going to create a two-page reader's digest summary of the attached paper. The goal of this summary is:
1. What the reserachers do, in language that is not too dense but sufficiently mathematically precise, and is clear to Ph.D. level economists.
2. Why does the literature care about this? Why is it a contribution and why where does it fit?
3. What is a key figure or theorem from the paper?

The headline paragraph of the summary should state "what is the one thing to learn from this paper?".
Your output should be in markdown.

"""


# h/t CJ Libassi (https://bsky.app/profile/clibassi.bsky.social/post/3lbufgd23sc2n)
big_prompt = """
Analyze the attached academic paper PDF and provide a comprehensive review. Format your response in a code-block artifact using the following Obsidian-compatible markdown structure that is in a codeblock that can be copied to my Obsidian session:

```markdown

# [Standardized Title]


## File Name

[Provide a standardized file name here following the format: AuthorLastNames_ShortTitle_Year.pdf]


## Paper Title

[Full title of the paper]


## Basic Information

- Authors: [Full names of all authors]

- Year: [Year of publication]

- Journal: [Journal or Working Paper Series Name]

- Field: [Main field of study]

- Subfield: [Specific subfield or area of focus]

- Study type: [Empirical, theoretical, descriptive, or causal]


## Objective and Contribution (100-150 words)

[Clearly state:

1. The main research question(s) or hypothesis of the paper

2. The key contribution to the existing literature

3. How this work relates to and builds upon previous research in the field

4. Any novel approaches or perspectives introduced by the authors]


## Methodology (200-300 words)

[Provide a detailed overview of the study's methodology, including:

1. Theoretical framework or model used (if applicable)

2. Data sources and key variables

3. Sample size and characteristics (if applicable)

4. Empirical strategy or experimental design

5. Statistical methods or analytical techniques employed

6. Key assumptions made by the authors and their plausibility

7. Any limitations or potential biases in the chosen methodology as implemented]


## Sample and Setting (150-200 words)

[Provide a detailed description of the study's sample and setting, including:

1. Sample definition: How the sample was selected or constructed (note any key exclusion criteria)

2. Sample size: Total number of observations, units, or participants

3. Time period: Years covered by the data or study

4. Geographic scope: Countries, regions, or specific locations involved

5. Unit of analysis: Individual, household, firm, country, etc.

6. Inclusion/exclusion criteria: Any specific requirements for inclusion in the sample

7. Data frequency: Cross-sectional, panel, or time series nature of the data

8. Response rates: For survey data, if applicable

9. Attrition: For longitudinal studies, if applicable


## Main Findings (200-300 words)

[Summarize the principal results of the study:

1. Key findings and their statistical significance (if applicable)

2. Effect sizes or magnitudes of observed relationships

3. Any unexpected or counterintuitive results

4. Robustness of the findings (e.g., sensitivity analyses, alternative specifications)

5. How the findings address the initial research question(s) or hypothesis

6. Any caveats or limitations to the interpretation of the results]


## Key Figures and Tables

[Summarize 2-3 key figures or tables from the paper. For each, provide:

1. A brief description of what the figure/table shows

2. The main takeaway or insight

3. Any limitations or potential improvements

4. How this visual representation enhances understanding of the paper's key points]


## Critical Analysis (300-400 words)

[Provide a comprehensive critical analysis of the paper, including:

1. Strengths of the study (e.g., innovative methodology, robust data)

2. Limitations and potential weaknesses

3. Evaluation of causal claims (if applicable)

4. Discussion of internal and external validity

5. Consideration of alternative explanations for the findings

6. Assessment of the generalizability of the results

7. Evaluation of how well the authors address potential criticisms

8. Your own perspective on the quality and significance of the research]


## Research Gaps and Future Directions

[Identify 2-3 key research gaps or unanswered questions highlighted by the paper. For each:

1. Briefly describe the gap or question

2. Explain why addressing this gap is important for the field

3. Suggest potential approaches or methodologies for addressing the gap

4. Discuss any challenges or limitations that future research might face in this area]


## Implications and Future Research (100-150 words)

[Discuss:

1. Theoretical implications of the findings

2. Practical or policy implications (if applicable)

3. How this research might influence future studies in the field

4. Potential interdisciplinary applications or relevance

5. Any specific suggestions made by the authors for future research

6. Your own ideas for how this research could be extended or applied]


## Code Availability and Reproducibility

[If code is not available with the publication, omit this section. If code is available with the publication:

1. Describe the programming language(s) and key libraries used

2. Outline the main components of the code (e.g., data preprocessing, analysis, visualization)

3. Assess the code's readability and documentation

4. Discuss any notable features or innovative approaches in the code

5. Evaluate the ease of reproducing the paper's results using the provided code

6. Suggest any potential improvements or extensions to the code]


## Equation Formatting

When including equations in your review:

1. Use LaTeX-style math notation enclosed in double dollar signs ($$) for displayed equations.

2. For inline equations, use single dollar signs ($).

3. Use \text{} for non-mathematical text within equations.

4. Use appropriate LaTeX commands for mathematical symbols (e.g., \beta for β, \sum for Σ, \varepsilon for ε).

5. Align multi-line equations using the align environment.

6. Number equations if they are referenced in the text.


Example of a displayed equation:

$$\text{Y}_{i} = \beta_0 + \beta_1 \text{X}_{i} + \varepsilon_{i}$$


Example of an inline equation: The model estimates $\beta_1$ as the effect of X on Y.


For complex equations or multiple related equations, use the align environment:


$$

\begin{align}

\text{Y}_{i} &= \beta_0 + \beta_1 \text{X}_{i} + \varepsilon_{i} \\

\text{E}[\varepsilon_{i}] &= 0

\end{align}

$$


Ensure that all variables are properly defined in the text accompanying the equations.



## Keywords/Tags

[Generate 5-10 relevant, clickable hashtags, considering:

1. Field using the Journal of Economic Literature (JEL) classification system

2. Methodology (e.g., "regression-discontinuity", "difference-in-differences")

3. Key concepts or theoretical frameworks

4. Main themes or topics

5. Study design (e.g., "longitudinal-study", "cross-sectional-analysis")

6. Data type (e.g., "administrative-data", "survey-data")

7. Geographic focus

8. Population of interest

Use hyphenated, lowercase formats for consistency. If the paper exhibits exceptional clarity or presentation, include a tag like "clear-writing" or "excellent-visuals". These should also be designed so they can be clicked on to show all other notes with the same tags in Obsidian.]


## Related Papers

[List 3-5 closely related papers using the format:

- [[Standardized Title Format]]

Include a brief (1-2 sentences) explanation of how each paper relates to the current study]

```

Ensure each section is separated by a blank line for proper rendering in Obsidian. Use appropriate markdown syntax for lists, emphasis, and links. For the Related Papers section, use double square brackets to create potential links to other papers in the Obsidian vault. Standardized Title and File Name Formatting:

Standardized Title (for the main heading):
Use last names of all authors, followed by the year in parentheses.
For two authors, use "&" between names: "LastName1 & LastName2 (Year)"
For three or more authors, use an Oxford comma and "& " before the last name: "LastName1, LastName2, & LastName3 (Year)"
Never use "et al." in titles to ensure consistent linking in Obsidian.
Examples:
One author: "Smith (2023)"
Two authors: "Smith & Jones (2023)"
Three authors: "Smith, Jones, & Lee (2023)"
Four authors: "Smith, Jones, Lee, & Brown (2023)"
Five or more authors: "Smith, Jones, Lee, Brown, & Garcia (2023)"
File Name (for saving PDFs locally):
Format: AuthorLastNames_ShortTitle_Year.pdf
Use camel case for author names and the short title (capitalize first letter of each word, no spaces)
For multiple authors, include all last names
Limit the short title to 3-5 key words
Examples:
One author: "Smith_EffectsOfClimateChange_2023.pdf"
Two authors: "SmithJones_LaborMarketOutcomes_2023.pdf"
Three authors: "SmithJonesLee_HigherEducationAccess_2023.pdf"
Four or more authors: "SmithJonesLeeBrownGarcia_EconomicInequalityTrends_2023.pdf"
Important: 'et al.' should never be used in any paper title throughout the entire note, including references to other papers. Always list all authors' last names in paper titles to ensure consistent linking in Obsidian.

When summarizing papers with advanced econometric methods:

Identify key technical concepts: As you review the paper, identify the main econometric concepts, models, or techniques that may be challenging for applied researchers to understand.
Provide plain language explanations: For each identified concept, provide a brief, clear explanation using everyday language and analogies where possible. Aim to make the concept accessible to someone with basic statistical knowledge but without advanced econometric training.
Integrate explanations: Incorporate these plain language explanations into the relevant sections of the summary, such as the Methodology, Main Findings, and Critical Analysis sections.
Use examples: Where appropriate, use simple examples or scenarios to illustrate how the econometric concepts apply in practice.
Highlight practical implications: Emphasize how the technical aspects of the paper translate into practical insights or applications for applied researchers.
Avoid jargon: When explaining technical concepts, minimize the use of specialized terminology. If technical terms must be used, provide brief definitions.
Connect to intuition: Try to relate the econometric methods to intuitive ideas or common research practices that applied researchers might be familiar with.
Explain limitations: If the econometric methods have important limitations or assumptions, explain these in simple terms and discuss their practical implications.
Visualize if possible: If a concept can be explained more clearly with a simple diagram or analogy, include a brief description of such a visual explanation.
Maintain balance: While providing plain language explanations, ensure that the technical accuracy of the summary is not compromised.
The goal is to make the summary accessible to applied researchers while still conveying the key methodological contributions and findings of the paper.


Additional Instructions:

Ensure consistency in formatting across all papers to maximize the likelihood of correct linking in Obsidian.
When mentioning other papers in the "Related Papers" section, use the exact standardized title format as it would appear in its own note.
If a paper's details are ambiguous or could be formatted in multiple ways, choose the most likely format and note this ambiguity in your analysis.
I encourage you to use bolding or italics in subsections where it makes sense (e.g. “Table 1:” in the key figures and tables list could be bolded) to make the note more readable
Adjust section focus and length as needed. Note unclear parts or low-confidence analyses. Distinguish between descriptive and causal papers, emphasizing causal claim plausibility.
"""

