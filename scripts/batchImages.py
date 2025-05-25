import os
import sys

script_dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(script_dir)

from imageScript import create_card as create_leader_image
from leadersFormatted import leaders

base_path = os.path.dirname(os.path.dirname(__file__))
result_path = os.path.join(base_path, "results")

if not os.path.exists(result_path):
    os.makedirs(result_path)

success_count = 0
error_count = 0

for leader in leaders:
    try:
        name = leader["name"]
        print(f"Creating image for: {name}")
        create_leader_image(leader)  
        success_count += 1 
    except Exception as e:
        print(f"Error generating image for {leader['name']}: {e}")
        error_count += 1  


print(f"\nImage creation complete.")
print(f"Leaders processed successfully: {success_count}")
print(f"Leaders with errors: {error_count}")
