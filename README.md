# AI-based Input Generation


Pre-trained large language models (LLMs) have recently emerged as a breakthrough technique,
and many researchers have been exploring how LLMs can be applied to software testing for
generating structured data, such as XML files.
For this option, you will use the pre-trained GPT2 as the input generator to generate XML files
and check if the generated files are syntactically valid. Specifically, you will need to:
1. Prepare a valid XML file as the example input for GPT2.
a. Here are some examples for your reference: example 1, example 2.
b. Please generate another valid XML file according to XML syntax rules.
2. Write a program to use libxml2 to parse XML files and to check if they are syntactically
valid.
a. Here are some examples for your reference.
3. Design at least five prompt templates to query the GPT2 model.
a. For example, you can prompt GPT2 in this way: ‘Here is an example XML file.
Please generate another one. <sample-xml>’.
b. You can either provide the example input or not.
4. Prompt GPT2 for XML file generation.
a. Import the Hugging Face checkpoint GPT2.
b. Prompt GPT2 using your designed prompt templates.
c. Collect the response from GPT2 (i.e., generated XML files).
5. Check syntactic validity.
a. Use the program in Step 2 to check the syntactic validity of the generated XML
files and record the results.
6. Compare prompt templates.
a. Which kinds of prompts perform well in generating valid XML files?
b. Which performs badly?
c. Why?
