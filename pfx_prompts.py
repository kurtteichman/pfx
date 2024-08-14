from langchain.prompts import PromptTemplate

EXAMPLE = """<Incidental Finding>
{Incidental_Finding}
</Incidental Finding>

<PFx>
```{{"Incidental_Finding":"{Incidental_Finding}", "ICD10_code":"{ICD10_code}", "PFx":"{PFx}", "PFx_ICD10_code":"{PFx_ICD10_code}"}}```
</PFx>

"""

BASELINE_ZEROSHOT_INSTRUCTION = """<Prompt>
Please generate new <PFx> for the <Incidental Finding>

Output should be formatted as a json with the following attributes/fields: finding, ICD10_code, PFx, PFx_ICD10_code

Additional Instructions:
1. Do not suggest follow-up steps with the doctor.
2. Use the patient friendly explanation sentences to determine a PFx ICD-10 code.
3. Please generate PFx at a {Reading_Level} Flesch-Kincaid reading level.
4. Please output PFx in 100 words or more.

</Prompt>

<Incidental Finding>
{Incidental_Finding}
</Incidental Finding>
"""

#TODO
ZEROSHOT_INSTRUCTION_WITH_REFLEXION_READING_LEVEL = """<Prompt>
Please generate a new <PFx> for the <Incidental Finding>

Output should be formatted as a json with the following attributes/fields: finding, ICD10_code, PFx, PFx_ICD10_code

Additional Instructions:
1. Do not suggest follow-up steps with the doctor.
2. Use the patient friendly explanation sentences to determine a PFx ICD-10 code.
3. Please generate PFx at a {Reading_Level} Flesch-Kincaid reading level.
4. Please output PFx in 100 words or more.

</Prompt>

<Incidental Finding>
{Incidental_Finding}
</Incidental Finding>

<PFx>
    ```{{"Incidental_Finding":"{Incidental_Finding}", "ICD10_code":"{ICD10_code}", "PFx":"{PFx}", "PFx_ICD10_code":"{PFx_ICD10_code}"}}```
</PFx>

The PFx above was at a {_0_reading_level} instead of a {Reading_Level} Flesch-Kincaid reading level. Please try again.

Please generate a new <PFx> for the <Incidental Finding>

Output should be formatted as a json with the following attributes/fields: finding, ICD10_code, PFx, PFx_ICD10_code

Additional Instructions:
1. Please follow the style. tone, and grade-level of these PFx as closely as possible based on <Examples>
2. Do not suggest follow-up steps with the doctor.
3. Use the patient friendly explanation sentences to determine a PFx ICD-10 code.
4. Please generate PFx at a {Reading_Level} Flesch-Kincaid reading level.
5. Please output PFx in 100 words or more.

</Prompt>

<Incidental Finding>
{Incidental_Finding}
</Incidental Finding>
"""

BASELINE_FEWSHOT_INSTRUCTION = """<Prompt>
Using the patient friendly explanations (PFx) in <Examples>, please generate new <PFx> for the <Incidental Finding>

Output should be formatted as a json with the following attributes/fields: finding, ICD10_code, PFx, PFx_ICD10_code

Additional Instructions:
1. Please follow the style. tone, and grade-level of these PFx as closely as possible based on <Examples>
2. Do not suggest follow-up steps with the doctor.
3. Use the patient friendly explanation sentences to determine a PFx ICD-10 code.
4. Please generate PFx at a {Reading_Level} Flesch-Kincaid reading level.
5. Please output PFx in 100 words or more.

</Prompt>

<Examples>
{examples}
</Examples>

<Incidental Finding>
{Incidental_Finding}
</Incidental Finding>
"""

ICD10_EXAMPLE = """<PFx>
{PFx}
</PFx>
<PFx_ICD10_code>
```{{"PFx_ICD10_code":"{PFx_ICD10_code}"}}```
</PFx_ICD10_code>

"""

BASELINE_FEWSHOT_ICD10_LABELING_INSTRUCTION = """<Prompt>
Using the patient friendly explanations (PFx) in <Examples> as well as their associated ICD10 codes <ICD10>, please generate a new <ICD10> for the <PFx> 

Output should be formatted as a json with the following attribute/field: ICD10_code
</Prompt>

<Examples>
{examples}
</Examples>

<PFx>
{PFx}
</PFx>
"""

example = PromptTemplate(
    input_variables=["Incidental_Finding","ICD10_code","PFx","PFx_ICD10_code"],
    template=EXAMPLE
    )

icd10_example = PromptTemplate(
    input_variables=["PFx_ICD10_code","PFx"],
    template=ICD10_EXAMPLE
    )

baseline_zeroshot_prompt = PromptTemplate(
                        input_variables=["Incidental_Finding"],
                        template = BASELINE_ZEROSHOT_INSTRUCTION,
                        )

zeroshot_prompt_reflexion_reading_level_error = PromptTemplate(
                        input_variables=["Incidental_Finding","ICD10_code","PFx","PFx_ICD10_code"],
                        template = ZEROSHOT_INSTRUCTION_WITH_REFLEXION_READING_LEVEL,
                        )

baseline_fewshot_prompt = PromptTemplate(
                        input_variables=["examples", "Incidental_Finding"],
                        template = BASELINE_FEWSHOT_INSTRUCTION,
                        )

baseline_fewshot_icd10_labeling_prompt = PromptTemplate(
                        input_variables=["examples", "PFx"],
                        template = BASELINE_FEWSHOT_ICD10_LABELING_INSTRUCTION,
                        )