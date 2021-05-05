import argparse
import json

parser = argparse.ArgumentParser()
json_dict = {}
sub_dict = {}
sub_keys = {}
flat_json_dict = {}
done = False

parser.add_argument("--input_file", "-f", type=str, required=True)
args = parser.parse_args()

def main():
    if(parser != None):
        with open(args.input_file, 'r') as file:
            # print(file.read())
            json_dict = json.load(file)
            file.close

    for key, value in json_dict.items():
        # print(key, value)
        if(isinstance(value, dict)):
            sub_keys = key
            sub_dict[key] = value
        else:
            flat_json_dict[key] = value
            # print(flat_json_dict)

    if(sub_dict != None):
        # print(sub_keys)
        temp = value
        for key, value in temp.items():
            key = sub_keys + "." + key
            flat_json_dict[key] = value
            # print(key,value)
        # print(flat_json_dict)
        done = True
    else:
        done = True

    if(flat_json_dict != None and done):
        with open("output_file", 'w') as file:
            json.dump(flat_json_dict, file)
            file.close

if __name__ == "__main__":
    main()