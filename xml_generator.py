from transformers import GPT2LMHeadModel, GPT2Tokenizer
import os
from bs4 import BeautifulSoup

def generate_xml(prompt, output_folder="output"):
    
    os.makedirs(output_folder, exist_ok=True)

    
    counter_file_path = os.path.join(output_folder, "counter.txt")
    if os.path.exists(counter_file_path):
        with open(counter_file_path, "r") as counter_file:
            generate_xml.count = int(counter_file.read().strip())
    else:
        generate_xml.count = 0

    model_name = "gpt2"
    model = GPT2LMHeadModel.from_pretrained(model_name)
    tokenizer = GPT2Tokenizer.from_pretrained(model_name)

   
    xml_file_path = "/home/lhbolanos/cs166/testprompt.xml"  
    with open(xml_file_path, "r", encoding="utf-8") as xml_file:
        xml_content = xml_file.read()

    input_ids = tokenizer.encode(prompt + xml_content, return_tensors="pt")
    output = model.generate(input_ids, max_length=300, num_return_sequences=1, no_repeat_ngram_size=2)

    generated_text = tokenizer.decode(output[0], skip_special_tokens=True)

    
    exclusion_text = "Generate an element with attribute values to the following XML file.\n\n"
    generated_text = generated_text.replace(exclusion_text, "")
    
    
    
    soup = BeautifulSoup(generated_text, "html.parser")
    xml_content = soup.prettify()

    if not xml_content:
        print("Error: Unable to find XML-like content.")
        return None

    
    generate_xml.count += 1
    output_file_path = os.path.join(output_folder, f"prompt{generate_xml.count}.xml")
    with open(output_file_path, "w", encoding="utf-8") as output_file:
        output_file.write(xml_content)

    
    with open(counter_file_path, "w") as counter_file:
        counter_file.write(str(generate_xml.count))

    return output_file_path

if __name__ == "__main__":
    prompt = "Generate an element with attribute values to the following XML file.\n\n"  
    generated_xml_path = generate_xml(prompt)
    
    if generated_xml_path:
        print(f"Generated XML saved to: {generated_xml_path}")

