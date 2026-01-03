from utils.simple_db_service import map_category_names, init_cookbook, get_recipe_headers
from utils.prompts import cooking_assistant_prompt
from utils.openai_service import OpenAIService

COOKBOOK_CATEGORIES = ['przystawki', 'zupy', 'sałatki', 'dania główne', 'desery', 'ciasta']
COOKBOOK_RECIPE_HEADERS = get_recipe_headers()

if __name__=="__main__":

    # Prepare cookbook_db directories
    categories_mapping = map_category_names(COOKBOOK_CATEGORIES)
    init_cookbook(categories_mapping.values())

    # Loop for assistant interaction
        # Get user message
        # Answer with OpenAIService
            # If related to cookbook, read from cookbook_db
            # If related to new recipe, get it from internet and store in cookbook_db

    openai_service = OpenAIService()

    while user_message := input("Enter your message (or press enter to quit): "):

        cook_ass_prompt_formatted = (cooking_assistant_prompt
                                     .replace("$cookbook_db_categories$", ", ".join(COOKBOOK_CATEGORIES))
                                     .replace("$cookbook_db_categories_mapping$", ", ".join(categories_mapping.values()))
                                     .replace("$json_recipe_headers$", ", ".join(COOKBOOK_RECIPE_HEADERS)))

        response = openai_service.initial_completion(messages=[
            {"role": "system", "content": cook_ass_prompt_formatted},
            {"role": "user", "content": user_message}
            ])
        print("Assistant response:", response.choices[0].message.content)

    pass