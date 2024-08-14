from langchain.prompts import PromptTemplate

EXAMPLE = """<Incidental Finding>
{Incidental_Finding}
</Incidental Finding>

<PFx>
```{{"finding":"{Incidental_Finding}", "ICD10_code":"{ICD10_code}", "PFx":"{PFx}", "PFx_ICD10_code":"{PFx_ICD10_code}"}}```
</PFx>

"""

BASELINE_ZEROSHOT_INSTRUCTION = """<Prompt>
Please generate new <PFx> for the <Incidental Finding>

Output should be formatted as a json with the following attributes/fields: finding, ICD10_code, PFx, PFx_ICD10_code

Additional Instructions:
1. Please follow the style. tone, and grade-level of these PFx as closely as possible based on <Examples>
2. Do not suggest follow-up steps with the doctor.
3. Use the patient friendly explanation sentences to determine a PFx ICD-10 code.
4. Please output PFx in 100 words or more.

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
4. Please output PFx in 100 words or more.

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

baseline_fewshot_prompt = PromptTemplate(
                        input_variables=["examples", "Incidental_Finding"],
                        template = BASELINE_FEWSHOT_INSTRUCTION,
                        )

baseline_fewshot_icd10_labeling_prompt = PromptTemplate(
                        input_variables=["examples", "PFx"],
                        template = BASELINE_FEWSHOT_ICD10_LABELING_INSTRUCTION,
                        )