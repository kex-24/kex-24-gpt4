import os
import sys
import openai
import json

def main(key, model_task, theme):
    openai.api_key = key

    with open(model_task, "r") as file:
        model = file.read()
        file.close()    
    
    # Call openai api to generate question
    # See: https://platform.openai.com/docs/guides/chat/introduction for more information on the call
    
    debug = False
    if debug:
        sys.stdout.write("This is a test\nWith a new line")
    else:
        response = openai.chat.completions.create(
            model="gpt-4-0125-preview",
            messages=[
                {"role": "system", "content": "You are a teacher that wants to help a student by creating a personalized programming task that explores the same core concepts. To help the student relate it will be personalized. Here is the model task:"},
                {"role": "assistant", "content": model},
                {"role": "assistant", "content": "Provide an exercise that imitates and goes through the same programming conepts as the provided model task. However it should instead of the provided theme use the following theme:"},
                {"role": "assistant", "content": theme},
                {"role": "assistant", "content": "Format the exercise in markdown similar to the model task except don't use emojis."},
            ]
        )
        
        print(response.choices[0].message.content)

    # end of function
    
    
if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3])
