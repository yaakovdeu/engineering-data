import os
import json
import requests
import forallpeople as si

def init_units():
    github_raw_url = 'https://raw.githubusercontent.com/yaakovdeu/engineering-data/main/my_unitsYD09042026.json'
    lib_path = os.path.dirname(si.__file__)
    target_path = os.path.join(lib_path, "environments", "my_units.json")

    try:
        response = requests.get(github_raw_url)
        response.raise_for_status()
        
        with open(target_path, 'w', encoding='utf-8') as f:
            json.dump(response.json(), f, indent=4)
            
        si.environment('my_units', top_level=True)
        print("✅ סביבת היחידות נמשכה מ-GitHub והופעלה בהצלחה!")
        
    except Exception as e:
        print(f"❌ תקלה בהפעלת היחידות: {e}")

# הפעלת הפונקציה אוטומטית כשקוראים לקובץ
init_units()
