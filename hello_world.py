def main():
    aakarsh_info = {
        "name": "Aakarsh Jayakar Darla",
        "title": "Data Analytics Consultant",
        "company": "Ernst & Young",
        "expertise": [
            "data transformations",
            "data extractions",
            "building efficient pipelines"
        ],
        "tools": ["Azure", "Databricks", "Power BI"],
        "goals": "transition into data science by leveraging GenAI and cutting-edge technologies",
        "hobbies": [
            "exploring philosophy",
            "walking",
            "music",
            "audiobooks",
            "fitness",
            "movies"
        ]
    }

    print(f"Hello, World! Meet {aakarsh_info['name']}.")
    print(f"{aakarsh_info['name']} is a {aakarsh_info['title']} at {aakarsh_info['company']}.")
    print(f"Expertise: {', '.join(aakarsh_info['expertise'])}")
    print(f"Tools: {', '.join(aakarsh_info['tools'])}")
    print(f"Goals: {aakarsh_info['goals']}")
    print(f"Hobbies: {', '.join(aakarsh_info['hobbies'])}")

if __name__ == "__main__":
    main()